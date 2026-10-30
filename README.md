<p align="center"><img src="/assets/header.svg" alt="Rishi (Shivaanjan) Bhattacharjee, Graduate Data and AI Engineer in London" width="100%"></p>

**Graduate Data & AI Engineer in London.** MSc Financial Technology, Warwick Business School (Distinction).

I build data pipelines that are tested and monitored, and LLM systems that are checked before anyone trusts them, mostly on finance data. Open to graduate data and AI engineering roles in the UK.

<p>
  <a href="https://dutylens.vercel.app"><img src="https://img.shields.io/badge/Try_it-DutyLens_live_demo-0F766E?style=for-the-badge&logo=vercel&logoColor=white" alt="Try the DutyLens live demo"></a>
  <a href="https://shivaanjan.co.uk"><img src="https://img.shields.io/badge/Explore-My_portfolio-1B3A5C?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Explore my portfolio"></a>
</p>

<sub><b>DutyLens</b> asks whether an LLM can spot vulnerable customers in complaints better than a cheap model, and at what cost. Label 3 real complaints in about 2 minutes; your answers stay in your browser.</sub>

### Featured work

| Project | What it does | Result |
|---|---|---|
| [**DashTalk**](https://github.com/ShivaanjanB/dashtalk) | Ask dashboards questions in plain English. A YAML semantic layer defines every metric once, and an MCP server enforces row-level permissions. | **0 permission leaks and 0 wrong figures** across two eval runs; caught 2 SEC data faults by checking answers against filings |
| [**FantasyCoach AI**](https://github.com/ShivaanjanB/Fantasy_AI) | Hybrid RAG over live football APIs: BM25 + dense retrieval, reranking and a verifier for every numeric claim. | Factual accuracy **62% → 89%**, hallucinations **38% → 11%** on a 30-query adversarial benchmark |
| [**LLM disclosure sentiment**](https://github.com/ShivaanjanB/dissertation-pilot) | MSc dissertation: GPT-4o vs FinBERT on 7,733 UK company disclosures from 186 firms. | An honest null: the main effect is not significant (p = 0.57), and the one reversal found does not survive trading costs |

<details>
<summary><b>How DashTalk works</b></summary>

```mermaid
flowchart LR
    Q[Question in plain English] --> A[Local LLM agent<br/>qwen3.5:9b via Ollama]
    A -->|MCP over stdio| S[DashTalk MCP server<br/>started for one user]
    S --> L[YAML semantic layer<br/>synonyms, units, row-level scope]
    L --> D[(DuckDB<br/>SEC XBRL · World Bank · sales)]
    D --> R[Rows, display value, caveats]
    R --> A
    S --> G[(Audit log)]
    A --> O[ANSWER / CLARIFY / REFUSED]
```

Permissions are enforced in the server, not the prompt, so a model that is talked into asking still cannot fetch a hidden figure.

</details>

<details>
<summary><b>How FantasyCoach AI works</b></summary>

```mermaid
flowchart LR
    S1[Sportmonks API] --> M[Fuzzy ID matching<br/>677 of 680 players]
    S2[FPL API] --> M
    M --> C[(852 semantic chunks<br/>in ChromaDB)]
    Q[Question] --> RT[Query router<br/>8 query types]
    RT --> H[Hybrid retrieval<br/>BM25 + dense, RRF]
    C --> H
    H --> RR[Cross-encoder rerank]
    RR --> LLM[Claude drafts the answer]
    LLM --> V{Every number<br/>found in the sources?}
    V -->|yes| UI[Streamed to the React app]
    V -->|no| LLM
```

</details>

<details>
<summary><b>How the dissertation test works</b></summary>

```mermaid
flowchart LR
    D[7,733 RNS disclosures<br/>186 UK firms, 2021–2025] --> G[GPT-4o sentiment]
    D --> F[FinBERT sentiment]
    G --> DV[Divergence:<br/>LLM minus baseline]
    F --> DV
    G --> CM[Common sentiment<br/>component]
    F --> CM
    DV --> P1[Within-firm panel regressions<br/>on abnormal returns]
    P1 --> R1[Divergence effect: null<br/>p = 0.57]
    CM --> P2[Within-firm panel regressions]
    P2 --> R2[−48.8 bps reversal]
    R2 --> BL[Portfolios net of<br/>trading costs]
    BL --> R3[Not tradable after costs]
```

</details>

### At a glance

<p>
  <img src="/metrics.languages.svg" alt="Most-used languages" width="49%" align="top">
  <img src="/metrics.lines.svg" alt="Lines of code by project" width="49%" align="top">
</p>

<sub>Infographics refreshed daily with <a href="https://github.com/lowlighter/metrics">lowlighter/metrics</a>.</sub>

### Toolkit

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![dbt](https://img.shields.io/badge/dbt-FF694B?style=flat-square) ![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![Claude API](https://img.shields.io/badge/Claude_API-D97757?style=flat-square&logo=anthropic&logoColor=white) ![MCP](https://img.shields.io/badge/MCP-111111?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-5A3E9B?style=flat-square)

### Elsewhere

[Portfolio](https://shivaanjan.co.uk) · [LinkedIn](https://www.linkedin.com/in/shivaanjan-bhattacharjee) · rishhbhatt06@gmail.com
