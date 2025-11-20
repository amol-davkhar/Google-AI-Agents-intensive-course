# AI Brand Studio - Project Specification

## Project Metadata

**Track:** Enterprise Agents
**Team Size:** [1-4 members]
**Submission Deadline:** December 1, 2025, 11:59 AM PT
**Repository:** [To be created]

---

## Executive Summary

**AI Brand Studio** is a multi-agent system that generates legally-clear, SEO-optimized brand names with complete brand narratives and marketing copy. Unlike simple name generators, it uses RAG (Retrieval-Augmented Generation) to check trademark conflicts, verify domain availability, and generate complete brand packages in minutes instead of weeks.

---

## 1. Problem Statement

### The Challenge
Early-stage founders and marketing teams face significant challenges in brand naming:
- **Time-consuming:** Average 20+ hours spent on naming and validation
- **Legal risks:** 67% of startups rebrand within the first year due to trademark conflicts
- **Fragmented process:** Requires checking multiple databases (trademarks, domains, SEO tools)
- **Inconsistent branding:** Name often doesn't align with tagline, story, or marketing copy
- **No context:** Generic generators don't understand industry-specific naming patterns

### Current Solutions & Gaps
**Existing tools:**
- Simple name generators (Namelix, Business Name Generator) - no validation
- Domain checkers - only check availability, no trademark screening
- SEO tools - generic suggestions, not brand-specific

**What's missing:**
- Integrated trademark + domain + SEO validation
- Industry-aware name generation using RAG
- Complete brand package (name + story + marketing copy)
- Iterative refinement based on user preferences
- Multi-agent orchestration for comprehensive brand creation

---

## 2. Solution Overview

### Value Proposition
> "Generate legally-clear, SEO-optimized brand identities with complete marketing narratives in under 10 minutes - reducing brand creation time by 90% while minimizing legal risks."

### Core Capabilities

1. **Intelligent Name Generation**
   - Industry-specific names using RAG from successful brands
   - Multiple naming styles (descriptive, invented, combined, acronyms)
   - Customizable brand personality (playful, professional, innovative, etc.)

2. **Legal & Technical Validation**
   - Real-time trademark conflict detection (USPTO, EU IPO)
   - Domain availability checking (.com, .ai, .io, etc.)
   - Similar brand name analysis to avoid confusion

3. **SEO Optimization**
   - Keyword-optimized brand names
   - SEO-ready meta titles and descriptions
   - Search-friendly taglines

4. **Complete Brand Package**
   - Brand name with variations
   - Tagline (3-5 options)
   - Brand story/narrative (150-300 words)
   - Landing page hero section copy
   - Meta descriptions for SEO

5. **Iterative Refinement**
   - Session memory for conversation context
   - Long-term memory for user preferences
   - Learning from accepted/rejected suggestions

---

## 3. Capstone Requirements Mapping

### Required: Demonstrate 3+ Key Concepts ✅

We're implementing **7 key concepts** from the course:

| # | Concept | Implementation |
|---|---------|----------------|
| 1 | **Multi-Agent System** | 6 specialized agents with parallel + sequential + loop workflows |
| 2 | **Custom Tools** | Trademark API, domain checker, SEO analyzer |
| 3 | **Built-in Tools** | Google Search for competitive research |
| 4 | **MCP Tools** | Integration with trademark databases (optional) |
| 5 | **Sessions & State Management** | DatabaseSessionService for conversation continuity |
| 6 | **Long-term Memory** | Memory Bank for user preferences across sessions |
| 7 | **Context Compaction** | Summarize long brainstorming sessions |
| 8 | **Agent Evaluation** | Test suite with sample brand briefs |
| 9 | **Observability** | Logging and tracing for debugging |

**Bonus Points:**
- ✅ Gemini models (5 pts)
- ✅ Agent deployment to Vertex AI Agent Engine (5 pts)
- ✅ YouTube demo video (10 pts)

---

## 4. Technical Architecture

### 4.1 Multi-Agent System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  User Input (Product Brief)              │
│  "AI meal planning app for busy millennial parents"     │
└───────────────────────┬─────────────────────────────────┘
                        ↓
┌───────────────────────────────────────────────────────────┐
│              ORCHESTRATOR AGENT (LLM-based)               │
│  - Analyzes user brief                                    │
│  - Coordinates sub-agents                                 │
│  - Manages workflow execution                             │
└───────────────────┬───────────────────────────────────────┘
                    ↓
        ┌───────────┴───────────┬───────────────────┐
        ↓                       ↓                   ↓
┌──────────────┐      ┌──────────────────┐   ┌──────────────┐
│   RESEARCH   │      │  NAME GENERATOR  │   │  VALIDATION  │
│    AGENT     │      │      AGENT       │   │   AGENT      │
│ (Parallel)   │      │  (Sequential)    │   │ (Parallel)   │
└──────┬───────┘      └────────┬─────────┘   └──────┬───────┘
       │                       │                     │
       │ • Industry trends     │ • 20-50 candidates  │ • Trademark check
       │ • Competitor names    │ • Multiple styles   │ • Domain check
       │ • Naming patterns     │ • RAG-enhanced      │ • Conflict analysis
       │                       │                     │
       └───────────────────────┴─────────────────────┘
                               ↓
                    ┌──────────────────┐
                    │   LOOP WORKFLOW  │
                    │  If conflicts:   │
                    │  → Regenerate    │
                    └────────┬─────────┘
                             ↓
                ┌────────────┴──────────────┐
                ↓                           ↓
        ┌──────────────┐           ┌──────────────┐
        │ SEO OPTIMIZER│           │    STORY     │
        │    AGENT     │           │   GENERATOR  │
        │ (Sequential) │           │    AGENT     │
        └──────┬───────┘           └──────┬───────┘
               │                          │
               │ • Keywords               │ • Brand narrative
               │ • Meta titles            │ • Taglines
               │ • Descriptions           │ • Marketing copy
               │                          │
               └──────────┬───────────────┘
                          ↓
                ┌─────────────────────┐
                │  APPROVAL WORKFLOW  │
                │ (Long-Running Op)   │
                │ User selects final  │
                └──────────┬──────────┘
                           ↓
                ┌──────────────────────┐
                │   BRAND PACKAGE      │
                │ • Final name         │
                │ • Tagline            │
                │ • Story              │
                │ • Marketing copy     │
                │ • Domain info        │
                │ • SEO metadata       │
                └──────────────────────┘
```

### 4.2 Agent Specifications

#### 4.2.1 Orchestrator Agent
```python
orchestrator = LlmAgent(
    name="brand_orchestrator",
    model="gemini-2.5-flash-lite",
    description="Coordinates brand creation workflow",
    instruction="""
    You are the orchestrator for AI Brand Studio. Your role:
    1. Analyze user's product brief and extract key attributes
    2. Coordinate sub-agents to generate brand names
    3. Ensure validation before proceeding to content generation
    4. Present results in a structured format
    """,
    sub_agents=[
        research_agent,
        name_generator_agent,
        validation_agent,
        seo_optimizer_agent,
        story_generator_agent
    ]
)
```

#### 4.2.2 Research Agent
```python
research_agent = LlmAgent(
    name="brand_research_agent",
    model="gemini-2.5-flash-lite",
    description="Researches industry trends and competitor brands",
    tools=[
        google_search,  # Built-in tool
        search_similar_brands,  # Custom RAG tool
        analyze_industry_patterns  # Custom tool
    ],
    instruction="""
    Research the industry and identify:
    - Top competitors and their naming patterns
    - Industry-specific keywords
    - Emerging trends in the space
    - Naming conventions to avoid
    """
)
```

#### 4.2.3 Name Generator Agent
```python
name_generator = LlmAgent(
    name="name_generator",
    model="gemini-2.5-pro",  # More powerful for creative generation
    description="Generates creative, industry-appropriate brand names",
    tools=[
        generate_portmanteau,  # Custom tool
        generate_descriptive_names,  # Custom tool
        generate_invented_names,  # Custom tool
        rag_retrieve_similar_names  # RAG tool
    ],
    instruction="""
    Generate 20-50 brand name candidates using:
    - Industry context from research
    - User's brand personality preferences
    - RAG retrieval of successful similar brands
    - Multiple naming strategies (portmanteau, descriptive, invented)

    Prioritize names that are:
    - Memorable and pronounceable
    - 2-3 syllables (ideal)
    - Available as .com domains (likely)
    - Unique and distinctive
    """
)
```

#### 4.2.4 Validation Agent
```python
validation_agent = LlmAgent(
    name="validation_agent",
    model="gemini-2.5-flash-lite",
    description="Validates names for legal and technical availability",
    tools=[
        check_domain_availability,  # Custom tool
        search_trademarks_uspto,  # Custom tool
        search_trademarks_euipo,  # Custom tool
        check_social_handles,  # Custom tool (bonus)
        analyze_brand_conflicts  # Custom tool
    ],
    instruction="""
    For each name candidate:
    1. Check .com, .ai, .io domain availability
    2. Search USPTO trademark database
    3. Search EU IPO trademark database
    4. Identify potential conflicts
    5. Assign risk score (low/medium/high)

    Flag any names with:
    - Exact trademark matches
    - High similarity to existing brands in same category
    - Domain unavailable with no good alternatives
    """
)
```

#### 4.2.5 SEO Optimizer Agent
```python
seo_optimizer = LlmAgent(
    name="seo_optimizer",
    model="gemini-2.5-flash-lite",
    description="Optimizes brand names and content for search engines",
    tools=[
        analyze_keyword_volume,  # Custom tool
        generate_meta_title,  # Custom tool
        generate_meta_description,  # Custom tool
        calculate_seo_score  # Custom tool
    ],
    instruction="""
    For each validated name:
    1. Analyze keyword search volume
    2. Generate SEO-optimized meta title (50-60 chars)
    3. Generate meta description (150-160 chars)
    4. Calculate overall SEO score (0-100)
    5. Suggest keyword variations

    Optimize for:
    - Search intent matching
    - Keyword inclusion without stuffing
    - Click-through rate optimization
    """
)
```

#### 4.2.6 Story Generator Agent
```python
story_generator = LlmAgent(
    name="story_generator",
    model="gemini-2.5-pro",  # More powerful for creative writing
    description="Creates brand narratives and marketing copy",
    tools=[
        generate_brand_story,  # Custom tool
        generate_taglines,  # Custom tool
        generate_landing_copy,  # Custom tool
        analyze_tone_consistency  # Custom tool
    ],
    instruction="""
    Create a complete brand narrative including:
    1. 3-5 tagline options (5-8 words each)
    2. Brand story (150-300 words)
    3. Landing page hero section (50-100 words)
    4. Value proposition statement (20-30 words)

    Match the tone to user's brand personality:
    - Professional: authoritative, trustworthy
    - Playful: fun, energetic, casual
    - Innovative: forward-thinking, cutting-edge
    - Luxury: sophisticated, exclusive
    """
)
```

### 4.3 Workflow Patterns

#### Pattern 1: Parallel Execution
```python
# Research and initial generation happen in parallel
parallel_workflow = ParallelAgent(
    agents=[research_agent, name_generator]
)
```

#### Pattern 2: Sequential Pipeline
```python
# Generation → Validation → SEO → Story
sequential_workflow = SequentialAgent(
    agents=[
        name_generator,
        validation_agent,
        seo_optimizer,
        story_generator
    ]
)
```

#### Pattern 3: Loop Refinement
```python
# If validation fails, regenerate names
loop_workflow = LoopAgent(
    agent=name_generator,
    condition=lambda result: result.validation_passed == False,
    max_iterations=3
)
```

---

## 5. RAG Implementation

### 5.1 RAG Architecture

```
┌─────────────────────────────────────────────────┐
│           BRAND NAME CORPUS                     │
│  • Top 10,000 successful brand names            │
│  • Product Hunt startups (2020-2024)            │
│  • Fortune 500 company names                    │
│  • Industry-specific brands                     │
│  • Trademark database extracts                  │
└────────────────────┬────────────────────────────┘
                     ↓
        ┌────────────────────────────┐
        │   EMBEDDING GENERATION      │
        │  (Vertex AI Embeddings)     │
        │  text-embedding-004         │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │   VECTOR DATABASE           │
        │  Vertex AI Vector Search    │
        │  • ~768 dimensions          │
        │  • Metadata: industry,      │
        │    year, category, status   │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │   RETRIEVAL QUERY           │
        │  User brief → Embedding     │
        │  → K-NN search (k=50)       │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │   AUGMENTED GENERATION      │
        │  Retrieved examples +       │
        │  User brief → LLM           │
        │  → New brand names          │
        └─────────────────────────────┘
```

### 5.2 Data Sources

**Primary Sources:**
1. **Product Hunt Dataset**
   - Source: Product Hunt API or web scraping
   - Data: ~50,000 startup names (2015-2024)
   - Metadata: category, launch date, upvotes

2. **USPTO Trademark Database**
   - Source: USPTO TESS (Trademark Electronic Search System)
   - Data: Active trademarks
   - Metadata: category, filing date, status

3. **Curated Brand Lists**
   - Fortune 500 companies
   - Y Combinator startups
   - TechCrunch featured companies
   - Category: AI, healthcare, fintech, etc.

**Metadata Schema:**
```json
{
  "brand_name": "Stripe",
  "industry": "fintech",
  "category": "payments",
  "year_founded": 2010,
  "description": "Online payment processing",
  "naming_strategy": "invented_word",
  "syllables": 1,
  "domain": "stripe.com",
  "trademark_status": "active"
}
```

### 5.3 Retrieval Strategy

```python
from vertexai.preview.generative_models import GenerativeModel
from vertexai.language_models import TextEmbeddingModel

# Initialize embedding model
embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-004")

def retrieve_similar_brands(user_brief: str, industry: str, k: int = 50) -> list:
    """
    Retrieve similar brand names from vector database

    Args:
        user_brief: User's product description
        industry: Target industry (e.g., "healthcare", "fintech")
        k: Number of results to return

    Returns:
        List of similar brand names with metadata
    """
    # Generate embedding for user brief
    query_embedding = embedding_model.get_embeddings([user_brief])[0].values

    # Search vector database with filters
    results = vector_search_index.search(
        embedding=query_embedding,
        num_neighbors=k,
        filter={
            "industry": industry,
            "trademark_status": "active"
        }
    )

    return results
```

### 5.4 Vector Database Setup (Vertex AI Vector Search)

```python
from google.cloud import aiplatform

# Create Vector Search index
index = aiplatform.MatchingEngineIndex.create_tree_ah_index(
    display_name="brand-names-index",
    dimensions=768,  # text-embedding-004 dimensions
    approximate_neighbors_count=50,
    distance_measure_type="DOT_PRODUCT_DISTANCE",
    shard_size="SHARD_SIZE_SMALL"
)

# Create index endpoint
index_endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
    display_name="brand-names-endpoint",
    public_endpoint_enabled=True
)

# Deploy index to endpoint
index_endpoint.deploy_index(
    index=index,
    deployed_index_id="brand_names_deployed"
)
```

---

## 6. Custom Tools Implementation

### 6.1 Domain Availability Checker

```python
import whois
from typing import Dict, List

def check_domain_availability(names: List[str]) -> Dict[str, dict]:
    """
    Check domain availability for brand names

    Args:
        names: List of brand names to check

    Returns:
        Dictionary with availability status for each domain
    """
    results = {}
    extensions = ['.com', '.ai', '.io', '.co']

    for name in names:
        name_clean = name.lower().replace(' ', '')
        results[name] = {}

        for ext in extensions:
            domain = f"{name_clean}{ext}"
            try:
                w = whois.whois(domain)
                # If domain_name exists, it's registered
                results[name][ext] = {
                    'available': w.domain_name is None,
                    'domain': domain
                }
            except Exception:
                # Exception usually means domain is available
                results[name][ext] = {
                    'available': True,
                    'domain': domain
                }

    return results
```

### 6.2 Trademark Search Tool

```python
import requests
from typing import List, Dict

def search_trademarks_uspto(brand_name: str, category: str = None) -> Dict:
    """
    Search USPTO trademark database for conflicts

    Args:
        brand_name: Brand name to search
        category: Nice classification category (optional)

    Returns:
        Dictionary with trademark search results
    """
    # USPTO TESS API endpoint (public data)
    base_url = "https://uspto.report/api/search/trademarks"

    params = {
        'query': brand_name,
        'status': 'active',
        'limit': 10
    }

    if category:
        params['nice_class'] = category

    try:
        response = requests.get(base_url, params=params)
        results = response.json()

        return {
            'brand_name': brand_name,
            'conflicts_found': len(results.get('results', [])),
            'exact_matches': [
                r for r in results.get('results', [])
                if r['mark'].lower() == brand_name.lower()
            ],
            'similar_marks': [
                r for r in results.get('results', [])
                if r['mark'].lower() != brand_name.lower()
            ],
            'risk_level': assess_trademark_risk(results)
        }
    except Exception as e:
        return {
            'error': str(e),
            'risk_level': 'unknown'
        }

def assess_trademark_risk(results: dict) -> str:
    """Assess trademark conflict risk level"""
    exact_matches = len([
        r for r in results.get('results', [])
        if r.get('status') == 'active'
    ])

    if exact_matches > 0:
        return 'high'
    elif len(results.get('results', [])) > 3:
        return 'medium'
    else:
        return 'low'
```

### 6.3 SEO Analyzer Tool

```python
from typing import Dict
import requests

def analyze_seo_metrics(brand_name: str, tagline: str) -> Dict:
    """
    Analyze SEO metrics for brand name and tagline

    Args:
        brand_name: Brand name to analyze
        tagline: Brand tagline

    Returns:
        SEO metrics and scores
    """
    combined_text = f"{brand_name} {tagline}"

    # Calculate various SEO metrics
    metrics = {
        'brand_name': brand_name,
        'length_score': calculate_length_score(brand_name),
        'pronounceability_score': calculate_pronounceability(brand_name),
        'memorability_score': calculate_memorability(brand_name),
        'keyword_density': analyze_keyword_density(combined_text),
        'search_volume': estimate_search_volume(brand_name),
        'overall_seo_score': 0
    }

    # Calculate overall score (weighted average)
    metrics['overall_seo_score'] = (
        metrics['length_score'] * 0.2 +
        metrics['pronounceability_score'] * 0.3 +
        metrics['memorability_score'] * 0.3 +
        metrics['search_volume'] * 0.2
    )

    return metrics

def calculate_length_score(name: str) -> float:
    """Score based on ideal name length (2-3 syllables)"""
    length = len(name)
    if 5 <= length <= 10:
        return 100.0
    elif 4 <= length <= 12:
        return 80.0
    else:
        return max(0, 100 - abs(8 - length) * 10)

def calculate_pronounceability(name: str) -> float:
    """Simple heuristic for pronounceability"""
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    vowel_count = sum(1 for c in name.lower() if c in vowels)
    consonant_count = sum(1 for c in name.lower() if c in consonants)

    # Ideal ratio is roughly 40% vowels
    vowel_ratio = vowel_count / len(name) if len(name) > 0 else 0
    ideal_ratio = 0.4

    score = max(0, 100 - abs(vowel_ratio - ideal_ratio) * 200)
    return score

def calculate_memorability(name: str) -> float:
    """Heuristic for name memorability"""
    score = 100.0

    # Penalize very long names
    if len(name) > 12:
        score -= (len(name) - 12) * 5

    # Reward unique letter patterns
    unique_chars = len(set(name.lower()))
    if unique_chars / len(name) > 0.7:
        score += 10

    # Penalize hard-to-type characters
    hard_chars = sum(1 for c in name if c in '-_.')
    score -= hard_chars * 10

    return max(0, min(100, score))

def estimate_search_volume(brand_name: str) -> float:
    """
    Estimate potential search volume (simplified)
    In production, use Google Keyword Planner API
    """
    # Placeholder: in reality, use actual search data
    # For now, score based on common word presence
    common_words = ['app', 'io', 'tech', 'ai', 'hub', 'lab']

    score = 50.0  # baseline
    for word in common_words:
        if word in brand_name.lower():
            score += 10

    return min(100, score)
```

### 6.4 Brand Story Generator Tool

```python
from vertexai.generative_models import GenerativeModel

def generate_brand_story(
    brand_name: str,
    product_description: str,
    brand_personality: str,
    target_audience: str
) -> Dict:
    """
    Generate comprehensive brand story and marketing copy

    Args:
        brand_name: Selected brand name
        product_description: What the product does
        brand_personality: Tone (professional, playful, innovative, luxury)
        target_audience: Who the product is for

    Returns:
        Dictionary with taglines, story, and marketing copy
    """
    model = GenerativeModel("gemini-2.5-pro")

    prompt = f"""
    You are a brand strategist creating a comprehensive brand identity.

    Brand Name: {brand_name}
    Product: {product_description}
    Personality: {brand_personality}
    Target Audience: {target_audience}

    Create:
    1. Five tagline options (5-8 words each, memorable and action-oriented)
    2. A brand story (200-300 words) that explains:
       - What the brand stands for
       - Why it exists (origin story)
       - How it helps the target audience
       - What makes it different
    3. Landing page hero section copy (50-100 words, conversion-focused)
    4. A value proposition statement (20-30 words, clear and compelling)

    Match the {brand_personality} tone throughout all copy.
    Make it authentic, not generic or cliché.

    Format the response as JSON with keys: taglines, story, hero_copy, value_prop
    """

    response = model.generate_content(prompt)

    # Parse JSON response
    import json
    story_content = json.loads(response.text)

    return {
        'brand_name': brand_name,
        'taglines': story_content.get('taglines', []),
        'story': story_content.get('story', ''),
        'hero_copy': story_content.get('hero_copy', ''),
        'value_proposition': story_content.get('value_prop', '')
    }
```

---

## 7. Google Cloud Infrastructure

### 7.1 Recommended Google Cloud Stack

| Component | Google Cloud Service | Purpose |
|-----------|---------------------|---------|
| **Agent Runtime** | Vertex AI Agent Engine | Host and scale the multi-agent system |
| **LLM Models** | Gemini 2.5 Flash / Pro | Power all agents |
| **Vector Database** | Vertex AI Vector Search | Store and retrieve brand name embeddings |
| **Session Storage** | Cloud SQL (PostgreSQL) | Persist session data |
| **Long-term Memory** | Vertex AI Memory Bank | Store user preferences across sessions |
| **File Storage** | Cloud Storage | Store datasets, logs, exports |
| **API Gateway** | Cloud Run | Alternative deployment option |
| **Monitoring** | Cloud Logging + Monitoring | Observability and debugging |
| **Secrets Management** | Secret Manager | Store API keys securely |
| **CI/CD** | Cloud Build | Automated deployment pipeline |

### 7.2 Architecture Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                         │
│              (Web App / API Client / CLI)                     │
└────────────────────────┬─────────────────────────────────────┘
                         ↓ HTTPS
┌────────────────────────────────────────────────────────────────┐
│                    CLOUD RUN (API Gateway)                      │
│                  - Rate limiting                                │
│                  - Authentication                               │
│                  - Request routing                              │
└────────────────────────┬───────────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────────────────────┐
│              VERTEX AI AGENT ENGINE                             │
│                                                                 │
│  ┌──────────────────────────────────────────────────────┐      │
│  │         Orchestrator Agent (gemini-2.5-flash)        │      │
│  └───┬──────────────────────────────────────────────┬───┘      │
│      │                                              │          │
│  ┌───┴─────────┐  ┌──────────────┐  ┌─────────────┴───┐      │
│  │  Research   │  │ Name Gen     │  │  Validation     │      │
│  │  Agent      │  │ Agent (Pro)  │  │  Agent          │      │
│  └─────────────┘  └──────────────┘  └─────────────────┘      │
│                                                                 │
│  ┌─────────────┐  ┌──────────────┐                            │
│  │ SEO Agent   │  │ Story Agent  │                            │
│  └─────────────┘  └──────────────┘                            │
└──────┬──────────────────┬──────────────────┬──────────────────┘
       │                  │                  │
       ↓                  ↓                  ↓
┌──────────────┐   ┌──────────────┐   ┌──────────────────┐
│ VERTEX AI    │   │  CLOUD SQL   │   │  VERTEX AI       │
│ VECTOR       │   │ (PostgreSQL) │   │  MEMORY BANK     │
│ SEARCH       │   │              │   │                  │
│              │   │ - Sessions   │   │ - User prefs     │
│ - Brand DB   │   │ - State mgmt │   │ - Past projects  │
│ - Embeddings │   │              │   │ - Feedback       │
└──────────────┘   └──────────────┘   └──────────────────┘
       │                                      │
       ↓                                      ↓
┌──────────────────────────────────────────────────────┐
│              CLOUD STORAGE                            │
│  - Brand name datasets                                │
│  - Trademark data extracts                            │
│  - Generated brand packages (exports)                 │
│  - Logs and analytics                                 │
└───────────────────────────────────────────────────────┘
       │
       ↓
┌──────────────────────────────────────────────────────┐
│         CLOUD LOGGING & MONITORING                    │
│  - Agent traces                                       │
│  - Performance metrics                                │
│  - Error tracking                                     │
│  - Usage analytics                                    │
└───────────────────────────────────────────────────────┘
```

### 7.3 Database Schema (Cloud SQL)

#### Sessions Table
```sql
CREATE TABLE sessions (
    session_id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    application_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    metadata JSONB
);

CREATE INDEX idx_sessions_user_id ON sessions(user_id);
CREATE INDEX idx_sessions_created_at ON sessions(created_at);
```

#### Events Table
```sql
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    session_id VARCHAR(255) REFERENCES sessions(session_id),
    author VARCHAR(50) NOT NULL, -- 'user' or 'agent'
    content TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    event_type VARCHAR(50), -- 'message', 'tool_call', 'compaction'
    metadata JSONB
);

CREATE INDEX idx_events_session_id ON events(session_id);
CREATE INDEX idx_events_timestamp ON events(timestamp);
```

#### Generated Brands Table (for analytics)
```sql
CREATE TABLE generated_brands (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(255) REFERENCES sessions(session_id),
    brand_name VARCHAR(255) NOT NULL,
    tagline TEXT,
    story TEXT,
    domain_status JSONB, -- {".com": "available", ".ai": "taken"}
    trademark_risk VARCHAR(20), -- 'low', 'medium', 'high'
    seo_score FLOAT,
    user_selected BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB
);

CREATE INDEX idx_brands_session_id ON generated_brands(session_id);
CREATE INDEX idx_brands_selected ON generated_brands(user_selected);
```

### 7.4 Environment Configuration

**.env (Local Development)**
```bash
# Google Cloud
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# Vertex AI
GOOGLE_GENAI_USE_VERTEXAI=1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/brandstudio
# Or for Cloud SQL:
# DATABASE_URL=postgresql://user:password@/brandstudio?host=/cloudsql/PROJECT:REGION:INSTANCE

# Vector Search
VECTOR_SEARCH_INDEX_ENDPOINT=projects/PROJECT_ID/locations/REGION/indexEndpoints/ENDPOINT_ID
VECTOR_SEARCH_DEPLOYED_INDEX_ID=brand_names_deployed

# Memory Bank (optional)
MEMORY_BANK_COLLECTION_ID=brand_studio_memories

# External APIs (for validation tools)
NAMECHEAP_API_KEY=your-namecheap-key  # For domain checking
USPTO_API_KEY=your-uspto-key  # If using premium API

# Observability
LOG_LEVEL=INFO
ENABLE_TRACING=true
```

**.agent_engine_config.json (Production Deployment)**
```json
{
    "min_instances": 0,
    "max_instances": 5,
    "resource_limits": {
        "cpu": "2",
        "memory": "4Gi"
    },
    "timeout": "600s",
    "environment_variables": {
        "GOOGLE_GENAI_USE_VERTEXAI": "1",
        "LOG_LEVEL": "INFO"
    }
}
```

### 7.5 Deployment Commands

#### Setup Google Cloud Project
```bash
# Set project
export GOOGLE_CLOUD_PROJECT=your-project-id
gcloud config set project $GOOGLE_CLOUD_PROJECT

# Enable required APIs
gcloud services enable \
  aiplatform.googleapis.com \
  storage.googleapis.com \
  sql-component.googleapis.com \
  sqladmin.googleapis.com \
  logging.googleapis.com \
  monitoring.googleapis.com \
  cloudtrace.googleapis.com \
  secretmanager.googleapis.com

# Authenticate
gcloud auth login
gcloud auth application-default login
```

#### Create Cloud SQL Instance
```bash
# Create PostgreSQL instance
gcloud sql instances create brandstudio-db \
  --database-version=POSTGRES_15 \
  --tier=db-f1-micro \
  --region=us-central1

# Create database
gcloud sql databases create brandstudio \
  --instance=brandstudio-db

# Create user
gcloud sql users create brandstudio-user \
  --instance=brandstudio-db \
  --password=SECURE_PASSWORD
```

#### Setup Vector Search
```bash
# Upload brand name dataset to Cloud Storage
gsutil mb gs://$GOOGLE_CLOUD_PROJECT-brand-names
gsutil cp brand_names_embeddings.json gs://$GOOGLE_CLOUD_PROJECT-brand-names/

# Create Vector Search index (done via Python SDK - see section 5.4)
```

#### Deploy to Agent Engine
```bash
# From project root
adk deploy agent_engine \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=us-central1 \
  brand_studio_agent \
  --agent_engine_config_file=.agent_engine_config.json

# Get deployment URL
gcloud ai agents list \
  --region=us-central1 \
  --project=$GOOGLE_CLOUD_PROJECT
```

### 7.6 Cost Estimation (Google Cloud Free Tier + Expected Usage)

**Free Tier Limits:**
- Vertex AI Agent Engine: 10 agents free
- Cloud SQL: f1-micro instance free in us-central1, us-east1, us-west1
- Cloud Storage: 5 GB free
- Cloud Logging: 50 GB free per month
- Gemini API: Pay-as-you-go (no free tier, but low cost)

**Estimated Monthly Costs (100 brand generations/month):**
| Service | Usage | Cost |
|---------|-------|------|
| Gemini 2.5 Flash | ~500K tokens | ~$1.25 |
| Gemini 2.5 Pro | ~100K tokens | ~$2.50 |
| Vector Search | 1M queries | $0.00 (under free tier) |
| Cloud SQL | f1-micro | $0.00 (free tier) |
| Cloud Storage | 2 GB | $0.00 (free tier) |
| Cloud Logging | 10 GB | $0.00 (free tier) |
| **Total** | | **~$4-5/month** |

**Note:** Costs scale linearly with usage. Production workloads would require upgrading instance sizes.

---

## 8. Implementation Roadmap

### Week 1: Foundation (Nov 18-24)
**Goals:** Setup infrastructure, basic agent structure

**Tasks:**
- [ ] Create new GitHub repository
- [ ] Setup Google Cloud project and enable APIs
- [ ] Configure Cloud SQL database
- [ ] Implement Orchestrator Agent (basic)
- [ ] Implement Name Generator Agent (basic, no RAG yet)
- [ ] Create domain availability checker tool
- [ ] Basic CLI interface for testing
- [ ] Write unit tests for tools

**Deliverables:**
- Working multi-agent skeleton
- Domain checking functionality
- Basic name generation (10-20 names)

### Week 2: Core Features (Nov 25 - Dec 1... actually Nov 25-28 to leave buffer)
**Goals:** RAG, validation, complete workflow

**Tasks:**
- [ ] Curate brand name dataset (5,000+ names)
- [ ] Generate embeddings using Vertex AI
- [ ] Setup Vertex AI Vector Search index
- [ ] Implement RAG retrieval in Name Generator
- [ ] Build Validation Agent with trademark checking
- [ ] Implement Research Agent
- [ ] Create sequential workflow (research → generate → validate)
- [ ] Add session management (DatabaseSessionService)
- [ ] Implement context compaction

**Deliverables:**
- RAG-enhanced name generation
- Trademark validation working
- End-to-end workflow functional

### Week 3: Content Generation & Polish (Nov 29 - Dec 1)
**Goals:** SEO, story generation, user experience

**Tasks:**
- [ ] Implement SEO Optimizer Agent
- [ ] Build Story Generator Agent
- [ ] Create approval workflow (long-running operation)
- [ ] Add Memory Bank for user preferences
- [ ] Build evaluation test suite (10+ test cases)
- [ ] Run evaluations and fix issues
- [ ] Add observability (LoggingPlugin)
- [ ] Improve prompt engineering for all agents
- [ ] Create comprehensive README.md

**Deliverables:**
- Complete brand package generation
- Evaluation passing 80%+ test cases
- Documentation complete

### Week 4: Deployment & Submission (Nov 29-30 - buffer for issues)
**Goals:** Deploy, create video, submit

**Tasks:**
- [ ] Deploy to Vertex AI Agent Engine
- [ ] Test deployed agent thoroughly
- [ ] Create demo video (under 3 minutes)
- [ ] Write project writeup (<1500 words)
- [ ] Prepare submission materials
- [ ] Submit to Kaggle competition

**Deliverables:**
- Live deployed agent
- YouTube video published
- Kaggle submission complete

---

## 9. Agent Evaluation Plan

### 9.1 Test Cases

#### Test Case 1: Healthcare AI App
```json
{
  "eval_id": "healthcare_ai_mental_wellness",
  "conversation": [
    {
      "user_content": {
        "parts": [{
          "text": "I'm building an AI-powered mental wellness app for Gen Z users aged 18-25. The app uses conversational AI to provide daily check-ins and mood tracking. Brand personality should be warm, approachable, and non-clinical."
        }]
      },
      "expected_output": {
        "num_names": {"min": 15, "max": 50},
        "domain_available_com": {"min": 5},
        "trademark_risk_low": {"min": 3},
        "seo_score_avg": {"min": 70},
        "has_taglines": true,
        "has_brand_story": true
      }
    }
  ]
}
```

#### Test Case 2: Fintech Startup
```json
{
  "eval_id": "fintech_expense_tracking",
  "conversation": [
    {
      "user_content": {
        "parts": [{
          "text": "Building a fintech app that helps freelancers track expenses and automate tax filing. Target audience is creative professionals (designers, writers, photographers). Brand should feel professional but not stuffy."
        }]
      },
      "expected_output": {
        "num_names": {"min": 15},
        "domain_available_com": {"min": 5},
        "trademark_risk_low": {"min": 3},
        "names_contain_finance_keywords": true
      }
    }
  ]
}
```

#### Test Case 3: E-commerce SaaS
```json
{
  "eval_id": "ecommerce_inventory_management",
  "conversation": [
    {
      "user_content": {
        "parts": [{
          "text": "Enterprise SaaS platform for e-commerce inventory management across multiple warehouses. Target: operations managers at mid-size retailers. Professional, trustworthy tone."
        }]
      },
      "expected_output": {
        "num_names": {"min": 15},
        "trademark_risk_low": {"min": 5},
        "names_pronounceable": true
      }
    }
  ]
}
```

### 9.2 Evaluation Criteria

**Custom Evaluation Metrics:**

1. **Name Quality Score** (0-100)
   - Pronounceability (30%)
   - Memorability (30%)
   - Industry relevance (20%)
   - Uniqueness (20%)

2. **Validation Accuracy** (Pass/Fail)
   - Domain availability check accuracy: >95%
   - Trademark risk assessment: verified against actual USPTO data
   - No false positives (flagging available names as taken)

3. **Content Quality Score** (0-100)
   - Tagline relevance and catchiness (human evaluation)
   - Brand story coherence and tone match (human evaluation)
   - SEO optimization (automated: keyword presence, length)

4. **Performance Metrics**
   - Time to generate complete brand package: <2 minutes
   - Success rate: >90% (no errors/failures)

### 9.3 Evaluation Commands

```bash
# Run all evaluation test cases
adk eval brand_studio_agent tests/integration.evalset.json \
  --config_file_path=tests/eval_config.json \
  --print_detailed_results

# Run specific test case
adk eval brand_studio_agent tests/healthcare.evalset.json

# Generate evaluation report
python scripts/generate_eval_report.py \
  --results_file=eval_results.json \
  --output_file=evaluation_report.md
```

---

## 10. Demo Scenarios

### Scenario 1: Meal Planning App (Concierge Track Use Case)

**User Input:**
```
Product: AI-powered meal planning app for busy millennial parents
Target Audience: Parents aged 28-40 with young children
Brand Personality: Warm, helpful, family-oriented
Key Features: Quick recipes, nutrition tracking, grocery lists
```

**Expected Output:**
```
=== AI BRAND STUDIO - RESULTS ===

TOP 5 BRAND NAMES:

1. ⭐ NutriNest
   Domain: nutrinest.com ✅ Available
   Alternatives: nutrinest.ai ✅ | nutrinest.io ✅
   Trademark: ⚠️  1 similar mark in EU (food services)
   Risk Level: MEDIUM
   SEO Score: 89/100

   Tagline: "Nourishing your family, naturally"

2. ⭐ MealMuse
   Domain: mealmuse.com ✅ Available
   Trademark: ✅ Clear (no conflicts)
   Risk Level: LOW
   SEO Score: 92/100

   Tagline: "Inspire every family meal"

[... 3 more names ...]

=== SELECTED: MealMuse ===

📖 BRAND STORY:
MealMuse was born from a simple truth: every parent deserves to feel
confident in the kitchen, even on the busiest days. We're not just another
meal planning app—we're your creative companion in the kitchen, turning
the daily question of "what's for dinner?" into an opportunity for
nourishing, joyful family moments.

Our AI understands your family's unique needs, preferences, and schedule,
offering personalized recipe suggestions that actually work for your life.
Whether you have 15 minutes or an hour, picky eaters or adventurous
foodies, MealMuse adapts to you...

🎯 TAGLINE OPTIONS:
1. "Inspire every family meal"
2. "Where creativity meets convenience"
3. "Your mealtime muse awaits"
4. "Family meals, made meaningful"
5. "Cook with confidence, every time"

💼 LANDING PAGE HERO COPY:
"Turn meal planning from stressful to inspired. MealMuse's AI creates
personalized, kid-approved recipes that fit your schedule, dietary needs,
and family preferences. Spend less time planning, more time enjoying meals
together."

📊 SEO METADATA:
Title: "MealMuse - AI Meal Planning App for Busy Parents | Quick Healthy Recipes"
Meta Description: "Transform family meal planning with MealMuse's AI-powered
app. Get personalized, kid-friendly recipes and automated grocery lists in
minutes. Try free for 14 days."
```

### Scenario 2: Enterprise Use Case

**User Input:**
```
Product: Sales lead qualification and scoring platform using AI
Target Audience: B2B sales teams at mid-market companies (100-1000 employees)
Brand Personality: Professional, data-driven, results-oriented
Key Features: Automated lead enrichment, predictive scoring, CRM integration
```

**Expected Output:**
```
TOP 5 BRAND NAMES:

1. ⭐ Leadcraft
   Domain: leadcraft.ai ✅ Available (.com taken)
   Trademark: ✅ Clear
   SEO Score: 88/100
   Tagline: "Craft your pipeline with precision"

2. ⭐ QualifyIQ
   Domain: qualifyiq.com ✅ Available
   Trademark: ⚠️  2 similar marks (different industries)
   SEO Score: 91/100
   Tagline: "Intelligent qualification, proven results"

[Additional examples...]
```

---

## 11. Success Metrics

### User-Facing Metrics
- **Time Savings:** Reduce brand naming from 20+ hours to <10 minutes (>95% reduction)
- **Legal Safety:** 0 trademark conflicts in final selected names (100% safe)
- **Domain Availability:** >80% of top suggestions have .com available
- **User Satisfaction:** >4.5/5 stars on name quality (user survey)

### Technical Metrics
- **Generation Speed:** Complete brand package in <2 minutes
- **Uptime:** >99.5% availability (if deployed)
- **Error Rate:** <1% failed generations
- **RAG Relevance:** >85% of retrieved examples rated as relevant

### Capstone Evaluation Alignment
- **Pitch Score Target:** 25+/30 points
  - Strong problem articulation
  - Clear value proposition
  - Well-written submission

- **Implementation Score Target:** 65+/70 points
  - Demonstrates 7+ key concepts (exceeds 3 requirement)
  - Clean, well-documented code
  - Comprehensive README

- **Bonus Points Target:** 20/20 points
  - ✅ Gemini model usage (5 pts)
  - ✅ Agent Engine deployment (5 pts)
  - ✅ YouTube video (10 pts)

**Total Target Score:** 100+/100 points

---

## 12. Risk Mitigation

### Technical Risks

**Risk 1: RAG Dataset Quality**
- **Impact:** Poor name suggestions if dataset is low quality
- **Mitigation:**
  - Curate initial dataset manually (top 1000 brands)
  - Validate embeddings with sample queries
  - Implement feedback loop to improve over time

**Risk 2: Trademark API Limitations**
- **Impact:** Inaccurate conflict detection
- **Mitigation:**
  - Use multiple data sources (USPTO + web scraping)
  - Add disclaimer: "Always verify with legal counsel"
  - Provide links to official trademark search

**Risk 3: Domain Checking Rate Limits**
- **Impact:** Can't check all domains in real-time
- **Mitigation:**
  - Cache results for 5 minutes
  - Batch domain checks
  - Use multiple domain APIs (Namecheap, GoDaddy)

**Risk 4: Deployment Costs**
- **Impact:** Exceeding Google Cloud free tier
- **Mitigation:**
  - Start with min_instances=0 (scale to zero)
  - Monitor usage via Cloud Console
  - Set up billing alerts at $10, $20, $50

### Timeline Risks

**Risk 5: Scope Creep**
- **Impact:** Missing deadline
- **Mitigation:**
  - MVP first: focus on name generation + domain checking
  - Add features incrementally
  - Cut optional features if needed (social handle check, etc.)

**Risk 6: RAG Implementation Complexity**
- **Impact:** Delays in Week 2
- **Mitigation:**
  - Start with simple keyword search as fallback
  - Use pre-built Vertex AI Vector Search (managed service)
  - Allocate buffer time in Week 3

---

## 13. Optional Enhancements (Post-Submission)

If time permits or for future iterations:

1. **Social Media Handle Checker**
   - Check Twitter, Instagram, LinkedIn availability
   - Suggest alternatives if taken

2. **Logo Generation**
   - Integrate with Imagen or DALL-E
   - Generate logo concepts for selected name

3. **A2A Protocol Integration**
   - Expose Brand Studio as A2A service
   - Allow other agents to request brand naming

4. **User Collaboration**
   - Multi-user sessions
   - Team voting on name preferences
   - Comments and feedback

5. **Advanced Analytics**
   - Track which industries get best names
   - A/B test different RAG strategies
   - User engagement metrics

6. **Export Formats**
   - PDF brand guideline document
   - PowerPoint presentation
   - Figma brand kit

---

## 14. Resources & References

### Course Materials
- Day 1: Multi-agent workflows (Sequential, Parallel, Loop)
- Day 2: Custom tools, Agent delegation, MCP
- Day 3: Sessions, Memory Bank, Context compaction
- Day 4: Observability, Logging, Evaluation
- Day 5: A2A protocol, Agent Engine deployment

### Documentation
- [ADK Documentation](https://google.github.io/adk-docs/)
- [Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- [Vertex AI Vector Search](https://cloud.google.com/vertex-ai/docs/vector-search/overview)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [Cloud SQL PostgreSQL](https://cloud.google.com/sql/docs/postgres)

### APIs & Tools
- [USPTO TESS](https://tess2.uspto.gov/) - Trademark search
- [Namecheap API](https://www.namecheap.com/support/api/intro/) - Domain checking
- [python-whois](https://pypi.org/project/python-whois/) - Domain WHOIS lookup
- [Product Hunt API](https://api.producthunt.com/v2/docs) - Startup name data

### Inspiration
- [Namelix](https://namelix.com/) - AI name generator
- [Squadhelp](https://www.squadhelp.com/) - Brand naming platform
- [BrandBucket](https://www.brandbucket.com/) - Curated brand names

---

## 15. Team & Roles (If Applicable)

**For Team Submissions:**

Suggested role distribution for a 2-4 person team:

**Role 1: Agent Architect**
- Design multi-agent workflow
- Implement orchestrator and core agents
- Prompt engineering

**Role 2: Data Engineer**
- RAG implementation
- Vector database setup
- Dataset curation and embeddings

**Role 3: Tools Developer**
- Custom tool implementation (domain, trademark, SEO)
- API integrations
- Error handling

**Role 4: DevOps & Documentation**
- Google Cloud setup and deployment
- CI/CD pipeline
- README, documentation, video

**For Solo Submission:**
- Follow weekly roadmap
- Focus on MVP features first
- Use pre-built tools where possible

---

## 16. Submission Checklist

### Code & Repository
- [ ] GitHub repository created and public
- [ ] README.md with setup instructions
- [ ] Code well-commented
- [ ] requirements.txt complete
- [ ] .env.example provided (no secrets!)
- [ ] Agent evaluation tests included

### Documentation
- [ ] Problem statement clearly articulated
- [ ] Solution architecture diagram
- [ ] API integration documentation
- [ ] Deployment instructions (if deployed)
- [ ] Demo screenshots/examples

### Capstone Submission
- [ ] Title and subtitle
- [ ] Card/thumbnail image
- [ ] Track selected: Enterprise Agents
- [ ] YouTube video URL (if created)
- [ ] Project description (<1500 words)
- [ ] GitHub repository link
- [ ] Submission before Dec 1, 11:59 AM PT

### Bonus Items
- [ ] Deployed to Vertex AI Agent Engine
- [ ] YouTube video published (under 3 min)
- [ ] Using Gemini models
- [ ] Evidence of deployment in writeup/code

---

## 17. Contact & Support

**Kaggle Discord:** [Join for team formation and Q&A]
**Course Resources:** [Link to Kaggle course notebooks]
**Google Cloud Support:** [Cloud Console support chat]

**Project Repository:** [To be created]
**Team Members:** [To be determined]

---

## Conclusion

AI Brand Studio is a comprehensive multi-agent system that demonstrates advanced ADK concepts while solving a real business problem. By combining RAG, multi-agent workflows, custom tools, and Google Cloud infrastructure, this project showcases the full potential of AI agents in enterprise workflows.

The project is scoped to be completed within the 2-week timeline while leaving room for optional enhancements. With clear success metrics and evaluation criteria, it aligns perfectly with the Capstone requirements and has strong potential for top 3 placement in the Enterprise Agents track.

**Next Steps:**
1. Create GitHub repository
2. Setup Google Cloud project
3. Begin Week 1 implementation
4. Iterate based on evaluation results
5. Deploy and submit before deadline

Good luck! 🚀
