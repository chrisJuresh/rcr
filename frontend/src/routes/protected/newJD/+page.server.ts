import type { PageServerLoad, Actions } from './$types.js';
import { fail } from '@sveltejs/kit';
import { superValidate, message, setError, withFiles } from 'sveltekit-superforms';
import { formSchema } from './schema';
import { zod } from 'sveltekit-superforms/adapters';
import axios from 'axios';
import type { components } from '$lib/types.d.ts';

export const load: PageServerLoad = async (event) => {
	const fetchSpecialities = async () => {
		const response = await axios.get<components['schemas']['SpecialitiesOut']>(
			'http://localhost:8000/api/specialities/specialities'
		);
		return response.data.specialities;
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
		user: await fetchUser(),
		specialities: await fetchSpecialities(),
		form: await superValidate(zod(formSchema))
	};
};

export const actions: Actions = {
	default: async (event) => {
		const form = await superValidate(event, zod(formSchema));
		console.log(form);
		if (!form.valid) return fail(400, { form });

		const jdData = JSON.stringify({
			consultant_type: form.data.consultant_type.toUpperCase(),
			primary_specialities: form.data.primary_specialities,
			sub_specialities: form.data.sub_specialities
		});

		const formData = new FormData();

		formData.append('jd', jdData);
		formData.append('file', form.data.file);

		console.log(formData);

		try {
			await axios.post('http://localhost:8000/api/jds/jd/', formData, {
				headers: {
					Authorization: `Bearer ${event.cookies.get('token')}`
				}
			});
			return { form: withFiles(form) }; // this parses the superform object to a serializable object
		} catch (e) {
			return setError(form, 'file', e);
		}
	}
};
