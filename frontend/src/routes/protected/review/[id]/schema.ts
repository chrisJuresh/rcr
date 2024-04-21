import { z } from 'zod';

export const formSchema = z.object({
	jd_id: z.number(),
	requirements_met: z.boolean(),
	submit: z.boolean().optional(),
	checklist: z.array(
		z
			.object({
				question: z.object({
					id: z.number(),
					text: z.string(),
					required: z.boolean()
				}),
				answer: z.object({
					id: z.number(),
					present: z.boolean().optional(),
					page_numbers: z.string().nullable(),
					description: z.string().nullable(),
					rcr_comments: z.string().nullable(),
					rsa_comments: z.string().nullable()
				})
			})
			.refine(
				(item) => {
					if (item.question.required) {
						return item.answer.page_numbers != '';
					}
					return true;
				},
				{
					message: 'required',
					path: ['answer', 'page_numbers']
				}
			)
	)
});

export type FormSchema = typeof formSchema;
