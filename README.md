# This is my Dissertation Project.

[View the report](report/report.pdf)

I recieved 92.7% and won the Electronic Engineering and Computer Science Final Year Project Prize for Outstanding Achievement

The following installation guide assumes you are running Linux. It will run fine on Windows too but you may have to make some adaptations. Notably with entering the virtual environment.

# Installation

## Django

Install Python (distro dependant)
```
https://www.python.org/
```

Enter directory
```bash
cd rcr/backend
```

Create and enter a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Migrate database
```bash
python manage.py makemigrations
```
## SvelteKit

Install npm (distro dependant)
```bash
https://www.npmjs.com/
```

Enter directory (`cd ../../` if you are still in backend)
```bash
cd rcr/frontend
```
Install dependencies
```bash
npm install
```

# Usage

I recomend running Django first to generate the types for SvelteKit
```bash
# rcr/backend/
python manage.py runserver
```
```bash
# rcr/frontend
npm run dev
```

# Deployment

The public portfolio deployment is a self-contained SvelteKit demonstration using clearly labelled synthetic data. The original Django application remains in `backend/` as the dissertation implementation, but it is not required for the public demo.

Vercel should be configured with:

```text
Framework preset: SvelteKit
Root directory: frontend
Build command: npm run build
Output directory: leave at the framework default
```

The frontend uses Vercel's supported SvelteKit adapter. For local development:

```bash
cd frontend
npm install
npm run dev
```

The optional legacy authenticated routes can still connect to Django by setting `PUBLIC_API_BASE_URL` to the API base URL. Email verification additionally requires `POSTMARK_SERVER_TOKEN`.

The original deployment architecture used:

```
https://kit.svelte.dev/docs/adapter-node 
nginx with the rcr config provided
gunicorn
namecheap
certbot
```

# Postmark

You will need to add your own api key in the SvelteKit code.

