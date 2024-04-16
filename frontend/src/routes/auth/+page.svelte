<script lang="ts">
	import LoginTab from './login.svelte';
	import RegisterTab from './register.svelte';
	import * as Card from '$lib/components/ui/card';
	import * as Tabs from '$lib/components/ui/tabs';
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<div class="h-[50vh]">
	<div class="flex h-full justify-center">
		<div class="flex items-end">
			<Card.Root class="neu w-96 ">
				<Card.Header>
					<Card.Title class="text-2xl font-bold">Authenticate</Card.Title>
					<Card.Description>Access your account or create a new one</Card.Description>
				</Card.Header>
				<Card.Content>
					<Tabs.Root value="login" class="w-full">
						<Tabs.List>
							<Tabs.Trigger value="login">Login</Tabs.Trigger>
							<Tabs.Trigger value="register">Register</Tabs.Trigger>
						</Tabs.List>
						<Tabs.Content value="login">
							<LoginTab data={data.loginForm} />
						</Tabs.Content>
						<Tabs.Content value="register">
							<RegisterTab data={data.registerForm} />
						</Tabs.Content>
					</Tabs.Root>
				</Card.Content>
			</Card.Root>
		</div>
	</div>
</div>
