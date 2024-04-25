import type { PageServerLoad } from './$types';
import { getJDPanel, getAACPanel } from '$lib/api';

export const load: PageServerLoad = async ({ cookies }) => {
	const token = cookies.get('token');
	return {
		jds: await getJDPanel(token, { panel: 'Panel' }),
		aacs: await getAACPanel(token)
	};
};
