# Open-Source SaaS Alternatives

> A growing directory of open-source projects and honest alternatives to popular SaaS apps.

This is the common index for alternatives built or documented in this repository. The [root README](../../README.md) contains the broader popularity queue; this page tracks the projects that have a catalog record and the individual pages added so far.

Each individual alternative will live at:

~~~text
open-source/alternatives/<app-slug>/README.md
~~~

An app gets an individual page when it has a substantive implementation or comparison. We do not create empty folders or call a project open source before its license and scope can be reviewed.

## Published projects

| Project | Workflow | Status | Repository |
| --- | --- | --- | --- |
| [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI) | Image and video generation studio | MIT | [source](https://github.com/Anil-matcha/Open-Generative-AI) |
| [Open-Pomelli](https://github.com/SamurAIGPT/Open-Pomelli) | Brand and campaign assets | MIT | [source](https://github.com/SamurAIGPT/Open-Pomelli) |
| [Vibe Workflow](https://github.com/SamurAIGPT/Vibe-Workflow) | Visual creative pipelines | MIT | [source](https://github.com/SamurAIGPT/Vibe-Workflow) |
| [AI Clipping Generator](https://github.com/SamurAIGPT/ai-clipping-generator) | Long-form to short-form video | MIT | [source](https://github.com/SamurAIGPT/ai-clipping-generator) |
| [AI YouTube Shorts Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator) | Short-form video production | MIT | [source](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator) |
| [AI Faceless Video Generator](https://github.com/SamurAIGPT/AI-Faceless-Video-Generator) | Script-to-faceless video | MIT | [source](https://github.com/SamurAIGPT/AI-Faceless-Video-Generator) |
| [AI B-roll](https://github.com/Anil-matcha/AI-B-roll) | Script-line visual assets | MIT | [source](https://github.com/Anil-matcha/AI-B-roll) |
| [Open-VidIQ](https://github.com/SamurAIGPT/Open-VidIQ) | Creator and YouTube research | MIT | [source](https://github.com/SamurAIGPT/Open-VidIQ) |
| [social-post](https://github.com/SamurAIGPT/social-post) | Social content and publishing | License needed | [source](https://github.com/SamurAIGPT/social-post) |
| [My Podcast](https://github.com/SamurAIGPT/my-podcast) | Podcast voiceover and assets | License needed | [source](https://github.com/SamurAIGPT/my-podcast) |
| [Amazon Product Studio](https://github.com/SamurAIGPT/amazon-product-studio) | Product imagery and scenes | License needed | [source](https://github.com/SamurAIGPT/amazon-product-studio) |

## Planned projects

| Project | Workflow | Catalog record |
| --- | --- | --- |
| Open SEO / Open GEO | Site audits, rank snapshots, and search visibility | [metadata](../../data/apps/open-seo.json) |
| Open YouTube Growth Radar | Channel baselines, outlier research, and publishing assets | [metadata](../../data/apps/open-youtube-growth-radar.json) |

## Popularity queue

The [root README popularity shortlist](../../README.md#upcoming-popular-workflows) contains every source-directory app with at least five public community replacement votes in the 2026-09-17 snapshot. Choose the next app from that queue, then add its internal page here when the work is substantive.

## Individual page checklist

Every page under this directory should:

- Use the H1 format “Open-source alternatives to [App]”.
- Explain the paid app’s core workflow in plain language.
- Separate verified open-source projects from planned or partial alternatives.
- State what the project covers and what the user gives up.
- Include setup, dependencies, license, screenshots or a demo when available.
- Link back to this index, the root catalog, and closely related alternatives.
- Avoid unsupported claims of feature parity, security, privacy, or production readiness.

## Adding a page

1. Choose an app from the popularity queue or an existing catalog record.
2. Add open-source/alternatives/<app-slug>/README.md.
3. Add or update data/apps/<app-slug>.json.
4. Link the page from this index and the relevant root README section.
5. Run python scripts/validate.py.

The directory is intentionally incremental. A useful page is better than a large collection of empty keyword targets.
