import type { LayoutServerLoad } from './$types';
import axios from 'axios';

export const load: LayoutServerLoad = async () => {
	
 	const rolesResponse = await axios.get('http://localhost:8000/api/users/roles')

	return {
		roles: rolesResponse.data,
	};
};