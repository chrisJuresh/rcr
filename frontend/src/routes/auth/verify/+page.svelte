<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	let timeLeft = 3; // Starting countdown from 5

	onMount(() => {
		const interval = setInterval(() => {
			timeLeft -= 1; // Decrease time left by 1 every second
			if (timeLeft <= 0) {
				clearInterval(interval); // Stop the countdown
				goto('/protected/profile'); // Redirect when countdown reaches 0
			}
		}, 1000);
	});
</script>

<div class="flex min-h-screen flex-row items-center justify-center">
	<h1>Redirecting...</h1>
	<p>Please wait {timeLeft} seconds.</p>
</div>
