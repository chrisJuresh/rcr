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

<div class="flex flex-col h-lvh">
	<svlete:head>
		<header class="fixed w-full" class:bar-head={$page.url.pathname !== '/auth'}>
			<Nav user_roles={data.user_roles} />
		</header>
	</svlete:head>
	
<div class="mt-52 md:mt-36 xl:mt-32 2xl:mt-44"></div>
<div class="flex-grow flex justify-center">
	<slot />
</div>

	<footer class="w-full mt-auto">
		<div class="mr-6 flex justify-end">
			<Logo {size} />
		</div>
	</footer>
</div>

<ModeWatcher />
<Toaster />
