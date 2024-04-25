<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { setMode, resetMode } from 'mode-watcher';
	import type { components } from '$lib/types';
	import { rolesStore } from '$lib/store';

	import Sun from 'svelte-radix/Sun.svelte';
	import Moon from 'svelte-radix/Moon.svelte';
	import Exit from 'svelte-radix/Exit.svelte';
	import Person from 'svelte-radix/Person.svelte';
	import EnvelopeClosed from 'svelte-radix/EnvelopeClosed.svelte';
	import Pencil1 from 'svelte-radix/Pencil1.svelte';
	import Pencil2 from 'svelte-radix/Pencil2.svelte';
	import Reader from 'svelte-radix/Reader.svelte';
	import CardStackPlus from 'svelte-radix/CardStackPlus.svelte';
	import ChatBubble from 'svelte-radix/ChatBubble.svelte';

	let stateValue: string[] = [];
	rolesStore.subscribe((items) => {
		stateValue = Array.isArray(items) ? items.map((item) => item.label) : [];
	});

	export let user_roles: components['schemas']['UserRolesOut'];

	function handleLogout() {
		goto('/logout');
	}

	function navigateTo(path: string) {
		rolesStore.set([]);
		goto(path);
		updateButtonStyles(path);
	}

	let baseButtons = [
		{
			icon: Person,
			label: 'Profile',
			path: '/protected/profile',
			variant: 'outline',
			disabled: false
		},
		{
			icon: EnvelopeClosed,
			label: 'Tasks',
			path: '/protected/panel',
			variant: 'outline',
			disabled: false
		}
	];

	type ButtonType = {
		icon: any;
		label: string;
		path: string;
		variant: string;
		disabled: boolean;
	};

	let buttons: ButtonType[] = [];

	$: {
		let isTrustEmployee = user_roles.roles?.includes('Trust Employee');
		let isReviewer = user_roles.roles?.includes('Reviewer');
		let isRCREmployee = user_roles.roles?.includes('RCR Employee');
		let isRepresentative = user_roles.roles?.includes('Representative');
		let additionalButtons = [];

		if (isTrustEmployee) {
			additionalButtons.push(
				{
					icon: Pencil2,
					label: 'New JD',
					path: '/protected/trust/newJD',
					variant: 'outline',
					disabled: false
				},
				{
					icon: Pencil1,
					label: 'Edit JD',
					path: '/protected/trust/editJD',
					variant: 'outline',
					disabled: false
				}
			);
		} else if (
			!isTrustEmployee &&
			(stateValue.includes('Trust Employee') ||
				user_roles.requested_roles?.includes('Trust Employee'))
		) {
			additionalButtons.push(
				{
					icon: Pencil2,
					label: 'New JD',
					path: '/protected/trust/newJD',
					variant: 'secondary',
					disabled: true
				},
				{
					icon: Pencil1,
					label: 'Edit JD',
					path: '/protected/trust/editJD',
					variant: 'secondary',
					disabled: true
				}
			);
		}

		if (isReviewer || isRCREmployee) {
			additionalButtons.push({
				icon: Reader,
				label: 'Review JD',
				path: '/protected/review',
				variant: 'outline',
				disabled: false
			});
		} else if (
			(!isReviewer && !isRCREmployee && stateValue.includes('Reviewer')) ||
			stateValue.includes('RCR Employee') ||
			user_roles.requested_roles?.includes('Reviewer') ||
			user_roles.requested_roles?.includes('RCR Employee')
		) {
			additionalButtons.push({
				icon: Reader,
				label: 'Review JD',
				path: '/protected/review',
				variant: 'secondary',
				disabled: true
			});
		}

		if (isTrustEmployee || isRepresentative) {
			additionalButtons.push(
				{
					icon: CardStackPlus,
					label: 'New AAC',
					path: '/protected/trust/newAAC',
					variant: 'outline',
					disabled: false
				},
				{
					icon: ChatBubble,
					label: 'View AAC',
					path: '/protected/trust/viewAAC',
					variant: 'outline',
					disabled: false
				}
			);
		} else if (
			!isTrustEmployee &&
			(stateValue.includes('Trust Employee') ||
				user_roles.requested_roles?.includes('Trust Employee'))
		) {
			additionalButtons.push(
				{
					icon: CardStackPlus,
					label: 'New AAC',
					path: '/protected/trust/newAAC',
					variant: 'secondary',
					disabled: true
				},
				{
					icon: ChatBubble,
					label: 'View AAC',
					path: '/protected/trust/viewAAC',
					variant: 'secondary',
					disabled: true
				}
			);
		}

		buttons = [...baseButtons, ...additionalButtons];

		updateButtonStyles($page.url.pathname);
	}

	function updateButtonStyles(activePath: string) {
		buttons = buttons.map((button) => ({
			...button,
			variant:
				button.variant === 'secondary'
					? 'secondary'
					: activePath.startsWith(button.path)
						? 'default'
						: 'outline'
		}));
	}

	$: updateButtonStyles($page.url.pathname);
</script>

<nav>
	<ul class="grid grid-cols-5 gap-4">
		<li class="m-6 place-self-start">
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
		{#if $page.url.pathname !== '/auth'}
			<li class="col-span-3 m-4 flex flex-wrap justify-center">
				{#each buttons as { icon, label, path, variant, disabled }}
					<Button
						on:click={disabled ? null : () => navigateTo(path)}
						{variant}
						{disabled}
						class="m-1 w-28 2xl:m-2"
					>
						<svelte:component this={icon} class="mr-2 max-h-4 min-h-4 min-w-4 max-w-4" />
						{label}</Button
					>
				{/each}
			</li>

			<li class="m-6 place-self-end">
				<Button variant="destructive" on:click={handleLogout}>
					<Exit class="mr-2 h-4 w-4" />
					Log Out
				</Button>
			</li>
		{/if}
	</ul>
</nav>
