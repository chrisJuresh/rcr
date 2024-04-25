<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Form from '$lib/components/ui/form';
	import { Input, InputFile } from '$lib/components/ui/input';
	import { formSchema, type FormSchema } from './schema';
	import SuperDebug, {
		type SuperValidated,
		type Infer,
		superForm,
		fileProxy
	} from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import * as Select from '$lib/components/ui/select';
	import type { components } from '$lib/types.d.ts';
	import { toast } from 'svelte-sonner';
	import LockClosed from 'svelte-radix/LockClosed.svelte';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button';
</script>

<Card.Root>
	<Card.Header>
		<Card.Title class="text-2xl font-bold">Upload Outcome Form</Card.Title>
		<Card.Description
			>Please submit a completed outcome form once the panel is complete.</Card.Description
		>
		<Card.Description
			>You may download a copy of the form <a href class="text-blue-500">here</a></Card.Description
		>
	</Card.Header>
	<Card.Content>
		<div class="flex flex-col gap-2">
			<Label>Outcome Form</Label>
			<InputFile type="file" />

			<Button>Submit</Button>
		</div>
	</Card.Content>
</Card.Root>
