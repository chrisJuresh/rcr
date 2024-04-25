<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import AACTable from '../../(components)/data-table.svelte';
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<Card.Root class="neu h-min w-11/12 2xl:w-6/12">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">View AACs</Card.Title>
		<Card.Description>Please select the AAC you would like to view</Card.Description>
	</Card.Header>
	<Card.Content>
		<AACTable aacs={data.aacs} />
	</Card.Content>
</Card.Root>
