================================================================
  SHOWDOWN DRAFT — GUIA DO DESENVOLVEDOR
================================================================


----------------------------------------------------------------
  1. MODO DEV (testar sem buildar)
----------------------------------------------------------------

Rode o comando abaixo no terminal do VS Code:

    dev.bat

Isso sobe o servidor Vite (frontend) e abre o app apontando
para localhost:5173. Qualquer mudança no frontend aparece
automaticamente sem precisar reiniciar.

Para parar: feche a janela do app.

Requisitos:
  - Python com pywebview instalado
  - Node.js instalado
  - Dependências do frontend instaladas (rode uma vez):
        cd frontend
        npm install


----------------------------------------------------------------
  2. BUILD (gerar o .exe)
----------------------------------------------------------------

Rode no terminal:

    build.bat

Isso faz duas coisas:
  1. Builda o frontend (npm run build) -> gera a pasta dist/
  2. Empacota tudo com PyInstaller -> gera dist/Showdown Draft.exe

O .exe gerado é standalone — não precisa de Python instalado.

Requisitos:
  - PyInstaller instalado: pip install pyinstaller
  - pywebview instalado:   pip install pywebview


----------------------------------------------------------------
  3. SALVAR NO GIT (subir mudancas para o GitHub)
----------------------------------------------------------------

Depois de fazer qualquer mudança no código:

    git add .
    git commit -m "descrição do que mudou"
    git push

Exemplos de mensagem de commit:
  - "adiciona novo universo Dragon Ball"
  - "corrige bug no sistema de undo"
  - "melhora visual da tela de resultado"

Obs: o .exe, a pasta dist/ e a pasta build/ são ignorados
automaticamente pelo .gitignore — não vão pro GitHub.


----------------------------------------------------------------
  4. LANÇAR NOVA RELEASE (atualização para os jogadores)
----------------------------------------------------------------

Um único comando no terminal:

    .\release.bat 1.0.3

Substitua 1.0.3 pelo número da versão que quer lançar.
Incremente sempre: 1.0.2 -> 1.0.3 -> 1.0.4 -> etc.

O que acontece automaticamente:
  1. Atualiza o número de versão no código (updater.py)
  2. Faz commit e cria a tag no Git
  3. Faz push para o GitHub
  4. GitHub Actions builda o .exe (aguarde ~5-10 minutos)
  5. Publica o release com o .exe disponível para download

Acompanhe o build em:
  https://github.com/WcgStark/Showdown/actions

Quando terminar, os jogadores que abrirem o app vão ver o
banner de atualização automaticamente e podem instalar com
um clique.


----------------------------------------------------------------
  FLUXO RESUMIDO DO DIA A DIA
----------------------------------------------------------------

  Mexeu no código?
    -> git add . && git commit -m "..." && git push

  Quer que os jogadores recebam a versão nova?
    -> .\release.bat 1.X.X

================================================================
