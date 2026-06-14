"""
Jujutsu Kaisen power profiles — pilot for the battle-analysis system.

SPOILER POLICY for this universe: the "completo" mode covers the anime up to the
Culling Game. So `reveal_max` stops at "culling_game", and any ability shown only
later in the manga must be tagged with a later arc (and will be hidden), OR kept
visible but written at a safe `disclosure` level.

The Yuta case is the reference for `disclosure="exists"`: his domain expansion is
acknowledged to EXIST and to be usable to nullify an enemy domain (tag
"domain_counter"), but its actual effect is never described.

STAT SCALE: 0–100, intentionally NON-linear so power tiers are dramatic — drafting
a Gojo/Sukuna should tower over a team of fodder. Rough tiers:
    god (Gojo, Sukuna) ........ 95–100
    special grade ............. 78–92
    grade 1 (strong) .......... 50–78
    grade 2 / mid ............. 35–55
    support / civilians ....... 8–35   (a healer is weak in power, huge in utility)
Calibrate to taste; characters with no profile fall back to a neutral 50.
"""

from __future__ import annotations

from config.power_profiles import UniversePower


# Ordered reveal tiers, earliest → latest (anime continuity).
ARCS = [
    "intro",          # Fushiguro/Itadori intro, Cursed Womb
    "vs_mahito",      # Junpei / Mahito introduction
    "kyoto_event",    # Goodwill Event (Todo, Kyoto students)
    "death_painting", # Death Paintings / Choso intro
    "shibuya",        # Shibuya Incident
    "perfect_prep",   # Itadori's extermination / aftermath
    "culling_game",   # Culling Game (anime boundary for "completo")
]

REVEAL_MAX = {
    "completo": "culling_game",
    "teste":    "culling_game",
}


# disclosure levels: "full" | "named" | "exists"
PROFILES: dict[str, dict] = {
    # ── Protagonistas ──────────────────────────────────────────────────────
    "Yuji Itadori": {
        "stats": {"power": 62, "durability": 70, "speed": 60, "utility": 35},
        "positions": {"Duelist": 0.85, "Tank": 0.7, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Físico sobre-humano — força e resistência muito acima do normal."},
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["burst"],
             "text": "Punho Divergente e Lampejo Negro — segundo impacto e golpes amplificados."},
            {"reveal": "intro", "disclosure": "named",
             "tags": ["versatility"],
             "text": "Recipiente de Sukuna — abriga o Rei das Maldições (risco e poder latente)."},
            # His own cursed technique is never mentioned within the anime
            # boundary, so we don't acknowledge it at all.
        ],
    },
    "Megumi Fushiguro": {
        "stats": {"power": 68, "durability": 60, "speed": 64, "utility": 80},
        "positions": {"Tank": 0.85, "Duelist": 0.78, "Support": 0.72, "Vice Captain": 0.72, "Captain": 0.6},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["versatility", "guard", "lockdown"],
             "text": "Técnica das Dez Sombras — invoca shikigami para atacar e defender."},
            {"reveal": "death_painting", "disclosure": "named",
             "tags": ["domain", "domain_counter", "lockdown"],
             "text": "Possui uma expansão de domínio incompleta (Jardim Sombrio Profundo)."},
        ],
    },
    "Nobara Kugisaki": {
        "stats": {"power": 48, "durability": 40, "speed": 42, "utility": 50},
        "positions": {"Duelist": 0.75, "Support": 0.6},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["burst", "debuff", "utility"],
             "text": "Técnica do Boneco de Palha — Ressonância ataca o alvo à distância via objeto amaldiçoado."},
        ],
    },
    # ── Professores e feiticeiros de Tokyo ─────────────────────────────────
    "Satoru Gojo": {
        "stats": {"power": 100, "durability": 95, "speed": 100, "utility": 95},
        "positions": {"Captain": 1.0, "Duelist": 0.9, "Tank": 0.75, "Support": 0.6, "Healer": 0.65},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["ace", "leadership", "lockdown"],
             "text": "Limitless + Seis Olhos: Infinito torna ataques diretos quase inúteis."},
            {"reveal": "intro", "disclosure": "full",
             "tags": ["domain", "domain_counter", "aoe"],
             "text": "Expansão de Domínio (Vazio Infinito) — anula domínios inimigos."},
            {"reveal": "intro", "disclosure": "full",
             "tags": ["heal", "sustain"],
             "text": "Técnica Reversa — energia amaldiçoada positiva que cura ferimentos graves."},
        ],
    },
    "Kento Nanami": {
        "stats": {"power": 62, "durability": 62, "speed": 52, "utility": 52},
        "positions": {"Duelist": 0.8, "Tank": 0.7, "Vice Captain": 0.7},
        "abilities": [
            {"reveal": "vs_mahito", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Técnica do Ponto Fraco (Razão 7:3) — cria pontos de corte fatais."},
        ],
    },
    "Shoko Ieiri": {
        "stats": {"power": 14, "durability": 22, "speed": 35, "utility": 90},
        "positions": {"Healer": 1.0, "Support": 0.6},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["heal", "sustain", "revive"],
             "text": "Técnica de Cura Reversa — trata ferimentos graves dos aliados."},
        ],
    },
    "Masamichi Yaga": {
        "stats": {"power": 35, "durability": 35, "speed": 28, "utility": 58},
        "positions": {"Support": 0.75, "Captain": 0.55, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["utility", "versatility", "leadership"],
             "text": "Manipulação de Corpos Amaldiçoados — cria bonecos de combate autônomos."},
        ],
    },
    # ── Alunos Tokyo ───────────────────────────────────────────────────────
    "Maki Zenin": {
        "stats": {"power": 80, "durability": 74, "speed": 86, "utility": 55},
        "positions": {"Duelist": 0.9, "Tank": 0.72, "Vice Captain": 0.62, "Captain": 0.6},
        "abilities": [
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Mestra em ferramentas amaldiçoadas — domina arsenal de armas especiais."},
            {"reveal": "intro", "disclosure": "full",
             "tags": ["versatility", "guard"],
             "text": "Restrição Celestial — sem energia amaldiçoada, físico e percepção sobre-humanos."},
            # Awakened state (Perfect Preparation arc, within the Culling Game
            # boundary). Describe the POWER, not the events behind it.
            {"reveal": "perfect_prep", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst"],
             "text": "Restrição Celestial plena — força física que rivaliza com feiticeiros de grau especial."},
        ],
    },
    "Toge Inumaki": {
        "stats": {"power": 45, "durability": 25, "speed": 38, "utility": 75},
        "positions": {"Support": 0.95, "Duelist": 0.5},
        "abilities": [
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["buff", "debuff", "lockdown", "utility"],
             "text": "Fala Amaldiçoada — comandos que paralisam, repelem ou ferem inimigos."},
        ],
    },
    "Panda": {
        "stats": {"power": 48, "durability": 62, "speed": 38, "utility": 40},
        "positions": {"Tank": 0.85, "Duelist": 0.6},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["tank", "durability", "guard"],
             "text": "Corpo amaldiçoado resistente — encara dano de frente."},
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Núcleos múltiplos — alterna para o Núcleo Gorila, trocando defesa por potência."},
        ],
    },
    # ── Alunos Kyoto ───────────────────────────────────────────────────────
    "Aoi Todo": {
        "stats": {"power": 78, "durability": 66, "speed": 66, "utility": 68},
        "positions": {"Duelist": 0.85, "Support": 0.75, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["versatility", "utility", "burst"],
             "text": "Boogie Woogie — troca a posição de alvos com uma palma, reposicionando a luta."},
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["bruiser"],
             "text": "Físico de elite e domínio do Lampejo Negro."},
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["anti_domain", "guard"],
             "text": "Domínio Simples — barreira que anula o acerto garantido de expansões de domínio."},
        ],
    },
    "Mai Zenin": {
        "stats": {"power": 24, "durability": 24, "speed": 35, "utility": 40},
        "positions": {"Support": 0.6, "Duelist": 0.5},
        "abilities": [
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["utility", "burst"],
             "text": "Técnica de Construção — materializa objetos (como projéteis) a alto custo."},
        ],
    },
    "Kasumi Miwa": {
        "stats": {"power": 24, "durability": 24, "speed": 45, "utility": 28},
        "positions": {"Duelist": 0.6, "Tank": 0.55},
        "abilities": [
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["guard", "burst", "anti_domain"],
             "text": "Novo Estilo das Sombras (Saque Veloz) e Domínio Simples — barreira que anula o acerto garantido de expansões de domínio."},
        ],
    },
    "Noritoshi Kamo": {
        "stats": {"power": 48, "durability": 40, "speed": 48, "utility": 50},
        "positions": {"Duelist": 0.7, "Support": 0.6, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["versatility", "burst"],
             "text": "Manipulação de Sangue — flechas e jatos de sangue de longo alcance."},
        ],
    },
    "Mechamaru": {
        "stats": {"power": 45, "durability": 14, "speed": 35, "utility": 75},
        "positions": {"Support": 0.8, "Traitor": 0.7, "Duelist": 0.55},
        "abilities": [
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["utility", "versatility", "recon"],
             "text": "Marionete (Ultimate Mechamaru) — controla um corpo de combate à distância."},
            {"reveal": "shibuya", "disclosure": "named",
             "tags": ["betrayal", "sabotage"],
             "text": "Restrição Celestial inversa — enorme energia amaldiçoada num corpo frágil; firmou pacto duvidoso."},
        ],
    },
    "Momo Nishimiya": {
        "stats": {"power": 16, "durability": 16, "speed": 45, "utility": 50},
        "positions": {"Support": 0.75},
        "abilities": [
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["recon", "utility"],
             "text": "Voa numa vassoura amaldiçoada — reconhecimento e mobilidade pelo campo."},
        ],
    },
    # ── Aliados ────────────────────────────────────────────────────────────
    "Yuta Okkotsu": {
        "stats": {"power": 95, "durability": 74, "speed": 86, "utility": 84},
        "positions": {"Duelist": 0.92, "Captain": 0.72, "Support": 0.55, "Healer": 0.6},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["versatility", "utility"],
             "text": "Copia técnicas amaldiçoadas de outros feiticeiros."},
            {"reveal": "intro", "disclosure": "full",
             "tags": ["bruiser", "ace", "burst"],
             "text": "Manifesta Rika — reserva colossal de energia amaldiçoada."},
            {"reveal": "intro", "disclosure": "full",
             "tags": ["heal", "sustain"],
             "text": "Técnica Reversa — energia positiva suficiente para curar a si e aliados."},
            # Acknowledged to exist (cited during the Ishigori fight in the
            # Culling Game) AND that he can use it to nullify an opponent's —
            # but never WHAT it actually does.
            {"reveal": "culling_game", "disclosure": "exists",
             "tags": ["domain", "domain_counter"],
             "text": "Possui uma expansão de domínio — pode usá-la para anular a de um oponente."},
        ],
    },
    "Mei Mei": {
        "stats": {"power": 60, "durability": 40, "speed": 50, "utility": 52},
        "positions": {"Duelist": 0.7, "Support": 0.6, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["versatility", "recon", "burst"],
             "text": "Manipulação de Corvos — reconhecimento e a Manobra do Pássaro Negro, golpe garantido proporcional ao risco."},
        ],
    },
    "Ui Ui": {
        "stats": {"power": 16, "durability": 16, "speed": 35, "utility": 60},
        "positions": {"Support": 0.75},
        "abilities": [
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["utility", "versatility"],
             "text": "Teletransporta aliados pelo campo — reposiciona o time instantaneamente."},
        ],
    },
    "Naobito Zenin": {
        "stats": {"power": 62, "durability": 40, "speed": 90, "utility": 52},
        "positions": {"Duelist": 0.8, "Captain": 0.6, "Vice Captain": 0.65},
        "abilities": [
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["bruiser", "burst", "leadership"],
             "text": "Feitiçaria de Projeção — move-se em 24 quadros por segundo; quem falha o ritmo congela."},
        ],
    },
    "Naoya Zenin": {
        "stats": {"power": 60, "durability": 40, "speed": 88, "utility": 40},
        "positions": {"Duelist": 0.8},
        "abilities": [
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Feitiçaria de Projeção — velocidade extrema que aprisiona quem não acompanha o ritmo."},
        ],
    },
    "Choso": {
        "stats": {"power": 62, "durability": 64, "speed": 50, "utility": 52},
        "positions": {"Duelist": 0.8, "Tank": 0.6, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["bruiser", "burst", "versatility"],
             "text": "Manipulação de Sangue — Sangue Perfurante, Convergência e Escama Rubra reforçando o corpo."},
        ],
    },
    # ── Vilões — Maldições ─────────────────────────────────────────────────
    "Ryomen Sukuna": {
        "stats": {"power": 99, "durability": 95, "speed": 92, "utility": 85},
        "positions": {"Duelist": 1.0, "Captain": 0.85, "Tank": 0.6, "Healer": 0.55},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["bruiser", "ace", "burst"],
             "text": "Corte e Despedaçar — talho de curta e longa distância."},
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["domain", "domain_counter", "aoe"],
             "text": "Expansão de Domínio (Santuário Maligno) — acerto garantido em área."},
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["heal", "sustain"],
             "text": "Técnica Reversa — regenera o próprio corpo com energia positiva."},
        ],
    },
    "Mahito": {
        "stats": {"power": 80, "durability": 66, "speed": 66, "utility": 78},
        "positions": {"Duelist": 0.85, "Support": 0.55, "Healer": 0.45},
        "abilities": [
            {"reveal": "vs_mahito", "disclosure": "full",
             "tags": ["versatility", "manipulation", "burst"],
             "text": "Transfiguração Ociosa — remodela a alma ao toque, deformando corpos."},
            {"reveal": "vs_mahito", "disclosure": "full",
             "tags": ["heal"],
             "text": "Remodela a própria alma para se reconstituir — cura limitada de si mesmo."},
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["domain", "domain_counter", "aoe"],
             "text": "Expansão de Domínio (Personificação do Eu Perfeito) — toca a alma de quem entra."},
        ],
    },
    "Jogo": {
        "stats": {"power": 78, "durability": 82, "speed": 52, "utility": 66},
        "positions": {"Duelist": 0.82, "Tank": 0.75, "Captain": 0.6},
        "abilities": [
            {"reveal": "vs_mahito", "disclosure": "full",
             "tags": ["bruiser", "burst", "aoe"],
             "text": "Manipulação de fogo e magma — Chamas do Desastre e erupções em área."},
            {"reveal": "vs_mahito", "disclosure": "full",
             "tags": ["tank", "durability", "guard"],
             "text": "Corpo de magma e crânio vulcânico — aguenta golpes pesados sem ceder."},
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["domain", "domain_counter", "aoe"],
             "text": "Expansão de Domínio (Caixão da Montanha de Ferro) — preenche a área com calor vulcânico."},
        ],
    },
    "Hanami": {
        "stats": {"power": 64, "durability": 76, "speed": 52, "utility": 54},
        "positions": {"Tank": 0.75, "Duelist": 0.7},
        "abilities": [
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["tank", "durability", "debuff", "versatility"],
             "text": "Manipulação de plantas — raízes, sementes drenantes e flores que sugam energia amaldiçoada."},
            {"reveal": "kyoto_event", "disclosure": "full",
             "tags": ["anti_domain", "guard"],
             "text": "Ampliação de Domínio — reveste-se de barreira que anula técnicas e domínios ao toque."},
        ],
    },
    "Dagon": {
        "stats": {"power": 62, "durability": 64, "speed": 52, "utility": 66},
        "positions": {"Tank": 0.7, "Duelist": 0.7},
        "abilities": [
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["versatility", "guard"],
             "text": "Invoca shikigami marinhos para enxamear e proteger."},
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["domain", "domain_counter", "aoe", "lockdown"],
             "text": "Expansão de Domínio (Horizonte do Skandha Cativante) — praia infinita de shikigami inesgotáveis."},
        ],
    },
    # ── Vilões — Usuários de Jujutsu ───────────────────────────────────────
    "Suguru Geto": {
        "stats": {"power": 80, "durability": 52, "speed": 52, "utility": 90},
        "positions": {"Captain": 0.8, "Support": 0.75, "Traitor": 0.6},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["versatility", "utility", "leadership"],
             "text": "Manipulação de Espíritos Amaldiçoados — absorve e comanda um arsenal de maldições."},
            {"reveal": "shibuya", "disclosure": "named",
             "tags": ["aoe", "burst"],
             "text": "Uzumaki Máximo — funde maldições absorvidas num único disparo devastador."},
        ],
    },
    "Haruta Shigemo": {
        "stats": {"power": 36, "durability": 28, "speed": 48, "utility": 50},
        "positions": {"Duelist": 0.6, "Traitor": 0.5},
        "abilities": [
            {"reveal": "shibuya", "disclosure": "full",
             "tags": ["versatility", "utility"],
             "text": "Técnica ligada à sorte — manipula a probabilidade a seu favor em combate."},
        ],
    },
    "Toji Fushiguro": {
        "stats": {"power": 68, "durability": 72, "speed": 84, "utility": 60},
        "positions": {"Duelist": 0.95, "Captain": 0.6, "Traitor": 0.6},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["bruiser", "ace", "burst"],
             "text": "Restrição Celestial — físico sobre-humano e invisível ao sentido amaldiçoado."},
            {"reveal": "intro", "disclosure": "full",
             "tags": ["versatility", "utility"],
             "text": "Inventário de Maldições — arsenal de ferramentas amaldiçoadas para qualquer alvo."},
        ],
    },
    # ── Culling Game (parcial) ─────────────────────────────────────────────
    "Kirara Hoshi": {
        "stats": {"power": 26, "durability": 26, "speed": 38, "utility": 62},
        "positions": {"Support": 0.8, "Duelist": 0.5},
        "abilities": [
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["utility", "debuff", "lockdown"],
             "text": "Encontro Amoroso — atribui polos magnéticos que atraem ou repelem alvos."},
        ],
    },
    "Higuruma Hiromi": {
        "stats": {"power": 86, "durability": 66, "speed": 60, "utility": 82},
        "positions": {"Duelist": 0.85, "Tank": 0.65, "Support": 0.55, "Traitor": 0.6},
        "abilities": [
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Exímio com a lâmina amaldiçoada — combatente perigoso mesmo fora do domínio."},
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["domain", "domain_counter", "manipulation", "lockdown", "guard", "ace"],
             "text": "Tribunal Privado — domínio de julgamento: neutraliza a violência dos presentes e, ao 'culpado', uma lâmina executora abate ao toque e confisca sua técnica."},
        ],
    },
    "Reggie Star": {
        "stats": {"power": 48, "durability": 48, "speed": 48, "utility": 60},
        "positions": {"Duelist": 0.7, "Support": 0.6, "Healer": 0.5},
        "abilities": [
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["versatility", "utility"],
             "text": "Materializa objetos a partir de recibos — versátil em ataque e armadilha."},
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["heal"],
             "text": "Materializa itens de recuperação a partir de recibos — cura pontual."},
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["anti_domain"],
             "text": "Recurso anti-domínio — neutraliza a expansão de domínio inimiga."},
        ],
    },
    "Remi": {
        "stats": {"power": 26, "durability": 26, "speed": 38, "utility": 28},
        "positions": {"Duelist": 0.5, "Support": 0.5},
        "abilities": [
            {"reveal": "culling_game", "disclosure": "named",
             "tags": ["utility"],
             "text": "Feiticeira participante do Jogo do Abate — técnica de apoio."},
        ],
    },
    "Ryu Ishigori": {
        "stats": {"power": 88, "durability": 74, "speed": 62, "utility": 60},
        "positions": {"Duelist": 0.9, "Tank": 0.62, "Captain": 0.55},
        "abilities": [
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["bruiser", "burst", "aoe"],
             "text": "Explosão de Granito — disparo de energia amaldiçoada bruta e contínua."},
            # Has a domain; its effect is never disclosed.
            {"reveal": "culling_game", "disclosure": "exists",
             "tags": ["domain", "domain_counter"],
             "text": "Possui uma expansão de domínio (efeito não revelado)."},
        ],
    },
    "Takako Uro": {
        "stats": {"power": 80, "durability": 66, "speed": 76, "utility": 66},
        "positions": {"Duelist": 0.9, "Captain": 0.55, "Support": 0.5},
        "abilities": [
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["versatility", "burst", "aoe", "bruiser", "lockdown"],
             "text": "Trata o céu como superfície — distorce e 'esfrega' o espaço aéreo contra o alvo."},
            # Has a domain; its effect is never disclosed.
            {"reveal": "culling_game", "disclosure": "exists",
             "tags": ["domain", "domain_counter"],
             "text": "Possui uma expansão de domínio (efeito não revelado)."},
        ],
    },
    "Dhruv Lakdawalla": {
        "stats": {"power": 74, "durability": 68, "speed": 64, "utility": 58},
        "positions": {"Duelist": 0.82, "Tank": 0.62, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["bruiser", "burst", "versatility"],
             "text": "Feiticeiro veterano do Jogo do Abate — combate físico apoiado por shikigami."},
        ],
    },
    "Kurourushi": {
        "stats": {"power": 72, "durability": 90, "speed": 46, "utility": 60},
        "positions": {"Tank": 0.82, "Duelist": 0.6},
        "abilities": [
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["tank", "durability", "guard", "aoe"],
             "text": "Maldição-barata — enxameia ovos amaldiçoados e sufoca o campo."},
            {"reveal": "culling_game", "disclosure": "full",
             "tags": ["burst", "aoe"],
             "text": "Máximo: Meteoro — descarga massiva de energia amaldiçoada em área."},
            {"reveal": "culling_game", "disclosure": "named",
             "tags": ["sustain"],
             "text": "Regeneração extrema — recompõe ferimentos quase indefinidamente."},
        ],
    },
    # ── Outros ─────────────────────────────────────────────────────────────
    "Junpei Yoshino": {
        "stats": {"power": 22, "durability": 14, "speed": 26, "utility": 38},
        "positions": {"Support": 0.6, "Duelist": 0.5},
        "abilities": [
            {"reveal": "vs_mahito", "disclosure": "full",
             "tags": ["debuff", "utility"],
             "text": "Shikigami água-viva — veneno e paralisia em quem encosta."},
        ],
    },
    "Riko Amanai": {
        "stats": {"power": 8, "durability": 14, "speed": 24, "utility": 16},
        "positions": {"Support": 0.3},
        "abilities": [
            {"reveal": "intro", "disclosure": "named",
             "tags": ["utility"],
             "text": "Recipiente de Plasma Estelar — civil sem técnica de combate, alvo de proteção."},
        ],
    },
    "Misato Kuroi": {
        "stats": {"power": 16, "durability": 16, "speed": 26, "utility": 30},
        "positions": {"Support": 0.45},
        "abilities": [
            {"reveal": "intro", "disclosure": "full",
             "tags": ["utility"],
             "text": "Tutora treinada — usa ferramentas amaldiçoadas básicas em apoio."},
        ],
    },
}


JUJUTSU_POWER = UniversePower(
    arcs=ARCS,
    reveal_max=REVEAL_MAX,
    profiles=PROFILES,
    default_reveal="culling_game",
)
