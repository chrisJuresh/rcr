<script lang="ts">
	import type { PageData } from './$types';
	import AuthForm from './AuthForm.svelte';
	export let data: PageData;
</script>

<AuthForm loginForm={data.loginForm} registerForm={data.registerForm} />
