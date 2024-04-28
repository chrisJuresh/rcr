<script lang="ts">
	import type { components } from '$lib/types.d.ts';
	import { createTable, Render, Subscribe, createRender } from 'svelte-headless-table';
	import {
		addPagination,
		addSortBy,
		addTableFilter,
		addHiddenColumns,
		addSelectedRows
	} from 'svelte-headless-table/plugins';
	import DataTableCheckbox from './(data-table)/data-table-checkbox.svelte';
	import DataTableActions from './(data-table)/data-table-actions.svelte';
	import { readable } from 'svelte/store';
	import ArrowUpDown from 'lucide-svelte/icons/arrow-up-down';
	import * as Table from '$lib/components/ui/table';
	import { Button } from '$lib/components/ui/button';
	import { Input } from '$lib/components/ui/input';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { page } from '$app/stores';
	import MixerHorizontal from 'svelte-radix/MixerHorizontal.svelte';
	import * as Select from '$lib/components/ui/select';
	import ChevronRight from 'svelte-radix/ChevronRight.svelte';
	import ChevronLeft from 'svelte-radix/ChevronLeft.svelte';
	import DoubleArrowRight from 'svelte-radix/DoubleArrowRight.svelte';
	import DoubleArrowLeft from 'svelte-radix/DoubleArrowLeft.svelte';
	import { Badge } from '$lib/components/ui/badge';

	export let jds: components['schemas']['JDPanel']['jds'];
	export let aacs: components['schemas']['AACPanel']['aacs'];
	export let reps: components['schemas']['RepsOut']['reps'];

	export let consultant_type: string;

	const mergeData = () => {
		const safeAacs = Array.isArray(aacs) ? aacs : []; 
		const safeJds = Array.isArray(jds) ? jds : []; 
		const safeReps = Array.isArray(reps) ? reps : []; 

		const mappedJds = safeJds.map((jd) => ({
			...jd,
			type: 'JD'
		}));

		const mappedAacs = safeAacs.map((aac) => ({
			...aac,
			type: 'AAC'
		}));

		const mappedReps = safeReps.map((rep) => ({
			...rep,
			type: 'Rep'
		}));

		return [...mappedJds, ...mappedAacs, ...mappedReps];
	};

	const panel = mergeData();

	const table = createTable(readable(panel), {
		page: addPagination(),
		sort: addSortBy({ disableMultiSort: true }),
		filter: addTableFilter({
			fn: ({ filterValue, value }) => value.toLowerCase().includes(filterValue.toLowerCase())
		}),
		hide: addHiddenColumns(),
		select: addSelectedRows()
	});

	const columns = table.createColumns([
		table.display({
			id: 'select',
			header: '',
			cell: ({ row }, { pluginStates }) => {
				const { getRowState } = pluginStates.select;
				const { isSelected } = getRowState(row);
				return createRender(DataTableCheckbox, {
					checked: isSelected
				});
			},
			plugins: {
				sort: {
					disable: true
				}
			}
		}),
		table.column({
			accessor: 'id',
			header: 'ID'
		}),
		table.column({
			accessor: 'consultant_type',
			header: 'Consultant Type',
			plugins: {
				sort: {
					disable: true
				}
			}
		}),
		table.column({
			accessor: 'primary_specialties',
			header: 'Primary Specialties',
			plugins: {
				sort: {
					disable: true
				}
			}
		}),
		table.column({
			accessor: 'sub_specialties',
			header: 'Sub Specialties',
			plugins: {
				sort: {
					disable: true
				}
			}
		}),
		table.column({
			accessor: 'status',
			header: 'Status',
			plugins: {
				sort: {
					disable: true
				}
			}
		}),
		table.column({
			accessor: 'date',
			header: 'Date'
		}),
		table.column({
			accessor: ({ id }) => id.toString(),
			header: '',
			cell: ({ value }) => {
				return createRender(DataTableActions, { id: value });
			}
		})
	]);

	const { headerRows, pageRows, tableAttrs, tableBodyAttrs, pluginStates, flatColumns, rows } =
		table.createViewModel(columns);

	const { hasNextPage, hasPreviousPage, pageIndex, pageCount, pageSize } = pluginStates.page;
	const { filterValue } = pluginStates.filter;
	const { hiddenColumnIds } = pluginStates.hide;
	const { selectedDataIds } = pluginStates.select;

	const ids = flatColumns.map((col) => col.id);
	let hideForId = Object.fromEntries(ids.map((id) => [id, true]));

	$: $hiddenColumnIds = Object.entries(hideForId)
		.filter(([, hide]) => !hide)
		.map(([id]) => id);

	const hidableCols = [
		'consultant_type',
		'primary_specialties',
		'sub_specialties',
		'status',
		'date'
	];

	const currentPage = $page.url.pathname;

	ids.forEach((id) => {
		if (currentPage.startsWith('/protected/trust/newAAC')) {
			if (id === 'status' || id === 'date') {
				hideForId[id] = false;
			}
			if (id === 'select') {
				hideForId[id] = true;
			}
		} else if (currentPage.startsWith('/protected/trust/viewAAC')) {
			if (id === 'sub_specialties') {
				hideForId[id] = false;
			} else {
			}
		} else {
			if (id === 'select') {
				hideForId[id] = false;
			} else {
			}
		}
	});

	export let jd_ids;
	export let rep_ids;

	$: if (currentPage.startsWith('/protected/trust/newAAC')) {
		jd_ids = Object.entries($selectedDataIds)
			.filter(([_, isSelected]) => isSelected)
			.map(([id, _]) => parseInt(id))
			.map((index) => jds[index].id);
	}

	$: if (currentPage.startsWith('/protected/trust/viewAAC')) {
		rep_ids = Object.entries($selectedDataIds)
			.filter(([_, isSelected]) => isSelected)
			.map(([id, _]) => parseInt(id))
			.map((index) => reps[index].id);
	}
</script>

<div>
	<div class="flex items-center pb-4">
		<Input class="w-96" placeholder="Filter rows..." type="text" bind:value={$filterValue} />

		<DropdownMenu.Root>
			<DropdownMenu.Trigger asChild let:builder>
				<Button variant="outline" size="sm" class="ml-auto hidden h-8 lg:flex" builders={[builder]}>
					<MixerHorizontal class="mr-2 h-4 w-4" />
					View
				</Button>
			</DropdownMenu.Trigger>
			<DropdownMenu.Content>
				{#each flatColumns as col}
					{#if hidableCols.includes(col.id)}
						<DropdownMenu.CheckboxItem bind:checked={hideForId[col.id]}>
							{col.header}
						</DropdownMenu.CheckboxItem>
					{/if}
				{/each}
			</DropdownMenu.Content>
		</DropdownMenu.Root>
	</div>
	<div class="rounded-md border">
		<Table.Root {...$tableAttrs}>
			<Table.Header>
				{#each $headerRows as headerRow}
					<Subscribe rowAttrs={headerRow.attrs()}>
						<Table.Row>
							{#each headerRow.cells as cell (cell.id)}
								<Subscribe attrs={cell.attrs()} let:attrs props={cell.props()} let:props>
									<Table.Head {...attrs} class="[&:has([role=checkbox])]:pl-3">
										{#if cell.id === 'id'}
											<div class="pl-4">
												<Button variant="ghost" class="-ml-4" on:click={props.sort.toggle}>
													<Render of={cell.render()} />
													<ArrowUpDown class={'ml-2 h-4 w-4'} />
												</Button>
											</div>
										{:else if cell.id === 'date'}
											<Button variant="ghost" class="-ml-4" on:click={props.sort.toggle}>
												<Render of={cell.render()} />
												<ArrowUpDown class={'ml-2 h-4 w-4'} />
											</Button>
										{:else}
											<Render of={cell.render()} />
										{/if}
									</Table.Head>
								</Subscribe>
							{/each}
						</Table.Row>
					</Subscribe>
				{/each}
			</Table.Header>
			<Table.Body {...$tableBodyAttrs}>
				{#each $pageRows as row (row.id)}
					{#if row.cells.find((c) => c.id === 'consultant_type' && c.value !== consultant_type) === undefined || !currentPage.startsWith('/protected/trust/newAAC')}
						<Subscribe rowAttrs={row.attrs()} let:rowAttrs>
							<Table.Row {...rowAttrs} data-state={$selectedDataIds[row.id] && 'selected'}>
								{#each row.cells as cell (cell.id)}
									<Subscribe attrs={cell.attrs()} let:attrs>
										<Table.Cell {...attrs}>
											{#if cell.id === 'id'}
												<div class="flex pl-4">
													<div class="w-10">
														<Render of={cell.render()} />
													</div>
													<Badge class="ml-2" variant="outline"
														>{panel[parseInt(cell.row.id)].type}</Badge
													>
												</div>
											{:else}
												<Render of={cell.render()} />
											{/if}
										</Table.Cell>
									</Subscribe>
								{/each}
							</Table.Row>
						</Subscribe>
					{/if}
				{/each}
			</Table.Body>
		</Table.Root>
		{#if !consultant_type && currentPage.startsWith('/protected/trust/newAAC')}
			<div class="m-4 mx-auto flex justify-center">
				<h1 class="text-muted-foreground">Please select a Consultant Type to proceed</h1>
			</div>
		{:else if jds}
			{#if jds.length === 0}
				<div class="m-4 mx-auto flex justify-center">
					<h1>No JDs</h1>
				</div>
			{/if}
		{:else if aacs}
			{#if aacs.length === 0}
				<div class="m-4 mx-auto flex justify-center">
					<h1>No AACs</h1>
				</div>
			{/if}
		{/if}
	</div>
	<div class="mt-4 flex items-center justify-between px-2">
		<div class="flex-1 text-sm text-muted-foreground">
			{#if currentPage.startsWith('/protected/trust/newAAC')}
				{Object.keys($selectedDataIds).length} of {$rows.length} row(s) selected.
			{/if}
		</div>
		<div class="flex items-center space-x-6 lg:space-x-1">
			<div class="ml-8 flex items-center space-x-2">
				<p class="text-sm font-medium">Rows per page</p>
				<Select.Root
					onSelectedChange={(selected) => pageSize.set(Number(selected?.value))}
					selected={{ value: 10, label: '10' }}
				>
					<Select.Trigger class="h-8 w-[70px]">
						<Select.Value placeholder="Select page size" />
					</Select.Trigger>
					<Select.Content>
						<Select.Item value="10">10</Select.Item>
						<Select.Item value="20">20</Select.Item>
						<Select.Item value="30">30</Select.Item>
						<Select.Item value="40">40</Select.Item>
						<Select.Item value="50">50</Select.Item>
					</Select.Content>
				</Select.Root>
			</div>
			<div class="flex w-[100px] items-center justify-center text-sm font-medium">
				Page {$pageIndex + 1} of {$pageCount}
			</div>
			<div class="flex items-center space-x-2">
				<Button
					variant="outline"
					class="hidden h-8 w-8 p-0 lg:flex"
					on:click={() => ($pageIndex = 0)}
					disabled={!$hasPreviousPage}
				>
					<span class="sr-only">Go to first page</span>
					<DoubleArrowLeft size={15} />
				</Button>
				<Button
					variant="outline"
					class="h-8 w-8 p-0"
					on:click={() => ($pageIndex = $pageIndex - 1)}
					disabled={!$hasPreviousPage}
				>
					<span class="sr-only">Go to previous page</span>
					<ChevronLeft size={15} />
				</Button>
				<Button
					variant="outline"
					class="h-8 w-8 p-0"
					disabled={!$hasNextPage}
					on:click={() => ($pageIndex = $pageIndex + 1)}
				>
					<span class="sr-only">Go to next page</span>
					<ChevronRight size={15} />
				</Button>
				<Button
					variant="outline"
					class="hidden h-8 w-8 p-0 lg:flex"
					disabled={!$hasNextPage}
					on:click={() => ($pageIndex = Math.ceil($rows.length / $pageRows.length) - 1)}
				>
					<span class="sr-only">Go to last page</span>
					<DoubleArrowRight size={15} />
				</Button>
			</div>
		</div>
	</div>
</div>
