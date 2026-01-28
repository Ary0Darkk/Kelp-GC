<!-- Animated Header -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:22c55e,50:10b981,100:06b6d4&height=200&section=header&text=🌿%20KELP&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Automated%20Deal%20Flow%20Pipeline&descSize=25&descAlignY=55&descAlign=50" width="100%"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=22C55E&center=true&vCenter=true&multiline=true&repeat=true&width=800&height=100&lines=Transform+Company+Data+into+Investor+Teasers;AI-Powered+%7C+GPU+Accelerated+%7C+100%25+Offline;Built+for+IIT+Bombay+Hackathon+2026+%F0%9F%8F%86" alt="Typing SVG" />
</p>

<!-- Animated Badges -->
<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/🚀_Quick_Start-22c55e?style=for-the-badge" alt="Quick Start"/></a>
  <a href="#-architecture"><img src="https://img.shields.io/badge/🏗️_Architecture-3b82f6?style=for-the-badge" alt="Architecture"/></a>
  <a href="#-features"><img src="https://img.shields.io/badge/✨_Features-8b5cf6?style=for-the-badge" alt="Features"/></a>
  <a href="#-tech-stack"><img src="https://img.shields.io/badge/🛠️_Tech_Stack-f59e0b?style=for-the-badge" alt="Tech Stack"/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776ab?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Ollama-Local_LLM-7c3aed?style=flat-square&logo=ollama&logoColor=white" alt="Ollama"/>
  <img src="https://img.shields.io/badge/PyTorch-GPU_Accelerated-ee4c2c?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/License-MIT-22c55e?style=flat-square" alt="License"/>
  <img src="https://img.shields.io/github/stars/shubro18202758/KELP?style=flat-square&color=yellow" alt="Stars"/>
  <img src="https://img.shields.io/github/last-commit/shubro18202758/KELP?style=flat-square&color=blue" alt="Last Commit"/>
</p>

---

## 🎬 Demo

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">
</p>

<table align="center">
<tr>
<td align="center" width="50%">

### 📥 Input
```
📄 Company Markdown Files
├── Financial Reports
├── Business Description  
└── Product Information
```

</td>
<td align="center" width="50%">

### 📤 Output
```
📊 Investment Teaser PPT
├── Cover Slide
├── Business Overview
├── Financial Charts
└── Investment Highlights
```

</td>
</tr>
</table>

---

## 🎯 What is KELP?

<img align="right" src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="200">

**KELP** (Knowledge-Enhanced Lean Presentations) is an AI-powered pipeline that automatically generates professional **Investment Teaser PowerPoint presentations** from raw company data.

### ✨ Key Capabilities

| Feature | Description |
|:-------:|-------------|
| 📊 | **Dynamic Charts** - Donut, Area, Column, Gauge |
| 🔍 | **Web Research** - Real-time market intelligence |
| 🖼️ | **Smart Images** - Sector-specific auto-fetch |
| 🤖 | **Local LLM** - 100% offline, privacy-first |
| 📈 | **Market Data** - TAM, CAGR, Industry trends |

---

## 🏗️ Architecture

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">
</p>

```mermaid
flowchart LR
    subgraph INPUT["📄 INPUT"]
        A[Company Data<br/>Markdown/PDF]
    end
    
    subgraph PROCESS["🔄 AI PROCESSING"]
        B[🔍 Data Ingestion]
        C[🏷️ Sector Classification]
        D[💰 Financial Extraction]
        E[🌐 Web Research]
        F[🤖 LLM Generation]
        G[🖼️ Image Fetching]
    end
    
    subgraph OUTPUT["📊 OUTPUT"]
        H[Investment Teaser<br/>PPTX]
    end
    
    A --> B --> C --> D --> E --> F --> G --> H
    
    style INPUT fill:#1e3a5f,stroke:#3b82f6,color:#fff
    style PROCESS fill:#1e2d3d,stroke:#22c55e,color:#fff
    style OUTPUT fill:#1e3a2f,stroke:#22c55e,color:#fff
```

### 🔄 Pipeline Flow

```mermaid
graph TB
    subgraph Layer1["Layer 1: Data Ingestion"]
        A1[📄 Markdown Parser]
        A2[📊 Financial Extractor]
        A3[🏢 Entity Recognition]
    end
    
    subgraph Layer2["Layer 2: Intelligence"]
        B1[🏷️ Sector Classifier]
        B2[🌐 Web Research Engine]
        B3[📈 Market Intelligence]
    end
    
    subgraph Layer3["Layer 3: Content"]
        C1[🤖 LLM Generator]
        C2[📝 Narrative Writer]
        C3[🎯 Highlight Extractor]
    end
    
    subgraph Layer4["Layer 4: Presentation"]
        D1[📊 Chart Generator]
        D2[🖼️ Image Sourcer]
        D3[🎨 PPTX Assembler]
    end
    
    Layer1 --> Layer2 --> Layer3 --> Layer4
    
    style Layer1 fill:#3b82f6,stroke:#60a5fa,color:#fff
    style Layer2 fill:#8b5cf6,stroke:#a78bfa,color:#fff
    style Layer3 fill:#f59e0b,stroke:#fbbf24,color:#fff
    style Layer4 fill:#22c55e,stroke:#4ade80,color:#fff
```

---

## 📁 Project Structure

<img align="right" src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="150">

```
🌿 KELP/
│
├── 📂 src/
│   ├── 📂 data_ingestion/        # Parse & extract
│   ├── 📂 sector_intelligence/   # ML classification
│   ├── 📂 content_generation/    # LLM narratives
│   ├── 📂 image_intelligence/    # Image sourcing
│   ├── 📂 presentation/          # PPTX generation
│   ├── 📂 citation/              # Source attribution
│   ├── 📂 web_scraping/          # Web data
│   └── 📂 vision/                # Visual AI
│
├── 📂 Company Data/              # 6 sample companies
├── 📂 config/                    # Settings
├── 📂 docs/                      # Documentation
│
├── 🐍 pipeline_v5_enhanced.py    # Main entry
├── 📋 requirements.txt           # Dependencies
└── 📖 README.md                  # You are here!
```

---

## ✨ Features

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="100">
</p>

### 🤖 AI-Powered Content Generation

<table>
<tr>
<td width="60%">

```python
# What KELP does with your data:

1. 🔍 Parse company markdown files
2. 🏷️ Classify into 6 industry sectors
3. 💰 Extract financial metrics (Revenue, EBITDA)
4. 🌐 Research market size & CAGR online
5. 🤖 Generate investor narratives via LLM
6. 📊 Create dynamic charts automatically
7. 🖼️ Fetch sector-relevant images
8. 📑 Assemble professional PPTX
```

</td>
<td width="40%" align="center">

<img src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="200">

</td>
</tr>
</table>

### 🌐 Gemini-Style Web Research

```mermaid
sequenceDiagram
    participant K as KELP
    participant D as DuckDuckGo
    participant W as Webpages
    participant L as Local LLM
    
    K->>D: 🔍 Search "Manufacturing India market size"
    D-->>K: 📄 Return 20+ URLs
    K->>W: 📖 Fetch & Read 5-8 pages
    W-->>K: 📊 Raw content
    K->>L: 🤖 Synthesize insights
    L-->>K: ✅ Market: $768B, CAGR: 8.0%
```

### 📊 Chart Types Generated

<table>
<tr>
<td align="center">🍩<br/><b>Donut</b><br/><sub>Revenue Split</sub></td>
<td align="center">📈<br/><b>Area</b><br/><sub>EBITDA Trend</sub></td>
<td align="center">📊<br/><b>Column</b><br/><sub>YoY Growth</sub></td>
<td align="center">📉<br/><b>Combo</b><br/><sub>Revenue+Margin</sub></td>
</tr>
<tr>
<td align="center">🎯<br/><b>Gauge</b><br/><sub>KPI Metrics</sub></td>
<td align="center">📶<br/><b>Stacked</b><br/><sub>Segments</sub></td>
<td align="center">📈<br/><b>Line</b><br/><sub>Trajectory</sub></td>
<td align="center">🥧<br/><b>Pie</b><br/><sub>Market Share</sub></td>
</tr>
</table>

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100">
</p>

<table align="center">
<tr>
<td align="center" width="96">
<img src="https://techstack-generator.vercel.app/python-icon.svg" alt="Python" width="65" height="65" />
<br>Python
</td>
<td align="center" width="96">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pytorch/pytorch-original.svg" width="65" height="65" />
<br>PyTorch
</td>
<td align="center" width="96">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" width="65" height="65" />
<br>Pandas
</td>
<td align="center" width="96">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" width="65" height="65" />
<br>NumPy
</td>
<td align="center" width="96">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/matplotlib/matplotlib-original.svg" width="65" height="65" />
<br>Matplotlib
</td>
</tr>
</table>

### 🧠 AI & ML Stack

| Component | Technology | Purpose |
|:---------:|:----------:|---------|
| 🤖 | **Ollama + qwen2.5:7b** | Local LLM inference |
| 🔥 | **PyTorch 2.1+** | GPU acceleration |
| 🤗 | **Transformers** | Model loading |
| 🌐 | **ddgs** | Web search |
| 🍲 | **BeautifulSoup** | HTML parsing |

### 📊 Presentation Stack

| Component | Technology | Purpose |
|:---------:|:----------:|---------|
| 📑 | **python-pptx** | PPTX generation |
| 📈 | **Matplotlib** | Chart rendering |
| 🖼️ | **Pillow** | Image processing |
| 📄 | **pdfplumber** | PDF extraction |

### ⚙️ LLM Configuration

```python
GENERATION_CONFIG = {
    "model": "qwen2.5:7b",
    "temperature": 0.4,      # 🎯 Factual precision
    "top_p": 0.85,           # 📊 Balanced diversity  
    "repeat_penalty": 1.15,  # 🔄 Reduce repetition
    "num_ctx": 4096,         # 📖 Large context
}
```

---

## 🚀 Quick Start

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d899-44b4-b1d9-4c9c4c41f31f.gif" width="400">
</p>

### 📋 Prerequisites

```bash
✅ Python 3.10+
✅ NVIDIA GPU (recommended) or CPU
✅ Ollama installed
```

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/shubro18202758/KELP.git
cd KELP

# Create virtual environment
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Install LLM model
ollama pull qwen2.5:7b
```

### ▶️ Running KELP

```bash
# Process ALL companies
python pipeline_v5_enhanced.py

# Process SINGLE company
python pipeline_v5_enhanced.py --company kalyani

# Quiet mode
python pipeline_v5_enhanced.py --quiet
```

### 📺 Expected Output

```
======================================================================
🌿 KELP PIPELINE V5 - ENHANCED DATA-DENSE LAYOUTS
======================================================================

📦 Processing: FORGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ Loaded 42,404 characters
  ✓ Sector: Manufacturing & Industrials (72%)
  ✓ Revenue: ₹2366Cr, EBITDA: 10.1%
  🔍 Found 22 sources, read 6 pages
  ✓ Market: $768.28B, CAGR: 8.0%
  ✓ Generated investment narratives
  ✓ Fetched 7 sector images
  📊 Created 5 slides with charts

✅ SUCCESS: Project Velocity
   📊 PPT: Project_Velocity_Manufacturing.pptx
   ⏱ Time: 54.0s
```

---

## 📊 Sample Results

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="400">
</p>

### 🏆 Companies Processed

| Company | Sector | Revenue | EBITDA | Market | CAGR |
|:--------|:-------|--------:|-------:|-------:|-----:|
| 🏭 Kalyani Forge | Manufacturing | ₹2,366 Cr | 10.1% | $768B | 8.0% |
| 🔌 Centum | Electronics | ₹11,554 Cr | 8.4% | $175B | 5.8% |
| 🎬 Connplex | Entertainment | ₹960 Cr | 27.3% | - | 9.8% |
| 🚚 Gati | Logistics | ₹15,100 Cr | 4.3% | $1.2B | 8.5% |
| 💊 Ind Swift | Pharma | ₹5,022 Cr | 9.7% | $129B | 8.1% |
| 💻 Ksolves | Technology | - | - | $166B | 13% |

### ⚡ Performance Metrics

```
┌─────────────────────────────────────────────────────────────┐
│                    PERFORMANCE DASHBOARD                     │
├─────────────────────────────────────────────────────────────┤
│  ⏱️  Processing Time     │  ~55 seconds per company         │
│  📄  Sources Found       │  20-25 per sector                │
│  📖  Pages Read          │  5-8 per company                 │
│  📊  Charts Generated    │  4-6 per presentation            │
│  🖼️  Images Fetched      │  7 per presentation              │
│  💾  VRAM Usage          │  ~4.4 GB (qwen2.5:7b)            │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎨 Slide Preview

```
┌────────────────────────────────────────────────────────┐
│  SLIDE 1: COVER                                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │     🏭                                           │  │
│  │     PROJECT VELOCITY                             │  │
│  │     Manufacturing & Industrials                  │  │
│  │     ━━━━━━━━━━━━━━━━━━━━━━                      │  │
│  │     Confidential Investment Teaser               │  │
│  └──────────────────────────────────────────────────┘  │
├────────────────────────────────────────────────────────┤
│  SLIDE 2: BUSINESS OVERVIEW (4-Quadrant)              │
│  ┌────────────────┬─────────────────────────────────┐  │
│  │  Description   │   Key Products                  │  │
│  ├────────────────┼─────────────────────────────────┤  │
│  │  Clients       │   Market Position               │  │
│  └────────────────┴─────────────────────────────────┘  │
├────────────────────────────────────────────────────────┤
│  SLIDE 3: FINANCIAL DEEP-DIVE                         │
│  ┌──────────┬──────────┬────────────────────────────┐  │
│  │  🍩      │  📈      │  Key Metrics               │  │
│  │  Revenue │  EBITDA  │  • Revenue: ₹2,366 Cr      │  │
│  │  Split   │  Trend   │  • EBITDA: 10.1%           │  │
│  └──────────┴──────────┴────────────────────────────┘  │
├────────────────────────────────────────────────────────┤
│  SLIDE 4: INVESTMENT HIGHLIGHTS                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │  ✅ Strong market position                       │  │
│  │  ✅ Diversified client base                      │  │
│  │  ✅ Consistent revenue growth                    │  │
│  │  ✅ Expansion opportunities                      │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

---

## 💻 Hardware Tested

<table align="center">
<tr>
<td align="center">🎮<br/><b>GPU</b><br/>RTX 4070<br/><sub>8GB VRAM</sub></td>
<td align="center">🖥️<br/><b>CPU</b><br/>i9-14900HX<br/><sub>24 Cores</sub></td>
<td align="center">💾<br/><b>RAM</b><br/>32GB<br/><sub>DDR5</sub></td>
<td align="center">💿<br/><b>Storage</b><br/>NVMe<br/><sub>SSD</sub></td>
</tr>
</table>

---

## 🔮 Roadmap

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284094-e50ceae2-de86-4dd6-9c31-f47d6e9f8e47.gif" width="400">
</p>

- [ ] 🌍 Multi-language support
- [ ] 📱 Streamlit web interface  
- [ ] 🔗 REST API endpoint
- [ ] 📊 More chart types (Waterfall, Sankey)
- [ ] 🤖 Fine-tuned domain LLM
- [ ] 📈 Real-time stock integration

---

## 🤝 Contributing

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284145-bf2c01a8-c7e1-4e82-8f66-dfd6e8a6f95e.gif" width="400">
</p>

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Fork → Clone → Branch → Commit → Push → PR
git checkout -b feature/amazing-feature
git commit -m "Add amazing feature"
git push origin feature/amazing-feature
```

---

## 📜 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

<table align="center">
<tr>
<td align="center">🏆<br/><b>IIT Bombay</b><br/><sub>Hackathon 2026</sub></td>
<td align="center">🦙<br/><b>Ollama</b><br/><sub>Local LLM</sub></td>
<td align="center">📊<br/><b>python-pptx</b><br/><sub>PPTX Gen</sub></td>
<td align="center">🦆<br/><b>DuckDuckGo</b><br/><sub>Web Search</sub></td>
</tr>
</table>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:22c55e,50:10b981,100:06b6d4&height=120&section=footer&animation=fadeIn" width="100%"/>
</p>

<p align="center">
  <b>Built with 💚 by Team KELP for IIT Bombay Hackathon 2026</b>
</p>

<p align="center">
  <a href="https://github.com/shubro18202758/KELP/stargazers">⭐ Star this repo</a> •
  <a href="https://github.com/shubro18202758/KELP/issues">🐛 Report Bug</a> •
  <a href="https://github.com/shubro18202758/KELP/issues">💡 Request Feature</a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=shubro18202758&repo=KELP&label=Profile%20Views&color=22c55e&style=flat-square" alt="Profile Views"/>
</p>
