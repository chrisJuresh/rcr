import type { Handle } from "@sveltejs/kit";
import axios from "axios";
import { goto } from '$app/navigation';

export const handle: Handle = async ({ event, resolve }) => {
 
    // Ensure session and session data are properly initialized
const token = event.cookies.get('cookie'); 
  console.log(token); // Check if the cookie was fetched
  if (token) {
    axios.defaults.headers.common['Authorization'] = `Token ${token}`;
    try {
      // Replace with your API endpoint for validating tokens
      const response = await axios.get('http://localhost:8000/validate_token/');
      event.locals.user = response.data;  // Assuming the response contains user data
    } catch (error) {
      // Token validation failed
      event.locals.user = {};
      if (event.locals.session) { // Ensure session exists before attempting to delete data
        event.locals.session.data = {}; // Set to empty object instead of deleting
      }
      goto('/'); // Redirect to login page (if it exists)
      // Optionally redirect to login if validation fails
    }
  }

  return resolve(event);
};