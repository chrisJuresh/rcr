import type { PageServerLoad, Actions } from './$types';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { formSchema } from './schema';
import axios from 'axios';

export const load: PageServerLoad = async (event) => {
	const token = event.cookies.get('token');
	const response = await axios.get('http://localhost:8000/users/api/profile', {
		headers: { Authorization: `Bearer ${token}` }
	});
	event.locals.user = response.data;
	return {
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
			const token = event.cookies.get('token');
			console.log(token);
const response = await axios.put('http://localhost:8000/users/api/profile/', {
  title: form.data.title,
  first_name: form.data.first_name,
  last_name: form.data.last_name
}, {
  headers: { Authorization: `Bearer ${token}` }
});
			event.locals.user = response.data;
		} catch (error) {
			console.log(error);
		}
		return {
			form
		};
	}
};
