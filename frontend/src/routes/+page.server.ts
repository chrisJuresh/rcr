import type { PageServerLoad, Actions } from "./$types";
import { fail, redirect } from "@sveltejs/kit";
import { superValidate } from "sveltekit-superforms/server";
import { formSchema } from "./schema";
import axios from "axios";

export const load: PageServerLoad = async ({ locals }) => {
  if (locals.user) {
    redirect(302, '/panel');
  }
  return { form: await superValidate(formSchema) };
};

export const actions: Actions = {
  login: async (event) => {
    return handleFormSubmission({
      event,
      url: '/login/',
      successRedirect: '/panel'
    });
  },

  register: async (event) => {
    return handleFormSubmission({
      event,
      url: '/register/',
      successRedirect: '/profile'
    });
  },
};

async function handleFormSubmission({ event, url, successRedirect }) {
  const form = await superValidate(event, formSchema);
  if (!form.valid) {
    return fail(400, { form });
  }

  try {
    const response = await axios.post(`http://localhost:8000${url}`, {
      username: form.data.username,
      password: form.data.password,
    });
    setAuthCookie(event, response.data.token);
  
  } catch (error) {
    return fail(401, { form, error: `${url.split('/').pop()} failed` }); 
  }
    redirect(302, successRedirect);
}

function setAuthCookie(event, token) {
  event.cookies.set('token', token, {
    path: '/',
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    maxAge: 60 * 60 * 24
  });
}