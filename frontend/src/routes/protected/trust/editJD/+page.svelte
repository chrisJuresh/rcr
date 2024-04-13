<script lang="ts">
	import type { PageData } from './$types.js';
	import SelectJD from './select-jd.svelte';
	export let data: PageData;
</script>

<div class="w-11/12 justify-center lg:w-[1080px]">
	<SelectJD jds={data.jds} />
</div>
