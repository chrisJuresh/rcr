<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Table from '$lib/components/ui/table/index.js';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { Label } from '$lib/components/ui/label';
	import { Textarea } from '$lib/components/ui/textarea';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { formSchema, type FormSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import { toast } from 'svelte-sonner';
	import { invalidateAll } from '$app/navigation';

	export let data: SuperValidated<Infer<FormSchema>>;

	const form = superForm(data, {
		resetForm: false,
		dataType: 'json',
		validators: zodClient(formSchema),
		onUpdated: ({ form }) => {
			if (form.valid) {
				toast.success('Form Saved Successfully');
				invalidateAll();
			}
		}
	});

	const { form: formData, enhance } = form;

	$: $formData = $formData;
</script>

<Card.Root class="neu w-full">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">JD Review Form</Card.Title>
		<Card.Description>Please fill in the form to continue</Card.Description>
	</Card.Header>
	<Card.Content>
		<form use:enhance method="POST" action="?/save">
			<Table.Root>
				<Form.Fieldset {form} name="checklist">
					<Table.Header>
						<Table.Row>
							<Table.Head class="w-4/12">Question</Table.Head>
							<Table.Head class=" w-1/12 text-center">Present</Table.Head>
							<Table.Head class="min-w-20">Page</Table.Head>
							<Table.Head class="w-full">Comments</Table.Head>
						</Table.Row>
					</Table.Header>
					<Table.Body>
						{#each $formData.checklist as _, i}
							<Table.Row>
								<Table.Cell>
									<Form.ElementField {form} name="checklist[{i}].question.text">
										<Form.Control let:attrs>
											<Form.Label>{$formData.checklist[i].question.text}</Form.Label>
											{#if $formData.checklist[i].question.required}
												<Label class="text-red-500">*</Label>
											{/if}
											<Form.FieldErrors />
										</Form.Control>
									</Form.ElementField>
								</Table.Cell>
								<Table.Cell class="p-1 text-center">
									<Form.ElementField {form} name="checklist[{i}].answer.present">
										<Form.Control let:attrs>
											<Checkbox {...attrs} bind:checked={$formData.checklist[i].answer.present} />
										</Form.Control>
										<Form.FieldErrors />
									</Form.ElementField>
								</Table.Cell>
								<Table.Cell>
									<Form.ElementField {form} name="checklist[{i}].answer.page_numbers">
										<Form.Control let:attrs>
											<Input
												{...attrs}
												bind:value={$formData.checklist[i].answer.page_numbers}
												type="number"
											/>
										</Form.Control>
										<Form.FieldErrors />
									</Form.ElementField>
								</Table.Cell>
								<Table.Cell>
									<Form.ElementField {form} name="checklist[{i}].answer.description">
										<Form.Control let:attrs>
											<Textarea
												class="min-h-1"
												{...attrs}
												bind:value={$formData.checklist[i].answer.description}
											/>
										</Form.Control>
										<Form.FieldErrors />
									</Form.ElementField>
								</Table.Cell>
							</Table.Row>
						{/each}
					</Table.Body>
					<Table.Caption>
						<Form.FieldErrors />
						<div class="mb-2 mr-2 flex justify-end">
							<Form.Button>Save</Form.Button>
						</div>
					</Table.Caption>
				</Form.Fieldset>
			</Table.Root>
		</form>

		<div class="mb-2 mr-2 flex justify-end">
			<form method="POST" action="?/submit">
				<Form.Button disabled={!$formData.requirements_met}>Submit For Review</Form.Button>
			</form>
		</div>
	</Card.Content>
</Card.Root>
