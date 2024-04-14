import { redirect, type Handle } from '@sveltejs/kit';
import { verifyUser } from '$lib/api';

export const handle: Handle = async ({ event, resolve }) => {
	
	const token = event.cookies.get('token');
	if (event.url.pathname.startsWith('/protected')) {
		try {
			await verifyUser(token);
		} catch {
			redirect(303, '/auth');
		}
	}

	const response = await resolve(event);

	return response;
};
