<script lang="ts">
	import DataTable from './(components)/data-table.svelte';
	import data from './(data)/tasks.json';
	import * as Card from '$lib/components/ui/card';
</script>

<Card.Root class="neu xl:w-[1080px] w-11/12">
			<Card.Header>
				<h2 class="text-2xl font-bold tracking-tight">Welcome back!</h2>
			</Card.Header>
			<Card.Content>
				<DataTable {data} />
			</Card.Content>
		</Card.Root>
