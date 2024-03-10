<script lang="ts">
	import '../app.pcss';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { Button } from '$lib/components/ui/button';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { setMode, resetMode, ModeWatcher } from 'mode-watcher';
	import Sun from 'svelte-radix/Sun.svelte';
	import Moon from 'svelte-radix/Moon.svelte';
	import Exit from 'svelte-radix/Exit.svelte';

	function handleLogout() {
		goto('/logout');
	}

	let buttons = [
		{ label: 'Edit Profile', path: '/protected/profile' },
		{ label: 'View Panel', path: '/protected/panel' }
	];

	function navigateTo(path) {
		goto(path);
		updateButtonStyles(path);
	}

	function updateButtonStyles(activePath) {
		buttons = buttons.map((button) => ({
			...button,
			variant: button.path === activePath ? 'default' : 'outline'
		}));
	}

	$: updateButtonStyles($page.url.pathname);
</script>

<ul class="fixed flex w-full justify-between" class:nav={$page.url.pathname !== '/login'}>
	<li class="m-6">
		<DropdownMenu.Root>
			<DropdownMenu.Trigger asChild let:builder>
				<Button builders={[builder]} variant="outline" size="icon" class="">
					<Sun
						class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
					/>
					<Moon
						class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
					/>
					<span class="sr-only">Toggle theme</span>
				</Button>
			</DropdownMenu.Trigger>
			<DropdownMenu.Content align="end">
				<DropdownMenu.Item on:click={() => setMode('light')}>Light</DropdownMenu.Item>
				<DropdownMenu.Item on:click={() => setMode('dark')}>Dark</DropdownMenu.Item>
				<DropdownMenu.Item on:click={() => resetMode()}>System</DropdownMenu.Item>
			</DropdownMenu.Content>
		</DropdownMenu.Root>
	</li>
	{#if $page.url.pathname !== '/login'}
		<li class="m-6">
			{#each buttons as { label, path, variant }}
				<Button on:click={() => navigateTo(path)} {variant} class="mx-2">{label}</Button>
			{/each}
		</li>

		<li class="m-6">
			<Button variant="destructive" on:click={handleLogout}>
				<Exit class="mr-2 h-4 w-4" />
				Log Out
			</Button>
		</li>
	{/if}
	
</ul>
<ModeWatcher></ModeWatcher>
<slot />
