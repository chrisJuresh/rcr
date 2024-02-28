import type { PageServerLoad, Actions } from './$types';
import { fail, redirect } from '@sveltejs/kit'; 
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { loginFormSchema, registerFormSchema } from './schema';
import axios from 'axios';

export const load: PageServerLoad = async () => {
	return {
		loginForm: await superValidate(zod(loginFormSchema)),
		registerForm: await superValidate(zod(registerFormSchema))
	};
};

const setTokenCookie = (event, value) => {
	event.cookies.set('token', value, {
		path: '/',
		httpOnly: true,
		sameSite: 'strict',
		secure: process.env.NODE_ENV === 'production',
		maxAge: 60 * 60 * 24 * 7 // 1 week
	});
};

const handleUserForm = async (event, schema, url) => {
	const form = await superValidate(event, zod(schema));
	if (!form.valid) {
		return fail(400, { form });
	}
	try {
		const response = await axios.post(url, {
			email: form.data.email,
			password: form.data.password
		});
		setTokenCookie(event, response.data.access);
	} catch (error) {
		console.error(error);
	}
	throw redirect(302, '/protected/profile');
};

export const actions: Actions = {
	login: async (event) => {
		await handleUserForm(event, loginFormSchema, 'http://localhost:8000/users/api/token/pair');
	},

	register: async (event) => {
		await handleUserForm(event, registerFormSchema, 'http://localhost:8000/users/api/register');
	}
};
