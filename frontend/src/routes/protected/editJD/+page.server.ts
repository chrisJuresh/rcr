import type { PageServerLoad, Actions } from './$types.js';
import axios from 'axios';
import type { components } from '$lib/types.d.ts';

export const load: PageServerLoad = async (event) => {
	const fetchJDIDs = async () => {
		const response = await axios.get<components['schemas']['JDIDsOut']>(
			'http://localhost:8000/api/jds/jd-ids',
			{
				headers: { Authorization: `Bearer ${event.cookies.get('token')}` }
			}
		);
		return response.data.ids;
	};
	return {
		jd_ids: await fetchJDIDs()
	};
};

export const actions: Actions = {
	default: async (event) => {
		return;
	}
};
