<script lang="ts">
	import LoginTab from './LoginTab.svelte';
	import RegisterTab from './RegisterTab.svelte';
	import * as Card from '$lib/components/ui/card';
	import * as Tabs from '$lib/components/ui/tabs';
	import { type LoginFormSchema, type RegisterFormSchema } from './schema';
	import type { SuperValidated } from 'sveltekit-superforms';

	export let loginForm: SuperValidated<LoginFormSchema>;
	export let registerForm: SuperValidated<RegisterFormSchema>;
</script>

<div class="flex min-h-screen items-center justify-center">
	<Card.Root class="w-[400px]">
		<Card.Header>
			<Card.Title>Authenticate</Card.Title>
			<Card.Description>Access your account or create a new one.</Card.Description>
		</Card.Header>
		<Card.Content>
			<Tabs.Root value="login" class="w-full">
				<Tabs.List>
					<Tabs.Trigger value="login">Login</Tabs.Trigger>
					<Tabs.Trigger value="register">Register</Tabs.Trigger>
				</Tabs.List>
				<Tabs.Content value="login">
					<LoginTab form={loginForm}/>
				</Tabs.Content>
				<Tabs.Content value="register">
					<RegisterTab form={registerForm}/>
				</Tabs.Content>
			</Tabs.Root>
		</Card.Content>
	</Card.Root>
</div>