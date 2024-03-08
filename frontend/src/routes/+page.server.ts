import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import axios from 'axios';

export const load: PageServerLoad = async (event) => {
	try {
		await axios.post('http://localhost:8000/api/token/verify', {
			token: event.cookies.get('token')
		});
	} catch (error) {
		throw redirect(303, '/login');
	}
	throw redirect(303, '/protected/profile');
};
