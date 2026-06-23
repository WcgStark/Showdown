"""
JoJo's Bizarre Adventure power profiles — battle-analysis data (Partes 1–6).

Todas as partes estão jogáveis em todos os modos ("classico", "arena", "teste"),
então não há corte por spoiler: REVEAL_MAX cobre até a Parte 6. O `reveal` por
parte serve de organização.

TRUNFO: como em Dragon Ball, NÃO usamos as tags `domain`/`conqueror` (texto fixo
do motor é de outras franquias). O que decide é a escala de stats — e em JoJo a
"habilidade" do Stand importa tanto quanto a força bruta, então um Stand de
efeito quebrado (parar o tempo, reverter ações) recebe stats altos de utilidade
e burst, não só potência.

STAT SCALE: 0–100, não-linear. Tiers aproximados:
    Stand quebra-realidade (Requiem, Made in Heaven, parar o tempo) .. 90–100
    Stand de combate de elite / Pilar Supremo ...................... 78–90
    Stand forte ................................................... 62–80
    Stand de efeito / suporte ..................................... 46–66
    Hamon/luta sem Stand notável .................................. 30–56
Personagens sem perfil caem no neutro 50.
"""

from __future__ import annotations

from config.power_profiles import UniversePower


ARCS = ["part1", "part2", "part3", "part4", "part5", "part6"]

REVEAL_MAX = {
    "classico": "part6",
    "arena":    "part6",
    "teste":    "part6",
}


# disclosure levels: "full" | "named" | "exists"
PROFILES: dict[str, dict] = {
    # ── Parte 1 — Phantom Blood ──────────────────────────────────────────────
    "Jonathan Joestar": {
        "stats": {"power": 58, "durability": 56, "speed": 50, "utility": 48},
        "positions": {"Duelist": 0.74, "Tank": 0.6, "Captain": 0.55},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["bruiser", "burst", "guard"],
             "text": "Hamon (Sopro do Sol) — energia vital que devasta mortos-vivos; cavalheiro de força e coração imensos."},
        ],
    },
    "Dio Brando": {
        "stats": {"power": 92, "durability": 84, "speed": 90, "utility": 80},
        "positions": {"Captain": 0.82, "Duelist": 0.95, "Tank": 0.66},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["bruiser", "sustain", "betrayal"],
             "text": "Vampiro — congela com o olhar, regenera-se e absorve a vida alheia; força sobre-humana."},
            {"reveal": "part3", "disclosure": "full",
             "tags": ["ace", "burst", "lockdown", "versatility"],
             "text": "The World — para o tempo por vários segundos e age livre nele; espanca o inimigo congelado."},
        ],
    },
    "Will A. Zeppeli": {
        "stats": {"power": 56, "durability": 50, "speed": 52, "utility": 60},
        "positions": {"Support": 0.66, "Duelist": 0.66},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["bruiser", "burst", "leadership"],
             "text": "Mestre do Hamon — canaliza o Sopro com técnica refinada e ensina o caminho a Jonathan."},
        ],
    },
    # ── Parte 2 — Battle Tendency ────────────────────────────────────────────
    "Joseph Joestar": {
        "stats": {"power": 60, "durability": 56, "speed": 58, "utility": 78},
        "positions": {"Duelist": 0.72, "Support": 0.74, "Captain": 0.6, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "part2", "disclosure": "full",
             "tags": ["versatility", "utility", "recon", "manipulation"],
             "text": "Hamon e astúcia — vence pela trapaça e pela leitura do oponente; mais tarde o Hermit Purple revela imagens à distância."},
        ],
    },
    "Caesar Zeppeli": {
        "stats": {"power": 58, "durability": 52, "speed": 60, "utility": 56},
        "positions": {"Duelist": 0.72, "Support": 0.55},
        "abilities": [
            {"reveal": "part2", "disclosure": "full",
             "tags": ["burst", "guard", "versatility"],
             "text": "Hamon em bolhas — esferas de luz que cortam, prendem e protegem com precisão."},
        ],
    },
    "Lisa Lisa": {
        "stats": {"power": 62, "durability": 56, "speed": 64, "utility": 60},
        "positions": {"Duelist": 0.76, "Support": 0.6, "Captain": 0.55},
        "abilities": [
            {"reveal": "part2", "disclosure": "full",
             "tags": ["bruiser", "burst", "leadership"],
             "text": "Mestra do Hamon — conduz o Sopro por um cachecol e luta com elegância mortal."},
        ],
    },
    "Kars": {
        "stats": {"power": 92, "durability": 90, "speed": 86, "utility": 78},
        "positions": {"Duelist": 0.94, "Captain": 0.7, "Tank": 0.78},
        "abilities": [
            {"reveal": "part2", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "sustain", "durability"],
             "text": "Forma de Vida Suprema — lâminas de luz, adaptação instantânea e imortalidade; pode copiar qualquer ser vivo."},
        ],
    },
    "Wamuu": {
        "stats": {"power": 74, "durability": 72, "speed": 72, "utility": 56},
        "positions": {"Duelist": 0.84, "Tank": 0.66},
        "abilities": [
            {"reveal": "part2", "disclosure": "full",
             "tags": ["bruiser", "burst", "aoe"],
             "text": "Pilar Supremo do vento — Vento Divino que gera tornados cortantes; guerreiro de honra implacável."},
        ],
    },
    "Esidisi": {
        "stats": {"power": 70, "durability": 66, "speed": 64, "utility": 58},
        "positions": {"Duelist": 0.78, "Tank": 0.6},
        "abilities": [
            {"reveal": "part2", "disclosure": "full",
             "tags": ["burst", "aoe", "versatility"],
             "text": "Pilar Supremo do calor — sangue a 500°C jorrando em jatos escaldantes e veias-chicote."},
        ],
    },
    # ── Parte 3 — Stardust Crusaders ─────────────────────────────────────────
    "Jotaro Kujo": {
        "stats": {"power": 90, "durability": 80, "speed": 92, "utility": 70},
        "positions": {"Captain": 0.8, "Duelist": 0.96, "Vice Captain": 0.66},
        "abilities": [
            {"reveal": "part3", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "lockdown"],
             "text": "Star Platinum — Stand de precisão e força absurdas que também para o tempo por alguns segundos (ORA ORA ORA)."},
        ],
    },
    "Avdol": {
        "stats": {"power": 66, "durability": 60, "speed": 60, "utility": 62},
        "positions": {"Duelist": 0.76, "Support": 0.6, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "part3", "disclosure": "full",
             "tags": ["burst", "aoe", "versatility"],
             "text": "Magician's Red — Stand de fogo que dispara chamas em forma de ave e cria barreiras de calor."},
        ],
    },
    "Kakyoin": {
        "stats": {"power": 64, "durability": 56, "speed": 66, "utility": 70},
        "positions": {"Duelist": 0.74, "Support": 0.66, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "part3", "disclosure": "full",
             "tags": ["burst", "lockdown", "recon", "versatility"],
             "text": "Hierophant Green — Emerald Splash de longo alcance e uma rede de tentáculos que prende e vigia o campo."},
        ],
    },
    "Polnareff": {
        "stats": {"power": 64, "durability": 56, "speed": 72, "utility": 56},
        "positions": {"Duelist": 0.78, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "part3", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Silver Chariot — esgrima ultrarrápida; ao soltar a armadura, velocidade de retalhar antes que o olho acompanhe."},
        ],
    },
    "Iggy": {
        "stats": {"power": 56, "durability": 50, "speed": 64, "utility": 66},
        "positions": {"Duelist": 0.66, "Support": 0.62},
        "abilities": [
            {"reveal": "part3", "disclosure": "full",
             "tags": ["versatility", "guard", "aoe"],
             "text": "The Fool — Stand de areia que molda escudos, clones e veículos; cão esperto e independente."},
        ],
    },
    "Vanilla Ice": {
        "stats": {"power": 72, "durability": 66, "speed": 74, "utility": 60},
        "positions": {"Duelist": 0.82, "Traitor": 0.55},
        "abilities": [
            {"reveal": "part3", "disclosure": "full",
             "tags": ["burst", "lockdown", "sustain", "versatility"],
             "text": "Cream — devora o espaço à sua frente, virando um vazio invisível que aniquila tudo que toca."},
        ],
    },
    "Hol Horse": {
        "stats": {"power": 56, "durability": 50, "speed": 56, "utility": 60},
        "positions": {"Duelist": 0.66, "Support": 0.55, "Traitor": 0.6},
        "abilities": [
            {"reveal": "part3", "disclosure": "full",
             "tags": ["burst", "versatility"],
             "text": "Emperor — uma pistola-Stand cujas balas ele guia em curvas até o alvo."},
        ],
    },
    # ── Parte 4 — Diamond is Unbreakable ─────────────────────────────────────
    "Josuke": {
        "stats": {"power": 80, "durability": 72, "speed": 80, "utility": 80},
        "positions": {"Duelist": 0.9, "Healer": 0.78, "Captain": 0.66, "Support": 0.6},
        "abilities": [
            {"reveal": "part4", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "heal", "revive", "sustain"],
             "text": "Crazy Diamond — soco rápido e potente que também RESTAURA: reconstrói objetos e cura ferimentos de aliados (mas não os próprios)."},
        ],
    },
    "Koichi": {
        "stats": {"power": 58, "durability": 50, "speed": 56, "utility": 70},
        "positions": {"Support": 0.72, "Duelist": 0.62},
        "abilities": [
            {"reveal": "part4", "disclosure": "full",
             "tags": ["lockdown", "debuff", "versatility", "burst"],
             "text": "Echoes (Atos 1–3) — implanta sons que viram efeitos reais; o Ato 3 (3 Freeze) multiplica o peso do alvo e o prega no chão."},
        ],
    },
    "Okuyasu": {
        "stats": {"power": 66, "durability": 62, "speed": 60, "utility": 58},
        "positions": {"Duelist": 0.74, "Tank": 0.6},
        "abilities": [
            {"reveal": "part4", "disclosure": "full",
             "tags": ["bruiser", "burst", "lockdown"],
             "text": "The Hand — apaga o espaço com a mão direita, aproximando o inimigo ou removendo qualquer coisa da existência."},
        ],
    },
    "Rohan": {
        "stats": {"power": 50, "durability": 46, "speed": 54, "utility": 86},
        "positions": {"Support": 0.84, "Duelist": 0.55, "Traitor": 0.6},
        "abilities": [
            {"reveal": "part4", "disclosure": "full",
             "tags": ["manipulation", "debuff", "lockdown", "recon"],
             "text": "Heaven's Door — transforma o alvo num livro: lê seus segredos e escreve comandos que o controlam."},
        ],
    },
    "Yoshikage Kira": {
        "stats": {"power": 78, "durability": 66, "speed": 72, "utility": 80},
        "positions": {"Duelist": 0.86, "Traitor": 0.66, "Captain": 0.6},
        "abilities": [
            {"reveal": "part4", "disclosure": "full",
             "tags": ["ace", "burst", "versatility", "manipulation"],
             "text": "Killer Queen — tudo que toca vira uma bomba; Sheer Heart Attack persegue o calor e Bites the Dust reseta o tempo numa armadilha letal."},
        ],
    },
    # ── Parte 5 — Golden Wind ────────────────────────────────────────────────
    "Giorno": {
        "stats": {"power": 88, "durability": 74, "speed": 82, "utility": 90},
        "positions": {"Captain": 0.78, "Duelist": 0.92, "Healer": 0.7, "Support": 0.62},
        "abilities": [
            {"reveal": "part5", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "heal", "versatility"],
             "text": "Gold Experience — dá vida à matéria, acelera os sentidos e cura criando órgãos; o Requiem zera qualquer ação e impede que ela 'aconteça'."},
        ],
    },
    "Bucciarati": {
        "stats": {"power": 74, "durability": 66, "speed": 72, "utility": 74},
        "positions": {"Duelist": 0.82, "Captain": 0.66, "Vice Captain": 0.7, "Support": 0.6},
        "abilities": [
            {"reveal": "part5", "disclosure": "full",
             "tags": ["bruiser", "burst", "versatility", "lockdown", "leadership"],
             "text": "Sticky Fingers — abre zíperes em qualquer superfície (e no espaço) para emboscar, desmembrar e teletransportar pelo cenário."},
        ],
    },
    "Mista": {
        "stats": {"power": 70, "durability": 60, "speed": 66, "utility": 60},
        "positions": {"Duelist": 0.8, "Support": 0.55},
        "abilities": [
            {"reveal": "part5", "disclosure": "full",
             "tags": ["burst", "versatility", "aoe"],
             "text": "Sex Pistols — seis pequenos Stands que desviam e guiam suas balas em ricochetes impossíveis."},
        ],
    },
    "Narancia": {
        "stats": {"power": 66, "durability": 56, "speed": 70, "utility": 58},
        "positions": {"Duelist": 0.76, "Support": 0.55},
        "abilities": [
            {"reveal": "part5", "disclosure": "full",
             "tags": ["burst", "aoe", "recon"],
             "text": "Aerosmith — um aviãozinho-Stand que rastreia pelo CO₂ e despeja rajadas e bombas em área."},
        ],
    },
    "Abbacchio": {
        "stats": {"power": 60, "durability": 56, "speed": 56, "utility": 76},
        "positions": {"Support": 0.78, "Duelist": 0.6, "Traitor": 0.55},
        "abilities": [
            {"reveal": "part5", "disclosure": "full",
             "tags": ["recon", "utility", "versatility"],
             "text": "Moody Blues — reproduz fielmente eventos passados de qualquer lugar; investigação e leitura de movimentos."},
        ],
    },
    "Fugo": {
        "stats": {"power": 70, "durability": 56, "speed": 62, "utility": 64},
        "positions": {"Duelist": 0.76, "Support": 0.55},
        "abilities": [
            {"reveal": "part5", "disclosure": "full",
             "tags": ["aoe", "debuff", "burst", "sustain"],
             "text": "Purple Haze — punhos que liberam um vírus carnívoro letal que se espalha e dissolve tudo por perto."},
        ],
    },
    "Diavolo": {
        "stats": {"power": 86, "durability": 76, "speed": 88, "utility": 78},
        "positions": {"Duelist": 0.92, "Captain": 0.7, "Traitor": 0.66},
        "abilities": [
            {"reveal": "part5", "disclosure": "full",
             "tags": ["ace", "burst", "lockdown", "versatility"],
             "text": "King Crimson — apaga até dez segundos do tempo (Epitáfio prevê o futuro próximo) e age dentro desse intervalo apagado, surgindo já com o golpe dado."},
        ],
    },
    "Risotto": {
        "stats": {"power": 74, "durability": 64, "speed": 64, "utility": 76},
        "positions": {"Duelist": 0.82, "Support": 0.6, "Traitor": 0.6},
        "abilities": [
            {"reveal": "part5", "disclosure": "full",
             "tags": ["burst", "debuff", "versatility", "sabotage"],
             "text": "Metallica — controla o ferro do próprio sangue do alvo: lâminas internas, agulhas e invisibilidade."},
        ],
    },
    "Ghiaccio": {
        "stats": {"power": 66, "durability": 64, "speed": 66, "utility": 56},
        "positions": {"Duelist": 0.76, "Tank": 0.6},
        "abilities": [
            {"reveal": "part5", "disclosure": "full",
             "tags": ["burst", "guard", "aoe", "lockdown"],
             "text": "White Album — uma armadura de gelo que congela o ambiente e protege como uma fortaleza ambulante."},
        ],
    },
    "Cioccolata": {
        "stats": {"power": 68, "durability": 58, "speed": 58, "utility": 70},
        "positions": {"Duelist": 0.72, "Support": 0.58, "Traitor": 0.62},
        "abilities": [
            {"reveal": "part5", "disclosure": "full",
             "tags": ["aoe", "debuff", "sustain", "sabotage"],
             "text": "Green Day — espalha um mofo mortal que se multiplica em quem desce de altura; epidemia que toma a cidade."},
        ],
    },
    # ── Parte 6 — Stone Ocean ────────────────────────────────────────────────
    "Jolyne": {
        "stats": {"power": 78, "durability": 66, "speed": 74, "utility": 76},
        "positions": {"Duelist": 0.86, "Captain": 0.66, "Vice Captain": 0.62, "Support": 0.58},
        "abilities": [
            {"reveal": "part6", "disclosure": "full",
             "tags": ["bruiser", "burst", "versatility", "lockdown", "guard"],
             "text": "Stone Free — desfaz o corpo em fio para amarrar, armar teias, remendar e golpear em rajada."},
        ],
    },
    "Weather Report": {
        "stats": {"power": 84, "durability": 72, "speed": 74, "utility": 82},
        "positions": {"Duelist": 0.88, "Support": 0.66, "Captain": 0.6},
        "abilities": [
            {"reveal": "part6", "disclosure": "full",
             "tags": ["ace", "aoe", "burst", "versatility", "lockdown"],
             "text": "Weather Report — comanda o clima (raios, geada, sapos venenosos) e, liberado, o Heavy Weather espalha uma ilusão fatal pela luz."},
        ],
    },
    "Anasui": {
        "stats": {"power": 72, "durability": 62, "speed": 66, "utility": 70},
        "positions": {"Duelist": 0.8, "Support": 0.58},
        "abilities": [
            {"reveal": "part6", "disclosure": "full",
             "tags": ["bruiser", "versatility", "lockdown"],
             "text": "Diver Down — mergulha dentro de objetos e corpos para rearranjá-los por dentro e liberar a força guardada."},
        ],
    },
    "Hermes": {
        "stats": {"power": 64, "durability": 58, "speed": 62, "utility": 62},
        "positions": {"Duelist": 0.74, "Support": 0.55},
        "abilities": [
            {"reveal": "part6", "disclosure": "full",
             "tags": ["burst", "versatility", "debuff"],
             "text": "Kiss — cola adesivos que criam um duplicado de qualquer coisa; ao arrancar, o dano dobra de volta no alvo."},
        ],
    },
    "Foo Fighters": {
        "stats": {"power": 58, "durability": 64, "speed": 56, "utility": 72},
        "positions": {"Support": 0.74, "Tank": 0.6, "Healer": 0.55},
        "abilities": [
            {"reveal": "part6", "disclosure": "full",
             "tags": ["versatility", "sustain", "guard", "aoe"],
             "text": "F.F. — uma colônia de plâncton num corpo: regenera-se, dispara jatos d'água sob pressão e reformata sua forma."},
        ],
    },
    "Pucci": {
        "stats": {"power": 90, "durability": 76, "speed": 92, "utility": 92},
        "positions": {"Captain": 0.82, "Duelist": 0.95, "Traitor": 0.7},
        "abilities": [
            {"reveal": "part6", "disclosure": "full",
             "tags": ["ace", "burst", "manipulation", "versatility", "lockdown"],
             "text": "Whitesnake → C-Moon → Made in Heaven — rouba memórias e Stands, inverte a gravidade e por fim ACELERA o tempo do universo até reescrever a realidade."},
        ],
    },
}


JOJO_POWER = UniversePower(
    arcs=ARCS,
    reveal_max=REVEAL_MAX,
    profiles=PROFILES,
    default_reveal="part6",
)
