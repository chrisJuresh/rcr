<script lang="ts">
	import '../app.pcss';
	import { page } from '$app/stores';
	import { ModeWatcher } from 'mode-watcher';
	import { Toaster } from '$lib/components/ui/sonner';
	import Nav from './nav.svelte';
	import Logo from '$lib/icons/logo.svelte';
	import type { PageData } from './$types';
	export let data: PageData;

	let size = 4;
</script>

<div class="flex min-h-screen flex-col">
	<svlete:head>
		<header class="fixed w-full" class:bar-head={$page.url.pathname !== '/auth'}>
			<Nav user_roles={data.user_roles} />
		</header>
	</svlete:head>

	<div class="mt-36 flex flex-grow justify-center lg:mt-24">
		<div class="flex w-full items-center justify-center">
			<div class="flex h-full w-full justify-center lg:h-[70vh]">
				<slot />
			</div>
		</div>
	</div>

	<footer class="w-full">
		<div class="mr-6 flex justify-end">
			<Logo {size} />
		</div>
	</footer>
</div>

<ModeWatcher />
<Toaster />
