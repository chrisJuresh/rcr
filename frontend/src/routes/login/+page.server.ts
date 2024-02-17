import type { PageServerLoad, Actions } from './$types';
import { fail, redirect } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms/server';
import { loginFormSchema, registerFormSchema } from './schema';
import axios from 'axios';

export const load: PageServerLoad = async (event) => {
	if (event.cookies.get('cookie')) {
		redirect(302, '/panel');
	}
	return { 
		loginForm: await superValidate(loginFormSchema), 
		registerForm: await superValidate(registerFormSchema) 
	};
};

export const actions: Actions = {
	login: async (event) => {
		return handleFormSubmission({
			event,
			url: '/login/',
			successRedirect: '/panel',
			schema: loginFormSchema
		});
	},

	register: async (event) => {
		return handleFormSubmission({
			event,
			url: '/register/',
			successRedirect: '/profile',
			schema: registerFormSchema
		});
	}
};

async function handleFormSubmission({ event, url, successRedirect, schema }) {
	const form = await superValidate(event, schema);
	if (!form.valid) {
		return fail(400, { form });
	}

	try {
		const response = await axios.post(`http://localhost:8000${url}`, {
			username: form.data.username,
			password: form.data.password
		});
		setAuthCookie(event, response.data.token);
	} catch (error) {
		return fail(401, { form, error: `${url.split('/').pop()} failed` });
	}
	redirect(302, successRedirect);
}

function setAuthCookie(event, token) {
	event.cookies.set('cookie', token, {
		path: '/',
		httpOnly: true,
		secure: true,
		sameSite: 'strict',
		maxAge: 60 * 60 * 24
	});
}
