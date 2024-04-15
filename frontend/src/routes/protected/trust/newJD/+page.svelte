<script lang="ts">
	import type { PageData } from './$types.js';
	import NewJDForm from './new-jd-form.svelte';
	export let data: PageData;
</script>

<div class="hy-auto min-w-96">
	<NewJDForm data={data.form} user_trust={data.user_trust} specialities={data.specialities} />
</div>
