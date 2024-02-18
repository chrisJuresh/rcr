
import type { Handle } from '@sveltejs/kit';
import axios from 'axios';

export const handle: Handle = async ({ event, resolve }) => {
    // Attempt to retrieve the cookie from the request
    const token = event.cookies.get('cookie'); // Change 'cookie' to the actual name of your token cookie
console.log('token',token)
    // If a token exists, set it in the default headers for all Axios requests and attach user data to locals
    if (token) {
        try {
 
    const config = {
        headers: { Authorization: `Bearer ${token}` }
    };
      console.log('config', config)
          // Replace with your API endpoint for validating tokens
            const response = await axios.get('http://localhost:8000/api/users/profile', config);
            console.log('response',response.data)
            // Assuming the response contains user data, attach it to event.locals
            event.locals.user = response.data;
        } catch (error) {
            // If the token is invalid or any error occurs, clear the user from event.locals
            event.locals.user = null;

            // Optionally, clear the cookie if the token is invalid
            event.cookies.delete('cookie', { path: '/' }); // Ensure the cookie name matches what you used above
        }
    } else {
        // If no token is found, clear user data
        event.locals.user = null;
    }

    // Continue to the endpoint or page logic
    return await resolve(event);
};