"""
Bleach power profiles — battle-analysis data.

SPOILER POLICY: a pool em config.universes tem três modos — "completo" (todas as
sagas, incl. Mil Anos de Sangue / TYBW), "pre_tybw" (remove exclusivos do arco
final) e "teste". O gate por `reveal` é a segunda camada: power-ups vistos só na
TYBW (Bankais reforjados, Royal Guard, Quincy/Wandenreich) recebem reveal="tybw"
e somem no modo pre_tybw.

TRUNFO: como em Dragon Ball, NÃO usamos as tags `domain`/`conqueror` (texto fixo
do motor é de outras franquias). A hierarquia de poder é carregada pela escala
de stats não-linear: um Capitão-Comandante ou o Aizen transcendente esmagam em
pontuação bruta.

STAT SCALE: 0–100, não-linear. Tiers aproximados:
    transcendente (Yhwach, Aizen pós-Hogyoku) ........... 96–100
    Capitão de elite / Espada superior / Royal Guard .... 84–94
    Capitão / Visored / Espada ......................... 72–86
    Tenente forte / Arrancar médio ..................... 54–72
    humano avançado / hollow comum ..................... 38–56
    apoio / civil ...................................... 8–40  (Orihime é fraca em
        ataque, mas decisiva em utilidade)
Personagens sem perfil caem no neutro 50.
"""

from __future__ import annotations

from config.power_profiles import UniversePower


# Ordered reveal tiers, earliest → latest (continuidade do anime).
ARCS = [
    "agent",          # Substituto Ceifador (intro, hollows de Karakura)
    "soul_society",   # Sociedade das Almas (Gotei 13, revelação de Aizen)
    "arrancar",       # Arrancar / Hueco Mundo / Karakura Falsa (Espada, Visored)
    "fullbring",      # O Agente Perdido (Fullbringers)
    "tybw",           # Mil Anos de Sangue (Wandenreich / Royal Guard)
]

REVEAL_MAX = {
    "completo": "tybw",
    "pre_tybw": "fullbring",
    "teste":    "tybw",
}


# disclosure levels: "full" | "named" | "exists"
PROFILES: dict[str, dict] = {
    # ── Karakura (protagonistas) ─────────────────────────────────────────────
    "Ichigo Kurosaki": {
        "stats": {"power": 92, "durability": 86, "speed": 90, "utility": 64},
        "positions": {"Captain": 0.9, "Duelist": 0.96, "Vice Captain": 0.7, "Tank": 0.65},
        "abilities": [
            {"reveal": "agent", "disclosure": "full",
             "tags": ["bruiser", "burst", "ace"],
             "text": "Ceifador substituto — Zangetsu dispara o Getsuga Tenshou, uma lâmina de energia espiritual."},
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "Máscara Hollow e Bankai — velocidade e potência multiplicadas; no limite, o Getsuga Tenshou Final."},
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["ace", "burst", "bruiser"],
             "text": "Zangetsu verdadeira (reforjada) — o Bankai pleno que une Ceifador, Hollow e Quincy."},
        ],
    },
    "Rukia Kuchiki": {
        "stats": {"power": 66, "durability": 56, "speed": 64, "utility": 66},
        "positions": {"Duelist": 0.74, "Support": 0.6, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["lockdown", "debuff", "versatility"],
             "text": "Sode no Shirayuki — zampakuto de gelo que congela tudo ao redor."},
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["ace", "burst", "lockdown"],
             "text": "Bankai (Hakka no Togame) — abaixa a própria temperatura ao zero absoluto e cristaliza o inimigo."},
        ],
    },
    "Orihime Inoue": {
        "stats": {"power": 22, "durability": 30, "speed": 40, "utility": 92},
        "positions": {"Healer": 1.0, "Support": 0.7},
        "abilities": [
            {"reveal": "agent", "disclosure": "full",
             "tags": ["heal", "revive", "sustain", "guard"],
             "text": "Shun Shun Rikka — rejeita eventos: cura ferimentos mortais e até reverte a destruição; escudo Santen Kesshun."},
        ],
    },
    "Yasutora Sado": {
        "stats": {"power": 60, "durability": 70, "speed": 50, "utility": 44},
        "positions": {"Tank": 0.78, "Duelist": 0.66},
        "abilities": [
            {"reveal": "agent", "disclosure": "full",
             "tags": ["bruiser", "tank", "durability", "burst"],
             "text": "Braços do Gigante e do Diabo — um braço-escudo defensivo e um braço-canhão de poder devastador."},
        ],
    },
    "Uryū Ishida": {
        "stats": {"power": 64, "durability": 56, "speed": 70, "utility": 66},
        "positions": {"Duelist": 0.78, "Support": 0.6, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "agent", "disclosure": "full",
             "tags": ["burst", "versatility", "recon"],
             "text": "Último Quincy — arco de energia espiritual que dispara uma chuva de flechas precisas a longa distância."},
        ],
    },
    # ── Gotei 13 (capitães) ──────────────────────────────────────────────────
    "Genryūsai Shigekuni Yamamoto": {
        "stats": {"power": 94, "durability": 86, "speed": 78, "utility": 80},
        "positions": {"Captain": 0.95, "Duelist": 0.94, "Tank": 0.7},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "leadership"],
             "text": "Ryūjin Jakka — a zampakuto de fogo mais poderosa; o Capitão-Comandante incinera tudo num raio imenso."},
        ],
    },
    "Retsu Unohana": {
        "stats": {"power": 80, "durability": 66, "speed": 72, "utility": 84},
        "positions": {"Healer": 0.95, "Duelist": 0.82, "Captain": 0.66, "Support": 0.7},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["heal", "sustain", "revive"],
             "text": "Minazuki — a maior curandeira do Gotei 13, capaz de regenerar ferimentos catastróficos."},
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst"],
             "text": "Minazuki (Bankai) — a primeira Kenpachi; uma espadachim letal por trás da médica gentil."},
        ],
    },
    "Byakuya Kuchiki": {
        "stats": {"power": 82, "durability": 70, "speed": 84, "utility": 64},
        "positions": {"Duelist": 0.9, "Captain": 0.7, "Vice Captain": 0.66},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "lockdown"],
             "text": "Senbonzakura — a lâmina se desfaz em milhões de pétalas cortantes; o Bankai cobre o campo de aço."},
        ],
    },
    "Kenpachi Zaraki": {
        "stats": {"power": 88, "durability": 88, "speed": 72, "utility": 40},
        "positions": {"Duelist": 0.94, "Tank": 0.82, "Captain": 0.68},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["bruiser", "burst", "durability", "tank"],
             "text": "Poder espiritual monstruoso e selado — combatente nato que corta o que quiser por pura força."},
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["ace", "burst", "aoe"],
             "text": "Nozarashi (Shikai/Bankai) — solta toda a sua força bruta; cortes que rasgam o céu."},
        ],
    },
    "Tōshirō Hitsugaya": {
        "stats": {"power": 76, "durability": 62, "speed": 80, "utility": 64},
        "positions": {"Duelist": 0.84, "Captain": 0.62, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "lockdown"],
             "text": "Hyōrinmaru — o gelo mais forte; o Bankai (Daiguren) cria asas e cauda de gelo."},
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["lockdown", "debuff"],
             "text": "Maturidade do Bankai — congela tudo o que toca dentro de um tempo-limite implacável."},
        ],
    },
    "Mayuri Kurotsuchi": {
        "stats": {"power": 70, "durability": 56, "speed": 58, "utility": 86},
        "positions": {"Support": 0.82, "Duelist": 0.7, "Captain": 0.6, "Traitor": 0.55},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["versatility", "debuff", "sabotage", "utility"],
             "text": "Cientista do Gotei — venenos, autodissolução e o Bankai Konjiki Ashisogi Jizō; planos dentro de planos."},
        ],
    },
    "Shunsui Kyōraku": {
        "stats": {"power": 86, "durability": 72, "speed": 78, "utility": 74},
        "positions": {"Captain": 0.85, "Duelist": 0.88, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["ace", "versatility", "debuff", "lockdown"],
             "text": "Katen Kyōkotsu — transforma a luta num jogo mortal de regras; o Bankai impõe um conto trágico ao inimigo."},
        ],
    },
    "Suì-Fēng": {
        "stats": {"power": 70, "durability": 58, "speed": 88, "utility": 60},
        "positions": {"Duelist": 0.82, "Vice Captain": 0.6, "Traitor": 0.5},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["burst", "versatility"],
             "text": "Suzumebachi — dois toques no mesmo ponto matam; comandante das forças secretas e mestra do Shunpo."},
        ],
    },
    "Sajin Komamura": {
        "stats": {"power": 74, "durability": 80, "speed": 58, "utility": 50},
        "positions": {"Tank": 0.86, "Duelist": 0.72, "Captain": 0.6},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser", "guard"],
             "text": "Tenken (Bankai) — invoca um guerreiro gigante que espelha seus golpes; resistência inabalável."},
        ],
    },
    "Shinji Hirako": {
        "stats": {"power": 74, "durability": 62, "speed": 70, "utility": 68},
        "positions": {"Duelist": 0.8, "Captain": 0.6, "Support": 0.55},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["debuff", "versatility", "lockdown"],
             "text": "Sakanade — inverte os sentidos do oponente (cima/baixo, esquerda/direita); líder dos Visored com máscara Hollow."},
        ],
    },
    "Renji Abarai": {
        "stats": {"power": 70, "durability": 64, "speed": 66, "utility": 52},
        "positions": {"Duelist": 0.78, "Vice Captain": 0.66, "Tank": 0.58},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["bruiser", "burst", "aoe"],
             "text": "Zabimaru — espada-chicote segmentada; o Bankai Hihiō Zabimaru vira uma serpente-babuíno colossal."},
        ],
    },
    "Rangiku Matsumoto": {
        "stats": {"power": 54, "durability": 46, "speed": 58, "utility": 56},
        "positions": {"Support": 0.7, "Duelist": 0.6},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["debuff", "lockdown", "versatility"],
             "text": "Haineko — dispersa a lâmina em cinzas cortantes que cercam e prendem o alvo."},
        ],
    },
    "Hachigen Ushōda": {
        "stats": {"power": 56, "durability": 60, "speed": 44, "utility": 84},
        "positions": {"Support": 0.85, "Healer": 0.75, "Tank": 0.6},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["guard", "heal", "lockdown", "utility"],
             "text": "Mestre do Kidō entre os Visored — barreiras quase indestrutíveis, prisões de energia e reparo de membros."},
        ],
    },
    "Isane Kotetsu": {
        "stats": {"power": 40, "durability": 44, "speed": 50, "utility": 76},
        "positions": {"Healer": 0.9, "Support": 0.6},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["heal", "sustain", "utility"],
             "text": "Tenente da 4ª Divisão — perita em Kidō de cura para tratar o time em campo."},
        ],
    },
    # ── Aizen & traidores ──────────────────────────────────────────────────
    "Sousuke Aizen": {
        "stats": {"power": 97, "durability": 88, "speed": 88, "utility": 96},
        "positions": {"Captain": 0.95, "Duelist": 0.95, "Support": 0.7, "Traitor": 0.85},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["manipulation", "debuff", "betrayal", "versatility"],
             "text": "Kyōka Suigetsu — hipnose absoluta: quem vê a liberação fica preso a ilusões perfeitas dos cinco sentidos."},
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["ace", "burst", "sustain", "durability"],
             "text": "Fusão com o Hogyoku — transcende Ceifador e Hollow; regeneração e poder quase ilimitados."},
        ],
    },
    "Gin Ichimaru": {
        "stats": {"power": 76, "durability": 60, "speed": 84, "utility": 66},
        "positions": {"Duelist": 0.84, "Traitor": 0.75, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["burst", "versatility", "betrayal"],
             "text": "Shinsō — lâmina que se estende à velocidade do som; o Bankai Kamishini no Yari dissolve com veneno."},
        ],
    },
    "Kaname Tōsen": {
        "stats": {"power": 70, "durability": 58, "speed": 68, "utility": 58},
        "positions": {"Duelist": 0.76, "Traitor": 0.7},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["debuff", "lockdown", "versatility", "betrayal"],
             "text": "Suzumushi — rouba visão, som e olfato do campo (Clima do Silêncio); ressonância sônica paralisante."},
        ],
    },
    # ── Espada / Arrancar (Hueco Mundo) ─────────────────────────────────────
    "Coyote Starrk": {
        "stats": {"power": 84, "durability": 70, "speed": 82, "utility": 70},
        "positions": {"Duelist": 0.88, "Captain": 0.6, "Support": 0.55},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "versatility"],
             "text": "Los Lobos (Espada nº1) — fragmenta a própria alma num exército de lobos de energia e dispara Ceros contínuos."},
        ],
    },
    "Baraggan Louisenbairn": {
        "stats": {"power": 82, "durability": 74, "speed": 50, "utility": 78},
        "positions": {"Duelist": 0.8, "Tank": 0.66, "Captain": 0.55},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["aoe", "debuff", "lockdown"],
             "text": "Senescência (Espada nº2) — um campo que envelhece e apodrece tudo ao redor, anulando o tempo do inimigo."},
        ],
    },
    "Tier Harribel": {
        "stats": {"power": 80, "durability": 70, "speed": 74, "utility": 64},
        "positions": {"Duelist": 0.84, "Captain": 0.6, "Tank": 0.58},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["ace", "burst", "aoe"],
             "text": "Tiburón (Espada nº3) — controla a água como arma cortante e dispara ondas devastadoras."},
        ],
    },
    "Ulquiorra Cifer": {
        "stats": {"power": 86, "durability": 80, "speed": 84, "utility": 62},
        "positions": {"Duelist": 0.92, "Tank": 0.66},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["ace", "burst", "sustain", "versatility"],
             "text": "Murciélago (Espada nº4) — Cero Oscuras e Lança do Relâmpago; única Espada com segunda ressurreição e regeneração."},
        ],
    },
    "Grimmjow Jaegerjaquez": {
        "stats": {"power": 78, "durability": 70, "speed": 80, "utility": 48},
        "positions": {"Duelist": 0.86, "Tank": 0.6},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["bruiser", "burst", "ace"],
             "text": "Pantera (Espada nº6) — felino feroz de garras laceriantes e dardos explosivos (Desgarrón)."},
        ],
    },
    "Nnoitra Gilga": {
        "stats": {"power": 74, "durability": 84, "speed": 64, "utility": 44},
        "positions": {"Tank": 0.82, "Duelist": 0.78},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Santa Teresa (Espada nº5) — a pele mais dura do Hueco Mundo e seis braços com foices."},
        ],
    },
    "Nelliel Tu Odelschwanck": {
        "stats": {"power": 78, "durability": 68, "speed": 74, "utility": 58},
        "positions": {"Duelist": 0.84, "Tank": 0.58, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["bruiser", "burst", "versatility"],
             "text": "Gamuza (ex-Espada nº3) — devolve ao inimigo o próprio Cero engolido (Cero Doble); centaura lanceira."},
        ],
    },
    "Szayelaporro Granz": {
        "stats": {"power": 62, "durability": 54, "speed": 60, "utility": 80},
        "positions": {"Support": 0.76, "Duelist": 0.62, "Traitor": 0.5},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["versatility", "debuff", "sabotage", "sustain"],
             "text": "Fornicarás (Espada nº8) — cientista que clona, dissolve e renasce; controla bonecos vodu dos órgãos do alvo."},
        ],
    },
    "Yammy Llargo": {
        "stats": {"power": 70, "durability": 84, "speed": 46, "utility": 38},
        "positions": {"Tank": 0.85, "Duelist": 0.68},
        "abilities": [
            {"reveal": "arrancar", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser", "aoe"],
             "text": "Ira (Espada nº0) — quanto mais furioso, maior e mais forte fica; bruta-força colossal."},
        ],
    },
    # ── Urahara Shop / aliados ───────────────────────────────────────────────
    "Kisuke Urahara": {
        "stats": {"power": 86, "durability": 70, "speed": 82, "utility": 92},
        "positions": {"Support": 0.85, "Duelist": 0.88, "Captain": 0.7},
        "abilities": [
            {"reveal": "agent", "disclosure": "full",
             "tags": ["versatility", "utility", "lockdown", "sabotage"],
             "text": "Benihime — gênio inventor por trás de tudo; barreiras, armadilhas, restaurações e o Bankai revelado tardiamente."},
        ],
    },
    "Yoruichi Shihōin": {
        "stats": {"power": 80, "durability": 66, "speed": 92, "utility": 74},
        "positions": {"Duelist": 0.88, "Support": 0.66, "Vice Captain": 0.62},
        "abilities": [
            {"reveal": "soul_society", "disclosure": "full",
             "tags": ["burst", "versatility", "bruiser"],
             "text": "Deusa do Shunpo — a mais veloz; o Shunkō reveste o corpo de Kidō e potencializa cada golpe."},
        ],
    },
    "Tessai Tsukabishi": {
        "stats": {"power": 64, "durability": 70, "speed": 52, "utility": 82},
        "positions": {"Support": 0.82, "Tank": 0.62, "Healer": 0.6},
        "abilities": [
            {"reveal": "agent", "disclosure": "full",
             "tags": ["guard", "utility", "heal", "lockdown"],
             "text": "Grão-mestre do Kidō — barreiras de altíssimo nível, selos e restaurações poderosas."},
        ],
    },
    # ── Fullbringers ───────────────────────────────────────────────────────
    "Kūgo Ginjō": {
        "stats": {"power": 74, "durability": 66, "speed": 70, "utility": 64},
        "positions": {"Duelist": 0.82, "Captain": 0.6, "Traitor": 0.7},
        "abilities": [
            {"reveal": "fullbring", "disclosure": "full",
             "tags": ["bruiser", "burst", "versatility", "betrayal"],
             "text": "Cross of Scaffold — Fullbring que vira uma grande lâmina; rouba e copia o poder de outros Fullbringers."},
        ],
    },
    "Shūkurō Tsukishima": {
        "stats": {"power": 64, "durability": 56, "speed": 64, "utility": 82},
        "positions": {"Support": 0.78, "Duelist": 0.64, "Traitor": 0.72},
        "abilities": [
            {"reveal": "fullbring", "disclosure": "full",
             "tags": ["manipulation", "debuff", "betrayal", "versatility"],
             "text": "Book of the End — ao cortar alguém, insere-se no passado da vítima, reescrevendo memórias e lealdades."},
        ],
    },
    # ── Mil Anos de Sangue (Wandenreich / Royal Guard) ──────────────────────
    "Yhwach": {
        "stats": {"power": 99, "durability": 92, "speed": 88, "utility": 98},
        "positions": {"Captain": 0.96, "Duelist": 0.95, "Support": 0.7},
        "abilities": [
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["ace", "burst", "manipulation", "versatility"],
             "text": "O Todo-Poderoso (The Almighty) — enxerga e reescreve todos os futuros possíveis; absorve poderes e desfaz habilidades alheias."},
        ],
    },
    "Jugram Haschwalth": {
        "stats": {"power": 84, "durability": 72, "speed": 80, "utility": 74},
        "positions": {"Duelist": 0.88, "Captain": 0.66, "Vice Captain": 0.7},
        "abilities": [
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["ace", "burst", "debuff", "versatility"],
             "text": "O Equilíbrio (The Balance) — transfere o infortúnio acumulado para o inimigo; espadachim de elite."},
        ],
    },
    "Askin Nakk Le Vaar": {
        "stats": {"power": 80, "durability": 72, "speed": 66, "utility": 80},
        "positions": {"Duelist": 0.8, "Support": 0.66, "Traitor": 0.55},
        "abilities": [
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["debuff", "aoe", "versatility", "sabotage"],
             "text": "A Morte (The Deathdealing) — controla a dose letal de qualquer substância; envenena o campo na medida exata."},
        ],
    },
    "Lille Barro": {
        "stats": {"power": 84, "durability": 76, "speed": 78, "utility": 60},
        "positions": {"Duelist": 0.88, "Tank": 0.62},
        "abilities": [
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "O Pistoleiro (The X-Axis) — tiros que ignoram qualquer obstáculo e sempre acertam o alvo; forma angelical."},
        ],
    },
    "Pernida Parnkgjas": {
        "stats": {"power": 82, "durability": 80, "speed": 60, "utility": 74},
        "positions": {"Duelist": 0.8, "Tank": 0.66},
        "abilities": [
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["debuff", "aoe", "versatility", "sustain"],
             "text": "A Compaixão (The Compulsory) — controla e deforma tudo o que toca seus nervos, regenerando-se ao se dividir."},
        ],
    },
    "Gremmy Thoumeaux": {
        "stats": {"power": 84, "durability": 60, "speed": 64, "utility": 86},
        "positions": {"Duelist": 0.82, "Support": 0.7},
        "abilities": [
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["versatility", "aoe", "manipulation", "burst"],
             "text": "A Visionária (The Visionary) — tudo o que ele imagina vira realidade: meteoros, monstros, exércitos."},
        ],
    },
    "Bazz-B": {
        "stats": {"power": 78, "durability": 66, "speed": 74, "utility": 52},
        "positions": {"Duelist": 0.84, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["burst", "aoe", "bruiser"],
             "text": "O Calor (The Heat) — chamas explosivas concentradas que perfuram e incineram."},
        ],
    },
    "Ichibe'e Hyōsube": {
        "stats": {"power": 92, "durability": 84, "speed": 80, "utility": 90},
        "positions": {"Captain": 0.85, "Duelist": 0.9, "Support": 0.7},
        "abilities": [
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["ace", "versatility", "debuff", "lockdown"],
             "text": "Ichimonji — nomeia e renomeia a essência das coisas; pintar o nome do inimigo enfraquece e domina seu poder. Chefe da Royal Guard."},
        ],
    },
    "Tenjirō Kirinji": {
        "stats": {"power": 80, "durability": 72, "speed": 84, "utility": 82},
        "positions": {"Duelist": 0.82, "Healer": 0.8, "Support": 0.66},
        "abilities": [
            {"reveal": "tybw", "disclosure": "full",
             "tags": ["heal", "sustain", "burst", "versatility"],
             "text": "Águas Quentes do Sangue — o curandeiro da Royal Guard; suas águas restauram e seus golpes escaldam."},
        ],
    },
}


BLEACH_POWER = UniversePower(
    arcs=ARCS,
    reveal_max=REVEAL_MAX,
    profiles=PROFILES,
    default_reveal="tybw",
)
