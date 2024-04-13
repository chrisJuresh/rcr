<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Form from '$lib/components/ui/form';
	import { Input, InputFile } from '$lib/components/ui/input';
	import { formSchema, type FormSchema } from './schema';
	import SuperDebug, {
		type SuperValidated,
		type Infer,
		superForm,
		fileProxy
	} from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import * as Select from '$lib/components/ui/select';
	import type { components } from '$lib/types.d.ts';
	import { toast } from 'svelte-sonner';
	import LockClosed from 'svelte-radix/LockClosed.svelte';
	import { Label } from '$lib/components/ui/label';
	import Dash from 'svelte-radix/Dash.svelte';
	import { goto } from '$app/navigation';

	import ChevronLeft from 'lucide-svelte/icons/chevron-left';
	import ChevronRight from 'lucide-svelte/icons/chevron-right';
	import Copy from 'lucide-svelte/icons/copy';
	import { Button } from '$lib/components/ui/button';
	import * as Pagination from '$lib/components/ui/pagination';
	import { Separator } from '$lib/components/ui/separator';

	export let jd: components['schemas']['JDOut'];
	export let jd_ids: components['schemas']['JDIDsOut']['ids'];

	$: currentIndex = jd_ids.indexOf(jd.id);

	$: previousJDid = currentIndex > 0 ? jd_ids[currentIndex - 1] : undefined;

	$: nextJDid = currentIndex < jd_ids.length - 1 ? jd_ids[currentIndex + 1] : undefined;

	console.log(nextJDid, previousJDid);
</script>

<Card.Root class="overflow-hidden">
	<Card.Header class="flex flex-row items-start bg-muted/50">
		<div class="grid gap-0.5">
			<Card.Title class="group flex items-center gap-2 text-lg">
				{jd.id}
				<Button
					size="icon"
					variant="outline"
					class="h-6 w-6 opacity-0 transition-opacity group-hover:opacity-100"
				>
					<Copy class="h-3 w-3" />
					<span class="sr-only">Copy ID</span>
				</Button>
			</Card.Title>
			<Card.Description>{jd.trust}</Card.Description>
		</div>
		<div class="ml-auto flex items-center gap-1">
			<LockClosed class="text-muted-foreground" />
		</div>
	</Card.Header>
	<Card.Content class="p-6 text-sm">
		<div class="grid gap-3">
			<div class="font-semibold">Job Description</div>
			<ul class="grid gap-3">
				<li class="flex items-center justify-between">
					<span class="text-muted-foreground"> File </span>
					<span>Add download link</span>
				</li>
				<li class="flex items-center justify-between">
					<span class="text-muted-foreground"> Consultant Type </span>
					<span>{jd.consultant_type}</span>
				</li>
			</ul>
			<Separator class="my-2" />
			<div class="font-semibold">Primary Specialities</div>
			<ul class="grid gap-3">
				{#each jd.primary_specialities || [] as primary_speciality}
					<li class="flex items-center">
						<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
						{primary_speciality}
					</li>
				{/each}
			</ul>
			<Separator class="my-2" />
			<div class="font-semibold">Sub Specialities</div>
			<ul class="grid gap-3">
				{#each jd.sub_specialities || [] as sub_speciality}
					<li class="flex items-center">
						<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
						<span>{sub_speciality}</span>
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
		{#if previousJDid !== undefined || nextJDid !== undefined}
			<Pagination.Root count={10} class="ml-auto mr-0 w-auto">
				<Pagination.Content>
					{#if previousJDid !== undefined}
						<Pagination.Item>
							<Button
								on:click={() => goto(`${previousJDid}`)}
								size="icon"
								variant="outline"
								class="h-6 w-6"
							>
								<ChevronLeft class="h-3.5 w-3.5" />
								<span class="sr-only">Previous JD</span>
							</Button>
						</Pagination.Item>
					{/if}
					{#if nextJDid !== undefined}
						<Pagination.Item>
							<Button
								on:click={() => goto(`${nextJDid}`)}
								size="icon"
								variant="outline"
								class="h-6 w-6"
							>
								<ChevronRight class="h-3.5 w-3.5" />
								<span class="sr-only">Next JD</span>
							</Button>
						</Pagination.Item>
					{/if}
				</Pagination.Content>
			</Pagination.Root>
		{/if}
	</Card.Footer>
</Card.Root>
