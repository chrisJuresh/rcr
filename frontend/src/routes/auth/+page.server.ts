import type { PageServerLoad, Actions } from './$types';
import { fail, redirect, error } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { loginFormSchema, registerFormSchema } from './schema';
import { v4 as uuidv4 } from 'uuid';
import axios from 'axios';
import postmark from 'postmark';

export const load: PageServerLoad = async (event) => {
	const token = event.cookies.get('token');
	if (token) {
		await axios
			.post('http://localhost:8000/api/token/verify', {
				token: token
			})
			.then(() => {
				redirect(302, '/protected/profile');
			});
	}

	return {
		loginForm: await superValidate(zod(loginFormSchema)),
		registerForm: await superValidate(zod(registerFormSchema))
	};
};

const sendVerificationEmail = async (email, token) => {
	const verificationUrl = `http://localhost:5173/auth/verify?token=${token}`;
	console.log(verificationUrl);
	//const client = new postmark.ServerClient('cd8d27e7-e383-4d6d-ad5e-daa45fbcd2f5');
	//
	//try {
	//	await client.sendEmail({
	//		From: 'verify@chrisj.uk',
	//		To: email,
	//		Subject: 'Verify your email',
	//		HtmlBody: `<strong>Please verify your email</strong> by clicking <a href="${verificationUrl}">here</a>.`,
	//		TextBody: `Please verify your email by visiting this link: ${verificationUrl}`,
	//		MessageStream: 'outbound'
	//	});
	//} catch (error) {
	//	console.error('Failed to send verification email:', error);
	//	throw error;
	//}
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

		await axios
			.post('http://localhost:8000/api/token/pair', {
				email: form.data.email,
				password: form.data.password
			})
			.then((response) => {
				setTokenCookie(event, response.data.access);
				redirect(302, '/protected/profile');
			})
			.catch((err) => {
				error(400, { message: err.response.data.detail });
			});
	},

	register: async (event) => {
		const form = await superValidate(event, zod(registerFormSchema));
		if (!form.valid) {
			return fail(400, { form });
		}

		const verificationToken = uuidv4();
		await axios
			.post('http://localhost:8000/api/users/register-unauthenticated', {
				email: form.data.email,
				password: form.data.password,
				token: verificationToken
			})
			.then(() => {
				sendVerificationEmail(form.data.email, verificationToken);
			})
			.catch((err) => {
				error(400, { message: err.response.data });
			});
	}
};
