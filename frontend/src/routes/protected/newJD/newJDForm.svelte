<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { formSchema, type FormSchema } from './schema';
	import { type SuperValidated, type Infer, superForm, fileProxy } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import * as Select from '$lib/components/ui/select';
	import type {components } from '$lib/types.d.ts';

	export let data: SuperValidated<Infer<FormSchema>>;
	export let specialities: components['schemas']['SpecialitiesOut']['specialities'];
  
		console.log(data)

	let oncologySpecialities = [];
	let radiologySpecialities = [];

  const splitSpecialities = () => {
    oncologySpecialities = specialities.filter(c => c.consultant_type.name === 'ONCOLOGY');
    radiologySpecialities = specialities.filter(c => c.consultant_type.name === 'RADIOLOGY');
  };

  splitSpecialities();

	const form = superForm(data, {
		validators: zodClient(formSchema)
	});

	const { form: formData, enhance } = form;

	$: selectedConsultantType = $formData.consultant_type
		? {
				label: $formData.consultant_type,
				value: $formData.consultant_type
			}
		: undefined;
	
	$: selectedPrimarySpecialities = 
	$formData.primary_specialities?.map((specialityId) => ({ 
		label: specialities.find((speciality) => speciality.id === specialityId)?.name, 
		value: specialityId 
	})) || [];

	$: selectedSubSpecialities = 
	$formData.sub_specialities?.map((specialityId) => ({ 
		label: specialities.find((speciality) => speciality.id === specialityId)?.name, 
		value: specialityId 
	})) || [];

</script>

<Card.Root class="neu">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">Create JD</Card.Title>
		<Card.Description
			>Please fill in the information below and submit your Job Description</Card.Description
		>
	</Card.Header>
	<Card.Content>
		<form method="POST" use:enhance enctype="multipart/form-data">
			<Form.Field {form} name="file">
				<Form.Control let:attrs>
					<div class="grid w-full max-w-sm items-center gap-1.5">
						<Form.Label>Job Description File</Form.Label>
						<Input type="file" {...attrs} bind:value={$formData.file} />
					</div>
				</Form.Control>
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
							<Select.Trigger {...attrs}>
								<Select.Value placeholder={'Select a Consultant Type'} />
							</Select.Trigger>
							<Select.Content>
								<Select.Item value="Radiology" label="Radiology" />
								<Select.Item value="Oncology" label="Oncology" />
							</Select.Content>
						</Select.Root>
						<input hidden {...attrs} bind:value={$formData.consultant_type}/>
					</Form.Control>
					<Form.FieldErrors />
				</Form.Field>
			
			<Form.Field {form} name="primary_specialities">
				<Form.Control let:attrs>
					<Form.Label>Roles</Form.Label>
					<Select.Root
						multiple
						selected={selectedPrimarySpecialities}
						onSelectedChange={(v) => {
								$formData.primary_specialities = v.map((speciality) => speciality.value);
						}}
					>
				{#each $formData.primary_specialities as speciality}
						<input name={attrs.name} hidden value={speciality} />
				{/each}
						<Select.Trigger {...attrs}>
							<Select.Value placeholder={"Select a speciality"} />
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
				<Form.FieldErrors />
				<Form.Description>You may select multiple primary specialities</Form.Description>
			</Form.Field>

			<Form.Field {form} name="sub_specialities">
				<Form.Control let:attrs>
					<Form.Label>Roles</Form.Label>
					<Select.Root
						multiple
						selected={selectedSubSpecialities}
						onSelectedChange={(v) => {
								$formData.sub_specialities = v.map((speciality) => speciality.value);
						}}
					>
				{#each $formData.sub_specialities as speciality}
						<input name={attrs.name} hidden value={speciality} />
				{/each}
						<Select.Trigger {...attrs}>
							<Select.Value placeholder={"Select a speciality"} />
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
				<Form.Description>You may select multiple sub specialities</Form.Description>
				<Form.FieldErrors />
			</Form.Field>

			
			<Form.Button>Submit</Form.Button>
		</form>
	</Card.Content>
</Card.Root>
