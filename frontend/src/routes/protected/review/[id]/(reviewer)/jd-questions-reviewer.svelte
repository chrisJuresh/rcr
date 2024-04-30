<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Table from '$lib/components/ui/table/index.js';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { Label } from '$lib/components/ui/label';
	import { Textarea } from '$lib/components/ui/textarea';
	import * as Form from '$lib/components/ui/form';
	import { formSchema, type FormSchema } from '../schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import { toast } from 'svelte-sonner';
	import { invalidateAll } from '$app/navigation';
	import type { components } from '$lib/types.d.ts';
	import JDApprove from './jd-approve-reviewer.svelte';
	import JDReject from '../jd-reject.svelte';

	export let data: SuperValidated<Infer<FormSchema>>;
	export let jd: components['schemas']['JDOut'];

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

	const { form: formData, enhance, tainted, isTainted } = form;

	$: $formData = $formData;

	$: disabled = jd.status !== 'RCR Approved' && jd.status !== 'Trust Amended';

	$: valid = !disabled && !isTainted($tainted);
</script>

<Card.Root class="neu w-full">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">JD Review Form</Card.Title>

		{#if disabled}
			<Card.Description>Please approve or reject this JD</Card.Description>
		{:else}
			<Card.Description>Please fill in the form to continue</Card.Description>
		{/if}
	</Card.Header>
	<Card.Content>
		<form use:enhance method="POST" action="?/save">
			<Table.Root>
				<Form.Fieldset {form} name="checklist">
					<Table.Header>
						<Table.Row>
							<Table.Head class="w-4/12">Question</Table.Head>
							<Table.Head class=" w-1/12 text-center">Present</Table.Head>
							<Table.Head class="text-center">Page</Table.Head>
							<Table.Head class="w-3/12">Trust Comments</Table.Head>
							<Table.Head class="w-full">RCR Comments</Table.Head>
						</Table.Row>
					</Table.Header>
					<Table.Body>
						{#each $formData.checklist as _, i}
							<Table.Row>
								<Table.Cell>
									{$formData.checklist[i].question.text}
									{#if $formData.checklist[i].question.required}
										<Label class="text-red-500">*</Label>
									{/if}
								</Table.Cell>
								<Table.Cell class="p-1 text-center">
									<Checkbox bind:checked={$formData.checklist[i].answer.present} disabled />
								</Table.Cell>
								<Table.Cell>
									<p class="text-center font-bold">
										{$formData.checklist[i].answer.page_numbers}
									</p>
								</Table.Cell>
								<Table.Cell>
									{$formData.checklist[i].answer.description}
								</Table.Cell>
								<Table.Cell>
									<Form.ElementField {form} name="checklist[{i}].answer.rcr_comments">
										<Form.Control let:attrs>
											<Textarea
												class="min-h-1"
												{...attrs}
												bind:value={$formData.checklist[i].answer.rcr_comments}
											/>
										</Form.Control>
									</Form.ElementField>
								</Table.Cell>
							</Table.Row>
						{/each}
					</Table.Body>
					<Table.Caption>
						<Form.FieldErrors />
						<div class="mb-2 mr-2 flex justify-end gap-2">
							<Form.Button class="text-current" variant="outline" {disabled}>Save</Form.Button>
							<JDApprove {valid} />
							<JDReject {valid} />
						</div>
					</Table.Caption>
				</Form.Fieldset>
			</Table.Root>
		</form>
	</Card.Content>
</Card.Root>
