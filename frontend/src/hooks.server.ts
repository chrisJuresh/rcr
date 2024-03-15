import { redirect, type Handle } from '@sveltejs/kit';
import axios from 'axios';

export const handle: Handle = async ({ event, resolve }) => {
	if (event.url.pathname.startsWith('/protected')) {
		try {
			await axios.post('http://localhost:8000/api/token/verify', {
				token: event.cookies.get('token')
			});
		} catch (error) {
			throw redirect(303, '/auth');
		}
	}

	const response = await resolve(event);

	return response;
};
