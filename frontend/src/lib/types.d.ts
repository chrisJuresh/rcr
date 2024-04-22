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
        post: operations["3a52d838_controller_obtain_token"];
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
        post: operations["cbc31912_controller_refresh_token"];
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
        post: operations["e373c1f9_controller_verify_token"];
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
    "/api/users/roles/": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Roles */
        get: operations["users_api_get_roles"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/users/trust": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Trust */
        get: operations["users_api_get_trust"];
        put?: never;
        post?: never;
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
    "/api/specialities/specialities/": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Specialities */
        get: operations["specialities_api_get_specialities"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/jds/jd/": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        put?: never;
        /** Create Jd */
        post: operations["jds_api_create_jd"];
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/jds/{jd_id}/": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Jd */
        get: operations["jds_api_get_jd"];
        /** Update Jd */
        put: operations["jds_api_update_jd"];
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/jds/panel": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Jd Panel */
        get: operations["jds_api_get_jd_panel"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/jds/ids": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Jd Ids */
        get: operations["jds_api_get_jd_ids"];
        put?: never;
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/jds/{jd_id}/checklist/": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Jd Checklist */
        get: operations["jds_api_get_jd_checklist"];
        /** Update Jd Checklist */
        put: operations["jds_api_update_jd_checklist"];
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/jds/{jd_id}/{state}/": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        get?: never;
        /** Update Jd State */
        put: operations["jds_api_update_jd_state"];
        post?: never;
        delete?: never;
        options?: never;
        head?: never;
        patch?: never;
        trace?: never;
    };
    "/api/jds/reviewers/{jd_id}": {
        parameters: {
            query?: never;
            header?: never;
            path?: never;
            cookie?: never;
        };
        /** Get Reviewers */
        get: operations["jds_api_get_reviewers"];
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
        /** RegionOut */
        RegionOut: {
            /** Name */
            name: string;
        };
        /** SpecialitiesOut */
        SpecialitiesOut: {
            /** Specialities */
            specialities: components["schemas"]["SpecialityOut"][];
        };
        /** TrustOut */
        TrustOut: {
            /** Id */
            id: number;
            /** Name */
            name: string;
            region: components["schemas"]["RegionOut"];
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
            trust: components["schemas"]["TrustOut"] | null;
            /** Approved Trusts */
            approved_trusts: string[] | null;
            /** Roles */
            roles: string[] | null;
            /** Approved Roles */
            approved_roles: string[] | null;
            /** Consultant Type */
            consultant_type: string | null;
            /** Specialities */
            specialities: components["schemas"]["SpecialitiesOut"][] | null;
            /** Updated */
            updated: string | null;
        };
        /** UserProfileIn */
        UserProfileIn: {
            /** Title */
            title?: string | null;
            /** First Name */
            first_name?: string | null;
            /** Last Name */
            last_name?: string | null;
            /** Trust */
            trust?: number | null;
            /** Roles */
            roles?: number[] | null;
            /** Consultant Type */
            consultant_type?: string | null;
            /** Specialities */
            specialities?: number[] | null;
        };
        /** UserRolesOut */
        UserRolesOut: {
            /** Roles */
            roles: string[];
            /** Requested Roles */
            requested_roles: string[];
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
        /** TrustsOut */
        TrustsOut: {
            /** Trusts */
            trusts: components["schemas"]["TrustOut"][];
        };
        /** SpecialityOut */
        SpecialityOut: {
            /** Id */
            id: number;
            /** Name */
            name: string;
            /** Consultant Type */
            consultant_type: string;
        };
        /** JDID */
        JDID: {
            /** Id */
            id: number;
        };
        /** JDIn */
        JDIn: {
            /** Consultant Type */
            consultant_type: string;
            /** Primary Specialities */
            primary_specialities: number[];
            /** Sub Specialities */
            sub_specialities: number[] | null;
        };
        /** JDOut */
        JDOut: {
            /** Id */
            id: number;
            /** File */
            file: string;
            /** Trust */
            trust: string;
            /** Status */
            status: string;
            /** Reviewer */
            reviewer: string | null;
            /** Date */
            date: string;
            /** Consultant Type */
            consultant_type: string;
            /** Primary Specialities */
            primary_specialities: string[];
            /** Sub Specialities */
            sub_specialities: string[] | null;
            /** State Diagram */
            state_diagram: string | null;
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
            /** Status */
            status: string;
            /** Date */
            date: string;
            /** Consultant Type */
            consultant_type: string;
            /** Primary Specialties */
            primary_specialties: string[];
            /** Sub Specialties */
            sub_specialties: string[] | null;
        };
        /** JDIDsOut */
        JDIDsOut: {
            /** Ids */
            ids: number[];
        };
        /** AnswerOut */
        AnswerOut: {
            /** Id */
            id: number;
            /** Present */
            present: boolean;
            /** Page Numbers */
            page_numbers: string | null;
            /** Description */
            description: string | null;
            /** Rcr Comments */
            rcr_comments: string | null;
            /** Rsa Comments */
            rsa_comments: string | null;
        };
        /** ChecklistItemOut */
        ChecklistItemOut: {
            question: components["schemas"]["QuestionOut"];
            answer: components["schemas"]["AnswerOut"];
        };
        /** JDChecklistOut */
        JDChecklistOut: {
            /** Jd Id */
            jd_id: number;
            /** Requirements Met */
            requirements_met: boolean;
            /** Checklist */
            checklist: components["schemas"]["ChecklistItemOut"][];
        };
        /** QuestionOut */
        QuestionOut: {
            /** Id */
            id: number;
            /** Text */
            text: string;
            /** Required */
            required: boolean;
        };
        /** AnswerIn */
        AnswerIn: {
            /** Id */
            id: number;
            /** Present */
            present: boolean;
            /** Page Numbers */
            page_numbers: string | null;
            /** Description */
            description: string | null;
            /** Rcr Comments */
            rcr_comments?: string | null;
            /** Rsa Comments */
            rsa_comments?: string | null;
        };
        /** ChecklistItemIn */
        ChecklistItemIn: {
            question: components["schemas"]["QuestionIn"];
            answer: components["schemas"]["AnswerIn"];
        };
        /** JDChecklistIn */
        JDChecklistIn: {
            /** Jd Id */
            jd_id: number;
            /** Requirements Met */
            requirements_met: boolean;
            /** Checklist */
            checklist: components["schemas"]["ChecklistItemIn"][];
        };
        /** QuestionIn */
        QuestionIn: {
            /** Id */
            id: number;
            /** Text */
            text: string;
            /** Required */
            required: boolean;
        };
        /** ReviewerOut */
        ReviewerOut: {
            /** Id */
            id: number;
            /** Name */
            name: string;
            /** Same Region */
            same_region: string;
            /** Trusts */
            trusts: components["schemas"]["TrustOut"][];
        };
        /** ReviewersOut */
        ReviewersOut: {
            /** Reviewers */
            reviewers: components["schemas"]["ReviewerOut"][];
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
    "3a52d838_controller_obtain_token": {
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
    cbc31912_controller_refresh_token: {
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
    e373c1f9_controller_verify_token: {
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
    users_api_get_roles: {
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
                    "application/json": components["schemas"]["UserRolesOut"];
                };
            };
        };
    };
    users_api_get_trust: {
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
                    "application/json": components["schemas"]["TrustOut"];
                };
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
    specialities_api_get_specialities: {
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
                    "application/json": components["schemas"]["SpecialitiesOut"];
                };
            };
        };
    };
    jds_api_create_jd: {
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
                    jd: components["schemas"]["JDIn"];
                };
            };
        };
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["JDID"];
                };
            };
        };
    };
    jds_api_get_jd: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                jd_id: number;
            };
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
                    "application/json": components["schemas"]["JDOut"];
                };
            };
        };
    };
    jds_api_update_jd: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                jd_id: number;
            };
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
                    jd: components["schemas"]["JDIn"];
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
    jds_api_get_jd_panel: {
        parameters: {
            query?: {
                panel?: string | null;
            };
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
    jds_api_get_jd_ids: {
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
                    "application/json": components["schemas"]["JDIDsOut"];
                };
            };
        };
    };
    jds_api_get_jd_checklist: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                jd_id: number;
            };
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
                    "application/json": components["schemas"]["JDChecklistOut"];
                };
            };
        };
    };
    jds_api_update_jd_checklist: {
        parameters: {
            query?: {
                panel?: string | null;
            };
            header?: never;
            path: {
                jd_id: number;
            };
            cookie?: never;
        };
        requestBody: {
            content: {
                "application/json": components["schemas"]["JDChecklistIn"];
            };
        };
        responses: {
            /** @description OK */
            200: {
                headers: {
                    [name: string]: unknown;
                };
                content: {
                    "application/json": components["schemas"]["JDChecklistOut"];
                };
            };
        };
    };
    jds_api_update_jd_state: {
        parameters: {
            query?: {
                reviewer?: string | null;
            };
            header?: never;
            path: {
                jd_id: number;
                state: string;
            };
            cookie?: never;
        };
        requestBody?: never;
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
    jds_api_get_reviewers: {
        parameters: {
            query?: never;
            header?: never;
            path: {
                jd_id: number;
            };
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
                    "application/json": components["schemas"]["ReviewersOut"];
                };
            };
        };
    };
}
