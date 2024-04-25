import { z } from 'zod';

export const formSchema = z.object({
	rep_id: z.any()
});

export type FormSchema = typeof formSchema;
