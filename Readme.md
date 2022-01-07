# Django Tailwind Starter

A simple starter kit for integrating TailwindCss in Django

## Full Installation

### 1. Clone the project
```bash
 git clone https://github.com/MindMansion/DjangoTailwindStarter.git
 cd DjangoTailwindStarter
```

### 2. Create your environment

```bash
    python3 -m venv virtual-env
    python -m venv virtual-env # on windows
    # activate env
    source virtual-env/bin/activate
```

### 3. install requirements

```bash
    pip install -r requirements.txt
```

### 4. getting tailwind ready
```bash
    cd theme
    npm install
    npm run build
    npm run watch # to keep the scss watcher alive 
```

### 5. Runserver
from a new terminal window run:
```bash
    python3 manage.py runserver
```
Then visit the link in your browser `http://127.0.0.1:8000`

<img src="static/images/screen.png" height="1000" width="1000" alt="screen">

### Quick Installation

If you already have a Django project, and you're only interested in 
including tailwind in your project, follow these steps.

### 1. create a directory
```bash
    mkdir theme
    cd theme
```

### 2. clone the tailwind setup folder
This will add a `global.css` file to your `static` directory.
```bash
    npx degit https://github.com/MindMansion/DjangoTailwindStarter/theme
    npm install
    npm run build
    npm run watch
```

### 3. CSS file
Add the CSS file to your head tag
```html
    link rel="stylesheet" href="{% static 'css/global.css' %}">
```