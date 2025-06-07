from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search
from load_text import load_text
from test_algorithm import test_algorithm
from generate_md import generate_md


text1 = load_text("task_3/text1.txt")
text2 = load_text("task_3/text2.txt")

existing1 = "Також, у теорії алгоритмів жадібні алгоритми відіграють важливу роль."         # існуючий у тексті
existing2 = "На основі одержаних результатів з таблиці 2 було побудовано графік"
non_existing = "неіснуючий111111"  # вигаданий

algorithms = {
    'KMP': kmp_search,
    'Rabin-Karp': rabin_karp_search,
    'Boyer-Moore': boyer_moore_search
}

results = {
    "text1.txt": {},
    "text2.txt": {}
}

for name, algo in algorithms.items():
    exist1 = test_algorithm(algo, text1, existing1)
    fake1 = test_algorithm(algo, text1, non_existing)
    exist2 = test_algorithm(algo, text2, existing2)
    fake2 = test_algorithm(algo, text2, non_existing)

    results["text1.txt"][name] = (exist1, fake1)
    results["text2.txt"][name] = (exist2, fake2)

for filename, alg_data in results.items():
    print(f"\n📄 {filename}")
    for alg, (exist, fake) in alg_data.items():
        print(f"{alg:<12} | існує: {exist:.6f} сек | вигаданий: {fake:.6f} сек")


   

print("results", results)

md_text = generate_md(results)

with open("search_comparison.md", "w", encoding="utf-8") as f:
    f.write(md_text)
