# This is my Dissertation Project.

[View the report](report/report.pdf)

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
You will have to find instructions elsewhere if you plan on deploying this in build mode.

Here are the tools I used anyway:
```
https://kit.svelte.dev/docs/adapter-node 
nginx with the rcr config provided
gunicorn
namecheap
certbot
```

# Postmark

You will need to add your own api key in the SvelteKit code.

