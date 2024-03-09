<script lang="ts">
	import DataTable from "./(components)/data-table.svelte";
	import UserNav from "./(components)/user-nav.svelte";
	import data from "./(data)/tasks.json";
</script>

<div class="flex min-h-screen items-center justify-center">
	<div class=" h-[1000px]" >
<h1 class="text-2xl font-bold">This page is a work in progress</h1>
<h2 class="text-xl">Below is an example of how the panel table may be formatted</h2>
		<div class="neu mt-7" >
<div class="hidden h-full flex-1 flex-col space-y-8 p-8 md:flex">
	<div class="flex items-center justify-between space-y-2">
		<div>
			<h2 class="text-2xl font-bold tracking-tight">Welcome back!</h2>
			<p class="text-muted-foreground">Here's a list of your tasks for this month!</p>
		</div>
		<div class="flex items-center space-x-2">
			<UserNav />
		</div>
	</div>
	<DataTable {data} />
</div>
		</div>
	</div>
</div>