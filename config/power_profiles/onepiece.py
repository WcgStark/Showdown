"""
One Piece power profiles — battle-analysis data, second universe after Jujutsu.

SPOILER POLICY: the playable pool is already split by filter in config.universes
(`manga`, `anime`, `adilson` = só até Wano, `teste`). Post-Wano / manga-only
characters are EXCLUDED from the pool wholesale in those modes, so the per-ability
`reveal` gate here is a second layer of safety: a power-up shown only late (e.g.
Gear 5 / Nika, revealed in Wano) is tagged with its arc, and REVEAL_MAX drops it
for any mode whose boundary comes earlier. `disclosure="named"` is used for
manga-only fighters whose feats aren't fully established yet (Holy Knights, Elbaf
royals, Imu), so we acknowledge the power without over-claiming specifics.

STAT SCALE: 0–100, intentionally NON-linear so power tiers are dramatic. Tiers:
    world top (Roger, prime Whitebeard, Imu, Kaidou, Big Mom) .. 95–100
    Yonko / Admiral / Mihawk / Gorosei ........................ 90–96
    Yonko commander / top Warlord / legend ..................... 82–90
    elite fighter (Worst Gen, Vinsmokes, CP0) .................. 72–84
    strong (named officer, supernova lieutenant) .............. 58–74
    mid (utility Straw Hat, gimmick fruit) .................... 42–58
    support / civilian ........................................ 8–42  (a healer
        is weak in raw power but huge in utility)
Characters with no profile fall back to a neutral 50.

CONQUEROR'S HAKI ("conqueror" tag) is the One Piece trump card, mirroring the
domain mechanic in Jujutsu: a side fielding advanced Conqueror's Haki in combat
overwhelms a side that lacks it entirely. Two CoC users cancel out (a clash).
"""

from __future__ import annotations

from config.power_profiles import UniversePower


# Ordered reveal tiers, earliest → latest (story continuity / saga order).
ARCS = [
    "east_blue",      # East Blue saga
    "alabasta",       # Baroque Works / Arabasta (+ Little Garden, Drum)
    "skypiea",        # Jaya / Skypiea
    "water7",         # Water 7 / Enies Lobby (CP9)
    "thriller_bark",  # Thriller Bark
    "marineford",     # Sabaody / Impel Down / Marineford War
    "fishman",        # Fishman Island
    "dressrosa",      # Punk Hazard / Dressrosa
    "zou_wci",        # Zou / Whole Cake Island
    "wano",           # Wano Country (anime boundary for "adilson" = até Wano)
    "egghead",        # Egghead (final saga — animated by ~2026)
    "elbaf",          # Elbaf / latest manga
]

REVEAL_MAX = {
    "manga":   "elbaf",     # tudo
    "anime":   "egghead",   # anime alcançou Egghead
    "adilson": "wano",      # somente até Wano
    "teste":   "elbaf",     # só Luffy + Whitebeard, não importa o corte
    "arena":   "elbaf",     # se algum dia One Piece ganhar modo arena
}


# disclosure levels: "full" | "named" | "exists"
PROFILES: dict[str, dict] = {
    # ── Chapéus de Palha ───────────────────────────────────────────────────
    "Monkey D. Luffy": {
        "stats": {"power": 97, "durability": 90, "speed": 92, "utility": 80},
        "positions": {"Captain": 1.0, "Duelist": 0.95, "Vice Captain": 0.7, "Tank": 0.7},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["bruiser", "burst", "leadership"],
             "text": "Fruta de Borracha — corpo elástico imune a impactos e balas; Gears 2 e 3 multiplicam velocidade e potência."},
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Gear 4 (Boundman/Snakeman) — Haki do Armamento avançado e golpes elásticos imprevisíveis."},
            {"reveal": "wano", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "conqueror"],
             "text": "Gear 5 (Nika) — liberdade total: dobra o ambiente como borracha e impõe Haki do Rei avançado."},
        ],
    },
    "Roronoa Zoro": {
        "stats": {"power": 84, "durability": 82, "speed": 80, "utility": 55},
        "positions": {"Duelist": 0.95, "Vice Captain": 0.85, "Tank": 0.7, "Captain": 0.55},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["bruiser", "burst", "ace"],
             "text": "Estilo de Três Espadas (Santoryu) — espadachim de elite com cortes em longo alcance."},
            {"reveal": "wano", "disclosure": "full",
             "tags": ["bruiser", "burst", "conqueror"],
             "text": "Haki do Rei avançado e o Reino dos Mortos — cortes que ferem até a pele de aço de um Imperador."},
        ],
    },
    "Nami": {
        "stats": {"power": 30, "durability": 28, "speed": 46, "utility": 78},
        "positions": {"Support": 0.9, "Vice Captain": 0.45},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["utility", "debuff", "recon"],
             "text": "Clima Tact — manipula raios, vento e tempo para atordoar e abrir brechas; navegadora genial."},
        ],
    },
    "Sanji": {
        "stats": {"power": 80, "durability": 78, "speed": 86, "utility": 62},
        "positions": {"Duelist": 0.9, "Vice Captain": 0.7, "Support": 0.55, "Tank": 0.6},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Diable Jambe — chutes flamejantes de altíssima velocidade; não usa as mãos para proteger as do cozinheiro."},
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["bruiser", "versatility", "recon"],
             "text": "Raid Suit Germa — exoesqueleto que confere invisibilidade e corpo aprimorado."},
        ],
    },
    "Jinbe": {
        "stats": {"power": 82, "durability": 86, "speed": 70, "utility": 66},
        "positions": {"Tank": 0.9, "Duelist": 0.82, "Vice Captain": 0.78, "Captain": 0.55},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["bruiser", "tank", "durability", "guard"],
             "text": "Karatê Homem-Peixe — golpeia a água como matéria sólida; timoneiro e muralha do bando."},
        ],
    },
    "Nico Robin": {
        "stats": {"power": 52, "durability": 42, "speed": 50, "utility": 84},
        "positions": {"Support": 0.92, "Duelist": 0.55},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["utility", "lockdown", "versatility", "recon"],
             "text": "Fruta Flor — brota membros em qualquer lugar para imobilizar; arqueóloga que lê Poneglyphs."},
            {"reveal": "wano", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Demonio Fleur (gigante) — clona um corpo colossal para esmagar oponentes."},
        ],
    },
    "Usopp": {
        "stats": {"power": 34, "durability": 30, "speed": 44, "utility": 70},
        "positions": {"Support": 0.88, "Duelist": 0.45},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["debuff", "utility", "recon"],
             "text": "Atirador de elite — munição de plantas, fumaça e ilusões; mira sobre-humana e nervos de aço quando importa."},
        ],
    },
    "Tony Tony Chopper": {
        "stats": {"power": 46, "durability": 44, "speed": 50, "utility": 80},
        "positions": {"Healer": 0.95, "Support": 0.7, "Duelist": 0.5, "Tank": 0.55},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["heal", "sustain", "utility"],
             "text": "Médico do bando — diagnostica e trata qualquer ferimento; Rumble Balls alteram suas formas de combate."},
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["bruiser", "tank", "durability"],
             "text": "Monster Point — transformação gigantesca de força e resistência brutas."},
        ],
    },
    "Brook": {
        "stats": {"power": 58, "durability": 50, "speed": 72, "utility": 64},
        "positions": {"Duelist": 0.75, "Support": 0.6},
        "abilities": [
            {"reveal": "thriller_bark", "disclosure": "full",
             "tags": ["burst", "debuff", "utility"],
             "text": "Esgrima gelada — cortes ultrarrápidos que congelam; alma que sai do corpo para explorar e assombrar."},
        ],
    },
    "Franky": {
        "stats": {"power": 62, "durability": 74, "speed": 48, "utility": 76},
        "positions": {"Tank": 0.82, "Support": 0.72, "Duelist": 0.6},
        "abilities": [
            {"reveal": "water7", "disclosure": "full",
             "tags": ["tank", "durability", "burst", "utility"],
             "text": "Ciborgue — corpo blindado movido a cola; canhões, Radical Beam e engenharia de combate."},
        ],
    },
    # ── East Blue (vilões e aliados) ───────────────────────────────────────
    "Buggy": {
        "stats": {"power": 32, "durability": 40, "speed": 38, "utility": 72},
        "positions": {"Captain": 0.7, "Support": 0.6, "Traitor": 0.5},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["versatility", "guard", "leadership"],
             "text": "Fruta Picada — corpo se separa em partes flutuantes, imune a cortes; sorte absurda o alça a posições muito acima de sua força."},
        ],
    },
    "Kuro": {
        "stats": {"power": 48, "durability": 40, "speed": 78, "utility": 50},
        "positions": {"Duelist": 0.7, "Traitor": 0.55},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["burst", "versatility"],
             "text": "Pés-Gato (garras) e velocidade fantasma — ataques tão rápidos que viram borrões imprecisos."},
        ],
    },
    "Krieg": {
        "stats": {"power": 50, "durability": 52, "speed": 40, "utility": 58},
        "positions": {"Duelist": 0.65, "Captain": 0.5},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["versatility", "burst", "aoe"],
             "text": "Armadura de Batalha cheia de armas traiçoeiras — rede de aço, bombas e gás venenoso."},
        ],
    },
    "Arlong": {
        "stats": {"power": 56, "durability": 60, "speed": 50, "utility": 48},
        "positions": {"Duelist": 0.7, "Tank": 0.6, "Captain": 0.5},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["bruiser", "durability"],
             "text": "Homem-peixe serra — mandíbula que serra metal e força física brutal, ainda maior na água."},
        ],
    },
    "Helmeppo": {
        "stats": {"power": 36, "durability": 34, "speed": 44, "utility": 40},
        "positions": {"Duelist": 0.5, "Support": 0.45},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["versatility"],
             "text": "Oficial da Marinha treinado por Garp — dois kukris e disciplina crescente."},
        ],
    },
    "Koby": {
        "stats": {"power": 48, "durability": 44, "speed": 58, "utility": 56},
        "positions": {"Duelist": 0.6, "Support": 0.6, "Vice Captain": 0.5},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["bruiser", "recon"],
             "text": "Marinheiro prodígio — Rokushiki e um Haki da Observação que ouve as vozes do campo de batalha."},
        ],
    },
    # ── Whitebeard / Roger / Shanks (lendas) ───────────────────────────────
    "Portgas D. Ace": {
        "stats": {"power": 84, "durability": 72, "speed": 78, "utility": 70},
        "positions": {"Duelist": 0.9, "Vice Captain": 0.78, "Captain": 0.6},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "conqueror"],
             "text": "Fruta da Chama (Logia) — comandante do Whitebeard que cobre o mar de fogo; porta o Haki do Rei."},
        ],
    },
    "Shanks": {
        "stats": {"power": 96, "durability": 90, "speed": 90, "utility": 92},
        "positions": {"Captain": 1.0, "Duelist": 0.92, "Vice Captain": 0.7},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["ace", "bruiser", "leadership", "conqueror"],
             "text": "Imperador do Mar — Haki do Rei tão denso que rasga o céu; presença que encerra guerras só com a chegada."},
        ],
    },
    "Uta": {
        "stats": {"power": 58, "durability": 40, "speed": 50, "utility": 78},
        "positions": {"Support": 0.85, "Duelist": 0.55},
        "abilities": [
            {"reveal": "egghead", "disclosure": "named",
             "tags": ["lockdown", "debuff", "aoe", "utility"],
             "text": "Fruta Canção — prende a consciência de quem ouve num mundo de canto e invoca o demônio Tot Musica."},
        ],
    },
    # ── Alabasta / Baroque Works ───────────────────────────────────────────
    "Nefertari Vivi": {
        "stats": {"power": 24, "durability": 24, "speed": 40, "utility": 56},
        "positions": {"Support": 0.7, "Captain": 0.45},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["leadership", "utility"],
             "text": "Princesa de Alabasta — Peacock Slashers e uma diplomacia que move reinos."},
        ],
    },
    "Crocodile": {
        "stats": {"power": 85, "durability": 70, "speed": 68, "utility": 80},
        "positions": {"Captain": 0.8, "Duelist": 0.85, "Support": 0.6, "Traitor": 0.55},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["ace", "aoe", "versatility", "debuff"],
             "text": "Fruta da Areia (Logia) — disseca a umidade do alvo e do ambiente; estrategista frio que comanda o Cross Guild."},
        ],
    },
    "Bentham": {
        "stats": {"power": 54, "durability": 48, "speed": 64, "utility": 66},
        "positions": {"Duelist": 0.68, "Support": 0.62},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["versatility", "utility", "bruiser"],
             "text": "Fruta Clone (Okama Kenpo) — copia o rosto e o corpo de qualquer um que tocou; balé de combate."},
        ],
    },
    "Daz Bonez": {
        "stats": {"power": 64, "durability": 62, "speed": 58, "utility": 48},
        "positions": {"Duelist": 0.75, "Tank": 0.6},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Fruta da Lâmina — transforma o corpo em aço cortante; assassino de elite da Baroque Works."},
        ],
    },
    "Chaka": {
        "stats": {"power": 58, "durability": 56, "speed": 60, "utility": 50},
        "positions": {"Duelist": 0.7, "Tank": 0.58, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["bruiser", "versatility"],
             "text": "Fruta Cão (Chacal) — guardião real de Alabasta, esgrima e instinto animal."},
        ],
    },
    "Pell": {
        "stats": {"power": 58, "durability": 56, "speed": 72, "utility": 52},
        "positions": {"Duelist": 0.7, "Support": 0.55},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["bruiser", "recon", "versatility"],
             "text": "Fruta Falcão — voa em alta velocidade; o guardião que carregou uma bomba para o céu."},
        ],
    },
    # ── Marinha (G-Quintet / capitães) ─────────────────────────────────────
    "Tashigi": {
        "stats": {"power": 52, "durability": 48, "speed": 58, "utility": 50},
        "positions": {"Duelist": 0.68, "Support": 0.5},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["bruiser", "versatility"],
             "text": "Espadachim da Marinha — perita em espadas amaldiçoadas e tática de captura."},
        ],
    },
    "Smoker": {
        "stats": {"power": 68, "durability": 64, "speed": 62, "utility": 62},
        "positions": {"Duelist": 0.78, "Tank": 0.6, "Captain": 0.55},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["ace", "lockdown", "versatility"],
             "text": "Fruta da Fumaça (Logia) — prende e arrasta alvos; bastão de Kairoseki contra usuários de fruta."},
        ],
    },
    # ── Skypiea ────────────────────────────────────────────────────────────
    "Enel": {
        "stats": {"power": 80, "durability": 66, "speed": 88, "utility": 78},
        "positions": {"Duelist": 0.82, "Captain": 0.6, "Support": 0.55},
        "abilities": [
            {"reveal": "skypiea", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "recon"],
             "text": "Fruta do Trovão (Logia) — 200 milhões de volts e Mantra (Observação) que prevê cada movimento."},
        ],
    },
    "Gan Fall": {
        "stats": {"power": 56, "durability": 54, "speed": 58, "utility": 56},
        "positions": {"Duelist": 0.66, "Support": 0.6, "Captain": 0.5},
        "abilities": [
            {"reveal": "skypiea", "disclosure": "full",
             "tags": ["bruiser", "versatility"],
             "text": "Cavaleiro do Céu — lança montado no pássaro Pierre e veterano experiente."},
        ],
    },
    "Mont Blanc Noland": {
        "stats": {"power": 40, "durability": 42, "speed": 44, "utility": 48},
        "positions": {"Duelist": 0.55, "Support": 0.5},
        "abilities": [
            {"reveal": "skypiea", "disclosure": "named",
             "tags": ["versatility", "leadership"],
             "text": "Explorador e guerreiro histórico — coragem que virou lenda (e provérbio)."},
        ],
    },
    "Kalgara": {
        "stats": {"power": 56, "durability": 54, "speed": 52, "utility": 44},
        "positions": {"Duelist": 0.66, "Tank": 0.55},
        "abilities": [
            {"reveal": "skypiea", "disclosure": "named",
             "tags": ["bruiser", "leadership"],
             "text": "Guerreiro de Shandia — bravura feroz e a Grande Serpente como aliada."},
        ],
    },
    "Ohm": {
        "stats": {"power": 54, "durability": 52, "speed": 56, "utility": 48},
        "positions": {"Duelist": 0.66, "Tank": 0.55},
        "abilities": [
            {"reveal": "skypiea", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Sacerdote de Skypiea — espada de Eisen (nuvem de ferro) que corta com fios invisíveis."},
        ],
    },
    "Shura": {
        "stats": {"power": 52, "durability": 48, "speed": 56, "utility": 46},
        "positions": {"Duelist": 0.64, "Support": 0.5},
        "abilities": [
            {"reveal": "skypiea", "disclosure": "full",
             "tags": ["burst", "aoe"],
             "text": "Sacerdote de Skypiea — fogo montado no pássaro Fuza, ordálio das chamas."},
        ],
    },
    "Satori": {
        "stats": {"power": 52, "durability": 48, "speed": 54, "utility": 52},
        "positions": {"Duelist": 0.62, "Support": 0.52},
        "abilities": [
            {"reveal": "skypiea", "disclosure": "full",
             "tags": ["burst", "recon"],
             "text": "Sacerdote de Skypiea — Mantra e bolas-surpresa explosivas, o ordálio das esferas."},
        ],
    },
    "Holy": {
        "stats": {"power": 50, "durability": 50, "speed": 50, "utility": 44},
        "positions": {"Duelist": 0.6, "Tank": 0.5},
        "abilities": [
            {"reveal": "skypiea", "disclosure": "named",
             "tags": ["bruiser"],
             "text": "Combatente de Skypiea — força de classe sacerdotal nas ilhas do céu."},
        ],
    },
    # ── Water 7 / Enies Lobby (CP9) ────────────────────────────────────────
    "Iceburg": {
        "stats": {"power": 24, "durability": 28, "speed": 36, "utility": 64},
        "positions": {"Support": 0.72, "Captain": 0.45},
        "abilities": [
            {"reveal": "water7", "disclosure": "full",
             "tags": ["utility", "leadership"],
             "text": "Prefeito e mestre-naval de Water 7 — engenharia genial e liderança política."},
        ],
    },
    "Rob Lucci": {
        "stats": {"power": 85, "durability": 76, "speed": 82, "utility": 64},
        "positions": {"Duelist": 0.92, "Vice Captain": 0.66, "Traitor": 0.5},
        "abilities": [
            {"reveal": "water7", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst"],
             "text": "Fruta Gato-Leopardo + Rokushiki mestre — Rokuougan e, despertado, agente mais letal do CP0."},
        ],
    },
    "Kaku": {
        "stats": {"power": 74, "durability": 62, "speed": 70, "utility": 58},
        "positions": {"Duelist": 0.82, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "water7", "disclosure": "full",
             "tags": ["bruiser", "burst", "versatility"],
             "text": "Fruta Girafa + Rokushiki — esgrima de Tempestade e Rankyaku cortante."},
        ],
    },
    "Kalifa": {
        "stats": {"power": 58, "durability": 48, "speed": 60, "utility": 60},
        "positions": {"Support": 0.7, "Duelist": 0.6},
        "abilities": [
            {"reveal": "water7", "disclosure": "full",
             "tags": ["debuff", "lockdown", "utility"],
             "text": "Fruta da Bolha — ensaboa o alvo e rouba sua força, deixando-o escorregadio e impotente."},
        ],
    },
    "Blueno": {
        "stats": {"power": 66, "durability": 58, "speed": 60, "utility": 66},
        "positions": {"Duelist": 0.72, "Support": 0.6},
        "abilities": [
            {"reveal": "water7", "disclosure": "full",
             "tags": ["versatility", "utility", "burst"],
             "text": "Fruta da Porta — abre portais em qualquer superfície (e no ar) para flanquear e escapar."},
        ],
    },
    "Jabra": {
        "stats": {"power": 72, "durability": 62, "speed": 68, "utility": 54},
        "positions": {"Duelist": 0.8, "Tank": 0.58},
        "abilities": [
            {"reveal": "water7", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Fruta Lobo + Rokushiki — Tekkai férreo e mordidas que rasgam aço."},
        ],
    },
    "Spandam": {
        "stats": {"power": 28, "durability": 30, "speed": 36, "utility": 44},
        "positions": {"Traitor": 0.7, "Support": 0.45},
        "abilities": [
            {"reveal": "water7", "disclosure": "full",
             "tags": ["sabotage", "betrayal", "manipulation"],
             "text": "Chefe covarde do CP9 — espada-elefante Funkfreed e poder político para tramar pelas costas."},
        ],
    },
    # ── Thriller Bark ──────────────────────────────────────────────────────
    "Gecko Moria": {
        "stats": {"power": 76, "durability": 64, "speed": 50, "utility": 82},
        "positions": {"Captain": 0.7, "Support": 0.72, "Duelist": 0.66},
        "abilities": [
            {"reveal": "thriller_bark", "disclosure": "full",
             "tags": ["versatility", "utility", "aoe"],
             "text": "Fruta da Sombra — rouba sombras e monta um exército de zumbis; Shadow's Asgard gigante."},
        ],
    },
    "Absalom": {
        "stats": {"power": 60, "durability": 58, "speed": 56, "utility": 66},
        "positions": {"Duelist": 0.68, "Support": 0.62, "Traitor": 0.5},
        "abilities": [
            {"reveal": "thriller_bark", "disclosure": "full",
             "tags": ["versatility", "recon", "burst"],
             "text": "Fruta da Invisibilidade — ataca sem ser visto; comanda os experimentos de Hogback."},
        ],
    },
    "Perona": {
        "stats": {"power": 44, "durability": 36, "speed": 48, "utility": 70},
        "positions": {"Support": 0.8, "Duelist": 0.45},
        "abilities": [
            {"reveal": "thriller_bark", "disclosure": "full",
             "tags": ["debuff", "lockdown", "utility"],
             "text": "Fruta dos Fantasmas — Hollows Negativos que afundam o alvo em depressão paralisante; corpo astral intangível."},
        ],
    },
    "Hogback": {
        "stats": {"power": 30, "durability": 34, "speed": 38, "utility": 62},
        "positions": {"Support": 0.7, "Healer": 0.5},
        "abilities": [
            {"reveal": "thriller_bark", "disclosure": "full",
             "tags": ["utility", "heal"],
             "text": "Cirurgião genial e macabro — remenda corpos e ergue zumbis de combate."},
        ],
    },
    "Shimotsuki Ryuma": {
        "stats": {"power": 78, "durability": 66, "speed": 70, "utility": 50},
        "positions": {"Duelist": 0.9, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "thriller_bark", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst"],
             "text": "Lenda da espada de Wano — o samurai que teria abatido um dragão; cortes que fendem o ar."},
        ],
    },
    "Oars": {
        "stats": {"power": 78, "durability": 84, "speed": 40, "utility": 40},
        "positions": {"Tank": 0.85, "Duelist": 0.7},
        "abilities": [
            {"reveal": "thriller_bark", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser", "aoe"],
             "text": "Demônio Ancião — gigante colossal de força esmagadora e resistência absurda."},
        ],
    },
    # ── Marineford — Whitebeard Pirates ────────────────────────────────────
    "Edward Newgate": {
        "stats": {"power": 99, "durability": 95, "speed": 72, "utility": 86},
        "positions": {"Captain": 1.0, "Duelist": 0.92, "Tank": 0.85, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "tank", "durability", "conqueror"],
             "text": "Fruta do Tremor — racha o ar e o mar com terremotos; o Homem Mais Forte do Mundo, mesmo ferido, segura uma guerra inteira."},
        ],
    },
    "Marco": {
        "stats": {"power": 84, "durability": 88, "speed": 80, "utility": 82},
        "positions": {"Vice Captain": 0.85, "Healer": 0.75, "Duelist": 0.82, "Tank": 0.8},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["heal", "sustain", "tank", "durability", "bruiser"],
             "text": "Fruta Fênix (Zoan mítica) — chamas azuis que regeneram o próprio corpo e curam aliados; comandante e médico do bando."},
        ],
    },
    "Jozu": {
        "stats": {"power": 80, "durability": 88, "speed": 56, "utility": 50},
        "positions": {"Tank": 0.9, "Duelist": 0.75},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser", "guard"],
             "text": "Fruta do Diamante — corpo de diamante que para ataques de Almirante e arremessa icebergs."},
        ],
    },
    "Vista": {
        "stats": {"power": 78, "durability": 70, "speed": 74, "utility": 54},
        "positions": {"Duelist": 0.86, "Vice Captain": 0.62},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["bruiser", "burst", "ace"],
             "text": "Espadachim Florido — duas espadas que trocam golpes de igual com Mihawk por instantes."},
        ],
    },
    "Sengoku": {
        "stats": {"power": 90, "durability": 84, "speed": 70, "utility": 82},
        "positions": {"Captain": 0.85, "Duelist": 0.82, "Tank": 0.72},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "aoe", "leadership", "bruiser"],
             "text": "Fruta Humano-Buda (Zoan mítica) — forma dourada gigante e ondas de choque; mente estratégica de Almirante-de-Frota."},
        ],
    },
    "Monkey D. Garp": {
        "stats": {"power": 95, "durability": 90, "speed": 80, "utility": 76},
        "positions": {"Captain": 0.85, "Duelist": 0.92, "Tank": 0.8, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "conqueror"],
             "text": "Punho do Herói — Haki do Armamento tão denso que seus socos rivalizam com balas de canhão; encurralou Roger e Rocks."},
        ],
    },
    "Boa Hancock": {
        "stats": {"power": 85, "durability": 70, "speed": 76, "utility": 80},
        "positions": {"Duelist": 0.85, "Captain": 0.7, "Support": 0.62},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "lockdown", "debuff", "conqueror"],
             "text": "Fruta do Amor — petrifica quem sente atração e dispara chutes de Haki; Imperatriz com Haki do Rei."},
        ],
    },
    "Shirahoshi": {
        "stats": {"power": 20, "durability": 40, "speed": 30, "utility": 70},
        "positions": {"Support": 0.6},
        "abilities": [
            {"reveal": "fishman", "disclosure": "named",
             "tags": ["utility"],
             "text": "Princesa Sereia — uma das Armas Ancestrais (Poseidon): comanda os Reis do Mar, mas é uma civil indefesa."},
        ],
    },
    "Silvers Rayleigh": {
        "stats": {"power": 92, "durability": 84, "speed": 82, "utility": 88},
        "positions": {"Vice Captain": 0.9, "Duelist": 0.9, "Captain": 0.78},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "bruiser", "leadership", "conqueror"],
             "text": "Rei das Trevas — braço-direito de Roger; mestre dos três Haki, ainda capaz de deter um Almirante."},
        ],
    },
    # ── Marinha — Almirantes & Frota ───────────────────────────────────────
    "Sakazuki": {
        "stats": {"power": 95, "durability": 86, "speed": 80, "utility": 80},
        "positions": {"Captain": 0.85, "Duelist": 0.95, "Tank": 0.7},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "burst", "aoe"],
             "text": "Fruta do Magma (Logia) — magma que supera o fogo em calor e destruição; Almirante-de-Frota implacável (Justiça Absoluta)."},
        ],
    },
    "Borsalino": {
        "stats": {"power": 94, "durability": 82, "speed": 99, "utility": 80},
        "positions": {"Captain": 0.78, "Duelist": 0.95},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "burst", "aoe"],
             "text": "Fruta da Luz (Logia) — move-se e ataca à velocidade da luz com chutes e raios laser."},
        ],
    },
    "Kuzan": {
        "stats": {"power": 92, "durability": 82, "speed": 78, "utility": 84},
        "positions": {"Duelist": 0.92, "Captain": 0.72, "Tank": 0.7, "Traitor": 0.5},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "lockdown", "aoe", "versatility"],
             "text": "Fruta do Gelo (Logia) — congela mares inteiros e aprisiona alvos; ex-Almirante de moral ambígua."},
        ],
    },
    "Issho": {
        "stats": {"power": 93, "durability": 82, "speed": 76, "utility": 86},
        "positions": {"Duelist": 0.92, "Captain": 0.75, "Tank": 0.72},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["ace", "aoe", "lockdown", "versatility"],
             "text": "Fruta da Gravidade — puxa meteoros do céu e altera o peso do campo; Almirante cego que enxerga por Haki."},
        ],
    },
    "Aramaki": {
        "stats": {"power": 92, "durability": 84, "speed": 74, "utility": 80},
        "positions": {"Duelist": 0.9, "Captain": 0.72, "Tank": 0.72},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["ace", "aoe", "sustain", "debuff"],
             "text": "Fruta da Floresta — faz brotar uma selva que drena a vida dos inimigos e alimenta a sua; Almirante."},
        ],
    },
    "Sentomaru": {
        "stats": {"power": 70, "durability": 72, "speed": 56, "utility": 58},
        "positions": {"Tank": 0.8, "Duelist": 0.68, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["tank", "guard", "bruiser", "durability"],
             "text": "Guarda-costas de Vegapunk — Haki do Armamento defensivo de elite e um machado colossal."},
        ],
    },
    # ── Fishman / aliados Mink ─────────────────────────────────────────────
    "Inuarashi": {
        "stats": {"power": 80, "durability": 72, "speed": 78, "utility": 64},
        "positions": {"Duelist": 0.85, "Captain": 0.66, "Vice Captain": 0.62},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["bruiser", "burst", "leadership"],
             "text": "Duque do Dia — mink-cão mestre em esgrima; na forma Sulong, sob a lua cheia, multiplica sua força."},
        ],
    },
    "Nekomamushi": {
        "stats": {"power": 80, "durability": 72, "speed": 82, "utility": 62},
        "positions": {"Duelist": 0.85, "Captain": 0.66, "Vice Captain": 0.62},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["bruiser", "burst", "leadership"],
             "text": "Mestre da Noite — mink-gato de garras relâmpago; Sulong libera potência devastadora."},
        ],
    },
    "Carrot": {
        "stats": {"power": 62, "durability": 54, "speed": 76, "utility": 56},
        "positions": {"Duelist": 0.7, "Support": 0.55},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["burst", "versatility"],
             "text": "Mink-coelha elétrica — saltos relâmpago e, em Sulong, golpes de força brutal."},
        ],
    },
    "Pedro": {
        "stats": {"power": 68, "durability": 60, "speed": 70, "utility": 58},
        "positions": {"Duelist": 0.76, "Vice Captain": 0.58},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["bruiser", "burst", "ace"],
             "text": "Guardião da Floresta — mink-jaguar e espadachim que aposta a própria vida pelo futuro."},
        ],
    },
    "Bepo": {
        "stats": {"power": 60, "durability": 56, "speed": 64, "utility": 54},
        "positions": {"Duelist": 0.68, "Support": 0.52, "Vice Captain": 0.5},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["bruiser", "versatility"],
             "text": "Mink-urso navegador dos Heart Pirates — Kung Fu eletrificado, mais forte sob a lua cheia."},
        ],
    },
    # ── Dressrosa — Família Doflamingo ─────────────────────────────────────
    "Donquixote Doflamingo": {
        "stats": {"power": 88, "durability": 76, "speed": 80, "utility": 86},
        "positions": {"Captain": 0.88, "Duelist": 0.9, "Support": 0.6, "Traitor": 0.6},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["ace", "lockdown", "versatility", "manipulation", "conqueror"],
             "text": "Fruta dos Fios — cortes e marionetes à distância, gaiola-pássaro que cerca cidades; mente manipuladora com Haki do Rei."},
        ],
    },
    "Donquixote Rosinante": {
        "stats": {"power": 52, "durability": 50, "speed": 54, "utility": 70},
        "positions": {"Support": 0.78, "Traitor": 0.55, "Duelist": 0.5},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["utility", "debuff", "betrayal"],
             "text": "Fruta da Calmaria — cria um campo de silêncio absoluto que abafa todo som; agente infiltrado de bom coração."},
        ],
    },
    "Rebecca": {
        "stats": {"power": 38, "durability": 34, "speed": 56, "utility": 44},
        "positions": {"Duelist": 0.58, "Support": 0.5},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["versatility", "guard"],
             "text": "Gladiadora que nunca fere — esquiva impecável e espada defensiva."},
        ],
    },
    "Kyros": {
        "stats": {"power": 74, "durability": 66, "speed": 72, "utility": 50},
        "positions": {"Duelist": 0.85, "Vice Captain": 0.58},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst"],
             "text": "Lenda dos gladiadores — invicto em mil lutas; um único corte derruba até um executivo."},
        ],
    },
    "Diamante": {
        "stats": {"power": 74, "durability": 68, "speed": 62, "utility": 58},
        "positions": {"Duelist": 0.8, "Tank": 0.62},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["bruiser", "versatility"],
             "text": "Fruta Flutter — torna o próprio corpo e objetos maleáveis como tecido, desviando golpes."},
        ],
    },
    "Trebol": {
        "stats": {"power": 70, "durability": 72, "speed": 40, "utility": 64},
        "positions": {"Tank": 0.75, "Support": 0.6, "Duelist": 0.6},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["tank", "lockdown", "aoe"],
             "text": "Fruta da Cola — prende o alvo num lodo grudento e o explode; conselheiro do trono."},
        ],
    },
    "Pica": {
        "stats": {"power": 78, "durability": 80, "speed": 50, "utility": 60},
        "positions": {"Tank": 0.85, "Duelist": 0.72},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["tank", "durability", "aoe", "lockdown"],
             "text": "Fruta da Pedra — funde-se à rocha e move montanhas como golem colossal do terreno."},
        ],
    },
    "Senor Pink": {
        "stats": {"power": 66, "durability": 70, "speed": 52, "utility": 50},
        "positions": {"Tank": 0.78, "Duelist": 0.66},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Fruta do Nado — mergulha no chão como se fosse água e ressurge para golpear; durão sentimental."},
        ],
    },
    "Sugar": {
        "stats": {"power": 30, "durability": 24, "speed": 38, "utility": 82},
        "positions": {"Support": 0.85, "Traitor": 0.55},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["debuff", "lockdown", "manipulation", "utility"],
             "text": "Fruta do Brinquedo — transforma qualquer um em brinquedo ao toque e apaga sua existência da memória de todos."},
        ],
    },
    "Vergo": {
        "stats": {"power": 76, "durability": 78, "speed": 66, "utility": 58},
        "positions": {"Tank": 0.82, "Duelist": 0.76, "Traitor": 0.72},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser", "betrayal"],
             "text": "Haki do Armamento por todo o corpo — bambu indestrutível; mole infiltrado na Marinha e no G-5."},
        ],
    },
    "Monet": {
        "stats": {"power": 60, "durability": 54, "speed": 56, "utility": 66},
        "positions": {"Support": 0.7, "Duelist": 0.58, "Traitor": 0.62},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["versatility", "lockdown", "betrayal", "recon"],
             "text": "Fruta da Neve (Logia) — nevascas e prisões de gelo; espiã leal e fria de Doflamingo."},
        ],
    },
    "Caesar Clown": {
        "stats": {"power": 70, "durability": 56, "speed": 58, "utility": 78},
        "positions": {"Support": 0.74, "Duelist": 0.66, "Traitor": 0.66},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["ace", "aoe", "debuff", "sabotage", "versatility"],
             "text": "Fruta do Gás (Logia) — gases venenosos e explosivos e remoção de oxigênio; cientista sem escrúpulos."},
        ],
    },
    "Baby 5": {
        "stats": {"power": 56, "durability": 50, "speed": 54, "utility": 64},
        "positions": {"Duelist": 0.66, "Support": 0.6},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["versatility", "burst", "aoe"],
             "text": "Fruta da Arma — transforma qualquer parte do corpo em armas (de foice a canhão)."},
        ],
    },
    "Buffalo": {
        "stats": {"power": 54, "durability": 52, "speed": 58, "utility": 50},
        "positions": {"Duelist": 0.62, "Support": 0.55},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["versatility", "recon"],
             "text": "Fruta da Rotação — gira o corpo como hélice para voar e transportar aliados."},
        ],
    },
    "Brownbeard": {
        "stats": {"power": 50, "durability": 56, "speed": 48, "utility": 44},
        "positions": {"Tank": 0.6, "Duelist": 0.55},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["tank", "bruiser"],
             "text": "Centauro pirata — corpo híbrido robusto e cavalaria pesada."},
        ],
    },
    "Bellamy": {
        "stats": {"power": 58, "durability": 52, "speed": 64, "utility": 46},
        "positions": {"Duelist": 0.66},
        "abilities": [
            {"reveal": "skypiea", "disclosure": "full",
             "tags": ["burst", "bruiser"],
             "text": "Fruta da Mola — comprime e dispara o corpo como projétil saltitante (Spring Snipe)."},
        ],
    },
    "Dellinger": {
        "stats": {"power": 60, "durability": 54, "speed": 68, "utility": 46},
        "positions": {"Duelist": 0.7},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["burst", "bruiser"],
             "text": "Híbrido homem-peixe (peixe-lutador) — sede de sangue e chutes ferozes em alta velocidade."},
        ],
    },
    "Mansherry": {
        "stats": {"power": 18, "durability": 22, "speed": 40, "utility": 86},
        "positions": {"Healer": 1.0, "Support": 0.6},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["heal", "revive", "sustain"],
             "text": "Fruta da Cura — lágrimas que restauram ferimentos e estruturas quase instantaneamente, ao custo da própria energia."},
        ],
    },
    "Leo": {
        "stats": {"power": 44, "durability": 38, "speed": 56, "utility": 64},
        "positions": {"Support": 0.7, "Duelist": 0.5},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["utility", "lockdown"],
             "text": "Fruta da Costura — costura objetos e pessoas ao cenário, prendendo-os no lugar; líder Tontatta."},
        ],
    },
    "Bartolomeo": {
        "stats": {"power": 66, "durability": 74, "speed": 54, "utility": 64},
        "positions": {"Tank": 0.85, "Support": 0.6, "Duelist": 0.58},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["tank", "guard", "lockdown", "durability"],
             "text": "Fruta da Barreira — paredes invisíveis impenetráveis para defender ou prensar inimigos."},
        ],
    },
    "Cavendish": {
        "stats": {"power": 72, "durability": 60, "speed": 78, "utility": 52},
        "positions": {"Duelist": 0.85, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["bruiser", "burst", "ace"],
             "text": "Esgrima refinada e, quando dorme, a personalidade Hakuba — velocidade letal e incontrolável."},
        ],
    },
    # ── Whole Cake Island — Big Mom Pirates ────────────────────────────────
    "Charlotte Linlin": {
        "stats": {"power": 96, "durability": 94, "speed": 70, "utility": 84},
        "positions": {"Captain": 0.95, "Duelist": 0.92, "Tank": 0.85},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["ace", "aoe", "burst", "tank", "durability", "conqueror"],
             "text": "Fruta da Alma — rouba o tempo de vida de quem a teme e o injeta em Prometheus, Zeus e Napoleon; Imperatriz quase indestrutível."},
        ],
    },
    "Charlotte Katakuri": {
        "stats": {"power": 90, "durability": 84, "speed": 82, "utility": 78},
        "positions": {"Duelist": 0.95, "Vice Captain": 0.82, "Tank": 0.72, "Captain": 0.62},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "lockdown", "conqueror"],
             "text": "Fruta do Mochi — molda mochi para atacar e se esquivar; Observação avançada que enxerga o futuro próximo."},
        ],
    },
    "Charlotte Smoothie": {
        "stats": {"power": 80, "durability": 70, "speed": 64, "utility": 66},
        "positions": {"Duelist": 0.82, "Tank": 0.66},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["bruiser", "debuff", "aoe"],
             "text": "Fruta do Espremer — drena o líquido de qualquer coisa viva e cresce gigantesca de força."},
        ],
    },
    "Charlotte Cracker": {
        "stats": {"power": 80, "durability": 82, "speed": 66, "utility": 64},
        "positions": {"Duelist": 0.82, "Tank": 0.8},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["tank", "guard", "bruiser", "lockdown"],
             "text": "Fruta do Biscoito — exército infinito de soldados de biscoito e uma armadura que parece imbatível."},
        ],
    },
    "Charlotte Perospero": {
        "stats": {"power": 72, "durability": 70, "speed": 56, "utility": 72},
        "positions": {"Tank": 0.76, "Support": 0.66, "Duelist": 0.62, "Traitor": 0.5},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["lockdown", "tank", "versatility", "aoe"],
             "text": "Fruta do Doce — modela balas de açúcar para prender, blindar e erguer estruturas."},
        ],
    },
    "Charlotte Pudding": {
        "stats": {"power": 50, "durability": 40, "speed": 52, "utility": 74},
        "positions": {"Support": 0.78, "Traitor": 0.66},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["manipulation", "utility", "betrayal", "recon"],
             "text": "Fruta da Memória — apaga e reescreve lembranças; o terceiro olho que lê Poneglyphs."},
        ],
    },
    # ── Germa 66 — Vinsmoke ────────────────────────────────────────────────
    "Vinsmoke Reiju": {
        "stats": {"power": 70, "durability": 66, "speed": 70, "utility": 68},
        "positions": {"Duelist": 0.74, "Healer": 0.6, "Support": 0.6},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["bruiser", "heal", "debuff"],
             "text": "Veneno Rosa — absorve e neutraliza toxinas (curando aliados); Raid Suit que reforça o corpo."},
        ],
    },
    "Vinsmoke Ichiji": {
        "stats": {"power": 74, "durability": 70, "speed": 72, "utility": 56},
        "positions": {"Duelist": 0.8, "Vice Captain": 0.58},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["bruiser", "burst", "aoe"],
             "text": "Sparking Red — Raid Suit com corpo modificado e rajadas incendiárias."},
        ],
    },
    "Vinsmoke Niji": {
        "stats": {"power": 74, "durability": 68, "speed": 74, "utility": 56},
        "positions": {"Duelist": 0.8, "Support": 0.55},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Electric Blue — Raid Suit que descarrega eletricidade em alta velocidade."},
        ],
    },
    "Vinsmoke Yonji": {
        "stats": {"power": 72, "durability": 72, "speed": 64, "utility": 52},
        "positions": {"Tank": 0.7, "Duelist": 0.72},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["tank", "bruiser", "durability"],
             "text": "Winch Green — Raid Suit de força bruta e estrutura reforçada."},
        ],
    },
    # ── Wano — Beasts Pirates & samurais ───────────────────────────────────
    "Kaidou": {
        "stats": {"power": 99, "durability": 98, "speed": 76, "utility": 80},
        "positions": {"Captain": 0.95, "Duelist": 0.95, "Tank": 0.92},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["ace", "aoe", "burst", "tank", "durability", "conqueror"],
             "text": "Fruta Dragão Azul (Zoan mítica) — a Criatura Mais Forte do Mundo; bastão Conqueror e Bolides que arrasam ilhas."},
        ],
    },
    "Kouzuki Oden": {
        "stats": {"power": 90, "durability": 82, "speed": 80, "utility": 70},
        "positions": {"Captain": 0.82, "Duelist": 0.92, "Vice Captain": 0.7},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "conqueror"],
             "text": "Estilo de Duas Espadas (Oden Nitoryu) — Tougen e Toguro; o único a ferir Kaidou, com Haki do Rei."},
        ],
    },
    "Kouzuki Momonosuke": {
        "stats": {"power": 40, "durability": 50, "speed": 48, "utility": 56},
        "positions": {"Support": 0.55, "Tank": 0.5, "Captain": 0.45},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["versatility", "leadership"],
             "text": "Pode assumir a forma de um dragão artificial colossal; herdeiro de Wano amadurecendo na liderança."},
        ],
    },
    "Yamato": {
        "stats": {"power": 87, "durability": 82, "speed": 78, "utility": 70},
        "positions": {"Duelist": 0.9, "Tank": 0.78, "Vice Captain": 0.72, "Captain": 0.6},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "tank", "conqueror"],
             "text": "Fruta Lobo-Divino (Okuchi no Makami) — gelo sagrado e força que troca golpes com Kaidou; porta o Haki do Rei."},
        ],
    },
    "Kin'emon": {
        "stats": {"power": 68, "durability": 60, "speed": 62, "utility": 60},
        "positions": {"Duelist": 0.76, "Vice Captain": 0.62, "Captain": 0.55},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["bruiser", "burst", "versatility", "leadership"],
             "text": "Estilo da Raposa de Fogo — corta as próprias chamas do inimigo e as devolve; líder dos Nove Bainhas Vermelhas."},
        ],
    },
    "Denjiro": {
        "stats": {"power": 72, "durability": 64, "speed": 68, "utility": 56},
        "positions": {"Duelist": 0.8, "Vice Captain": 0.62},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["bruiser", "burst", "ace"],
             "text": "Saque relâmpago (Iai) — espadachim dos Nove Bainhas cujo corte some antes de ser visto."},
        ],
    },
    "Raizo": {
        "stats": {"power": 56, "durability": 54, "speed": 60, "utility": 66},
        "positions": {"Support": 0.7, "Duelist": 0.58},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["utility", "versatility", "recon"],
             "text": "Ninja de Wano — artes ninja com pergaminhos e técnicas de água e fumaça."},
        ],
    },
    "Kikunojo": {
        "stats": {"power": 68, "durability": 58, "speed": 70, "utility": 52},
        "positions": {"Duelist": 0.78, "Vice Captain": 0.58},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Esgrima de neve dos Nove Bainhas — cortes elegantes e devastadores com uma só lâmina."},
        ],
    },
    "King": {
        "stats": {"power": 86, "durability": 86, "speed": 78, "utility": 64},
        "positions": {"Duelist": 0.9, "Vice Captain": 0.78, "Tank": 0.8},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "tank", "durability"],
             "text": "Lunariano — pode acender chamas no corpo que o tornam quase intocável; Zoan de pteranodonte e braço-direito de Kaidou."},
        ],
    },
    "Queen": {
        "stats": {"power": 82, "durability": 80, "speed": 66, "utility": 74},
        "positions": {"Duelist": 0.82, "Tank": 0.76, "Support": 0.6},
        "abilities": [
            {"reveal": "wano", "disclosure": "full",
             "tags": ["bruiser", "aoe", "debuff", "versatility", "tank"],
             "text": "Ciborgue e Zoan de braquiossauro — armas embutidas, vírus Ice Oni e força bruta; cientista dos Beasts."},
        ],
    },
    "Jack": {
        "stats": {"power": 80, "durability": 84, "speed": 60, "utility": 50},
        "positions": {"Tank": 0.85, "Duelist": 0.76},
        "abilities": [
            {"reveal": "zou_wci", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser", "aoe"],
             "text": "Fruta Mamute (Zoan ancestral) — investidas colossais e resistência que ignora punições; a Seca dos Beasts."},
        ],
    },
    # ── Egghead — Vegapunk & Marinha moderna ───────────────────────────────
    "Vegapunk": {
        "stats": {"power": 26, "durability": 30, "speed": 34, "utility": 95},
        "positions": {"Support": 0.92, "Captain": 0.5},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["utility", "versatility", "recon"],
             "text": "Mente do século — a maior inteligência do mundo; tecnologia que move 500 anos à frente, mas corpo de cientista."},
        ],
    },
    "Vegapunk Shaka": {
        "stats": {"power": 52, "durability": 48, "speed": 50, "utility": 80},
        "positions": {"Support": 0.82, "Duelist": 0.55},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["utility", "recon", "versatility", "burst"],
             "text": "Satélite 'Bem' — a razão de Vegapunk; lógica fria, armamento de defesa e análise tática."},
        ],
    },
    "Vegapunk Lilith": {
        "stats": {"power": 48, "durability": 44, "speed": 50, "utility": 76},
        "positions": {"Support": 0.8, "Duelist": 0.52},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["utility", "versatility", "burst"],
             "text": "Satélite 'Maldade' — a ganância; manipula recursos e dispara o armamento do laboratório."},
        ],
    },
    "Vegapunk Edison": {
        "stats": {"power": 36, "durability": 34, "speed": 40, "utility": 82},
        "positions": {"Support": 0.85},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["utility", "versatility", "recon"],
             "text": "Satélite 'Pensamento' — gera invenções a jato; o motor criativo de Egghead."},
        ],
    },
    "Vegapunk Pythagoras": {
        "stats": {"power": 30, "durability": 32, "speed": 36, "utility": 84},
        "positions": {"Support": 0.85},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["utility", "recon"],
             "text": "Satélite 'Sabedoria' — cálculo e medição perfeitos; quantifica tudo no campo."},
        ],
    },
    "Vegapunk Atlas": {
        "stats": {"power": 58, "durability": 54, "speed": 56, "utility": 70},
        "positions": {"Duelist": 0.62, "Support": 0.72, "Tank": 0.55},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["burst", "versatility", "utility"],
             "text": "Satélite 'Violência' — a mais combativa; punho mecânico e equipamento de demolição."},
        ],
    },
    "Vegapunk York": {
        "stats": {"power": 28, "durability": 34, "speed": 34, "utility": 64},
        "positions": {"Support": 0.66, "Traitor": 0.6},
        "abilities": [
            {"reveal": "egghead", "disclosure": "named",
             "tags": ["utility", "betrayal", "sabotage"],
             "text": "Satélite 'Desejo' — a ambição que se volta contra o próprio criador."},
        ],
    },
    "Stussy": {
        "stats": {"power": 66, "durability": 58, "speed": 64, "utility": 70},
        "positions": {"Support": 0.7, "Duelist": 0.68, "Traitor": 0.7},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["versatility", "betrayal", "recon", "debuff"],
             "text": "Agente do CP0 e clone de elite — sopro sônico que desfaz tecidos; agente dupla de fina infiltração."},
        ],
    },
    "S-Bear": {
        "stats": {"power": 84, "durability": 84, "speed": 70, "utility": 70},
        "positions": {"Duelist": 0.85, "Tank": 0.82, "Support": 0.55},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["ace", "burst", "tank", "durability", "versatility"],
             "text": "Serafim (clone de Kuma) — corpo lunariano blindado e a Fruta da Pata: repele ar, dor e ataques como projéteis."},
        ],
    },
    "S-Hawk": {
        "stats": {"power": 86, "durability": 82, "speed": 76, "utility": 58},
        "positions": {"Duelist": 0.9, "Tank": 0.78},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "durability"],
             "text": "Serafim (clone de Mihawk) — corpo lunariano e lâmina que dispara cortes voadores devastadores."},
        ],
    },
    "S-Shark": {
        "stats": {"power": 84, "durability": 84, "speed": 72, "utility": 56},
        "positions": {"Duelist": 0.85, "Tank": 0.82},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["ace", "bruiser", "tank", "durability"],
             "text": "Serafim (clone de Jinbe) — corpo lunariano e Karatê Homem-Peixe que golpeia a própria água."},
        ],
    },
    "S-Snake": {
        "stats": {"power": 82, "durability": 80, "speed": 74, "utility": 68},
        "positions": {"Duelist": 0.84, "Tank": 0.78, "Support": 0.55},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["ace", "lockdown", "debuff", "durability"],
             "text": "Serafim (clone de Hancock) — corpo lunariano e o olhar Medusa que petrifica quem mira, sem precisar de atração."},
        ],
    },
    # ── Worst Generation (Supernovas) ──────────────────────────────────────
    "Trafalgar D. Water Law": {
        "stats": {"power": 84, "durability": 68, "speed": 76, "utility": 92},
        "positions": {"Captain": 0.78, "Duelist": 0.85, "Support": 0.78, "Healer": 0.6},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "versatility", "utility", "burst", "lockdown"],
             "text": "Fruta da Operação — dentro do 'Room' reposiciona, corta e reorganiza tudo; Gamma Knife e cirurgia de elite. Desperta o Puncture Wille."},
        ],
    },
    "Eustass Kid": {
        "stats": {"power": 86, "durability": 78, "speed": 64, "utility": 70},
        "positions": {"Captain": 0.78, "Duelist": 0.86, "Tank": 0.66},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "bruiser", "conqueror"],
             "text": "Fruta do Magnetismo — atrai metais para montar punhos e canhões colossais (Damned Punk); porta o Haki do Rei."},
        ],
    },
    "Killer": {
        "stats": {"power": 72, "durability": 66, "speed": 76, "utility": 54},
        "positions": {"Duelist": 0.82, "Vice Captain": 0.66},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["bruiser", "burst", "ace"],
             "text": "Massacre Soldier — foices rotativas em alta velocidade; braço-direito de Kid."},
        ],
    },
    "Basil Hawkins": {
        "stats": {"power": 70, "durability": 64, "speed": 60, "utility": 78},
        "positions": {"Support": 0.74, "Duelist": 0.7, "Tank": 0.6},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["versatility", "guard", "utility", "lockdown"],
             "text": "Fruta da Palha — bonecos vodu que transferem o dano recebido a outras pessoas; cartas que preveem probabilidades."},
        ],
    },
    "Scratchmen Apoo": {
        "stats": {"power": 70, "durability": 60, "speed": 64, "utility": 72},
        "positions": {"Support": 0.72, "Duelist": 0.7, "Traitor": 0.55},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["burst", "aoe", "debuff", "versatility"],
             "text": "Fruta do Som — transforma sons em ataques explosivos diretos no corpo do alvo."},
        ],
    },
    "X Drake": {
        "stats": {"power": 74, "durability": 72, "speed": 64, "utility": 64},
        "positions": {"Duelist": 0.8, "Tank": 0.68, "Traitor": 0.62},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["bruiser", "tank", "durability", "betrayal"],
             "text": "Fruta Alossauro (Zoan ancestral) — mordida e couraça pré-histórica; agente secreto do SWORD infiltrado."},
        ],
    },
    "Jewelry Bonney": {
        "stats": {"power": 48, "durability": 42, "speed": 50, "utility": 78},
        "positions": {"Support": 0.78, "Duelist": 0.52},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["debuff", "manipulation", "utility", "versatility"],
             "text": "Fruta da Idade — altera a idade de si e dos outros, envelhecendo ou rejuvenescendo o alvo em combate."},
        ],
    },
    "Capone Bege": {
        "stats": {"power": 64, "durability": 80, "speed": 50, "utility": 80},
        "positions": {"Tank": 0.82, "Support": 0.74, "Captain": 0.6, "Traitor": 0.66},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["tank", "guard", "utility", "versatility", "betrayal"],
             "text": "Fruta do Castelo — abriga um exército e uma fortaleza inteira dentro do corpo (Big Father); mafioso calculista."},
        ],
    },
    "Urouge": {
        "stats": {"power": 72, "durability": 70, "speed": 58, "utility": 56},
        "positions": {"Duelist": 0.78, "Tank": 0.66},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["bruiser", "tank", "burst"],
             "text": "Monge enlouquecido — converte o dano que sofre em força física, ficando cada vez mais perigoso."},
        ],
    },
    # ── Lendas de Roger / Rocks ────────────────────────────────────────────
    "Gol D. Roger": {
        "stats": {"power": 99, "durability": 94, "speed": 88, "utility": 90},
        "positions": {"Captain": 1.0, "Duelist": 0.96, "Vice Captain": 0.7},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "leadership", "conqueror"],
             "text": "Rei dos Piratas — espadachim sem Akuma no Mi que rivalizou com Whitebeard; Haki do Rei que rachava o céu e ouvia 'a voz de todas as coisas'."},
        ],
    },
    "Scopper Gaban": {
        "stats": {"power": 86, "durability": 78, "speed": 76, "utility": 64},
        "positions": {"Duelist": 0.9, "Vice Captain": 0.78},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["ace", "bruiser", "burst"],
             "text": "Veterano dos Piratas de Roger — um dos guerreiros mais temíveis da tripulação lendária."},
        ],
    },
    "Crocus": {
        "stats": {"power": 40, "durability": 46, "speed": 40, "utility": 70},
        "positions": {"Healer": 0.85, "Support": 0.6},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["heal", "sustain", "utility"],
             "text": "Médico dos Piratas de Roger — manteve vivo um capitão doente em sua última jornada; guardião do farol da Reverse Mountain."},
        ],
    },
    # ── Blackbeard Pirates ─────────────────────────────────────────────────
    "Marshall D. Teach": {
        "stats": {"power": 94, "durability": 88, "speed": 66, "utility": 84},
        "positions": {"Captain": 0.92, "Duelist": 0.9, "Tank": 0.78, "Traitor": 0.72},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "aoe", "burst", "betrayal", "manipulation"],
             "text": "Trevas + Tremor — única pessoa com duas frutas: a escuridão suga poderes e gravidade, o tremor racha o mundo; o traidor que matou para subir."},
        ],
    },
    "Jesus Burgess": {
        "stats": {"power": 76, "durability": 76, "speed": 58, "utility": 50},
        "positions": {"Tank": 0.8, "Duelist": 0.76},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["tank", "bruiser", "durability", "burst"],
             "text": "Campeão dos Blackbeard — força física que ergue e arremessa estruturas colossais."},
        ],
    },
    "Shiryu": {
        "stats": {"power": 84, "durability": 72, "speed": 78, "utility": 66},
        "positions": {"Duelist": 0.9, "Vice Captain": 0.66, "Traitor": 0.55},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "versatility"],
             "text": "Fruta da Invisibilidade — espadachim mestre que ataca sem ser visto; ex-carcereiro de Impel Down."},
        ],
    },
    "Van Augur": {
        "stats": {"power": 76, "durability": 56, "speed": 66, "utility": 80},
        "positions": {"Support": 0.78, "Duelist": 0.74},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["burst", "versatility", "utility", "recon"],
             "text": "Fruta do Teletransporte — desloca a si, aos outros e às próprias balas no espaço; atirador que nunca erra."},
        ],
    },
    # ── Gorosei / Topo do Mundo ────────────────────────────────────────────
    "Nerona Imu": {
        "stats": {"power": 99, "durability": 92, "speed": 82, "utility": 95},
        "positions": {"Captain": 0.95, "Duelist": 0.9, "Support": 0.7},
        "abilities": [
            {"reveal": "egghead", "disclosure": "named",
             "tags": ["ace", "aoe", "manipulation", "leadership"],
             "text": "Soberano oculto do Trono Vazio — autoridade absoluta sobre o mundo e o poder de apagar do mapa o que ameaça o Governo."},
        ],
    },
    "Rocks D. Xebec": {
        "stats": {"power": 98, "durability": 90, "speed": 82, "utility": 84},
        "positions": {"Captain": 0.95, "Duelist": 0.94, "Vice Captain": 0.7},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["ace", "bruiser", "leadership", "conqueror"],
             "text": "Capitão dos Piratas Rocks — reuniu futuros Imperadores num só bando e quase tomou o mundo em God Valley."},
        ],
    },
    "Jaygarcia Saturn": {
        "stats": {"power": 93, "durability": 90, "speed": 70, "utility": 84},
        "positions": {"Captain": 0.82, "Duelist": 0.88, "Tank": 0.82},
        "abilities": [
            {"reveal": "egghead", "disclosure": "full",
             "tags": ["ace", "tank", "durability", "aoe", "versatility"],
             "text": "Ancião do Governo — Zoan mítico (aranha-boi) gigantesco que resiste a ataques de Almirante e impõe medo sobrenatural."},
        ],
    },
    "Marcus Mars": {
        "stats": {"power": 91, "durability": 86, "speed": 80, "utility": 70},
        "positions": {"Duelist": 0.88, "Tank": 0.76},
        "abilities": [
            {"reveal": "egghead", "disclosure": "named",
             "tags": ["ace", "bruiser", "burst", "durability"],
             "text": "Ancião do Governo — Zoan mítico alado (Itsumade) que mergulha sobre o alvo; regenera ferimentos graves."},
        ],
    },
    "Topman Warcury": {
        "stats": {"power": 92, "durability": 90, "speed": 64, "utility": 66},
        "positions": {"Tank": 0.86, "Duelist": 0.86},
        "abilities": [
            {"reveal": "egghead", "disclosure": "named",
             "tags": ["ace", "tank", "durability", "bruiser", "aoe"],
             "text": "Ancião do Governo — Zoan mítico (javali Fengxi) cuja mordida e investida demolem estruturas."},
        ],
    },
    "Ethanbaron V. Nusjuro": {
        "stats": {"power": 92, "durability": 86, "speed": 82, "utility": 72},
        "positions": {"Duelist": 0.9, "Tank": 0.76},
        "abilities": [
            {"reveal": "egghead", "disclosure": "named",
             "tags": ["ace", "bruiser", "burst"],
             "text": "Ancião do Governo — Zoan mítico (cavalo-esqueleto Bakotsu) e uma lâmina que corta com precisão fria."},
        ],
    },
    "Shepherd Ju Peter": {
        "stats": {"power": 90, "durability": 88, "speed": 62, "utility": 66},
        "positions": {"Tank": 0.84, "Duelist": 0.84},
        "abilities": [
            {"reveal": "egghead", "disclosure": "named",
             "tags": ["ace", "tank", "durability", "aoe"],
             "text": "Ancião do Governo — Zoan mítico (verme-da-areia) colossal que engole e tritura o terreno."},
        ],
    },
    # ── Holy Knights / God's Knights (mangá) ───────────────────────────────
    "Figarland Garling": {
        "stats": {"power": 93, "durability": 84, "speed": 82, "utility": 76},
        "positions": {"Captain": 0.8, "Duelist": 0.92},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["ace", "bruiser", "burst", "leadership"],
             "text": "Comandante Supremo dos Cavaleiros Sagrados — figura temida desde God Valley, autoridade quase divina."},
        ],
    },
    "Figarland Shamrock": {
        "stats": {"power": 90, "durability": 80, "speed": 82, "utility": 70},
        "positions": {"Duelist": 0.9, "Captain": 0.66},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["ace", "bruiser", "burst"],
             "text": "Cavaleiro Sagrado — espadachim de elite com uma fera invocada e domínio dos três Haki."},
        ],
    },
    "Rimoshifu Killingham": {
        "stats": {"power": 86, "durability": 78, "speed": 74, "utility": 74},
        "positions": {"Duelist": 0.84, "Support": 0.6},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["ace", "versatility", "debuff", "manipulation"],
             "text": "Cavaleiro Sagrado — Zoan de unicórnio ligado a sonhos; impõe condições sobrenaturais ao combate."},
        ],
    },
    "Shepherd Sommers": {
        "stats": {"power": 84, "durability": 74, "speed": 78, "utility": 64},
        "positions": {"Duelist": 0.84},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["ace", "burst", "debuff"],
             "text": "Cavaleiro Sagrado — poder ofensivo que pune o oponente com efeitos dolorosos ao toque."},
        ],
    },
    "Manmayer Gunko": {
        "stats": {"power": 84, "durability": 72, "speed": 80, "utility": 72},
        "positions": {"Duelist": 0.84, "Support": 0.62},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["ace", "burst", "versatility", "lockdown"],
             "text": "Cavaleira Sagrada — manipula o espaço para disparar flechas que ignoram a distância."},
        ],
    },
    "Satchels Maffey": {
        "stats": {"power": 82, "durability": 72, "speed": 80, "utility": 66},
        "positions": {"Duelist": 0.82},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["ace", "burst", "versatility"],
             "text": "Cavaleiro Sagrado — combatente de elite a serviço do Governo Mundial."},
        ],
    },
    # ── Red Hair / Revolução ───────────────────────────────────────────────
    "Benn Beckman": {
        "stats": {"power": 86, "durability": 76, "speed": 74, "utility": 82},
        "positions": {"Vice Captain": 0.9, "Duelist": 0.84, "Support": 0.6},
        "abilities": [
            {"reveal": "marineford", "disclosure": "full",
             "tags": ["ace", "bruiser", "leadership", "recon"],
             "text": "Imediato dos Red Hair — Haki e mira tão intimidantes que fizeram um Almirante recuar sem disparo."},
        ],
    },
    "Lucky Roux": {
        "stats": {"power": 74, "durability": 66, "speed": 64, "utility": 56},
        "positions": {"Duelist": 0.78, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "named",
             "tags": ["bruiser", "burst"],
             "text": "Oficial dos Red Hair — pontaria letal e reflexos surpreendentes apesar da aparência tranquila."},
        ],
    },
    "Yasopp": {
        "stats": {"power": 70, "durability": 60, "speed": 66, "utility": 74},
        "positions": {"Support": 0.78, "Duelist": 0.7},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["burst", "recon", "utility"],
             "text": "Atirador dos Red Hair — mira sobre-humana, capaz de acertar formigas à distância; pai de Usopp."},
        ],
    },
    "Monkey D. Dragon": {
        "stats": {"power": 94, "durability": 82, "speed": 80, "utility": 88},
        "positions": {"Captain": 0.9, "Duelist": 0.85, "Support": 0.65},
        "abilities": [
            {"reveal": "marineford", "disclosure": "named",
             "tags": ["ace", "aoe", "leadership", "versatility"],
             "text": "Líder do Exército Revolucionário — o Homem Mais Procurado do Mundo, ligado a tempestades inexplicáveis."},
        ],
    },
    # ── Gigantes (Elbaf / Little Garden) ───────────────────────────────────
    "Dorry": {
        "stats": {"power": 78, "durability": 84, "speed": 50, "utility": 50},
        "positions": {"Tank": 0.85, "Duelist": 0.76},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser", "aoe"],
             "text": "Gigante de Elbaf — guerreiro lendário de Little Garden, espadão e resistência colossal."},
        ],
    },
    "Brogy": {
        "stats": {"power": 78, "durability": 84, "speed": 50, "utility": 50},
        "positions": {"Tank": 0.85, "Duelist": 0.76},
        "abilities": [
            {"reveal": "alabasta", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser", "aoe"],
             "text": "Gigante de Elbaf — rival eterno de Dorry; machado e brados de guerra que abalam o chão."},
        ],
    },
    "Loki": {
        "stats": {"power": 84, "durability": 82, "speed": 64, "utility": 64},
        "positions": {"Duelist": 0.86, "Tank": 0.8, "Captain": 0.6},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["ace", "bruiser", "tank", "durability", "conqueror"],
             "text": "Príncipe de Elbaf — gigante tido como o mais forte de sua geração, mantido acorrentado por seu próprio poder."},
        ],
    },
    "Hajrudin": {
        "stats": {"power": 76, "durability": 80, "speed": 56, "utility": 52},
        "positions": {"Tank": 0.82, "Duelist": 0.78},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser", "burst"],
             "text": "Capitão dos Novos Guerreiros Gigantes — socos que despedaçam executivos e o sonho de chegar a Elbaf."},
        ],
    },
    "Gerd": {
        "stats": {"power": 72, "durability": 78, "speed": 54, "utility": 48},
        "positions": {"Tank": 0.8, "Duelist": 0.72},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Guerreira gigante de Elbaf — força bruta e resistência típicas dos lendários soldados da ilha."},
        ],
    },
    "Goldberg": {
        "stats": {"power": 72, "durability": 78, "speed": 52, "utility": 46},
        "positions": {"Tank": 0.8, "Duelist": 0.72},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Guerreiro gigante de Elbaf — combatente colossal a serviço do reino dos gigantes."},
        ],
    },
    "Road": {
        "stats": {"power": 72, "durability": 78, "speed": 52, "utility": 46},
        "positions": {"Tank": 0.8, "Duelist": 0.72},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Guerreiro gigante de Elbaf — força esmagadora na linha de frente do reino."},
        ],
    },
    "Oimo": {
        "stats": {"power": 70, "durability": 78, "speed": 48, "utility": 46},
        "positions": {"Tank": 0.8, "Duelist": 0.7},
        "abilities": [
            {"reveal": "water7", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Gigante guardião — montanha viva que defende os portões com um machado descomunal."},
        ],
    },
    "Kashii": {
        "stats": {"power": 70, "durability": 78, "speed": 48, "utility": 46},
        "positions": {"Tank": 0.8, "Duelist": 0.7},
        "abilities": [
            {"reveal": "water7", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Gigante guardião — parceiro de Oimo na muralha, golpes que esmagam navios."},
        ],
    },
    "Stansen": {
        "stats": {"power": 58, "durability": 70, "speed": 46, "utility": 50},
        "positions": {"Tank": 0.74, "Support": 0.5},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["tank", "durability"],
             "text": "Gigante de porte avantajado — força física natural da raça dos gigantes."},
        ],
    },
    "Jarul": {
        "stats": {"power": 74, "durability": 80, "speed": 48, "utility": 60},
        "positions": {"Tank": 0.8, "Captain": 0.55, "Support": 0.55},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["tank", "durability", "leadership"],
             "text": "Ancião gigante de Elbaf — veterano de batalha cuja experiência guia os guerreiros mais jovens."},
        ],
    },
    # ── Espadachim Supremo / outros ────────────────────────────────────────
    "Dracule Mihawk": {
        "stats": {"power": 94, "durability": 78, "speed": 84, "utility": 70},
        "positions": {"Duelist": 1.0, "Captain": 0.7, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "east_blue", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst"],
             "text": "O Maior Espadachim do Mundo — cortes que partem montanhas e atravessam o oceano; precisão absoluta com a Yoru."},
        ],
    },
    "Douglas Bullet": {
        "stats": {"power": 88, "durability": 86, "speed": 70, "utility": 72},
        "positions": {"Duelist": 0.9, "Tank": 0.84, "Captain": 0.6},
        "abilities": [
            {"reveal": "dressrosa", "disclosure": "named",
             "tags": ["ace", "tank", "durability", "aoe", "bruiser"],
             "text": "Herança do Demônio — Fruta da Fusão: une máquinas e destroços num colosso gigantesco; força da era de Roger."},
        ],
    },
    "Ryu": {
        "stats": {"power": 70, "durability": 76, "speed": 54, "utility": 50},
        "positions": {"Tank": 0.78, "Duelist": 0.7},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Guerreiro gigante de Elbaf — força e resistência colossais a serviço do reino."},
        ],
    },
    "Harald": {
        "stats": {"power": 82, "durability": 80, "speed": 60, "utility": 66},
        "positions": {"Captain": 0.7, "Duelist": 0.82, "Tank": 0.74},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["ace", "bruiser", "tank", "leadership"],
             "text": "Rei de Elbaf — soberano gigante respeitado, força lendária à frente do reino dos guerreiros."},
        ],
    },
    "Candelle": {
        "stats": {"power": 66, "durability": 64, "speed": 60, "utility": 54},
        "positions": {"Duelist": 0.7, "Tank": 0.6},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["bruiser", "versatility"],
             "text": "Combatente ligado a Elbaf — guerreiro competente cujos feitos ainda se revelam."},
        ],
    },
    "Zaza": {
        "stats": {"power": 66, "durability": 64, "speed": 60, "utility": 54},
        "positions": {"Duelist": 0.7, "Tank": 0.6},
        "abilities": [
            {"reveal": "elbaf", "disclosure": "named",
             "tags": ["bruiser", "versatility"],
             "text": "Combatente ligado a Elbaf — guerreiro competente cujos feitos ainda se revelam."},
        ],
    },
    # ── Lendas do Século Vazio ─────────────────────────────────────────────
    "Joy Boy": {
        "stats": {"power": 96, "durability": 88, "speed": 86, "utility": 84},
        "positions": {"Captain": 0.9, "Duelist": 0.9, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "wano", "disclosure": "named",
             "tags": ["ace", "leadership", "conqueror", "aoe"],
             "text": "O Guerreiro da Libertação do Século Vazio — figura lendária cujo legado ainda move o mundo; poder à altura do mito."},
        ],
    },
    "Nika": {
        "stats": {"power": 97, "durability": 90, "speed": 92, "utility": 82},
        "positions": {"Captain": 0.92, "Duelist": 0.95, "Tank": 0.7},
        "abilities": [
            {"reveal": "wano", "disclosure": "named",
             "tags": ["ace", "burst", "aoe", "conqueror"],
             "text": "O Deus Sol Nika — o guerreiro que traz liberdade e alegria; dobra a realidade ao redor como borracha, lutando ao ritmo do tambor da libertação."},
        ],
    },
}


ONEPIECE_POWER = UniversePower(
    arcs=ARCS,
    reveal_max=REVEAL_MAX,
    profiles=PROFILES,
    default_reveal="elbaf",
)
