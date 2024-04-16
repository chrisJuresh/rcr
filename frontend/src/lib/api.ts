import { getData, postData, putData } from './api-utils'; 
import type { components } from './types.d.ts';

export const getJDPanel = async (token: string, params?: Record<string, any>) => {
    return getData<components['schemas']['JDPanel']>('/jds/panel', { token, params }).then(data => data.jds);
}

export const getJD = async (jd_id: string, token: string) => {
	return getData<components['schemas']['JDOut']>(`/jds/${jd_id}`, { token });
};

export const getJDIds = async (token: string) => {
	return getData<components['schemas']['JDIDsOut']>('/jds/ids', { token });
};

export const getJDChecklist = async (jd_id: string, token: string) => {
	return getData<components['schemas']['JDChecklistOut']>(`/jds/${jd_id}/checklist`, { token });
};

export const getUserRoles = async (token: string) => {
    return getData<components['schemas']['RolesOut']>('/users/roles', { token });
}

export const getRoles = async () => {
    return getData<components['schemas']['RolesOut']>('/roles/roles').then(data => data.roles);
}

export const getTrusts = async () => {
    return getData<components['schemas']['TrustsOut']>('/trusts/trusts').then(data => data.trusts);
}

export const getSpecialities = async () => {
    return getData<components['schemas']['SpecialitiesOut']>('/specialities/specialities').then(data => data.specialities);
}

export const getUserProfile = async (token: string) => {
    return getData<components['schemas']['UserProfileOut']>('/users/profile', { token });
}

export const getUserTrust = async (token: string) => {
    return getData<components['schemas']['TrustOut']>('/users/trust', { token });
}

export const verifyUser = async (token: string) => {
    return postData('/token/verify', { token });
}

export const loginUser = async (data: any)  => {
    return postData('/token/pair', data);
}

export const registerUnauthenticatedUser = async (data: any) => {
    return postData('/users/register-unauthenticated', data);
}

export const registerAuthenticateUser = async (data: any) => {
    return postData('/users/register-authenticate', data);
}

export const putUserProfile = async (data: any, token: string,) => {
    return putData('/users/profile/', data, { token });
}

export const postJD = async (data: any, token: string,) => {
    return postData<components['schemas']['JDID']>('/jds/jd/', data, { token });
}

export const putJDChecklist = async (jd_id: string, data: any, token: string,) => {
    return putData(`/jds/${jd_id}/checklist/`, data, { token });
}

export const submitJD = async (jd_id: string, token: string) => {
    return putData(`/jds/${jd_id}/submit/`, {}, { token });
}