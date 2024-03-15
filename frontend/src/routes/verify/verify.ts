import type { RequestHandler } from '@sveltejs/kit';
import { error, redirect } from '@sveltejs/kit';
import { verifyTokenAndGetEmail, handleUserForm, registerFormSchema } from '../login/+page.server'; // Adjust the import paths as necessary

export const get: RequestHandler = async ({ url }) => {
    const token = url.searchParams.get('token');
    if (!token) {
        // No token was provided
        return error(400, 'Invalid verification link');
    }

    const email = verifyTokenAndGetEmail(token);
    if (!email) {
        // The token was invalid or expired
        return error(400, 'Invalid or expired token');
    }

    // Here, instead of directly calling `handleUserForm`, you might need to finalize the registration
    // process since `handleUserForm` seems designed for form submission.
    // You should replace the below with whatever finalization logic is appropriate,
    // such as creating the user record, sending a confirmation email, etc.
    // I've put a redirect here for the sake of example:

    // Redirect to a confirmation page or login page after successful verification
    throw redirect(303, '/confirmation'); // Adjust the redirect location as necessary
};