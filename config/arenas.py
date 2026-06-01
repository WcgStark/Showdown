from dataclasses import dataclass, field


@dataclass
class Arena:
    id: str
    name: str
    flavor: str
    image: str
    conditions: list
    buffs: list
    debuffs: list
    special: str
    part: int = 0
    part_name: str = ""


JOJO_ARENAS: list[Arena] = [
    # ── Parte 1 — Phantom Blood ──────────────────────────────────────────────
    Arena(
        id="mansao_joestar",
        name="Mansão Joestar",
        flavor="Interior vitoriano de 3 andares, iluminação fraca",
        image="Joestar Mansion.jpeg",
        conditions=["Espaço interno", "Múltiplos andares", "Iluminação fraca"],
        buffs=[
            "Curto alcance domina corredores estreitos",
            "Personagens ágeis transitam rápido entre andares",
            "Escuridão favorece estilos furtivos",
        ],
        debuffs=[
            "Longo alcance severamente cortado",
            "Personagens grandes perdem mobilidade",
        ],
        special="Incêndio progressivo: ao fim de cada rodada, uma zona fecha permanentemente",
        part=1, part_name="Phantom Blood",
    ),
    Arena(
        id="windknights_lot",
        name="Windknight's Lot",
        flavor="Vila ao sul de Londres, noturna, labiríntica",
        image="Windknight's Lot.jpeg",
        conditions=["Visibilidade mínima", "Terreno irregular", "Labirinto de ruas"],
        buffs=[
            "Furtivos quase indetectáveis na escuridão",
            "Resistentes ignoram penalidade de terreno",
        ],
        debuffs=[
            "Suporte perde linha de visão com frequência",
            "Ranged severamente limitado pelas construções",
        ],
        special="Obstáculos vivos: bloqueios surgem em zonas aleatórias a cada turno",
        part=1, part_name="Phantom Blood",
    ),
    Arena(
        id="castelo_de_dio",
        name="Castelo de Dio",
        flavor="Fortaleza europeia, estrutura instável, variação de altura",
        image="Dio Mansion.jpeg",
        conditions=["Estrutura instável", "Cobertura abundante", "Variação de altura"],
        buffs=[
            "Voadores dominam verticalmente",
            "Cobertura protege personagens frágeis",
        ],
        debuffs=[
            "Chão instável pode derrubar estruturas sobre aliados",
            "Healer tem acesso limitado a certas zonas",
        ],
        special="Colapso estrutural: zona aleatória desmorona — personagens ali ficam imóveis 1 turno",
        part=1, part_name="Phantom Blood",
    ),
    # ── Parte 2 — Battle Tendency ─────────────────────────────────────────────
    Arena(
        id="colosseum_underground",
        name="Colosseum Underground",
        flavor="Caverna secreta sob o Coliseu, colunas, esculturas primitivas",
        image="Colosseum Underground.jpeg",
        conditions=["Caverna vasta", "Colunas e esculturas", "Escuridão total"],
        buffs=[
            "Habilidades de área ecoam nas paredes de pedra — alcance ampliado",
            "Tanques dominam corredores em funil",
        ],
        debuffs=[
            "Alta velocidade inútil em espaço fechado e irregular",
            "Ranged perde ângulo de ataque nas curvas das colunas",
        ],
        special="Faixa de luz solar: cruzar sem proteção causa dano automático — única fonte de luz",
        part=2, part_name="Battle Tendency",
    ),
    Arena(
        id="air_supplena_island",
        name="Air Supplena Island",
        flavor="Ilha gótica no Adriático, torre central, fosso de espinhos",
        image="Air Supplena Island.jpeg",
        conditions=["Ilha isolada", "Fosso de espinhos", "Torre central"],
        buffs=[
            "Personagens resistentes ignoram dano do fosso de espinhos",
            "Suporte aproveita as torres como cobertura elevada",
        ],
        debuffs=[
            "Cair no fosso causa dano passivo por turno",
            "Saída só por passarela estreita — retirada penalizada",
        ],
        special="Fosso ativo: personagem derrubado sobre espinhos fica imóvel e sangra HP por turno até ser resgatado",
        part=2, part_name="Battle Tendency",
    ),
    Arena(
        id="skeleton_heel_stone",
        name="Skeleton Heel Stone",
        flavor="Arena circular de pedra antiga com pista de biga, sopé do Piz Bernina",
        image="Skeleton Heel Stone.jpeg",
        conditions=["Arena circular aberta", "Pista de corrida", "Pilares com armas"],
        buffs=[
            "Personagens velozes dominam a pista circular — kiting perfeito",
            "Armas nos pilares ficam disponíveis a cada volta",
        ],
        debuffs=[
            "Sem cobertura no centro — qualquer personagem parado vira alvo fácil",
            "Healer vulnerável na pista aberta",
        ],
        special="Arma no pilar: a cada rodada, 1 item de combate aparece num pilar — primeiro a chegar o usa",
        part=2, part_name="Battle Tendency",
    ),
    # ── Parte 3 — Stardust Crusaders ──────────────────────────────────────────
    Arena(
        id="deserto_do_egito",
        name="Deserto do Egito",
        flavor="Visibilidade total, calor extremo, sem cobertura",
        image="Deserto do Egito.jpg",
        conditions=["Visibilidade total", "Calor extremo", "Sem cobertura"],
        buffs=[
            "Alcance máximo para ranged",
            "Resistência aumenta com o tempo",
        ],
        debuffs=[
            "Furtivos completamente expostos",
            "Energia cai gradualmente pelo calor",
        ],
        special="Tempestade de areia: 1 turno sem visibilidade — ataques erram e furtivos ficam ocultos",
        part=3, part_name="Stardust Crusaders",
    ),
    Arena(
        id="big_daddy",
        name="Big Daddy (Navio Fantasma)",
        flavor="Cargueiro abandonado no oceano, maquinário ativo, sem tripulação",
        image="Big Daddy.jpeg",
        conditions=["Navio abandonado", "Maquinário ativo e imprevisível", "Borda com queda no oceano"],
        buffs=[
            "Personagens pequenos e ágeis navegam melhor por corredores e porões",
            "Maquinário pode ser usado como cobertura ou alavanca tática",
        ],
        debuffs=[
            "Personagens grandes têm mobilidade limitada pelos corredores estreitos",
            "Borda da embarcação — queda = eliminação instantânea",
        ],
        special="Maquinário autônomo: guindastes e ganchos se movem sozinhos — personagem atingido é arremessado para zona aleatória",
        part=3, part_name="Stardust Crusaders",
    ),
    Arena(
        id="luxor",
        name="Luxor (Egito)",
        flavor="Cidade histórica à beira do Nilo, ruas e construções antigas",
        image="Luxor.jpeg",
        conditions=["Visibilidade média", "Ruas e becos históricos", "Terreno irregular"],
        buffs=[
            "Furtivos aproveitam sombras de construções milenares",
            "Personagens ágeis transitam rápido entre becos",
        ],
        debuffs=[
            "Ranged perde alcance por obstrução de muros e estruturas",
            "Suporte não mantém linha de visão com o time inteiro",
        ],
        special="Apagão: arena escurece por 1 turno — só personagens com percepção não-visual agem sem penalidade",
        part=3, part_name="Stardust Crusaders",
    ),
    # ── Parte 4 — Diamond is Unbreakable ──────────────────────────────────────
    Arena(
        id="angelo_rock",
        name="Angelo Rock – Jozenji, Morioh",
        flavor="Bairro residencial, semi-aberto, civis transitando",
        image="Angelo Rock.jpeg",
        conditions=["Semi-aberto", "Civis presentes", "Terreno plano"],
        buffs=[
            "Versáteis ganham bônus por usar objetos do ambiente",
            "Suporte acessa recursos espalhados pelo cenário",
        ],
        debuffs=[
            "Área de efeito colide com estruturas urbanas — dano reduzido",
            "Personagens grandes sofrem penalidade em ruas estreitas",
        ],
        special="Dano colateral: atacar zona com civis gera debuff de moral no time inteiro por 1 turno",
        part=4, part_name="Diamond is Unbreakable",
    ),
    Arena(
        id="ghost_girl_alley",
        name="Ghost Girl's Alley – Morioh",
        flavor="Rua residencial oculta com casas abandonadas, espaço que dobra sobre si mesmo",
        image="Ghost Girl's Alley.jpeg",
        conditions=["Espaço que se distorce", "Casas abandonadas", "Saída apenas pela entrada"],
        buffs=[
            "Furtivos se camuflam facilmente nas casas abandonadas",
            "Personagens com percepção não-padrão ignoram a distorção espacial",
        ],
        debuffs=[
            "Todos têm 20% de chance de retornar involuntariamente à posição inicial ao avançar demais",
            "Healer não consegue localizar aliados com precisão no espaço distorcido",
        ],
        special="Olhar para trás: personagem que recuar além da entrada é removido da arena por 1 turno pelas mãos fantasmas",
        part=4, part_name="Diamond is Unbreakable",
    ),
    Arena(
        id="futatsumori_tunnel",
        name="Futatsumori Tunnel – Morioh",
        flavor="Túnel de 450m sem luz, saída obscurecida pela curva, atmosfera de assombração",
        image="Futatsumori Tunnel.jpeg",
        conditions=["Espaço muito estreito", "Sem iluminação", "Curva que oculta a saída"],
        buffs=[
            "Habilidades de área ricocheteiam nas paredes — alcance dobrado",
            "Curto alcance domina o corredor",
        ],
        debuffs=[
            "Stands grandes não se manifestam totalmente",
            "Ranged não tem ângulo limpo sem atingir aliados",
        ],
        special="Colapso do túnel: pedras bloqueiam uma saída aleatória — time preso naquela extremidade perde mobilidade por 2 turnos",
        part=4, part_name="Diamond is Unbreakable",
    ),
    # ── Parte 5 — Golden Wind ─────────────────────────────────────────────────
    Arena(
        id="napoles_porto",
        name="Nápoles – Ruas do Porto",
        flavor="Becos italianos costeiros, sombra, múltiplos ângulos cegos",
        image="Nápoles.jpeg",
        conditions=["Espaço fechado", "Visibilidade baixa", "Ângulos cegos"],
        buffs=[
            "Furtivos ganham invisibilidade nas sombras dos becos",
            "Vice-capitão pode coordenar emboscada — ataque surpresa grátis",
        ],
        debuffs=[
            "Grande porte perde 30% de alcance",
            "Ranged não usa alcance máximo em becos curvados",
        ],
        special="Emboscada: no round 2, time com mais furtivos ganha 1 ataque antes do turno normal",
        part=5, part_name="Golden Wind",
    ),
    Arena(
        id="veneza_canais",
        name="Veneza – Canais e Pontes",
        flavor="Canais separando zonas, pontes como choke points, água por toda parte",
        image="Veneza.jpeg",
        conditions=["Terreno fragmentado por canais", "Pontes estreitas", "Água entre zonas"],
        buffs=[
            "Stands de fluxo dominam os canais",
            "Ágeis cruzam pontes com vantagem de posicionamento",
        ],
        debuffs=[
            "Pesados arriscam cair nos canais — save de mobilidade a cada movimento rápido",
            "Suporte tem dificuldade de cobrir zonas separadas por água",
        ],
        special="Queda no canal: personagem derrubado na água fica imóvel 1 turno e perde bônus de evasão",
        part=5, part_name="Golden Wind",
    ),
    Arena(
        id="coliseu_de_roma",
        name="Coliseu de Roma",
        flavor="Grande arena oval histórica com ruínas internas, noite, sem plateia",
        image="Coliseu de Roma.jpeg",
        conditions=["Espaço amplo e circular", "Ruínas internas como cobertura", "Sem cobertura no centro"],
        buffs=[
            "Ranged domina o centro com alcance irrestrito",
            "Rápidos flanqueiam pelo perímetro sem obstáculo",
        ],
        debuffs=[
            "Sem cobertura no centro — personagem exposto é alvo fácil",
            "Healer vulnerável por falta de obstáculos protetores",
        ],
        special="Controle de arena: time que dominar o centro ao fim de cada round acumula buff de moral",
        part=5, part_name="Golden Wind",
    ),
    # ── Parte 6 — Stone Ocean ─────────────────────────────────────────────────
    Arena(
        id="green_dolphin_prison",
        name="Green Dolphin Street Prison",
        flavor="Prisão de segurança máxima, grades, corredores, celas",
        image="Green Dolphin Street Prison.jpeg",
        conditions=["Espaço fechado", "Grades e barreiras", "Saídas controladas"],
        buffs=[
            "Penetração e fio têm alcance dobrado pelas grades",
            "Corredores em funil favorecem personagens resistentes",
        ],
        debuffs=[
            "Grandes ficam presos entre grades — mobilidade severamente reduzida",
            "Suporte não cobre o mapa com visibilidade limitada",
        ],
        special="Lockdown: todas as zonas travam por 1 turno — nenhum personagem pode se reposicionar",
        part=6, part_name="Stone Ocean",
    ),
    Arena(
        id="everglades",
        name="Everglades – Pântano da Flórida",
        flavor="Terreno alagado, vegetação densa, fauna hostil, clima instável",
        image="Everglades.jpeg",
        conditions=["Terreno alagado e irregular", "Visibilidade média", "Clima instável"],
        buffs=[
            "Stands de natureza ganham aliados ambientais passivos",
            "Vegetação favorece furtivos e emboscadas",
        ],
        debuffs=[
            "Mobilidade reduzida 20% pelo terreno alagado",
            "Clima muda todo turno — efeito surpresa positivo ou negativo",
        ],
        special="Chuva intensa: zona aleatória inunda — personagens ali ficam imóveis por 1 turno",
        part=6, part_name="Stone Ocean",
    ),
    Arena(
        id="kennedy_space_center",
        name="Kennedy Space Center",
        flavor="Plataforma de lançamento aberta, vento fortíssimo, pressão de tempo crescente",
        image="Kennedy Space Center.jpeg",
        conditions=["Espaço totalmente aberto", "Vento fortíssimo", "Pressão de tempo crescente"],
        buffs=[
            "Velocidade cresce com bônus acumulativo a cada turno",
            "Ranged tem alcance ilimitado",
        ],
        debuffs=[
            "Efeitos de duração reduzidos à metade",
            "Lentos acumulam penalidade crescente a cada turno",
        ],
        special="Reset de posição: turno 4 — todos reposicionados aleatoriamente e buffs ativos zerados",
        part=6, part_name="Stone Ocean",
    ),
]

ARENAS_BY_UNIVERSE: dict[str, list[Arena]] = {
    "jojo": JOJO_ARENAS,
}
