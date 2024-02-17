<script lang="ts">
    import * as Form from "$lib/components/ui/form";
    import * as Card from "$lib/components/ui/card";
    import * as Tabs from "$lib/components/ui/tabs";
    import { formSchema } from "./schema"; 
    import type { FormSchema } from "./schema"; 
    import type { SuperValidated } from "sveltekit-superforms";

    export let form: SuperValidated<FormSchema>;

</script>

<div class="flex justify-center items-center min-h-screen">
    <Card.Root class="auth-page w-[400px]">
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
                    <Form.Root action="?/login"  method="POST" {form} schema={formSchema} let:config class="flex flex-col space-y-4">
                                <Form.Field {config} name="username">
                            <Form.Item>
                                    <Form.Label>Email</Form.Label>
                                    <Form.Input type="text" required />
                                    <Form.Validation />
                            </Form.Item>
                                </Form.Field>
                                <Form.Field {config} name="password">
                            <Form.Item>
                                    <Form.Label>Password</Form.Label>
                                    <Form.Input type="password" required />
                                    <Form.Validation />
                            </Form.Item>
                                </Form.Field>
                            <Form.Button>Submit</Form.Button>
                    </Form.Root>
                </Tabs.Content>
                <Tabs.Content value="register">
                    <Form.Root action="?/register" method="POST" {form} schema={formSchema} let:config class="flex flex-col space-y-4">
                                <Form.Field {config} name="username">
                            <Form.Item>
                                    <Form.Label>Email</Form.Label>
                                    <Form.Input type="text" required />
                                    <Form.Validation />
                            </Form.Item>
                                </Form.Field>
                                <Form.Field {config} name="password">
                            <Form.Item>
                                    <Form.Label>Password</Form.Label>
                                    <Form.Input type="password" required />
                                    <Form.Validation />
                            </Form.Item>
                                </Form.Field>
                            <Form.Button>Submit</Form.Button>
                    </Form.Root>
                </Tabs.Content>
            </Tabs.Root>
        </Card.Content>
    </Card.Root>
</div>