# Pagerank-Spark
Pagerank-Spark


## 🗂️ Overview

This project applies **Apache Spark** techniques to implement the **PageRank algorithm** and **Word Count** from scratch, along with a bonus task involving **synthetic k-mer sentence generation**.

It showcases the use of Spark RDDs, data parsing, custom transformations, and iterative computations, with results visualized in a notebook.

---

## 📁 Folder Structure

- `notebook/` – Jupyter notebook with PageRank logic and results  
- `scripts/` – Python scripts for generating links, random data, and computing word count  
- `data/` – Sample pagelinks input data  
- `report/` – Submitted homework and bonus PDF reports  
- `requirements.txt` – Required Python libraries  
- `README.md` – This file  

---


### 🧠 Scripts

- `scripts/generate_pagelinks.py` – Generates input graph for PageRank
- `scripts/sentence_generator.py` – Produces random k-mer sentences (bonus)
- `scripts/word_count.py` – Standard Spark-based Word Count program

### 📂 Data

- `data/pagelinks.txt` – Input graph structure for PageRank

### 📑 Reports

- `Report.pdf` – report for k-mer generation task

---



## ⚙️ How to Run

### 📦 Install Requirements

Run the following to install all dependencies:

```bash
pip install -r requirements.txt
