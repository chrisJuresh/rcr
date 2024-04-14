import { z } from 'zod';

export const formSchema = z.object({
	jd_id: z.number(),
	checklist: z.array(
		z
			.object({
				question: z.object({
					text: z.string(),
					required: z.boolean()
				}),
				answer: z.object({
					id: z.number(),
					present: z.boolean().nullable(),
					page_numbers: z.string().nullable(),
					description: z.string().nullable()
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
