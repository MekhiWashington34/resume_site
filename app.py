"""
Mekhi Washington's resume website, built with Python + Flask.

Run it:      python app.py           -> open http://127.0.0.1:5000
Build it:    python app.py build     -> writes a static site to ./docs (ready for GitHub Pages)

Edit your details in resume.py.
"""

import datetime
import shutil
import sys
from pathlib import Path

from flask import Flask, render_template

import resume

app = Flask(__name__)
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


@app.template_filter("ym")
def format_month(ym):
    """(2021, 8) -> 'Aug 2021'; None -> 'Present'."""
    return "Present" if ym is None else f"{MONTHS[ym[1] - 1]} {ym[0]}"


@app.template_global()
def duration(start, end):
    """Length of a role, counting both the first and last month: 'Aug 2021 – Jan 2022' -> '6 months'."""
    if end is None:
        today = datetime.date.today()
        end = (today.year, today.month)
    months = (end[0] - start[0]) * 12 + (end[1] - start[1]) + 1
    years, rest = divmod(months, 12)
    parts = []
    if years:
        parts.append(f"{years} year{'s' if years > 1 else ''}")
    if rest:
        parts.append(f"{rest} month{'s' if rest > 1 else ''}")
    return " ".join(parts)


@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=resume.PROFILE, about=resume.ABOUT, skills=resume.SKILLS,
        experience=resume.EXPERIENCE, projects=resume.PROJECTS, education=resume.EDUCATION,
        other_work=resume.OTHER_WORK, footer=resume.FOOTER,
    )


def build(out_dir="docs"):
    """Render the site to plain files so it can be hosted for free (e.g. GitHub Pages)."""
    out = Path(out_dir)
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(Path(app.static_folder), out / "static")
    with app.test_request_context("/"):
        html = home()
    (out / "index.html").write_text(html, encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built static site in {out.resolve()}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        build()
    else:
        app.run(debug=True)
