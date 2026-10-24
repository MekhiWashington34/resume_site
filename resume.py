"""Your resume content. Edit this file to update the website; no HTML needed."""

PROFILE = {
    "name": "Mekhi Washington",
    "initials": "MW",
    "role": "Software developer",
    "tagline": "in Delaware. Java and Spring Boot back ends, JavaScript front ends, and AI tools in Python.",
    "email": "mekhiwash34@gmail.com",
    "linkedin": ("mekhi-washington", "https://www.linkedin.com/in/mekhi-washington-85221b211/"),
    "github": ("MekhiW34", "https://github.com/MekhiW34"),
}

ABOUT = [
    "I'm a coding bootcamp graduate who spent six months as a software intern at JPMorgan Chase, "
    "building banking and polling APIs with Java, Spring Boot and MySQL.",
    "I studied computer engineering at Delaware Tech and trained in Java through Year Up and "
    "Wilmington University. These days I'm building AI projects in Python.",
]

# "core" skills are highlighted in the accent color.
SKILLS = [
    ("Languages & frameworks", ["Java", "Spring Boot", "JavaScript", "Python", "HTML", "CSS"],
     {"Java", "Spring Boot", "JavaScript"}),
    ("Tools", ["MySQL", "IntelliJ", "VS Code", "Splunk", "Grafana", "Git"], set()),
    ("Hardware", ["Installation & troubleshooting"], set()),
]

# Dates are (year, month). Use None for "Present".
EXPERIENCE = [
    {
        "title": "Intern, JPMorgan Chase",
        "where": "Wilmington, DE · through Year Up",
        "start": (2021, 8), "end": (2022, 1),
        "bullets": [
            "Worked with a team to build a back-end banking API that creates customer accounts and lets "
            "users deposit, withdraw and pay bills.",
            "Built a polling API in Java, Spring Boot and MySQL that creates polls, records votes and "
            "stores them in a database.",
            "Pulled data from company applications with Splunk and Grafana and turned it into graphs and charts.",
            "Built a personal portfolio site in HTML, CSS and JavaScript, and completed a series of "
            "developer training modules.",
        ],
        "tags": ["Java", "Spring Boot", "MySQL", "Splunk", "Grafana"],
    },
]

PROJECTS = [
    {"name": "J.A.R.V.I.S. voice assistant", "meta": "Python · Claude API · 2026", "featured": True,
     "text": "A desktop assistant you talk to. It answers out loud, remembers things between sessions, "
             "opens apps and websites, runs commands with your approval and searches the web."},
    {"name": "Banking API", "meta": "Java · Spring Boot · MySQL",
     "text": "Team-built back end for creating customer accounts, deposits, withdrawals and bill pay."},
    {"name": "Polling API", "meta": "Java · Spring Boot · MySQL",
     "text": "Create polls, collect votes and store results in a MySQL database."},
]

EDUCATION = [
    {"title": "Java Training", "where": "Year Up / Wilmington University · New Castle, DE",
     "start": (2021, 3), "end": (2022, 1)},
    {"title": "Computer Engineering", "where": "Delaware Technical Community College · Stanton, DE",
     "start": (2017, 8), "end": (2019, 5)},
    {"title": "High School Diploma", "where": "Middletown High School · Middletown, DE",
     "start": (2014, 8), "end": (2017, 6)},
]

OTHER_WORK = [
    {"name": "WilmInvest", "where": "New Castle, DE", "start": (2024, 9), "end": None},
    {"name": "On The Mark Logistics", "where": "New Castle, DE", "start": (2023, 8), "end": (2024, 9)},
    {"name": "Amazon Flex", "where": "Middletown, DE", "start": (2021, 4), "end": (2024, 8)},
    {"name": "Warehouse Worker, Amazon", "where": "Middletown, DE", "start": (2020, 8), "end": (2020, 12)},
    {"name": "Pizza Maker, Grotto Pizza", "where": "Middletown, DE", "start": (2018, 3), "end": (2020, 8)},
]

FOOTER = "Open to software developer roles. The quickest way to reach me is email."
