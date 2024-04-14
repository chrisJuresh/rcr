import type { LayoutServerLoad } from './$types';
import { getUserRoles } from '$lib/api';

export const load: LayoutServerLoad = async ({ cookies }) => {
	const token = cookies.get('token');

	return {
		user_roles: await getUserRoles(token).catch(() => [])
	};
};
