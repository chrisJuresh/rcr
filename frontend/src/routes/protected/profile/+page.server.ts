import type { PageServerLoad, Actions } from './$types';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { formSchema } from './schema';
import axios from 'axios';

export const load: PageServerLoad = async (event) => {
	const fetchRoles = async () => {
		const response = await axios.get('http://localhost:8000/api/roles/roles');
		return response.data;
	};
	const fetchTrusts = async () => {
		const response = await axios.get('http://localhost:8000/api/trusts/trusts');
		return response.data;
	};
	const fetchUser = async () => {
		const response = await axios.get('http://localhost:8000/api/users/profile', {
			headers: { Authorization: `Bearer ${event.cookies.get('token')}` }
		});
		console.log(response.data);
		return response.data;
	};
	return {
		roles: await fetchRoles(),
		user: await fetchUser(),
		trusts: await fetchTrusts(),
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
			console.log(form.data.trust?.value || null);
			await axios.put(
				'http://localhost:8000/api/users/profile/',
				{
					title: form.data.title || null,
					first_name: form.data.first_name || null,
					last_name: form.data.last_name || null,
					trust: form.data.trust?.value || null,
					roles: form.data.roles?.map((role) => role.value) ?? []
				},
				{
					headers: { Authorization: `Bearer ${event.cookies.get('token')}` }
				}
			);
			return { form };
		} catch {
			// Do nothing
		}
		return {
			form
		};
	}
};
