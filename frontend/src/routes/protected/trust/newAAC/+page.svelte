<script lang="ts">
	import type { PageData } from './$types.js';
	import NewAACForm from './new-aac-form.svelte';
	export let data: PageData;
</script>

<div class="hy-auto min-w-96">
	<NewAACForm data={data.form} user_trust={data.user_trust} jds={data.jds} />
</div>
