<script lang="ts">
    import * as Form from "$lib/components/ui/form";
    import * as Card from "$lib/components/ui/card";
    import * as Tabs from "$lib/components/ui/tabs";
    import { formSchema } from "./schema"; 
    import type { FormSchema } from "./schema"; 
    import type { SuperValidated } from "sveltekit-superforms";
    import axios from 'axios';
    import { goto } from '$app/navigation';

    export let form: SuperValidated<FormSchema>;

    let selectedTab = 'login'; 

    async function handleSubmit(event, action) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const formObject = Object.fromEntries(formData);

        try {
            const url = `http://localhost:8000/${action}/`;
            const response = await axios.post(url, formObject);
            console.log(response.data);
            goto('/profile');
        } catch (error) {
            console.error('Error submitting form:', error);
        }
    }
</script>

<div class="flex justify-center items-center min-h-screen">
    <Card.Root class="auth-page w-[400px]">
        <Card.Header>
            <Card.Title>Login or Register</Card.Title>
            <Card.Description>Access your account or create a new one.</Card.Description>
        </Card.Header>
        <Card.Content>
            <Tabs.Root bind:value={selectedTab} class="w-full">
                <Tabs.List>
                    <Tabs.Trigger value="login">Login</Tabs.Trigger>
                    <Tabs.Trigger value="register">Register</Tabs.Trigger>
                </Tabs.List>
                <Tabs.Content value="login">
                    <Form.Root method="POST" {form} schema={formSchema} let:config class="flex flex-col space-y-4">
                        <form on:submit={(event) => handleSubmit(event, 'login')}>
                            <Form.Item>
                                <Form.Field {config} name="username">
                                    <Form.Label>Email</Form.Label>
                                    <Form.Input type="text" required />
                                    <Form.Validation />
                                </Form.Field>
                            </Form.Item>
                            <Form.Item>
                                <Form.Field {config} name="password">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Input type="password" required />
                                    <Form.Validation />
                                </Form.Field>
                            </Form.Item>
                            <button type="submit" class="form-button">Login</button>
                        </form>
                    </Form.Root>
                </Tabs.Content>
                <Tabs.Content value="register">
                    <Form.Root method="POST" {form} schema={formSchema} let:config class="flex flex-col space-y-4">
                        <form on:submit={(event) => handleSubmit(event, 'register')}>
                            <Form.Item>
                                <Form.Field {config} name="username">
                                    <Form.Label>Email</Form.Label>
                                    <Form.Input type="text" required />
                                    <Form.Validation />
                                </Form.Field>
                            </Form.Item>
                            <Form.Item>
                                <Form.Field {config} name="password">
                                    <Form.Label>Password</Form.Label>
                                    <Form.Input type="password" required />
                                    <Form.Validation />
                                </Form.Field>
                            </Form.Item>
                            <button type="submit" class="form-button">Register</button>
                        </form>
                    </Form.Root>
                </Tabs.Content>
            </Tabs.Root>
        </Card.Content>
    </Card.Root>
</div>