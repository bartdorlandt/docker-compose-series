import pathlib
import weasyprint

BASE_DIR = pathlib.Path(__file__).parent.resolve()
OUTPUT = BASE_DIR / "01-intro-slides.pdf"

CSS = """
@page {
    size: 1080px 1080px;
    margin: 0;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: system-ui, -apple-system, sans-serif;
    background: #ffffff;
    color: #212529;
}

.slide {
    width: 1080px;
    height: 1080px;
    padding: 64px;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    overflow: hidden;
    background: #ffffff;
}

.slide:last-child {
    page-break-after: avoid;
}

.label {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #0066cc;
    margin-bottom: 20px;
}

.headline {
    font-size: 52px;
    font-weight: 800;
    color: #212529;
    line-height: 1.15;
    margin-bottom: 28px;
}

.body {
    font-size: 28px;
    color: #495057;
    line-height: 1.6;
}

.body p {
    margin-bottom: 16px;
}

.body ul {
    padding-left: 32px;
}

.body li {
    margin-bottom: 14px;
}

.code-box {
    background: #f0f4ff;
    border: 1px solid #dee2e6;
    border-radius: 10px;
    padding: 20px 24px;
    font-family: ui-monospace, monospace;
    font-size: 22px;
    color: #0066cc;
    margin: 20px 0;
    line-height: 1.5;
}

.slide-image {
    width: 100%;
    border-radius: 10px;
    margin-top: 20px;
}

.caption {
    font-size: 20px;
    color: #6c757d;
    margin-top: 12px;
}

.cta-question {
    margin-top: 32px;
    font-size: 26px;
    color: #0066cc;
    font-style: italic;
    line-height: 1.5;
}

.divider {
    border: none;
    border-top: 2px solid #dee2e6;
    margin: 28px 0;
}
"""


def slide(label, content):
    return f'<div class="slide"><div class="label">{label}</div>{content}</div>\n'


def build_html(slides_html):
    body = "\n".join(slides_html)
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""


if __name__ == "__main__":
    slides = []

    # Slide 1 — Hook
    slides.append(slide(
        "Docker Compose Series · Post 1",
        """
        <div class="headline">You've got three containers to run.</div>
        <div class="body">
            <p>So you open a terminal and start typing.</p>
            <p><code>docker run -d --name redis redis:alpine</code> — fine.
            <code>docker run -d --name web -p 8080:80 --network app-net nginx:alpine</code> — okay.</p>
            <p>Now add a database, a background worker, and a metrics exporter.
            Suddenly you have a 200-line shell script that breaks every time someone joins the team
            and forgets to run it in the right order.</p>
            <hr class="divider">
            <p><strong>There's a better way.</strong></p>
        </div>
        """
    ))

    # Slide 2 — Definition
    slides.append(slide(
        "Docker Compose Series · Post 1",
        """
        <div class="headline">What is Docker Compose?</div>
        <div class="body">
            <p>Docker Compose is a tool for defining and running multi-container applications
            using a single YAML file.</p>
            <p>Instead of juggling <code>docker run</code> commands, you describe your entire stack —
            services, networks, volumes — in one place.</p>
            <div class="code-box">docker compose up</div>
            <p>Starts everything. <code>docker compose down</code> tears it all down.</p>
            <p>That's the whole mental model.</p>
        </div>
        """
    ))

    # Slide 3 — Install
    slides.append(slide(
        "Docker Compose Series · Post 1",
        """
        <div class="headline">Getting Docker Compose</div>
        <div class="body">
            <p>Ships with <strong>Docker Desktop</strong> on Mac and Windows — nothing extra to install.</p>
            <p>On Linux, install it as a plugin:</p>
        </div>
        <img class="slide-image" src="01-intro-code-1.png" alt="Install command">
        """
    ))

    # Slide 4 — Compose file
    slides.append(slide(
        "Docker Compose Series · Post 1",
        """
        <div class="headline">From docker run to Compose</div>
        <div class="body">
            <p>Two services, zero configuration headaches:</p>
        </div>
        <img class="slide-image" src="01-intro-code-2.png" alt="docker-compose.yml example">
        <div class="caption">Both services land on the same internal network automatically — no --link flags, no manual wiring.</div>
        """
    ))

    # Slide 5 — Raw docker comparison
    slides.append(slide(
        "Docker Compose Series · Post 1",
        """
        <div class="headline">vs. Raw Docker Commands</div>
        <div class="body">
            <p>The equivalent commands you'd otherwise need:</p>
        </div>
        <img class="slide-image" src="01-intro-code-3.png" alt="Raw docker commands">
        <div class="caption">Same result — but now it's a script, not a file. No version control, no reproducibility.</div>
        """
    ))

    # Slide 6 — Why it matters
    slides.append(slide(
        "Docker Compose Series · Post 1",
        """
        <div class="headline">Why This Matters Beyond Convenience</div>
        <div class="body">
            <p>The Compose file is <strong>checked into version control</strong>. Your entire local development
            environment is code.</p>
            <p>It evolves with your project, gets reviewed in pull requests, and is
            <strong>consistent across every developer's machine</strong>.</p>
            <p>When a teammate clones your repo, they don't need to know any of this.
            They just run <code>docker compose up</code>.</p>
            <p>It also maps directly to <strong>Docker Swarm</strong>, and gives you the mental model
            that scales to <strong>Kubernetes</strong>.</p>
        </div>
        """
    ))

    # Slide 7 — Key takeaways
    slides.append(slide(
        "Docker Compose Series · Post 1",
        """
        <div class="headline">Key Takeaways</div>
        <div class="body">
            <ul>
                <li>Replaces ad-hoc <code>docker run</code> chains with a single declarative YAML file</li>
                <li><code>docker compose up</code> starts all services; <code>docker compose down</code> removes them cleanly</li>
                <li>Services are automatically placed on a shared internal network — no manual wiring required</li>
                <li>The Compose file lives in version control — your dev environment is reproducible for the whole team</li>
                <li>Docker Desktop bundles Compose; Linux users install the <code>docker-compose-plugin</code> package</li>
            </ul>
        </div>
        """
    ))

    # Slide 8 — CTA
    slides.append(slide(
        "Docker Compose Series · Post 1",
        """
        <div class="headline">Try It Yourself</div>
        <div class="body">
            <p>The full example is in the repo at <code>examples/01-intro/</code>.</p>
            <p>Clone it and run <code>docker compose up</code> — nginx will be live at
            <strong>http://localhost:8080</strong> in seconds.</p>
        </div>
        <div class="cta-question">
            How do you currently manage multi-container apps locally?
            Shell scripts, a Makefile, something else?
        </div>
        """
    ))

    html = build_html(slides)
    weasyprint.HTML(string=html, base_url=str(BASE_DIR)).write_pdf(str(OUTPUT))
    print(f"Written: {OUTPUT}")
