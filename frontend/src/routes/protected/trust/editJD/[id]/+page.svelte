<script lang="ts">
	import type { PageData } from './$types.js';
	import JD from './jd.svelte';
	import JDQuestions from './jd-questions.svelte';
	export let data: PageData;
</script>

<div class="flex flex-wrap justify-center w-11/12">
	<div class="w-96 mx-6 mb-6">
		<JD jd={data.jd} jd_ids={data.jd_ids} />
	</div>

	<div class="min-w-96 lg:w-6/12 w-11/12">
		<JDQuestions data={data.form} jd_checklist={data.jd_checklist} />
	</div>

	<div class="2xl:w-96 2xl:block hidden"></div>
</div>
