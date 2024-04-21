<script lang="ts">
	import { buttonVariants } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import * as Tooltip from "$lib/components/ui/tooltip";
	import * as Form from '$lib/components/ui/form/index.js';

	export let valid: boolean;

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
    		<Dialog.Footer>
    			<div class="mb-2 mr-2 flex justify-end">
    				<form method="POST" action="?/approve">
    					<Form.Button disabled={!valid}>Approve JD</Form.Button>
    				</form>
    			</div>
    		</Dialog.Footer>
    	</Dialog.Content>
    </Dialog.Root>
  </Tooltip.Trigger>
  <Tooltip.Content class=bg-slate-600>
    <p>You must save any changes before you can approve</p>
  </Tooltip.Content>
</Tooltip.Root>