<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import { loginFormSchema, type LoginFormSchema } from './schema';
	import type { SuperValidated } from 'sveltekit-superforms';

	export let form: SuperValidated<LoginFormSchema>;

</script>

<Form.Root
	action="?/login"
	method="POST"
	{form}
	schema={loginFormSchema}
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
	<Form.Button>Submit</Form.Button>
</Form.Root>