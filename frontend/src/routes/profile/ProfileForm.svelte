<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import * as Card from '$lib/components/ui/card';
	import { formSchema } from './schema';
	import type { FormSchema } from './schema';
	import type { SuperValidated } from 'sveltekit-superforms';
	import * as Select from '$lib/components/ui/select';
	
	export let form: SuperValidated<FormSchema>;
	export let user;


	const frameworks = [
		{
			value: 'dr',
			label: 'Dr'
		},
		{
			value: 'mr',
			label: 'Mr'
		},
		{
			value: 'mrs',
			label: 'Mrs'
		},
		{
			value: 'miss',
			label: 'Miss'
		},
		{
			value: 'ms',
			label: 'Ms'
		},
		{
			value: 'mx',
			label: 'Mx'
		}
	];


</script>

<div class="flex min-h-screen items-center justify-center">
	<Card.Root class="w-[400px]">
		<Card.Header>
			<Card.Title>Edit Profile</Card.Title>
			<Card.Description
				>Please ensure your details are correct before submitting JDs or AACs</Card.Description
			>
		</Card.Header>
		<Card.Content>
			<Form.Root
				method="POST"
				{form}
				schema={formSchema}
				let:config
				class="flex flex-col space-y-4"
			>
				<Form.Field {config} name="title">
					<Form.Item>
						<Form.Label>Title</Form.Label>
						<Form.Select>
							<Form.SelectTrigger placeholder="Select a title" />
							<Form.SelectContent>
								{#each frameworks as framework}
									<Select.Item value={framework.value} label={framework.label}
										>{framework.label}</Select.Item
									>
								{/each}
							</Form.SelectContent>
						</Form.Select>
						<Form.Validation />
					</Form.Item>
				</Form.Field>
				<Form.Field {config} name="first_name">
					<Form.Item>
						<Form.Label>First Name</Form.Label>
						<Form.Input type="text" placeholder={user.first_name}/>
						<Form.Validation />
					</Form.Item>
				</Form.Field>
				<Form.Field {config} name="last_name">
					<Form.Item>
						<Form.Label>Last Name</Form.Label>
						<Form.Input type="text" placeholder={user.last_name}/>
						<Form.Validation />
					</Form.Item>
				</Form.Field>
				<Form.Button>Submit</Form.Button>
			</Form.Root>
		</Card.Content>
	</Card.Root>
</div>
