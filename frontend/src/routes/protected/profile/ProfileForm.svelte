<script lang="ts">
  import * as Form from "$lib/components/ui/form";
  import { Input } from "$lib/components/ui/input";
  import { formSchema, type FormSchema } from "./schema";
  import {
    type SuperValidated,
    type Infer,
    superForm,
  } from "sveltekit-superforms";
  import { zodClient } from "sveltekit-superforms/adapters";
 
  export let data: SuperValidated<Infer<FormSchema>>;
  export let user
 
  const form = superForm(data, {
    validators: zodClient(formSchema),
    dataType: 'json'
  });
 
  const { form: formData, enhance } = form;

</script>
 

<div class="flex min-h-screen items-center justify-center">
<form method="POST" use:enhance>
  <Form.Field {form} name="title">
    <Form.Control let:attrs>
      <Form.Label>Title</Form.Label>
      <Input {...attrs} bind:value={$formData.title} placeholder={user.title}/>
    </Form.Control>
    <Form.FieldErrors />
  </Form.Field>
  
  <Form.Field {form} name="first_name">
    <Form.Control let:attrs>
      <Form.Label>First Name</Form.Label>
      <Input {...attrs} bind:value={$formData.first_name} placeholder={user.first_name}/>
    </Form.Control>
    <Form.FieldErrors />
  </Form.Field>
  
  <Form.Field {form} name="last_name">
    <Form.Control let:attrs>
      <Form.Label>Last Name</Form.Label>
      <Input {...attrs} bind:value={$formData.last_name} placeholder={user.last_name}/>
    </Form.Control>
    <Form.FieldErrors />
  </Form.Field>
  
  <Form.Button>Submit</Form.Button>
</form>
</div>	