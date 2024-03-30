import { z } from 'zod';

export const formSchema = z.object({
	file: z.any(),
	primary_speciality: z.array(z.number()),
	sub_speciality: z.array(z.number())
});

export type FormSchema = typeof formSchema;
