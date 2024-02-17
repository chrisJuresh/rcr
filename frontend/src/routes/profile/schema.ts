import { z } from 'zod';
export const formSchema = z.object({
	title: z.string().min(2, {message:"Please select a title"}).max(4),
  first_name: z.string().min(2).max(50).optional().or(z.literal('')),
  last_name: z.string().min(2).max(50).optional().or(z.literal('')),
});
export type FormSchema = typeof formSchema;
