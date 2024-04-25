<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import * as Select from '$lib/components/ui/select';
	import type { components } from '$lib/types.d.ts';
	import { toast } from 'svelte-sonner';
	import LockClosed from 'svelte-radix/LockClosed.svelte';

	import RepTable from '../../../(components)/data-table.svelte';

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
	import { formSchema, type FormSchema } from './schema';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';

	export let data: SuperValidated<Infer<FormSchema>>;

	export let reps: components['schemas']['JDPanel']['jds'];

	const form = superForm(data, {
		validators: zodClient(formSchema),
		onUpdated: ({ form }) => {
			if (form.valid) {
				toast.success('Rep saved!');
			}
		}
	});

	const { form: formData, enhance } = form;

	let rep_ids;

	// $: jd_ids,
	//
	$: $formData.rep_id = rep_ids;
	//
	$: serialisedRepID = JSON.stringify($formData.rep_id || []);
</script>

<Card.Root class="neu">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">Select a Rep</Card.Title>
		<Card.Description
			>Please feel free to contact any of the representatives on this list<br />and submit their row
			if they agree.</Card.Description
		>
	</Card.Header>
	<Card.Content>
		<form method="POST" enctype="multipart/form-data">
			<Label>Reps</Label>
			<Form.Field class="-mx-2 -mb-6 mt-4" {form} name="rep_id">
				<Form.Control let:attrs>
					<RepTable bind:rep_ids {reps} />
					<input {...attrs} type="hidden" bind:value={serialisedRepID} />
				</Form.Control>
			</Form.Field>
			<Form.Button class="mt-10 w-full">Save</Form.Button>
		</form>
	</Card.Content>
</Card.Root>
