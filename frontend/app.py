import streamlit as st
import tempfile
from fpdf import FPDF

from assemblyai_transcriber import upload_audio, transcribe_audio
from huggingface_summarizer import generate_summary, simplify_text

# Page config
st.set_page_config(page_title="Transcribe-AI", layout="wide")

# Title & Intro
st.markdown("## 🧠 Transcribe-AI")
st.markdown("Upload your meeting or lecture audio to generate:")
st.markdown("- ✅ Transcriptions\n- ✍️ Summaries\n- 🪄 Simplified Notes")

st.markdown("---")
st.subheader("🔊 Upload Audio")

# File uploader
uploaded_file = st.file_uploader("Upload Audio File", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    st.success(f"Uploaded file: {uploaded_file.name}")

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    with st.spinner("Uploading to AssemblyAI..."):
        audio_url = upload_audio(tmp_file_path)

    with st.spinner("Transcribing..."):
        transcript = transcribe_audio(audio_url)

    st.markdown("---")
    st.subheader("📝 Transcription")
    st.write(transcript)

    st.markdown("---")
    st.subheader("✨ AI Tools")

    # Summary
    if st.button("📝 Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = generate_summary(transcript)
            st.subheader("📄 Summary:")
            st.write(summary)

            # TXT download
            st.download_button(
                label="📄 Download Summary (TXT)",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

            # PDF download
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in summary.split('\n'):
                pdf.multi_cell(0, 10, line)
            pdf_path = "/tmp/summary.pdf"
            pdf.output(pdf_path)

            with open(pdf_path, "rb") as f:
                st.download_button("📄 Download Summary (PDF)", f, "summary.pdf")

    # Simplified Notes
    if st.button("🧠 Simplify Notes"):
        with st.spinner("Simplifying text..."):
            simplified = simplify_text(transcript)
            st.subheader("🪄 Simplified Notes:")
            st.write(simplified)

            # TXT download
            st.download_button(
                label="🪄 Download Simplified Notes (TXT)",
                data=simplified,
                file_name="simplified_notes.txt",
                mime="text/plain"
            )

            # PDF download
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in simplified.split('\n'):
                pdf.multi_cell(0, 10, line)
            pdf_path = "/tmp/simplified_notes.pdf"
            pdf.output(pdf_path)

            with open(pdf_path, "rb") as f:
                st.download_button("🪄 Download Simplified Notes (PDF)", f, "simplified_notes.pdf")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by  Team-7 for Elisa Hackathon ✨")
