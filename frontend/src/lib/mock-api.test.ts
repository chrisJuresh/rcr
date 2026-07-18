import { describe, expect, it } from 'vitest';
import { getMockApiResponse } from './mock-api';
import type { components } from './types';

describe('mock API', () => {
	it('requires the explicit demo session token', () => {
		expect(() => getMockApiResponse('POST', '/token/verify', {}, {})).toThrow();
		expect(() =>
			getMockApiResponse('POST', '/token/verify', { token: 'demo-access-token' }, {})
		).not.toThrow();
	});

	it('provides populated JD and AAC panels', () => {
		const jdPanel = getMockApiResponse<components['schemas']['JDPanel']>(
			'GET',
			'/jds/panel',
			{},
			{ panel: 'Panel' }
		);
		const aacPanel = getMockApiResponse<components['schemas']['AACPanel']>(
			'GET',
			'/aacs/panel/',
			{},
			{}
		);

		expect(jdPanel.jds.length).toBeGreaterThanOrEqual(10);
		expect(aacPanel.aacs.length).toBeGreaterThanOrEqual(3);
	});
});
