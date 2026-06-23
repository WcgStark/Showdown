"""
Naruto power profiles — battle-analysis data.

SPOILER POLICY: a pool tem dois modos — "completo" (Naruto + Boruto) e "naruto"
(clássico, sem a era Boruto). O gate por `reveal` é a segunda camada: tudo da era
Boruto recebe reveal="boruto" e some no modo clássico (REVEAL_MAX para "war").

TRUNFO: como em Dragon Ball, NÃO usamos as tags `domain`/`conqueror` (texto fixo
do motor é de outras franquias). A hierarquia é carregada pela escala de stats.

STAT SCALE: 0–100, não-linear. Tiers aproximados:
    divino (Kaguya, Hagoromo, Naruto/Sasuke do Sábio dos Seis Caminhos) .. 95–100
    Kage lendário (Hashirama, Madara, Minato, Isshiki) .................. 88–96
    Akatsuki de elite / Sannin / Jinchūriki ............................ 78–90
    jōnin forte / Kage / Akatsuki ...................................... 70–84
    chūnin/genin notável ............................................... 48–70
    apoio / civil ...................................................... 8–46
Personagens sem perfil caem no neutro 50.
"""

from __future__ import annotations

from config.power_profiles import UniversePower


# Ordered reveal tiers, earliest → latest (continuidade do anime).
ARCS = [
    "part1",      # Naruto clássico (País das Ondas, Exame Chūnin, resgate de Sasuke)
    "shippuden",  # Shippūden (Akatsuki, Invasão de Pain, Cúpula dos Cinco Kage)
    "war",        # Quarta Grande Guerra Ninja (Madara, Obito, Kaguya)
    "boruto",     # Era Boruto (Kara, Ōtsutsuki, Jigen)
]

REVEAL_MAX = {
    "completo": "boruto",
    "naruto":   "war",
}


# disclosure levels: "full" | "named" | "exists"
PROFILES: dict[str, dict] = {
    # ── Time 7 / protagonistas ───────────────────────────────────────────────
    "Naruto Uzumaki": {
        "stats": {"power": 94, "durability": 90, "speed": 88, "utility": 80},
        "positions": {"Captain": 0.95, "Duelist": 0.95, "Vice Captain": 0.7, "Tank": 0.7},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["bruiser", "burst", "leadership"],
             "text": "Clones das Sombras e Rasengan — enxameia o campo com cópias sólidas e concentra chakra num turbilhão."},
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "Modo Sábio e Jinchūriki da Kurama — sente a natureza e libera o poder da Raposa de Nove Caudas."},
            {"reveal": "war", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "sustain"],
             "text": "Modo Sábio dos Seis Caminhos — chakra de todas as Bestas com Cauda, voo e Rasenshuriken que rasgam o espaço."},
        ],
    },
    "Sasuke Uchiha": {
        "stats": {"power": 92, "durability": 80, "speed": 90, "utility": 78},
        "positions": {"Duelist": 0.96, "Captain": 0.7, "Vice Captain": 0.66},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Sharingan e Chidori — copia técnicas, prevê movimentos e perfura com uma lança de relâmpago."},
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "Mangekyō Sharingan e Susanoo — chamas negras de Amaterasu e um guerreiro etéreo blindado."},
            {"reveal": "war", "disclosure": "full",
             "tags": ["ace", "burst", "lockdown"],
             "text": "Rinnegan dos Seis Caminhos — teletransporte espacial (Amenotejikara) e Susanoo perfeito."},
        ],
    },
    "Sakura Haruno": {
        "stats": {"power": 62, "durability": 56, "speed": 58, "utility": 84},
        "positions": {"Healer": 0.95, "Duelist": 0.7, "Support": 0.66},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["heal", "sustain", "revive", "bruiser"],
             "text": "Ninjutsu Médico e força sobre-humana — cura ferimentos graves e desfere socos que partem o chão; o Selo Yin libera reservas extras."},
        ],
    },
    "Kakashi Hatake": {
        "stats": {"power": 78, "durability": 68, "speed": 78, "utility": 80},
        "positions": {"Captain": 0.8, "Duelist": 0.86, "Vice Captain": 0.7, "Support": 0.6},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["versatility", "burst", "leadership", "recon"],
             "text": "Ninja Copiador — o Sharingan lê e replica mil jutsus; o Raikiri perfura, o Kamui (war) bane o alvo para outra dimensão."},
        ],
    },
    "Might Guy": {
        "stats": {"power": 86, "durability": 70, "speed": 84, "utility": 40},
        "positions": {"Duelist": 0.9, "Tank": 0.66, "Captain": 0.55},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Mestre do taijutsu — abre os Portões Internos para multiplicar força e velocidade muito além do limite."},
            {"reveal": "war", "disclosure": "full",
             "tags": ["ace", "burst", "aoe"],
             "text": "Oitavo Portão (Pavão Noturno) — ao custo da própria vida, golpes que rivalizam com um deus."},
        ],
    },
    "Rock Lee": {
        "stats": {"power": 66, "durability": 60, "speed": 80, "utility": 36},
        "positions": {"Duelist": 0.82, "Tank": 0.55},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Gênio do taijutsu puro — Lótus e abertura dos Portões Internos; pura velocidade e força física."},
        ],
    },
    "Neji Hyūga": {
        "stats": {"power": 60, "durability": 54, "speed": 66, "utility": 60},
        "positions": {"Duelist": 0.78, "Support": 0.55, "Tank": 0.55},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["bruiser", "guard", "debuff", "recon"],
             "text": "Punho Gentil e Byakugan — visão de 360°, fecha os pontos de chakra e gira o Kaiten defensivo."},
        ],
    },
    "Shikamaru Nara": {
        "stats": {"power": 48, "durability": 44, "speed": 50, "utility": 86},
        "positions": {"Support": 0.85, "Vice Captain": 0.66, "Captain": 0.6, "Traitor": 0.5},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["lockdown", "manipulation", "utility", "leadership"],
             "text": "Posse das Sombras — imobiliza e controla o corpo do alvo pela sombra; o estrategista mais brilhante da vila."},
        ],
    },
    "Hinata Hyūga": {
        "stats": {"power": 52, "durability": 50, "speed": 58, "utility": 58},
        "positions": {"Duelist": 0.68, "Support": 0.58},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["bruiser", "guard", "debuff"],
             "text": "Punho Gentil e Byakugan — Leões Gêmeos de chakra e bloqueio dos pontos vitais do inimigo."},
        ],
    },
    "Gaara": {
        "stats": {"power": 80, "durability": 82, "speed": 60, "utility": 72},
        "positions": {"Tank": 0.9, "Duelist": 0.8, "Captain": 0.7},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["tank", "durability", "guard", "aoe", "lockdown"],
             "text": "Controle da Areia — escudo automático que esmaga e aprisiona (Caixão de Areia); como Kazekage, defesa absoluta."},
        ],
    },
    # ── Sannin & Kages ───────────────────────────────────────────────────────
    "Jiraiya": {
        "stats": {"power": 82, "durability": 74, "speed": 72, "utility": 80},
        "positions": {"Duelist": 0.86, "Captain": 0.7, "Support": 0.62},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["ace", "burst", "versatility", "leadership"],
             "text": "Modo Sábio dos Sapos — Rasengan ampliado, invocação do Chefe Sapo e ninjutsu versátil."},
        ],
    },
    "Tsunade": {
        "stats": {"power": 78, "durability": 76, "speed": 64, "utility": 88},
        "positions": {"Healer": 1.0, "Duelist": 0.78, "Captain": 0.7, "Tank": 0.66},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["heal", "revive", "sustain", "bruiser"],
             "text": "Selo Yin (Criação) e Ninjutsu Médico supremo — regenera o próprio corpo continuamente e cura toda a aldeia; socos que demolem."},
        ],
    },
    "Orochimaru": {
        "stats": {"power": 80, "durability": 78, "speed": 68, "utility": 88},
        "positions": {"Duelist": 0.8, "Support": 0.72, "Traitor": 0.8, "Captain": 0.6},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["versatility", "sustain", "manipulation", "sabotage", "betrayal"],
             "text": "Imortalidade por troca de corpos, invocação de serpentes e Edo Tensei — ressuscita os mortos como soldados."},
        ],
    },
    "Hashirama Senju": {
        "stats": {"power": 94, "durability": 90, "speed": 80, "utility": 88},
        "positions": {"Captain": 0.9, "Duelist": 0.92, "Tank": 0.78, "Support": 0.66},
        "abilities": [
            {"reveal": "war", "disclosure": "full",
             "tags": ["ace", "aoe", "tank", "sustain", "leadership"],
             "text": "Estilo Madeira — florestas e golems colossais; o Deus da Shinobi com regeneração e Modo Sábio."},
        ],
    },
    "Tobirama Senju": {
        "stats": {"power": 86, "durability": 76, "speed": 88, "utility": 84},
        "positions": {"Duelist": 0.88, "Support": 0.7, "Captain": 0.66},
        "abilities": [
            {"reveal": "war", "disclosure": "full",
             "tags": ["ace", "burst", "versatility", "lockdown"],
             "text": "Mestre do Estilo Água e do Voo do Trovão — teletransporte por selos e criador do Edo Tensei."},
        ],
    },
    "Minato Namikaze": {
        "stats": {"power": 88, "durability": 76, "speed": 96, "utility": 82},
        "positions": {"Duelist": 0.94, "Captain": 0.78, "Vice Captain": 0.66},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "Relâmpago Amarelo — teletransporte instantâneo (Hiraishin) e Rasengan; reflexos imbatíveis."},
        ],
    },
    "Hiruzen Sarutobi": {
        "stats": {"power": 78, "durability": 68, "speed": 66, "utility": 84},
        "positions": {"Captain": 0.72, "Duelist": 0.78, "Support": 0.62},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["ace", "versatility", "leadership"],
             "text": "O Professor — dominava todos os jutsus da vila; invoca Enma e usa o selo da morte (Shiki Fūjin)."},
        ],
    },
    "Ōnoki": {
        "stats": {"power": 80, "durability": 64, "speed": 60, "utility": 78},
        "positions": {"Duelist": 0.8, "Captain": 0.66, "Support": 0.6},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "versatility"],
             "text": "Estilo Pó (Liberação de Partículas) — desintegra o alvo em escala atômica; manipula o próprio peso para voar."},
        ],
    },
    "A (Fourth Raikage)": {
        "stats": {"power": 84, "durability": 82, "speed": 90, "utility": 56},
        "positions": {"Duelist": 0.88, "Tank": 0.72, "Captain": 0.66},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["bruiser", "burst", "durability"],
             "text": "Manto de Relâmpago — velocidade que rivaliza com o Hiraishin e golpes de força demolidora."},
        ],
    },
    "Killer B": {
        "stats": {"power": 84, "durability": 84, "speed": 76, "utility": 64},
        "positions": {"Duelist": 0.86, "Tank": 0.78, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["bruiser", "burst", "tank", "durability"],
             "text": "Jinchūriki do Gyūki (Oito Caudas) — controle pleno da Besta com Cauda e kenjutsu de sete espadas."},
        ],
    },
    "Mei Terumī": {
        "stats": {"power": 72, "durability": 60, "speed": 66, "utility": 64},
        "positions": {"Duelist": 0.78, "Captain": 0.62},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["burst", "aoe", "debuff"],
             "text": "Estilos Lava e Vapor — derrete defesas com ácido e cobre o campo de névoa escaldante; a Mizukage."},
        ],
    },
    # ── Akatsuki ───────────────────────────────────────────────────────────
    "Itachi Uchiha": {
        "stats": {"power": 86, "durability": 70, "speed": 82, "utility": 86},
        "positions": {"Duelist": 0.92, "Support": 0.66, "Traitor": 0.7, "Captain": 0.62},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["ace", "burst", "manipulation", "lockdown", "versatility"],
             "text": "Mangekyō Sharingan — Tsukuyomi prende a mente, Amaterasu queima sem apagar e o Susanoo empunha a Espada de Totsuka que sela o alvo."},
        ],
    },
    "Nagato": {
        "stats": {"power": 88, "durability": 70, "speed": 70, "utility": 90},
        "positions": {"Duelist": 0.88, "Captain": 0.7, "Support": 0.7},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["ace", "aoe", "burst", "versatility", "revive"],
             "text": "Os Seis Caminhos de Pain e o Rinnegan — repulsão gravitacional que arrasa vilas, controle de almas e ressurreição dos mortos."},
        ],
    },
    "Konan": {
        "stats": {"power": 66, "durability": 56, "speed": 62, "utility": 64},
        "positions": {"Duelist": 0.74, "Support": 0.62},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["aoe", "versatility", "lockdown"],
             "text": "Estilo Papel — corpo desfeito em folhas explosivas; um mar de bilhões de tags-bomba como armadilha final."},
        ],
    },
    "Kisame Hoshigaki": {
        "stats": {"power": 80, "durability": 78, "speed": 70, "utility": 70},
        "positions": {"Duelist": 0.86, "Tank": 0.7},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["bruiser", "sustain", "aoe", "versatility"],
             "text": "Samehada e Estilo Água — a espada viva drena chakra sem fim; inunda o campo e funde-se à água como um tubarão."},
        ],
    },
    "Deidara": {
        "stats": {"power": 72, "durability": 56, "speed": 64, "utility": 68},
        "positions": {"Duelist": 0.78, "Support": 0.55},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["burst", "aoe", "versatility"],
             "text": "Argila Explosiva — esculturas-bomba que voam e detonam; a 'arte é uma explosão', até o C0 suicida."},
        ],
    },
    "Sasori": {
        "stats": {"power": 70, "durability": 66, "speed": 60, "utility": 80},
        "positions": {"Support": 0.74, "Duelist": 0.72, "Tank": 0.6},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["versatility", "debuff", "aoe", "sustain"],
             "text": "Mestre das Marionetes — um exército de cem fantoches venenosos e o próprio corpo convertido em boneco imortal."},
        ],
    },
    "Hidan": {
        "stats": {"power": 60, "durability": 78, "speed": 56, "utility": 58},
        "positions": {"Tank": 0.8, "Duelist": 0.66, "Traitor": 0.6},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["tank", "durability", "debuff", "sustain"],
             "text": "Ritual de Jashin — imortal: ao provar o sangue do alvo, todo dano que sofre é refletido na vítima."},
        ],
    },
    "Kakuzu": {
        "stats": {"power": 76, "durability": 80, "speed": 64, "utility": 66},
        "positions": {"Tank": 0.82, "Duelist": 0.78},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["tank", "durability", "burst", "aoe", "sustain"],
             "text": "Cinco corações e máscaras elementais — sobrevive a golpes fatais e dispara fogo, vento e raio simultâneos."},
        ],
    },
    "Obito Uchiha": {
        "stats": {"power": 90, "durability": 78, "speed": 80, "utility": 88},
        "positions": {"Duelist": 0.9, "Captain": 0.72, "Traitor": 0.75},
        "abilities": [
            {"reveal": "war", "disclosure": "full",
             "tags": ["ace", "burst", "versatility", "lockdown", "betrayal"],
             "text": "Kamui — atravessa qualquer ataque tornando-se intangível e bane alvos a outra dimensão; Jinchūriki dos Dez Caudas."},
        ],
    },
    "Madara Uchiha": {
        "stats": {"power": 96, "durability": 90, "speed": 86, "utility": 90},
        "positions": {"Captain": 0.92, "Duelist": 0.96, "Tank": 0.78},
        "abilities": [
            {"reveal": "war", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "sustain", "leadership"],
             "text": "Rinnegan e Susanoo Perfeito — meteoros, Estilo Madeira, Limbo (sombras invisíveis) e regeneração; Jinchūriki dos Dez Caudas."},
        ],
    },
    "Kaguya Ōtsutsuki": {
        "stats": {"power": 100, "durability": 96, "speed": 92, "utility": 96},
        "positions": {"Captain": 0.92, "Duelist": 0.98, "Tank": 0.8},
        "abilities": [
            {"reveal": "war", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "lockdown", "versatility"],
             "text": "Deusa Coelha — abre portais entre dimensões à vontade, manipula a matéria e drena o chakra de todos; o Tsukuyomi Infinito."},
        ],
    },
    "Hagoromo Ōtsutsuki": {
        "stats": {"power": 98, "durability": 90, "speed": 88, "utility": 96},
        "positions": {"Captain": 0.85, "Duelist": 0.92, "Support": 0.72},
        "abilities": [
            {"reveal": "war", "disclosure": "full",
             "tags": ["ace", "versatility", "leadership", "buff"],
             "text": "O Sábio dos Seis Caminhos — pai do ninjutsu; concede chakra e poderes aos aliados e sela ameaças cósmicas."},
        ],
    },
    "Black Zetsu": {
        "stats": {"power": 50, "durability": 60, "speed": 54, "utility": 84},
        "positions": {"Support": 0.78, "Traitor": 0.82, "Duelist": 0.5},
        "abilities": [
            {"reveal": "war", "disclosure": "full",
             "tags": ["manipulation", "betrayal", "sabotage", "versatility"],
             "text": "Vontade de Kaguya — funde-se a qualquer um para controlá-lo; arquiteto milenar de toda a trama."},
        ],
    },
    # ── Aliados de Konoha / outros ───────────────────────────────────────────
    "Yamato": {
        "stats": {"power": 64, "durability": 64, "speed": 58, "utility": 76},
        "positions": {"Tank": 0.74, "Support": 0.72, "Duelist": 0.6},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["guard", "lockdown", "tank", "utility"],
             "text": "Estilo Madeira — ergue paredes, prisões e estruturas; contém e suprime o chakra das Bestas com Cauda."},
        ],
    },
    "Sai": {
        "stats": {"power": 56, "durability": 50, "speed": 60, "utility": 66},
        "positions": {"Support": 0.7, "Duelist": 0.62, "Traitor": 0.5},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["versatility", "recon", "aoe"],
             "text": "Pintura Ninja Super Bestial — desenhos de tinta que ganham vida para atacar, espionar e transportar."},
        ],
    },
    "Temari": {
        "stats": {"power": 62, "durability": 52, "speed": 60, "utility": 60},
        "positions": {"Duelist": 0.74, "Support": 0.55},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["aoe", "burst", "versatility"],
             "text": "Leque Gigante — lâminas de vento de longo alcance que varrem o campo."},
        ],
    },
    "Chiyo": {
        "stats": {"power": 56, "durability": 48, "speed": 52, "utility": 80},
        "positions": {"Healer": 0.82, "Support": 0.7, "Duelist": 0.58},
        "abilities": [
            {"reveal": "shippuden", "disclosure": "full",
             "tags": ["heal", "revive", "versatility", "lockdown"],
             "text": "Anciã das Marionetes — controla dezenas de fantoches e domina a técnica de transmutação que devolve a vida (ao custo da sua)."},
        ],
    },
    "Kabuto Yakushi": {
        "stats": {"power": 74, "durability": 72, "speed": 70, "utility": 84},
        "positions": {"Support": 0.76, "Duelist": 0.74, "Traitor": 0.7, "Healer": 0.6},
        "abilities": [
            {"reveal": "war", "disclosure": "full",
             "tags": ["sustain", "heal", "manipulation", "versatility", "betrayal"],
             "text": "Modo Sábio das Serpentes e Edo Tensei aprimorado — regeneração, dissecação médica e um exército de mortos reanimados."},
        ],
    },
    "Zabuza Momochi": {
        "stats": {"power": 64, "durability": 58, "speed": 64, "utility": 60},
        "positions": {"Duelist": 0.78, "Vice Captain": 0.55, "Traitor": 0.55},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["bruiser", "burst", "versatility", "recon"],
             "text": "Demônio da Névoa Oculta — Estilo Água e a Espada Decapitadora; ataca de dentro de uma névoa que cega o inimigo."},
        ],
    },
    "Haku": {
        "stats": {"power": 58, "durability": 48, "speed": 78, "utility": 56},
        "positions": {"Duelist": 0.74, "Support": 0.5},
        "abilities": [
            {"reveal": "part1", "disclosure": "full",
             "tags": ["burst", "lockdown", "versatility"],
             "text": "Espelhos de Gelo Cristalino — cerca o alvo com espelhos e ataca de todos os lados em velocidade ofuscante."},
        ],
    },
    # ── Era Boruto ───────────────────────────────────────────────────────────
    "Boruto Uzumaki": {
        "stats": {"power": 78, "durability": 68, "speed": 78, "utility": 70},
        "positions": {"Duelist": 0.84, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "boruto", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "Jougan e o Karma — Rasengan que some, percepção de fluxos de chakra e o poder Ōtsutsuki crescendo nele."},
        ],
    },
    "Kawaki": {
        "stats": {"power": 82, "durability": 74, "speed": 74, "utility": 70},
        "positions": {"Duelist": 0.86, "Tank": 0.62},
        "abilities": [
            {"reveal": "boruto", "disclosure": "full",
             "tags": ["ace", "burst", "versatility", "guard"],
             "text": "Karma — absorve e remodela ninjutsu, transforma o corpo em armas e devolve qualquer técnica."},
        ],
    },
    "Isshiki Ōtsutsuki": {
        "stats": {"power": 96, "durability": 88, "speed": 92, "utility": 88},
        "positions": {"Captain": 0.9, "Duelist": 0.96, "Tank": 0.74},
        "abilities": [
            {"reveal": "boruto", "disclosure": "full",
             "tags": ["ace", "burst", "lockdown", "versatility"],
             "text": "Sukunahikona e Daikokuten — encolhe e amplia qualquer objeto à vontade e os teletransporta; um Ōtsutsuki quase imbatível."},
        ],
    },
    "Jigen": {
        "stats": {"power": 92, "durability": 84, "speed": 86, "utility": 80},
        "positions": {"Duelist": 0.92, "Captain": 0.78, "Tank": 0.7},
        "abilities": [
            {"reveal": "boruto", "disclosure": "full",
             "tags": ["ace", "burst", "lockdown", "versatility"],
             "text": "Recipiente de Isshiki — bastões de chakra negro e teletransporte dimensional; supera os Kage com folga."},
        ],
    },
    "Code": {
        "stats": {"power": 84, "durability": 76, "speed": 80, "utility": 66},
        "positions": {"Duelist": 0.86, "Tank": 0.62},
        "abilities": [
            {"reveal": "boruto", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "Karma Branco e Marcas de Claw — abre portais para deslocar golpes pelo espaço; força liberada sem limitador."},
        ],
    },
    "Delta": {
        "stats": {"power": 72, "durability": 74, "speed": 66, "utility": 56},
        "positions": {"Duelist": 0.78, "Tank": 0.64},
        "abilities": [
            {"reveal": "boruto", "disclosure": "full",
             "tags": ["burst", "aoe", "durability"],
             "text": "Ciborgue da Kara — olhos que disparam rajadas devastadoras e corpo modificado de alta resistência."},
        ],
    },
    "Koji Kashin": {
        "stats": {"power": 80, "durability": 66, "speed": 72, "utility": 70},
        "positions": {"Duelist": 0.82, "Support": 0.6, "Traitor": 0.6},
        "abilities": [
            {"reveal": "boruto", "disclosure": "full",
             "tags": ["burst", "aoe", "versatility", "betrayal"],
             "text": "Clone de Jiraiya — Modo Sábio dos Sapos e um Estilo Fogo intenso o bastante para ferir os Interiores da Kara."},
        ],
    },
}


NARUTO_POWER = UniversePower(
    arcs=ARCS,
    reveal_max=REVEAL_MAX,
    profiles=PROFILES,
    default_reveal="boruto",
)
