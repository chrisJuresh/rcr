<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import * as Select from '$lib/components/ui/select';
	import * as Card from '$lib/components/ui/card';
	import { Input } from '$lib/components/ui/input';
	import { formSchema, type FormSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import { toast } from 'svelte-sonner';
	import type { components } from '$lib/types.d.ts';

	export let data: SuperValidated<Infer<FormSchema>>;
	export let user: components['schemas']['UserProfileOut'];
	export let roles: components['schemas']['RolesOut']['roles'];
	export let trusts: components['schemas']['TrustsOut']['trusts'];
	export let specialities: components['schemas']['SpecialitiesOut']['specialities'];

	console.log(specialities);

	const form = superForm(data, {
		validators: zodClient(formSchema),
		dataType: 'json',
		onUpdated: ({ form }) => {
			if (form.valid) {
				toast.success('Profile Updated Successfully');
			}
		}
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
				label: trusts.find((trust) => trust.id === $formData.trust)?.name,
				value: $formData.trust
			}
		: null;

	$: selectedRoles =
		$formData.roles?.map((roleId) => ({
			label: roles.find((role) => role.id === roleId)?.name,
			value: roleId
		})) || [];

	function rolesPlaceholder(user) {
		const str =
			user.roles && user.roles.length > 0
				? user.roles.map((role) => role.name).join(', ')
				: 'Select your roles';

		return str;
	}

	function trustPlaceholder(user) {
		return user.trust && user.trust ? user.trust : 'Select your trust';
	}

	let oncologySpecialities = [];
	let radiologySpecialities = [];

	const splitSpecialities = () => {
		oncologySpecialities = specialities.filter((c) => c.consultant_type.name === 'ONCOLOGY');
		radiologySpecialities = specialities.filter((c) => c.consultant_type.name === 'RADIOLOGY');
	};

	splitSpecialities();

	$: selectedConsultantType = $formData.consultant_type
		? {
				label: $formData.consultant_type,
				value: $formData.consultant_type
			}
		: undefined;

	$: selectedSpecialities =
		$formData.specialities?.map((specialityId) => ({
			label: specialities.find((speciality) => speciality.id === specialityId)?.name,
			value: specialityId
		})) || [];

	$: hasRole = (roleNames) => {
	  const roleArray = [].concat(roleNames);
	  if (selectedRoles.length) {
		return selectedRoles.some(role => roleArray.includes(role.label));
	  }
	  return user.roles?.some(role => roleArray.includes(role.name)) || false;
	};
</script>

<Card.Root class="neu mb-6 w-11/12 sm:w-[500px]">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">Edit Profile</Card.Title>
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
						<input hidden {...attrs} bind:value={$formData.title} placeholder={user.title} />
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

			<Form.Field {form} name="roles">
				<Form.Control let:attrs>
					<Form.Label>Roles</Form.Label>
					<Select.Root
						multiple
						selected={selectedRoles}
						onSelectedChange={(v) => {
							$formData.roles = v.map((role) => role.value);
						}}
					>
						<input name={attrs.name} hidden value={selectedRoles} />
						<Select.Trigger {...attrs}>
							<Select.Value placeholder={rolesPlaceholder(user)} />
						</Select.Trigger>
						<Select.Content>
							{#each roles as { id, name }}
								<Select.Item value={id} label={name} />
							{/each}
						</Select.Content>
					</Select.Root>
				</Form.Control>
				<Form.FieldErrors />
				<Form.Description>You may select multiple roles</Form.Description>
			</Form.Field>

			<Form.Field {form} name="trust">
				<Form.Control let:attrs>
					<Form.Label>Trust</Form.Label>
					<Select.Root
						selected={selectedTrust ? selectedTrust : undefined}
						onSelectedChange={(v) => {
							v && ($formData.trust = v.value);
						}}
					>
						<input hidden value={selectedTrust} name={attrs.name} />
						<Select.Trigger
							disabled={!hasRole(['Reviewer', 'Representative', 'Trust Employee'])}
							{...attrs}
						>
							<Select.Value placeholder={trustPlaceholder(user)} />
						</Select.Trigger>
						<Select.Content>
							{#each trusts as trust}
								<Select.Item value={trust.id} label={trust.name} />
							{/each}
						</Select.Content>
					</Select.Root>
				</Form.Control>
				<Form.Description>You must select a role before you can chose a trust</Form.Description>
				<Form.FieldErrors />
			</Form.Field>

			<Form.Field {form} name="consultant_type">
				<Form.Control let:attrs>
					<Form.Label>Consultant Type</Form.Label>
					<Select.Root
						selected={selectedConsultantType}
						onSelectedChange={(v) => {
							v && ($formData.consultant_type = v.value);
						}}
					>
						<Select.Trigger disabled={!hasRole(['Reviewer', 'Representative'])} {...attrs}>
							<Select.Value placeholder={'Select a Consultant Type'} />
						</Select.Trigger>
						<Select.Content>
							<Select.Item value="Radiology" label="Radiology" />
							<Select.Item value="Oncology" label="Oncology" />
						</Select.Content>
					</Select.Root>
					<input hidden {...attrs} bind:value={$formData.consultant_type} />
				</Form.Control>
				<Form.Description>This option is for Reviewers and Representatives only</Form.Description>
				<Form.FieldErrors />
			</Form.Field>

			<Form.Field {form} name="specialities">
				<Form.Control let:attrs>
					<Form.Label>Specialities</Form.Label>
					<Select.Root
						multiple
						selected={selectedSpecialities}
						onSelectedChange={(v) => {
							$formData.specialities = v.map((speciality) => speciality.value);
						}}
					>
						{#each $formData.specialities || [] as speciality}
							<input name={attrs.name} hidden value={speciality} />
						{/each}

						<Select.Trigger disabled={!hasRole('Representative')} {...attrs}>
							<Select.Value placeholder={'Select your specialities'} />
						</Select.Trigger>
						<Select.Content>
							{#if $formData.consultant_type === 'Radiology'}
								{#each radiologySpecialities as { id, name }}
									<Select.Item value={id} label={name} />
								{/each}
							{:else if $formData.consultant_type === 'Oncology'}
								{#each oncologySpecialities as { id, name }}
									<Select.Item value={id} label={name} />
								{/each}
							{:else}
								<Select.Item value="0" label="Select a Consultant Type First" />
							{/if}
						</Select.Content>
					</Select.Root>
				</Form.Control>
				<Form.Description
					>You may select multiple specialities<br />This option is for Representatives only</Form.Description
				>
				<Form.FieldErrors />
			</Form.Field>

			<Form.Button>Update</Form.Button>
		</form>
	</Card.Content>
</Card.Root>
