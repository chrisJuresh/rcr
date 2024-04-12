<script lang="ts">
	import type { PageData } from './$types.js';
	import SelectJD from './select-jd.svelte';
	export let data: PageData;
</script>

<div class="flex flex-wrap justify-center space-x-6">
	<div class="w-64">
		<SelectJD jd_ids={data.jd_ids} />
	</div>
</div>
