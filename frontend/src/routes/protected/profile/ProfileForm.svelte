<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import * as Select from '$lib/components/ui/select';
	import * as Card from '$lib/components/ui/card';
	import { Input } from '$lib/components/ui/input';
	import { formSchema, type FormSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import Approved from './Approved.svelte';

	export let data: SuperValidated<Infer<FormSchema>>;
	export let user;
	export let roles;
	export let trusts;
	console.log(trusts);

	const form = superForm(data, {
		validators: zodClient(formSchema),
		dataType: 'json'
	});

	const { form: formData, enhance } = form;
	$: selectedTitle = $formData.title
		? {
				label: $formData.title,
				value: $formData.title
			}
		: undefined;

	$: selectedTrust = $formData.trust
		? {
				label: $formData.trust.name,
				value: $formData.trust.value
			}
		: null;

	$: selectedRoles = $formData.roles?.map((role) => ({ label: role.name, value: role.value }));

	function getUserRolesAsString(user) {
		return user.roles.map((role) => role.name).join(', ');
	}

</script>

<div class="flex min-h-screen flex-row items-center justify-center">
	<div class=" h-[400px]">
		<div class="flex justify-center">

			
			<div class="w-72">
				<Approved user={user}></Approved>
			</div>

				<Card.Root class="neu w-128">
					<Card.Header>
						<Card.Title>Edit Profile</Card.Title>
						<Card.Description>{user.email}</Card.Description>
					</Card.Header>
					<Card.Content>
						<form method="POST" use:enhance>
							<div class="grid grid-cols-2 gap-6">
								<Form.Field {form} name="title">
									<Form.Control let:attrs>
										<Form.Label>Title</Form.Label>
										<Select.Root
											selected={selectedTitle}
											onSelectedChange={(v) => {
												v && ($formData.title = v.value);
											}}
										>
											<Select.Trigger {...attrs}>
												<Select.Value placeholder={user.title ? user.title : 'Select a title'} />
											</Select.Trigger>
											<Select.Content>
												<Select.Item value="Mr" label="Mr" />
												<Select.Item value="Mrs" label="Mrs" />
												<Select.Item value="Miss" label="Miss" />
												<Select.Item value="Ms" label="Ms" />
												<Select.Item value="Dr" label="Dr" />
												<Select.Item value="Prof" label="Prof" />
												<Select.Item value="Team" label="Team" />
											</Select.Content>
										</Select.Root>
										<input
											hidden
											{...attrs}
											bind:value={$formData.title}
											placeholder={user.title}
										/>
									</Form.Control>
									<Form.FieldErrors />
								</Form.Field>
							</div>

							{#if $formData.title != 'Team'}
								<div class="grid grid-cols-2 gap-6">
									<Form.Field {form} name="first_name">
										<Form.Control let:attrs>
											<Form.Label>First Name</Form.Label>
											<Input
												{...attrs}
												bind:value={$formData.first_name}
												placeholder={user.first_name ? user.first_name : 'First Name'}
											/>
										</Form.Control>
										<Form.FieldErrors />
									</Form.Field>

									<Form.Field {form} name="last_name">
										<Form.Control let:attrs>
											<Form.Label>Last Name</Form.Label>
											<Input
												{...attrs}
												bind:value={$formData.last_name}
												placeholder={user.last_name ? user.last_name : 'Last Name'}
											/>
										</Form.Control>
										<Form.FieldErrors />
									</Form.Field>
								</div>
							{/if}

							<Form.Field {form} name="trust">
								<Form.Control let:attrs>
									<Form.Label>Trust</Form.Label>
									<Select.Root
										bind:selected={selectedTrust}
										onSelectedChange={(s) => {
											if (s) {
												const trust = trusts.find((trust) => trust.id === s.value);
												$formData.trust = {
													value: trust.id,
													name: trust ? trust.name : ''
												};
											} else {
												$formData.trust = null;
											}
										}}
									>
										<input hidden value={selectedTrust} name={attrs.name} />
										<Select.Trigger {...attrs}>
											<Select.Value placeholder={user.trust ? user.trust : 'Select your trust'} />
										</Select.Trigger>
										<Select.Content>
											{#each trusts as trust}
												<Select.Item value={trust.id} label={trust.name} />
											{/each}
										</Select.Content>
									</Select.Root>
								</Form.Control>
								<Form.FieldErrors />
							</Form.Field>

							<Form.Field {form} name="roles">
								<Form.Control let:attrs>
									<Form.Label>Roles</Form.Label>
									<Select.Root
										multiple
										selected={selectedRoles}
										onSelectedChange={(s) => {
											if (s) {
												$formData.roles = s.map((selected) => {
													const role = roles.find((role) => role.id === selected.value);
													return {
														value: selected.value,
														name: role ? role.name : ''
													};
												});
											} else {
												$formData.roles = [];
											}
										}}
									>
										<input name={attrs.name} hidden value={selectedRoles} />
										<Select.Trigger {...attrs}>
											<Select.Value
												placeholder={getUserRolesAsString(user)
													? getUserRolesAsString(user)
													: 'Select your roles'}
											/>
										</Select.Trigger>
										<Select.Content>
											{#each roles as { id, name }}
												<Select.Item value={id} label={name} />
											{/each}
										</Select.Content>
									</Select.Root>
								</Form.Control>
								<Form.Description>You may select multiple roles</Form.Description>
								<Form.FieldErrors />
							</Form.Field>

							<Form.Button>Update</Form.Button>
						</form>
					</Card.Content>
				</Card.Root>

			<div class="w-72"></div>
	
			</div>
	</div>
</div>
