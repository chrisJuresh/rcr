import type { LayoutServerLoad } from './$types';
import { getUserRoles } from '$lib/api';

export const load: LayoutServerLoad = async ({ cookies, url }) => {
	const token = cookies.get('token');
	return {
		user_roles: await getUserRoles(token).catch(() => [])
	};
};
