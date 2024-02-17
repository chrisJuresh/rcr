// src/routes/logout/+page.server.ts
import { redirect } from '@sveltejs/kit';

  import axios from 'axios';
export const load = async ({ cookies }) => {
 axios.get('http://localhost:8000/logout/')
 
    if (cookies.get('token')) {
        cookies.delete('token', { path: '/' }); 
    }

    throw redirect(302, '/');  
};


