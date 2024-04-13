<script lang="ts">
	import type { PageData } from './$types';
	import ProfileForm from './profile-form.svelte';
	import Approved from './approved.svelte';
	export let data: PageData;
</script>

<div class="flex flex-wrap-reverse justify-center space-x-6">
	<div class="w-72">
		<Approved user={data.user}></Approved>
	</div>
	<div class="hy-auto mb-6">
		<ProfileForm
			data={data.form}
			user={data.user}
			roles={data.roles}
			trusts={data.trusts}
			specialities={data.specialities}
		/>
	</div>
	<div class="xl:w-72"></div>
</div>
