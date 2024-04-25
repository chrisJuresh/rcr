<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import type { components } from '$lib/types.d.ts';
	import LockClosed from 'svelte-radix/LockClosed.svelte';
	import Dash from 'svelte-radix/Dash.svelte';
	import { goto } from '$app/navigation';
	import ChevronLeft from 'lucide-svelte/icons/chevron-left';
	import ChevronRight from 'lucide-svelte/icons/chevron-right';
	import Copy from 'lucide-svelte/icons/copy';
	import { Button } from '$lib/components/ui/button';
	import * as Pagination from '$lib/components/ui/pagination';
	import { Separator } from '$lib/components/ui/separator';

	export let aac: components['schemas']['AACOut'];
	export let aac_ids: components['schemas']['AACIDsOut'];

	$: currentIndex = aac_ids.ids.indexOf(aac.id);

	$: previousAACid = currentIndex > 0 ? aac_ids.ids[currentIndex - 1] : undefined;

	$: nextAACid = currentIndex < aac_ids.ids.length - 1 ? aac_ids.ids[currentIndex + 1] : undefined;

	function getFilename(url) {
		return url.substring(url.lastIndexOf('/') + 1);
	}
</script>

<Card.Root>
	<Card.Header class="flex flex-row items-start bg-muted/50">
		<div class="grid gap-0.5">
			<Card.Title class="group flex items-center gap-2 text-lg">
				{aac.id}
				<Button
					size="icon"
					variant="outline"
					class="h-6 w-6 opacity-0 transition-opacity group-hover:opacity-100"
				>
					<Copy class="h-3 w-3" />
					<span class="sr-only">Copy ID</span>
				</Button>
			</Card.Title>
			<Card.Description>{aac.trust}</Card.Description>
		</div>
		<div class="ml-auto flex items-center gap-1">
			<LockClosed class="text-muted-foreground" />
		</div>
	</Card.Header>
	<Card.Content class="flex-1 p-6 text-sm">
		<div class="grid h-full gap-3">
			<div class="font-semibold">AAC</div>
			<ul class="grid gap-3">
				<li class="flex items-center justify-between">
					<span class="text-muted-foreground"> Consultant Type </span>
					<span>{aac.consultant_type}</span>
				</li>
				<li class="flex items-center justify-between">
					<span class="text-muted-foreground"> Date </span>
					<span>{aac.date}</span>
				</li>
			</ul>
			<Separator class="my-2" />

			<div class="font-semibold">Job Descriptions</div>

			{#each aac.jds || [] as jd}
				<div class="font-medium">{jd.id}</div>
				<ul class="grid gap-3">
					<li class="flex items-center justify-between">
						<span class="text-muted-foreground"> File </span>
						<span>
							<a href="http://localhost:8000{jd.file}">
								<p class="text-cyan-800 underline">{getFilename(jd.file)}</p>
							</a>
						</span>
					</li>
					<li class="flex items-center justify-between">
						<span class="text-muted-foreground"> Primary Specialities </span>
						<span>{jd.primary_specialities}</span>
					</li>
					<li class="flex items-center justify-between">
						<span class="text-muted-foreground"> Sub Specialities </span>
						{#if jd.sub_specialities.length > 0}
							<span>{jd.sub_specialities}</span>
						{:else}
							<span><p class="text-muted-foreground">None</p></span>
						{/if}
					</li>
				</ul>
				<Separator />
			{/each}
		</div>
	</Card.Content>
	<Card.Footer class="flex flex-row items-center border-t bg-muted/50 px-6 py-3">
		<div class="text-xs text-muted-foreground">
			Last Updated <time dateTime={aac.date}>{aac.date}</time>
		</div>
		{#if previousAACid !== undefined || nextAACid !== undefined}
			<Pagination.Root count={10} class="ml-auto mr-0 w-auto">
				<Pagination.Content>
					{#if previousAACid !== undefined}
						<Pagination.Item>
							<Button
								on:click={() => goto(`${previousAACid}`)}
								size="icon"
								variant="outline"
								class="h-6 w-6"
							>
								<ChevronLeft class="h-3.5 w-3.5" />
								<span class="sr-only">Previous AAC</span>
							</Button>
						</Pagination.Item>
					{/if}
					{#if nextAACid !== undefined}
						<Pagination.Item>
							<Button
								on:click={() => goto(`${nextAACid}`)}
								size="icon"
								variant="outline"
								class="h-6 w-6"
							>
								<ChevronRight class="h-3.5 w-3.5" />
								<span class="sr-only">Next AAC</span>
							</Button>
						</Pagination.Item>
					{/if}
				</Pagination.Content>
			</Pagination.Root>
		{/if}
	</Card.Footer>
</Card.Root>
