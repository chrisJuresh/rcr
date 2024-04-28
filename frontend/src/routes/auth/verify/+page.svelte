<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	let timeLeft = 3; 

	onMount(() => {
		const interval = setInterval(() => {
			timeLeft -= 1;
			if (timeLeft <= 0) {
				clearInterval(interval); 
				goto('/protected/profile');
			}
		}, 1000);
	});
</script>

<div class="flex min-h-screen flex-row items-center justify-center">
	<h1>Redirecting...</h1>
	<p>Please wait {timeLeft} seconds.</p>
</div>
