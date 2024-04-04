<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Form from '$lib/components/ui/form';
	import {Input, InputFile} from '$lib/components/ui/input';
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

</script>

<Card.Root class="neu">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">JD Review Form</Card.Title>
		<Card.Description>Please fill in the fields below to continue</Card.Description>
	</Card.Header>
	<Card.Content>
	</Card.Content>
</Card.Root>
