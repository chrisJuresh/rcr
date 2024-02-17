import { redirect } from '@sveltejs/kit';

import type { PageServerLoad} from './$types';

import axios from 'axios';

export const load: PageServerLoad = async (event) => {
	axios.get('http://localhost:8000/logout/');
	event.cookies.delete('cookie', { path: '/login' });
	console.log(event.cookies.get('cookie'));
	redirect(303, '/login');
};