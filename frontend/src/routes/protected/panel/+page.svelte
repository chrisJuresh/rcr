<script lang="ts">
	import DataTable from './data-table.svelte';
	import * as Card from '$lib/components/ui/card';
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<Card.Root class="neu w-11/12 xl:w-[1080px]">
	<Card.Header>
		<h2 class="text-2xl font-bold tracking-tight">Welcome back!</h2>
	</Card.Header>
	<Card.Content>
		<DataTable jds={data.jds} />
	</Card.Content>
</Card.Root>
