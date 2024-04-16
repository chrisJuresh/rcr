import { getJD, getJDIds, getJDChecklist, putJDChecklist, submitJD } from '$lib/api';
import type { PageServerLoad, Actions } from './$types';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { formSchema } from './schema';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async ({ cookies, params: { id } }) => {
	const token = cookies.get('token');

	return {
		jd_ids: await getJDIds(token),
		jd: await getJD(id, token),
		form: await superValidate(await getJDChecklist(id, token), zod(formSchema), { errors: false })
	};
};

export const actions: Actions = {
	save: async (event) => {
		let form = await superValidate(event, zod(formSchema));
		if (!form.valid) {
			return fail(400, {
				form
			});
		}
		console.log(form.data);
		const token = event.cookies.get('token');
		try {
			await putJDChecklist(event.params.id, form.data, token);
			return { form };
		} catch {
			//
		}
	},
	submit: async (event) => {
		const token = event.cookies.get('token');
		try {
			await submitJD(event.params.id, token);
		} catch {
			//
		}
	}
};
