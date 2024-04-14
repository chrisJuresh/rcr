import { getJD, getJDIds, getJDChecklist } from '$lib/api';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ cookies, params: { id } }) => {
	const token = cookies.get('token');

	return {
		jd_ids: await getJDIds(token),
		jd: await getJD(id, token),
		jd_checklist: await getJDChecklist(id, token)
	};
};
