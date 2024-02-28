<script lang="ts">
	import '../app.pcss';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { Separator } from '$lib/components/ui/separator';
	import { Button } from '$lib/components/ui/button';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { setMode, resetMode, ModeWatcher } from 'mode-watcher';
    import Sun from "svelte-radix/Sun.svelte";
    import Moon from "svelte-radix/Moon.svelte";
    import Exit from "svelte-radix/Exit.svelte";

	function handleLogout() {
		goto('/logout');
	}

	function editProfile() {
		goto('/protected/profile');
	}

	function gotoPanel() {
		goto('/protected/panel');
	}
</script>

{#if $page.url.pathname !== '/login' }
	<div class="absolute right-4 top-4 md:right-8 md:top-8">
		<Button variant="destructive" on:click={handleLogout}>
			<Exit class="mr-2 h-4 w-4" />
			Log Out
		</Button>
	</div>

	<div class="flex justify-center">
		<div class="absolute top-4 md:top-8">
			<div class="flex h-10 space-x-4">
				<Button on:click={editProfile} variant="ghost">Edit Profile</Button>
				<Separator orientation="vertical" />
				<Button on:click={gotoPanel} variant="ghost">View Panel</Button>
			</div>
		</div>
	</div>
{/if}

<DropdownMenu.Root>
	<DropdownMenu.Trigger asChild let:builder>
		<Button
			builders={[builder]}
			variant="outline"
			size="icon"
			class="absolute left-4 top-4 md:left-8 md:top-8"
		>
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
<ModeWatcher></ModeWatcher>
<slot />