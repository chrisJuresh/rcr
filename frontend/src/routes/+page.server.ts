import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async (event) => {
  const token = event.cookies.get('cookie');
  return {
    token,
  };
};
  