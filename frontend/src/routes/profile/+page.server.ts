import type { PageServerLoad } from './$types';
import { superValidate } from 'sveltekit-superforms/server';
import { formSchema } from './schema';

export const load: PageServerLoad = async (event) => {
    return {
        user: event.locals.user,
        form: await superValidate(formSchema),
    };
};

//import type { PageServerLoad } from './$types';
//import { superValidate } from 'sveltekit-superforms/server';
//import { formSchema } from './schema';
//import axios from 'axios';
//
//export const load: PageServerLoad = async (event) => {
//	const token = event.cookies.get('cookie');
//
//	const config = {
//		headers: { Authorization: `Bearer ${token}` }
//	};
//	const response = await axios.put('http://localhost:8000/profile/', {}, config); // Note the empty data object {}
//	
//	const user = response.data;
//	return {
//		user,
//		form: await superValidate(formSchema),
//	};
//};