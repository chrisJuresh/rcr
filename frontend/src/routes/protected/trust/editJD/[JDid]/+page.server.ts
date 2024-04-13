import type { PageServerLoad, Actions } from './$types.js';
import axios from 'axios';
import type { components } from '$lib/types.d.ts';

export const load: PageServerLoad = async (event) => {
	const fetchJD = async (jd_id) => {
		const response = await axios.get<components['schemas']['JDOut']>(
			`http://localhost:8000/api/jds/${jd_id}`,
			{
				headers: { Authorization: `Bearer ${event.cookies.get('token')}` }
			}
		);
		console.log(response.data);
		return response.data;
	};
	const fetchJDIDs = async () => {
		const response = await axios.get<components['schemas']['JDIDsOut']>(
			'http://localhost:8000/api/jds/ids',
			{
				headers: { Authorization: `Bearer ${event.cookies.get('token')}` }
			}
		);
		console.log(response.data.ids);
		return response.data.ids;
	};
	const fetchJDChecklist = async (jd_id) => {
		const response = await axios.get<components['schemas']['JDChecklistOut']>(
			`http://localhost:8000/api/jds/${jd_id}/checklist/`,
			{
				headers: { Authorization: `Bearer ${event.cookies.get('token')}` }
			}
		);
		console.log(response.data);
		return response.data;
	};
	return {
		jd_ids: await fetchJDIDs(),
		jd: await fetchJD(event.params.JDid),
		jd_checklist: await fetchJDChecklist(event.params.JDid)
	};
};
