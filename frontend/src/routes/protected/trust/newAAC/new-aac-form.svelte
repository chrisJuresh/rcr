<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Form from '$lib/components/ui/form';
	import { Input, } from '$lib/components/ui/input';
	import { formSchema, type FormSchema } from './schema';
	import {
		type SuperValidated,
		type Infer,
		superForm,
	} from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import * as Select from '$lib/components/ui/select';
	import type { components } from '$lib/types.d.ts';
	import { toast } from 'svelte-sonner';
	import LockClosed from 'svelte-radix/LockClosed.svelte';

	import JDTable from '../../(components)/data-table.svelte';

	export let data: SuperValidated<Infer<FormSchema>>;
	export let user_trust: components['schemas']['TrustOut'];
	export let jds: components['schemas']['JDsO'][];

	const form = superForm(data, {
		validators: zodClient(formSchema),
		onUpdated: ({ form }) => {
			if (form.valid) {
				toast.success('Job Description Saved');
			}
		}
	});

	const { form: formData, enhance } = form;

	$: selectedConsultantType = $formData.consultant_type
		? {
				label: $formData.consultant_type,
				value: $formData.consultant_type
			}
		: undefined;

</script>

{#if user_trust}
	<Card.Root class="neu">
		<Card.Header>
			<Card.Title class="text-2xl font-bold">Create AAC</Card.Title>
			<Card.Description>Please fill in this form and select<br>the JD's relevant to this AAC</Card.Description>
		</Card.Header>
		<Card.Content>
			<form method="POST" use:enhance enctype="multipart/form-data">

				<Form.Field {form} name="trust">
					<Form.Control let:attrs>
						<Form.Label>Trust</Form.Label>
						<div class="flex items-center space-x-2">
							<Input disabled placeholder={user_trust.name} />
							<LockClosed class="text-gray-300" />
						</div>
						<input name={attrs.name} hidden value={user_trust.id} />
					</Form.Control>
					<Form.FieldErrors />
					<Form.Description>Please edit in the profile page if incorrect</Form.Description>
				</Form.Field>

				<Form.Field {form} name="consultant_type">
					<Form.Control let:attrs>
						<Form.Label>Consultant Type</Form.Label>
						<Select.Root
							selected={selectedConsultantType}
							onSelectedChange={(v) => {
								if (v && $formData.consultant_type !== v.value) {
									$formData.consultant_type = v.value;
								}
							}}
						>
							<Select.Trigger {...attrs}>
								<Select.Value placeholder={'Select a Consultant Type'} />
							</Select.Trigger>
							<Select.Content>
								<Select.Item value="Radiology" label="Radiology" />
								<Select.Item value="Oncology" label="Oncology" />
							</Select.Content>
						</Select.Root>
						<input hidden {...attrs} bind:value={$formData.consultant_type} />
					</Form.Control>
					<Form.FieldErrors />
				</Form.Field>

				<Form.Field {form} name="JDs">
					<Form.Control let:attrs>
						<Form.Label>JDs</Form.Label>
							<JDTable jds={jds}/>
						<input hidden {...attrs} bind:value={$formData.JDs} />
					</Form.Control>
					<Form.FieldErrors />
				</Form.Field>
				
				<Form.Button class="w-full">Save</Form.Button>
			</form>
		</Card.Content>
	</Card.Root>
{:else}
	<h1>Your requested Trust does not match any Approved Trusts on your account</h1>
	<p>Please contact us at a@c.uk if you require assistance</p>
{/if}
