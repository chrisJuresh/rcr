<script lang="ts">
	import { buttonVariants } from '$lib/components/ui/button/index.js';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import * as Form from '$lib/components/ui/form/index.js';
	import * as Tooltip from '$lib/components/ui/tooltip';
	import { Label } from "$lib/components/ui/label/index.js";
	import { Input, InputFile } from '$lib/components/ui/input';
	export let disabled: boolean;

</script>

    <Tooltip.Root>
        <Tooltip.Trigger>
            <Dialog.Root>
                <Dialog.Trigger disabled={disabled} class={buttonVariants({ variant: 'secondary' })}>
                    Upload JD
                </Dialog.Trigger>
                <Dialog.Content class="sm:max-w-[425px]">
                    
<form enctype="multipart/form-data" method="POST" action="?/upload">
                    <Dialog.Header>
                        <Dialog.Title>Upload updated JD</Dialog.Title>
                    </Dialog.Header>
                    <Dialog.Description>
                        <div class="grid w-full max-w-sm items-center gap-1.5 mt-4">
                            <Label for="jd">Job Description</Label>
                            <Input id="jd" type="file" name="file"/>
                        </div>
                    </Dialog.Description>
                    <Dialog.Footer>
                        <div class="mb-2 mt-4 mr-2 flex justify-end">
                            <Form.Button type="submit" disabled={disabled}>Upload</Form.Button>
                        </div>
                    </Dialog.Footer>
                    </form>
                    
                </Dialog.Content>
            </Dialog.Root>
        </Tooltip.Trigger>
    </Tooltip.Root>