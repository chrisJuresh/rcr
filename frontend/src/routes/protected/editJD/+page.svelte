<script lang="ts">
	import type { PageData } from './$types.js';
	import JD from './jd.svelte';
	import JDQuestions from './jd-questions.svelte';
	export let data: PageData;
</script>

<div class="flex flex-wrap justify-center space-x-6">
	<div class="w-96 mb-6">
	<JD data={data.form} user={data.user} specialities={data.specialities} />
</div>
	
<div class=mx-auto>
<JDQuestions/>
</div>

	<div class="w-96 "></div>
</div>
