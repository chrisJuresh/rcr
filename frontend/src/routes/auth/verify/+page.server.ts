import type { PageServerLoad } from './$types';
import { registerAuthenticateUser } from '$lib/api';

const setTokenCookie = (event, value: string): void => {
	event.cookies.set('token', value, {
		path: '/',
		httpOnly: true,
		sameSite: 'Strict',
		secure: process.env.NODE_ENV === 'production',
		maxAge: 60 * 60 * 24 * 7 // 1 week
	});
};

export const load: PageServerLoad = async (event) => {
	const urlToken = event.url.searchParams.get('token');
	if (urlToken) {
		try {
			const response = await registerAuthenticateUser({
				token: urlToken
			});
			setTokenCookie(event, response.access);
		} catch {
			// Do nothing
		}
	}
};
