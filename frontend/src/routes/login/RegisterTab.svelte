<script lang="ts">
	import * as Form from '$lib/components/ui/form';
  import { Input } from "$lib/components/ui/input";
	import { registerFormSchema, type RegisterFormSchema } from './schema';
  import {
    type SuperValidated,
    type Infer,
    superForm,
  } from "sveltekit-superforms";

  import { zodClient } from "sveltekit-superforms/adapters";

	export let data: SuperValidated<Infer<RegisterFormSchema>>;

    const form = superForm(data, {
    validators: zodClient(registerFormSchema),
  });
 
  const { form: formData, enhance } = form;

</script>


<form method="POST" use:enhance
	action="?/register"
	class="flex flex-col space-y-4"
>
	<Form.Field {form} name="username">
		<Form.Control let:attrs>
			<Form.Label>Email</Form.Label>
			<Input {...attrs} bind:value={$formData.username} />
    <Form.FieldErrors />
		</Form.Control>
	</Form.Field>
	<Form.Field {form} name="password">
		<Form.Control let:attrs>
			<Form.Label>Password</Form.Label>
			<Input {...attrs} bind:value={$formData.password} />
    <Form.FieldErrors />
		</Form.Control>
	</Form.Field>
    
	<Form.Field {form} name="confirm_password">
		<Form.Control let:attrs>
			<Form.Label>Confirm Password</Form.Label>
			<Input {...attrs} bind:value={$formData.confirm_password} />
    <Form.FieldErrors />
		</Form.Control>
	</Form.Field>
	<Form.Button>Submit</Form.Button>
</form>
