<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import JDTable from '../../(components)/data-table.svelte';
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<Card.Root class="neu h-min w-11/12 2xl:w-6/12">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">Find JD</Card.Title>
		<Card.Description>Please select the JD that you would like to edit</Card.Description>
	</Card.Header>
	<Card.Content>
		<JDTable jds={data.jds} />
	</Card.Content>
</Card.Root>
