<script lang="ts">
	import type { PageData } from './$types';
	import ProfileForm from './ProfileForm.svelte';
	export let data: PageData;
</script>

<ProfileForm data={data.form} user={data.user} roles={data.roles} />
