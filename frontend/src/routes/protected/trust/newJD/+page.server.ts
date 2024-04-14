import type { PageServerLoad, Actions } from './$types.js';
import { fail, redirect } from '@sveltejs/kit';
import { superValidate, setError } from 'sveltekit-superforms';
import { formSchema } from './schema.js';
import { zod } from 'sveltekit-superforms/adapters';
import { getUserTrust, getSpecialities, postJD } from '$lib/api.js';

export const load: PageServerLoad = async ({ cookies }) => {
	const token = cookies.get('token');
	return {
		user_trust: await getUserTrust(token),
		specialities: await getSpecialities(),
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

		const token = event.cookies.get('token');
		try {
			response = await postJD(formData, token);
			success = true;
		} catch (e) {
			return setError(form, 'file', e);
		}

		if (success) {
			redirect(302, `/protected/trust/editJD/${response.id}`);
		}
	}
};
