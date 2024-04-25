<script lang="ts">
	import Ellipsis from 'lucide-svelte/icons/ellipsis';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Button } from '$lib/components/ui/button';
	import { goto } from '$app/navigation';
	import ChevronRight from 'svelte-radix/ChevronRight.svelte';
	import { page } from '$app/stores';

	export let id: string;
</script>

{#if $page.url.pathname === '/protected/trust/editJD'}
	<Button class="pl-0" type="submit" variant="link" on:click={() => goto(`editJD/${id}`)}>
		Edit <ChevronRight class="h-4 w-4" />
	</Button>
{:else if $page.url.pathname === '/protected/review'}
	<Button class="pl-0" type="submit" variant="link" on:click={() => goto(`review/${id}`)}>
		Review <ChevronRight class="h-4 w-4" />
	</Button>
{:else if $page.url.pathname === '/protected/trust/viewAAC'}
	<Button class="pl-0" type="submit" variant="link" on:click={() => goto(`viewAAC/${id}`)}>
		View <ChevronRight class="h-4 w-4" />
	</Button>
{:else}
	<DropdownMenu.Root>
		<DropdownMenu.Trigger asChild let:builder>
			<Button variant="ghost" builders={[builder]} size="icon" class="relative h-8 w-8 p-0">
				<span class="sr-only">Open menu</span>
				<Ellipsis class="h-4 w-4" />
			</Button>
		</DropdownMenu.Trigger>
		<DropdownMenu.Content>
			<DropdownMenu.Group>
				<DropdownMenu.Label>Actions</DropdownMenu.Label>
				<DropdownMenu.Item on:click={() => navigator.clipboard.writeText(id)}>
					Copy ID
				</DropdownMenu.Item>
			</DropdownMenu.Group>
			<DropdownMenu.Separator />
			<DropdownMenu.Item on:click={() => goto(`trust/editJD/${id}`)}>Edit JD</DropdownMenu.Item>
			<DropdownMenu.Item on:click={() => goto(`review/${id}`)}>Review JD</DropdownMenu.Item>
		</DropdownMenu.Content>
	</DropdownMenu.Root>
{/if}
