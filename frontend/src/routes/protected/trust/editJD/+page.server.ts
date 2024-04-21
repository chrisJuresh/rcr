import type { PageServerLoad } from './$types';
import { getJDPanel } from '$lib/api';

export const load: PageServerLoad = async ({ cookies }) => {
	const token = cookies.get('token');
	let jds;
	try {
		jds = await getJDPanel(token, { panel: 'Edit' });
	} catch {
		jds = [];
	}
	return {
		jds: jds
	};
};
