{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyNPywrzfxpu0c0325Q1KOM+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Khalid514-ali/clone/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "yv8oiiTkQsCj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "with open('app.py','w') as f:\n",
        "  f.write(\"\"\"import streamlit as st\n",
        "from PyPDF2 import PdfReader\n",
        "import torch\n",
        "import soundfile as sf\n",
        "import os\n",
        "from TTS.api import TTS\n",
        "\n",
        "st.set_page_config(page_title=\"PDF to Audiobook\", layout=\"centered\")\n",
        "\n",
        "st.title(\"PDF → Audiobook (Voice Cloning)\")\n",
        "st.write(\"Upload a PDF and a voice sample to create an audiobook in the same voice\")\n",
        "\n",
        "# Create temp folder\n",
        "os.makedirs(\"temp\", exist_ok=True)\n",
        "\n",
        "# Upload PDF\n",
        "pdf_file = st.file_uploader(\"Upload PDF\", type=[\"pdf\"])\n",
        "\n",
        "# Upload voice sample\n",
        "voice_file = st.file_uploader(\"Upload Voice Sample (5–15 sec)\", type=[\"wav\", \"mp3\"])\n",
        "\n",
        "if pdf_file and voice_file:\n",
        "    # Save voice sample\n",
        "    sample_path = \"temp/sample.wav\"\n",
        "    with open(sample_path, \"wb\") as f:\n",
        "        f.write(voice_file.read())\n",
        "\n",
        "    # Extract text from PDF\n",
        "    reader = PdfReader(pdf_file)\n",
        "    text = \"\"\n",
        "    for page in reader.pages:\n",
        "        text += page.extract_text() + \"\\n\"\n",
        "\n",
        "    st.subheader(\"Extracted Text Preview\")\n",
        "    st.text_area(\"PDF Text\", text[:2000], height=200)\n",
        "\n",
        "    if st.button(\"Generate Audiobook\"):\n",
        "        with st.spinner(\"Generating audiobook... this may take time ⏳\"):\n",
        "            device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n",
        "\n",
        "            tts = TTS(\n",
        "                model_name=\"tts_models/multilingual/multi-dataset/xtts_v2\",\n",
        "                progress_bar=False\n",
        "            ).to(device)\n",
        "\n",
        "            output_path = \"temp/audiobook.wav\"\n",
        "\n",
        "            tts.tts_to_file(\n",
        "                text=text,\n",
        "                speaker_wav=sample_path,\n",
        "                language=\"en\",\n",
        "                file_path=output_path\n",
        "            )\n",
        "\n",
        "        st.success(\"Audiobook generated!\")\n",
        "\n",
        "        # Audio player\n",
        "        audio_bytes = open(output_path, \"rb\").read()\n",
        "        st.audio(audio_bytes, format=\"audio/wav\")\n",
        "\n",
        "        # Download button\n",
        "        st.download_button(\n",
        "            label=\" Download Audiobook\",\n",
        "            data=audio_bytes,\n",
        "            file_name=\"audiobook.wav\",\n",
        "            mime=\"audio/wav\"\n",
        "        ))\"\"\")"
      ],
      "metadata": {
        "id": "KTyzG9vdeC49"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "with open(\"requirements.txt\",'w') as f:\n",
        "  f.write(\"Streamlit\\nPyPDF2\\ntorch\\nsoundfile\\ncoqui-tts\\n\")"
      ],
      "metadata": {
        "id": "wCc9XhkafBB1"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}