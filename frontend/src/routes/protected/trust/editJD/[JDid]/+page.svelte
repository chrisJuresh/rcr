<script lang="ts">
	import type { PageData } from './$types.js';
	import JD from './jd.svelte';
	import JDQuestions from './jd-questions.svelte';
	export let data: PageData;
</script>

<div class="flex h-96 flex-wrap justify-center space-x-6">
	<div class="mb-6 w-96">
		<JD jd={data.jd} jd_ids={data.jd_ids} />
	</div>

	<div class="w-8/12">
		<JDQuestions jd_checklist={data.jd_checklist} />
	</div>

	<div class="w-96"></div>
</div>
