import type { PageServerLoad, Actions } from './$types';
import { fail } from '@sveltejs/kit';
import { superValidate, setError } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { formSchema } from './schema';
import { putUserProfile, getRoles, getTrusts, getSpecialities, getUserProfile } from '$lib/api';

export const load: PageServerLoad = async ({ cookies }) => {
	const token = cookies.get('token');
	return {
		user: await getUserProfile(token),
		roles: await getRoles(),
		trusts: await getTrusts(),
		specialities: await getSpecialities(),
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
		const token = event.cookies.get('token');
		try {
			await putUserProfile(form.data, token);
			return { form };
		} catch (e) {
			return setError(form, '', e);
		}
	}
};
