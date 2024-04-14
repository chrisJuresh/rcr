import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { verifyUser } from '$lib/api';

export const load: PageServerLoad = async ({ cookies }) => {
	const token = cookies.get('token');
	try {
		await verifyUser(token);
	} catch {
		redirect(303, '/auth');
	}
	redirect(303, '/protected/profile');
};
