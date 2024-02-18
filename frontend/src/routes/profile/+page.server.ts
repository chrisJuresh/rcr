import type { PageServerLoad } from './$types';
import { superValidate } from 'sveltekit-superforms/server';
import { formSchema } from './schema';

export const load: PageServerLoad = async (event) => {
	console.log(event.locals.user);
	return {
		user: event.locals.user,
		form: await superValidate(formSchema),
	};
};