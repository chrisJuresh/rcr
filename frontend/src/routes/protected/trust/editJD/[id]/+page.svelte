<script lang="ts">
	import type { PageData } from './$types.js';
	import JD from './jd.svelte';
	import JDQuestions from './jd-questions.svelte';
	export let data: PageData;
</script>

<div class="flex w-11/12 flex-wrap justify-center">
	<div class="mx-6 mb-6 w-96">
		<JD jd={data.jd} jd_ids={data.jd_ids} />
	</div>

	<div class="w-11/12 min-w-96 lg:w-6/12">
		<JDQuestions data={data.form} />
	</div>

	<div class="hidden 2xl:block 2xl:w-96"></div>
</div>
