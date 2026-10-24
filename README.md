# Mekhi Washington – Resume Site

My resume website, built with Python and Flask.

## Run it

```
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000. The page reloads its content each time you refresh, so edit and refresh.

## Update the content

Everything on the page comes from **`resume.py`**: your name, contact links, skills, jobs, projects and education. Edit that file; you don't need to touch the HTML. Dates are written as `(year, month)`, and `None` means "Present". Job lengths like "6 months" are calculated for you.

The look lives in `templates/index.html` (layout) and `static/style.css` (colors and fonts). It switches to dark mode automatically when your computer is in dark mode.

## Put it online for free (GitHub Pages)

```
python app.py build
```

This writes a plain copy of the site into the `docs` folder. Commit and push it, then on GitHub go to the repo's **Settings → Pages**, choose **Deploy from a branch**, pick `main` and the `/docs` folder, and save. GitHub gives you a link like `https://<your-username>.github.io/resume_site/`. Run `python app.py build` and push again whenever you change `resume.py`.
