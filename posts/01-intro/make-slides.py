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
    # slides will be added in Task 3
    html = build_html(slides)
    weasyprint.HTML(string=html, base_url=str(BASE_DIR)).write_pdf(str(OUTPUT))
    print(f"Written: {OUTPUT}")
