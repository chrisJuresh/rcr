<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import Dash from 'svelte-radix/Dash.svelte';

	export let user;

	const colorClasses = [
		'fill-purple-400 text-purple-400',
	];

	function getRandomColorClass() {
		return colorClasses[Math.floor(Math.random() * colorClasses.length)];
	}
</script>

	<Card.Root>
		<Card.Header>
			<Card.Title>Approved</Card.Title>
			<Card.Description>You have been approved for the following by the RCR</Card.Description>
		</Card.Header>
		<Card.Content>
			Roles
{#each user.approved_roles as approved_roles}
	<div class="flex items-center">
		<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
		<small>{approved_roles.name}<br /></small>
	</div>
{:else}
	<div class="flex items-center">
		<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
		<small>None<br /></small>
	</div>
{/each}
		</Card.Content>
		<Card.Content>
			Trusts
			<div class="flex items-center">
				<Dash class="mr-1 h-3 w-3 {getRandomColorClass()}" />
				<small>{user.trust ? user.trust : 'None'}<br /></small>
			</div>
		</Card.Content>
	</Card.Root>
