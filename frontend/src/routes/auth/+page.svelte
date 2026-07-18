<script lang="ts">
	import LoginTab from './login.svelte';
	import RegisterTab from './register.svelte';
	import * as Card from '$lib/components/ui/card';
	import * as Tabs from '$lib/components/ui/tabs';
	import { Button } from '$lib/components/ui/button';
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
					<div class="my-4 flex items-center gap-3 text-xs text-muted-foreground">
						<div class="h-px flex-1 bg-border"></div>
						<span>or</span>
						<div class="h-px flex-1 bg-border"></div>
					</div>
					<form method="POST" action="?/demo">
						<Button type="submit" variant="outline" class="w-full">Explore the demo</Button>
					</form>
				</Card.Content>
			</Card.Root>
		</div>
	</div>
</div>
