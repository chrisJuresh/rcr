import { z } from 'zod';

export const formSchema = z.object({
	trust: z.number(),
	consultant_type: z.string().min(1, {
		message: 'You must select a consultant type.'
	}),
	JDs: z.any(),
	date: z.string().refine((v) => v, { message: 'A date is required.' })
});

export type FormSchema = typeof formSchema;
