<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { goto } from '$app/navigation';
	import { Button } from '$lib/components/ui/button';
	import type { components } from '$lib/types';
	import * as Table from '$lib/components/ui/table';
	import ChevronRight from 'svelte-radix/ChevronRight.svelte';
	import { Label } from '$lib/components/ui/label';
	import JDTable from '../../panel/data-table.svelte';

	export let jds: components['schemas']['JDPanel']['jds'];
</script>

<Card.Root class="neu w-full">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">Find JD</Card.Title>
		<Card.Description>Please select the JD <br />that you would like to edit</Card.Description>
	</Card.Header>
	<Card.Content>
		<JDTable {jds} />
	</Card.Content>
</Card.Root>
