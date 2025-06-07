
def generate_md(results):
    md = "Порівняння алгоритмів пошуку підрядка\n\n"

    fastest_z_too = None

    for text, data in results.items():
        md += f"## Текст: `{text}`\n"
        md += "| Алгоритм     | Існуючий (сек) | Вигаданий (сек) |\n"
        md += "|--------------|----------------|-----------------|\n"

        fastest = None
        fastest_time = float("inf")

        for algo, (exist_time, fake_time) in data.items():
            md += f"| {algo:<13} | {exist_time:<14.4f} | {fake_time:<15.4f} |\n"
            avg_time = (exist_time + fake_time) / 2
            if avg_time < fastest_time:
                fastest_time = avg_time
                fastest = algo

        md += f"\n **Найшвидший:** {fastest}\n\n"


    return md