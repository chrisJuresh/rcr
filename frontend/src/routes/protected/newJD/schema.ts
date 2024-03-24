import { z } from 'zod';

export const formSchema = z.object({
	file: z
		.instanceof(File, { message: 'Please upload a file.' })
		.refine((f) => f.size < 1000_000_000, 'Max 1GB upload size.'),
	primary_speciality: z.string(),
	size: z.number().min(1)
});

export type FormSchema = typeof formSchema;
