import { z } from 'zod';

export const loginFormSchema = z.object({
	email: z.string().email(),
	password: z.string().min(8).max(50)
});
export type LoginFormSchema = typeof loginFormSchema;

export const registerFormSchema = z
	.object({
		email: z.string().email(),
		password: z.string().min(8).max(50),
		confirm_password: z.string().min(8).max(50)
	})
	.refine((data) => data.password === data.confirm_password, {
		message: 'Passwords do not match',
		path: ['confirm_password']
	});

export type RegisterFormSchema = typeof registerFormSchema;
