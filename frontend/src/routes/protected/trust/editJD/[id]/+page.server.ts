import { getJD, getJDIds, getJDChecklist, putJDChecklist, putJDState, putJD } from '$lib/api';
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

		const token = event.cookies.get('token');
		try {
			await putJDChecklist(event.params.id, form.data, token, { panel: 'Edit' });
			return { form };
		} catch {
			//
		}
	},
	submit: async (event) => {
		const token = event.cookies.get('token');
		try {
			await putJDState(event.params.id, 'submit', token);
		} catch {
			//
		}
	},
	upload: async (event) => {
		const token = event.cookies.get('token');
		const form = await event.request.formData();
		const file = form.get('file');

		const formData = new FormData();
		formData.append('file', file);
		try {
		await putJD(event.params.id, formData, token);
		} catch(e) {
			console.log(e)
			//
		}
	}
};
