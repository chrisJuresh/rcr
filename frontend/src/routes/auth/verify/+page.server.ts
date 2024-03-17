import type { PageServerLoad } from './$types';
import axios from 'axios';

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
			const response = await axios.post('http://localhost:8000/api/users/register-authenticate', {
				token: urlToken
			});
			setTokenCookie(event, response.data.access);
		} catch {
			// Do nothing
		}
	}
};
