<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { formSchema, type FormSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';

	export let data: SuperValidated<Infer<FormSchema>>;

	const form = superForm(data, {
		validators: zodClient(formSchema)
	});

	const { form: formData, enhance } = form;
</script>

<Card.Root class="neu">
	<Card.Header>
		<Card.Title>Create JD</Card.Title>
		<Card.Description
			>Please fill in the information below and submit your Job Description</Card.Description
		>
	</Card.Header>
	<Card.Content>
		<form method="POST" use:enhance>
			<Form.Field {form} name="file">
				<Form.Control let:attrs>
					<div class="grid w-full max-w-sm items-center gap-1.5">
						<Form.Label>File</Form.Label>
						<Input type="file" {...attrs} bind:value={$formData.file} />
					</div>
				</Form.Control>
				<Form.FieldErrors />
			</Form.Field>

			<Form.Field {form} name="primary_speciality">
				<Form.Control let:attrs>
					<Form.Label>Primary Speciality</Form.Label>
					<Input {...attrs} bind:value={$formData.primary_speciality} />
				</Form.Control>
				<Form.FieldErrors />
			</Form.Field>
			<Form.Button>Submit</Form.Button>
		</form>
	</Card.Content>
</Card.Root>
