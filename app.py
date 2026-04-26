import gradio as gr


def generate_llms_txt(brand_name, tagline, description, pages_raw, services_raw, social_links_raw, contact_email, contact_url):
    if not brand_name.strip():
        return "Please enter your brand name."

    lines = []
    lines.append(f"# {brand_name.strip()}")
    lines.append("")

    if tagline.strip():
        lines.append(f"> {tagline.strip()}")
        lines.append("")

    if description.strip():
        for para in description.strip().split("\n\n"):
            para = para.strip()
            if para:
                lines.append(para)
                lines.append("")

    if services_raw.strip():
        lines.append("## Services")
        lines.append("")
        for s in services_raw.strip().splitlines():
            s = s.strip()
            if s:
                lines.append(f"- {s}")
        lines.append("")

    if pages_raw.strip():
        lines.append("## Key Pages")
        lines.append("")
        for line in pages_raw.strip().splitlines():
            line = line.strip()
            if not line:
                continue
            if "|" in line:
                parts = line.split("|", 1)
                name = parts[0].strip()
                url = parts[1].strip()
                lines.append(f"- [{name}]({url})")
            else:
                lines.append(f"- {line}")
        lines.append("")

    contact_lines = []
    if contact_email.strip():
        contact_lines.append(f"- Email: {contact_email.strip()}")
    if contact_url.strip():
        u = contact_url.strip()
        contact_lines.append(f"- Contact: [{u}]({u})")
    if social_links_raw.strip():
        for s in social_links_raw.strip().splitlines():
            s = s.strip()
            if s:
                contact_lines.append(f"- {s}")

    if contact_lines:
        lines.append("## Contact & Links")
        lines.append("")
        lines.extend(contact_lines)
        lines.append("")

    return "\n".join(lines).strip()


demo = gr.Interface(
    fn=generate_llms_txt,
    inputs=[
        gr.Textbox(label="Brand Name *", placeholder="Taptwice Media"),
        gr.Textbox(label="Tagline (one sentence)", placeholder="The AEO & GEO agency that makes brands cited by AI engines."),
        gr.Textbox(label="Brand Description", placeholder="What you do, who you serve, your mission.", lines=4),
        gr.Textbox(label="Key Pages (one per line — format: Page Name | https://url)", placeholder="Home | https://yourdomain.com\nAbout | https://yourdomain.com/about\nBlog | https://yourdomain.com/blog", lines=5),
        gr.Textbox(label="Services (one per line)", placeholder="Answer Engine Optimization\nGenerative Engine Optimization\nSchema Markup", lines=4),
        gr.Textbox(label="Social Links (one per line)", placeholder="LinkedIn: https://linkedin.com/company/yourco\nTwitter: https://twitter.com/yourco", lines=3),
        gr.Textbox(label="Contact Email", placeholder="hello@yourdomain.com"),
        gr.Textbox(label="Contact Page URL", placeholder="https://yourdomain.com/contact"),
    ],
    outputs=gr.Textbox(label="Your llms.txt — copy and publish at yourdomain.com/llms.txt", lines=25),
    title="llms.txt Generator by Taptwice Media",
    description=(
        "Generate a ready-to-publish llms.txt file for your website. "
        "llms.txt tells AI engines (ChatGPT, Perplexity, Claude, Gemini) what your brand is, what you do, and where to find your key content. "
        'Built by <a href="https://taptwicemedia.com" target="_blank">Taptwice Media</a> — the AEO &amp; GEO specialists.'
    ),
    flagging_mode="never",
)

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())
