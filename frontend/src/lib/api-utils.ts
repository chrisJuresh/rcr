import axios from 'axios';
import type { AxiosRequestConfig, Method } from 'axios';

const baseUrl = 'http://localhost:8000/api';

type ApiConfig = {
    token?: string;
    headers?: Record<string, string>;
};

function buildAxiosConfig(config: ApiConfig): AxiosRequestConfig {
    return {
        headers: {
            Authorization: `Bearer ${config.token}`,
            ...config.headers
        }
    };
}

async function makeRequest<T>(method: Method, endpoint: string, data: any = {}, config: ApiConfig = {}): Promise<T> {
    const fullUrl = `${baseUrl}${endpoint}`;
    const axiosConfig = buildAxiosConfig(config);

    try {
        const response = await axios.request<T>({
            url: fullUrl,
            method: method,
            data: method !== 'GET' ? data : undefined,
            ...axiosConfig
        });
        return response.data;
    } catch (error) {
        throw error;
    }
}

async function getData<T = any>(endpoint: string, config: ApiConfig = {}): Promise<T> {
    return makeRequest<T>('GET', endpoint, {}, config);
}

async function postData<T = any>(endpoint: string, data: any, config: ApiConfig = {}): Promise<T> {
    return makeRequest<T>('POST', endpoint, data, config);
}

async function putData<T = any>(endpoint: string, data: any, config: ApiConfig = {}): Promise<T> {
    return makeRequest<T>('PUT', endpoint, data, config);
}

export { getData, postData, putData};