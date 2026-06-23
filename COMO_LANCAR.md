# Como lançar uma versão (LEIA ANTES DE PUBLICAR)

## ⚠️ A causa do bug do v1.3.3: CACHE do WebView2 (não era o build)

O Dragon Ball aparecia sem banner e o lobby sem paginação **mesmo com o build certo**.
A causa real: o `main.py`/exe carregam o frontend de um caminho **fixo**
(`file://.../dist/index.html`), então o **WebView2 guarda a UI antiga em cache** numa
pasta persistente (`%LOCALAPPDATA%\ShowdownDraft\webview\EBWebView`) e continua servindo
a versão velha **depois da atualização**. O `dev.py` nunca sofreu disso porque usa um
cache separado (`webview-dev`) e carrega via servidor Vite, que serve sempre fresco.

**Conserto já aplicado no código:** [main.py](main.py) agora chama `_clear_webview_cache()`
no início, apagando `Cache`/`Code Cache`/`GPUCache` a cada abertura (as configurações do
usuário ficam em `Local Storage` e **não** são tocadas). Com isso, toda atualização passa
a mostrar a UI nova. **Não remova essa função.**

Se algum dia a UI voltar a aparecer "velha" depois de um update, o suspeito nº 1 é o
cache do WebView2 — não o build.

## A outra regra de ouro: sempre rode `npm run build`

O `.exe` empacota a pasta **`dist/`** (frontend já compilado), não o `frontend/src/`.
Se você não rodar `npm run build`, o `dist/` continua o do build anterior → você publica
**backend novo + interface velha**. O `dev.py` ignora o `dist/` (roda o Vite ao vivo),
então **passar no dev não prova que o build está certo**.

## O jeito certo: use a release.bat inteira

```
release.bat 1.3.4
```

Faz, nesta ordem, abortando se algo falhar:

1. `_set_version.py` — atualiza a versão no código
2. `npm run build` — compila o frontend pro `dist/`
3. `pyinstaller showdown.spec` — gera o `.exe` empacotando o `dist/`
4. `git commit` + `push` + `gh release create`

Não faça os passos na mão (a mensagem de commit que não for o `release vX.Y.Z` exato que a
release.bat gera é sinal de release manual — onde é fácil esquecer um passo).

## Antes de publicar: TESTE O .EXE

Abra o `dist\ShowdownDraft.exe` real (não o `dev.py`) e confirme:
- [ ] universo novo aparece **com banner**
- [ ] lobby pagina em **3×2 com seta** quando passa de 6 universos
- [ ] versão no canto certa

## Para corrigir um release já publicado: SUBA A VERSÃO

O auto-updater ([updater.py](updater.py)) só baixa se a versão do GitHub for **maior** que a
instalada (`latest <= atual` → não atualiza). Re-subir o **mesmo** número **não** alcança
quem já atualizou — para empurrar correção, suba o número (ex.: 1.3.4).

## Checklist rápido

- [ ] `release.bat X.Y.Z` (nunca na mão)
- [ ] `npm run build` rodou de fato
- [ ] abri o `dist\ShowdownDraft.exe` e validei banner + paginação + versão
- [ ] `_clear_webview_cache()` continua no `main.py`
- [ ] número da versão subiu em relação ao último release
- [ ] só então publiquei
