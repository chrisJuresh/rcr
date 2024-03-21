<script lang="ts">
	import DataTable from './(components)/data-table.svelte';
	import data from './(data)/tasks.json';
	import * as Card from '$lib/components/ui/card';
</script>

<div class="flex min-h-screen flex-row items-center justify-center">
	<div class="h-[1000px] w-[1080px]">
		<Card.Root class="neu">
			<Card.Header>
				<h2 class="text-2xl font-bold tracking-tight">Welcome back!</h2>
			</Card.Header>
			<Card.Content>
				<DataTable {data} />
			</Card.Content>
		</Card.Root>
	</div>
</div>
