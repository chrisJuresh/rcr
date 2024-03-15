import type { PageServerLoad, Actions } from './$types';
import { fail, redirect, error } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { loginFormSchema, registerFormSchema } from './schema';
import { v4 as uuidv4 } from 'uuid';
import axios from 'axios';
import postmark from 'postmark';

export const load: PageServerLoad = async (event) => {
	let loggedIn = false;
	if (event.cookies.get('token')) {
		try {
			await axios.post('http://localhost:8000/api/token/verify', {
				token: event.cookies.get('token')
			});
			loggedIn = true;
		} catch (error) {
			// stay on /login
		} finally {
			if (loggedIn) {
				redirect(302, '/protected/profile');
			}
		}
	}

	return {
		loginForm: await superValidate(zod(loginFormSchema)),
		registerForm: await superValidate(zod(registerFormSchema))
	};
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

const handleUserForm = async (event, schema, url) => {
	const form = await superValidate(event, zod(schema));
	if (!form.valid) {
		return fail(400, { form });
	}
	const response = await axios
		.post(url, {
			validateStatus: () => true,
			email: form.data.email,
			password: form.data.password
		})
		.catch((error) => {
			return error.response;
		});
	setTokenCookie(event, response.data.access);
	if (response.status === 200) {
		redirect(302, '/protected/profile');
	} else {
		console.log(response.data.detail);
		return error(response.status, { message: response.data.detail });
	}
};

const sendVerificationEmail = async (email, token) => {
  const verificationUrl = `http://localhost:5173/login/verify?token=${token}`;

 // Create a new Postmark client
 const client = new postmark.ServerClient("cd8d27e7-e383-4d6d-ad5e-daa45fbcd2f5");

 // Send an email using the Postmark client
 try {
   await client.sendEmail({
     "From": "verify@chrisj.uk",
     "To": email,
     "Subject": "Verify your email",
     "HtmlBody": `<strong>Verify your email</strong> by clicking <a href="${verificationUrl}">here</a>.`,
     "TextBody": `Verify your email by visiting this link: ${verificationUrl}`,
     "MessageStream": "outbound"  // Remove this line if you are not using Postmark's message streams feature.
   });
 } catch (error) {
   console.error("Failed to send verification email:", error);
   throw error; // Re-throw the error for upstream error handling
 }
};

export const actions: Actions = {
	login: async (event) => {
		await handleUserForm(event, loginFormSchema, 'http://localhost:8000/api/token/pair');
	},

	register: async (event) => {

	const form = await superValidate(event, zod(registerFormSchema));
	if (!form.valid) {
		return fail(400, { form });
	}
 
	const verificationToken = uuidv4();
	await axios
		.post( 'http://localhost:8000/api/users/register-unauthenticated', {
			validateStatus: () => true,
			email: form.data.email,
			password: form.data.password,
			token: verificationToken
		})
	
	sendVerificationEmail(form.data.email, verificationToken);
	}
};
