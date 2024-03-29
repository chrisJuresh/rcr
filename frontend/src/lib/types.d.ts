/**
 * This file was auto-generated by openapi-typescript.
 * Do not make direct changes to the file.
 */

export interface paths {
    "/api/token/pair": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /** Obtain Token */
        post: operations["243aa61a_controller_obtain_token"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/token/refresh": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /** Refresh Token */
        post: operations["7395fb1e_controller_refresh_token"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/token/verify": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /** Verify Token */
        post: operations["ed8db929_controller_verify_token"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/users/register-unauthenticated": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /** Register Unauthenticated */
        post: operations["users_api_register_unauthenticated"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/users/register-authenticate": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /** Register Authenticate */
        post: operations["users_api_register_authenticate"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/users/profile/": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Profile */
        get: operations["users_api_get_profile"];
        /** Update Profile */
        put: operations["users_api_update_profile"];
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/users/jds/": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Jd Panel */
        get: operations["users_api_get_jd_panel"];
        put?: never;
        /** Upload Jd */
        post: operations["users_api_upload_jd"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/roles/roles/": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Roles */
        get: operations["roles_api_get_roles"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/trusts/trusts/": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Trusts */
        get: operations["trusts_api_get_trusts"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
}
export type webhooks = Record<string, never>;
export interface components {
    schemas: {
        /** TokenObtainPairOutputSchema */
        TokenObtainPairOutputSchema: {
            /** Email Address */
            email: string;
            /** Refresh */
            refresh: string;
            /** Access */
            access: string;
        };
        /** TokenObtainPairInputSchema */
        TokenObtainPairInputSchema: {
            /** Password */
            password: string;
            /** Email Address */
            email: string;
        };
        /** TokenRefreshOutputSchema */
        TokenRefreshOutputSchema: {
            /** Refresh */
            refresh: string;
            /** Access */
            access: string | null;
        };
        /** TokenRefreshInputSchema */
        TokenRefreshInputSchema: {
            /** Refresh */
            refresh: string;
        };
        /** Schema */
        Schema: Record<string, never>;
        /** TokenVerifyInputSchema */
        TokenVerifyInputSchema: {
            /** Token */
            token: string;
        };
        /** UnauthenticatedUserIn */
        UnauthenticatedUserIn: {
            /** Email */
            email: string;
            /** Password */
            password: string;
            /** Token */
            token: string;
        };
        /** TokenIn */
        TokenIn: {
            /** Token */
            token: string;
        };
        /** UserApprovedRolesOut */
        UserApprovedRolesOut: {
            /** Name */
            name: string;
        };
        /** UserProfileOut */
        UserProfileOut: {
            /** Email */
            email: string;
            /** Title */
            title: string | null;
            /** First Name */
            first_name: string | null;
            /** Last Name */
            last_name: string | null;
            /** Trust */
            trust: string | null;
            /** Roles */
            roles: components["schemas"]["UserRolesOut"][] | null;
            /** Approved Roles */
            approved_roles: components["schemas"]["UserApprovedRolesOut"][] | null;
        };
        /** UserRolesOut */
        UserRolesOut: {
            /** Name */
            name: string;
        };
        /** UserProfileIn */
        UserProfileIn: {
            /** Title */
            title: string | null;
            /** First Name */
            first_name: string | null;
            /** Last Name */
            last_name: string | null;
            /** Trust */
            trust: number | null;
            /** Roles */
            roles: number[] | null;
        };
        /** JDPanel */
        JDPanel: {
            /** Jds */
            jds: components["schemas"]["PanelJD"][];
        };
        /** PanelJD */
        PanelJD: {
            /** Id */
            id: number;
            /** Consultant Type */
            consultant_type: string;
            /** Primary Specialties */
            primary_specialties: string[];
            /** Sub Specialties */
            sub_specialties: string[] | null;
            /** Date */
            date: string;
        };
        /** JDCreate */
        JDCreate: {
            /** Trust */
            trust: number;
            /** Consultant Type */
            consultant_type: string;
            /** Primary Specialities */
            primary_specialities: number[];
            /**
             * Sub Specialities
             * @default []
             */
            sub_specialities: number[];
            /** Creator */
            creator: number;
        };
        /** RoleOut */
        RoleOut: {
            /** Id */
            id: number;
            /** Name */
            name: string;
        };
        /** RolesOut */
        RolesOut: {
            /** Roles */
            roles: components["schemas"]["RoleOut"][];
        };
        /** RegionOut */
        RegionOut: {
            /** Name */
            name: string;
        };
        /** TrustOut */
        TrustOut: {
            /** Id */
            id: number;
            /** Name */
            name: string;
            region: components["schemas"]["RegionOut"];
        };
        /** TrustsOut */
        TrustsOut: {
            /** Trusts */
            trusts: components["schemas"]["TrustOut"][];
        };
    };
    responses: never;
    parameters: never;
    requestBodies: never;
    headers: never;
    pathItems: never;
}
export type $defs = Record<string, never>;
export interface operations {
    "243aa61a_controller_obtain_token": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["TokenObtainPairInputSchema"];
            };
        };
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["TokenObtainPairOutputSchema"];
                };
            };
        };
    };
    "7395fb1e_controller_refresh_token": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["TokenRefreshInputSchema"];
            };
        };
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["TokenRefreshOutputSchema"];
                };
            };
        };
    };
    ed8db929_controller_verify_token: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["TokenVerifyInputSchema"];
            };
        };
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["Schema"];
                };
            };
        };
    };
    users_api_register_unauthenticated: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["UnauthenticatedUserIn"];
            };
        };
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content?: never;
            };
        };
    };
    users_api_register_authenticate: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["TokenIn"];
            };
        };
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content?: never;
            };
        };
    };
    users_api_get_profile: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["UserProfileOut"];
                };
            };
        };
    };
    users_api_update_profile: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["UserProfileIn"];
            };
        };
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["UserProfileOut"];
                };
            };
        };
    };
    users_api_get_jd_panel: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["JDPanel"];
                };
            };
        };
    };
    users_api_upload_jd: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody: {
            content: {
                "multipart/form-data": {
                    /**
                     * File
                     * Format: binary
                     */
                    file: string;
                    jd: components["schemas"]["JDCreate"];
                };
            };
        };
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content?: never;
            };
        };
    };
    roles_api_get_roles: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["RolesOut"];
                };
            };
        };
    };
    trusts_api_get_trusts: {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        requestBody?: never;
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["TrustsOut"];
                };
            };
        };
    };
}
