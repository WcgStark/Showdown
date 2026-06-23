"""
Invincible power profiles — battle-analysis data.

A pool tem dois modos — "default" (todos) e "teste". Não há corte por spoiler de
arco, então REVEAL_MAX cobre tudo; o `reveal` por arco serve só de organização.

TRUNFO: como em Dragon Ball, NÃO usamos as tags `domain`/`conqueror` (texto fixo
do motor é de outras franquias). A hierarquia vem da escala de stats.

STAT SCALE: 0–100, não-linear. Tiers aproximados:
    topo Viltrumita / cósmico (Thragg, Conquest, Allen) ... 90–100
    Viltrumita / herói de elite (Omni-Man, Invincible, Eve)  84–94
    super-herói/vilão forte ............................... 66–84
    operativo / herói médio ............................... 48–66
    estrategista / apoio / civil .......................... 8–48
Personagens sem perfil caem no neutro 50.
"""

from __future__ import annotations

from config.power_profiles import UniversePower


ARCS = [
    "season1",   # Início (Mark descobre seus poderes, traição de Omni-Man)
    "season2",   # Expansão (Viltrum, multiverso, guerras)
    "later",     # Eventos tardios (guerra Viltrumita)
]

REVEAL_MAX = {
    "default": "later",
    "teste":   "later",
}


# disclosure levels: "full" | "named" | "exists"
PROFILES: dict[str, dict] = {
    # ── Família Grayson ──────────────────────────────────────────────────────
    "Invincible": {
        "stats": {"power": 90, "durability": 88, "speed": 90, "utility": 60},
        "positions": {"Captain": 0.9, "Duelist": 0.95, "Vice Captain": 0.7, "Tank": 0.7},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["bruiser", "burst", "leadership", "durability"],
             "text": "Meio-Viltrumita — voo, força e resistência sobre-humanas que crescem a cada batalha contra inimigos cada vez maiores."},
        ],
    },
    "Omni-Man": {
        "stats": {"power": 94, "durability": 92, "speed": 92, "utility": 64},
        "positions": {"Captain": 0.85, "Duelist": 0.95, "Tank": 0.78, "Traitor": 0.8},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "durability", "betrayal"],
             "text": "Nolan, guerreiro Viltrumita de elite — séculos de experiência, força esmagadora e voo supersônico."},
        ],
    },
    "Atom Eve": {
        "stats": {"power": 90, "durability": 70, "speed": 70, "utility": 96},
        "positions": {"Support": 0.9, "Duelist": 0.86, "Healer": 0.8, "Captain": 0.6},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["versatility", "aoe", "heal", "guard", "burst"],
             "text": "Manipulação da matéria a nível atômico — cria qualquer coisa, ergue barreiras, cura ferimentos e desfaz o que existe; um dos poderes mais fortes do planeta."},
        ],
    },
    "Oliver Grayson": {
        "stats": {"power": 74, "durability": 72, "speed": 76, "utility": 50},
        "positions": {"Duelist": 0.78, "Tank": 0.6},
        "abilities": [
            {"reveal": "season2", "disclosure": "full",
             "tags": ["bruiser", "burst", "durability"],
             "text": "Irmão híbrido de Mark — herda a força Viltrumita e amadurece num ritmo acelerado."},
        ],
    },
    "Debbie Grayson": {
        "stats": {"power": 6, "durability": 16, "speed": 30, "utility": 56},
        "positions": {"Support": 0.6},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["utility", "leadership"],
             "text": "Civil de coração firme — o âncora emocional da família, sem poderes de combate."},
        ],
    },
    # ── Viltrumites ──────────────────────────────────────────────────────────
    "Thragg": {
        "stats": {"power": 99, "durability": 96, "speed": 92, "utility": 70},
        "positions": {"Captain": 0.92, "Duelist": 0.98, "Tank": 0.85},
        "abilities": [
            {"reveal": "later", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "durability", "leadership"],
             "text": "Grande Regente do Império Viltrum — o Viltrumita mais poderoso, criado para a guerra; força e resistência sem rival."},
        ],
    },
    "Conquest": {
        "stats": {"power": 94, "durability": 92, "speed": 84, "utility": 50},
        "positions": {"Duelist": 0.94, "Tank": 0.8, "Captain": 0.66},
        "abilities": [
            {"reveal": "season2", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "durability"],
             "text": "Executor Viltrumita — uma mão mecânica e séculos de massacre; golpes que despedaçam concreto e ossos."},
        ],
    },
    "Anissa": {
        "stats": {"power": 88, "durability": 86, "speed": 84, "utility": 56},
        "positions": {"Duelist": 0.9, "Tank": 0.74},
        "abilities": [
            {"reveal": "season2", "disclosure": "full",
             "tags": ["bruiser", "burst", "durability"],
             "text": "Agente Viltrumita de elite — força e velocidade brutais, fanática pela superioridade da espécie."},
        ],
    },
    "Kregg": {
        "stats": {"power": 84, "durability": 84, "speed": 80, "utility": 52},
        "positions": {"Duelist": 0.86, "Tank": 0.74, "Captain": 0.6},
        "abilities": [
            {"reveal": "later", "disclosure": "full",
             "tags": ["bruiser", "burst", "durability", "leadership"],
             "text": "General Viltrumita — comanda invasões com a brutalidade típica do império."},
        ],
    },
    "Lucan": {
        "stats": {"power": 82, "durability": 82, "speed": 78, "utility": 46},
        "positions": {"Duelist": 0.84, "Tank": 0.72},
        "abilities": [
            {"reveal": "later", "disclosure": "full",
             "tags": ["bruiser", "burst", "durability"],
             "text": "Soldado Viltrumita — resistência e força muito acima de qualquer humano."},
        ],
    },
    # ── Forças cósmicas / aliens ─────────────────────────────────────────────
    "Allen the Alien": {
        "stats": {"power": 92, "durability": 94, "speed": 80, "utility": 64},
        "positions": {"Duelist": 0.92, "Tank": 0.85, "Captain": 0.66, "Vice Captain": 0.62},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["ace", "bruiser", "durability", "tank"],
             "text": "Campeão da Coalizão de Planetas — fica mais forte a cada quase-morte; resistência colossal e força crescente."},
        ],
    },
    "Battle Beast": {
        "stats": {"power": 88, "durability": 86, "speed": 78, "utility": 40},
        "positions": {"Duelist": 0.92, "Tank": 0.78},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["bruiser", "burst", "durability"],
             "text": "Guerreiro felino alienígena — busca a luta perfeita; garras e força capazes de rasgar Viltrumitas."},
        ],
    },
    "Space Racer": {
        "stats": {"power": 82, "durability": 76, "speed": 88, "utility": 66},
        "positions": {"Duelist": 0.84, "Support": 0.6},
        "abilities": [
            {"reveal": "season2", "disclosure": "full",
             "tags": ["burst", "aoe", "versatility"],
             "text": "Lenda cósmica — pilota pelo espaço e dispara um canhão de energia capaz de vaporizar exércitos."},
        ],
    },
    "Universa": {
        "stats": {"power": 78, "durability": 66, "speed": 64, "utility": 72},
        "positions": {"Duelist": 0.8, "Support": 0.62},
        "abilities": [
            {"reveal": "later", "disclosure": "full",
             "tags": ["burst", "aoe", "versatility"],
             "text": "Manipula energia em escala planetária — encolhe e comprime alvos com força gravitacional."},
        ],
    },
    "Dinosaurus": {
        "stats": {"power": 76, "durability": 80, "speed": 56, "utility": 78},
        "positions": {"Tank": 0.8, "Support": 0.66, "Duelist": 0.66},
        "abilities": [
            {"reveal": "season2", "disclosure": "full",
             "tags": ["tank", "durability", "aoe", "versatility"],
             "text": "Gênio numa fera colossal — planos de batalha brilhantes e força de destruição em massa."},
        ],
    },
    # ── Guardiões do Globo / aliados ─────────────────────────────────────────
    "The Immortal": {
        "stats": {"power": 70, "durability": 78, "speed": 60, "utility": 60},
        "positions": {"Tank": 0.82, "Duelist": 0.74, "Captain": 0.66, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["tank", "durability", "sustain", "bruiser", "leadership"],
             "text": "Líder milenar dos Guardiões — regenera-se de quase qualquer ferimento e luta há séculos."},
        ],
    },
    "Robot": {
        "stats": {"power": 50, "durability": 56, "speed": 52, "utility": 88},
        "positions": {"Support": 0.88, "Captain": 0.66, "Traitor": 0.66},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["utility", "versatility", "leadership", "manipulation"],
             "text": "Mente genial que comanda drones por controle remoto — tecnologia avançada e planos de longo prazo."},
        ],
    },
    "Rex Splode": {
        "stats": {"power": 60, "durability": 52, "speed": 58, "utility": 60},
        "positions": {"Duelist": 0.72, "Support": 0.55},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["burst", "aoe", "versatility"],
             "text": "Energiza e detona qualquer objeto inorgânico que toca — granadas improvisadas a partir do cenário."},
        ],
    },
    "Dupli-Kate": {
        "stats": {"power": 52, "durability": 46, "speed": 56, "utility": 74},
        "positions": {"Support": 0.78, "Duelist": 0.62},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["versatility", "aoe", "utility"],
             "text": "Cria múltiplas cópias de si mesma — enxameia o campo e recompõe os números à vontade."},
        ],
    },
    "Monster Girl": {
        "stats": {"power": 66, "durability": 72, "speed": 54, "utility": 50},
        "positions": {"Tank": 0.8, "Duelist": 0.68},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Transforma-se numa fera colossal de força bruta (rejuvenescendo a cada mudança)."},
        ],
    },
    "Black Samson": {
        "stats": {"power": 60, "durability": 68, "speed": 50, "utility": 52},
        "positions": {"Tank": 0.78, "Duelist": 0.66, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser", "guard"],
             "text": "Veterano dos Guardiões — exoesqueleto de combate blindado e experiência tática."},
        ],
    },
    "Bulletproof": {
        "stats": {"power": 58, "durability": 70, "speed": 56, "utility": 48},
        "positions": {"Tank": 0.78, "Duelist": 0.64},
        "abilities": [
            {"reveal": "season2", "disclosure": "full",
             "tags": ["tank", "durability", "guard"],
             "text": "Campo de força que reveste o corpo — encara fogo pesado sem ceder."},
        ],
    },
    "Darkwing": {
        "stats": {"power": 54, "durability": 50, "speed": 60, "utility": 66},
        "positions": {"Duelist": 0.7, "Support": 0.6, "Traitor": 0.5},
        "abilities": [
            {"reveal": "season2", "disclosure": "full",
             "tags": ["versatility", "lockdown", "recon"],
             "text": "Acessa a Zona de Sombras para teletransportar, emboscar e prender alvos no escuro."},
        ],
    },
    "Shapesmith": {
        "stats": {"power": 56, "durability": 54, "speed": 56, "utility": 70},
        "positions": {"Support": 0.7, "Duelist": 0.6},
        "abilities": [
            {"reveal": "season2", "disclosure": "full",
             "tags": ["versatility", "guard", "utility"],
             "text": "Alienígena Martiano que remodela o próprio corpo em qualquer forma ou arma."},
        ],
    },
    "Tech Jacket": {
        "stats": {"power": 62, "durability": 64, "speed": 58, "utility": 70},
        "positions": {"Duelist": 0.7, "Support": 0.62, "Tank": 0.58},
        "abilities": [
            {"reveal": "season2", "disclosure": "full",
             "tags": ["versatility", "burst", "utility", "guard"],
             "text": "Traje simbiótico alienígena — adapta-se ao combate gerando armas e escudos sob demanda."},
        ],
    },
    # ── Comando / estratégia ─────────────────────────────────────────────────
    "Cecil Stedman": {
        "stats": {"power": 18, "durability": 30, "speed": 40, "utility": 92},
        "positions": {"Captain": 0.7, "Support": 0.9, "Traitor": 0.6},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["leadership", "utility", "manipulation", "recon", "versatility"],
             "text": "Diretor da ADG — teletransporte tático, exércitos, recursos secretos e a frieza de mover heróis como peças."},
        ],
    },
    "Donald Ferguson": {
        "stats": {"power": 40, "durability": 60, "speed": 48, "utility": 64},
        "positions": {"Tank": 0.66, "Support": 0.66, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["guard", "durability", "utility", "sustain"],
             "text": "Agente leal da ADG — corpo reconstruído com aprimoramentos que o trazem de volta de novo e de novo."},
        ],
    },
    # ── Vilões ───────────────────────────────────────────────────────────────
    "Angstrom Levy": {
        "stats": {"power": 64, "durability": 56, "speed": 58, "utility": 88},
        "positions": {"Support": 0.78, "Duelist": 0.66, "Traitor": 0.78},
        "abilities": [
            {"reveal": "season2", "disclosure": "full",
             "tags": ["versatility", "manipulation", "lockdown", "betrayal"],
             "text": "Abre portais entre realidades — desloca, isola ou despeja monstros de outros mundos sobre o inimigo."},
        ],
    },
    "Mauler Twins": {
        "stats": {"power": 70, "durability": 74, "speed": 50, "utility": 80},
        "positions": {"Tank": 0.78, "Support": 0.74, "Duelist": 0.66},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["tank", "durability", "versatility", "utility"],
             "text": "Cientistas-clones gigantes — força bruta somada a engenhocas geniais; reclonam-se quando morrem."},
        ],
    },
    "Machine Head": {
        "stats": {"power": 30, "durability": 38, "speed": 42, "utility": 80},
        "positions": {"Support": 0.78, "Traitor": 0.7, "Captain": 0.5},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["leadership", "manipulation", "utility", "sabotage"],
             "text": "Chefão do crime — implante que processa tudo em tempo real; comanda exércitos de capangas e mercenários."},
        ],
    },
    "Titan": {
        "stats": {"power": 58, "durability": 70, "speed": 48, "utility": 50},
        "positions": {"Tank": 0.8, "Duelist": 0.62},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Pele de rocha — corpo de pedra que resiste a castigo pesado e bate como um aríete."},
        ],
    },
    "Doc Seismic": {
        "stats": {"power": 60, "durability": 54, "speed": 44, "utility": 60},
        "positions": {"Duelist": 0.66, "Support": 0.55},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["aoe", "burst", "lockdown"],
             "text": "Luvas sísmicas — gera terremotos e ergue vulcões, devastando o campo de batalha inteiro."},
        ],
    },
    "D.A. Sinclair": {
        "stats": {"power": 28, "durability": 36, "speed": 40, "utility": 76},
        "positions": {"Support": 0.76, "Traitor": 0.66},
        "abilities": [
            {"reveal": "season1", "disclosure": "full",
             "tags": ["utility", "versatility", "sabotage", "aoe"],
             "text": "Cientista macabro — converte cativos em ReAnimen, soldados ciborgues sem dor nem medo."},
        ],
    },
}


INVINCIBLE_POWER = UniversePower(
    arcs=ARCS,
    reveal_max=REVEAL_MAX,
    profiles=PROFILES,
    default_reveal="later",
)
