import { z } from 'zod';

export const formSchema = z.object({
	file: z.any(),
	consultant_type: z.string().min(1, {
		message: 'You must select a consultant type.'
	}),
	primary_specialities: z.array(z.number()).min(1, {
		message: 'At least one primary speciality must be selected.'
	}),
	sub_specialities: z.array(z.number())
});

export type FormSchema = typeof formSchema;
