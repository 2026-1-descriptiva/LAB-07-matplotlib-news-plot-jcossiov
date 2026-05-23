"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os

    import matplotlib.pyplot as plt
    import pandas as pd

    data_path = os.path.join("files", "input", "news.csv")
    output_dir = os.path.join("files", "plots")
    output_path = os.path.join(output_dir, "news.png")

    data = pd.read_csv(data_path, index_col=0)

    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(10, 6))
    for column in data.columns:
        plt.plot(data.index, data[column], marker="o", label=column)

    plt.title("Medios de comunicación en porcentaje de uso por año")
    plt.xlabel("Año")
    plt.ylabel("Participación (%)")
    plt.xticks(data.index)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
