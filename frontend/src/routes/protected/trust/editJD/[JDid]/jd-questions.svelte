<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import { Input } from '$lib/components/ui/input';
	import { goto } from '$app/navigation';
	import { Button } from '$lib/components/ui/button';
	import type { components } from '$lib/types';
	import * as Select from '$lib/components/ui/select';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { Label } from '$lib/components/ui/label';
	import { Textarea } from '$lib/components/ui/textarea';
	export let jd_checklist: components['schemas']['JDChecklistOut'];

	import * as Table from '$lib/components/ui/table/index.js';
</script>

<Card.Root class="neu w-full">
	<Card.Header>
		<Card.Title class="text-2xl font-bold">JD Review Form</Card.Title>
		<Card.Description>Please fill in the form to continue</Card.Description>
	</Card.Header>
	<Card.Content>
		<Table.Root>
			<Table.Header>
				<Table.Row>
					<Table.Head class="w-4/12">Question</Table.Head>
					<Table.Head class="w-1/12 text-center">Present</Table.Head>
					<Table.Head class="w-1/12">Page</Table.Head>
					<Table.Head>Comments</Table.Head>
				</Table.Row>
			</Table.Header>
			<Table.Body>
				{#each jd_checklist.checklist as checklist, i (i)}
					<Table.Row>
						<Table.Cell>
							<Label>{checklist.question.text}</Label>
						</Table.Cell>
						<Table.Cell class="p-1 text-center">
							<Checkbox />
						</Table.Cell>
						<Table.Cell>
							<Input type="number" />
						</Table.Cell>
						<Table.Cell>
							<Textarea class="min-h-1" />
						</Table.Cell>
					</Table.Row>
				{/each}
			</Table.Body>
		</Table.Root>

		<Button class="mt-6 w-full">Submit</Button>
	</Card.Content>
</Card.Root>
