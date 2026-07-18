import type { Method } from 'axios';
import type { components } from './types';

type PanelJD = components['schemas']['PanelJD'];
type JDOut = components['schemas']['JDOut'];
type PanelAAC = components['schemas']['PanelAAC'];

const trust = {
	id: 1,
	name: 'Northbridge University Hospitals NHS Trust',
	region: { name: 'London' }
};

const trusts = [
	trust,
	{ id: 2, name: 'West Mercia Teaching Hospitals NHS Trust', region: { name: 'West Midlands' } },
	{ id: 3, name: 'Severn Coast NHS Foundation Trust', region: { name: 'South West' } },
	{ id: 4, name: 'Calder & Pennine Hospitals NHS Trust', region: { name: 'North West' } },
	{ id: 5, name: 'Eastborough University Hospitals NHS Trust', region: { name: 'East of England' } }
];

const roles = [
	{ id: 1, name: 'Trust Employee' },
	{ id: 2, name: 'Reviewer' },
	{ id: 3, name: 'RCR Employee' },
	{ id: 4, name: 'Representative' }
];

const specialities = [
	{ id: 1, name: 'General radiology', consultant_type: 'RADIOLOGY' },
	{ id: 2, name: 'Interventional radiology', consultant_type: 'RADIOLOGY' },
	{ id: 3, name: 'Neuroradiology', consultant_type: 'RADIOLOGY' },
	{ id: 4, name: 'Breast imaging', consultant_type: 'RADIOLOGY' },
	{ id: 5, name: 'Gastrointestinal imaging', consultant_type: 'RADIOLOGY' },
	{ id: 6, name: 'Musculoskeletal imaging', consultant_type: 'RADIOLOGY' },
	{ id: 7, name: 'Paediatric radiology', consultant_type: 'RADIOLOGY' },
	{ id: 8, name: 'Lung cancer', consultant_type: 'ONCOLOGY' },
	{ id: 9, name: 'Breast cancer', consultant_type: 'ONCOLOGY' },
	{ id: 10, name: 'Urological cancer', consultant_type: 'ONCOLOGY' },
	{ id: 11, name: 'Head and neck cancer', consultant_type: 'ONCOLOGY' },
	{ id: 12, name: 'Acute oncology', consultant_type: 'ONCOLOGY' }
];

const jds: PanelJD[] = [
	{
		id: 4102,
		consultant_type: 'Radiology',
		primary_specialties: ['Interventional radiology'],
		sub_specialties: ['Vascular', 'Emergency imaging'],
		status: 'Trust Submitted',
		date: '26-07-18 09:42'
	},
	{
		id: 4103,
		consultant_type: 'Oncology',
		primary_specialties: ['Breast cancer'],
		sub_specialties: ['Acute oncology'],
		status: 'RCR Approved',
		date: '26-07-17 16:18'
	},
	{
		id: 4104,
		consultant_type: 'Radiology',
		primary_specialties: ['Neuroradiology'],
		sub_specialties: ['Head and neck'],
		status: 'RSA Rejected',
		date: '26-07-17 13:05'
	},
	{
		id: 4105,
		consultant_type: 'Radiology',
		primary_specialties: ['Breast imaging'],
		sub_specialties: ['Screening'],
		status: 'RSA Approved',
		date: '26-07-16 11:24'
	},
	{
		id: 4106,
		consultant_type: 'Oncology',
		primary_specialties: ['Lung cancer'],
		sub_specialties: ['Stereotactic radiotherapy'],
		status: 'Trust Submitted',
		date: '26-07-16 09:10'
	},
	{
		id: 4107,
		consultant_type: 'Radiology',
		primary_specialties: ['Paediatric radiology'],
		sub_specialties: ['Paediatric neuroradiology'],
		status: 'Draft',
		date: '26-07-15 15:31'
	},
	{
		id: 4108,
		consultant_type: 'Radiology',
		primary_specialties: ['Gastrointestinal imaging'],
		sub_specialties: ['Oncological imaging', 'Ultrasound'],
		status: 'RSA Approved',
		date: '26-07-14 17:02'
	},
	{
		id: 4109,
		consultant_type: 'Oncology',
		primary_specialties: ['Urological cancer'],
		sub_specialties: ['Brachytherapy'],
		status: 'Trust Submitted',
		date: '26-07-14 10:46'
	},
	{
		id: 4110,
		consultant_type: 'Radiology',
		primary_specialties: ['Musculoskeletal imaging'],
		sub_specialties: ['Sports imaging'],
		status: 'RCR Approved',
		date: '26-07-13 14:22'
	},
	{
		id: 4111,
		consultant_type: 'Oncology',
		primary_specialties: ['Head and neck cancer'],
		sub_specialties: ['Thyroid cancer'],
		status: 'RSA Approved',
		date: '26-07-11 12:08'
	},
	{
		id: 4112,
		consultant_type: 'Radiology',
		primary_specialties: ['General radiology'],
		sub_specialties: ['Chest', 'Cardiac'],
		status: 'Draft',
		date: '26-07-10 08:54'
	},
	{
		id: 4113,
		consultant_type: 'Oncology',
		primary_specialties: ['Acute oncology'],
		sub_specialties: [],
		status: 'Trust Amended',
		date: '26-07-09 15:47'
	}
];

const jdTrusts = [trusts[0].name, trusts[1].name, trusts[2].name, trusts[3].name, trusts[4].name];

const jdDetails = Object.fromEntries(
	jds.map((jd, index) => [
		jd.id,
		{
			id: jd.id,
			file: `/mock/job-description-${jd.id}.pdf`,
			trust: jdTrusts[index % jdTrusts.length],
			status: jd.status,
			reviewer: ['Dr Aisha Rahman', 'Dr Oliver Grant', 'Dr Priya Shah'][index % 3],
			date: jd.date,
			consultant_type: jd.consultant_type,
			primary_specialities: jd.primary_specialties,
			sub_specialities: jd.sub_specialties,
			state_diagram: null
		} satisfies JDOut
	])
) as Record<number, JDOut>;

const checklistQuestions = [
	'Does the job description clearly state the principal duties and responsibilities?',
	'Is the proposed weekly timetable included and internally consistent?',
	'Are programmed activities and supporting professional activities clearly identified?',
	'Are on-call commitments, frequency and compensatory arrangements described?',
	'Are the facilities, equipment and supporting staff appropriate for the post?',
	'Are teaching, training, research and continuing professional development addressed?',
	'Does the person specification align with the duties of the post?',
	'Are the clinical governance and accountability arrangements clear?'
];

const aacs: PanelAAC[] = [
	{
		id: 31,
		status: 'Representative confirmed',
		date: '2026-07-24',
		consultant_type: 'Radiology',
		primary_specialties: ['Breast imaging'],
		sub_specialties: ['Screening']
	},
	{
		id: 32,
		status: 'Invitation sent',
		date: '2026-07-29',
		consultant_type: 'Radiology',
		primary_specialties: ['Gastrointestinal imaging'],
		sub_specialties: ['Oncological imaging']
	},
	{
		id: 33,
		status: 'Submitted',
		date: '2026-08-06',
		consultant_type: 'Oncology',
		primary_specialties: ['Head and neck cancer'],
		sub_specialties: ['Thyroid cancer']
	}
];

function getPanelJDs(panel: string | undefined) {
	if (panel === 'AAC') return jds.filter(({ status }) => status === 'RSA Approved');
	if (panel === 'Edit') {
		return jds.filter(({ status }) => ['Draft', 'RSA Rejected', 'Trust Amended'].includes(status));
	}
	if (panel === 'Review') {
		return jds.filter(({ status }) =>
			['Trust Submitted', 'RCR Approved', 'Trust Amended'].includes(status)
		);
	}
	return jds;
}

function getChecklist(jdId: number) {
	return {
		jd_id: jdId,
		requirements_met: jdDetails[jdId]?.status === 'RSA Approved',
		checklist: checklistQuestions.map((text, index) => ({
			question: { id: index + 1, text, required: index < 5 },
			answer: {
				id: jdId * 100 + index,
				present: index !== 4,
				page_numbers: index === 4 ? '' : `${index + 2}${index === 1 ? '-4' : ''}`,
				description:
					index === 4
						? 'The equipment section needs one additional sentence.'
						: 'Evidence located in the submitted job description.',
				rcr_comments:
					index === 4 ? 'Please confirm access to cross-sectional imaging workstations.' : '',
				rsa_comments: index === 3 ? 'On-call arrangements are appropriate for this post.' : ''
			}
		}))
	};
}

export function getMockApiResponse<T>(
	method: Method,
	endpoint: string,
	data: unknown,
	params: Record<string, unknown> = {}
): T {
	if (endpoint === '/token/verify') {
		const token = (data as { token?: string } | undefined)?.token;
		if (token !== 'demo-access-token') throw new Error('Invalid demo token');
		return {} as T;
	}
	if (endpoint === '/token/pair') {
		return { refresh: 'demo-refresh-token', access: 'demo-access-token' } as T;
	}
	if (endpoint === '/users/register-unauthenticated') return {} as T;
	if (endpoint === '/users/register-authenticate') {
		return {
			message: 'Demo account verified',
			refresh: 'demo-refresh-token',
			access: 'demo-access-token'
		} as T;
	}
	if (endpoint === '/users/roles/') {
		return {
			roles: ['Trust Employee', 'Reviewer', 'RCR Employee', 'Representative'],
			requested_roles: []
		} as T;
	}
	if (endpoint === '/roles/roles/') return { roles } as T;
	if (endpoint === '/trusts/trusts/') return { trusts } as T;
	if (endpoint === '/specialities/specialities/') return { specialities } as T;
	if (endpoint === '/users/profile/') {
		return {
			email: 'demo.user@example.test',
			title: 'Dr',
			first_name: 'Alex',
			last_name: 'Morgan',
			trust,
			approved_trusts: [trust.name],
			roles: ['Trust Employee', 'Reviewer', 'RCR Employee', 'Representative'],
			approved_roles: ['Trust Employee', 'Reviewer', 'RCR Employee', 'Representative'],
			consultant_type: 'RADIOLOGY',
			specialities: specialities.slice(0, 4),
			updated: '18-07-26 09:42'
		} as T;
	}
	if (endpoint === '/users/trust') return trust as T;
	if (endpoint === '/jds/panel')
		return { jds: getPanelJDs(params.panel as string | undefined) } as T;
	if (endpoint === '/jds/ids') return { ids: jds.map(({ id }) => id) } as T;

	const jdChecklistMatch = endpoint.match(/^\/jds\/(\d+)\/checklist\/$/);
	if (jdChecklistMatch) return getChecklist(Number(jdChecklistMatch[1])) as T;

	const jdMatch = endpoint.match(/^\/jds\/(\d+)\/$/);
	if (jdMatch) return (jdDetails[Number(jdMatch[1])] || jdDetails[jds[0].id]) as T;

	const reviewersMatch = endpoint.match(/^\/users\/reviewers\/(\d+)$/);
	if (reviewersMatch) {
		return {
			reviewers: [
				{
					id: 101,
					name: 'Dr Aisha Rahman',
					same_region: 'Same region',
					trusts: [trusts[0], trusts[4]]
				},
				{ id: 102, name: 'Dr Oliver Grant', same_region: 'Same region', trusts: [trusts[1]] },
				{
					id: 103,
					name: 'Dr Priya Shah',
					same_region: 'Other region',
					trusts: [trusts[2], trusts[3]]
				}
			]
		} as T;
	}

	if (endpoint === '/aacs/panel/') return { aacs } as T;
	if (endpoint === '/aacs/ids/') return { ids: aacs.map(({ id }) => id) } as T;

	const aacMatch = endpoint.match(/^\/aacs\/(\d+)\/$/);
	if (aacMatch) {
		const id = Number(aacMatch[1]);
		const panel = aacs.find((item) => item.id === id) || aacs[0];
		return {
			id: panel.id,
			date: panel.date,
			trust: trust.name,
			consultant_type: panel.consultant_type,
			status: panel.status,
			jds: jds
				.filter(({ status }) => status === 'RSA Approved')
				.slice(0, 2)
				.map((jd) => ({
					id: jd.id,
					file: `/mock/job-description-${jd.id}.pdf`,
					primary_specialities: jd.primary_specialties,
					sub_specialities: jd.sub_specialties || []
				}))
		} as T;
	}

	const repsMatch = endpoint.match(/^\/users\/reps\/(\d+)\/$/);
	if (repsMatch) {
		return {
			reps: [
				{
					id: 201,
					consultant_type: 'Radiology',
					primary_specialties: ['Breast imaging'],
					status: 'Available',
					date: '2026-07-24',
					selected: false
				},
				{
					id: 202,
					consultant_type: 'Radiology',
					primary_specialties: ['General radiology'],
					status: 'Available',
					date: '2026-07-24',
					selected: false
				},
				{
					id: 203,
					consultant_type: 'Radiology',
					primary_specialties: ['Oncological imaging'],
					status: 'Invited',
					date: '2026-07-24',
					selected: true
				}
			]
		} as T;
	}

	if (method === 'POST' && endpoint === '/jds/jd/') return { id: 4114 } as T;
	if (method === 'PUT' || method === 'POST') return (data || {}) as T;

	throw new Error(`No mock response configured for ${method} ${endpoint}`);
}
