import type { PageServerLoad, Actions } from './$types';
import { error, redirect } from '@sveltejs/kit'; // Use `error` instead of `fail` for consistency with SvelteKit naming conventions
import { superValidate } from 'sveltekit-superforms/server';
import { loginFormSchema, registerFormSchema } from './schema';
import axios from 'axios';

export const load: PageServerLoad = async ({ cookies }) => {
	if (cookies.get('cookie')) {
		throw redirect(302, '/panel'); // Use `throw` with `redirect`
	}
	return {
		loginForm: await superValidate(loginFormSchema),
		registerForm: await superValidate(registerFormSchema)
	};
};

export const actions: Actions = {
	login: async (event) => {
		const result = await handleFormSubmission({
			event,
			url: '/login/',
			successRedirect: '/panel',
			schema: loginFormSchema
		});
		if (result) return result; // Only return if there's a result to return
	},

	register: async (event) => {
		const result = await handleFormSubmission({
			event,
			url: '/register/',
			successRedirect: '/profile',
			schema: registerFormSchema
		});
		if (result) return result; // Only return if there's a result to return
	}
};

async function handleFormSubmission({ event, url, successRedirect, schema }) {
    const form = await superValidate(event, schema);
    if (!form.valid) {
        throw error(400, { form }); // Correct usage of SvelteKit's error function
    }
    try {
        const response = await axios.post(`http://localhost:8000${url}`, {
            username: form.data.username,
            password: form.data.password
        });
        setAuthCookie(event, response.data.token);
    } catch (catchError) { // Renamed to avoid naming conflict
        throw error(401, { form, error: `${url.split('/').pop()} failed` }); // Now 'error' refers to SvelteKit's function
    }
        throw redirect(302, successRedirect); // Correctly throw redirect
}

function setAuthCookie(event, token) {
	event.cookies.set('cookie', token, {
		path: '/',
		httpOnly: true,
		secure: process.env.NODE_ENV === 'production', // Only use secure cookies in production
		sameSite: 'strict',
		maxAge: 60 * 60 * 24 // 24 hours
	});
}
