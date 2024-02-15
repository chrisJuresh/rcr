<script lang="ts">
    import { goto } from '$app/navigation';
    import axios from 'axios';
    import { writable } from 'svelte/store';
  
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
  