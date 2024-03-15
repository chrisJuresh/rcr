import type { PageServerLoad} from './$types';
import {redirect, error} from '@sveltejs/kit';
import axios from 'axios';

export const load: PageServerLoad = async (event) => {
	let loggedIn = false;
	if (event.cookies.get('token')) {
		try {
			await axios.post('http://localhost:8000/api/token/verify', {
				token: event.cookies.get('token')
			});
			loggedIn = true;
		} catch (error) {
			// stay on /login
		} finally {
			if (loggedIn) {
				redirect(302, '/protected/profile');
			}
		}
	}


const setTokenCookie = (event, value) => {
	event.cookies.set('token', value, {
		path: '/',
		httpOnly: true,
		sameSite: 'Strict',
		secure: process.env.NODE_ENV === 'production',
		maxAge: 60 * 60 * 24 * 7 // 1 week
	});
};
    
	const token = event.url.searchParams.get('token');
	if (token) {
			const response = await axios.post('http://localhost:8000/api/users/register-validate', {
                token: token
            })
		.catch((error) => {
			return error.response;
		});
	setTokenCookie(event, response.data.access);
	if (response.status === 200) {
		redirect(302, '/protected/profile');
	} else {
		console.log(response.data.detail);
		return error(response.status, { message: response.data.detail });
	}
}
};
