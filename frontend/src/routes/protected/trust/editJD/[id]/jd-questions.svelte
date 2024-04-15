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

	//export let jd_checklist: components['schemas']['JDChecklistOut'];

	export let data: SuperValidated<Infer<FormSchema>>;

	const form = superForm(data, {
		dataType: 'json',
		validators: zodClient(formSchema)
	});

	const { form: formData, enhance } = form;

	console.log($formData.checklist);

	import { writable } from 'svelte/store';

	const isSubmitted = writable(false);

	function handleSubmit() {
		isSubmitted.set(true);
	}
</script>

<Card.Root class="neu w-full">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">JD Review Form</Card.Title>
		<Card.Description>Please fill in the form to continue</Card.Description>
	</Card.Header>
	<Card.Content>
		<form use:enhance method="POST" on:submit|preventDefault={handleSubmit}>
			<Table.Root>
				<Form.Fieldset {form} name="checklist">
					<Table.Header>
						<Table.Row>
							<Table.Head class="w-4/12">Question</Table.Head>
							<Table.Head class="w-1/12 text-center">Present</Table.Head>
							<Table.Head class="w-1/12">Page</Table.Head>
							<Table.Head>Comments</Table.Head>
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
											{#if $isSubmitted}
												<Form.FieldErrors />
											{/if}
										</Form.Control>
									</Form.ElementField>
								</Table.Cell>
								<Table.Cell class="p-1 text-center">
									<Checkbox />
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
										{#if $isSubmitted}
											<Form.FieldErrors />
										{/if}
									</Form.ElementField>
								</Table.Cell>
								<Table.Cell>
									<Form.ElementField {form} name="checklist[{i}].answer.description">
										<Textarea class="min-h-1" />
									</Form.ElementField>
								</Table.Cell>
							</Table.Row>
						{/each}
					</Table.Body>
					<Table.Caption>
						{#if $isSubmitted}
							<Form.FieldErrors />
						{/if}
						<div class="mb-2 mr-2 flex justify-end">
							<Form.Button>Submit</Form.Button>
						</div>
					</Table.Caption>
				</Form.Fieldset>
			</Table.Root>
		</form>
	</Card.Content>
</Card.Root>
