import type { PageServerLoad, Actions } from './$types';
import { fail, redirect, error } from '@sveltejs/kit'; 
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
	const response = await axios.post(url, {
			validateStatus:() => true,
			email: form.data.email,
			password: form.data.password
		}).catch((error) => {
			return error.response;
		});
	setTokenCookie(event, response.data.access);
	if (response.status === 200) {
		redirect(302, '/protected/profile');
	} else {
		console.log(response.data.detail)
	return error(response.status, { message: response.data.detail});
	}
};

export const actions: Actions = {
	login: async (event) => {
		await handleUserForm(event, loginFormSchema, 'http://localhost:8000/api/token/pair');
	},

	register: async (event) => {
		await handleUserForm(event, registerFormSchema, 'http://localhost:8000/api/users/register');
	}
};