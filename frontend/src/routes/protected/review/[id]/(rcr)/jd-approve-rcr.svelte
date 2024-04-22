<script lang="ts">
	import { buttonVariants } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import * as Form from '$lib/components/ui/form/index.js';
	import * as Tooltip from '$lib/components/ui/tooltip';
	import * as Select from '$lib/components/ui/select/index.js';
	import type { components } from '$lib/types.d.ts';

	export let valid: boolean;
	export let reviewers: components['schemas']['ReviewersOut']['reviewers'];

	let selectedReviewer: number = -1;

	// Group reviewers by region
	let groupedReviewers = reviewers.reduce((acc, reviewer) => {
		let region = reviewer.same_region;
		if (!acc[region]) {
			acc[region] = [];
		}
		acc[region].push(reviewer);
		return acc;
	}, {});
</script>

<Tooltip.Root>
	<Tooltip.Trigger>
		<Dialog.Root>
			<Dialog.Trigger disabled={!valid} class={buttonVariants({ variant: 'default' })}>
				Approve
			</Dialog.Trigger>
			<Dialog.Content class="sm:max-w-[425px]">
				<Dialog.Header>
					<Dialog.Title>Approve this JD</Dialog.Title>
					<Dialog.Description>
						Are you sure you would like to approve this JD?
						<br /> You will not be able to make any changes once you approve.
					</Dialog.Description>
				</Dialog.Header>
				<form method="POST" action="?/approve">
					<Select.Root
						onSelectedChange={(v) => {
							v && (selectedReviewer = v.value);
						}}
					>
						<Select.Trigger class="w-[180px]">
							<Select.Value placeholder="Select a Reviewer" />
						</Select.Trigger>
						<Select.Content>
							{#each Object.entries(groupedReviewers) as [region, regionReviewers]}
								<Select.Group>
									<Select.Label>{region}</Select.Label>
									{#each regionReviewers as reviewer}
										<Select.Item value={reviewer.id} label={reviewer.name}></Select.Item>
									{/each}
									<div class="mt-5"></div>
								</Select.Group>
							{/each}
						</Select.Content>
						<Select.Input name="selectedReviewer" />
					</Select.Root>
					<input name="reviewer" type="hidden" bind:value={selectedReviewer} />

					<div class="mb-2 mr-2 flex justify-end gap-2">
						<Form.Button disabled={!valid}>Approve JD</Form.Button>
					</div>
				</form>
			</Dialog.Content>
		</Dialog.Root>
	</Tooltip.Trigger>
	<Tooltip.Content class="bg-slate-600">
		<p>You must save any changes before you can approve</p>
	</Tooltip.Content>
</Tooltip.Root>
