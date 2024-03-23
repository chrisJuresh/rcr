<script lang="ts">
	import type { PageData } from './$types';
	import ProfileForm from './ProfileForm.svelte';
	import Approved from './Approved.svelte';
	export let data: PageData;
</script>

<div class="flex flex-wrap-reverse justify-center">
	<div class="mr-6 ml-6 w-60">
		<Approved user={data.user}></Approved>
	</div>
	<ProfileForm data={data.form} user={data.user} roles={data.roles} trusts={data.trusts} />
	<div class="mr-6 ml-6 w-60"></div>
</div>
