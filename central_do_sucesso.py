import os
import webbrowser
import ctypes


def central():
    print("--- 🌟 CENTRAL DO SUCESSO - ESTUDANTE ESTÁCIO 🌟 ---")
    print("1. 🧹 LIMPAR A BAGUNÇA (Organizar Pastas)")
    print("2. 💼 BUSCAR EMPREGO (Java, Python, React, JS)")
    print("3. 🚪 SAIR")

    opcao = input("\nO que a sua babá deve fazer hoje? ")

    if opcao == "1":
        # Aqui ele chama a função de organizar que já deixamos perfeita
        from script1 import organizar_meu_caos
        organizar_meu_caos()

    elif opcao == "2":
        # Aqui ele abre as vagas para você
        print("🚀 Abrindo portais de emprego... Boa sorte!")
        vagas = [
            "https://www.linkedin.com/jobs/search/?keywords=Desenvolvedor%20Junior",
            "https://portal.gupy.io/job-search/term=desenvolvedor",
            "https://br.indeed.com/jobs?q=junior+developer"
        ]
        for link in vagas:
            webbrowser.open(link)
        ctypes.windll.user32.MessageBoxW(0, "Portais abertos! Hora de brilhar.", "Babá Tecnológica", 64)


if __name__ == "__main__":
    central()