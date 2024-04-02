<script lang="ts">
	import type { PageData } from './$types.js';
	import NewJdForm from './newJDForm.svelte';
	export let data: PageData;
</script>

<div class="">
	<NewJdForm data={data.form} specialities={data.specialities} />
</div>
