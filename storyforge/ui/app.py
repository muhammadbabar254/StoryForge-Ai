"""
StoryForge AI — Web Dashboard

Launch with: streamlit run storyforge/ui/app.py
"""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[2]

st.set_page_config(
    page_title="StoryForge AI",
    page_icon="⚔",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 2.4rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-header { color: #94a3b8; font-size: 1rem; margin-bottom: 2rem; }
    .feature-card {
        background: linear-gradient(145deg, #1e1b4b 0%, #312e81 100%);
        border: 1px solid #4338ca33;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 0.8rem;
    }
    .feature-card h4 { color: #c4b5fd; margin: 0 0 0.4rem 0; }
    .feature-card p { color: #a5b4fc; font-size: 0.85rem; margin: 0; }
    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.6rem 2rem;
    }
    div[data-testid="stSidebar"] { background: #0f172a; }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.markdown('<p class="main-header">⚔ StoryForge AI</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">Forge compelling novels with intelligent AI storytelling · '
    '<a href="https://babar.site.je" target="_blank">babar.site.je</a></p>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### Navigation")
    page = st.radio(
        "Go to",
        ["Generate Story", "Story History", "Character Builder", "World Builder", "About"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("**Author:** Muhammad Babar")
    st.markdown("[GitHub](https://github.com/muhammadbabar254)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/muhammad-babardev)")

if page == "Generate Story":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Story Prompt")
        prompt_text = st.text_area(
            "Describe your story",
            height=200,
            placeholder="Write a sci-fi thriller about a detective on Mars investigating...",
        )
        prompt_file = st.file_uploader("Or upload a prompt file", type=["txt", "md"])

    with col2:
        st.markdown("### StoryForge Features")
        char_builder = st.toggle("Character Builder", value=True)
        world_builder = st.toggle("World Builder", value=True)
        build_timeline = st.toggle("Story Timeline", value=True)
        export_pdf = st.toggle("Export PDF", value=False)
        export_epub = st.toggle("Export EPUB", value=False)

        st.markdown("### Model")
        model = st.selectbox(
            "Primary model",
            ["ollama://llama3:70b", "google://gemini-1.5-flash", "google://gemini-1.5-pro"],
        )

    st.markdown("---")
    if st.button("⚔ Forge Story", type="primary", use_container_width=True):
        if not prompt_text and not prompt_file:
            st.error("Please enter a prompt or upload a file.")
        else:
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".txt", delete=False, encoding="utf-8"
            ) as tmp:
                if prompt_file:
                    tmp.write(prompt_file.read().decode("utf-8"))
                else:
                    tmp.write(prompt_text)
                tmp_path = tmp.name

            cmd = [
                sys.executable,
                str(ROOT / "forge.py"),
                "-Prompt",
                tmp_path,
                "-InitialOutlineModel",
                model,
                "-ChapterOutlineModel",
                model,
                "-ChapterS1Model",
                model,
                "-ChapterS2Model",
                model,
                "-ChapterS3Model",
                model,
                "-ChapterS4Model",
                model,
                "-NoBanner",
            ]
            if char_builder:
                cmd.append("-CharacterBuilder")
            if world_builder:
                cmd.append("-WorldBuilder")
            if not build_timeline:
                cmd.append("-NoTimeline")
            if export_pdf:
                cmd.append("-ExportPDF")
            if export_epub:
                cmd.append("-ExportEPUB")

            with st.spinner("Forging your story... This may take a while."):
                result = subprocess.run(
                    cmd, capture_output=True, text=True, cwd=str(ROOT)
                )

            os.unlink(tmp_path)

            if result.returncode == 0:
                st.success("Story forged successfully!")
                st.code(result.stdout[-3000:] if len(result.stdout) > 3000 else result.stdout)
            else:
                st.error("Generation failed.")
                st.code(result.stderr or result.stdout)

elif page == "Story History":
    st.markdown("### Story History")
    from storyforge.history.store import list_stories, rebuild_index_from_disk

    if st.button("Rebuild index from disk"):
        count = rebuild_index_from_disk()
        st.info(f"Indexed {count} stories.")

    stories = list_stories()
    if not stories:
        st.info("No stories yet. Generate your first story!")
    else:
        for story in stories:
            with st.expander(f"📖 {story.get('title', 'Untitled')} — {story.get('created_at', '')[:10]}"):
                st.write(story.get("summary", ""))
                cols = st.columns(4)
                cols[0].metric("Words", story.get("word_count", 0))
                cols[1].metric("Time", f"{story.get('elapsed_seconds', 0)}s")
                cols[2].write(f"**Tags:** {story.get('tags', '')}")
                if story.get("md_path") and Path(story["md_path"]).exists():
                    cols[3].download_button(
                        "Download MD",
                        Path(story["md_path"]).read_text(encoding="utf-8"),
                        file_name=Path(story["md_path"]).name,
                    )

elif page == "Character Builder":
    st.markdown("### Character Builder")
    st.markdown("Generate detailed character profiles for your story.")

    cb_prompt = st.text_area("Story concept", height=120, key="cb_prompt")
    if st.button("Build Characters"):
        if not cb_prompt:
            st.error("Enter a story concept first.")
        else:
            with st.spinner("Building characters..."):
                import Writer.Config
                import Writer.Interface.Wrapper
                import Writer.PrintUtils
                from storyforge.builders.character import build_characters, format_for_prompt

                logger = Writer.PrintUtils.Logger()
                interface = Writer.Interface.Wrapper.Interface(
                    [Writer.Config.INITIAL_OUTLINE_WRITER_MODEL]
                )
                data = build_characters(interface, logger, cb_prompt)
                st.markdown(format_for_prompt(data))
                st.json(data)

elif page == "World Builder":
    st.markdown("### World Builder")
    st.markdown("Create rich, consistent world settings for your narrative.")

    wb_prompt = st.text_area("Story concept", height=120, key="wb_prompt")
    if st.button("Build World"):
        if not wb_prompt:
            st.error("Enter a story concept first.")
        else:
            with st.spinner("Building world..."):
                import Writer.Config
                import Writer.Interface.Wrapper
                import Writer.PrintUtils
                from storyforge.builders.world import build_world, format_for_prompt

                logger = Writer.PrintUtils.Logger()
                interface = Writer.Interface.Wrapper.Interface(
                    [Writer.Config.INITIAL_OUTLINE_WRITER_MODEL]
                )
                data = build_world(interface, logger, wb_prompt)
                st.markdown(format_for_prompt(data))
                st.json(data)

elif page == "About":
    st.markdown("### About StoryForge AI")
    st.markdown(
        """
StoryForge AI is an open-source platform for generating full-length novels using
large language models. Built on a multi-stage pipeline with character consistency,
world-building, scene-by-scene generation, and export capabilities.

**Features:**
- Multi-stage chapter writing (plot → character → dialogue → polish)
- Character Builder & World Builder for narrative consistency
- Story Timeline tracking across chapters
- PDF & EPUB export
- Story History with searchable index
- Support for Ollama, Google Gemini, and OpenRouter

**Author:** [Muhammad Babar](https://babar.site.je)
- [GitHub](https://github.com/muhammadbabar254)
- [LinkedIn](https://www.linkedin.com/in/muhammad-babardev)

Licensed under [AGPL-3.0](LICENSE). Based on AIStoryWriter by datacrystals.
        """
    )

    cols = st.columns(3)
    with cols[0]:
        st.markdown('<div class="feature-card"><h4>Character Builder</h4><p>Structured profiles with arcs, relationships, and voice notes.</p></div>', unsafe_allow_html=True)
    with cols[1]:
        st.markdown('<div class="feature-card"><h4>World Builder</h4><p>Locations, cultures, rules, and atmosphere for your setting.</p></div>', unsafe_allow_html=True)
    with cols[2]:
        st.markdown('<div class="feature-card"><h4>Story Timeline</h4><p>Track events, plot threads, and chapter flow automatically.</p></div>', unsafe_allow_html=True)
