import streamlit as st
import tempfile
from fpdf import FPDF
from assemblyai_transcriber import upload_audio, transcribe_audio
from huggingface_summarizer import generate_summary, simplify_text

def apply_custom_style():
    st.markdown("""
        <style>
            div.block-container {
                max-width: 900px;
                padding: 2rem 2rem 2rem 2rem;
                margin: auto;
            }
            h1, h2, h3 {
                margin-top: 1.2em;
                margin-bottom: 0.6em;
            }
            button[kind="primary"] {
                font-size: 16px !important;
                font-weight: 600 !important;
            }
            footer {
                visibility: hidden;
            }
        </style>
    """, unsafe_allow_html=True)


apply_custom_style()

st.markdown("<h1 style='text-align: center;'>🧠 Transcribe-AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Turn any meeting or lecture audio into clear, summarized, and simplified notes.</p>", unsafe_allow_html=True)

st.markdown("### ✨ Features")
st.markdown("""
- ✅ **Transcriptions** powered by AssemblyAI  
- ✍️ **Smart Summaries** with Hugging Face Transformers  
- 🪄 **Simplified Notes** anyone can understand  
- 📥 Download as PDF or TXT  
""")

st.markdown("---")
st.markdown("### 🔊 Upload Audio")

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
    st.markdown("### 📝 View Transcription")
    st.write(transcript)

    st.markdown("---")
    st.markdown("### 🤖 AI Tools")

    if st.button("📝 Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = generate_summary(transcript)
            st.subheader("📄 Summary")
            st.write(summary)

            st.download_button("📄 Download Summary (TXT)", data=summary, file_name="summary.txt", mime="text/plain")

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in summary.split('\n'):
                pdf.multi_cell(0, 10, line)
            summary_pdf_path = "/tmp/summary.pdf"
            pdf.output(summary_pdf_path)

            with open(summary_pdf_path, "rb") as f:
                st.download_button("📄 Download Summary (PDF)", f, "summary.pdf")

    if st.button("Simplify Notes"):
        with st.spinner("Simplifying..."):
            simplified = simplify_text(transcript)
            st.subheader("🪄 Simplified Notes")
            st.write(simplified)

            st.download_button("🪄 Download Simplified Notes (TXT)", data=simplified, file_name="simplified_notes.txt", mime="text/plain")

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in simplified.split('\n'):
                pdf.multi_cell(0, 10, line)
            simplified_pdf_path = "/tmp/simplified_notes.pdf"
            pdf.output(simplified_pdf_path)

            with open(simplified_pdf_path, "rb") as f:
                st.download_button("🪄 Download Simplified Notes (PDF)", f, "simplified_notes.pdf")

st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with ❤️ by <strong>Team-FOMO</strong> for Elisa AI Hackathon (2024) </p>", unsafe_allow_html=True)
