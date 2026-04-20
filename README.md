# StoryForge AI

> Forge compelling novels with intelligent AI storytelling.

**StoryForge AI** is a powerful, open-source platform for generating full-length novels using large language models. Built with a multi-stage writing pipeline, it produces coherent narratives with strong character consistency, rich world-building, and smooth chapter flow.

**Author:** [Muhammad Babar](https://babar.site.je) · [GitHub](https://github.com/muhammadbabar254) · [LinkedIn](https://www.linkedin.com/in/muhammad-babardev)

---

## Features

### Core Generation
- **Multi-stage chapter writing** — Plot → character development → dialogue → final polish
- **Scene-by-scene pipeline** — Breaks chapters into scenes for richer, more detailed prose
- **Outline revision loop** — AI critique and revision for stronger story structure
- **Multi-provider support** — Ollama (local), Google Gemini, and OpenRouter

### StoryForge Exclusive
- **Character Builder** — Structured profiles with arcs, relationships, and voice notes
- **World Builder** — Locations, cultures, rules, and atmosphere for consistent settings
- **Story Timeline** — Automatic tracking of events and plot threads across chapters
- **PDF & EPUB Export** — Publish-ready output formats
- **Story History** — Searchable index of all generated stories
- **Web Dashboard** — Modern Streamlit UI for visual story management

### Additional
- Translation support for prompts and finished stories
- Flexible model configuration per pipeline stage
- Automatic model downloading via Ollama
- Cross-platform (Windows, macOS, Linux)

---

## Quick Start

### 1. Install dependencies

```sh
pip install -r requirements.txt
```

### 2. Install Ollama (for local models)

Download from [ollama.com](https://ollama.com/) and pull a model:

```sh
ollama pull llama3:70b
```

### 3. Configure API keys (optional)

```sh
cp .env.example .env
```

Add your keys for Google Gemini or OpenRouter if not using local models.

### 4. Generate a story

```sh
python forge.py -Prompt ExamplePrompts/Example1/Prompt.txt
```

With StoryForge features enabled:

```sh
python forge.py -Prompt ExamplePrompts/Example1/Prompt.txt -CharacterBuilder -WorldBuilder -ExportPDF -ExportEPUB
```

### 5. Launch the web dashboard

```sh
streamlit run storyforge/ui/app.py
```

---

## CLI Reference

| Flag | Description |
|------|-------------|
| `-Prompt` | Path to your story prompt file |
| `-Output` | Custom output path (without extension) |
| `-CharacterBuilder` | Generate character profiles before writing |
| `-WorldBuilder` | Generate world profile before writing |
| `-BuildTimeline` | Generate narrative timeline (default: on) |
| `-ExportPDF` | Export finished story as PDF |
| `-ExportEPUB` | Export finished story as EPUB |
| `-Translate` | Translate story to specified language |
| `-ExpandOutline` | Expand outline chapter-by-chapter |
| `-Debug` | Print system prompts during generation |

Model format: `{provider}://{model}@{host}?param=value`

Supported providers: `ollama`, `google`, `openrouter`

Example with mixed models:

```sh
python forge.py -Prompt ExamplePrompts/Example1/Prompt.txt \
  -InitialOutlineModel "google://gemini-1.5-pro" \
  -ChapterS1Model "ollama://llama3:70b@127.0.0.1:11434"
```

See `python forge.py --help` for all options.

---

## Project Structure

```
StoryForge-AI/
├── forge.py                  # Primary CLI entry point
├── Write.py                  # Legacy CLI (deprecated)
├── storyforge/               # Main package
│   ├── pipeline.py           # Generation orchestrator
│   ├── cli.py                # Argument parser
│   ├── branding.py           # Branding & display
│   ├── builders/             # Character, World, Timeline
│   ├── export/               # PDF & EPUB export
│   ├── history/              # Story history index
│   └── ui/                   # Streamlit web dashboard
├── Writer/                   # Core generation engine
│   ├── Config.py             # Default model configuration
│   ├── Prompts.py            # AI prompt templates
│   ├── Chapter/              # Chapter generation pipeline
│   ├── Scene/                # Scene-by-scene generation
│   ├── Outline/              # Story element extraction
│   └── Interface/            # LLM provider adapters
├── ExamplePrompts/           # Sample story prompts
├── Stories/                  # Generated story output
└── Docs/                     # Architecture documentation
```

---

## Hardware Recommendations

See [Docs/Models.md](Docs/Models.md) for model suggestions based on your GPU capabilities.

| GPU VRAM | Recommended Models |
|----------|-------------------|
| 8 GB | gemma2:9b, mistral:7b |
| 16 GB | llama3:8b, gemma2:27b |
| 24 GB+ | llama3:70b, qwen2:72b |
| Cloud | google://gemini-1.5-pro |

---

## Architecture

![Block Diagram](Docs/BlockDiagram.drawio.svg)

The pipeline follows these stages:

1. **Builders** — Character & World profiles (optional)
2. **Outline** — Story elements → initial outline → revision loop
3. **Expansion** — Per-chapter detailed outlines with scenes
4. **Writing** — Multi-stage chapter generation with continuity checks
5. **Post-processing** — Scrubbing, translation, timeline, export

---

## Legacy Compatibility

`Write.py` still works but is deprecated. All new development uses `forge.py` and the `storyforge` package.

```sh
# Old (still works)
python Write.py -Prompt ExamplePrompts/Example1/Prompt.txt

# New (recommended)
python forge.py -Prompt ExamplePrompts/Example1/Prompt.txt
```

---

## Contributing

Contributions are welcome! Please open issues or pull requests on [GitHub](https://github.com/muhammadbabar254).

---

## License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

This project is a fork and substantial modification of [AIStoryWriter](https://github.com/datacrystals/AIStoryWriter) by datacrystals. See [NOTICES.md](NOTICES.md) for attribution details.

If you modify this code and use it to provide a service over a network, you must make your modified source code available to users of that service, per AGPL-3.0 requirements.

Full license text: [LICENSE](LICENSE) · [gnu.org/licenses/agpl-3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)

---

Built with ⚔ by [Muhammad Babar](https://babar.site.je)

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Installation

```bash
npm install
# or
pip install -r requirements.txt
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## License

This project is licensed under the [MIT License](LICENSE).

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.

## Usage

```bash
# Basic usage
python main.py --help

# Run with config
python main.py --config config.yaml
```

## Changelog

### Unreleased
- Improved performance
- Fixed edge case in validation
- Updated dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

> **Note:** This feature is still in development. Please report any bugs via GitHub Issues.
