<script lang="ts">
  import * as Form from "$lib/components/ui/form";
  import * as Select from "$lib/components/ui/select";
  import * as Card from "$lib/components/ui/card";
  import { Input } from "$lib/components/ui/input";
  import { formSchema, type FormSchema } from "./schema";
  import {
    type SuperValidated,
    type Infer,
    superForm,
  } from "sveltekit-superforms";
  import { zodClient } from "sveltekit-superforms/adapters";
 
  export let data: SuperValidated<Infer<FormSchema>>;
  export let user;
  export let roles;
 
  const form = superForm(data, {
    validators: zodClient(formSchema),
    dataType: 'json'
  });
 
  const { form: formData, enhance } = form;
 $: selectedTitle = $formData.title
    ? {
        label: $formData.title,
        value: $formData.title
      }
    : undefined;

$: selectedRoles = $formData.roles?.map((role) => ({ label: role.name, value: role.value }));

  function getUserRolesAsString(user) {
    return user.roles.map(role => role.name).join(', ');
  }

</script>
 

<div class="flex min-h-screen items-center justify-center">
  <Card.Root class="w-[600px]">
    <Card.Header>
      <Card.Title>Edit {user.email}</Card.Title>
      <Card.Description>Your email address is your unique identifier <br> These details must be correct as they will be tied to your JDs and/or AACs</Card.Description>
      </Card.Header>
      <Card.Content>
<form method="POST" use:enhance>
  <Form.Field {form} name="title">
    <Form.Control let:attrs>
      
      <Form.Label>Title</Form.Label>
<Select.Root
        selected={selectedTitle}
        onSelectedChange={(v) => {
          v && ($formData.title = v.value);
        }}
      >
        <Select.Trigger {...attrs}>
          <Select.Value placeholder={user.title ? user.title : 'Select a title'} />
        </Select.Trigger>
        <Select.Content>
          <Select.Item value="Mr" label="Mr" />
          <Select.Item value="Ms" label="Ms" />
          <Select.Item value="Mrs" label="Mrs" />
        </Select.Content>
      </Select.Root>
        <input hidden {...attrs} bind:value={$formData.title} placeholder={user.title}/>
    </Form.Control>
    <Form.FieldErrors />
  </Form.Field>
  
  <Form.Field {form} name="first_name">
    <Form.Control let:attrs>
      <Form.Label>First Name</Form.Label>
      <Input {...attrs} bind:value={$formData.first_name} placeholder={user.first_name ? user.first_name : 'First Name'}/>
    </Form.Control>
    <Form.FieldErrors />
  </Form.Field>
  
  <Form.Field {form} name="last_name">
    <Form.Control let:attrs>
      <Form.Label>Last Name</Form.Label>
      <Input {...attrs} bind:value={$formData.last_name} placeholder={user.last_name ? user.last_name : 'Last Name'}/>
    </Form.Control>
    <Form.FieldErrors />
  </Form.Field>

	<Form.Field {form} name="roles">
  <Form.Control let:attrs>
			<Form.Label>Roles</Form.Label>
			<Select.Root
				multiple
        selected={selectedRoles}

onSelectedChange={(s) => {
    if (s) {
        $formData.roles = s.map((selected) => {
            const role = roles.find((role) => role.id === selected.value);
            return {
                value: selected.value,
                name: role ? role.name : ''
            };
        });
    } else {
        $formData.roles = [];
    }
}}
			>
					<input name={attrs.name} hidden value={selectedRoles} />
<Select.Trigger {...attrs}> <!-- Adjusted height -->
  <Select.Value placeholder={getUserRolesAsString(user) ? getUserRolesAsString(user) : 'Select your roles'} />
</Select.Trigger>
				<Select.Content>
					{#each roles as {id, name}}
						<Select.Item value={id} label={name} />
					{/each}
				</Select.Content>
			</Select.Root>
			<Form.FieldErrors />
		</Form.Control>
  </Form.Field>

  <Form.Button>Update</Form.Button>
</form>
</Card.Content>
  </Card.Root>
</div>	