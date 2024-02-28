import { redirect, type Handle } from '@sveltejs/kit';
import axios from 'axios';

export const handle: Handle = async ({ event, resolve }) => {
    console.log(event.cookies.get('token'))

    if(event.url.pathname.startsWith('/protected')){
        try{ const response = await axios.post('http://localhost:8000/users/api/token/verify', {  
        token:event.cookies.get('token')
        });
        console.log(response)
    } catch (error) {
            throw redirect(303, '/login')
        }
    }

    const response = await resolve(event);

    return response
}