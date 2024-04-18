import re

bib_data = """
@inproceedings{VanLandeghem2020a,
    author = "Van Landeghem, Jordy and Blaschko, Matthew B and Anckaert, Bertrand and Moens, Marie-Francine",
    year = "2020",
    title = "{Predictive Uncertainty for Probabilistic Novelty Detection in Text Classification}",
    booktitle = "ICML Workshop on Uncertainty and Robustness in Deep Learning"
}

@article{VanLandeghem2022a,
    author = "Van Landeghem, Jordy and Blaschko, Matthew and Anckaert, Bertrand and Moens, Marie-Francine",
    year = "2022",
    title = "{Benchmarking Scalable Predictive Uncertainty in Text Classification}",
    journal = "IEEE Access",
    doi = "10.1109/ACCESS.2022.3168734"
}

@inproceedings{VanLandeghem2023dude,
    author = {Van Landeghem, Jordy and Tito, Rub{\`e}n and Borchmann, {\L}ukasz and Pietruszka, Micha{\l} and Joziak, Pawel and Powalski, Rafal and Jurkiewicz, Dawid and Coustaty, Micka{\"e}l and Anckaert, Bertrand and Valveny, Ernest and Blaschko, Matthew and Moens, Marie-Francine and Stanis{\l}awek, Tomasz},
    year = "2023",
    title = "{Document Understanding Dataset and Evaluation (DUDE)}",
    booktitle = "Proceedings of the IEEE/CVF International Conference on Computer Vision",
    pages = "19528--19540"
}

@inproceedings{VanLandeghem2023icdar,
    author = {Van Landeghem, Jordy and Tito, Rub{\`e}n and Borchmann, {\L}ukasz and Pietruszka, Micha{\l} and Jurkiewicz, Dawid and Powalski, Rafa{\l} and J{\'o}ziak, Pawe{\l} and Biswas, Sanket and Coustaty, Micka{\"e}l and Stanis{\l}awek, Tomasz},
    year = "2023",
    title = "{ICDAR 2023 Competition on Document UnderstanDing of Everything (DUDE)}",
    booktitle = "International Conference on Document Analysis and Recognition",
    pages = "420--434",
    organization = "Springer"
}

@inproceedings{VanLandeghem2024bdpc,
    author = "Van Landeghem, Jordy and Biswas, Sanket and Blaschko, Matthew and Moens, Marie-Francine",
    year = "2024",
    title = "{Beyond Document Page Classification: Design, Datasets, and Challenges}",
    booktitle = "Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision",
    pages = "2962--2972"
}

@inproceedings{VanLandeghem2024kdd,
    author = "Van Landeghem, Jordy and Maity, Subhajit and Banerjee, Ayan and Blaschko, Matthew B and Moens, Marie-Francine and Llados, Josep and Biswas, Sanket",
    year = "2024",
    title = "{DistilDoc: Knowledge Distillation for Visually-Rich Document Applications}",
    booktitle = "International Conference on Document Analysis and Recognition"
}
"""

# Split the BibTeX entries
entries = re.split(r"\n\s*\n", bib_data.strip())

# Write each entry to a separate file
for entry in entries:
    # Extract the key
    key_match = re.search(r"@[^{]+{([^,]+),", entry)
    if key_match:
        key = key_match.group(1)
        # Write entry to file
        with open(f"{key}.bib", "w") as file:
            file.write(entry)
