<script lang="ts">
	import type { PageData } from './$types';
	import ProfileForm from './profile-form.svelte';
	import Approved from './approved.svelte';
	export let data: PageData;
</script>

<div class="flex w-11/12 flex-wrap-reverse justify-center">
	<div class="min-w-96 max-w-96 md:min-w-80 md:max-w-80">
		<Approved user={data.user}></Approved>
	</div>
	<div class="mx-6 mb-6 w-11/12 min-w-96 max-w-xl md:w-9/12 lg:w-5/12 xl:w-5/12 2xl:w-4/12">
		<ProfileForm
			data={data.form}
			user={data.user}
			roles={data.roles}
			trusts={data.trusts}
			specialities={data.specialities}
		/>
	</div>
	<div class="hidden 2xl:block 2xl:w-80"></div>
</div>
