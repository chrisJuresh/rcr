import type { PageServerLoad, Actions } from './$types';
import { fail } from '@sveltejs/kit';
import { superValidate, setError } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { formSchema } from './schema';
import axios from 'axios';
import type { components } from '$lib/types.d.ts';

export const load: PageServerLoad = async (event) => {
	const fetchRoles = async () => {
		const response = await axios.get<components['schemas']['RolesOut']>(
			'http://localhost:8000/api/roles/roles'
		);
		return response.data.roles;
	};
	const fetchTrusts = async () => {
		const response = await axios.get<components['schemas']['TrustsOut']>(
			'http://localhost:8000/api/trusts/trusts'
		);
		return response.data.trusts;
	};
	const fetchUser = async () => {
		const response = await axios.get<components['schemas']['UserProfileOut']>(
			'http://localhost:8000/api/users/profile',
			{
				headers: { Authorization: `Bearer ${event.cookies.get('token')}` }
			}
		);
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
			await axios.put(
				'http://localhost:8000/api/users/profile/',
				{
					title: form.data.title || null,
					first_name: form.data.first_name || null,
					last_name: form.data.last_name || null,
					trust: form.data.trust || null,
					roles: form.data.roles?.map((role) => role.value) ?? []
				},
				{
					headers: { Authorization: `Bearer ${event.cookies.get('token')}` }
				}
			);
			return { form };
		} catch (e) {
			return setError(form, '', e);
		}
	}
};
