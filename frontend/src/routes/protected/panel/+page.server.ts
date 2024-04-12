import type { PageServerLoad } from './$types';
import axios from 'axios';
import type { components } from '$lib/types.d.ts';

export const load: PageServerLoad = async (event) => {
	const fetchJDs = async () => {
		const response = await axios.get<components['schemas']['JDPanel']>(
			'http://localhost:8000/api/jds/jd-panel',
			{
				headers: { Authorization: `Bearer ${event.cookies.get('token')}` }
			}
		);
		console.log(response.data);
		return response.data.jds;
	};
	return {
		jds: await fetchJDs()
	};
};
