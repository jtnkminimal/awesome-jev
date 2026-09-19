# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated projects built with [Jev](https://docs.typesafe.ai), TypeSafe's System One model.

Jev answers typed questions — [Choice](https://docs.typesafe.ai/primitives/choice.md), [Noul](https://docs.typesafe.ai/primitives/noul.md) and [Score](https://docs.typesafe.ai/primitives/score.md) — with calibrated probabilities instead of prose, so ordinary code keeps control of the workflow. This list collects what people have built with it.

**136 ranked projects** plus **18 upstream integrations**. Every entry was checked against the repository itself; See [Method](#method).

## Contents

- [Top 25](#top-25)
- [Models and Runtimes](#models-and-runtimes)
- [Agent Tooling](#agent-tooling)
- [Guardrails and Code Review](#guardrails-and-code-review)
- [Search, Ranking and Extraction](#search-ranking-and-extraction)
- [Applications](#applications)
- [Trading and Markets](#trading-and-markets)
- [Benchmarks and Evaluations](#benchmarks-and-evaluations)
- [Games and Fun](#games-and-fun)
- [Framework Integrations](#framework-integrations)
- [Other Lists](#other-lists)
- [Upstream Integrations](#upstream-integrations)
- [Method](#method)
## Top 25

Ranked by an even blend of popularity (log-scaled stars) and how compelling the project is. The *Interest* column is a 0–4 rating from Jev itself, averaged over its probability distribution.

| # | Project | Stars | Interest | Score |
| --: | --- | --: | --: | --: |
| 1 | [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 5.1k | 2.9 | 86.8 |
| 2 | [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 2.9k | 3.0 | 84.5 |
| 3 | [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) | 1.5k | 3.0 | 80.2 |
| 4 | [vercel-labs/ai-cli](https://github.com/vercel-labs/ai-cli) | 800 | 3.0 | 76.2 |
| 5 | [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) | 863 | 2.6 | 71.6 |
| 6 | [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) | 825 | 2.5 | 70.6 |
| 7 | [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | 334 | 2.9 | 70.6 |
| 8 | [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) | 260 | 2.7 | 66.2 |
| 9 | [donvito/ai-backends](https://github.com/donvito/ai-backends) | 145 | 2.8 | 64.7 |
| 10 | [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) | 260 | 2.5 | 64.1 |
| 11 | [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) | 142 | 2.7 | 63.2 |
| 12 | [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) | 58 | 3.1 | 62.4 |
| 13 | [AbdelStark/awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe) | 220 | 2.4 | 62.1 |
| 14 | [yibie/awesome-jev](https://github.com/yibie/awesome-jev) | 137 | 2.6 | 61.3 |
| 15 | [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) | 127 | 2.6 | 60.8 |
| 16 | [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | 224 | 2.3 | 60.1 |
| 17 | [jkudish/jev-browser](https://github.com/jkudish/jev-browser) | 89 | 2.7 | 59.5 |
| 18 | [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) | 70 | 2.7 | 58.6 |
| 19 | [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) | 116 | 2.4 | 57.6 |
| 20 | [hr98w/jev-visual](https://github.com/hr98w/jev-visual) | 102 | 2.4 | 57.3 |
| 21 | [giuliosmall/pg_typesafe](https://github.com/giuliosmall/pg_typesafe) | 76 | 2.5 | 57.2 |
| 22 | [Dicklesworthstone/skillranker](https://github.com/Dicklesworthstone/skillranker) | 44 | 2.8 | 56.8 |
| 23 | [Mapika/decider](https://github.com/Mapika/decider) | 23 | 3.0 | 56.6 |
| 24 | [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) | 30 | 2.9 | 56.0 |
| 25 | [mizchi/jev-playground](https://github.com/mizchi/jev-playground) | 14 | 3.2 | 56.0 |

## Models and Runtimes

*Open reimplementations, local serving, ports and speedups of Jev-style typed decision models.*

- [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) — Semantic ifs from open models, on a 3090 at home. Independent; not affiliated with Jev or TypeSafe. `★ 1.5k`
- [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) — Train a small model that picks among a changing list of text options in one pass. `★ 863`
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) — A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline. `★ 334`
- [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) — Jev-compatible API endpoint based on open models (prefill-only). `★ 142`
- [hr98w/jev-visual](https://github.com/hr98w/jev-visual) — An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos. `★ 102`
- [Mapika/decider](https://github.com/Mapika/decider) — One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B. `★ 23`
- [bnsd55/jevmlx](https://github.com/bnsd55/jevmlx) — Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass. `★ 23`
- [bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) — Local typed decisions, contrastive data curation, and model evaluation. `★ 28`
- [razorback16/openjev](https://github.com/razorback16/openjev) — Open, Jev-compatible System One decision server on DiffusionGemma. `★ 25`
- [genai-craft/openvons](https://github.com/genai-craft/openvons) — openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド. `★ 7`
- [zmtomorrow/typear](https://github.com/zmtomorrow/typear) — Type-Safe Decoding for Autoregressive LLMs. `★ 8`
- [Heman10x-NGU/Verdict-open-jev](https://github.com/Heman10x-NGU/Verdict-open-jev) — Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU… `★ 4`
- [komorra/Eugeniusz](https://github.com/komorra/Eugeniusz) — Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine. `★ 6`
- [mmastrac/djev-spark](https://github.com/mmastrac/djev-spark) — DiffusionGemma NVFP4 structured decisions on a DGX Spark: container recipe. `★ 8`
- [Hoyant-Su/JevSpawn](https://github.com/Hoyant-Su/JevSpawn) — Let a small model decide when to spawn another agent. `★ 1`
- [ziyacivan/s1decide](https://github.com/ziyacivan/s1decide) — An open decision model: typed questions answered in one forward pass, with published calibration and the negative controls that make it honest. `★ 0`
- [AdamPippert/granite-decisions](https://github.com/AdamPippert/granite-decisions) — GraniteJev. `★ 1`

## Agent Tooling

*Harnesses, routers, CLIs, MCP servers, skills and context plumbing.*

- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — i. am. speed. `★ 5.1k`
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are… `★ 2.9k`
- [vercel-labs/ai-cli](https://github.com/vercel-labs/ai-cli) — Generate anything from your terminal. `★ 800`
- [donvito/ai-backends](https://github.com/donvito/ai-backends) — AI API server for common use cases — supports multiple models and providers. Run locally with Ollama or LM Studio, or in the cloud via OpenRouter, OpenAI… `★ 145`
- [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) — Route to the cheapest model in claude code for your task using jev-router. `★ 127`
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — Agent skills for building with TypeSafe's System One API. `★ 224`
- [jkudish/jev-browser](https://github.com/jkudish/jev-browser) — Browser use using Typesafe's Jev model. `★ 89`
- [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) — Standalone mobile agent for Mobilerun, driven by Jev decisions. `★ 116`
- [Dicklesworthstone/skillranker](https://github.com/Dicklesworthstone/skillranker) — Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured… `★ 44`
- [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) — Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn. `★ 30`
- [mizchi/jev-playground](https://github.com/mizchi/jev-playground) — Playground for calling Jev from MoonBit. `★ 14`
- [dbreunig/building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) — A skill for writing and improving programs that call Jev, TypeSafe's System One model. `★ 91`
- [TheoOliveira/pi-jev](https://github.com/TheoOliveira/pi-jev) — Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev. `★ 11`
- [dannote/jev](https://github.com/dannote/jev) — TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer. `★ 12`
- [SawyerHood/sawyer-plugins](https://github.com/SawyerHood/sawyer-plugins) — Sawyer Hood's BB plugins: Cascade, Compact Nav, CoW copy, Miku Companion, SlopCop, and T3 Sidebar in one repository. `★ 14`
- [BorisLeMeec/jev](https://github.com/BorisLeMeec/jev) — A claude code plugin for jev. `★ 4`
- [shantanugoel/ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill) — Skill for Hermes, and other agents, to ask typesafe's jev. `★ 27`
- [nitoba/questions](https://github.com/nitoba/questions) — Define decisions with Zod 4 schemas or typed question batches over async/await and Web Streams. `★ 3`
- [devagrawal09/jev-code](https://github.com/devagrawal09/jev-code) — Bounded TypeSafe Jev workflows for coding agents. `★ 6`
- [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter) — A lightweight Jev-powered router for models, tools, and subagents. `★ 4`
- [AntonioCoppe/jev-harness](https://github.com/AntonioCoppe/jev-harness) — Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job. `★ 2`
- [matthewdonsemail-lab/open-typesafe-camoufox](https://github.com/matthewdonsemail-lab/open-typesafe-camoufox) — CLI that drives a headed Camoufox browser toward a plain-English goal, without sending screenshots. `★ 2`
- [skastr0/prism](https://github.com/skastr0/prism) — Agents, skills, hooks and typed multi-model workflows written once in TypeScript, compiled for a dozen agents. `★ 1`
- [EliaAlberti/jev-rules](https://github.com/EliaAlberti/jev-rules) — Jev picks which of your rules apply to each prompt, so Claude only sees the ones that matter. `★ 5`
- [hqman/JevScout](https://github.com/hqman/JevScout) — Coding-agent skill that hunts AI and software jobs on real company sites. `★ 14`
- [thejorgg/omp-jev](https://github.com/thejorgg/omp-jev) — Jev routing for Oh My Pi, with an opt-in checkpoint orchestrator. `★ 3`
- [chensirui2008/fast-jev-compaction](https://github.com/chensirui2008/fast-jev-compaction) — Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are… `★ 1`
- [mateonunez/jod](https://github.com/mateonunez/jod) — Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers. `★ 3`
- [haseeb-heaven/jev-system-one](https://github.com/haseeb-heaven/jev-system-one) — A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports. `★ 2`
- [reachjalil/jev-tree](https://github.com/reachjalil/jev-tree) — Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap. `★ 2`
- [joelhooks/pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction) — Pi extension: verbatim context compaction with TypeSafe Jev decisions. `★ 3`
- [jcpsimmons/jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop) — Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter… `★ 0`
- [burnigtm/jev-mcp](https://github.com/burnigtm/jev-mcp) — MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client. `★ 1`
- [youyo/decio](https://github.com/youyo/decio) — Turn context into typed decisions and pre-declared actions. `★ 1`
- [pauloportella/codex-dots](https://github.com/pauloportella/codex-dots) — Reusable Codex bundles. `★ 0`
- [lukeliu95/ra2-commander](https://github.com/lukeliu95/ra2-commander) — 让 Claude 多 AI Agent 实时指挥网页版红警2（王二火大 / Chrono Divide, gonghui.k0s.cn）对战，赛后复盘学习对手并进化打法。A Claude Code skill for multi-agent RTS command. `★ 0`
- [dejager/Maybe](https://github.com/dejager/Maybe) — Your code can finally say: I'm not sure. `★ 0`
- [AshutoshVJTI/progressgate](https://github.com/AshutoshVJTI/progressgate) — Detect semantic stagnation in AI agent loops. `★ 0`
- [iefnaf/pi-jev](https://github.com/iefnaf/pi-jev) — Pi extension suite powered by Jev: selective context compaction and model routing. `★ 0`
- [gmaxxxie/jev-cli](https://github.com/gmaxxxie/jev-cli) — CLI for the Jev decision model via the OpenRouter Decisions API. `★ 1`
- [yannip1234/ask-jev](https://github.com/yannip1234/ask-jev) — Continuous AskJev CLI checks throughout Astra work, plus the standalone AskJev skill. `★ 0`
- [picaye/jev-compaction](https://github.com/picaye/jev-compaction) — Context compaction for Hermes sessions that never summarises: every tool call is scored by TypeSafe's Jev model, stale calls are dropped, everything kept… `★ 0`
- [chapel/hermes-jev-skills](https://github.com/chapel/hermes-jev-skills) — Hermes plugin adding semantic skill search and turn-start suggestions. `★ 0`
- [pZacca/askjev](https://github.com/pZacca/askjev) — Unofficial MCP server for Jev (Typesafe AI). `★ 0`
- [Ayush0054/metis](https://github.com/Ayush0054/metis) — Metis: automatic GitHub issue triage powered by TypeSafe AI Jev. A reusable GitHub Action. `★ 0`
- [wadadanet/faq-jev-router](https://github.com/wadadanet/faq-jev-router) — Cascade FAQ routing with TypeSafe Jev — category → FAQ or not found (GitHub Pages demo). `★ 0`
- [av/naiou](https://github.com/av/naiou) — Yes/no agent. `★ 3`

## Guardrails and Code Review

*Permission gates, risk scoring, review workflows and policy enforcement.*

- [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) — A staged code-review workflow and local dashboard built with TypeSafe Jev. `★ 260`
- [leepokai/jev-guard](https://github.com/leepokai/jev-guard) — Auto mode for every coding agent, built on Jev: risk-scores every tool call with session context (deny / ask / allow), flags prompt injection in results… `★ 4`
- [Nyarlathoteppppp/pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) — Runtime constraints for the pi coding agent: checks every side-effecting tool call against what you said, before it runs. Powered by TypeSafe Jev. `★ 2`
- [nicolasmontone/jev-tool-permissions](https://github.com/nicolasmontone/jev-tool-permissions) — Jev-backed tool approval gate and tool-list pruning for the Vercel AI SDK. `★ 1`
- [doeixd/jev-pref](https://github.com/doeixd/jev-pref) — Turn your AGENTS.md preferences into a fast, Jev-powered AI linter. `★ 2`
- [caiovicentino/jev-align](https://github.com/caiovicentino/jev-align) — Calibrated alignment verifier for LLM responses and agent plans — powered by Jev. `★ 0`
- [Madhumasa84/jrx](https://github.com/Madhumasa84/jrx) — Deterministic execution control for autonomous coding agents. `★ 0`
- [vayungodara/jev-lint](https://github.com/vayungodara/jev-lint) — Lint a Markdown knowledge base (Obsidian vault or LLM wiki) for contradictions, stale claims, unresolved markers and missing pages, using TypeSafe Jev. `★ 0`
- [ntedvs/commentcop](https://github.com/ntedvs/commentcop) — Put your code comments on trial. Powered by Jev. `★ 1`
- [santos-sanz/jev-audio-beeper](https://github.com/santos-sanz/jev-audio-beeper) — Low-latency audio censorship POC using Jev typed decisions and ffmpeg. `★ 0`

## Search, Ranking and Extraction

*Reranking, classification, triage and scoring pipelines.*

- [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) — Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API. `★ 70`
- [reachjalil/jevlogs](https://github.com/reachjalil/jevlogs) — Open-source Jev log triage for OpenTelemetry. Score the signal before expensive LLM analysis. `★ 7`
- [hev/reranker](https://github.com/hev/reranker) — Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0. `★ 1`
- [thrashr888/clue](https://github.com/thrashr888/clue) — Semantic ranking for CLI output, local search, and bounded agent context. Works with gh, bd, Cider, SQLite, and JSON/JSONL. `★ 1`

## Applications

*End-user apps: browsers, calendars, robotics, audio, extensions.*

- [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) — Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz. `★ 58`
- [trungdq88/youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection) — Detect youtube sponsor segment with live audio and transcript powered by Jev. `★ 49`
- [ChetasLua/jevmeter](https://github.com/ChetasLua/jevmeter) — Put a live Jev (TypeSafe) meter on any video: every sentence scored, rendered as a 16:9 edit. `★ 53`
- [AlbionaHoti/refgarden](https://github.com/AlbionaHoti/refgarden) — A spatial reference explorer for creators. Local Jev query choices, metadata highlights and source-linked collections. `★ 6`
- [the-data-sherpa/project_blackout](https://github.com/the-data-sherpa/project_blackout) — Interactive cybersecurity lab for watching Jev assess an unfolding attack. `★ 2`
- [iomiras/sponsor-skipper](https://github.com/iomiras/sponsor-skipper) — Chrome extension that skips creator-inserted sponsor reads using a Jev classifier on timed captions. `★ 6`
- [AIsa-team/worth-replying](https://github.com/AIsa-team/worth-replying) — Worth Replying by AIsa. `★ 3`
- [choxos/jev-reviewer](https://github.com/choxos/jev-reviewer) — Ask a trial report and its supplements for systematic review data by voice, text or a questions file. Jev (TypeSafe System One) points at the lines; every… `★ 1`
- [reycn/smart-switch](https://github.com/reycn/smart-switch) — Reimagined window switcher for macOS using frontier artificial intelligence. Predicted by TypeSafe's Jev model. `★ 2`
- [MithrilMan/your-signal](https://github.com/MithrilMan/your-signal) — Open-source BYOK Chrome extension for personal, reversible X timeline filters. `★ 1`
- [ai-suifeng/comment-jev-chrome](https://github.com/ai-suifeng/comment-jev-chrome) — Typed four-way triage of social-media comments, with hostility scoring for malicious ones. `★ 1`
- [TheOnlyArtz/JevIsraeliElections](https://github.com/TheOnlyArtz/JevIsraeliElections) — ג'ב — יועצת בחירת מפלגה. Hebrew/RTL React app ranking the 14 Knesset-26 lists against your ideology. `★ 1`
- [zsoXi/FeedGate](https://github.com/zsoXi/FeedGate) — Precision-first Chrome feed filter (v2.1.0) using TypeSafe Jev judgments: promotional posts are kept unless independently strong spam or ad evidence… `★ 0`
- [blackopsrepl/jev-team-calendar](https://github.com/blackopsrepl/jev-team-calendar) — Resume-discovered project teams, scheduled by SolverForge. `★ 0`
- [svmanth/jmarket](https://github.com/svmanth/jmarket) — Polymarket tells you what the crowd thinks. This tells you what Jev thinks. `★ 1`
- [Wizhill05/typesafe-image-diffusion](https://github.com/Wizhill05/typesafe-image-diffusion) — Diffusion-style pixel art out of a general classifier (TypeSafe Jev): 256 parallel pixel questions + refinement passes. `★ 0`
- [arielweinberger/jev-autopilot](https://github.com/arielweinberger/jev-autopilot) — This demo uses Jev from TypeSafe AI to autonomously fly a drone in a random city from point A to point B, avoiding obstacles along the way. A trip costs… `★ 3`
- [opaielsheikh/zero-shot-vision-robotics](https://github.com/opaielsheikh/zero-shot-vision-robotics) — Zero-shot vision-driven tabletop robotics simulation with PyBullet and multimodal Vision-Language Models. `★ 0`
- [0xnairb/jevpot](https://github.com/0xnairb/jevpot) — AI-powered jackpot number predictor and intelligence oracle built with TypeSafe System One (Jev). `★ 0`

## Trading and Markets

*Market and financial decision-making.*

- [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) — One AI trade decision every Monad block. Jev on Kuru MON-USDC. `★ 825`
- [aowang-ai/jev-trade](https://github.com/aowang-ai/jev-trade) — Live Jev trader on Hyperliquid. `★ 5`
- [zadescoxp/Jev-Trades](https://github.com/zadescoxp/Jev-Trades) — Trading bot with the all new TypeSafe AI's first system one model named as Jev. `★ 8`
- [0xnairb/research_desk](https://github.com/0xnairb/research_desk) — TypeSafe Jev demonstration for new analyzation — experimenting with Jev for fast analysis of news and tickers. `★ 1`

## Benchmarks and Evaluations

*Measuring Jev against other models on cost, speed and accuracy.*

- [iammrduncan/typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) — This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev. `★ 31`
- [zhuyansen/jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval) — Does a TypeSafe Jev rerank beat embedding search? Graded relevance eval (9,831 pairs, 164 zh/en queries) over the Agent Skills Hub catalog, with the… `★ 3`
- [wondertwins/jev-benchmark](https://github.com/wondertwins/jev-benchmark) — Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs. `★ 2`
- [memovai/openevals](https://github.com/memovai/openevals) — Affordable for parallel online agent evals and observability. Powered by JEV. `★ 1`
- [goodrahstar/jev-column-race](https://github.com/goodrahstar/jev-column-race) — Jev vs Gemini 3.8 Flash: labelling 1,000 app reviews, 4.1× faster and 7× cheaper. `★ 11`
- [abhixhek/jevcal](https://github.com/abhixhek/jevcal) — Stop guessing confidence thresholds: calibrate, threshold, and drift-check typed decision models (TypeSafe Jev) against an LLM teacher. `★ 4`
- [zhuyansen/jev-news-cold-start](https://github.com/zhuyansen/jev-news-cold-start) — Cross-domain check on MIND news: a zero-shot Jev headline prior is worth ~500 labelled articles, adds +0.069 ρ as features, and lifts a Thompson-sampling… `★ 0`
- [onlyoneaman/jev-eval](https://github.com/onlyoneaman/jev-eval) — TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts. `★ 0`
- [zhuyansen/jev-issue-pulse](https://github.com/zhuyansen/jev-issue-pulse) — Can a Jev-labelled GitHub issue stream catch a broken release before the fix? No at daily cadence (null, n=7). Per issue, Jev matches triage labels far… `★ 0`
- [aieo-product/jev-gamebenchmark](https://github.com/aieo-product/jev-gamebenchmark) — Sandbox & benchmark: optimize how you ask Jev (TypeSafe System One) to play falling-block puzzle games, head-to-head against LLMs. `★ 0`
- [gemanor/jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark) — Comparing Jev, Gemini Flash, and Claude Fable on Python code review rules: cost, speed, accuracy, and consistency. Includes results, charts, and… `★ 1`
- [Shogo-nfrealmusic/jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval) — Third-party check of Jev against GPT and Claude on multilingual booking-inquiry routing. `★ 0`
- [zhuyansen/jev-support-pulse](https://github.com/zhuyansen/jev-support-pulse) — Does a Jev-labelled support-tweet stream spike before a brand admits an outage? At equal false alarms it catches 17 vs 10 incidents (volume), ~4h ahead; a… `★ 0`
- [TanayPadar/gpt-vs-jev](https://github.com/TanayPadar/gpt-vs-jev) — Compare GPT generated language with JEV structured Noul decisions on the same input. `★ 1`

## Games and Fun

*Games, toys and deliberately playful projects.*

- [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) — A TypeSafe/Jev agent that plays Super Mario Bros. from structured emulator state. `★ 260`
- [standardagents/jevpilot](https://github.com/standardagents/jevpilot) — A playable Three.js driving simulator with Jev-powered autopilot. `★ 62`
- [phyous/tsai-sc](https://github.com/phyous/tsai-sc) — TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities. `★ 15`
- [mizuamedesu/SuperTuxKart-Jev](https://github.com/mizuamedesu/SuperTuxKart-Jev) — SuperTuxKart fork with a local controller that lets Jev drive the kart. `★ 0`
- [kspviswa/chakravyuha-jev](https://github.com/kspviswa/chakravyuha-jev) — Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it… `★ 0`
- [mkotlikov/jev-grug](https://github.com/mkotlikov/jev-grug) — Helping JEV speak <3. `★ 3`
- [kentaro/jev-shogi](https://github.com/kentaro/jev-shogi) — 判定特化モデル Jev に将棋を指させる実験（ロリポップ！AIゲートウェイ経由）. `★ 0`
- [willprout/magic-8-ball](https://github.com/willprout/magic-8-ball) — A beautifully minimal Magic 8 Ball powered by Jev from TypeSafe. Twenty classic answers, one fast AI judgment. `★ 1`
- [0xtrou/rubikjev](https://github.com/0xtrou/rubikjev) — Challenge the Jev's intelligence in Rubik Cube puzzles. `★ 1`
- [stbenjam/jev-eight-ball](https://github.com/stbenjam/jev-eight-ball) — A liquid magic eight ball powered by TypeSafe Jev decisions through OpenRouter. `★ 0`
- [robipop22/Jev-is-odd](https://github.com/robipop22/Jev-is-odd) — Ask Jev by TypeSafe AI whether a number is odd. TypeScript, real token usage, and latency benchmarks. `★ 0`
- [wobsoriano/is-jeven](https://github.com/wobsoriano/is-jeven) — Is it even? Ask Jev. `★ 0`
- [TurboGuo/jev-dating](https://github.com/TurboGuo/jev-dating) — Jev vs chat models on dating: a red-flag detector and a live "is she/he interested?" meter, both judged against the same standard. Live at jevdating.pages.dev. `★ 0`

## Framework Integrations

*Jev as a provider or backend inside another framework.*

- [giuliosmall/pg_typesafe](https://github.com/giuliosmall/pg_typesafe) — Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification. `★ 76`
- [jomatsu/zod-jev](https://github.com/jomatsu/zod-jev) — Compose Jev semantic checks into Zod 4 schemas; shape rules stay in Zod. `★ 7`
- [yusukebe/hono-jev-router](https://github.com/yusukebe/hono-jev-router) — Route HTTP requests by meaning. A semantic router for Hono powered by Jev. `★ 24`
- [DomMonte/n8n-nodes-typesafe-ai](https://github.com/DomMonte/n8n-nodes-typesafe-ai) — n8n community node for the TypeSafe AI System One API — typed yes/no, choice and score questions with calibrated probabilities. `★ 0`

## Other Lists

*Sibling directories of the same ecosystem.*

- [AbdelStark/awesome-typesafe](https://github.com/AbdelStark/awesome-typesafe) — A curated list of official resources and community projects for TypeSafe, System One models, and Jev. `★ 220`
- [yibie/awesome-jev](https://github.com/yibie/awesome-jev) — A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions. `★ 137`
- [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) — Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync. `★ 26`
- [valentynkit/awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe) — Typed decisions with TypeSafe's Jev, the first System One model. `★ 6`
- [daftAI2026/awesome-jev](https://github.com/daftAI2026/awesome-jev) — TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai). `★ 2`

## Upstream Integrations

*Jev landing inside established projects. Star counts belong to the host project, so these are listed separately rather than ranked.*

- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — Jev added to the model-provider list, plus skill routing. `#113847, #114376 open` `★ 246.9k`
- [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) — Jev skill routing and skill suggestion for the coding agent. `#12364, #12373 open` `★ 31.8k`
- [trycua/cua](https://github.com/trycua/cua) — Jev-use agent recipe and example for the cua driver. `#3916 merged` `★ 23.1k`
- [BoundaryML/baml](https://github.com/BoundaryML/baml) — TypeSafe System One provider. `#4906 open` `★ 9.2k`
- [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway) — LLM guardrail example built on Jev. `#3529 merged` `★ 4.9k`
- [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) — Jev scripts for desktop computer use. `scripts/jev` `★ 1.3k`
- [laravel/ai](https://github.com/laravel/ai) — TypeSafe AI classification in the Laravel AI SDK. `#1010 merged` `★ 1.2k`
- [CelestoAI/celesto](https://github.com/CelestoAI/celesto) — PR review example. `examples/pr-review-jev` `★ 943`
- [uezo/aiavatarkit](https://github.com/uezo/aiavatarkit) — Jev turn-end gate with configurable hold ranges. `#428 merged` `★ 674`
- [baggiiiie/pi-stuff](https://github.com/baggiiiie/pi-stuff) — Jev-backed approval package for Pi. `packages/approve-for-me` `★ 38`
- [rcarmo/go-pherence](https://github.com/rcarmo/go-pherence) — Jev-like model in a pure-Go tensor framework. `model/jevlike` `★ 10`
- [ByteSliceHQ/looms](https://github.com/ByteSliceHQ/looms) — Jev as a first-class run kind. `#5 open` `★ 9`
- [iamlemec/llama.cpp](https://github.com/iamlemec/llama.cpp) — Classification tool in a llama.cpp fork. `classify branch, tools/classify` `★ 4`
- [jamesward/hello-zio-bedrock](https://github.com/jamesward/hello-zio-bedrock) — Typed tool selection in a ZIO + Bedrock sample. `better-tools branch` `★ 2`
- [pcc-labs/tetris](https://github.com/pcc-labs/tetris) — Jev decision labels in the viewer and a jev-latest benchmark arm. `#21 open` `★ 1`
- [jamescorbett/mlx-vlm](https://github.com/jamescorbett/mlx-vlm) — System One decoding for vision language models on MLX. `mlx_vlm/systemone` `★ 1`
- [TrainLCD/Functions](https://github.com/TrainLCD/Functions) — Feedback triage and station reranking via TypeSafe. `#33, #35 merged` `★ 0`
- [kiarina/labs](https://github.com/kiarina/labs) — Safety-judgment experiment. `2026/09/17/typesafe-jev-safety-judgment` `★ 0`

## Method

Every candidate was checked before being listed, because a name containing "jev" or "typesafe" proves nothing — "type-safe" is an ordinary programming term.

1. **Static evidence.** Each repository was scanned for `api.typesafe.ai`, `TYPESAFE_API_KEY`, `typesafe-sdk`, `@typesafe-ai/sdk`, `jev-latest`, `/v1/systemone` and `noul`, across the README, the file tree and dependency manifests.
2. **Semantic judgment.** Jev itself was asked two questions per repository: whether the text refers to TypeSafe's model rather than generic type safety, and what the project's relationship to Jev is (calls the hosted API, open alternative, tooling, benchmark, curated list, or unrelated).
3. **Combination in code.** Static evidence is authoritative; the model judgment resolves the ambiguous cases. A project is listed when either is affirmative and neither contradicts the other. Upstream pull requests and subdirectories were opened and confirmed individually.

Ranking keeps the raw signals separate and combines them with weights in code: `score = 50 × log-scaled stars + 50 × (interest ÷ 4)`. Interest is a Score question answered over the repository description and README; stars come from the GitHub API. Change the weights and the ranking changes without re-running any inference.


## Contributing

Pull requests welcome. Please keep entries one line, describe what the project does rather than how good it is, and include evidence that the project actually calls Jev or implements a Jev-style typed decision model.

## License

[CC0-1.0](LICENSE). Star counts and judgments were collected on 2026-09-18 and will drift.
