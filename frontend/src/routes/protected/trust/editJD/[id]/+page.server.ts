import { getJD, getJDIds, getJDChecklist } from '$lib/api';
import type { PageServerLoad, Actions } from './$types';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { formSchema } from './schema';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async ({ cookies, params: { id } }) => {
	const token = cookies.get('token');

	const response = await getJDChecklist(id, token);
	const checklist = response.checklist;

	return {
		jd_ids: await getJDIds(token),
		jd: await getJD(id, token),
		jd_checklist: await getJDChecklist(id, token),
		form: await superValidate({ checklist }, zod(formSchema))
	};
};

export const actions: Actions = {
	default: async (event) => {
		const form = await superValidate(event, zod(formSchema));
		console.log('form##############');
		console.log(form);
		console.log('form.data##############');
		console.log(form.data);
		console.log('form.data.checklist##############');
		console.log(form.data.checklist);
		console.log('##############');
		if (!form.valid) {
			return fail(400, {
				form
			});
		}
		return {
			form
		};
	}
};
