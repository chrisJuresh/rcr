// +page.server.ts
import type { PageServerLoad } from './$types';
import axios from 'axios';

export const load: PageServerLoad = async ({ cookies }) => {
  const token = cookies.get('token');
  if (!token) {
    // Redirect or handle the absence of a token as necessary
    return {};
  }

  const headers = { 'Authorization': `Token ${token}` };

  try {
    const [userResponse, trustsResponse, rolesResponse] = await Promise.all([
      axios.get('http://localhost:8000/profile/', { headers }),
      axios.get('http://localhost:8000/trusts/', { headers }),
      axios.get('http://localhost:8000/roles/', { headers }),
    ]);

    return {
      user: userResponse.data,
      trusts: trustsResponse.data,
      roles: rolesResponse.data,
    };
  } catch (error) {
    console.error(error);
    // Handle errors as necessary, maybe return an error state
    return {};
  }
};