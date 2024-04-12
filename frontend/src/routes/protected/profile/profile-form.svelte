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

	let oncologySpecialities: components['schemas']['SpecialitiesOut']['specialities'];
	let radiologySpecialities: components['schemas']['SpecialitiesOut']['specialities'];

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

	const splitSpecialities = () => {
		oncologySpecialities = specialities.filter((c) => c.consultant_type === 'ONCOLOGY');
		radiologySpecialities = specialities.filter((c) => c.consultant_type === 'RADIOLOGY');
	};

	splitSpecialities();

	$: hasRole = (roleNames) => {
		const roleArray = [].concat(roleNames);
		if (selectedRoles.length) {
			return selectedRoles.some((role) => roleArray.includes(role.label));
		}
		return user.roles?.some((role) => roleArray.includes(role)) || false;
	};

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

	function rolesPlaceholder() {
		return user.roles && user.roles.length ? user.roles.join(', ') : 'Select your Roles';
	}

	$: consultantTypePlaceholder = () => {
		if (hasRole(['Reviewer', 'Representative'])) {
			return user.consultant_type || 'Select a Consultant Type';
		} else if (hasRole(['RCR Employee', 'Trust Employee'])) {
			return 'Reviewers and Representatives only';
		} else {
			return 'Select a Role first';
		}
	};

	$: consultantTypeMismatch = false;

	$: specialitiesPlaceholder = () => {
		if (!hasRole(['Representative'])) {
			return hasRole(['RCR Employee', 'Trust Employee', 'Reviewer'])
				? 'Representatives only'
				: 'Select a Role first';
		}

		if (!$formData.consultant_type && !user.consultant_type) {
			return 'Select a Consultant Type first';
		}

		if (consultantTypeMismatch) {
			return 'Select your Specialities';
		}

		return user.specialities && user.specialities.length > 0
			? user.specialities.map((speciality) => speciality.name).join(', ')
			: 'Select your Specialities';
	};

	$: trustPlaceholder = () => {
		if (hasRole(['Reviewer', 'Representative', 'Trust Employee'])) {
			return user.trust.name || 'Select your trust';
		} else if (hasRole('RCR Employee')) {
			return 'RCR Employees do not have trusts';
		} else {
			return 'Select a Role first';
		}
	};
</script>

<Card.Root class="neu w-11/12 sm:w-[500px]">
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

			<Card.Header class="px-0">
				<Card.Title class="text-2xl font-bold">Permissions</Card.Title>
				<Card.Description
					>These fields will be used to assign JDs and AACs<br />Role and Trust have no effect
					untill they are approved
				</Card.Description>
			</Card.Header>

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
				<Form.Description>You may select multiple</Form.Description>
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
				<Form.FieldErrors />
			</Form.Field>

			<Form.Field {form} name="consultant_type">
				<Form.Control let:attrs>
					<Form.Label>Consultant Type</Form.Label>
					<Select.Root
						selected={selectedConsultantType}
						onSelectedChange={(v) => {
							if (v && $formData.consultant_type !== v.value) {
								$formData.consultant_type = v.value;
								$formData.specialities = [];
								consultantTypeMismatch = true;
							}
						}}
					>
						<Select.Trigger disabled={!hasRole(['Reviewer', 'Representative'])} {...attrs}>
							<Select.Value placeholder={consultantTypePlaceholder(user)} />
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

			<Form.Field {form} name="specialities">
				<Form.Control let:attrs>
					<Form.Label>Specialities</Form.Label>
					<Select.Root
						multiple
						selected={selectedSpecialities}
						onSelectedChange={(v) => {
							$formData.specialities = v.map((speciality) => speciality.value);
							consultantTypeMismatch = false;
						}}
					>
						{#each $formData.specialities || [] as speciality}
							<input name={attrs.name} hidden value={speciality} />
						{/each}

						<Select.Trigger
							disabled={!hasRole('Representative') ||
								(!$formData.consultant_type && !user.consultant_type)}
							{...attrs}
						>
							<Select.Value placeholder={specialitiesPlaceholder(user)} />
						</Select.Trigger>
						<Select.Content>
							{#if ($formData.consultant_type ? $formData.consultant_type : user.consultant_type) === 'Radiology'}
								{#each radiologySpecialities as { id, name }}
									<Select.Item value={id} label={name} />
								{/each}
							{:else if ($formData.consultant_type ? $formData.consultant_type : user.consultant_type) === 'Oncology'}
								{#each oncologySpecialities as { id, name }}
									<Select.Item value={id} label={name} />
								{/each}
							{/if}
						</Select.Content>
					</Select.Root>
				</Form.Control>
				<Form.Description>You may select multiple</Form.Description>
				<Form.FieldErrors />
			</Form.Field>
			<Form.Button class="w-full">Update</Form.Button>
		</form>
	</Card.Content>
</Card.Root>
