import type { PageServerLoad } from './$types';
import { getAACPanel } from '$lib/api';

export const load: PageServerLoad = async ({ cookies }) => {
	const token = cookies.get('token');
	let aacs;
	try {
		aacs = await getAACPanel(token);
	} catch {
		aacs = [];
	}
	return {
		aacs: aacs
	};
};
