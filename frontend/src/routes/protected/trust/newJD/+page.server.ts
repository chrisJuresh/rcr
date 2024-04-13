import type { PageServerLoad, Actions } from './$types.js';
import { fail, redirect } from '@sveltejs/kit';
import { superValidate, message, setError, withFiles } from 'sveltekit-superforms';
import { formSchema } from './schema.js';
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
	const fetchUserTrust = async () => {
		const response = await axios.get<components['schemas']['TrustOut']>(
			'http://localhost:8000/api/users/trust',
			{
				headers: { Authorization: `Bearer ${event.cookies.get('token')}` }
			}
		);
		return response.data;
	};
	return {
		user_trust: await fetchUserTrust(),
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

		let success = false;
		let response;

		try {
			response = await axios.post<components['schemas']['JDID']>(
				'http://localhost:8000/api/jds/jd/',
				formData,
				{
					headers: {
						Authorization: `Bearer ${event.cookies.get('token')}`
					}
				}
			);
			success = true;
		} catch (e) {
			return setError(form, 'file', e);
		}

		if (success) {
			redirect(302, `/protected/trust/editJD/${response.data.id}`);
		}
	}
};
