<script lang="ts">
	import type { PageData } from './$types';
	import ProfileForm from './profile-form.svelte';
	import Approved from './approved.svelte';
	export let data: PageData;
</script>

<div class="flex flex-wrap-reverse justify-center w-11/12">
	<div class="md:max-w-80 md:min-w-80 min-w-96 max-w-96">
		<Approved user={data.user}></Approved>
	</div>
	<div class="min-w-96 w-11/12 md:w-9/12 lg:w-5/12 xl:w-5/12 2xl:w-4/12 max-w-xl mb-6 mx-6">
		<ProfileForm
			data={data.form}
			user={data.user}
			roles={data.roles}
			trusts={data.trusts}
			specialities={data.specialities}
		/>
	</div>
	<div class="2xl:w-80 2xl:block hidden"></div>
</div>
