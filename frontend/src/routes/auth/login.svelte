<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { loginFormSchema, type LoginFormSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';

	export let data: SuperValidated<Infer<LoginFormSchema>>;

	const form = superForm(data, {
		validators: zodClient(loginFormSchema)
	});

	const { form: formData, enhance, errors } = form;
</script>

<form method="POST" use:enhance action="?/login" class="flex flex-col space-y-1">
	<Form.Field {form} name="email">
		<Form.Control let:attrs>
			<Form.Label>Email</Form.Label>
			<Input {...attrs} bind:value={$formData.email} />
			<Form.FieldErrors />
		</Form.Control>
	</Form.Field>
	<Form.Field {form} name="password">
		<Form.Control let:attrs>
			<Form.Label>Password</Form.Label>
			<Input type="password" {...attrs} bind:value={$formData.password} />
			<Form.FieldErrors />
		</Form.Control>
		<Form.Description class="text-red-600">
			{#if $errors._errors !== undefined}
				<h1 class="">{$errors._errors}</h1>
			{:else}
				<h1 class="invisible">Placeholder</h1>
			{/if}
		</Form.Description>
	</Form.Field>
	<Form.Button>Log In</Form.Button>
</form>
