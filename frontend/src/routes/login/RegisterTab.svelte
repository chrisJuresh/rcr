<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import { registerFormSchema, type RegisterFormSchema } from './schema';
	import type { SuperValidated } from 'sveltekit-superforms';

	export let form: SuperValidated<RegisterFormSchema>;
</script>

<Form.Root
	action="?/register"
	method="POST"
	{form}
	schema={registerFormSchema}
	let:config
	class="flex flex-col space-y-4"
>
	<Form.Field {config} name="username">
		<Form.Item>
			<Form.Label>Email</Form.Label>
			<Form.Input type="text" />
			<Form.Validation />
		</Form.Item>
	</Form.Field>
	<Form.Field {config} name="password">
		<Form.Item>
			<Form.Label>Password</Form.Label>
			<Form.Input type="password" />
			<Form.Validation />
		</Form.Item>
	</Form.Field>
	<Form.Field {config} name="confirm_password">
		<Form.Item>
			<Form.Label>Confirm Password</Form.Label>
			<Form.Input type="password" />
			<Form.Validation />
		</Form.Item>
	</Form.Field>
	<Form.Button>Submit</Form.Button>
</Form.Root>