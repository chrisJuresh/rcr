import type { PageServerLoad, Actions } from './$types.js';
import { fail, redirect } from '@sveltejs/kit';
import { superValidate, setError } from 'sveltekit-superforms';
import { formSchema } from './schema.js';
import { zod } from 'sveltekit-superforms/adapters';
import { getUserTrust, getJDPanel, postAAC } from '$lib/api.js';

export const load: PageServerLoad = async ({ cookies }) => {
	const token = cookies.get('token');
	return {
		jds: await getJDPanel(token, { panel: 'AAC' }),
		user_trust: await getUserTrust(token),
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
			await postAAC(form.data, token);
			return { form };
		} catch {
			//
		}
	}
};
