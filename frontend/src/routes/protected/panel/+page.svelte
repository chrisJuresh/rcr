<script lang="ts">
	import DataTable from '../(components)/data-table.svelte';
	import * as Card from '$lib/components/ui/card';
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<Card.Root class="neu h-min w-11/12 2xl:w-6/12">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">Panel</Card.Title>
		<Card.Description>Here are your tasks</Card.Description>
	</Card.Header>
	<Card.Content>
		<DataTable jds={data.jds} aacs={data.aacs} />
	</Card.Content>
</Card.Root>
