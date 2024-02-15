<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import axios from 'axios';
    import { writable, derived } from 'svelte/store';
  
    // TypeScript interface definitions
    interface User {
      username?: string;
      first_name?: string;
      last_name?: string;
      trust?: string;
      roles?: string[];
      can_be_reviewer?: boolean;
      can_be_representative?: boolean;
      can_be_rcr_employee?: boolean;
    }
  
    interface Trust {
      id: string;
      name: string;
    }
  
    interface Role {
      id: string;
      name: string;
    }
  
    // Svelte stores
    const user = writable<User | null>(null);
    const trusts = writable<Trust[]>([]);
    const roles = writable<Role[]>([]);
  
    const allowedRoles = derived(user, $user => {
      const roles = ['TRUST_EMPLOYEE'];
      if ($user?.can_be_reviewer) roles.push('REVIEWER');
      if ($user?.can_be_representative) roles.push('REPRESENTATIVE');
      if ($user?.can_be_rcr_employee) roles.push('RCR_EMPLOYEE');
      return roles;
    });
  
    // On component mount
    onMount(async () => {
      const token = localStorage.getItem('token');
      if (!token) {
        goto('/login');
        return;
      }
      try {
        const headers = { 'Authorization': `Token ${token}` };
  
        const [userResponse, trustsResponse, rolesResponse] = await Promise.all([
          axios.get('http://localhost:8000/profile/', { headers }),
          axios.get('http://localhost:8000/trusts/', { headers }),
          axios.get('http://localhost:8000/roles/', { headers }),
        ]);
  
        user.set(userResponse.data);
        trusts.set(trustsResponse.data);
        roles.set(rolesResponse.data);
      } catch (error) {
        console.error(error);
      }
    });
  
    // Update profile function
    async function updateProfile(): Promise<void> {
      const token = localStorage.getItem('token');
      const userData = $user; // Get current user data
      if (!token || !userData) return;
      try {
        await axios.put('http://localhost:8000/profile/', userData, {
          headers: { 'Authorization': `Token ${token}` },
        });
        // Add success message or action here if needed
      } catch (error) {
        console.error(error);
        // Handle errors, maybe set an error message in your store
      }
    }
  </script>
  
  <div>
    {#if $user}
      <h1>Edit: {$user.username}</h1>
      <form on:submit|preventDefault={updateProfile}>
        <label for="firstName">First Name:</label>
        <input id="firstName" bind:value={$user.first_name} type="text" required>
  
        <label for="lastName">Last Name:</label>
        <input id="lastName" bind:value={$user.last_name} type="text" required>
  
        <label for="trusts">Trust:</label>
        <select id="trusts" bind:value={$user.trust} required>
          <option disabled value="">Please select a trust</option>
          {#each $trusts as trust}
            <option value={trust.id}>{trust.name}</option>
          {/each}
        </select>
  
        <label for="roles">Title (hold ctrl to select multiple| message the rcr for permission to other roles):</label>
        <select id="roles" bind:value={$user.roles} multiple>
          {#each $roles as role}
            <option value={role.id} class:highlight-role={$user.roles && $user.roles.includes(role.id)} disabled={!$allowedRoles.includes(role.name)}>
              {role.name}
            </option>
          {/each}
        </select>
        <button type="submit">Update</button>
      </form>
      <button on:click={() => goto('/panel')}>Go to Panel</button>
    {/if}
  </div>
