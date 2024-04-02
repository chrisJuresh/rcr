import { z } from 'zod';

export const formSchema = z.object({
	file: z
	.instanceof(File, { message: 'Please upload a file.'})
    .refine((f) => f.size < 100_000, 'Max 100 kB upload size.'),
	consultant_type: z.string().min(1, {
		message: 'You must select a consultant type.'
	}),
	primary_specialities: z.array(z.number()).min(1, {
		message: 'At least one primary speciality must be selected.'
	}),
	sub_specialities: z.array(z.number())
});

export type FormSchema = typeof formSchema;
