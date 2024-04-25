import { getAAC, getAACIds, getReps, putAACRep } from '$lib/api';
import type { PageServerLoad, Actions } from './$types';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { formSchema } from './schema';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async ({ cookies, params: { id } }) => {
	const token = cookies.get('token');
	console.log(await getReps(id, token));
	return {
		aac_ids: await getAACIds(token),
		aac: await getAAC(id, token),
		reps: await getReps(id, token),
		form: await superValidate(zod(formSchema))
	};
};

export const actions: Actions = {
	default: async (event) => {
		let form = await superValidate(event, zod(formSchema));
		if (!form.valid) {
			return fail(400, {
				form
			});
		}

		console.log(form.data);

		const token = event.cookies.get('token');
		try {
			await putAACRep(event.params.id, JSON.parse(form.data.rep_id)[0], token);
			return { form };
		} catch {
			//
		}
	}
};
