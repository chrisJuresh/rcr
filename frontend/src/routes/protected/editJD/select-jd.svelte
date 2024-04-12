<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Input } from '$lib/components/ui/input';
	import { goto } from '$app/navigation';
	import { Button } from '$lib/components/ui/button';
	import type { components } from '$lib/types';
	import * as Select from '$lib/components/ui/select';

	let selectedJD;

	export let jd_ids: components['schemas']['JDIDsOut']['ids'];
</script>

<Card.Root class="neu">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">JD Review Form</Card.Title>
		<Card.Description>Please select the JD <br />that you would like to edit</Card.Description>
	</Card.Header>
	<Card.Content>
		<div class="flex items-center space-x-2">
			<Select.Root
				onSelectedChange={(v) => {
					selectedJD = v.value;
				}}
			>
				<Select.Trigger>
					<Select.Value placeholder={'Select Your JD'} />
				</Select.Trigger>
				<Select.Content>
					{#each jd_ids as jd_id (jd_id)}
						<Select.Item value={String(jd_id)} label={String(jd_id)} />
					{/each}
				</Select.Content>
			</Select.Root>

			<Button type="submit" on:click={() => goto(`editJD/${selectedJD}`)}>Edit</Button>
		</div>
	</Card.Content>
</Card.Root>
