<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import Dash from 'svelte-radix/Dash.svelte';
	import type { components } from '$lib/types.d.ts';
	import { Label } from '$lib/components/ui/label';
	import ChevronLeft from 'lucide-svelte/icons/chevron-left';
	import ChevronRight from 'lucide-svelte/icons/chevron-right';
	import Copy from 'lucide-svelte/icons/copy';
	import { Button } from '$lib/components/ui/button';
	import * as Pagination from '$lib/components/ui/pagination';
	import { Separator } from '$lib/components/ui/separator';

	export let user: components['schemas']['UserProfileOut'];
</script>

<Card.Root class="overflow-hidden">
	<Card.Header class="flex flex-row items-start bg-muted/50">
		<div class="grid gap-0.5">
			<Card.Title class="group flex items-center gap-2 text-lg">Approvals</Card.Title>
			<Card.Description
				>Please contact us at a@r.uk once you have filled out this form to gain approval.</Card.Description
			>
		</div>
		<div class="ml-auto flex items-center gap-1"></div>
	</Card.Header>
	<Card.Content class="p-6 text-sm">
		<div class="grid gap-3">
			<div class="font-semibold">Roles</div>
			<ul class="grid gap-3">
				{#each user.approved_roles || [] as roles}
					<li class="flex items-center">
						<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
						{roles}
					</li>
				{:else}
					<li class="flex items-center">
						<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
						<span><p class="text-muted-foreground">None</p></span>
					</li>
				{/each}
			</ul>
			<Separator class="my-2" />
			<div class="font-semibold">Trusts</div>
			<ul class="grid gap-3">
				{#each user.approved_trusts || [] as trusts}
					<li class="flex items-center">
						<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
						<span>{trusts}</span>
					</li>
				{:else}
					<li class="flex items-center">
						<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
						<span><p class="text-muted-foreground">None</p></span>
					</li>
				{/each}
			</ul>
		</div>
	</Card.Content>
	<Card.Footer class="flex flex-row items-center border-t bg-muted/50 px-6 py-3">
		<div class="text-xs text-muted-foreground">
			Last Updated <time dateTime="2023-11-23">ADD DATE</time>
		</div>
	</Card.Footer>
</Card.Root>
