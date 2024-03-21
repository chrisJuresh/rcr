<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import Dash from 'svelte-radix/Dash.svelte';

	export let user;

	const colorClasses = [
		'fill-red-400 text-red-400',
		'fill-green-400 text-green-400',
		'fill-blue-400 text-blue-400',
		'fill-yellow-400 text-yellow-400',
		'fill-purple-400 text-purple-400',
		'fill-pink-400 text-pink-400',
		'fill-indigo-400 text-indigo-400'
	];

	function getRandomColorClass() {
		return colorClasses[Math.floor(Math.random() * colorClasses.length)];
	}
</script>

{#if user.approved_roles.length > 0}
	<Card.Root>
		<Card.Header>
			<Card.Title>Approved</Card.Title>
			<Card.Description>You have been approved for the following by the RCR</Card.Description>
		</Card.Header>
		<Card.Content>
			Roles
			{#each user.approved_roles as approved_roles}
				<div class="flex items-center">
					<Dash class="mr-1 h-3 w-3 {getRandomColorClass()}" />
					<small>{approved_roles.name}<br /></small>
				</div>
			{/each}
		</Card.Content>
		<Card.Content>
			Trusts
			<div class="flex items-center">
				<Dash class="mr-1 h-3 w-3 {getRandomColorClass()}" />
				<small>{user.trust}<br /></small>
			</div>
		</Card.Content>
	</Card.Root>
{/if}
