# Awesome DSH Plugin [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated guide to [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) — DeepSeek's open-source, everything-is-a-plugin coding agent — and the best community plugins built on it.

DeepSeek Harness is a runnable coding agent (Web UI + headless) built on [Cordis](https://github.com/cordiverse/cordis), where every part of the system — models, tools, sandboxes, session storage, UI, even the agent loop itself — is a swappable plugin. That architecture has produced a large, fast-moving plugin ecosystem: well over a thousand community plugins at last count. This list exists to make that ecosystem easy to scan: what a plugin does, in one line, sorted into the category you'd actually go looking under.

> [!WARNING]
> Installing any third-party `dsh` plugin runs its code on your machine with your own permissions. Being listed here is not a security review — read the source before installing, especially for plugins that touch credentials, the network, or your filesystem.

<p align="center"><a href="https://youtu.be/tiWhE0MoKsc"><img src="https://i.ytimg.com/vi/tiWhE0MoKsc/maxresdefault.jpg" width="720"></a></p>
<p align="center"><a href="https://youtu.be/tiWhE0MoKsc"><b>▶ Watch: Awesome DSH Plugin — Top 10 DeepSeek Harness Plugins You Need </b></a></p>


## Contents

- [What is DeepSeek Harness?](#what-is-deepseek-harness)
- [Getting Started](#getting-started)
- [Plugin Categories](#plugin-categories)
  - [UI Enhancements](#ui-enhancements)
  - [Usage & Billing](#usage--billing)
  - [Themes & Appearance](#themes--appearance)
  - [Models & Providers](#models--providers)
  - [Sessions & Messages](#sessions--messages)
  - [Memory](#memory)
  - [Tools & Capabilities](#tools--capabilities)
  - [Vision & Multimodal](#vision--multimodal)
  - [Skills](#skills)
  - [Workflow & Automation](#workflow--automation)
  - [Notifications & Integrations](#notifications--integrations)
  - [Git & Engineering](#git--engineering)
  - [Security & Governance](#security--governance)
  - [Remote Access & Mobile](#remote-access--mobile)
  - [Output & Deliverables](#output--deliverables)
  - [Domain & Specialist](#domain--specialist)
  - [Development & Runtime](#development--runtime)
  - [Plugin Markets & Managers](#plugin-markets--managers)
  - [Just for Fun](#just-for-fun)
- [Writing Your Own Plugin](#writing-your-own-plugin)
- [Related Projects](#related-projects)
- [Contributing](#contributing)

## What is DeepSeek Harness?

[`deepseek-ai/deepseek-harness`](https://github.com/deepseek-ai/deepseek-harness) is DeepSeek's open-source agent harness, currently in developer preview. Its defining idea is **everything is a plugin**: the model provider, the sandbox, the tool set, the session store, and the UI are all plugins loaded into a Cordis-based runtime, so you can replace or extend any layer without forking the harness itself. Plugins declare a `dsh.bundle` manifest and install with:

```sh
dsh plugin --profile web add <plugin-name>
```

## Getting Started

```sh
# run the Web UI (served at http://127.0.0.1:3080 by default)
npx @deepseek-ai/dsh web

# or from a source checkout
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness && pnpm install && pnpm run build && pnpm dsh web
```

Tag your own plugin repo with the [`dsh-plugin`](https://github.com/topics/dsh-plugin) GitHub topic so it's discoverable, and consider a plugin browser for one-click install/upgrade from inside the Web UI.

## Plugin Categories

### UI Enhancements
- [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) — Typewriter-animated rainbow status phrases, live status pill, tab titles, schedule presets — and every phrase floats by as video-site-style danmaku behind the UI.
- [0xsline/dsh-spotlight](https://github.com/0xsline/dsh-spotlight) — Keyboard-first command palette for the DSH Web UI.
- [1123762794/dsh-web-restart](https://github.com/1123762794/dsh-web-restart) — Sidebar footer button that restarts the dsh web process and persists across the restart it triggers.
- [13071301808/dsh-composer-expand](https://github.com/13071301808/dsh-composer-expand) — Expand/collapse toggle that grows the composer to a tall 70vh writing view for long drafts.
- [a179-sanae/dsh-auto-collapse](https://github.com/a179-sanae/dsh-auto-collapse) — Codex-style auto-collapse: finished turns fold into a single summary row, fully reversible on uninstall.
- [a735624258/dsh-skill-picker](https://github.com/a735624258/dsh-skill-picker) — Searchable skill picker beside the composer that inserts the official `/skill-name` gesture.
- [a903067276-rgb/dsh-hud](https://github.com/a903067276-rgb/dsh-hud) — HUD panel: Git status, MCP servers, skills, model and token usage, all floating.
- [a903067276-rgb/dsh-file-mentions](https://github.com/a903067276-rgb/dsh-file-mentions) — Clickable file paths in replies, with reveal-in-file-manager and a mentioned-files chip list.
- [AcidGr/dsh-web-lan-access](https://github.com/AcidGr/dsh-web-lan-access) — Fixes the Web UI so it survives LAN or Tailscale direct-IP access.
- [AKS1st/dsh-mermaid](https://github.com/AKS1st/dsh-mermaid) — Renders Mermaid fences as sanitized, theme-aware SVG diagrams.
- [AKS1st/dsh-sysmon](https://github.com/AKS1st/dsh-sysmon) — Floating CPU/memory/disk widget with threshold color warnings.
- [dsh-blue/blue](https://github.com/dsh-blue/blue) — Full interactive TUI for DeepSeek Harness: streaming Markdown transcript, tool-call cards, approval overlays, session management, and theming — every render component a hot-swappable plugin.
- [hanzhangzzz/dsh-diagram](https://github.com/hanzhangzzz/dsh-diagram) — Editable Excalidraw diagrams embedded directly in conversations.
- [giiiiiithub/terminal](https://github.com/giiiiiithub/terminal) — A real PTY terminal panel via node-pty and xterm.js, with multi-tab sessions and a dock/floating window.
- [Laplace-bit/dsh-smooth-stream](https://github.com/Laplace-bit/dsh-smooth-stream) — Fluid streaming rendering and smooth scrolling for the DeepSeek Harness Web UI.
- [lcsdg/dsh-quick-prompts](https://github.com/lcsdg/dsh-quick-prompts) — Quick-prompts bar above the DSH composer: per-category snippet chips, orange placeholder highlighting, two-column prompt/category management, and per-session category memory.
- [opencues/opencues](https://github.com/opencues/opencues/tree/master/integrations/dsh) — Word alternatives and underscore-gated fill-ins in the composer: end a line with `_` and it is filled, misspellings flagged as you type. Uses the model dsh is already configured with, so no API key.
- [Pasumao/dsh-plugin-choice-refresh](https://github.com/Pasumao/dsh-plugin-choice-refresh) — Adds "regenerate options" and "more options" buttons to ask_user_question / ask_user_choice cards — pure front-end, no core changes.
- [Pasumao/dsh-plugin-image-tools](https://github.com/Pasumao/dsh-plugin-image-tools) — Image choice cards for ask_user_choice (zoomable), inline images in replies via show_images, and blind-model image capture — zero-token local rendering.
- [Pasumao/dsh-plugin-workbench](https://github.com/Pasumao/dsh-plugin-workbench) — Editable VS Code-style workbench: file tree, code preview with syntax highlighting, right-click file ops (new/rename/delete/open), inline image preview.
- [PerryLink/dsh-composer-history](https://github.com/PerryLink/dsh-composer-history) — Terminal-style input history for the web composer: edge-first arrows with exact draft/caret restore, Ctrl+R reverse search, workspace-scoped recall, and sliding-context awareness.
- [NormanFxxkingRockwell/dsh-keyboard-history](https://github.com/NormanFxxkingRockwell/dsh-keyboard-history) — Minimal ↑/↓ input history for the DSH web composer: press ↑/↓ to walk back through sent messages. Nothing else.
- [PerryLink/dsh-output-styles](https://github.com/PerryLink/dsh-output-styles) — Runtime-switchable model output styles with Claude Code outputStyles parity, plus the output.render.* presentation protocol and a /style command.
- [PerryLink/dsh-session-pin](https://github.com/PerryLink/dsh-session-pin) — Pin sessions and workspaces to the top of the Web sidebar with per-pin row colors, boards, tags, saved views, and /goto.
- [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) — Voice-first session loop: composer microphone with browser/local speech-to-text (Web Speech, FunASR, whisper.cpp), a speak tool for TTS replies, event announcements, and speak-to-interrupt.
- [Ricketts-Guo/dsh-shortcuts](https://github.com/Ricketts-Guo/dsh-shortcuts) — 34 pre-registered keyboard shortcuts (sessions, views, clipboard, models, silent permission cycling), one-click recording to bind your own.
- [Nagi-ovo/dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) — In-conversation generative UI: the model renders interactive HTML cards into the chat stream, with streaming preview and sandboxed rendering.
- [PerryLink/dsh-budget](https://github.com/PerryLink/dsh-budget) — Cost governance: aggregated token/cost metering per model, session and day, session/daily/monthly caps with threshold alerts, alert/block/degrade over-limit policies, carbon estimation, and the /budget command.
- [urzeye/dsh-outline](https://github.com/urzeye/dsh-outline) — Realtime conversation outline: user questions plus Markdown headings, streaming updates, click-to-jump.
- [dsh-workspace-menu](https://github.com/0imzero/dsh-workspace-menu) — Workspace/chat context menu for the DSH home page: pin, rename, open in file explorer, archive, fork, copy, and open in a new window.
- [YannZhou/dsh-about](https://github.com/YannZhou/dsh-about) — Settings "About" tab: DeepSeek logo, version info, npm latest/next update check with one-click global update + auto-restart, and GitHub releases history.
- [SnowCrescenter-tech/dsh-milestone](https://github.com/SnowCrescenter-tech/dsh-milestone) — Git-style dot timeline on the right edge of the DSH web UI: one dot per user message, hover for content & metadata, click to jump; full-session list, in-session & cross-session search, #msg= deep-link bookmarks, keyboard nav.
- [stephenlzc/dsh-swarm-panel#dsh-swarm-plugin](https://github.com/stephenlzc/dsh-swarm-panel/tree/main/dsh-swarm-plugin) — Conversation Flow observability for DeepSeek Harness swarms, with topology, routed-message inspection, HITL pauses, Live follow, and child-session navigation.
- - [ssjob123/dsh-file-panel-left](https://github.com/ssjob123/dsh-file-panel-left) — Files-only workbench sidebar: always-docked file tree, CodeMirror editor, previews, and @-references with real line numbers.
- [YEYEYEYESHIFU/dsh-result-only-view](https://github.com/YEYEYEYESHIFU/dsh-result-only-view) — Results-only view toggle for the DSH Web GUI: folds thinking and tool-call process rows so conversations show only user messages and final replies, with live summary chips for running steps, a click-to-expand per-turn trace with hover-peek, auto/manual fold modes, and context-injection rows folded too.
- [YEYEYEYESHIFU/dsh-session-hotkeys](https://github.com/YEYEYEYESHIFU/dsh-session-hotkeys) — Keyboard-first session management for the DSH Web GUI: switch sessions like browser tabs (positional Alt+1-9, pinned slots, previous/next), keyboard model switching, alternate send, archive confirmation, focus-search — every binding rebindable with Windows/macOS presets.

- [weibaohui/dsh-settings-ui](https://github.com/weibaohui/dsh-settings-ui) — Customizes the native settings window: preset/custom sizes, fullscreen, background transparency, and theme, solid-color, or image backgrounds, with a floating ball for quick access; saved in the local browser.
- [SiriLee/dsh-approval-hotkeys](https://github.com/SiriLee/dsh-approval-hotkeys) — Keyboard-first approval: Enter approves once, Esc rejects, Esc pauses review — works across approval and question panels.
### Usage & Billing

- [melvinWEN/dsh-elegent-balance-tracker](https://github.com/melvinWEN/dsh-elegent-balance-tracker) — Elegant billing tracker: per-session cost (official peak/off-peak pricing by message time) under the composer stats plus official account balance right-aligned on the sidebar settings row, with per-minute balance re-alignment and real-time local-cost deduction in between.
- [02Muller25/dsh-api-balance](https://github.com/02Muller25/dsh-api-balance) — Real-time DeepSeek API account balance in the composer dock.
- [283Gawin/dsh-heatmap](https://github.com/283Gawin/dsh-heatmap) — GitHub-style activity heatmap of daily commits, token usage, and estimated spend.
- [940842546/dsh-usage-billing](https://github.com/940842546/dsh-usage-billing) — Usage and cost statistics with peak/off-peak pricing and a day/week/month/year/all usage heatmap.
- [bobcat848/dsh-calculator](https://github.com/bobcat848/dsh-calculator) — Session and all-time API spend plus account balance, with official pricing support.
- [bpc-oss/dsh-web-billing](https://github.com/bpc-oss/dsh-web-billing) — RMB/USD token-billing plugin for DeepSeek Harness: official-policy auto pricing (peak/off-peak), per-provider billing (usage/subscription/free-ride/local), source-grouped cost page, budget, balance, CSV/JSON export.
- [CN-Leo/dsh-deepseek-balance](https://github.com/CN-Leo/dsh-deepseek-balance) — Real-time account balance in the composer dock, auto-refreshing every 15 seconds.
- [DoggyHU/dsh-plugin-quota-monitor](https://github.com/DoggyHU/dsh-plugin-quota-monitor) — Sidebar footer quota & balance monitor: always-on DeepSeek Rage (¥) + OpenCode Go HP/MP/SP quota windows (monthly/weekly/5h) + SCNet (国家超算) Credits estimated locally from DSH session logs; data source & rate table configurable in Settings.
- [Ghost011118/dsh-balance-meter](https://github.com/Ghost011118/dsh-balance-meter) — Account balance and session cost in the composer dock with peak/off-peak support.
- [Han-1413141/dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) — Per-session and daily cost with a budget bar and one-click official price sync.
- [huanyuLv/dsh-balance-tide](https://github.com/huanyuLv/dsh-balance-tide) — Live peak/off-peak pricing badge with a countdown to the next pricing switch.
- [Jannchie/dsh-bill](https://github.com/Jannchie/dsh-bill) — Cost tracking priced per call from models.dev + OpenRouter (8000+ models): per-turn line attributed to tool output / model output / system prompt / commands, budget, forecast.
- [kirigayakazima/dsh-usage-vendor-stats](https://github.com/kirigayakazima/dsh-usage-vendor-stats) — Per-provider token/cache/output KPI dashboard: 53-week heatmap, hourly trend, model drilldown, CSV export, TTFT/speed/error-rate health cards.
- [Phant0Meow/dsh-meow-cachebilling](https://github.com/Phant0Meow/dsh-meow-cachebilling) — Per-round cache billing in the composer context meter's popover: what the current call spends on cache hits, misses, and output in CNY, with automatic official peak/off-peak and per-model pricing; hidden on non-official DeepSeek routes.
- [teethyachi/dsh-usage-mini](https://github.com/teethyachi/dsh-usage-mini) — Claude/Codex subscription usage windows with reset countdowns, next to today's DeepSeek API spend and balance, in one draggable floating window (用量小窗) that docks to a corner. Display-only companion to dsh-cost-meter and dsh-plugin-subscriptions; UI follows the DSH language setting.

### Themes & Appearance

- [0nt-one/dsh-neo-skin](https://github.com/0nt-one/dsh-neo-skin) — Neo-brutalism skin with hard shadows, sharp corners, and light/dark support.
- [AKS1st/dsh-cyber-particle](https://github.com/AKS1st/dsh-cyber-particle) — Full-screen, click-through particle-network background overlay.
- [BeiZi6/dsh-theme-plugin](https://github.com/BeiZi6/dsh-theme-plugin) — Theme studio with five presets plus fully customizable palettes, hot-swapped and persisted.
- [caoyiwei850/dsh-client-ui-skins](https://github.com/caoyiwei850/dsh-client-ui-skins) — Custom image skins where the palette follows the photo's dominant hue.
- [chinaRXQ/dsh-wallpaper](https://github.com/chinaRXQ/dsh-wallpaper) — Wallpaper skin with opacity, mask, and blur controls.
- [fengb3/dsh-theme-macintosh](https://github.com/fengb3/dsh-theme-macintosh) — Classic Macintosh (System 7) pixel theme: desktop pattern canvas, Finder sidebar, monochrome buttons and dialogs, light/dark support.
- [dhicoc/dsh-theme-mineradio](https://github.com/dhicoc/dsh-theme-mineradio) — Mineradio glassmorphism theme for the DSH web UI: champagne-gold glass panes, a fluid or wallpaper backdrop, and a one-switch restore to the stock look.
- [dgadelha1/dsh-explorer-plugin](https://github.com/dgadelha1/dsh-explorer-plugin) — VS Code-style workspace file tree + Monaco editor with real TextMate grammars (28 languages), multi-tab, live watcher, docked into the DSH web GUI.
- [Isilsolme/dsh-anthropic-fonts](https://github.com/Isilsolme/dsh-anthropic-fonts) — Anthropic Sans/Serif/Mono fonts with CJK fallback.
- [KinGao294/dsh-skin](https://github.com/KinGao294/dsh-skin) — Codex-style skin switcher with a custom wallpaper layer.
- [Lhy723/dsh-neu-theme](https://github.com/Lhy723/dsh-neu-theme) — Neumorphic theme with ambient lighting, material shadows, and frosted-glass surfaces.
- [PerryLink/dsh-local-ai](https://github.com/PerryLink/dsh-local-ai) — Ollama local-model integration: discover, pull, remove and inspect local models, route by task type or keyword with automatic cloud fallback, and a /ollama status overview.
- [PerryLink/dsh-translate](https://github.com/PerryLink/dsh-translate) — Vendor parameter translation across 11 vendors plus deterministic JSON repair for broken tool output, never fabricating data.
- [RevolutionLA/dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin) — 8 original themes, translucent wallpaper with opacity/blur, per-user accent, shareable theme-pack import/export.
- [shawnlone/dsh-theme-tuner](https://github.com/shawnlone/dsh-theme-tuner) — Theme-adjustment panel under Appearance: customize accent, background, foreground, contrast and gradient, applied live through theme token overrides.
- [Tkingxiao/dsh-any-background](https://github.com/Tkingxiao/dsh-any-background) — Full custom theme colors, background wallpapers, and per-section transparency/blur, with import/export.

### Models & Providers

- [BruceLanLan/dsh-tier-router](https://github.com/BruceLanLan/dsh-tier-router) — Two-tier routing: a strong tier plans and reviews, a cheap tier implements, with failure auto-escalation.
- [btspoony/dsh-llm-fallbacks](https://github.com/btspoony/dsh-llm-fallbacks) — Role-based LLM retry and fallback strategies.
- [dylan121322/llm-adaptive](https://github.com/dylan121322/llm-adaptive) — Per-request complexity classification with automatic provider routing.
- [fieldnote-ops/keyringseam](https://github.com/fieldnote-ops/keyringseam) — macOS Keychain credential provider replacing the local-file default.
- [franksong2702/dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) — Connects ChatGPT OAuth / OpenAI Codex models to the harness.
- [GodD6366/dsh-sub2api](https://github.com/GodD6366/dsh-sub2api) — OpenAI-compatible multi-provider routes (OpenAI/Claude/Grok/Gemini) behind one base URL.
- [MajidAsghariTabrizi/free-best-router](https://github.com/MajidAsghariTabrizi/free-best-router) — OpenAI-compat routing layer across 7 free LLM providers (OpenRouter, OpenCode/Zen, Groq, Cerebras, Mistral, DeepSeek, local) with Wilson + Bayesian scoring, per-failure cooldowns, and bounded 4-attempt fallback. MIT, zero telemetry.
- [kam74515-boop/dsh-everything-oauth](https://github.com/kam74515-boop/dsh-everything-oauth) — Imports existing Codex, Grok, Claude, and OpenCode logins so you don't re-auth per tool.
- [katsos/dsh-claude-cli](https://github.com/katsos/dsh-claude-cli) — Runs the local Claude Code CLI as a model backend over an existing subscription instead of a metered key.
- [NOirBRight/dsh-llm-ollama](https://github.com/NOirBRight/dsh-llm-ollama) — Ollama Cloud native chat adapter with model discovery and web search/fetch providers.
- [PerryLink/dsh-checkpoint-rewind](https://github.com/PerryLink/dsh-checkpoint-rewind) — Claude Code /rewind for DSH: git-first workspace snapshots, turn-boundary session forks, and one-shot restore via /checkpoint and /rewind.
- [PerryLink/dsh-claude-move](https://github.com/PerryLink/dsh-claude-move) — Four-source migration wizard: move Claude Code, Codex, OpenCode and Hermes sessions, memories, skills and slash commands into DSH as resumable sessions.
- [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) — Cross-device session sync through a dedicated git mirror with append-only three-way merge (keep-both + fork conflicts), a /sync command, and auto push/pull.
- [WNJXYK/dsh-codex-oauth](https://github.com/WNJXYK/dsh-codex-oauth) — Use a ChatGPT/Codex subscription in DSH with GPT models, image generation, web search, and browser or device-code OAuth sign-in.
- [r600a-code/dsh-swarm-router](https://github.com/r600a-code/dsh-swarm-router) — Routes heterogeneous tasks to the best-suited model with feedback-driven ranking.
- [PerryLink/dsh-autotier](https://github.com/PerryLink/dsh-autotier) — Automatic model-tier routing for DeepSeek Harness: one user instruction enters, one tier decision comes out — no manual model switching.
- [YUEYUEXYS/dsh-think-ultra](https://github.com/YUEYUEXYS/dsh-think-ultra) — Reasoning layer for DeepSeek Harness that keeps requests on native max effort while adding isolated Flash, Vision, and Pro depth controls and reasoning toolboxes.

### Sessions & Messages

- [3403473060/dsh-inline-images](https://github.com/3403473060/dsh-inline-images) — Renders local image paths from assistant replies inline with a click-to-zoom lightbox.
- [Anionex/dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) — Rewind conversation and workspace state via a persistent Change Ledger.
- [beijingwahw/dsh-companion](https://github.com/beijingwahw/dsh-companion) — Smart export (Markdown/PDF/JSON/PNG), context-handoff summaries, cost optimization, and global search.
- [Buyi-wsgzg/dsh-sidechain](https://github.com/Buyi-wsgzg/dsh-sidechain) — `/side` persistent side sessions and `/btw` one-shot questions in a temporary fork.
- [chouyong/dsh-fork-graph](https://github.com/chouyong/dsh-fork-graph) — Git-style conversation fork graph with colored lanes and click-to-jump navigation.
- [czm15053/dsh-peer-link](https://github.com/czm15053/dsh-peer-link) — Lets dsh and Claude Code sessions message each other directly.
- [dongsheng123132/task-passport](https://github.com/dongsheng123132/task-passport) — Carries durable task state across DeepSeek Harness, WorkBuddy, Claude Code, and Codex.
- [dream12347/dsh-session-manager](https://github.com/dream12347/dsh-session-manager) — Session trash/restore/purge, recent-activity stats, workspace grouping, and compaction threshold control.
- [fredalxin/dsh-solo-thinking](https://github.com/fredalxin/dsh-solo-thinking) — Visual branch brainstorming: isolated session per direction with automated parent/sibling/checkpoint handoffs and a full tree tab.
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) — Rolls conversation and workspace files back to before any user message, via shadow git snapshots with a diff-preview confirmation.
- [nickkkkkk123123/dsh-resume-on-restart](https://github.com/nickkkkkk123123/dsh-resume-on-restart) — Auto-wakes the main agent after a DSH service restart: compares last-run timestamps, posts a recovery notice with humanized downtime, and delivers it so interrupted work picks itself back up. Runs on plain cordis ctx, packaged-DSH-Desktop ready.
- [Renzic-Stone/DSH-EasyRewrite](https://github.com/Renzic-Stone/DSH-EasyRewrite) — Inline edit & recall for user-message bubbles in DSH Web — lazy commit, seamless replacement, version pager, draft auto-backup, trilingual i18n. DSH Web 内用户消息气泡内联编辑与撤回插件：惰性提交、无痕替换、版本翻页器、草稿自动备份、三语 i18n。
- [xiaoyuyu6420/dsh-backup](https://github.com/xiaoyuyu6420/dsh-backup) — One-command backup & restore of the whole `~/.dsh` workspace (sessions, settings, skills, MCP): typed `--types` backups, restart-surviving scheduled backups with tiered retention, sha256-verified merge restore with rollback and cross-machine guardrails, `/backup doctor` session-log repair with quarantine, pre-upgrade snapshots, an out-of-band rescue console, credential redaction to a local-only vault, and private-repo GitHub sync for machine migration.
- [yindf/taskfold](https://github.com/yindf/taskfold) — Wraps work in named tasks and folds each finished task's whole span of messages into one summary at the next step boundary, with the original messages restorable on demand.
- [SunshineR04/dsh-session-manager](https://github.com/SunshineR04/dsh-session-manager) — Manage archived sessions from the Settings page: restore or permanently delete them; red delete item in the session context menu; open sessions delete immediately (tombstone cleanup after restart).

- [weibaohui/dsh-smart-title](https://github.com/weibaohui/dsh-smart-title) — Smart session titles for DSH: after each conversation turn an independent auxiliary LLM call summarizes the full user+assistant transcript into a title that follows the session's real topic instead of echoing the first message; the first message is titled instantly, failed built-in titles auto-retry on later turns, manual renames are never overwritten, and subagent/fork sessions are skipped.
- [weibaohui/dsh-continue](https://github.com/weibaohui/dsh-continue) — Auto-resume for interrupted sessions: rules route by failure type (rate limit, quota, auth, context overflow, crashed orphan) into backoff retry, model switch, resume-after-compaction, or stop-loss notification, with a visual rule editor and activity log.
- [SiriLee/dsh-rewind](https://github.com/SiriLee/dsh-rewind) — In-place conversation rewind in the same session window without forking (Claude Code /rewind semantics): a per-message rewind button cuts the model context back to any user message, with optional Claude-Code-style file restore from disk-persisted before-backups.
### Memory

- [863683348/dsh-plugin-focus](https://github.com/863683348/dsh-plugin-focus) — Durable focus board pinning objective, constraints, and decisions across compaction and sessions.
- [aerince/dsh-active-context-pruning](https://github.com/aerince/dsh-active-context-pruning) — Model-authored context pruning through the official compaction API.
- [Aik358/dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) — Cache-friendly three-layer memory with per-turn consolidation and inheritance from other AI tools.
- [akslcw/dsh-negative-ledger](https://github.com/akslcw/dsh-negative-ledger) — Persists disproven paths and blocks repeat attempts until evidence changes.
- [bowenliang123/dsh-context](https://github.com/bowenliang123/dsh-context) — Context-insight panel showing exactly what's filling the model's window and why.
- [busabase/busabase-dsh-plugin](https://github.com/busabase/busabase-dsh-plugin) — Connects DSH agents to Busabase structured knowledge, bases, and records with live inspector rendering and approval-gated ChangeRequests.
- [flymysql/dsh-memory](https://github.com/flymysql/dsh-memory) — Cross-session memory vault: remember / recall / forget tools with prompt injection.
- [FuRongJun-1999/dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) — Multi-agent spatiotemporal memory graph with a self-evolving knowledge flywheel and auditable trust guardrails.
- [GIT121995/dsh-memory-gate](https://github.com/GIT121995/dsh-memory-gate) — Bounded local memory with explainable use/verify/ignore decisions, a full audit trail, and a tight per-call injection cap.
- [highland0971/dsh-native-memory](https://github.com/highland0971/dsh-native-memory) — Native per-workspace memory with approval-gated writes and deterministic recall — no external server.
- [PerryLink/dsh-click](https://github.com/PerryLink/dsh-click) — Cross-platform native desktop control (Windows first): screen_shot/screen_read, click/type/scroll/key, app_list/app_launch — approval-gated, never stealing foreground focus.
- [PerryLink/dsh-library](https://github.com/PerryLink/dsh-library) — Local document knowledge base: hybrid semantic+keyword search with diversity re-ranking, citation-aware injection, and a SQLite-backed index with zero model downloads.
- [PerryLink/dsh-memento](https://github.com/PerryLink/dsh-memento) — Bounded, layered, approval-gated cross-session memory with a typed seam, SQLite provider, and frozen-snapshot injection.
- [KLRSL/dsh-biomemory](https://github.com/KLRSL/dsh-biomemory) — Biomimetic memory: plain-Markdown data layer, memory metabolism ("dream"), memory pins, semantic recall, and cross-session retrieval.
- [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) — Multi-dimensional quality scoring for DSH plugins (install, maintenance, docs, security, protocol compliance) with real CLI evidence and a JSON/Markdown leaderboard.
- [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) — Isolated install-and-smoke test drives for DSH plugins in throwaway DSH_HOME profiles, emitting structured pass/fail result matrices.
- [rainow/dsh-simple-wiki-memory](https://github.com/rainow/dsh-simple-wiki-memory) — A super-simplified LLM-wiki memory plugin: one index document (auto-loaded) + one markdown file per topic (read only when needed) — no dumping everything into the context and burning tokens. Simple and lightweight, painless to install/uninstall, and freely editable however you like.
- [weibaohui/dsh-kb](https://github.com/weibaohui/dsh-kb) — Team knowledge base for offline knowledge sharing (FDE box scenario): browse, full-text search and refinement entry points; raw material is queued automatically and distilled into wiki pages by a serial bot session (Karpathy LLM Wiki pattern: immutable raw, two-step refinement, log stream, monthly lint).
- [dearbld/dsh-living-memory](https://github.com/dearbld/dsh-living-memory) - Self-tending living memory in one local SQLite file: nightly patrol (dedupe/merge/decay/cross-link), seven-signal RRF recall (FTS5+jieba, optional vectors, graph PPR), typed knowledge graph, conflict detection, web telemetry panels.
- [weibaohui/context-razor](https://github.com/weibaohui/context-razor) — Context trimmer: lists the current session's context entries with role, preview and ≈token estimate (cl100k), highlights over-threshold items, and removes selected entries exactly without LLM summarization.
- [weibaohui/hermes-loop](https://github.com/weibaohui/hermes-loop) — Automatic post-conversation retrospective that distills useful experience into reusable skills for the skill library, with approval mode and skill-library governance (archive/restore, never deletes directly).
- [Mutx163/dsh-model-memory](https://github.com/Mutx163/dsh-model-memory) — Reasoning-effort tier management for custom API models (low, medium, high, max) plus cross-session per-channel memory that restores the last model and effort level.

### Tools & Capabilities

- [988hj7tczd-oss/dsh-computer-use](https://github.com/988hj7tczd-oss/dsh-computer-use) — Cross-platform Computer Use: virtual-mouse operation, AX-tree zero-vision-cost mode, and safety guards.
- [Anionex/dsh-computer-use](https://github.com/Anionex/dsh-computer-use) — Accessibility-first macOS computer use with fresh observations, stale-state rejection, and scoped permissions.
- [AbnerAI/dsh-monitor](https://github.com/AbnerAI/dsh-monitor) — Persistent background watchers that wake the agent on new events — the harness analog of a Monitor tool.
- [akqwpeter-prog/dsh-agent-conductor](https://github.com/akqwpeter-prog/dsh-agent-conductor) — Dispatches tasks from DSH to 11 external agent CLIs (Codex, Claude Code, Cursor, Gemini, and more).
- [AngelosZou/dsh-multi-folder](https://github.com/AngelosZou/dsh-multi-folder) — Secondary working directories with equal read/write/exec permissions.
- [anweat/dsh-browser](https://github.com/anweat/dsh-browser) — Self-contained Playwright + OpenCLI browser runtime exposing 9 interactive browser tools.
- [anweat/dsh-voice-webspeech](https://github.com/anweat/dsh-voice-webspeech) — Browser Web Speech API voice input: zero server, zero keys.
- [Ivy Tendril](https://github.com/Ivy-Interactive/Ivy-Tendril): Open-source agentic software factory with an amazing UI that handles parallel Git worktrees for you, complete with programmatic verifications and fast review loops.
- [scriptsnet/dsh-fleet](https://github.com/scriptsnet/dsh-fleet) — Distributed compute fleet for DSH: pool idle machines (friends' PCs, LAN servers, cloud ECS) into a team and dispatch agent tasks to any online member with results flowing back.
- [franksong2702/dsh-dictate](https://github.com/franksong2702/dsh-dictate) — Browser Web Speech dictation for the Composer: recognition needs no dedicated ASR server, key, or model download; reuses Session text and a configured DSH model for contextual phrase hints and optional transcript polishing.
- [1na-ko/dsh-hdc-bridge](https://github.com/1na-ko/dsh-hdc-bridge) — HarmonyOS device bridge: screenshot/install/log/crash/UI automation loop.
- [6Mikao9/dsh-wsl-workspace](https://github.com/6Mikao9/dsh-wsl-workspace) — Adds a WSL workspace from the web GUI without reinstalling dsh inside WSL.
- [buhuikongpan/dsh-win-gitbash](https://github.com/buhuikongpan/dsh-win-gitbash) — Git Bash shell tool for Windows with timeout, sandbox, output truncation, and background jobs.
- [beihzb/dsh-envsel](https://github.com/beihzb/dsh-envsel) — Session environment picker for DSH: per-language conda / standalone R / WSL / custom-path slots in the conversation header plus a /env command and session_env tool.
- [dhicoc/dsh-codex-web-search-mcp](https://github.com/dhicoc/dsh-codex-web-search-mcp) — Registers codex-web-search-mcp as native DSH MCP tools (codex_web_search / codex_web_research / web_fetch) for model-independent Codex/Grok web search and deep research.
- [moguiyu/dsh-tavily](https://github.com/moguiyu/dsh-tavily) — Opt-in advanced Tavily search tools (search, extract, map, crawl) with multi-key rotation/failover, a live usage gauge, and a keyed settings card; one version serves DSH 0.1.0-rc.7 through 0.1.2-alpha hosts, and the built-in web_search is never replaced.

- [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) — Chinese novel writing assistant for DSH: sentence/emotion/imagery analysis, 6-dim writing-metric baseline band with per-chapter μ±σ, 12-axis vibe spectrum, style portrait report, local semantic search (0 token), plot & settings management, and 15 novel tools.

- [maddogfinance/dsh-trading](https://github.com/maddogfinance/dsh-trading) — Research-only trading workbench: typed market-data seam with BYO providers, multi-timeframe indicator snapshots, interactive chart cards with provenance-gated model annotations, and a pre-execute risk-guard that blocks execution-shaped tool calls.
- [dream-num/dsh-univer-office](https://github.com/dream-num/dsh-univer-office) — Give DeepSeek Harness a real office environment. Univer Office Plugin brings spreadsheets, docs, slides, canvases, relational tables, and more into one runtime — with connected data, validation, versioned changes, and isolated worktrees for multi-agent collaboration.
- [lxfu1/dsh-plugin-chart](https://github.com/lxfu1/dsh-plugin-chart) — Generates AntV chart and diagram images from natural-language requests, with support for formats such as line, bar, pie, Sankey, organization, network, and flow charts.
- [PerryLink/dsh-draw](https://github.com/PerryLink/dsh-draw) — Unified static-image generation router: one image_generate tool over config-driven OpenAI-compatible engines (OpenAI Images, Zhipu CogView) with health-aware fallback, durable attachments, and per-session quotas.
- [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) — The DSH plugin-development knowledge base as an on-demand agent skill: official constraints, task workflows, API reference, and community gotchas.
- [PerryLink/dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) — Security-audit skill pack plus the plugin_vet supply-chain gate: eight bilingual agent skills and an automated pre-install scanner.
- [beijingwahw/dsh-nuke-plugin](https://github.com/beijingwahw/dsh-nuke-plugin) — Transactional uninstall engine: every destructive action runs validate/preview/execute/undo with Saga rollback, WAL crash recovery, hash-chain audit, hardlink dedup, and a Bayesian oracle that predicts success probability before you commit.
- [xiehuan123/dsh-deepread](https://github.com/xiehuan123/dsh-deepread) — Evidence-first deep reading for books, articles, PDFs, and document sets with claim-evidence reports, knowledge maps, recall questions, a Host tool, and an optional Web reading panel.
- [weibaohui/dsh-file-share](https://github.com/weibaohui/dsh-file-share) — Session workspace file manager: adds a "Files" tab to the conversation area to browse the current session workspace directory tree and manage it in place (upload, download, mkdir, rename, delete, search), with files mentionable into the composer for the agent to process.
- [PerryLink/dsh-data-quality](https://github.com/PerryLink/dsh-data-quality) — Data quality checking for DeepSeek Harness: profiling, cleaning, and verification pipelines with structured reports.
- [maxmilian/dsh-grafana-query](https://github.com/maxmilian/dsh-grafana-query) — Read-only Grafana tools over the data source proxy: instance health, data sources, instant and range PromQL queries, current alert state, and provisioned alert rules.
- [maxmilian/dsh-sentry](https://github.com/maxmilian/dsh-sentry) — Read-only Sentry tools: project listing, issue search and detail, and the latest or a specific event with a trimmed stacktrace that drops local variables, request data, and secret-looking tags.
- [maxmilian/dsh-odoo](https://github.com/maxmilian/dsh-odoo) — Read-only Odoo tools over JSON-RPC: server info, model field introspection, and a restricted search_read on an allow list of models; a draft-create tool is registered only when allowWrite is enabled.

### Vision & Multimodal

- [54xkeee/dsh-vision](https://github.com/54xkeee/dsh-vision) — Zero-cost vision for text-only DeepSeek via a logged-in Chrome CDP bridge, with fallback providers.
- [akqwpeter-prog/dsh-media-skills](https://github.com/akqwpeter-prog/dsh-media-skills) — Free vision bridge and image generation for text-only models with engine failover.
- [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) — Intent-aware image Q&A, long-screenshot OCR, UI reproduction, and grounding.
- [ConsoleSun/Gemini-Eyes](https://github.com/ConsoleSun/Gemini-Eyes) — MCP bridge to gemini.google.com for vision analysis plus Imagen/Veo generation, no API key.
- [Einskyle/dsh-llm-vision-bridge](https://github.com/Einskyle/dsh-llm-vision-bridge) — Native vision bridge routing pasted images through a local VLM, then feeding the description to text-only DeepSeek.
- [exoticknight/dsh-labnana](https://github.com/exoticknight/dsh-labnana) — Labnana image generation for DeepSeek Harness: text-to-image / image-to-image / precise editing (NanoBanana Pro, GPT-Image-2, Wan2.7, Seedream).
- [FuzzySoul/dsh-free-vision](https://github.com/FuzzySoul/dsh-free-vision) — Free-tier vision bridge (Qwen3-VL-Flash, Doubao, DeepSeek-OCR) with a settings GUI.
- [Flyvhidbwo/dsh-vision-proxy](https://github.com/Flyvhidbwo/dsh-vision-proxy) — GUI images auto-transcribed to text for text-only DeepSeek via the official deepseek-v4-flash-vision-exp by default (a pure-text V4-Pro brain can see images); any OpenAI-compatible VLM or local Ollama as alternatives.
- [gloryxpnv/dsh-tool-vision](https://github.com/gloryxpnv/dsh-tool-vision) — Local-first structured vision returning JSON evidence — images never leave the machine.
- [good-boy4069/dsh-vision-guard](https://github.com/good-boy4069/dsh-vision-guard) — Transparent image guard avoiding session deadlocks, plus OCR/PDF/docx/pptx/video analysis.
- [haiziyao/dsh-vision-mix](https://github.com/haiziyao/dsh-vision-mix) — Combines text, vision, and image-generation APIs into one auto-routing Mix model.
- [Nicholaskin/vision-exp-tile](https://github.com/Nicholaskin/vision-exp-tile) — Large-image recognition for deepseek-v4-flash-vision-exp: lossless 800×800 tile recognition (smart/pipeline/full), local OCR with preprocessing & handwriting routing, optional multi-vendor GPU (DirectML/CUDA/OpenVINO) with auto CPU fallback.
- [PerryLink/dsh-background-agents](https://github.com/PerryLink/dsh-background-agents) — Durable background child agents on the official subagent seam plus persistent multi-agent team rooms with a message bus, shared task board, and approval-gated handoffs.
- [PerryLink/dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck) — Engineering-discipline guard: requirements grill before the first edit, red/green test-evidence gates, adversarial delivery review, and a per-dimension verification report.

### Skills

- [AKS1st/dsh-skill-manager](https://github.com/AKS1st/dsh-skill-manager) — Browse and edit system/user/workspace/preset skills, import from zip, export or delete.
- [Leo3-7/dsh-obsidian-inbox](https://github.com/Leo3-7/dsh-obsidian-inbox) — Obsidian 知识库入库技能：按 7 步标准流程把 DSH 对话的结论/错题/项目整理进 Obsidian，含公式与结构两级确定性校验脚本 (Obsidian knowledge-base ingest skill, installed as a `dsh.bundle` skill-pack with two-level validation).
- [GanyuanRan/Aegis](https://github.com/GanyuanRan/Aegis) — Software-engineering method pack: baseline-first planning, systematic debugging, and verification before completion.
- [gongyijie85/dsh-ecc](https://github.com/gongyijie85/dsh-ecc) — 273 ECC skills ported from a large operator-system skill catalog.
- [hackerFish/awesome-dsh-skills](https://github.com/hackerFish/awesome-dsh-skills) — 12 tested engineering skills, each passing a format validator and an isolated load smoke test.
- [hatsuyuki0103/oh-my-deepseek-harness](https://github.com/hatsuyuki0103/oh-my-deepseek-harness) — OMX-style workflow skills: deep-interview, ralplan, ralph, autopilot, team, code-review, and more.
- [Ikalus1988/MisakaNet](https://github.com/Ikalus1988/MisakaNet) — Failure-recovery memory with BM25 + semantic RAG retrieval over past engineering sessions.
- [dhicoc/dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) — 85-skill pack for reverse engineering and authorized pentesting/security research.

- [sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills) — 88 source-verifiable Agent Skills with a native DSH installer targeting `.dsh/skills`, covering research, social intelligence, marketing, and business workflows including multi-source evidence validation.
- [Daive1119/local-ocr](https://github.com/Daive1119/local-ocr) — Offline local OCR skill for vision-less models: Windows native engine first (RapidOCR/Tesseract fallback), images + PDF, structured JSON output with confidence semantics, zero cloud cost.
- [YTyangtao666/dsh-skills-bridge](https://github.com/YTyangtao666/dsh-skills-bridge) — Mount your existing Claude Code skills (~/.claude/skills, ~/.agents/skills, custom dirs) into DSH as a native SkillProvider: frontmatter auto-normalized (when_to_use→whenToUse), rank-250 conflict policy, optional hot-reload, zero runtime deps.
- [PerryLink/dsh-plugin-upgrade-015](https://github.com/PerryLink/dsh-plugin-upgrade-015) — Merged, version-locked plugin upgrade skill: 0.1.3-alpha.1 → 0.1.5-rc.1 as two closed legs — an evidence-bound version card plus a zero-dependency 20-seam scanner.
- [weibaohui/skills-management](https://github.com/weibaohui/skills-management) — Skill marketplace and manager: manage skills from all local coding agents (10+ executors, incl. Claude Code and Codex) in one page and import them into the DSH skill library; built-in market of 6600+ skills, per-skill token-overhead stats, and model visibility control.


### Workflow & Automation

- [1052326311/dsh-plan-lattice](https://github.com/1052326311/dsh-plan-lattice) — Persistent execution contracts and recursive work graphs for long or underspecified tasks.
- [940842546/dsh-permissions](https://github.com/940842546/dsh-permissions) — Claude Code-style permission tiers (hard/deny/ask/allow) with workspace-scoped rules.
- [alib8b8/dsh-plugin-aflare](https://github.com/alib8b8/dsh-plugin-aflare) — Deterministic YAML workflow DAGs with WAL crash recovery and Saga compensation, 300+ templates.
- [apheli0os/deepseek-harness-orchestrate](https://github.com/apheli0os/deepseek-harness-orchestrate) — Declarative task-DAG orchestration with parallel topological execution.
- [biociao/dsh-science](https://github.com/biociao/dsh-science) — Research workbench: ReAct research loop, versioned artifacts with provenance, and science skills.
- [btspoony/dsh-advisor](https://github.com/btspoony/dsh-advisor) — Pairs a second model that passively reviews each turn and injects notes.
- [chenzhi-clude/dsh-hooks-pack](https://github.com/chenzhi-clude/dsh-hooks-pack) — One-click Claude Code & Codex hooks for DSH: auto-discovers existing ~/.claude / ~/.codex hook config and runs it on the official bridge plugins, with an explicit sandbox-policy shim so hook commands never die silently.
- [ChongCyrus/Vibe-Mathematics](https://github.com/ChongCyrus/Vibe-Mathematics) — Multi-agent math solving: brainstorm → solve → multi-verifier debate → verified knowledge base.
- [cloader/dsh-taskboard](https://github.com/cloader/dsh-taskboard) — Task board with project/model assignment and cron scheduling.
- [EvilIrving/dsh-proof](https://github.com/EvilIrving/dsh-proof) — Independent read-only acceptance layer verifying each turn before it closes.
- [fakechris/dsh-track](https://github.com/fakechris/dsh-track) — Embedded task management engine: decision-point protocol, idea capture wall, Linear-style issue store.
- [february2015/dsh-taskswarm](https://github.com/february2015/dsh-taskswarm) — Dependency-ordered task waves run in parallel git-worktree lanes with cross-model review and crash recovery.
- [Jokasa7/dsh-product-subagent-console](https://github.com/Jokasa7/dsh-product-subagent-console) — Conversation-native multi-Agent planning and observability: editable task graphs, real child-session trees, plan-versus-run comparison, scoped recovery previews, and reusable run evidence.
- [dickpy/dsh-cloud-sync](https://github.com/dickpy/dsh-cloud-sync) — Syncs DSH profiles and plugin archives through WebDAV/S3-compatible storage with encrypted snapshots.
- [PerryLink/dsh-github](https://github.com/PerryLink/dsh-github) — Official-grade GitHub CI integration: a composite action, polling PR review bot with idempotent inline comments, a status-check gate, and approval-gated PR/issue tools.
- [PerryLink/dsh-lsp-actions](https://github.com/PerryLink/dsh-lsp-actions) — LSP action surface: diagnostics, formatting, completion, code actions, symbols, signature help, inlay hints and rename over real language servers.
- [PerryLink/dsh-team-rooms](https://github.com/PerryLink/dsh-team-rooms) — Persistent, cross-session multi-agent team rooms for DeepSeek Harness: members, a message bus, a shared task board, and a shared timeline that survive restarts.
- [weibaohui/dsh-tasks](https://github.com/weibaohui/dsh-tasks) — Scheduled tasks: run a prompt on cron schedules, each run opens a new agent session to do the work, with workspace binding, manual run, session auto-naming, and a fullscreen task management page.
- [weibaohui/dsh-process](https://github.com/weibaohui/dsh-process) — Process management: brings ntd-style processes (multi-stage, multi-step agent workflow templates) into the dsh web UI — browse, edit, validate, import/export and AI-generate processes; the built-in library is read-only while the personal library is writable with live file sync, and agents read the library through process_* tools and advance work stage by stage.

### Notifications & Integrations

- [2006spy/dsh-token-billing](https://github.com/2006spy/dsh-token-billing) — Real-time token billing with official CNY pricing and automatic peak/off-peak switching.
- [AbcdefgXW/dsh-msg-hub](https://github.com/AbcdefgXW/dsh-msg-hub) — IM channel bridge (WeChat/QQ/Feishu) with proactive push to your phone.
- [AI-Galaxy-GPU/dsh-sound](https://github.com/AI-Galaxy-GPU/dsh-sound) — Per-event sound notifications for completion, approval, question, and task-failure.
- [Alan2Z/dsh-speak](https://github.com/Alan2Z/dsh-speak) — Voice-announces the final reply via native OS voices on Windows and macOS.
- [alanpaul1969/dsh-agent-sticky-note](https://github.com/alanpaul1969/dsh-agent-sticky-note) — Agent-to-human notice board: renders pending decisions, notices, and version updates your agent (or background cron/headless workers) writes to a note file, as a Settings tab — survives chat floods and remote (Tailscale) sessions.
- [amlyczz/dsh-lark-link](https://github.com/amlyczz/dsh-lark-link) — High-reliability Feishu/Lark bridge with QR auth and card-based approval commands.
- [aokamoaki/dsh-notify](https://github.com/aokamoaki/dsh-notify) — Windows toast + sound on turn done/error/goal, plus ask & approval alerts.
- [Dawn388887/dsh-notify](https://github.com/Dawn388887/dsh-notify) — Windows desktop toast + remote-device browser notifications (Service Worker) when a session agent finishes or errors, with a /notify command and Settings toggle.
- [BiBoyang/dsh-im-bridge](https://github.com/BiBoyang/dsh-im-bridge) — Two-way WeChat bridge with in-chat approve/reject and message injection.
- [Bing-Bryan/dsh-unread-dot](https://github.com/Bing-Bryan/dsh-unread-dot) — macOS Dock badge and chime built on the Badging API.
- [cdxiaodong/dsh-island](https://github.com/cdxiaodong/dsh-island) — Bridges sessions, tool calls, and approvals to the macOS notch panel.
- [Pasumao/dsh-plugin-notify](https://github.com/Pasumao/dsh-plugin-notify) — Windows native toasts plus a system-tray whale icon when the agent stops (done/error/waiting/closed), zero dependencies.
- [PGZXB/dsh-feishu](https://github.com/PGZXB/dsh-feishu) — Feishu (Lark) UI for DeepSeek Harness: panel-driven control console, in-card approvals and questions, live streaming cards, one-QR setup.
- [shangjian2023/dsh-rss-daily](https://github.com/shangjian2023/dsh-rss-daily) — Daily news digest: fetches 46 curated RSS sources on schedule, LLM-edits them into a briefing with the model already configured in dsh (rule-based fallback), and delivers it to your IM via webhook (WeCom/Telegram/ServerChan/PushDeer/Bark/Gotify), with catch-up for missed runs and a Web panel.
- [temotee2103/dsh-overdrive](https://github.com/temotee2103/dsh-overdrive) — Multi-platform chat gateway for DeepSeek Harness (WhatsApp, Telegram, Discord, Slack, Feishu, DingTalk, WeCom) with in-chat trajectory replay, subagents, cron scheduling and tap-to-approve buttons.
- [ttmouse/dsh-dingtalk-channel](https://github.com/ttmouse/dsh-dingtalk-channel) — DingTalk IM channel via Stream-mode WebSocket: each chat drives its own tooled agent; replies stream back as messages, no public callback URL needed.
- [PerryLink/dsh-auto-review](https://github.com/PerryLink/dsh-auto-review) — Second-model auto-review on the approval answerer chain: a read-only reviewer subagent returns structured allow/deny verdicts, fail-closed by default.
- [PerryLink/dsh-defend](https://github.com/PerryLink/dsh-defend) — Prompt-injection, jailbreak, and secret-leak detection with allow/ask/block interception across user messages, tool arguments, and tool results.
- [PerryLink/dsh-mask](https://github.com/PerryLink/dsh-mask) — PII masking middleware: anonymize names, phones, emails, ID cards, bank cards, keys, and addresses before the model boundary and restore them at display; plaintext is never logged.
- [PerryLink/dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules) — Declarative Claude Code-style allow/deny/ask permission rules plus a Codex-style process-level network policy with a built-in local HTTP/CONNECT proxy.
- [UllrAI/dsh-mqtt](https://github.com/UllrAI/dsh-mqtt) — MQTT agent gateway for submitting, steering, observing, and cancelling DSH sessions over authenticated or TLS broker connections.
- [xmanrui/dsh-im](https://github.com/xmanrui/dsh-im) — Connects DeepSeek Harness to Feishu, WeChat, DingTalk, WeCom, QQ, Slack, Telegram, Discord, and WhatsApp through one settings page, using QR codes, an app manifest, or bot credentials.
- [PerryLink/dsh-reach](https://github.com/PerryLink/dsh-reach) — Pushes DSH approval and question cards to IM channels (WeChat first) and answers them from chat, with a session console and per-channel security.
- [PerryLink/dsh-ticktick](https://github.com/PerryLink/dsh-ticktick) — TickTick (Dida365) task bridge: a session-header task panel and curated agent tools over the official TickTick MCP endpoint.

### Git & Engineering

- [DamonKoy/dsh-web-ui#dsh-git-graph](https://github.com/DamonKoy/dsh-web-ui/tree/main/packages/dsh-git-graph) — Git branch selector and Git graph in the conversation header.
- [No-PRM/dsh-explorer](https://github.com/No-PRM/dsh-explorer) — Git-first file-tree sidebar: VS Code-style indent guides, M/A/U/D/R decorations, HEAD-vs-worktree diff preview, drag-to-reference.
- [WhitePlusMS/dsh-git-graph](https://github.com/WhitePlusMS/dsh-git-graph) — Dedicated read-only Git Graph view: commit topology, local/remote/tag refs, working-tree status, search and filtering.
- [Wongzexu/dsh-git-status](https://github.com/Wongzexu/dsh-git-status) — Git status drawer with a commit DAG lane graph, uncommitted changes and stash rows, inline diffs, one-click fetch from all remotes.
- [a179-sanae/dsh-code-check](https://github.com/a179-sanae/dsh-code-check) — Runs `tsc --noEmit` after edits and reports errors via a `code_check` tool.
- [AngelosZou/graphlint](https://github.com/AngelosZou/graphlint/tree/main/integrations/dsh) — Dead-code detection for AI-generated codebases via dependency-graph reachability.
- [loadingvx/deepseek-harness-workbench-plugin](https://github.com/loadingvx/deepseek-harness-workbench-plugin) — Full IDE workbench inside the Web UI: multi-tab editing, workspace terminal, file tree, and SCM (stage/commit/push/pull, branch switch, git graph, inline diffs).
- [temotee2103/dsh-ci-co-pilot](https://github.com/temotee2103/dsh-ci-co-pilot) — GitHub CI co-pilot for DeepSeek Harness: PR review, CI failure fixing, issue triage and release notes.
- [weibaohui/dsh-sync](https://github.com/weibaohui/dsh-sync) — Multi-machine sync: keeps multiple dsh replicas consistent through one private GitCode repository — skills, sessions, settings and plugin manifests each with an independent switch; changes go through branch, PR and merge, remote-only additions are pulled back before every push so nothing is deleted, and an AI smart-align step semantically merges files both sides changed (plus one-click conflict resolution); private repos enforced, pull never overwrites local edits.
- [maxmilian/dsh-forge](https://github.com/maxmilian/dsh-forge) — Read-only Gitea and Forgejo tools for self-hosted instances: repositories, issue and pull request search, PR diffs and changed files, and Actions runs, jobs and job logs.
- [weibaohui/dsh-git-server](https://github.com/weibaohui/dsh-git-server) — Git server: embeds ts-gogs (a TypeScript reimplementation of Gogs) and serves a full Git service on its own port — HTTP clone/push, web UI, issues/PRs/wiki — reusing user-management credentials, start/stop from the settings page.

### Security & Governance

- [KongFangXun/sofagent](https://github.com/KongFangXun/sofagent) — Commit-time agent governance harness: 24 deterministic audit rules over git diffs (secrets, out-of-scope edits, blind modifications, prompt-injection traces), HMAC-chained tamper-evident history, DSH plugin family via SkillHub.
- [cdxiaodong/dsh-guardian](https://github.com/cdxiaodong/dsh-guardian) — Agent security guardrail: intercepts and audits every tool call, requiring human confirmation on sensitive operations.
- [JohnXu22786/secret-guard](https://github.com/JohnXu22786/secret-guard) — Blocks agents from reading or writing sensitive files (.env, credentials, keys), masks leaked secret-shaped values, and keeps an audit journal.
- [LeslieWylie/dsh-fleet-audit](https://github.com/LeslieWylie/dsh-fleet-audit) — Read-only agent-fleet credential-hygiene audit: file permissions, embedded credentials in git remotes, provider-token literal counts.
- [863683348/dsh-gov](https://github.com/863683348/dsh-gov) — Agent governance: policy-based tool gating, a structured JSONL audit trail, per-agent token quotas.
- [odai-dsh-plugin](https://github.com/orziz/odai/tree/main/dsh/plugin) — Profile-wide DSH governance and routing with a Web Control Center for responsibility and evidence inspection, plus compaction, scoped semantic memory, safety continuity, and verified delivery; compatible with DSH 0.1.5-rc.1.
- [863683348/dsh-plugin-gate](https://github.com/863683348/dsh-plugin-gate) — Installation safety gate: antivirus-style scan of install scripts and permissions before `dsh plugin add`.
- [dfycaly98931680/dsh-trajectory-governance](https://github.com/dfycaly98931680/dsh-trajectory-governance) — Rebuilds session logs into multi-branch trajectory trees, detects loop deadlock, invalid retry, and goal drift, with cost-attributed alerts.
- [DamonKoy/dsh-plugins (dsh-approve-for-me)](https://github.com/DamonKoy/dsh-plugins/tree/main/packages/dsh-approve-for-me) — Auto-approves read-only tools and auto-denies dangerous commands via a fail-closed policy engine.
- [PerryLink/dsh-fast](https://github.com/PerryLink/dsh-fast) — Read-only performance diagnostics: session load timing, spill hits, compaction stats, context-injection token share, and LLM cache hit rate via /fast and fast_report.
- [PerryLink/dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) — MCP management console for the official DSH MCP client: /mcp health diagnostics, a Settings MCP tab with approval-gated server CRUD, and a tool trial console.
- [PerryLink/dsh-observe](https://github.com/PerryLink/dsh-observe) — OpenTelemetry and Langfuse observability exporter: turn/step/tool/LLM spans, token and cost metrics, sanitized capture, batching, and bounded offline buffering.
- [Raphaelutumn/dsh-change-budget](https://github.com/Raphaelutumn/dsh-change-budget) — Configurable per-turn budgets limiting distinct files, mutation calls, and payload bytes before file-mutation tools run.
- [liuqingman/dsh-hawkeye-scan](https://github.com/liuqingman/dsh-hawkeye-scan) — AI-driven source-code security scanning workbench: 5 model tools (start/finding/status/report/list) plus a /hawkeye web UI and JSON/Markdown/HTML vulnerability reports; zero-dependency Cordis plugin, installable as agent preset or npm package.
- [accpowered/dsh-credential-manager](https://github.com/accpowered/dsh-credential-manager) — Named credential manager: the model uses API keys, tokens, and logins by reference; secrets are injected into each shell run as `DSH_CM_*` env vars and never enter the conversation.
- [accpowered/dsh-auto-review](https://github.com/accpowered/dsh-auto-review) — LLM auto-review for sandbox-escalation approvals under the `'auto'` policy: deterministic filter plus a clean-context reviewer model, fail-closed on every error path; requires a patched harness core (patches in core-patches/).
- [weibaohui/user-management](https://github.com/weibaohui/user-management) — Login gate for the dsh web UI: unauthenticated visitors get a login/register page and the first registrant becomes admin; includes user and role management plus login and access audit logs.
- [maxmilian/dsh-sonarqube](https://github.com/maxmilian/dsh-sonarqube) — Read-only SonarQube Community Build tools: Quality Gate for a branch or pull request, issue and Security Hotspot search, and coverage, duplication or caller-selected measures.

- [Ox0400/dsh-vault](https://github.com/Ox0400/dsh-vault) — Encrypted local credentials vault for dsh: a web settings page and vault_* tools for passwords, API keys, TOTP secrets and cards, with health audits, expiry rotation, imports/exports and read-only/ask access modes.
- [SiriLee/dsh-edit-approval](https://github.com/SiriLee/dsh-edit-approval) — Per-edit approval gate: red/green line diff review before write/edit/stream operations, optional bash-command approval (default off), fully configurable.
### Remote Access & Mobile

- [jayantTang/DSH_Mobile](https://github.com/jayantTang/DSH_Mobile) — DSH Mobile：把电脑上的 DSH 装进 iPhone。原生 SwiftUI 客户端 + 电脑侧连接器（npm `dsh-plugin-mobile-link`）+ 可自建的公网中转；手机在 4G/5G 上直连自己电脑的 DSH，不需要公网 IP 或 Tailscale。
- [Phant0Meow/dsh-meow-smooth](https://github.com/Phant0Meow/dsh-meow-smooth) — Mobile-first UX polish for the DSH Web UI (composer auto-fold, compact mobile sidebar/header/settings, zoom lock) plus notifications when AI finishes long tasks or asks for permission (in-page cards, Web Push, Bark webhook); zero dsh changes, Tailscale phone-access guide included.
- [xgone/dsh-remote](https://github.com/xgone/dsh-remote) — Secure remote access for the DSH Web UI: account/password login gate, MFA/TOTP, role-based access, and an allowlisted in-browser file preview panel.
- [mrRisega/dsh-remote](https://github.com/mrRisega/dsh-remote) — Password-gated reverse-proxy gateway to control the DSH Web UI from a phone browser with full feature coverage (including privileged methods): loopback masquerading, WebSocket passthrough, login rate limiting, optional TLS, LAN or public reverse-proxy deployment.
- [Dawn388887/dsh-fileview](https://github.com/Dawn388887/dsh-fileview) — In-GUI file viewer/editor for remote browsers: same-origin fenced, path-allowlisted, encoding-preserving saves.
- [hutao562/dsh-remote-dsh](https://github.com/hutao562/dsh-remote-dsh) — Adds a row at the top of the sidebar that switches the whole Web GUI to another DSH host reached over a loopback port, with that host's session state on the row (running, unread activity, or waiting for your answer).
- [xgone/dsh-netshell](https://github.com/xgone/dsh-netshell) — Local and remote SSH terminals for DeepSeek Harness Web, with three permission levels, human approval for risky AI commands, and encrypted credential storage.

- [weibaohui/dsh-webdav-server](https://github.com/weibaohui/dsh-webdav-server) — WebDAV server: turns a shared directory into a WebDAV service that Windows, macOS and Linux can mount as a local disk, with token authentication, optional read-only mode, configurable directory/port/token, and per-platform mounting guides built into the settings page.

### Output & Deliverables

- [Devin-AXIS/deepseek-design#deepseek-idesign](https://github.com/Devin-AXIS/deepseek-design/tree/main/packages/deepseek-idesign) — Visual design studio for websites, prototypes, posters, and reports, with templates and direct element editing.
- [taxueseek/dsh-files](https://github.com/taxueseek/dsh-files) — File upload with color-coded attachment cards (session-isolated storage, sha256 dedup) plus a content-sniffing document-read tool for PDF/DOCX/XLSX/TXT.
- [SenmuuuuW/dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) — Deterministic agent reports from session logs: cost & token breakdown, collaboration review, live provider balance, PDF/PNG/HTML export.
- [beijingwahw/dsh-companion](https://github.com/beijingwahw/dsh-companion) — Smart conversation export (Markdown/PDF/JSON/PNG long-image) with privacy redaction and batch ZIP.
- [Nothree-code/folder-tree-sh](https://github.com/Nothree-code/folder-tree-sh) — Workspace file tree with multi-tab preview (text/DOCX/PDF/Markdown/CSV/images) and inline Markdown editing.
- [263311487-ux/dsh-verify](https://github.com/263311487-ux/dsh-verify) — Independent browser acceptance testing for agent deliverables: JSON spec in, real Chromium verdict out (PASS/FAIL with screenshots). MCP server + CLI + GitHub Action, works with any agent and CI.

### Domain & Specialist

- [863683348/dsh-plugin-academic-writing](https://github.com/863683348/dsh-plugin-academic-writing) — Academic writing toolkit: paper outlines, title/abstract skeletons, GB/T 7714 / APA / MLA citations, pre-submission checklist.
- [863683348/dsh-plugin-finance-data](https://github.com/863683348/dsh-plugin-finance-data) — Finance data toolkit: currency formatting (incl. Chinese wan/yi units), return/CAGR math, valuation ratios, risk metrics.
- [Asher-2000/dsh-expert-mode](https://github.com/Asher-2000/dsh-expert-mode) — Bilingual expert-mode preset: chief coordinator + domain-expert subagents (data analyst, legal review, product, frontend, growth, quant finance) with automatic task delegation.
- [literaf/dsh-ai4scholar](https://github.com/literaf/dsh-ai4scholar) — Academic search across Semantic Scholar, PubMed, Google Scholar, arXiv, bioRxiv/medRxiv, and DOI resolution, with citation graphs and auto-cite.
- [pengpengyi92/dsh-quant](https://github.com/pengpengyi92/dsh-quant) — Quantitative R&D toolkit: 46 tools across market data, indicators, factor evaluation, walk-forward ML validation, risk, options, bonds, fund simulation.
- [poplarity/dsh-science-workbench](https://github.com/poplarity/dsh-science-workbench) — Reproducible science workbench: agent-driven cells, inline figures with feedback/rerun, manifest provenance, environment snapshots, and publication-grade figure skills (9 `bio_*` tools + workbench UI).
- [Realyujie/dsh-us-stocks](https://github.com/Realyujie/dsh-us-stocks) — US stock quotes, price history, financial statements, analyst consensus and news.
- [wade20250715/dsh-pubmed](https://github.com/wade20250715/dsh-pubmed) — PubMed deep-research toolset: literature search, author investigation, same-name disambiguation, institution statistics.
- [xmutfyh/dsh-plugin-writing-guard](https://github.com/xmutfyh/dsh-plugin-writing-guard) — Academic writing guard: removes AI-style defensive writing, protects scientific evidence, calibrates tone toward a target journal.
- [kentleenot/dsh-trading-toolkit](https://github.com/kentleenot/dsh-trading-toolkit) — A-share and US stock trading toolkit for DSH agents: realtime quotes, OHLCV klines, ADX three-state regime signals and simple backtest previews via EastMoney. Read-only, never places orders.
- [liyc-sys/dsh-fixed-income-skills](https://github.com/liyc-sys/dsh-fixed-income-skills) — Fixed-income / credit skills: issuer rating-migration watch (fundamentals + market-implied spread + catalysts) and rate-scenario analysis (historically anchored curve scenarios with duration-based exposure impact). Ported from the LLMQuant financial Agent Skills library.
- [PerryLink/dsh-industry-research](https://github.com/PerryLink/dsh-industry-research) — Deterministic industry research reports for DeepSeek Harness: company and industry research flows produce structured, verifiable reports from staged evidence.
- [PerryLink/dsh-research-report](https://github.com/PerryLink/dsh-research-report) — Verifiable research-report engine with a content-addressed evidence ledger, versioned sealed reports where every claim carries a verification verdict, and retrieval orchestration over ctx.web and ctx.jobs.
- [PerryLink/dsh-fund-research](https://github.com/PerryLink/dsh-fund-research) — Deterministic research reports for Chinese public mutual funds: performance decomposition, holdings penetration, style attribution and manager profiles, with per-number snapshot traceability.
- [weibaohui/experts-management](https://github.com/weibaohui/experts-management) — Expert manager: manage ntd-format experts and expert teams (plugin.json + Agent MD + skill sets), browse and install from a built-in market of 50+ experts, and run tasks in an expert persona via /expert-<name> without consuming model directory tokens.
- [Haniubub/seo-toolkit](https://github.com/Haniubub/seo-toolkit) — Full local & technical SEO audit toolkit for DSH: deterministic Python measurement (53 scripts) + LLM judgment (24 sub-skills, 18 agents), weighted scoring, gated multi-agent fan-out, schema.org, E-E-A-T, GBP, GEO/AI Overviews. ~4¢ per audit.
- [Flan246/dsh-lit-search](https://github.com/Flan246/dsh-lit-search) — Academic literature search, citation formatting (GB/T 7714 / APA / BibTeX) and related-works tools, powered by Crossref + OpenAlex with no API key. Install via `dsh plugin add dsh-lit-search`.
- [Flan246/dsh-latex-guard](https://github.com/Flan246/dsh-latex-guard) — LaTeX compile check (auto xelatex/lualatex detection) plus BibTeX lint, field-fill and cite-audit tools. Install via `dsh plugin add dsh-latex-guard`.

- [shiyan688/dsh-novel-craft](https://github.com/shiyan688/dsh-novel-craft) — Novel-writing workbench that learns the author's taste: mark 👍/👎 while reading draft variants (keyboard j/k/G/B), and the marks are distilled into reusable writing rules — only the rules reach the writing context (three explicit, capped exceptions, documented in the README). Also ships: new-chapter workflow (scene-decision directions → candidate drafts → passage picking → merged final draft), note-driven revision that rewrites *only* the annotated paragraphs with character-exact verification, and local plot/ledger checks that never feed the manuscript to a model. 775 assertions; verified on dsh 0.1.5-rc.1/rc.2. Installable via `dsh plugin --profile web add dsh-novel-craft`.

### Development & Runtime

- [MajidAsghariTabrizi/universal-engineering-agent](https://github.com/MajidAsghariTabrizi/universal-engineering-agent) — Profile-agnostic, runnable, MIT reference implementation of the UEA 9-stage operating-kernel contract. Inspect → plan → implement → verify → classify → recover → test → generalize. Zero runtime deps. ([DSH #5513](https://github.com/deepseek-ai/deepseek-harness/discussions/5513))
- [863683348/dsh-plugin-verify](https://github.com/863683348/dsh-plugin-verify) — Evidence-based claim checking against workspace files with line citations.
- [863683348/dsh-trend-radar](https://github.com/863683348/dsh-trend-radar) — Ecosystem trend dashboard: new plugins, star gainers, category heat, keyword radar.
- [ai-eks/dsh-auth-tunnel](https://github.com/ai-eks/dsh-auth-tunnel) — Password-gated public access through Cloudflare Tunnels with an in-app directory picker.
- [Airmetro/dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) — Compares the harness and every plugin against npm/GitHub releases with one-click updates and rollback.
- [aokamoaki/dsh-startup-guard](https://github.com/aokamoaki/dsh-startup-guard) — Repairs corrupt session logs and quarantines crash-causing bundles so a broken plugin can't brick startup.
- [ayahunter/dsh-plugin-clinic](https://github.com/ayahunter/dsh-plugin-clinic) — Read-only health check of the installed plugin set: loader health, dependency integrity, install-script risk.
- [Pasumao/dsh-plugin-dev-kb](https://github.com/Pasumao/dsh-plugin-dev-kb) — Offline plugin-development knowledge base: full mirror of the official docs (168 pages) plus repo extras, with topic navigation and full-text search for the agent.
- [fakechris/dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) — Self-healing ops toolbox: daily-snapshot A/B rotation with acceptance-gated atomic switch and rollback, a 10s watchdog that auto-relaunches the web and resumes interrupted turns, and an out-of-band dsh-doctor for when web and agent are both down.
- [kanneiren/dsh-network-settings](https://github.com/kanneiren/dsh-network-settings) — Visualize the DSH process network path on Windows or WSL with layered DNS/TCP/TLS/HTTP probes, detect stale proxy configuration, and apply snapshot-guarded repairs.
- [Linxiushen/dsh-workflow-isolate](https://github.com/Linxiushen/dsh-workflow-isolate) — Runs model-written workflows in a fresh QuickJS/WASM runtime with bounded memory, execution fuel, wall time, and child-agent fan-out.
- [beihzb/dsh-notebook](https://github.com/beihzb/dsh-notebook) — Native Jupyter-style notebook: real ipykernel sidecar, VS Code-aligned cell UI, tqdm progress, inline figures, per-cell AI revision.

- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) — Local-first runtime whose installable `managed-agents` DSH plugin exposes six MCP tools for persistent sessions, streamed turns, artifacts, cancellation, audit/replay, and local/Docker/Kubernetes/self-hosted-worker sandboxes.
- [chunfenxiazhi-collab/dsh-stability-audit](https://github.com/chunfenxiazhi-collab/dsh-stability-audit) — Stability audit for installed dsh plugins: static risk grading (hook surface, startup work, inject, entry, dep ranges) plus optional isolated install verification.
- [sylkmpo/dsh-web-app-launcher](https://github.com/sylkmpo/dsh-web-app-launcher) — Runs dsh web like a Windows desktop app while the native web UI stays the engine (no Electron, no fork): auto-creates a DeepSeek Harness.lnk shortcut that opens the Web UI in a frameless Edge/Chrome/Brave/Vivaldi app window and exits the harness when the window closes.
- [PerryLink/dsh-plugin-kit](https://github.com/PerryLink/dsh-plugin-kit) — Plugin-authoring toolkit for DeepSeek Harness: shared provider seams, a bundle skeleton and family conventions (npm @perrylink/dsh-plugin-kit).
- [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) — Zero-dependency static + sandbox smoke detector for DeepSeek Harness plugins: R/K/D/CC four-layer checks.
- [PerryLink/dsh-cert-mcp](https://github.com/PerryLink/dsh-cert-mcp) — Read-only MCP server exposing the dsh-plugin-certification registry: grades, snapshot dates and five-dimension evidence.

### Plugin Markets & Managers

- [sandbaseai/dsh-plugin-store](https://github.com/sandbaseai/dsh-plugin-store) — Native Settings marketplace for discovering, filtering, installing, and managing the community catalog, with separate Community and Installed views.
- [1e0zj/dsh-plugin-mall](https://github.com/1e0zj/dsh-plugin-mall) — Live GitHub `dsh-plugin` topic search with per-repo manifest verification and anti-squatting checks.
- [863683348/dsh-insight](https://github.com/863683348/dsh-insight) — Plugin insight center: needs-matching, environment recipes, health scoring, security audit verdict.
- [863683348/dsh-need-finder](https://github.com/863683348/dsh-need-finder) — Requirement-driven plugin discovery matching natural-language needs to a curated directory.
- [863683348/dsh-plugin-audit](https://github.com/863683348/dsh-plugin-audit) — Ecosystem-wide health audit: maintenance/docs/downloads scoring, security scan, web leaderboard.
- [863683348/dsh-recipe](https://github.com/863683348/dsh-recipe) — Scenario bundles of plugins ("dotfiles for the plugin world") with ordered install sequences.
- [alex04130/dsh-forge](https://github.com/alex04130/dsh-forge) — Runtime extension suite: cross-session mailbox, agent teams, subagent spawn policy, plugin market.
- [DshMarketPlace/dsh-plugins-store](https://github.com/DshMarketPlace/dsh-plugins-store) — Browse and install DSH plugins from inside the harness through `/store`, a Settings tab, and agent search/install tools, with approval-gated installs.
- [huguangyu666/dsh-store](https://github.com/huguangyu666/dsh-store) — npm-authoritative catalog plus curated list (550+ plugins), with quality verification.
- [icefall7/dsh-plugin-scout](https://github.com/icefall7/dsh-plugin-scout) — Scouts every `dsh-plugin`-tagged repo and judges each as worth trying, watching, or skipping.
- [chenzhi-clude/dsh-plugin-market](https://github.com/chenzhi-clude/dsh-plugin-market) — AI-native marketplace with a machine-readable registry (all.json + llms.txt) built for agent-driven plugin search and one-command install.
- [weibaohui/dsh-fde-tools](https://github.com/weibaohui/dsh-fde-tools) — FDE toolbox bundle: installing this one plugin pulls in a curated set of common dsh plugins (git server, WebDAV mount, knowledge base, scheduled tasks, auto-resume, UI tweaks, auto-retrospection, file manager, smart titles, task board, plugin market, context trimmer, IM bridge, sidebar enhancements), with a panel showing install status and one-click gap-filling.
- [Noob-stupid/dsh-plugin-hub](https://github.com/Noob-stupid/dsh-plugin-hub) — DSH plugin management panel and marketplace: one-click enable/disable, multi-source search (GitHub/Gitee/custom), static plugin & skill index, suite/skill install, source management, and one-click framework upgrade with auto-rollback.

### Just for Fun

- [AmeKrance/anan-thermal-monitor](https://github.com/AmeKrance/anan-thermal-monitor) — Desktop pet showing real-time CPU/RAM/GPU/NVMe temperatures.
- [anneheartrecord/dsh-desk-pet](https://github.com/anneheartrecord/dsh-desk-pet) — macOS desk pet in a real always-on-top window rather than a page widget: six states driven by local DSH, and a bundled skill that turns one photo into a whole skin.
- [Awu12277/dsh-stock-watch](https://github.com/Awu12277/dsh-stock-watch) — A-share watchlist with intraday and candlestick charts in a collapsible popup.
- [hellodigua/dsh-emoji](https://github.com/hellodigua/dsh-emoji) — Automatically adds emojis to AI replies.
- [HuanLinOTO/dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) — Pops up a mini-game menu (wordle, match-3) while the model generates.
- [JAdpp/dsh-whale-galgame](https://github.com/JAdpp/dsh-whale-galgame) — Multi-character Galgame conversation view with affection, memory, and CG galleries.
- [Laplace-bit/dsh-pianist](https://github.com/Laplace-bit/dsh-pianist) — Piano performance plugin: ask the agent to play a piece and it renders on a Canvas2D grand piano with real Salamander Grand samples and a playable 88-key keyboard.
- [jitengfei/dsh-whale-arcade](https://github.com/jitengfei/dsh-whale-arcade) — Floating browser-local arcade with score games for breaks while waiting on the agent.
- [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) — Side-panel arcade with 18 offline mini-games.
- [lucky8197/dsh-devquest](https://github.com/lucky8197/dsh-devquest) — Turns coding into an RPG: XP, 27+ achievement badges, levels, and seasons.
- [minybear/DeepSeek-Harness-Pet](https://github.com/minybear/DeepSeek-Harness-Pet) — Codex-style desktop pet mirroring the agent's running state.
- [Nagi-ovo/dsh-ads](https://github.com/Nagi-ovo/dsh-ads) — Parody ads in 2005-Chinese-web style. All fictional.
- [nickkkkkk123123/dsh-whale-girl](https://github.com/nickkkkkk123123/dsh-whale-girl) — Interactive whale-girl desktop pet for DeepSeek Harness: live balance/usage/context occupancy, middle-button slingshot toss, easter-egg bubbles, eco mode. 346KB package, zero extra processes.
- [Sutera-Diffusus/dsh-whale-musume](https://github.com/Sutera-Diffusus/dsh-whale-musume) - Whale-girl desktop pet for the DSH Web UI: pat-to-raise growth, live work-state poses, 494 dialogue lines, 30 achievements and a built-in settings panel - all local, zero telemetry.
- [ywleeo/dsh-md-preview](https://github.com/ywleeo/dsh-md-preview) — Sidebar workspace-row trigger opens a Markdown preview panel: nested collapsible directory tree, inline rendering, theme-aware, open in the system default app.
- [dsh-persona-switcher](https://github.com/destr-z/dsh-persona-switcher) — Lightweight per-session persona switcher: template library in Settings, pick from the composer toolbar, applies instantly; single plugin, zero runtime dependencies, no core changes.
## Writing Your Own Plugin

1. Scaffold a `dsh.bundle` manifest declaring what your plugin extends (model, tool, sandbox, UI, session store, or the agent loop itself).
2. Tag the repo with the [`dsh-plugin`](https://github.com/topics/dsh-plugin) GitHub topic for discoverability.
3. Install locally with `dsh plugin --profile web add <path-or-name>` to iterate.
4. Read [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)'s architecture docs and AGENTS.md before building anything that touches the core agent loop.

## Related Projects

- [awesome-openclaw](https://github.com/Anil-matcha/awesome-openclaw) — curated resources for OpenClaw, the self-hosted messaging-first agent with the largest community skill catalog.
- [awesome-hermes-agent](https://github.com/Anil-matcha/awesome-hermes-agent) — curated resources for Hermes Agent (Nous Research), the self-evolving skill-generating agent.
- [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) — a broader curated hub of open-source generative AI tools and platforms.
- [Generative-Media-Skills](https://github.com/Anil-matcha/Generative-Media-Skills) — agent-skill building blocks for generative media workflows, in the same plugin/skill spirit as `dsh`.

## Contributing

PRs welcome. Keep entries to one line, link the actual plugin repo (not a fork or mirror), and make sure the plugin installs and does what its description says before submitting.

---

⭐ If this saved you time hunting through the plugin ecosystem, star it so others can find it too.
