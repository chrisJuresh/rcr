<script lang="ts">
	import type { PageData } from './$types.js';
	import JD from '../../../(components)/jd.svelte';
	import JDQuestions from './jd-questions.svelte';
	export let data: PageData;
	import * as Card from '$lib/components/ui/card';
	import { mode } from 'mode-watcher';

	$: invertStyle = $mode === 'dark' ? 'invert(95.5%)' : 'none';
</script>

<div class="flex w-11/12 flex-wrap justify-center">
	<div class=w-full>
		<div class="mx-auto mb-6 h-44 w-8/12">
			<Card.Root class="h-full">
				<Card.Content class="flex h-full justify-center">
					<img
						class="mt-3 h-full rounded-xl object-contain"
						src="http://localhost:8000{data.jd.state_diagram}"
						alt={data.jd.state_diagram}
						style="filter: {invertStyle};"
					/>
				</Card.Content>
			</Card.Root>
		</div>
		<div class="flex flex-wrap justify-center">
			<div class="mx-6 mb-6 w-96">
				<JD jd={data.jd} jd_ids={data.jd_ids} />
			</div>
			<div class="w-11/12 min-w-96 lg:w-6/12">
				<JDQuestions data={data.form} jd={data.jd} />
			</div>
		</div>
	</div>
	<div class="hidden 2xl:block 2xl:w-96"></div>
</div>
