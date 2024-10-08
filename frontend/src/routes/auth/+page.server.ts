import type { PageServerLoad, Actions } from './$types';
import { fail, redirect } from '@sveltejs/kit';
import { superValidate, setError } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { loginFormSchema, registerFormSchema } from './schema';
import { v4 as uuidv4 } from 'uuid';
import postmark from 'postmark';
import { verifyUser, loginUser, registerUnauthenticatedUser } from '$lib/api';

export const load: PageServerLoad = async ({ cookies, url }) => {
	const token = cookies.get('token');
	let success = false;
	if (token) {
		try {
			await verifyUser(token);
			success = true;
		} catch {
			// Stay on auth page
		}
	}

	if (success) {
		redirect(302, '/protected/profile');
	}

	return {
		loginForm: await superValidate(zod(loginFormSchema)),
		registerForm: await superValidate(zod(registerFormSchema))
	};
};

const sendVerificationEmail = async (email, token, url) => {
	const verificationUrl = `${url.origin}/auth/verify?token=${token}`;
	const client = new postmark.ServerClient('cd8d27e7-e383-4d6d-ad5e-daa45fbcd2f5');
	console.log(verificationUrl);

	try {
		await client.sendEmail({
			From: 'verify@chrisj.uk',
			To: email,
			Subject: 'Verify your email',
			HtmlBody: `<strong>Please verify your email</strong> by clicking <a href="${verificationUrl}">here</a>.`,
			TextBody: `Please verify your email by visiting this link: ${verificationUrl}`,
			MessageStream: 'outbound'
		});
	} catch (error) {
		console.error('Failed to send verification email:', error);
		throw error;
	}
};

const setTokenCookie = (event, value) => {
	event.cookies.set('token', value, {
		path: '/',
		httpOnly: true,
		sameSite: 'Strict',
		secure: process.env.NODE_ENV === 'production',
		maxAge: 60 * 60 * 24 * 7 // 1 week
	});
};

export const actions: Actions = {
	login: async (event) => {
		const form = await superValidate(event, zod(loginFormSchema));
		if (!form.valid) {
			return fail(400, { form });
		}

		let success = false;
		try {
			const response = await loginUser(form.data);
			setTokenCookie(event, response.access);
			success = true;
		} catch (e) {
			return setError(form, '', e.response.data.detail);
		}

		if (success) {
			redirect(302, '/protected/profile');
		}
	},

	register: async (event) => {
		const form = await superValidate(event, zod(registerFormSchema));
		if (!form.valid) {
			return fail(400, { form });
		}

		const verificationToken = uuidv4();
		try {
			await registerUnauthenticatedUser({
				email: form.data.email,
				password: form.data.password,
				token: verificationToken
			});
			sendVerificationEmail(form.data.email, verificationToken, event.url);
			return { form };
		} catch (e) {
			return setError(form, 'email', e.response.data.detail);
		}
	}
};
