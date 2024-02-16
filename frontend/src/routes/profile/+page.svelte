<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import axios from 'axios';
    import { writable, derived } from 'svelte/store';
    import { Button } from "$lib/components/ui/button";
    import * as Card from "$lib/components/ui/card";
    import * as Select from "$lib/components/ui/select";
    import { Input } from "$lib/components/ui/input";
    import { Label } from "$lib/components/ui/label";


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
  
{#if $user}
  <Card.Root class="max-w-xl mx-auto">
    <Card.Header>
      <Card.Title>Edit: {$user.username}</Card.Title>
    </Card.Header>
    <Card.Content>
      <form on:submit|preventDefault={updateProfile} class="space-y-4">
        <div class="flex flex-col space-y-1">
          <Label for="firstName">First Name:</Label>
          <Input id="firstName" bind:value={$user.first_name} type="text" required />
        </div>

        <div class="flex flex-col space-y-1">
          <Label for="lastName">Last Name:</Label>
          <Input id="lastName" bind:value={$user.last_name} type="text" required />
        </div>

        <div class="flex flex-col space-y-1">
          <Label for="trusts">Trust:</Label>
          <Select.Root bind:value={$user.trust} required>
            <Select.Trigger id="trusts">
              <Select.Value placeholder="Please select a trust" />
            </Select.Trigger>
            <Select.Content>
              {#each $trusts as trust}
                <Select.Item value={trust.id}>{trust.name}</Select.Item>
              {/each}
            </Select.Content>
          </Select.Root>
        </div>

        <div class="flex flex-col space-y-1">
          <Label for="roles">Title (hold ctrl to select multiple| message the rcr for permission to other roles):</Label>
          <Select.Root id="roles" multiple bind:value={$user.roles}>
            <Select.Trigger>
              <Select.Value placeholder="Select roles" />
            </Select.Trigger>
            <Select.Content>
              {#each $roles as role}
                <Select.Item value={role.id} disabled={!$allowedRoles.includes(role.name)}>
                  {role.name}
                </Select.Item>
              {/each}
            </Select.Content>
          </Select.Root>
        </div>

        <div class="flex justify-end space-x-4">
          <Button type="button" variant="outline" on:click={() => goto('/panel')}>Go to Panel</Button>
          <Button type="submit">Update</Button>
        </div>
      </form>
    </Card.Content>
  </Card.Root>
{/if}
