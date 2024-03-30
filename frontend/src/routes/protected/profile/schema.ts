import { z } from 'zod';

export const formSchema = z.object({
  title: z.string().min(2).max(4).nullable().optional(),
  first_name: z.string().min(2).max(50).nullable().optional(),
  last_name: z.string().min(2).max(50).nullable().optional(),
  trust: z.number().nullable().optional(),
  roles: z.array(z.number()).nullable().optional()
});

export type FormSchema = typeof formSchema;