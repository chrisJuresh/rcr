<script lang="ts">
	import type { PageData } from './$types';
	import ProfileForm from './ProfileForm.svelte';
	import Approved from './Approved.svelte';
	export let data: PageData;
</script>

<div class="flex min-h-screen flex-row items-center justify-center">
	<div class=" h-[400px]">
		<div class="flex justify-center">
			<div class="mr-6 w-56">
				<Approved user={data.user}></Approved>
			</div>
			<ProfileForm data={data.form} user={data.user} roles={data.roles} trusts={data.trusts} />
			<div class="mr-6 w-56"></div>
		</div>
	</div>
</div>
