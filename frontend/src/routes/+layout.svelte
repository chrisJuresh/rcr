<script lang="ts">
	import '../app.pcss';
	import { page } from '$app/stores';
	import { ModeWatcher } from 'mode-watcher';
	import { Toaster } from '$lib/components/ui/sonner';
	import Nav from './nav.svelte';
	import Logo from '$lib/icons/logo.svelte';

	let size = 4;
</script>

<div class="flex min-h-screen flex-col">
	<svlete:head>
	<header class="fixed w-full " class:bar-head={$page.url.pathname !== '/auth'}>
		<Nav />
	</header>
</svlete:head>

	<div class="flex flex-grow items-center justify-center mt-24">
	<slot />
	</div>

	<footer class="w-full">
		<div class="flex justify-end mr-6">
			<Logo {size} />
		</div>
	</footer>
</div>

<ModeWatcher />
<Toaster />