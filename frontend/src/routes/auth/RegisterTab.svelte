<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { registerFormSchema, type RegisterFormSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import { toast } from 'svelte-sonner';

	export let data: SuperValidated<Infer<RegisterFormSchema>>;

	const form = superForm(data, {
		validators: zodClient(registerFormSchema),
		onUpdated: ({ form }) => {
			if (form.valid) {
				toast.success('Please check your email and verify your account');
			}
		}
	});

	const { form: formData, enhance, message } = form;
</script>

<form method="POST" use:enhance action="?/register" class="flex flex-col space-y-1">
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
	</Form.Field>
	<Form.Field {form} name="confirm_password">
		<Form.Control let:attrs>
			<Form.Label>Confirm Password</Form.Label>
			<Input type="password" {...attrs} bind:value={$formData.confirm_password} />
			<Form.FieldErrors />
		</Form.Control>
		<Form.Description >
			You will receive an email to verify your account
		</Form.Description>
	</Form.Field>
	<Form.Button>Sign Up</Form.Button>
</form>
