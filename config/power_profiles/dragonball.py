"""
Dragon Ball power profiles — battle-analysis data.

SCOPE: o anime completo (Dragon Ball Z → Dragon Ball Super) até o fim do
Torneio do Poder (Jiren, Instinto Superior de Goku), MAIS os personagens e
formas exclusivos dos filmes (Broly e Gogeta de "Dragon Ball Super: Broly", e
as formas de filme de Gohan/Piccolo de "Super Hero").

SPOILER POLICY: dois modos existem na pool (ver config.universes):
  - "completo" → tudo, incluindo os filmes;
  - "anime"    → só até o fim do anime no Torneio do Poder. Broly e Gogeta
                 (exclusivos de filme) são removidos da pool inteira nesse modo,
                 e as formas de filme (Gohan Fera, Piccolo Laranja) ficam
                 escondidas pelo gate `reveal="movies"`.

TRUNFO: ao contrário de Jujutsu (domínio) e One Piece (Haki do Rei), Dragon Ball
NÃO usa as tags de trunfo `domain`/`conqueror` — o texto fixo do motor para essas
tags é de outras franquias. Aqui a fantasia de poder é carregada pela escala de
stats deliberadamente não-linear: um Deus da Destruição ou Goku em Instinto
Superior simplesmente esmaga em pontuação bruta.

STAT SCALE: 0–100, não-linear. Tiers aproximados:
    anjos / ser supremo (Whis, Grande Sacerdote) ........ 97–100
    Deus da Destruição (Beerus, Champa) ................. 94–98
    topo mortal (Jiren, Goku/Vegeta divinos, Gogeta) .... 92–97
    elite (Freeza Dourado, Hit, Fused Zamasu, Cell, Boo)  84–93
    forte (Piccolo, Androides 16/17/18, Trunks) ......... 68–84
    médio (humanos Z, Forças Ginyu, Saga Saiyajin) ...... 46–68
    apoio / civil (Dende, Mr. Satan, Babidi) ............ 8–46  (um curandeiro é
        fraco em poder bruto, mas enorme em utilidade)
Personagens sem perfil caem no neutro 50.
"""

from __future__ import annotations

from config.power_profiles import UniversePower


# Ordered reveal tiers, earliest → latest (continuidade do anime, depois filmes).
ARCS = [
    "early",             # Dragon Ball clássico (Pilaf, Rei Piccolo, Tao Pai Pai)
    "saiyan",            # Saga dos Saiyajins (Raditz, Nappa, Vegeta)
    "freeza",            # Saga Namekusei / Freeza (1ª transformação Super Saiyajin)
    "cell",              # Sagas dos Androides e Cell
    "buu",               # Saga Majin Boo (fim de Dragon Ball Z)
    "battle_gods",       # DBS: A Batalha dos Deuses / O Renascimento de F (SSG, SSB, Golden Freeza)
    "universe6",         # Torneio entre os Universos 6 e 7 (Hit, Cabba, Frost)
    "future_trunks",     # Saga do Trunks do Futuro (Goku Black, Zamasu)
    "tournament_power",  # Torneio do Poder (Jiren, Instinto Superior) — fim do anime
    "movies",            # Filmes (Broly, Gogeta, Gohan Fera, Piccolo Laranja)
]

REVEAL_MAX = {
    "completo": "movies",            # tudo, incluindo os filmes
    "anime":    "tournament_power",  # só até o fim do anime no Torneio do Poder
    "teste":    "movies",            # pool reduzida, sem corte
}


# disclosure levels: "full" | "named" | "exists"
PROFILES: dict[str, dict] = {
    # ── Dragon Ball clássico ─────────────────────────────────────────────────
    "Bulma": {
        "stats": {"power": 6, "durability": 16, "speed": 30, "utility": 88},
        "positions": {"Support": 0.9},
        "abilities": [
            {"reveal": "early", "disclosure": "full",
             "tags": ["utility", "recon", "versatility"],
             "text": "Gênio inventora — Radar do Dragão, cápsulas Hoipoi e engenhocas para qualquer situação; sem poder de luta."},
        ],
    },
    "Chi-Chi": {
        "stats": {"power": 34, "durability": 32, "speed": 46, "utility": 40},
        "positions": {"Duelist": 0.55, "Support": 0.45},
        "abilities": [
            {"reveal": "early", "disclosure": "full",
             "tags": ["bruiser", "versatility"],
             "text": "Princesa da Montanha Fogo — artista marcial habilidosa na juventude, esposa de Goku."},
        ],
    },
    "Yajirobe": {
        "stats": {"power": 44, "durability": 46, "speed": 50, "utility": 66},
        "positions": {"Support": 0.72, "Duelist": 0.5},
        "abilities": [
            {"reveal": "early", "disclosure": "full",
             "tags": ["utility", "burst", "sustain"],
             "text": "Samurai resmungão — entrega Sementes dos Deuses na hora certa e desfere cortes-surpresa decisivos (cortou a cauda de Vegeta)."},
        ],
    },
    "Korin": {
        "stats": {"power": 24, "durability": 30, "speed": 40, "utility": 84},
        "positions": {"Healer": 0.82, "Support": 0.7},
        "abilities": [
            {"reveal": "early", "disclosure": "full",
             "tags": ["heal", "sustain", "utility"],
             "text": "Gato eremita da Torre Karin — cultiva as Sementes dos Deuses que restauram qualquer ferimento e fome."},
        ],
    },
    "Kami": {
        "stats": {"power": 40, "durability": 44, "speed": 46, "utility": 82},
        "positions": {"Support": 0.85, "Healer": 0.55, "Captain": 0.5},
        "abilities": [
            {"reveal": "early", "disclosure": "full",
             "tags": ["utility", "heal", "leadership", "versatility"],
             "text": "Deus da Terra — criou as Esferas do Dragão; sabedoria namekusei, telepatia e o selo Mafuba."},
        ],
    },
    "Mr. Popo": {
        "stats": {"power": 30, "durability": 40, "speed": 40, "utility": 70},
        "positions": {"Support": 0.78},
        "abilities": [
            {"reveal": "early", "disclosure": "full",
             "tags": ["utility", "versatility"],
             "text": "Assistente do Templo Sagrado — guia treinamentos na Sala do Pêndulo e cuida do santuário; mais forte do que aparenta."},
        ],
    },
    "King Piccolo": {
        "stats": {"power": 66, "durability": 58, "speed": 56, "utility": 64},
        "positions": {"Duelist": 0.78, "Captain": 0.6, "Traitor": 0.5},
        "abilities": [
            {"reveal": "early", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "manipulation"],
             "text": "Rei Demônio Piccolo — gera filhos demônios à vontade e dispara a Onda Explosiva; aterrorizou o mundo."},
        ],
    },
    "Tao Pai Pai": {
        "stats": {"power": 50, "durability": 46, "speed": 56, "utility": 50},
        "positions": {"Duelist": 0.72, "Traitor": 0.62},
        "abilities": [
            {"reveal": "early", "disclosure": "full",
             "tags": ["burst", "versatility", "betrayal"],
             "text": "Assassino de aluguel — o letal Dodon Pa (raio do dedo); depois ciborgue com lâmina e granadas."},
        ],
    },
    "Pilaf": {
        "stats": {"power": 8, "durability": 14, "speed": 28, "utility": 60},
        "positions": {"Traitor": 0.65, "Support": 0.5},
        "abilities": [
            {"reveal": "early", "disclosure": "full",
             "tags": ["sabotage", "manipulation", "utility", "betrayal"],
             "text": "Imperador trapalhão — caça as Esferas do Dragão com robôs e armadilhas mirabolantes."},
        ],
    },
    "Launch": {
        "stats": {"power": 36, "durability": 30, "speed": 44, "utility": 42},
        "positions": {"Duelist": 0.52, "Support": 0.45},
        "abilities": [
            {"reveal": "early", "disclosure": "full",
             "tags": ["burst", "versatility"],
             "text": "Dupla personalidade — ao espirrar vira uma fora-da-lei furiosa de metralhadora em punho."},
        ],
    },
    # ── Guerreiros Z (heróis) ────────────────────────────────────────────────
    "Goku": {
        "stats": {"power": 95, "durability": 90, "speed": 96, "utility": 78},
        "positions": {"Captain": 1.0, "Duelist": 0.95, "Vice Captain": 0.7, "Tank": 0.65},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["bruiser", "ace", "leadership"],
             "text": "Saiyajin criado na Terra — o Kaioken multiplica força e velocidade; o Kamehameha concentra ki numa onda devastadora."},
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["burst", "ace"],
             "text": "Super Saiyajin — a transformação lendária despertada em Namekusei que multiplica drasticamente seu poder."},
            {"reveal": "buu", "disclosure": "full",
             "tags": ["burst", "aoe"],
             "text": "Super Saiyajin 3 — salto colossal de potência ao custo de muita energia; o Genki Dama reúne a energia de todos."},
            {"reveal": "battle_gods", "disclosure": "full",
             "tags": ["ace", "burst"],
             "text": "Super Saiyajin Blue (ki divino) — poder que rivaliza com Deuses da Destruição."},
            {"reveal": "tournament_power", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "Instinto Superior — o corpo reage e esquiva sozinho e ataca com precisão divina; auge no Torneio do Poder."},
        ],
    },
    "Vegeta": {
        "stats": {"power": 92, "durability": 88, "speed": 90, "utility": 70},
        "positions": {"Captain": 0.85, "Duelist": 0.95, "Vice Captain": 0.85, "Tank": 0.6, "Traitor": 0.5},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["bruiser", "ace", "leadership"],
             "text": "Príncipe dos Saiyajins — técnica de elite e o Galick Ho; cresce em poder a cada batalha (Zenkai)."},
            {"reveal": "cell", "disclosure": "full",
             "tags": ["burst"],
             "text": "Super Saiyajin e além — orgulho saiyajin convertido em potência bruta; o Final Flash arrasador."},
            {"reveal": "battle_gods", "disclosure": "full",
             "tags": ["ace", "burst"],
             "text": "Super Saiyajin Blue — ki divino à altura de Goku."},
            {"reveal": "future_trunks", "disclosure": "full",
             "tags": ["ace", "burst"],
             "text": "Blue Evoluído — rompe os próprios limites contra deuses renegados."},
        ],
    },
    "Gohan": {
        "stats": {"power": 88, "durability": 82, "speed": 84, "utility": 66},
        "positions": {"Duelist": 0.92, "Captain": 0.7, "Vice Captain": 0.78, "Tank": 0.6},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["versatility"],
             "text": "Potencial oculto imenso — filho de Goku que cresce em saltos quando enfurecido."},
            {"reveal": "cell", "disclosure": "full",
             "tags": ["ace", "burst"],
             "text": "Super Saiyajin 2 — desperta no Cell Games e supera o próprio pai em fúria."},
            {"reveal": "buu", "disclosure": "full",
             "tags": ["ace", "bruiser"],
             "text": "Gohan Definitivo (Místico) — todo o poder latente liberado pelo Velho Kaioshin, sem precisar se transformar."},
            {"reveal": "movies", "disclosure": "full",
             "tags": ["ace", "burst"],
             "text": "Besta (Gohan Beast) — forma de cabelos grisalhos de poder extremo alcançada num filme, ao limite da destruição."},
        ],
    },
    "Piccolo": {
        "stats": {"power": 72, "durability": 72, "speed": 68, "utility": 82},
        "positions": {"Duelist": 0.8, "Tank": 0.7, "Vice Captain": 0.78, "Captain": 0.62, "Support": 0.6},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["versatility", "leadership", "guard"],
             "text": "Guerreiro namekusei — regeneração, braços extensíveis e o Makankosappo (Raio Perfurante) que atravessa o alvo."},
            {"reveal": "cell", "disclosure": "full",
             "tags": ["bruiser", "versatility"],
             "text": "Fusão com Kami e Nail — salto de poder e a mente tática que orienta o time."},
            {"reveal": "movies", "disclosure": "full",
             "tags": ["bruiser", "ace", "tank"],
             "text": "Piccolo Laranja — forma alaranjada desperta num filme, com poder colossal liberado por desejo."},
        ],
    },
    "Krillin": {
        "stats": {"power": 56, "durability": 54, "speed": 60, "utility": 72},
        "positions": {"Duelist": 0.68, "Support": 0.78, "Vice Captain": 0.5},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["burst", "debuff", "utility"],
             "text": "Disco Destruidor — lâmina de ki que corta quase tudo; o Taiyoken (Solar) cega o oponente. O humano mais forte da Terra."},
        ],
    },
    "Tien Shinhan": {
        "stats": {"power": 60, "durability": 58, "speed": 62, "utility": 64},
        "positions": {"Duelist": 0.72, "Support": 0.6, "Tank": 0.5},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["burst", "versatility"],
             "text": "Shiyoken (multiplica os braços) e Kikoho (Tri-Feixe) — troca energia vital por dano massivo."},
            {"reveal": "cell", "disclosure": "full",
             "tags": ["lockdown", "debuff"],
             "text": "Barragem contínua de Kikoho — prende o inimigo no lugar mesmo se exaurindo."},
        ],
    },
    "Yamcha": {
        "stats": {"power": 46, "durability": 44, "speed": 56, "utility": 50},
        "positions": {"Duelist": 0.62, "Support": 0.5},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["burst", "versatility"],
             "text": "Punho do Lobo e Soukidan (bola de energia teleguiada) — bandido do deserto reformado."},
        ],
    },
    "Chiaotzu": {
        "stats": {"power": 30, "durability": 26, "speed": 40, "utility": 60},
        "positions": {"Support": 0.78, "Duelist": 0.45},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["debuff", "lockdown", "utility"],
             "text": "Telecinese e paralisia mental — trava o oponente; capaz de se autodestruir num último recurso."},
        ],
    },
    "Master Roshi": {
        "stats": {"power": 48, "durability": 46, "speed": 44, "utility": 66},
        "positions": {"Support": 0.7, "Duelist": 0.55, "Captain": 0.45},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["bruiser", "utility", "leadership"],
             "text": "Criador do Kamehameha — mestre ancião; em Potência Máxima ganha musculatura colossal por instantes."},
            {"reveal": "tournament_power", "disclosure": "full",
             "tags": ["versatility", "sustain"],
             "text": "Mafuba e fôlego renovado no Torneio do Poder — veterano astuto que economiza energia para durar."},
        ],
    },
    "Goten": {
        "stats": {"power": 58, "durability": 54, "speed": 60, "utility": 40},
        "positions": {"Duelist": 0.66, "Support": 0.45},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["burst"],
             "text": "Super Saiyajin ainda criança — talento prodigioso herdado de Goku."},
        ],
    },
    "Trunks": {
        "stats": {"power": 60, "durability": 56, "speed": 62, "utility": 42},
        "positions": {"Duelist": 0.68, "Support": 0.45},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["burst"],
             "text": "Super Saiyajin precoce — ainda mais forte que Goten; filho orgulhoso de Vegeta."},
        ],
    },
    "Future Trunks": {
        "stats": {"power": 80, "durability": 74, "speed": 78, "utility": 60},
        "positions": {"Duelist": 0.85, "Vice Captain": 0.66, "Captain": 0.55},
        "abilities": [
            {"reveal": "cell", "disclosure": "full",
             "tags": ["bruiser", "ace", "burst"],
             "text": "Espadachim do futuro — Super Saiyajin que viajou no tempo para mudar a história."},
            {"reveal": "future_trunks", "disclosure": "full",
             "tags": ["ace", "burst"],
             "text": "Super Saiyajin Ira — a esperança de toda a humanidade concentrada na espada."},
        ],
    },
    "Gotenks": {
        "stats": {"power": 84, "durability": 72, "speed": 80, "utility": 56},
        "positions": {"Duelist": 0.88, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["ace", "burst", "aoe"],
             "text": "Fusão de Goten e Trunks — Super Saiyajin 3 travesso; Fantasmas Suicidas explosivos. Dura só 30 minutos."},
        ],
    },
    "Vegito": {
        "stats": {"power": 96, "durability": 92, "speed": 95, "utility": 78},
        "positions": {"Duelist": 0.98, "Captain": 0.8, "Vice Captain": 0.7},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "Fusão Potara de Goku e Vegeta — poder esmagador, velocidade absurda e o Final Kamehameha; o guerreiro mais forte do seu tempo."},
        ],
    },
    "Android 18": {
        "stats": {"power": 76, "durability": 84, "speed": 76, "utility": 66},
        "positions": {"Duelist": 0.82, "Tank": 0.78, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "cell", "disclosure": "full",
             "tags": ["bruiser", "durability", "burst"],
             "text": "Androide de energia infinita — força e resistência muito acima dos humanos; barreira de energia."},
        ],
    },
    "Android 17": {
        "stats": {"power": 78, "durability": 88, "speed": 76, "utility": 72},
        "positions": {"Duelist": 0.82, "Tank": 0.85, "Vice Captain": 0.62, "Traitor": 0.5},
        "abilities": [
            {"reveal": "cell", "disclosure": "full",
             "tags": ["tank", "durability", "bruiser"],
             "text": "Androide de energia infinita — não se cansa e desgasta o inimigo com resistência inesgotável."},
            {"reveal": "tournament_power", "disclosure": "full",
             "tags": ["guard", "versatility", "ace"],
             "text": "Barreiras de energia e estratégia fria — peça decisiva e o último de pé do Universo 7 no Torneio do Poder."},
        ],
    },
    "Android 16": {
        "stats": {"power": 74, "durability": 86, "speed": 64, "utility": 58},
        "positions": {"Tank": 0.9, "Duelist": 0.72, "Vice Captain": 0.5},
        "abilities": [
            {"reveal": "cell", "disclosure": "full",
             "tags": ["tank", "durability", "guard", "aoe"],
             "text": "Androide pacifista colossal — Canhões do Inferno e força bruta num corpo blindado."},
        ],
    },
    "Majin Buu": {
        "stats": {"power": 86, "durability": 92, "speed": 70, "utility": 80},
        "positions": {"Duelist": 0.88, "Tank": 0.85, "Healer": 0.55, "Captain": 0.6},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["bruiser", "tank", "durability", "sustain", "aoe"],
             "text": "Regeneração extrema — reconstitui-se de qualquer dano; o Candy Beam transforma o alvo em doce e ele absorve oponentes para evoluir."},
        ],
    },
    "Mr. Satan": {
        "stats": {"power": 14, "durability": 22, "speed": 30, "utility": 60},
        "positions": {"Support": 0.65, "Captain": 0.4},
        "abilities": [
            {"reveal": "cell", "disclosure": "full",
             "tags": ["leadership", "utility"],
             "text": "Campeão mundial fanfarrão — sem poder de luta real, mas uma sorte e um carisma que mudam o ânimo de todos (até de Boo)."},
        ],
    },
    "Videl": {
        "stats": {"power": 30, "durability": 30, "speed": 44, "utility": 42},
        "positions": {"Duelist": 0.55, "Support": 0.5},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["bruiser", "versatility", "recon"],
             "text": "Filha de Mr. Satan — artista marcial habilidosa que aprende a voar."},
        ],
    },
    "Dende": {
        "stats": {"power": 10, "durability": 24, "speed": 36, "utility": 92},
        "positions": {"Healer": 1.0, "Support": 0.62},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["heal", "sustain", "revive", "utility"],
             "text": "Curandeiro namekusei — restaura ferimentos graves instantaneamente ao toque; depois, Guardião que recria as Esferas do Dragão."},
        ],
    },
    # ── Saga dos Saiyajins (vilões) ──────────────────────────────────────────
    "Raditz": {
        "stats": {"power": 50, "durability": 50, "speed": 56, "utility": 50},
        "positions": {"Duelist": 0.64, "Support": 0.45},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["bruiser", "recon"],
             "text": "Irmão de Goku — scouter que mede o poder de luta e força saiyajin brutal."},
        ],
    },
    "Nappa": {
        "stats": {"power": 60, "durability": 64, "speed": 54, "utility": 44},
        "positions": {"Tank": 0.7, "Duelist": 0.68},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["bruiser", "durability", "aoe"],
             "text": "General saiyajin — explosões de ki que arrasam cidades e força colossal."},
        ],
    },
    "King Kai": {
        "stats": {"power": 30, "durability": 36, "speed": 40, "utility": 86},
        "positions": {"Support": 0.85, "Healer": 0.5},
        "abilities": [
            {"reveal": "saiyan", "disclosure": "full",
             "tags": ["buff", "utility", "leadership", "recon"],
             "text": "Deus do Universo Norte — ensina o Kaioken e a Genki Dama; telepatia que coordena o time à distância."},
        ],
    },
    # ── Saga Freeza ──────────────────────────────────────────────────────────
    "Frieza": {
        "stats": {"power": 92, "durability": 80, "speed": 88, "utility": 76},
        "positions": {"Captain": 0.8, "Duelist": 0.92, "Support": 0.55, "Traitor": 0.5},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "leadership"],
             "text": "Imperador do universo — na forma final dispara Death Beams e a Supernova capaz de destruir um planeta inteiro."},
            {"reveal": "battle_gods", "disclosure": "full",
             "tags": ["ace", "burst"],
             "text": "Golden Freeza — forma dourada de poder imenso conquistada por puro treino."},
        ],
    },
    "Zarbon": {
        "stats": {"power": 60, "durability": 58, "speed": 60, "utility": 50},
        "positions": {"Duelist": 0.7, "Support": 0.5},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["bruiser", "versatility"],
             "text": "Braço-direito de Freeza — forma monstruosa que troca elegância por força bruta."},
        ],
    },
    "Dodoria": {
        "stats": {"power": 56, "durability": 62, "speed": 50, "utility": 42},
        "positions": {"Tank": 0.68, "Duelist": 0.6},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["bruiser", "durability"],
             "text": "Capanga de Freeza — couraça resistente e rajadas disparadas pela boca."},
        ],
    },
    "Captain Ginyu": {
        "stats": {"power": 70, "durability": 64, "speed": 66, "utility": 80},
        "positions": {"Duelist": 0.74, "Support": 0.62, "Traitor": 0.78, "Captain": 0.55},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["manipulation", "betrayal", "versatility", "utility"],
             "text": "Troca de Corpo (Change!) — assume o corpo do oponente, roubando seu poder; líder das Forças Especiais Ginyu."},
        ],
    },
    "Recoome": {
        "stats": {"power": 62, "durability": 66, "speed": 56, "utility": 44},
        "positions": {"Tank": 0.7, "Duelist": 0.68},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["bruiser", "durability", "burst"],
             "text": "Bruto das Forças Ginyu — encaixa castigo e devolve com o Recoome Eraser Gun."},
        ],
    },
    "Burter": {
        "stats": {"power": 58, "durability": 54, "speed": 72, "utility": 44},
        "positions": {"Duelist": 0.68},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["burst", "versatility"],
             "text": "O mais veloz das Forças Ginyu — golpes-relâmpago em alta velocidade."},
        ],
    },
    "Jeice": {
        "stats": {"power": 58, "durability": 52, "speed": 64, "utility": 48},
        "positions": {"Duelist": 0.68, "Support": 0.5},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["burst", "aoe"],
             "text": "Crusher Ball e ataques coordenados — o vermelho das Forças Ginyu."},
        ],
    },
    "Guldo": {
        "stats": {"power": 40, "durability": 36, "speed": 40, "utility": 70},
        "positions": {"Support": 0.72, "Duelist": 0.5},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["lockdown", "debuff", "utility"],
             "text": "Congela o tempo prendendo a respiração e usa telecinese para imobilizar o alvo."},
        ],
    },
    "King Cold": {
        "stats": {"power": 78, "durability": 70, "speed": 70, "utility": 60},
        "positions": {"Duelist": 0.8, "Captain": 0.62},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["ace", "bruiser", "leadership"],
             "text": "Pai de Freeza — imperador veterano de imenso poder."},
        ],
    },
    "Nail": {
        "stats": {"power": 58, "durability": 56, "speed": 56, "utility": 60},
        "positions": {"Duelist": 0.7, "Tank": 0.55, "Support": 0.55},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["bruiser", "sustain", "versatility"],
             "text": "Guerreiro namekusei de elite — regeneração e força; depois se funde a Piccolo para fortalecê-lo."},
        ],
    },
    "Guru": {
        "stats": {"power": 8, "durability": 24, "speed": 10, "utility": 92},
        "positions": {"Support": 0.9, "Healer": 0.5},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["buff", "utility", "heal"],
             "text": "Grande Patriarca de Namekusei — desperta o potencial oculto dos aliados ao toque; criou as Esferas do Dragão namekuseianas."},
        ],
    },
    "Bardock": {
        "stats": {"power": 54, "durability": 54, "speed": 58, "utility": 56},
        "positions": {"Duelist": 0.68, "Captain": 0.5, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "freeza", "disclosure": "full",
             "tags": ["bruiser", "burst", "recon"],
             "text": "Pai de Goku — saiyajin de classe baixa que luta acima do seu nível; visões do futuro o assombram."},
        ],
    },
    # ── Sagas dos Androides / Cell ──────────────────────────────────────────
    "Cell": {
        "stats": {"power": 86, "durability": 82, "speed": 80, "utility": 78},
        "positions": {"Duelist": 0.9, "Captain": 0.7, "Tank": 0.68},
        "abilities": [
            {"reveal": "cell", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "sustain", "versatility"],
             "text": "Bioandroide perfeito — copia técnicas (Kamehameha), regenera-se de um único núcleo e absorve oponentes para evoluir; cria Cell Júniores."},
        ],
    },
    "Dr. Gero": {
        "stats": {"power": 64, "durability": 60, "speed": 54, "utility": 70},
        "positions": {"Support": 0.68, "Duelist": 0.6, "Traitor": 0.55},
        "abilities": [
            {"reveal": "cell", "disclosure": "full",
             "tags": ["utility", "debuff", "versatility"],
             "text": "Androide cientista (Androide 20) — absorve energia pelas palmas para se reabastecer; mente criadora de todos os androides."},
        ],
    },
    "Android 19": {
        "stats": {"power": 60, "durability": 64, "speed": 52, "utility": 56},
        "positions": {"Tank": 0.68, "Duelist": 0.6},
        "abilities": [
            {"reveal": "cell", "disclosure": "full",
             "tags": ["durability", "debuff", "utility"],
             "text": "Androide de absorção — drena ki pelo toque das mãos; resistente e implacável."},
        ],
    },
    # ── Saga Majin Boo ───────────────────────────────────────────────────────
    "Babidi": {
        "stats": {"power": 20, "durability": 24, "speed": 30, "utility": 78},
        "positions": {"Support": 0.78, "Traitor": 0.7, "Captain": 0.45},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["manipulation", "buff", "debuff", "sabotage", "utility"],
             "text": "Mago do mal — controla mentes (selo 'Majin') e amplia o poder de seus servos; conjura magia à distância."},
        ],
    },
    "Dabura": {
        "stats": {"power": 72, "durability": 66, "speed": 64, "utility": 60},
        "positions": {"Duelist": 0.78, "Tank": 0.58},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["bruiser", "debuff", "versatility"],
             "text": "Rei do Mundo Demônio — cuspe que petrifica o alvo e uma espada demoníaca."},
        ],
    },
    "Supreme Kai": {
        "stats": {"power": 50, "durability": 48, "speed": 52, "utility": 74},
        "positions": {"Support": 0.8, "Captain": 0.55, "Healer": 0.5},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["utility", "leadership", "versatility", "recon"],
             "text": "Kaioshin do Universo 7 — divindade que orienta os deuses; telecinese e o saber sobre as ameaças cósmicas."},
        ],
    },
    "Kibito": {
        "stats": {"power": 48, "durability": 52, "speed": 48, "utility": 70},
        "positions": {"Healer": 0.8, "Support": 0.62, "Duelist": 0.5},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["heal", "sustain", "utility"],
             "text": "Atendente do Kaioshin — cura ferimentos e restaura energia instantaneamente; teletransporta o grupo."},
        ],
    },
    "Old Kai": {
        "stats": {"power": 20, "durability": 28, "speed": 24, "utility": 84},
        "positions": {"Support": 0.82, "Healer": 0.5},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["buff", "utility", "versatility"],
             "text": "Ancião Kaioshin — ritual que libera todo o potencial adormecido de um guerreiro; sabedoria milenar (e um humor questionável)."},
        ],
    },
    "Uub": {
        "stats": {"power": 70, "durability": 64, "speed": 66, "utility": 48},
        "positions": {"Duelist": 0.74, "Vice Captain": 0.5},
        "abilities": [
            {"reveal": "buu", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Encarnação humana do Boo Maligno — potencial colossal bruto, pronto para ser lapidado por Goku."},
        ],
    },
    # ── DBS: Deuses e Anjos (Batalha dos Deuses / Renascimento de F) ─────────
    "Beerus": {
        "stats": {"power": 98, "durability": 95, "speed": 95, "utility": 88},
        "positions": {"Captain": 0.9, "Duelist": 0.96, "Tank": 0.7},
        "abilities": [
            {"reveal": "battle_gods", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "leadership"],
             "text": "Deus da Destruição do Universo 7 — o Hakai apaga a existência do alvo; poder muito acima de qualquer mortal."},
        ],
    },
    "Whis": {
        "stats": {"power": 99, "durability": 96, "speed": 99, "utility": 95},
        "positions": {"Captain": 0.85, "Duelist": 0.92, "Healer": 0.7, "Support": 0.7},
        "abilities": [
            {"reveal": "battle_gods", "disclosure": "full",
             "tags": ["ace", "versatility", "heal", "sustain", "recon"],
             "text": "Anjo e mestre de Beerus — velocidade incomparável, reverte o tempo em curto alcance e cura ferimentos; o ser mais forte do Universo 7."},
        ],
    },
    "Jaco": {
        "stats": {"power": 40, "durability": 38, "speed": 56, "utility": 60},
        "positions": {"Support": 0.6, "Duelist": 0.5},
        "abilities": [
            {"reveal": "battle_gods", "disclosure": "full",
             "tags": ["burst", "utility", "recon"],
             "text": "Patrulheiro Galáctico — Elite Beam e tecnologia espacial; atrapalhado, mas com recursos para emergências."},
        ],
    },
    # ── Torneio dos Universos 6 e 7 ──────────────────────────────────────────
    "Hit": {
        "stats": {"power": 88, "durability": 80, "speed": 90, "utility": 82},
        "positions": {"Duelist": 0.92, "Captain": 0.66, "Traitor": 0.55},
        "abilities": [
            {"reveal": "universe6", "disclosure": "full",
             "tags": ["ace", "burst", "lockdown", "versatility"],
             "text": "Assassino lendário do Universo 6 — o Salto no Tempo congela instantes e seus golpes acertam pelo intervalo paralisado."},
        ],
    },
    "Champa": {
        "stats": {"power": 96, "durability": 92, "speed": 88, "utility": 70},
        "positions": {"Captain": 0.82, "Duelist": 0.92, "Tank": 0.66},
        "abilities": [
            {"reveal": "universe6", "disclosure": "full",
             "tags": ["ace", "burst", "aoe"],
             "text": "Deus da Destruição do Universo 6 — Hakai e poder divino, ainda que preguiçoso e glutão."},
        ],
    },
    "Vados": {
        "stats": {"power": 99, "durability": 95, "speed": 98, "utility": 94},
        "positions": {"Captain": 0.85, "Duelist": 0.92, "Healer": 0.68, "Support": 0.68},
        "abilities": [
            {"reveal": "universe6", "disclosure": "full",
             "tags": ["ace", "versatility", "heal", "recon"],
             "text": "Anjo do Universo 6 — irmã de Whis, ainda mais experiente; manipula tempo e espaço."},
        ],
    },
    "Cabba": {
        "stats": {"power": 68, "durability": 62, "speed": 66, "utility": 48},
        "positions": {"Duelist": 0.74, "Support": 0.5},
        "abilities": [
            {"reveal": "universe6", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Saiyajin educado do Universo 6 — desperta o Super Saiyajin pela emoção."},
        ],
    },
    "Frost": {
        "stats": {"power": 70, "durability": 64, "speed": 68, "utility": 66},
        "positions": {"Duelist": 0.72, "Traitor": 0.66, "Support": 0.55},
        "abilities": [
            {"reveal": "universe6", "disclosure": "full",
             "tags": ["debuff", "versatility", "betrayal"],
             "text": "Da mesma raça de Freeza — agulhas venenosas escondidas e golpes sujos sob a fachada de herói."},
        ],
    },
    "Botamo": {
        "stats": {"power": 56, "durability": 78, "speed": 40, "utility": 42},
        "positions": {"Tank": 0.85, "Duelist": 0.55},
        "abilities": [
            {"reveal": "universe6", "disclosure": "full",
             "tags": ["tank", "durability", "guard"],
             "text": "Lutador-urso do Universo 6 — corpo elástico que repele quase todo dano físico."},
        ],
    },
    "Magetta": {
        "stats": {"power": 64, "durability": 78, "speed": 40, "utility": 42},
        "positions": {"Tank": 0.82, "Duelist": 0.6},
        "abilities": [
            {"reveal": "universe6", "disclosure": "full",
             "tags": ["tank", "durability", "aoe"],
             "text": "Robô-magma do Universo 6 — couraça pesadíssima e lava incandescente."},
        ],
    },
    # ── Saga do Trunks do Futuro ─────────────────────────────────────────────
    "Goku Black": {
        "stats": {"power": 86, "durability": 80, "speed": 84, "utility": 72},
        "positions": {"Duelist": 0.9, "Captain": 0.66, "Traitor": 0.6},
        "abilities": [
            {"reveal": "future_trunks", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "Zamasu no corpo de Goku — Super Saiyajin Rosé e uma foice de ki; cresce em batalha como um saiyajin."},
        ],
    },
    "Zamasu": {
        "stats": {"power": 92, "durability": 90, "speed": 84, "utility": 76},
        "positions": {"Duelist": 0.9, "Tank": 0.78, "Captain": 0.66},
        "abilities": [
            {"reveal": "future_trunks", "disclosure": "full",
             "tags": ["ace", "durability", "sustain", "aoe"],
             "text": "Kaioshin renegado — corpo imortal que se regenera de qualquer ferimento; a Fusão Potara o torna quase indestrutível."},
        ],
    },
    # ── Torneio do Poder (fim do anime) ──────────────────────────────────────
    "Jiren": {
        "stats": {"power": 96, "durability": 94, "speed": 92, "utility": 70},
        "positions": {"Duelist": 0.98, "Captain": 0.78, "Tank": 0.82},
        "abilities": [
            {"reveal": "tournament_power", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "guard", "durability"],
             "text": "O Orgulho do Universo 11 — poder que supera Deuses da Destruição; rajadas que parecem parar o tempo e uma defesa praticamente impenetrável."},
        ],
    },
    "Toppo": {
        "stats": {"power": 90, "durability": 88, "speed": 80, "utility": 60},
        "positions": {"Duelist": 0.88, "Tank": 0.78, "Captain": 0.7},
        "abilities": [
            {"reveal": "tournament_power", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "leadership"],
             "text": "Líder das Tropas do Orgulho — desperta como Deus da Destruição em treinamento, com energia de Hakai por todo o corpo."},
        ],
    },
    "Dyspo": {
        "stats": {"power": 80, "durability": 70, "speed": 94, "utility": 55},
        "positions": {"Duelist": 0.84, "Support": 0.5},
        "abilities": [
            {"reveal": "tournament_power", "disclosure": "full",
             "tags": ["burst", "versatility"],
             "text": "Velocista do Universo 11 — no Modo Super Máximo de Luz move-se além da velocidade da luz."},
        ],
    },
    "Caulifla": {
        "stats": {"power": 78, "durability": 70, "speed": 78, "utility": 50},
        "positions": {"Duelist": 0.82, "Vice Captain": 0.55},
        "abilities": [
            {"reveal": "tournament_power", "disclosure": "full",
             "tags": ["bruiser", "burst"],
             "text": "Saiyajin durona do Universo 6 — domina o Super Saiyajin 2 em tempo recorde."},
        ],
    },
    "Kale": {
        "stats": {"power": 82, "durability": 76, "speed": 70, "utility": 45},
        "positions": {"Duelist": 0.8, "Tank": 0.6},
        "abilities": [
            {"reveal": "tournament_power", "disclosure": "full",
             "tags": ["bruiser", "burst", "aoe"],
             "text": "Super Saiyajin Lendária — forma berserk de força descomunal, a princípio descontrolada."},
        ],
    },
    "Kefla": {
        "stats": {"power": 90, "durability": 82, "speed": 88, "utility": 55},
        "positions": {"Duelist": 0.92, "Vice Captain": 0.6},
        "abilities": [
            {"reveal": "tournament_power", "disclosure": "full",
             "tags": ["ace", "burst", "aoe"],
             "text": "Fusão Potara de Caulifla e Kale — Super Saiyajin de poder explosivo que pressiona até o Instinto Superior."},
        ],
    },
    "Grand Priest": {
        "stats": {"power": 99, "durability": 96, "speed": 98, "utility": 92},
        "positions": {"Captain": 0.85, "Duelist": 0.9, "Support": 0.66},
        "abilities": [
            {"reveal": "tournament_power", "disclosure": "named",
             "tags": ["ace", "leadership", "versatility"],
             "text": "Grande Sacerdote — atendente do Rei de Tudo e pai dos anjos; reputado como um dos seres mais fortes dos 12 universos, embora nunca lute a sério."},
        ],
    },
    # ── Filmes (exclusivos — só no modo 'completo') ──────────────────────────
    "Broly": {
        "stats": {"power": 95, "durability": 96, "speed": 84, "utility": 50},
        "positions": {"Duelist": 0.95, "Tank": 0.9, "Captain": 0.6},
        "abilities": [
            {"reveal": "movies", "disclosure": "full",
             "tags": ["ace", "bruiser", "burst", "durability", "tank"],
             "text": "Saiyajin lendário (filme) — o poder cresce sem limite durante a luta; resistência monstruosa e fúria imparável."},
        ],
    },
    "Gogeta": {
        "stats": {"power": 97, "durability": 92, "speed": 96, "utility": 78},
        "positions": {"Duelist": 0.98, "Captain": 0.82, "Vice Captain": 0.7},
        "abilities": [
            {"reveal": "movies", "disclosure": "full",
             "tags": ["ace", "burst", "versatility"],
             "text": "Fusão por dança de Goku e Vegeta (filme) — Super Saiyajin Blue de velocidade e potência que superam qualquer guerreiro."},
        ],
    },
    "Cooler": {
        "stats": {"power": 90, "durability": 80, "speed": 86, "utility": 70},
        "positions": {"Duelist": 0.9, "Captain": 0.66, "Tank": 0.6},
        "abilities": [
            {"reveal": "movies", "disclosure": "full",
             "tags": ["ace", "burst", "aoe", "leadership"],
             "text": "Irmão de Freeza (filme) — uma quinta forma que ele não possui; como Metal Cooler, regenera-se e se adapta indefinidamente."},
        ],
    },
    "Turles": {
        "stats": {"power": 72, "durability": 66, "speed": 70, "utility": 60},
        "positions": {"Duelist": 0.8, "Captain": 0.55},
        "abilities": [
            {"reveal": "movies", "disclosure": "full",
             "tags": ["bruiser", "burst", "sustain"],
             "text": "Saiyajin sósia de Goku (filme) — o Fruto da Árvore do Poderio multiplica sua força."},
        ],
    },
    "Janemba": {
        "stats": {"power": 90, "durability": 84, "speed": 82, "utility": 78},
        "positions": {"Duelist": 0.9, "Tank": 0.66, "Captain": 0.55},
        "abilities": [
            {"reveal": "movies", "disclosure": "full",
             "tags": ["ace", "burst", "versatility", "manipulation"],
             "text": "Demônio do limbo (filme) — distorce a realidade, teletransporta-se e transforma o espaço ao redor em armas."},
        ],
    },
    "Bojack": {
        "stats": {"power": 80, "durability": 76, "speed": 72, "utility": 58},
        "positions": {"Duelist": 0.82, "Tank": 0.62, "Captain": 0.6},
        "abilities": [
            {"reveal": "movies", "disclosure": "full",
             "tags": ["bruiser", "burst", "aoe", "leadership"],
             "text": "Pirata galáctico (filme) — liberto de seu selo, transborda poder e comanda seus capangas Galáxia."},
        ],
    },
    "Paragus": {
        "stats": {"power": 56, "durability": 54, "speed": 54, "utility": 64},
        "positions": {"Support": 0.66, "Traitor": 0.7, "Captain": 0.5},
        "abilities": [
            {"reveal": "movies", "disclosure": "full",
             "tags": ["manipulation", "sabotage", "leadership", "betrayal"],
             "text": "Pai de Broly (filme) — usa um dispositivo para controlar a fúria do filho e movê-lo como arma."},
        ],
    },
}


DRAGONBALL_POWER = UniversePower(
    arcs=ARCS,
    reveal_max=REVEAL_MAX,
    profiles=PROFILES,
    default_reveal="movies",
)
