<script lang="ts">
    import { goto } from '$app/navigation';
    import axios from 'axios';
    import { writable } from 'svelte/store';

    import { Button } from "$lib/components/ui/button";
    import * as Card from "$lib/components/ui/card";
    import * as Select from "$lib/components/ui/select";
    import { Input } from "$lib/components/ui/input";
    import { Label } from "$lib/components/ui/label";

    // TypeScript interface definitions for state
    interface AuthState {
      username: string;
      password: string;
      errorMessage: string;
    }
  
    // Using Svelte's writable stores for reactive state
    const authState = writable<AuthState>({ username: '', password: '', errorMessage: '' });
  
    // Login method
    async function handleLogin(): Promise<void> {
      const { username, password } = $authState;
      try {
        const response = await axios.post('http://localhost:8000/login/', {
          username,
          password,
        });
        localStorage.setItem('token', response.data.token);
        axios.defaults.headers.common['Authorization'] = `Token ${response.data.token}`;
        goto('/profile'); // SvelteKit navigation
      } catch (error: any) {
        if (error.response && error.response.status === 400) {
          authState.update((state) => ({ ...state, errorMessage: 'Invalid Credentials' }));
        } else {
          authState.update((state) => ({ ...state, errorMessage: 'An error occurred during login' }));
        }
        console.error(error);
      }
    }
  
    // Register method
    async function handleRegister(): Promise<void> {
      const { username, password } = $authState;
      try {
        const response = await axios.post('http://localhost:8000/register/', {
          username,
          password,
        });
        localStorage.setItem('token', response.data.token);
        axios.defaults.headers.common['Authorization'] = `Token ${response.data.token}`;
        goto('/profile'); // SvelteKit navigation
      } catch (error: any) {
        let message = 'An error occurred during registration';
        if (error.response && error.response.status === 400) {
          if (error.response.data.username) {
            message = 'Email is already registered';
          } else {
            message = 'Invalid data';
          }
        }
        authState.update((state) => ({ ...state, errorMessage: message }));
        console.error(error);
      }
    }

    const frameworks = [
    {
      value: "sveltekit",
      label: "SvelteKit"
    },
    {
      value: "next",
      label: "Next.js"
    },
    {
      value: "astro",
      label: "Astro"
    },
    {
      value: "nuxt",
      label: "Nuxt.js"
    }
  ];
  </script>
  
  <div class="auth-page">
    <form on:submit|preventDefault>
      <label for="username">Email</label>
      <input id="username" bind:value={$authState.username} type="text" required>
  
      <label for="password">Password</label>
      <input id="password" bind:value={$authState.password} type="password" required>
  
      <button type="button" on:click={handleLogin}>Login</button>
      <button type="button" on:click={handleRegister}>Register</button>
    </form>
    {#if $authState.errorMessage}
      <div class="error-message">{$authState.errorMessage}</div>
    {/if}
  </div>
  

  <Card.Root class="auth-page">
    <Card.Header>
      <Card.Title>Login or Register</Card.Title>
      <Card.Description>Access your account or create a new one.</Card.Description>
    </Card.Header>
    <Card.Content>
      <form on:submit|preventDefault class="flex flex-col space-y-4">
        <div class="flex flex-col space-y-1.5">
          <Label for="username">Email</Label>
          <Input id="username" bind:value={$authState.username} type="text" required />
        </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="password">Password</Label>
          <Input id="password" bind:value={$authState.password} type="password" required />
        </div>
        {#if $authState.errorMessage}
          <div class="error-message">{$authState.errorMessage}</div>
        {/if}
      </form>
    </Card.Content>
    <Card.Footer class="flex justify-between">
      <Button variant="outline" on:click={handleLogin}>Login</Button>
      <Button on:click={handleRegister}>Register</Button>
    </Card.Footer>
  </Card.Root>

  
  <Card.Root class="w-[350px]">
    <Card.Header>
      <Card.Title>Create project</Card.Title>
      <Card.Description>Deploy your new project in one-click.</Card.Description>
    </Card.Header>
    <Card.Content>
      <form>
        <div class="grid w-full items-center gap-4">
          <div class="flex flex-col space-y-1.5">
            <Label for="name">Name</Label>
            <Input id="name" placeholder="Name of your project" />
          </div>
          <div class="flex flex-col space-y-1.5">
            <Label for="framework">Framework</Label>
            <Select.Root>
              <Select.Trigger id="framework">
                <Select.Value placeholder="Select" />
              </Select.Trigger>
              <Select.Content>
                {#each frameworks as framework}
                  <Select.Item value={framework.value} label={framework.label}
                    >{framework.label}</Select.Item
                  >
                {/each}
              </Select.Content>
            </Select.Root>
          </div>
        </div>
      </form>
    </Card.Content>
    <Card.Footer class="flex justify-between">
      <Button variant="outline">Cancel</Button>
      <Button>Deploy</Button>
    </Card.Footer>
  </Card.Root>