import { z } from 'zod';

const fileUploadSchema = z.object({
	filename: z.string(),
	mimeType: z.string(),
	size: z.number().min(1) // Minimum file size of 1 byte
});

export type FormSchema = typeof formSchema;
