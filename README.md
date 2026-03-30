# 🚀 Mostra Virtual - UFJ (Ciência da Computação)

Plataforma moderna e responsiva desenvolvida para a divulgação de projetos, pesquisas e agenda de eventos do curso de Ciência da Computação da **Universidade Federal de Jataí (UFJ)**.

---

## 📌 Sobre o Projeto
A **Mostra Virtual** nasceu da necessidade de centralizar e dar visibilidade à produção científica da universidade. O projeto foca em uma interface intuitiva ("Glassmorphism"), alta performance e um painel administrativo robusto para gestão de conteúdo.

## 🛠️ Tecnologias Utilizadas

### Backend & Banco de Dados
* **Python 3.12** com **Django Framework**
* **Banco de Dados Híbrido**: 
    - **SQLite**: Utilizado em ambiente de desenvolvimento pela sua praticidade.
    - **PostgreSQL**: Configurado para o ambiente de produção via `dj_database_url`.
* **Django-Jazzmin**: Interface administrativa personalizada e moderna.
* **WhiteNoise**: Gerenciamento eficiente de arquivos estáticos para deploy.

### Frontend
* **Bootstrap 5**: Estrutura e componentes responsivos.
* **Plus Jakarta Sans**: Tipografia moderna via Google Fonts.
* **AOS (Animate On Scroll)**: Animações de entrada suaves.
* **Particles.js**: Fundo dinâmico com efeito de partículas.
* **Bootstrap Icons**: Biblioteca de ícones vetoriais.

---

## 📱 Destaques de Design & UX

Durante o desenvolvimento, focamos em resolver desafios reais de usabilidade:

* **Menu Mobile "App-Like"**: Implementamos um sistema de navegação por abas horizontais no mobile, facilitando o acesso rápido com apenas um clique e eliminando o menu hambúrguer.
* **Identidade Visual UFJ**: Paleta de cores baseada na identidade da instituição (**Azul, Branco e Amarelo**), com alto contraste para garantir leitura perfeita.
* **Cards Interativos**: Efeito de "Glassmorphism" no container principal e cards de pesquisa com hover dinâmico e ícones destacados (lâmpada amarela para insights).
* **Admin Customizado**: Painel administrativo totalmente personalizado com a logo da UFJ e tema profissional, facilitando a gestão para usuários não-técnicos.

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/joaquimcaetano-creator/selecao_obsam.git](https://github.com/joaquimcaetano-creator/selecao_obsam.git)
   cd selecao_obsam