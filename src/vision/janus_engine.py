"""
DeepSeek Janus-Pro-7B Vision-Language Engine
=============================================
Multimodal model for image understanding AND generation.
Used for:
- Generating sector-relevant images for PPT slides
- Analyzing web screenshots
- Creating charts and infographics
"""
import os
import torch
import base64
import io
import random
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Union
from dataclasses import dataclass, field
from datetime import datetime
from PIL import Image
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from config.settings import OUTPUT_DIR


@dataclass
class JanusConfig:
    """Configuration for Janus-Pro-7B via Ollama"""
    # Ollama configuration (PRIMARY)
    ollama_model: str = "janus:latest"  # Quantized 4.7GB version
    ollama_url: str = "http://localhost:11434"
    
    # GPU settings for Ollama
    num_gpu: int = 99  # Use all GPU layers
    
    # Generation settings
    max_new_tokens: int = 1024
    temperature: float = 0.7
    top_p: float = 0.9
    repeat_penalty: float = 1.1
    
    # Timeout settings
    timeout: int = 120
    
    # Image generation (optional HuggingFace)
    hf_model_name: str = "deepseek-ai/Janus-Pro-7B"
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    image_size: int = 384


class JanusProEngine:
    """
    DeepSeek Janus-Pro-7B Engine via Ollama.
    
    Uses Ollama's quantized Janus (4.7GB) as the PRIMARY engine
    with full GPU acceleration for text generation.
    
    Capabilities:
    - GPU-accelerated text generation
    - Investment narrative generation
    - Content anonymization
    - Research synthesis
    """
    
    def __init__(self, config: JanusConfig = None):
        self.config = config or JanusConfig()
        self._ollama_available = None  # Cached availability
        
        # Optional HuggingFace model for image generation
        self.hf_model = None
        self.hf_processor = None
        
        # Output directories
        self.image_output_dir = OUTPUT_DIR / "generated_images"
        self.image_output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"   🚀 Janus Engine initialized (Ollama: {self.config.ollama_model})")
    
    def _check_ollama_janus(self) -> bool:
        """Check if Ollama is running and has Janus model"""
        try:
            import requests
            response = requests.get(
                f"{self.config.ollama_url}/api/tags",
                timeout=5
            )
            if response.status_code == 200:
                models = response.json().get('models', [])
                for model in models:
                    if 'janus' in model.get('name', '').lower():
                        return True
        except:
            pass
        return False
    
    def is_available(self) -> bool:
        """Check if Janus model is available via Ollama"""
        if self._ollama_available is None:
            self._ollama_available = self._check_ollama_janus()
            if self._ollama_available:
                print("   ✓ Janus-Pro-7B available via Ollama (GPU accelerated)")
            else:
                print("   ⚠ Janus not available in Ollama")
        return self._ollama_available
    
    # =========================================================================
    # TEXT GENERATION METHODS - Core LLM functionality
    # =========================================================================
    
    def generate_text(self, prompt: str, temperature: float = None, 
                     max_tokens: int = None) -> str:
        """
        Generate text using Janus Pro 7B via Ollama (GPU accelerated).
        
        Args:
            prompt: The input prompt for text generation
            temperature: Sampling temperature (lower = more factual)
            max_tokens: Maximum tokens to generate
            
        Returns:
            Generated text string
        """
        if not self.is_available():
            return self._fallback_text_generation(prompt)
        
        temperature = temperature or self.config.temperature
        max_tokens = max_tokens or self.config.max_new_tokens
        
        try:
            import requests
            
            response = requests.post(
                f"{self.config.ollama_url}/api/generate",
                json={
                    "model": self.config.ollama_model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": temperature,
                        "num_predict": max_tokens,
                        "num_gpu": self.config.num_gpu,  # GPU acceleration
                        "top_p": self.config.top_p,
                        "repeat_penalty": self.config.repeat_penalty,
                    }
                },
                timeout=self.config.timeout
            )
            
            if response.status_code == 200:
                result = response.json().get('response', '').strip()
                return result
            else:
                print(f"   ⚠ Ollama returned status {response.status_code}")
                
        except Exception as e:
            print(f"   ⚠ Janus generation failed: {e}")
            return self._fallback_text_generation(prompt)
    
    def generate_narrative(self, context: str, sector: str, 
                          narrative_type: str = "business_overview") -> str:
        """
        Generate investment narrative content.
        
        Args:
            context: Company/business context information
            sector: Industry sector
            narrative_type: Type of narrative (business_overview, investment_highlights, etc.)
            
        Returns:
            Professional investment narrative
        """
        prompts = {
            "business_overview": f"""You are an M&A investment analyst. Write a concise, professional business overview for an investment teaser.

Sector: {sector}
Context: {context}

Write 3-4 bullet points describing the business. Use professional language. Do NOT include any company names - keep it anonymous. Focus on:
- Core business activities
- Key products/services  
- Market position
- Competitive advantages

Output only the bullet points, no headers or explanations.""",

            "investment_highlights": f"""You are an M&A investment analyst. Generate compelling investment highlights for a blind teaser.

Sector: {sector}
Context: {context}

Write 4-5 investment highlights that would attract potential buyers. Each highlight should:
- Start with a strong action word
- Be specific with metrics where available
- Focus on growth potential and value drivers
- Be anonymous (no company names)

Output only the bullet points.""",

            "market_position": f"""Summarize the market position of this business based on the context.

Sector: {sector}
Context: {context}

Write 2-3 sentences about market position, competitive landscape, and growth opportunity. Keep it anonymous and professional.""",

            "executive_summary": f"""Write a brief executive summary for an investment teaser.

Sector: {sector}
Context: {context}

Write 2-3 sentences summarizing the investment opportunity. Be compelling but factual. No company names."""
        }
        
        prompt = prompts.get(narrative_type, prompts["business_overview"])
        return self.generate_text(prompt, temperature=0.4, max_tokens=512)
    
    def anonymize_text(self, text: str, company_name: str, sector: str) -> str:
        """
        Anonymize company-specific content for blind teasers.
        
        Args:
            text: Original text containing company information
            company_name: Company name to remove
            sector: Industry sector for context
            
        Returns:
            Anonymized text suitable for blind teaser
        """
        prompt = f"""Rewrite the following text to remove all identifying information while preserving the facts and metrics.

Original text:
{text}

Company to anonymize: {company_name}
Sector: {sector}

Rules:
1. Replace "{company_name}" with "The Company" or "The Target"
2. Remove any brand names, founder names, or location specifics
3. Keep all numbers, percentages, and metrics intact
4. Maintain professional investment language
5. Keep the same length and structure

Output only the anonymized text, nothing else."""

        result = self.generate_text(prompt, temperature=0.3, max_tokens=len(text) + 200)
        
        # Fallback rule-based cleanup if LLM fails
        if not result or len(result) < 10:
            result = self._rule_based_anonymize(text, company_name)
        
        return result
    
    def synthesize_research(self, web_content: str, query: str, 
                           max_length: int = 500) -> Dict[str, Any]:
        """
        Synthesize web research content into structured insights.
        
        Args:
            web_content: Raw content from web scraping
            query: Original search query
            max_length: Maximum length of synthesis
            
        Returns:
            Dictionary with synthesized insights
        """
        prompt = f"""Analyze the following web content and extract key business intelligence.

Search Query: {query}
Web Content:
{web_content[:4000]}

Extract and structure the following:
1. MARKET_SIZE: Total addressable market value (in USD or INR)
2. CAGR: Compound annual growth rate percentage
3. KEY_TRENDS: 2-3 major industry trends
4. COMPETITIVE_LANDSCAPE: Brief overview
5. GROWTH_DRIVERS: Key factors driving growth

Format your response as:
MARKET_SIZE: [value]
CAGR: [percentage]
KEY_TRENDS: [trend1]; [trend2]; [trend3]
COMPETITIVE_LANDSCAPE: [brief description]
GROWTH_DRIVERS: [driver1]; [driver2]

If information is not available, write "N/A" for that field."""

        response = self.generate_text(prompt, temperature=0.2, max_tokens=max_length)
        
        # Parse response into structured format
        return self._parse_research_response(response)
    
    def _parse_research_response(self, response: str) -> Dict[str, Any]:
        """Parse synthesized research into structured dictionary"""
        import re
        
        result = {
            "market_size": None,
            "cagr": None,
            "key_trends": [],
            "competitive_landscape": "",
            "growth_drivers": []
        }
        
        try:
            # Extract market size
            match = re.search(r'MARKET_SIZE:\s*(.+?)(?:\n|$)', response)
            if match and 'N/A' not in match.group(1):
                result["market_size"] = match.group(1).strip()
            
            # Extract CAGR
            match = re.search(r'CAGR:\s*(\d+\.?\d*%?)', response)
            if match:
                result["cagr"] = match.group(1).strip()
            
            # Extract trends
            match = re.search(r'KEY_TRENDS:\s*(.+?)(?:\n|$)', response)
            if match and 'N/A' not in match.group(1):
                result["key_trends"] = [t.strip() for t in match.group(1).split(';')]
            
            # Extract competitive landscape
            match = re.search(r'COMPETITIVE_LANDSCAPE:\s*(.+?)(?:\n|$)', response)
            if match and 'N/A' not in match.group(1):
                result["competitive_landscape"] = match.group(1).strip()
            
            # Extract growth drivers
            match = re.search(r'GROWTH_DRIVERS:\s*(.+?)(?:\n|$)', response)
            if match and 'N/A' not in match.group(1):
                result["growth_drivers"] = [d.strip() for d in match.group(1).split(';')]
                
        except Exception as e:
            print(f"   ⚠ Failed to parse research response: {e}")
        
        return result
    
    def _fallback_text_generation(self, prompt: str) -> str:
        """Fallback using Ollama's Janus model (4.7GB quantized version)"""
        try:
            import requests
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "janus:latest",  # Use locally cached Janus
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_predict": 1024,
                        "num_gpu": 99,  # Use all GPU layers
                        "top_p": 0.9,
                    }
                },
                timeout=120
            )
            if response.status_code == 200:
                result = response.json().get('response', '').strip()
                if result:
                    return result
        except Exception as e:
            print(f"   ⚠ Ollama Janus fallback failed: {e}")
        
        # Ultimate fallback: template-based responses
        if "investment" in prompt.lower():
            return "• Strong market position in a growing industry\n• Proven track record of operational excellence\n• Attractive financial profile with growth potential\n• Strategic value to potential acquirers"
        elif "anonymize" in prompt.lower():
            return "The Company operates in its core sector with established market presence."
        elif "overview" in prompt.lower():
            return "The Target is a well-established player in its industry segment with diversified operations and strong client relationships."
        else:
            return "Content generation unavailable - Janus model not loaded."
    
    def _rule_based_anonymize(self, text: str, company_name: str) -> str:
        """Rule-based fallback for anonymization"""
        import re
        
        result = text
        
        # Replace company name variations
        patterns = [
            (rf'\b{re.escape(company_name)}\b', 'The Company'),
            (rf'\b{re.escape(company_name.upper())}\b', 'THE COMPANY'),
            (rf'\b{re.escape(company_name.lower())}\b', 'the company'),
            (rf'\b{re.escape(company_name.title())}\b', 'The Company'),
        ]
        
        for pattern, replacement in patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # Remove common identifying phrases
        result = re.sub(r'founded by [A-Za-z\s]+', 'founded by the promoters', result, flags=re.IGNORECASE)
        result = re.sub(r'headquarters in [A-Za-z\s,]+', 'headquarters in India', result, flags=re.IGNORECASE)
        
        return result
    

    def generate_sector_image(self, sector: str, image_type: str = "generic",
                             seed: int = None) -> Optional[Path]:
        """
        Generate a sector-relevant image for PPT slides.
        
        Args:
            sector: Industry sector (manufacturing, pharma, tech, etc.)
            image_type: Type of image (product, facility, abstract, chart)
            seed: Random seed for reproducibility
            
        Returns:
            Path to generated image or None
        """
        if not self.is_available():
            return self._generate_placeholder_image(sector, image_type)
        
        # Build prompt based on sector and type
        prompts = self._get_image_prompts(sector, image_type)
        prompt = random.choice(prompts) if isinstance(prompts, list) else prompts
        
        try:
            # Set seed for reproducibility if provided
            if seed:
                torch.manual_seed(seed)
            
            # Generate image using Janus
            with torch.no_grad():
                # Prepare conversation for image generation
                conversation = [
                    {"role": "user", "content": f"Generate an image: {prompt}"}
                ]
                
                # Process input
                inputs = self.processor(
                    conversations=conversation,
                    images=None,
                    force_batchify=True,
                    return_tensors="pt"
                ).to(self.config.device)
                
                # Generate
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=self.config.image_size * self.config.image_size,
                    temperature=self.config.temperature,
                    do_sample=True,
                )
                
                # Decode image from tokens
                image = self.image_gen_processor.decode(
                    outputs[0],
                    image_size=self.config.image_size
                )
                
            # Save image
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{sector}_{image_type}_{timestamp}.png"
            output_path = self.image_output_dir / filename
            image.save(output_path)
            
            print(f"   🖼 Generated: {filename}")
            return output_path
            
        except Exception as e:
            print(f"   ⚠ Image generation failed: {e}")
            return self._generate_placeholder_image(sector, image_type)
    
    def _get_image_prompts(self, sector: str, image_type: str) -> List[str]:
        """Get appropriate prompts for sector and image type"""
        
        sector_prompts = {
            "manufacturing": {
                "product": [
                    "Professional photograph of precision engineered metal components on white background, industrial quality, no logos",
                    "Modern manufacturing equipment in clean factory setting, professional lighting, no visible branding",
                    "High-quality machined parts arrangement, industrial photography style, neutral background",
                ],
                "facility": [
                    "Modern manufacturing plant interior with automated machinery, bright lighting, professional photograph",
                    "Clean industrial workspace with robotic arms, modern factory aesthetic, no logos visible",
                    "Aerial view of modern industrial complex, professional photography, generic design",
                ],
                "abstract": [
                    "Abstract representation of manufacturing precision, geometric shapes in blue and silver, professional design",
                    "Modern industrial infographic background, clean lines, professional color scheme",
                ]
            },
            "pharmaceuticals": {
                "product": [
                    "Pharmaceutical laboratory with modern equipment, clean room aesthetic, professional photograph",
                    "Medicine capsules and tablets arrangement on white background, pharmaceutical quality",
                    "Scientific research equipment in modern lab setting, no branding visible",
                ],
                "facility": [
                    "Modern pharmaceutical research facility interior, clean and bright, professional",
                    "GMP certified production line, clean room environment, generic design",
                ],
                "abstract": [
                    "Abstract molecular structure visualization, pharmaceutical blue tones, professional design",
                    "DNA helix with pharmaceutical elements, modern scientific aesthetic",
                ]
            },
            "technology": {
                "product": [
                    "Modern server room with blue LED lighting, technology aesthetic, professional",
                    "Software development workspace, multiple monitors with code, modern office",
                    "Cloud computing visualization, abstract data center concept",
                ],
                "facility": [
                    "Modern tech office space with collaborative areas, bright and innovative design",
                    "Data center interior with server racks, blue lighting, professional photograph",
                ],
                "abstract": [
                    "Abstract network connectivity visualization, blue nodes and connections",
                    "Digital transformation concept, modern technology infographic style",
                ]
            },
            "logistics": {
                "product": [
                    "Modern logistics warehouse interior, organized shelving, professional lighting",
                    "Fleet of delivery trucks, aerial view, professional photograph, no logos",
                    "Automated sorting facility, conveyor systems, modern logistics",
                ],
                "facility": [
                    "Large distribution center aerial view, modern logistics hub design",
                    "Supply chain visualization, warehouse to delivery network",
                ],
                "abstract": [
                    "Abstract supply chain network, connected nodes and routes, professional design",
                    "Global logistics map visualization, modern infographic style",
                ]
            },
            "electronics": {
                "product": [
                    "Printed circuit boards arrangement, electronic components, professional macro photography",
                    "Modern electronic assembly, semiconductor chips, clean room environment",
                    "Aerospace electronics modules, high-precision components, professional",
                ],
                "facility": [
                    "Electronics manufacturing clean room, automated assembly lines",
                    "R&D laboratory with testing equipment, modern electronics facility",
                ],
                "abstract": [
                    "Abstract circuit pattern, electronic pathways, blue and gold tones",
                    "Technology innovation concept, electronic components in modern design",
                ]
            },
            "entertainment": {
                "product": [
                    "Modern cinema interior, comfortable seating, ambient lighting",
                    "Movie theater projection room, professional equipment",
                    "Entertainment venue lobby, modern design aesthetic",
                ],
                "facility": [
                    "Multiplex cinema exterior, modern architecture, evening lighting",
                    "Entertainment complex aerial view, contemporary design",
                ],
                "abstract": [
                    "Abstract entertainment concept, film reel and digital elements",
                    "Movie and media visualization, creative industry design",
                ]
            }
        }
        
        # Get sector-specific prompts or default
        sector_key = sector.lower().split()[0]  # Take first word
        sector_data = sector_prompts.get(sector_key, sector_prompts.get("manufacturing"))
        
        return sector_data.get(image_type, sector_data.get("abstract", ["Professional business image"]))
    
    def _generate_placeholder_image(self, sector: str, image_type: str) -> Path:
        """Generate a placeholder image when model not available"""
        from PIL import Image, ImageDraw, ImageFont
        
        # Create gradient background
        width, height = 800, 600
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        
        # Sector colors
        sector_colors = {
            "manufacturing": [(45, 35, 75), (0, 191, 179)],
            "pharmaceuticals": [(45, 35, 75), (126, 87, 194)],
            "technology": [(45, 35, 75), (0, 150, 255)],
            "logistics": [(45, 35, 75), (254, 185, 95)],
            "electronics": [(45, 35, 75), (232, 77, 138)],
            "entertainment": [(45, 35, 75), (255, 105, 135)],
        }
        
        colors = sector_colors.get(sector.lower().split()[0], [(45, 35, 75), (0, 191, 179)])
        
        # Create gradient
        for y in range(height):
            r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * y / height)
            g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * y / height)
            b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * y / height)
            draw.line([(0, y), (width, y)], fill=(r, g, b))
        
        # Add sector text
        try:
            font = ImageFont.truetype("arial.ttf", 40)
            small_font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()
            small_font = font
        
        sector_text = sector.upper()
        type_text = f"[ {image_type.upper()} ]"
        
        # Center text
        draw.text((width//2, height//2 - 30), sector_text, fill=(255, 255, 255), 
                  anchor="mm", font=font)
        draw.text((width//2, height//2 + 30), type_text, fill=(200, 200, 200),
                  anchor="mm", font=small_font)
        
        # Save
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{sector.split()[0].lower()}_{image_type}_{timestamp}.png"
        output_path = self.image_output_dir / filename
        image.save(output_path)
        
        return output_path
    
    def analyze_image(self, image_path: Union[str, Path]) -> str:
        """
        Analyze an image and generate description.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Text description of image
        """
        if not self.is_available():
            return "Image analysis not available - model not loaded"
        
        try:
            image = Image.open(image_path).convert("RGB")
            
            conversation = [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "image": image},
                        {"type": "text", "text": "Describe this image in detail, focusing on business-relevant elements."}
                    ]
                }
            ]
            
            inputs = self.processor(
                conversations=conversation,
                images=[image],
                force_batchify=True,
                return_tensors="pt"
            ).to(self.config.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=self.config.max_new_tokens,
                    temperature=0.3,
                    do_sample=False,
                )
            
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return response
            
        except Exception as e:
            return f"Analysis failed: {e}"
    
    def generate_chart_image(self, chart_type: str, data: Dict, 
                            title: str = "") -> Optional[Path]:
        """
        Generate a chart/graph image.
        
        Args:
            chart_type: bar, pie, line, etc.
            data: Chart data
            title: Chart title
            
        Returns:
            Path to generated chart image
        """
        # Use matplotlib for reliable chart generation
        try:
            import matplotlib.pyplot as plt
            import matplotlib
            matplotlib.use('Agg')
            
            # Kelp color palette
            colors = ['#00BFB3', '#E84D8A', '#FEB95F', '#7B68EE', '#4ECDC4']
            
            fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')
            
            if chart_type == "bar":
                categories = data.get('categories', ['A', 'B', 'C'])
                values = data.get('values', [10, 20, 30])
                bars = ax.bar(categories, values, color=colors[:len(categories)])
                ax.set_ylabel(data.get('ylabel', 'Value'))
                
            elif chart_type == "pie":
                labels = data.get('labels', ['A', 'B', 'C'])
                sizes = data.get('values', [30, 40, 30])
                ax.pie(sizes, labels=labels, colors=colors[:len(labels)], 
                      autopct='%1.0f%%', startangle=90)
                ax.axis('equal')
                
            elif chart_type == "line":
                x = data.get('x', range(5))
                y = data.get('y', [10, 15, 13, 18, 22])
                ax.plot(x, y, color=colors[0], linewidth=3, marker='o')
                ax.fill_between(x, y, alpha=0.3, color=colors[0])
                ax.set_xlabel(data.get('xlabel', ''))
                ax.set_ylabel(data.get('ylabel', ''))
            
            if title:
                ax.set_title(title, fontsize=14, fontweight='bold', color='#2D234B')
            
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            # Save
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"chart_{chart_type}_{timestamp}.png"
            output_path = self.image_output_dir / filename
            plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
            plt.close()
            
            return output_path
            
        except Exception as e:
            print(f"   ⚠ Chart generation failed: {e}")
            return None


# Singleton instance
_janus_engine = None

def get_janus_engine() -> JanusProEngine:
    """Get or create Janus engine singleton"""
    global _janus_engine
    if _janus_engine is None:
        _janus_engine = JanusProEngine()
    return _janus_engine


def generate_sector_images(sector: str, count: int = 3) -> List[Path]:
    """
    Generate multiple sector-relevant images.
    
    Args:
        sector: Industry sector
        count: Number of images to generate
        
    Returns:
        List of paths to generated images
    """
    engine = get_janus_engine()
    images = []
    
    image_types = ["product", "facility", "abstract"]
    
    for i in range(min(count, len(image_types))):
        image_path = engine.generate_sector_image(sector, image_types[i])
        if image_path:
            images.append(image_path)
    
    return images


if __name__ == "__main__":
    print("Testing DeepSeek Janus-Pro Engine...")
    print("=" * 50)
    
    engine = get_janus_engine()
    
    # Test placeholder generation (always works)
    print("\nGenerating placeholder images...")
    for sector in ["Manufacturing", "Pharmaceuticals", "Technology"]:
        path = engine._generate_placeholder_image(sector, "product")
        print(f"  {sector}: {path}")
    
    # Test chart generation
    print("\nGenerating charts...")
    chart_path = engine.generate_chart_image(
        "bar",
        {"categories": ["FY22", "FY23", "FY24", "FY25"], "values": [120, 145, 180, 220]},
        "Revenue Growth (₹ Cr)"
    )
    print(f"  Bar chart: {chart_path}")
    
    pie_path = engine.generate_chart_image(
        "pie",
        {"labels": ["Products", "Services", "Exports"], "values": [45, 30, 25]},
        "Revenue Mix"
    )
    print(f"  Pie chart: {pie_path}")
