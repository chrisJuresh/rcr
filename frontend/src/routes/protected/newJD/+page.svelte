<script lang="ts">
	import type { PageData } from './$types.js';
	import NewJdForm from './newJDForm.svelte';
	export let data: PageData;
</script>

<div class="w-11/12 md:w-[600px]">
	<NewJdForm data={data.form} specialities={data.specialities} />
</div>
