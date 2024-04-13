<script lang="ts">
	import Ellipsis from 'lucide-svelte/icons/ellipsis';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Button } from '$lib/components/ui/button';
	import { goto } from '$app/navigation';
	import ChevronRight from 'svelte-radix/ChevronRight.svelte';
	export let id: string;
</script>

<Button class="pl-0" type="submit" variant="link" on:click={() => goto(`editJD/${id}`)}>
	Edit <ChevronRight class="h-4 w-4" />
</Button>
