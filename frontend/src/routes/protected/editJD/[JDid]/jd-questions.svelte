<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Input } from '$lib/components/ui/input';
	import { goto } from '$app/navigation';
	import { Button } from '$lib/components/ui/button';
	import type { components } from '$lib/types';
	import * as Select from '$lib/components/ui/select';
</script>

<Card.Root class="neu">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">JD Review Form</Card.Title>
		<Card.Description>Please fill in the form to continue</Card.Description>
	</Card.Header>
	<Card.Content>
		<div class="flex items-center space-x-2"></div>
	</Card.Content>
</Card.Root>
