<p align="center">
  <img src="docs/images/kelp_banner.svg" alt="KELP Banner" width="100%"/>
</p>

<h1 align="center">🌿 KELP - Automated Deal Flow Pipeline</h1>

<p align="center">
  <strong>Transform Company Data into Investor-Ready Teasers in Seconds</strong>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-features">Features</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-sample-outputs">Samples</a> •
  <a href="#-contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Ollama-Local_LLM-purple?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama"/>
  <img src="https://img.shields.io/badge/PyTorch-GPU_Accelerated-orange?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"/>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/shubro18202758/KELP?style=social" alt="Stars"/>
  <img src="https://img.shields.io/github/forks/shubro18202758/KELP?style=social" alt="Forks"/>
  <img src="https://img.shields.io/github/issues/shubro18202758/KELP?style=flat-square" alt="Issues"/>
</p>

---

## 🎯 What is KELP?

**KELP** (Knowledge-Enhanced Lean Presentations) is an AI-powered pipeline that automatically generates professional **Investment Teaser PowerPoint presentations** from raw company data. Built for the **IIT Bombay Hackathon 2026**, KELP transforms markdown documents into stunning, investor-grade presentations with:

- 📊 **Dynamic Financial Charts** (Donut, Area, Column, Gauge charts)
- 🔍 **Real-time Web Research** with source citations
- 🖼️ **Sector-specific Images** auto-fetched from the web
- 🤖 **Local LLM Processing** (100% offline, privacy-first)
- 📈 **Market Intelligence** with TAM, CAGR, and industry trends

<p align="center">
  <img src="docs/images/kelp_workflow.png" alt="KELP Workflow" width="90%"/>
</p>

---

## 🏗️ Architecture

KELP follows a **modular, microservices-inspired architecture** where each component handles a specific task in the teaser generation pipeline:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           KELP ARCHITECTURE                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                   │
│  │   📄 INPUT    │    │  🔄 PROCESS  │    │   📊 OUTPUT  │                   │
│  │  (Markdown)  │───▶│   (AI/ML)    │───▶│    (PPTX)    │                   │
│  └──────────────┘    └──────────────┘    └──────────────┘                   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                        PROCESSING LAYERS                             │    │
│  ├─────────────────────────────────────────────────────────────────────┤    │
│  │                                                                      │    │
│  │  Layer 1: DATA INGESTION          Layer 2: SECTOR INTELLIGENCE      │    │
│  │  ├─ Markdown Parser               ├─ Industry Classifier            │    │
│  │  ├─ Financial Extractor           ├─ Sub-sector Detection           │    │
│  │  └─ Entity Recognition            └─ Confidence Scoring             │    │
│  │                                                                      │    │
│  │  Layer 3: CONTENT GENERATION      Layer 4: WEB RESEARCH             │    │
│  │  ├─ LLM Investment Writer         ├─ DuckDuckGo Search              │    │
│  │  ├─ Narrative Generator           ├─ Webpage Content Fetch          │    │
│  │  └─ Highlight Extractor           └─ LLM Synthesis & Citation       │    │
│  │                                                                      │    │
│  │  Layer 5: IMAGE INTELLIGENCE      Layer 6: PRESENTATION             │    │
│  │  ├─ Sector Image Fetcher          ├─ 4-Quadrant Layouts             │    │
│  │  ├─ Web Scraping Engine           ├─ Multi-Chart Generation         │    │
│  │  └─ Image Cache Manager           └─ Professional PPTX Export       │    │
│  │                                                                      │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 📁 Project Structure

```
KELP/
│
├── 📂 src/                          # Core source modules
│   ├── 📂 data_ingestion/           # Markdown parsing & data extraction
│   │   └── markdown_parser.py       # Parse company markdown files
│   │
│   ├── 📂 sector_intelligence/      # Industry classification
│   │   └── classifier.py            # ML-based sector detection
│   │
│   ├── 📂 content_generation/       # AI content creation
│   │   ├── advanced_research_engine.py    # 🌐 Gemini-style web research
│   │   ├── investment_content_generator.py # 📝 LLM narrative generation
│   │   ├── data_enrichment_engine.py      # 📊 Financial data extraction
│   │   ├── llm_generator.py               # 🤖 Ollama LLM interface
│   │   └── web_research_engine.py         # 🔍 Market intelligence
│   │
│   ├── 📂 image_intelligence/       # Image sourcing
│   │   ├── free_image_fetcher.py    # 🖼️ DuckDuckGo image scraper
│   │   └── image_sourcer.py         # Multi-source image manager
│   │
│   ├── 📂 presentation/             # PPTX generation
│   │   ├── enhanced_kelp_generator.py     # 🎨 Main PPT generator
│   │   ├── kelp_professional_generator.py # Professional layouts
│   │   └── rich_ppt_generator.py          # Rich text handling
│   │
│   ├── 📂 citation/                 # Source attribution
│   │   └── citation_generator.py    # 📚 Auto-generate citations
│   │
│   ├── 📂 web_scraping/             # Web data collection
│   │   ├── scraper.py               # Async web scraper
│   │   └── web_search.py            # Search engine integration
│   │
│   └── 📂 vision/                   # Visual AI (experimental)
│       ├── janus_engine.py          # DeepSeek Janus integration
│       └── vl_engine.py             # Vision-language models
│
├── 📂 config/                       # Configuration
│   └── settings.py                  # Global settings & paths
│
├── 📂 Company Data/                 # Input data (6 sample companies)
│   ├── automotive-kalyani-forge/    # 🏭 Manufacturing sector
│   ├── electronics-centum/          # 🔌 Electronics & Defense
│   ├── entertainment-connplex/      # 🎬 Entertainment & Media
│   ├── logistics-gati/              # 🚚 Logistics & Supply Chain
│   ├── pharma-ind-swift/            # 💊 Pharmaceuticals
│   └── technology-ksolves/          # 💻 Technology & IT Services
│
├── 📂 docs/                         # Documentation & assets
│   └── images/                      # README images & diagrams
│
├── 🐍 pipeline_v5_enhanced.py       # Main entry point
├── 📋 requirements.txt              # Python dependencies
├── 📖 README.md                     # This file
├── 📜 LICENSE                       # MIT License
└── 🤝 CONTRIBUTING.md               # Contribution guidelines
```

---

## ✨ Features

### 🤖 AI-Powered Content Generation

KELP uses **local LLMs** (via Ollama) to generate investor-grade narratives. No API keys, no cloud costs, complete privacy.

| Feature | Description |
|---------|-------------|
| 📝 **Investment Narratives** | Professional business overviews, growth stories, expansion plans |
| 🎯 **Highlight Extraction** | Auto-identify key investment highlights from raw data |
| 📊 **Financial Analysis** | Extract revenue, EBITDA, margins from unstructured text |
| 🏷️ **Sector Classification** | 100% accurate industry detection with sub-sector granularity |

### 🌐 Gemini-Style Web Research

Our **Advanced Research Engine** reads actual webpages (not just snippets) and synthesizes market intelligence:

```python
# What KELP does behind the scenes:
1. 🔍 Generate smart search queries for the sector
2. 📄 Fetch 20+ sources from DuckDuckGo
3. 📖 Actually READ 5-8 full webpages
4. 📊 Extract statistics, market sizes, CAGRs
5. 🤖 LLM synthesizes insights with citations
6. 📈 Add TAM/SAM badges to your slides
```

**Sample Research Output:**
```
📊 Research Results:
  Market Size: $1.74 Trillion (2026) per Mordor Intelligence
  CAGR: 7.26% (2026-2031) per Mordor Intelligence
  Key Trends: 3 trends found
    - Growing adoption of Industry 4.0 and smart manufacturing
    - Rapid growth in electronics sector with 15.3% CAGR
    - Asia Pacific leading with 42.7% market share
  Sources: 5 sources cited
```

### 📊 Dynamic Chart Generation

KELP generates **8 different chart types** automatically:

| Chart Type | Use Case |
|------------|----------|
| 🍩 **Donut Chart** | Revenue breakdown |
| 📈 **Area Chart** | EBITDA trends |
| 📊 **Column Chart** | YoY comparison |
| 📉 **Combo Chart** | Revenue + Margin |
| 🎯 **KPI Gauge** | Performance metrics |
| 📶 **Stacked Bar** | Segment analysis |
| 📈 **Line Chart** | Growth trajectory |
| 🥧 **Pie Chart** | Market share |

### 🖼️ Intelligent Image Sourcing

KELP auto-fetches **sector-relevant images** using web scraping (no API keys):

| Sector | Image Types |
|--------|-------------|
| 🏭 Manufacturing | Factory, assembly line, industrial equipment |
| 💊 Pharmaceuticals | Laboratory, research, medicine production |
| 💻 Technology | Server rooms, software interfaces, digital transformation |
| 🎬 Entertainment | Cinema, media production, streaming services |
| 🚚 Logistics | Warehouses, supply chain, transportation |
| 🔌 Electronics | Circuit boards, defense systems, electronic components |

---

## 🛠️ Tech Stack

KELP is built on a modern, GPU-accelerated Python stack:

### 🧠 AI & Machine Learning

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core Language | 3.10+ |
| **Ollama** | Local LLM Runtime | Latest |
| **PyTorch** | GPU Acceleration | 2.1+ |
| **Transformers** | Model Hub | 4.36+ |
| **qwen2.5:7b** | Primary LLM | 7B params |

### 📊 Data & Visualization

| Technology | Purpose | Version |
|------------|---------|---------|
| **python-pptx** | PPTX Generation | 0.6.21+ |
| **Pandas** | Data Analysis | 2.0+ |
| **Matplotlib** | Chart Rendering | 3.8+ |
| **pdfplumber** | PDF Extraction | 0.9+ |
| **Pillow** | Image Processing | 10.0+ |

### 🌐 Web & Scraping

| Technology | Purpose | Version |
|------------|---------|---------|
| **ddgs** | DuckDuckGo Search | Latest |
| **BeautifulSoup4** | HTML Parsing | 4.12+ |
| **aiohttp** | Async HTTP Client | 3.9+ |
| **icrawler** | Image Fetching | Latest |
| **requests** | HTTP Requests | 2.31+ |

### 🔧 LLM Configuration

KELP uses **qwen2.5:7b** via Ollama with optimized inference parameters:

```python
# Optimized for investor-grade content
GENERATION_CONFIG = {
    "model": "qwen2.5:7b",
    "temperature": 0.4,      # Lower = more factual/consistent
    "top_p": 0.85,           # Nucleus sampling threshold  
    "repeat_penalty": 1.15,  # Reduce repetition
    "num_ctx": 4096,         # Large context window
}
```

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `temperature` | 0.4 | Factual precision over creativity |
| `top_p` | 0.85 | Balanced token diversity |
| `repeat_penalty` | 1.15 | Varied language without loops |
| `num_ctx` | 4096 | Long document understanding |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **NVIDIA GPU** (recommended) or CPU
- **[Ollama](https://ollama.ai/)** installed with `qwen2.5:7b`

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/shubro18202758/KELP.git
cd KELP

# 2. Create virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Ollama model (one-time setup)
ollama pull qwen2.5:7b
```

### Running KELP

```bash
# Process ALL companies (6 sample companies included)
python pipeline_v5_enhanced.py

# Process a SINGLE company
python pipeline_v5_enhanced.py --company kalyani

# Process specific company
python pipeline_v5_enhanced.py --company centum

# Quiet mode (less output)
python pipeline_v5_enhanced.py --quiet
```

### Expected Output

```
======================================================================
PIPELINE V5 - ENHANCED DATA-DENSE LAYOUTS
======================================================================
📂 Data: ./Company Data
📂 Output: ./output/v5_enhanced

📋 Found 6 companies to process

============================================================
📦 Processing: FORGE
============================================================
  → Loading company data...
  ✓ Loaded 42,404 characters
  → Classifying sector...
  ✓ Sector: Manufacturing & Industrials (confidence: 72%)
  🚀 Extracting financial data with GPU...
  ✓ Revenue: ₹2366Cr, EBITDA: 10.1%
  🔍 Deep researching: Manufacturing & Industrials
  📄 Found 22 unique sources
  📖 Successfully read 6 pages
  ✓ Research: Market $768.28B, CAGR 8.0%, 3 trends
  🚀 Generating investment content with GPU...
  ✓ Investment-grade content generated
  🖼️ Fetching sector images (FREE web scraping)...
  ✓ Fetched 7 sector-appropriate images
  📊 Creating Slide 1: Cover - Project Velocity
  📊 Creating Slide 2: Business Overview (4-Quadrant)
  📊 Creating Slide 3: Financial Deep-Dive (Multi-Chart)
  📊 Creating Slide 4: Investment Highlights
  📊 Creating Slide 5: Disclaimer

✅ SUCCESS: Project Velocity
   📊 PPT: Project_Velocity_Manufacturing_20260121.pptx
   🖼️ Images: 7
   ⏱ Time: 54.0s
```

---

## 📊 Sample Outputs

KELP generates **professional, data-dense presentations** with multiple chart types:

### 📑 Slide Structure

| Slide | Content | Charts |
|-------|---------|--------|
| **1. Cover** | Project codename, sector badge, background image | - |
| **2. Business Overview** | 4-quadrant layout: Description, Products, Clients, Positioning | - |
| **3. Financial Deep-Dive** | Revenue, EBITDA trends, key metrics | Donut, Area, Column |
| **4. Investment Highlights** | Key strengths, market opportunity, growth drivers | KPI badges |
| **5. Disclaimer** | Standard investment teaser disclaimer | - |

### 🏆 Sample Companies Processed

| Company | Sector | Revenue | EBITDA | Market Size | CAGR |
|---------|--------|---------|--------|-------------|------|
| Kalyani Forge | Manufacturing | ₹2,366 Cr | 10.1% | $768B | 8.0% |
| Centum | Electronics & Defense | ₹11,554 Cr | 8.4% | $175B | 5.8% |
| Connplex | Entertainment | ₹960 Cr | 27.3% | - | 9.8% |
| Gati | Logistics | ₹15,100 Cr | 4.3% | $1.2B | 8.5% |
| Ind Swift | Pharmaceuticals | ₹5,022 Cr | 9.7% | $129B | 8.09% |
| Ksolves | Technology | - | - | $166B | 13% |

---

## 📈 Performance Benchmarks

| Metric | Value |
|--------|-------|
| **Processing Time** | ~50-55 seconds per company |
| **Web Pages Read** | 5-8 per company |
| **Sources Found** | 20-25 per sector |
| **Charts Generated** | 4-6 per presentation |
| **Images Fetched** | 7 per presentation |
| **LLM Model** | qwen2.5:7b (4.4GB VRAM) |

### 💻 Hardware Tested

| Component | Specification |
|-----------|---------------|
| **GPU** | NVIDIA RTX 4070 (8GB VRAM) |
| **CPU** | Intel i9-14900HX |
| **RAM** | 32GB DDR5 |
| **Storage** | NVMe SSD |

---

## 🎨 Customization

### Adding New Sectors

Edit `src/sector_intelligence/classifier.py`:

```python
SECTORS = {
    "your_new_sector": {
        "keywords": ["keyword1", "keyword2"],
        "sub_sectors": ["sub1", "sub2"],
    }
}
```

### Changing LLM Model

Edit `src/content_generation/llm_generator.py`:

```python
MODEL = "llama3.1:8b"  # or any Ollama-supported model
```

### Modifying Slide Templates

Edit `src/presentation/enhanced_kelp_generator.py`:

```python
# Customize colors, fonts, layouts
KELP_COLORS = {
    'primary': RGBColor(0, 82, 147),    # Navy blue
    'accent': RGBColor(0, 150, 136),    # Teal
    'highlight': RGBColor(255, 193, 7), # Amber
}
```

---

## 🔮 Roadmap

- [ ] 🌍 Multi-language support (Hindi, Chinese, Spanish)
- [ ] 📱 Streamlit web interface
- [ ] 🔗 API endpoint for integration
- [ ] 📊 More chart types (Waterfall, Sankey)
- [ ] 🤖 Fine-tuned domain-specific LLM
- [ ] 📈 Real-time stock data integration

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Fork the repo, then:
git checkout -b feature/amazing-feature
git commit -m "Add amazing feature"
git push origin feature/amazing-feature
# Open a Pull Request
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **IIT Bombay Hackathon 2026** - For the amazing challenge
- **Ollama** - For democratizing local LLM inference
- **python-pptx** - For PowerPoint generation capabilities
- **DuckDuckGo** - For privacy-respecting web search

---

## 👥 Team

Built with 💚 by **Team KELP** for the **IIT Bombay Hackathon 2026**

---

<p align="center">
  <strong>⭐ Star this repo if you find it useful! ⭐</strong>
</p>

<p align="center">
  <a href="https://github.com/shubro18202758/KELP/issues">Report Bug</a> •
  <a href="https://github.com/shubro18202758/KELP/issues">Request Feature</a>
</p>
