import { z } from 'zod';

export const formSchema = z.object({
	trust: z.any(),
	consultant_type: z.string().min(1, {
		message: 'You must select a consultant type.'
	}),
	JDs: z.number().array().min(1),
});

export type FormSchema = typeof formSchema;
