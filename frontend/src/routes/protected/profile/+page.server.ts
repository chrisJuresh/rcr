import type { PageServerLoad, Actions } from "./$types";
import { fail } from "@sveltejs/kit";
import { superValidate } from "sveltekit-superforms";
import { zod } from "sveltekit-superforms/adapters";
import { formSchema } from "./schema";
 
export const load: PageServerLoad = async (event) => {
 console.log('event.locals.user', event.locals.user) 
	return {
	user: event.locals.user,
	form: await superValidate(zod(formSchema)),
  };
};
 
export const actions: Actions = {
  default: async (event) => {
	const form = await superValidate(event, zod(formSchema));
	if (!form.valid) {
	  return fail(400, {
		form,
	  });
	}
	return {
	  form,
	};
  },
};