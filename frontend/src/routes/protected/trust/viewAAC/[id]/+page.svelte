<script lang="ts">
	import type { PageData } from './$types.js';
	import AAC from './aac.svelte';
	import AACOutcome from './aac-outcome-form.svelte';
	import RepTable from './select-rep.svelte';
	export let data: PageData;
	import * as Card from '$lib/components/ui/card';
	import { mode } from 'mode-watcher';

	$: invertStyle = $mode === 'dark' ? 'invert(95.5%)' : 'none';
</script>

<div class="flex w-11/12 flex-wrap justify-center">
	<div class="w-full">
		<div class="flex flex-wrap justify-center">
			<div class=" mb-6 w-96">
				<AAC aac={data.aac} aac_ids={data.aac_ids} />
			</div>
			<div class="mx-6 w-11/12 min-w-96 lg:w-6/12">
				<RepTable data={data.form} reps={data.reps} />
			</div>

			<div class="w-96">
				<AACOutcome />
			</div>
		</div>
	</div>
</div>
