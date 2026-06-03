# 🌐 Rakhine–English Parallel Corpus

A parallel corpus for **Rakhine ↔ English machine translation**, low-resource language research, and Natural Language Processing (NLP).

---

## 🎯 Purpose

This dataset is designed to support:

* Machine Translation (MT)
* Neural Machine Translation (NMT)
* Language Modeling
* Low-resource NLP research
* Linguistic and dialect studies
* Language preservation and documentation

---

## 📌 Overview

Rakhine is spoken by millions of people in Rakhine State, Myanmar and in diaspora communities. Despite its cultural and linguistic importance, publicly available digital resources remain limited.

The goal of this project is to build an open, high-quality parallel corpus that supports:

* 📚 Parallel sentence alignment (Rakhine ↔ English)
* 🧠 AI and machine translation research
* 🌍 Open-source language technology
* 🔊 Future speech and multimodal datasets
* 📝 Language preservation and documentation

---

## 📁 Repository Structure

```text
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
```

---

## 📊 Dataset Format

### CSV Schema

| Column  | Type   | Description                       |
| ------- | ------ | --------------------------------- |
| rakhine | string | Source sentence in Rakhine        |
| english | string | Corresponding English translation |

### Example

| rakhine         | english        |
| --------------- | -------------- |
| ငါ စားပြီးဗျာယ် | I have eaten.  |
| နင် ဇာမှာလဲ     | Where are you? |

---

## 📈 Dataset Statistics

| Metric           | Value     |
| ---------------- | --------- |
| Sentence Pairs   | TBD       |
| Training Split   | TBD       |
| Validation Split | TBD       |
| Test Split       | TBD       |
| License          | CC BY 4.0 |

---

## ⚙️ Dataset Creation Pipeline

### 1. Prepare Raw Data

Place source files in:

```text
raw_data/
├── rakhine_text.txt
└── english_text.txt
```

Each line should contain one sentence.

### 2. Clean Data

```bash
python scripts/clean_data.py
```

This removes:

* Empty rows
* Duplicate entries
* Invalid sentence pairs
* Formatting inconsistencies

### 3. Align Sentences

```bash
python scripts/align_sentences.py
```

The alignment pipeline supports sentence-level matching between Rakhine and English texts. Future versions may include semantic alignment using multilingual sentence embeddings.

### 4. Generate Dataset Splits

Output files:

```text
data/
├── train.csv
├── dev.csv
└── test.csv
```

---

## 🧠 Use Cases

* Neural Machine Translation (NMT)
* Large Language Model (LLM) training
* Chatbots and conversational AI
* Low-resource language research
* Linguistic analysis
* Language preservation
* NLP benchmarking

---

## 🚀 Roadmap

* Expand beyond 10,000 sentence pairs
* Improve semantic alignment quality
* Human verification and quality scoring
* Publish on Hugging Face Datasets
* Release benchmark evaluation sets
* Add speech and transcription datasets

---

## ⚠️ Limitations

* Some sentence pairs may require manual verification.
* Coverage may not represent all domains or dialect variations.
* Alignment quality depends on source data quality.
* The dataset is actively being expanded and improved.

---

## 📜 License

This dataset is released under the:

**Creative Commons Attribution 4.0 International (CC BY 4.0)**

You are free to share and adapt the material provided appropriate attribution is given.

---

## 📖 Citation

If you use this dataset in research, please cite:

```bibtex
@dataset{rakhine_english_parallel_corpus,
  title={Rakhine–English Parallel Corpus},
  author={Community Contributors},
  year={2026},
  url={https://github.com/<username>/rakhine-english-parallel-corpus}
}
```

---

## 🤝 Contributing

Contributions are welcome.

You can help by:

* Adding new sentence pairs
* Improving translations
* Correcting alignment errors
* Expanding vocabulary coverage
* Improving preprocessing scripts
* Reporting issues

Please open an issue or submit a pull request.

---

## 🌍 Project Goal

To support the preservation, accessibility, and technological development of the Rakhine language through open and reproducible NLP resources.

---

## 📬 Contact

Researchers, developers, linguists, educators, and community contributors interested in Rakhine language technology are welcome to collaborate.

