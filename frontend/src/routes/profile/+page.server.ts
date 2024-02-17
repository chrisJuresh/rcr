import type { PageServerLoad} from './$types';
import { superValidate } from 'sveltekit-superforms/server';
import { formSchema } from './schema';
import axios from 'axios';

export const load: PageServerLoad = async (event) => {
	const token = event.cookies.get('cookie');
	const response = await axios.put('http://localhost:8000/profile/', { headers: { Authorization: `Bearer ${token}` } });
	const user = response.data;
	return {
		user,
		form: await superValidate(formSchema),
	};
};
  