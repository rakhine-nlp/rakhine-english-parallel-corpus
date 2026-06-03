# 🌐 Rakhine–English Parallel Corpus

A parallel corpus for **Rakhine ↔ English machine translation** and Natural Language Processing (NLP) research.

---

## 🎯 Purpose

This dataset is designed for:

- Machine Translation (Rakhine ↔ English)
- Language Modeling
- NLP research on low-resource languages
- Dialect and linguistic analysis
- Language preservation and documentation

---

## 📌 Overview

Rakhine is a major regional variety of Burmese spoken in Rakhine State, Myanmar. Despite its linguistic significance, publicly available digital resources for Rakhine remain extremely limited.

This project aims to address that gap by building an open, structured parallel corpus to support research and language technology development.

The dataset is intended to support:

- 📚 Parallel sentence alignment (Rakhine–English)
- 🧠 Training data for neural machine translation (NMT)
- 🌍 Open NLP resources for low-resource language research
- 🔊 Future expansion into speech + multimodal datasets

---

## 📁 Dataset Structure

rakhine-english-parallel-corpus/
│
├── data/
│   ├── train.csv
│   ├── dev.csv
│   └── test.csv
│
├── raw_data/
│   ├── rakhine_text.txt
│   └── english_text.txt
│
├── scripts/
│   ├── align_sentences.py
│   └── clean_data.py
│
├── README.md
├── LICENSE
└── .gitignore

---

## 📊 Data Format

### Parallel Sentence Format (CSV)

| rakhine | english |
|--------|--------|
| ငါ စားပြီးဗျာယ် | I have eaten. |
| နင် ဇာမှာလဲ | Where are you? |

### CSV Schema

rakhine: string (source language sentence)
english: string (target language sentence)

---

## ⚙️ Dataset Creation Pipeline

### 1. Prepare Raw Data

Place monolingual text files in `raw_data/`:

- rakhine_text.txt
- english_text.txt

Each line should ideally represent one sentence.

---

### 2. Sentence Alignment

```bash
python scripts/align_sentences.py
```

This generates initial parallel sentence pairs using rule-based alignment.

---

### 3. Output Dataset

data/
├── train.csv
├── dev.csv
└── test.csv

---

## 🧠 Use Cases

- Neural Machine Translation (NMT)
- Chatbot systems
- Low-resource language research
- Linguistic and dialect studies
- Language preservation
- NLP benchmarking

---

## 🚀 Planned Improvements

- Expand to 10,000+ sentence pairs
- Improve alignment using semantic models
- Add human verification
- Publish on Hugging Face Hub
- Add evaluation benchmarks
- Extend to speech datasets

---

## ⚠️ Limitations

- Rule-based initial alignment (line-by-line)
- Requires human review for quality
- Limited coverage at early stage

---

## 📜 License

Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## 🤝 Contributions

- Add sentence pairs
- Improve translations
- Fix alignment issues
- Expand dialect coverage
- Improve preprocessing scripts
- Report dataset issues

---

## 🌍 Goal

To support the preservation and technological development of the Rakhine language through open NLP resources.

---

## 📬 Contact

Open to collaboration with researchers, linguists, and developers in low-resource NLP.
