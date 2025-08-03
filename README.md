# Project Context Generator

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/github/license/antonyandrade01/project-context-generator?style=for-the-badge)

<!-- English Version (Default) -->
<div align="center">

### 🇬🇧 English Version

A simple yet powerful Python script to automate the process of bundling multiple project files into a single, organized text file, perfect for AI-powered code reviews and analysis.
</div>

#### The Problem: Why This Tool?

As developers, we are increasingly using AI assistants (like ChatGPT, Gemini, Copilot, etc.) for code reviews, refactoring, and documentation. However, manually copying and pasting the content of dozens of files (`.py`, `.html`, `.css`, `.yml`) into a prompt is a tedious, time-consuming, and error-prone process. It's easy to miss a file and provide the AI with incomplete context.

#### ✨ The Solution: How It Works

This script solves that problem. It walks through your project directory and performs two main actions:

1.  **Full Project Tree Listing:** It first generates a complete list of all files and their paths, giving the AI a comprehensive overview of your project structure.
2.  **Selective Content Bundling:** It then reads a specified list of file names (`nomes_dos_arquivos.txt`), finds them within the project, and concatenates their full path and content into a single output file. It intelligently handles multiple character encodings to prevent errors.

The result is a single `resultado.txt` file that you can copy and paste in one go, providing the AI with perfect context every time.

#### 🚀 How to Use

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/antonyandrade01/project-context-generator.git
    cd project-context-generator
    ```

2.  **Define Your Files:**
    Create a file named `nomes_dos_arquivos.txt` in the same directory and list the names of all the files you want to include, one per line. For example:
    ```txt
    app.py
    models.py
    docker-compose.yml
    Dockerfile
    layout.html
    agenda.css
    ```

3.  **Run the Script:**
    Execute the Python script from your terminal. Update the paths inside the script if needed to point to your target project directory.
    ```bash
    python encontrar_e_copiar_arquivos.py
    ```

4.  **Get Your Context:**
    A file named `resultado.txt` will be generated. Open it, copy the entire content, and paste it into your AI prompt!

---
<!-- Collapsible Portuguese Version -->
<details align="center">
  <summary><b>🇧🇷 Clique aqui para ver a versão em Português</b></summary>
  
  ### 🇧🇷 Versão em Português

  <p>Um script Python simples, porém poderoso, para automatizar o processo de agrupar múltiplos arquivos de um projeto em um único arquivo de texto organizado, perfeito para análises e code reviews via IA.</p>

  <h4>O Problema: Por que esta Ferramenta?</h4>
  <p>Como desenvolvedores, usamos cada vez mais assistentes de IA (como ChatGPT, Gemini, Copilot, etc.) para revisão de código, refatoração e documentação. No entanto, o processo de copiar e colar manualmente o conteúdo de dezenas de arquivos (`.py`, `.html`, `.css`, `.yml`) em um prompt é tedioso, demorado e propenso a erros. É fácil esquecer um arquivo e fornecer um contexto incompleto para a IA.</p>
  
  <h4>✨ A Solução: Como Funciona</h4>
  <p>Este script resolve esse problema. Ele percorre o diretório do seu projeto e executa duas ações principais:</p>
  <ol>
    <li><strong>Listagem Completa da Árvore do Projeto:</strong> Primeiro, ele gera uma lista completa de todos os arquivos e seus caminhos, dando à IA uma visão geral da estrutura do seu projeto.</li>
    <li><strong>Agrupamento Seletivo de Conteúdo:</strong> Em seguida, ele lê uma lista de nomes de arquivos especificada (<code>nomes_dos_arquivos.txt</code>), os encontra dentro do projeto e concatena seu caminho completo e conteúdo em um único arquivo de saída. Ele lida de forma inteligente com múltiplas codificações de caracteres para evitar erros.</li>
  </ol>
  <p>O resultado é um único arquivo <code>resultado.txt</code> que você pode copiar e colar de uma só vez, fornecendo um contexto perfeito para a IA todas as vezes.</p>

  <h4>🚀 Como Usar</h4>
  <ol>
    <li><strong>Clone o Repositório:</strong>
      <pre><code>git clone https://github.com/antonyandrade01/project-context-generator.git
cd project-context-generator</code></pre>
    </li>
    <li><strong>Defina Seus Arquivos:</strong>
      <p>Crie um arquivo chamado <code>nomes_dos_arquivos.txt</code> no mesmo diretório e liste os nomes de todos os arquivos que você deseja incluir, um por linha. Por exemplo:</p>
      <pre><code>app.py
models.py
docker-compose.yml
Dockerfile
layout.html
agenda.css</code></pre>
    </li>
    <li><strong>Execute o Script:</strong>
      <p>Execute o script Python pelo seu terminal. Atualize os caminhos dentro do script, se necessário, para apontar para o diretório do projeto que você deseja analisar.</p>
      <pre><code>python encontrar_e_copiar_arquivos.py</code></pre>
    </li>
    <li><strong>Obtenha seu Contexto:</strong>
      <p>Um arquivo chamado <code>resultado.txt</code> será gerado. Abra-o, copie todo o conteúdo e cole no seu prompt de IA!</p>
    </li>
  </ol>
</details>

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This tool was born out of a real need to optimize my own development workflow. I hope it helps yours too!