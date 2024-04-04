<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import Dash from 'svelte-radix/Dash.svelte';
	import type { components } from '$lib/types.d.ts';

	export let user: components['schemas']['UserProfileOut'];

</script>

<Card.Root>
	<Card.Header>
		<Card.Title class="text-2xl font-bold">Approvals</Card.Title>
		<Card.Description
			>Please contact us at a@r.uk once you have filled out this form to gain approval.</Card.Description
		>
	</Card.Header>
	<Card.Content>
		Roles
		{#each user.approved_roles || [] as approved_roles}
			<div class="flex items-center">
				<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
				<small>{approved_roles}<br /></small>
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
		{#each user.approved_trusts || [] as approved_trusts}
			<div class="flex items-center">
				<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
				<small>{approved_trusts}<br /></small>
			</div>
		{:else}
			<div class="flex items-center">
				<Dash class="mr-1 h-3 w-3 fill-purple-400 text-purple-400" />
				<small>None<br /></small>
			</div>
		{/each}
	</Card.Content>
</Card.Root>
