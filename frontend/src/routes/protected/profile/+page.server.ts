import type { PageServerLoad, Actions } from './$types';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { formSchema } from './schema';
import axios from 'axios';

export const load: PageServerLoad = async (event) => {
	const rolesResponse = await axios.get('http://localhost:8000/api/roles/roles');
	const token = event.cookies.get('token');
	const userResponse = await axios.get('http://localhost:8000/api/users/profile', {
		headers: { Authorization: `Bearer ${token}` }
	});
	event.locals.user = userResponse.data;
	console.log(event.locals.user);
	return {
		roles: rolesResponse.data,
		user: event.locals.user,
		form: await superValidate(zod(formSchema))
	};
};

export const actions: Actions = {
	default: async (event) => {
		const form = await superValidate(event, zod(formSchema));
		if (!form.valid) {
			return fail(400, {
				form
			});
		}
		try {
			console.log(form.data)
			const token = event.cookies.get('token');
			const response = await axios.put(
				'http://localhost:8000/api/users/profile/',
				{
					title: form.data.title || null,
					first_name: form.data.first_name || null,
					last_name: form.data.last_name || null,
					roles: form.data.roles || null
				},
				{
					headers: { Authorization: `Bearer ${token}` }
				}
			);
			event.locals.user = response.data;
		} catch (error) {
			console.log(error);
		}
		return {
			form
		};
	}
};
