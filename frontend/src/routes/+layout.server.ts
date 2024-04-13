import type { LayoutServerLoad } from './$types';
import axios from 'axios';
import type { components } from '$lib/types.d.ts';

export const load: LayoutServerLoad = async (event) => {
	const response = await axios.get<components['schemas']['RolesOut']>(
		'http://localhost:8000/api/users/roles',
		{
			headers: {
				Authorization: `Bearer ${event.cookies.get('token')}`
			}
		}
	);
	return {
		user_roles: response.data
	};
};
