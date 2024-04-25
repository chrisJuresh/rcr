<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { formSchema, type FormSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import * as Select from '$lib/components/ui/select';
	import type { components } from '$lib/types.d.ts';
	import { toast } from 'svelte-sonner';
	import LockClosed from 'svelte-radix/LockClosed.svelte';

	import JDTable from '../../(components)/data-table.svelte';

	import CalendarIcon from 'svelte-radix/Calendar.svelte';
	import {
		CalendarDate,
		DateFormatter,
		type DateValue,
		getLocalTimeZone,
		parseDate,
		today
	} from '@internationalized/date';
	import { browser } from '$app/environment';
	import { page } from '$app/stores';
	import { cn } from '$lib/utils.js';
	import { Button, buttonVariants } from '$lib/components/ui/button/index.js';
	import { Calendar } from '$lib/components/ui/calendar/index.js';
	import * as Popover from '$lib/components/ui/popover/index.js';
	import { Label } from '$lib/components/ui/label/index.js';

	export let data: SuperValidated<Infer<FormSchema>>;
	export let user_trust: components['schemas']['TrustOut'];
	export let jds: components['schemas']['JDPanel']['jds'];

	const form = superForm(data, {
		validators: zodClient(formSchema),
		onUpdated: ({ form }) => {
			if (form.valid) {
				toast.success('AAC Saved');
			}
		}
	});

	const { form: formData, enhance } = form;

	$: selectedConsultantType = $formData.consultant_type
		? {
				label: $formData.consultant_type,
				value: $formData.consultant_type
			}
		: undefined;

	const df = new DateFormatter('en-US', {
		dateStyle: 'long'
	});

	let value: DateValue | undefined;

	$: value = $formData.date ? parseDate($formData.date) : undefined;

	let placeholder: DateValue = today(getLocalTimeZone());

	let jd_ids;

	let consultant_type;

	$: consultant_type = $formData.consultant_type;

	$: $formData.JDs = jd_ids;

	$: serialisedJDs = JSON.stringify($formData.JDs || []);
</script>

{#if user_trust}
	<Card.Root class="neu">
		<Card.Header>
			<Card.Title class="text-2xl font-bold">Create AAC</Card.Title>
			<Card.Description
				>Please fill in this form and select<br />the JD's relevant to this AAC</Card.Description
			>
		</Card.Header>
		<Card.Content>
			<form method="POST" use:enhance enctype="multipart/form-data">
				<div class="flex flex-col gap-2">
					<Form.Field {form} name="trust">
						<Form.Control let:attrs>
							<Form.Label>Trust</Form.Label>
							<div class="flex items-center space-x-2">
								<Input disabled placeholder={user_trust.name} />
								<LockClosed class="text-gray-300" />
							</div>
							<input name={attrs.name} hidden value={user_trust.id} />
						</Form.Control>
						<Form.FieldErrors />
						<Form.Description>Please edit in the profile page if incorrect</Form.Description>
					</Form.Field>

					<Form.Field {form} name="consultant_type">
						<Form.Control let:attrs>
							<Form.Label>Consultant Type</Form.Label>
							<Select.Root
								selected={selectedConsultantType}
								onSelectedChange={(v) => {
									if (v && $formData.consultant_type !== v.value) {
										$formData.consultant_type = v.value;
									}
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
							<input hidden {...attrs} bind:value={$formData.consultant_type} />
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>

					<Label>JDs</Label>
					<Card.Root class="mb-4 mt-2">
						<Card.Content>
							<Form.Field class="-mx-2 -mb-6 mt-4" {form} name="JDs">
								<Form.Control let:attrs>
									<JDTable bind:consultant_type bind:jd_ids {jds} />
									<input type="hidden" {...attrs} bind:value={serialisedJDs} />
								</Form.Control>
								<Form.FieldErrors />
							</Form.Field>
						</Card.Content>
					</Card.Root>
					<Form.Field {form} name="date" class="flex flex-col">
						<Form.Control let:attrs>
							<Form.Label>AAC Panel Date</Form.Label>
							<Popover.Root>
								<Popover.Trigger
									{...attrs}
									class={cn(
										buttonVariants({ variant: 'outline' }),
										'w-[280px] justify-start pl-4 text-left font-normal',
										!value && 'text-muted-foreground'
									)}
								>
									{value ? df.format(value.toDate(getLocalTimeZone())) : 'Pick a date'}
									<CalendarIcon class="ml-auto h-4 w-4 opacity-50" />
								</Popover.Trigger>
								<Popover.Content class="w-auto p-0" side="top">
									<Calendar
										{value}
										bind:placeholder
										calendarLabel="Date of birth"
										initialFocus
										onValueChange={(v) => {
											if (v) {
												$formData.date = v.toString();
											} else {
												$formData.date = '';
											}
										}}
									/>
								</Popover.Content>
							</Popover.Root>
							<Form.Description
								>You will be provided with the representatives most likely to be available at this
								date</Form.Description
							>
							<Form.FieldErrors />
							<input hidden value={$formData.date} name={attrs.name} />
						</Form.Control>
					</Form.Field>
					<Form.Button class="w-full">Save</Form.Button>
				</div>
			</form>
		</Card.Content>
	</Card.Root>
{:else}
	<h1>Your requested Trust does not match any Approved Trusts on your account</h1>
	<p>Please contact us at a@c.uk if you require assistance</p>
{/if}
