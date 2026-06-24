"""
Universes configuration.
Each universe defines its characters, fandom API URL, asset folder,
and UI theme used by both the collector and the main app.
"""

from dataclasses import dataclass, field


# ──────────────────────────────────────────────
# Data classes
# ──────────────────────────────────────────────

@dataclass
class Theme:
    """Visual theme for a universe."""
    bg: str
    panel_bg: str
    border: str
    title_fg: str
    text_fg: str
    text_secondary: str
    button_start_bg: str
    button_start_fg: str
    font_family: str
    icon: str
    entry_bg: str
    entry_fg: str
    entry_insert: str


@dataclass
class FilterSet:
    """Named subset of characters (e.g. 'anime-only' pool)."""
    label: str
    description: str
    exclude: set = field(default_factory=set)


@dataclass
class Universe:
    """Full definition of a playable franchise."""
    key: str                        # internal id, e.g. "onepiece"
    name: str                       # display name
    api_url: str                    # fandom MediaWiki API endpoint
    asset_folder: str               # relative path under assets/
    characters: list                # master character list
    positions: list                 # draft slot names
    theme: Theme
    filters: dict = field(default_factory=dict)  # name -> FilterSet
    default_filter: str = "default"
    collector_skip: set = field(default_factory=set)  # skip these names in collector


# ──────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────

def _build_op_theme() -> Theme:
    return Theme(
        bg="#2B1A0E",
        panel_bg="#3D2210",
        border="#F5C842",
        title_fg="#F5C842",
        text_fg="#F5C842",
        text_secondary="#F0E0C0",
        button_start_bg="#4CAF50",
        button_start_fg="white",
        font_family="Georgia",
        icon="☠",
        entry_bg="#4A2A08",
        entry_fg="#F0E0C0",
        entry_insert="#F5C842",
    )


def _build_inv_theme() -> Theme:
    return Theme(
        bg="#0A1628",
        panel_bg="#0F1F38",
        border="#FFE500",
        title_fg="#FFE500",
        text_fg="#E8F4FF",
        text_secondary="#7BA8D4",
        button_start_bg="#FFE500",
        button_start_fg="#0A1628",
        font_family="Arial",
        icon="⚡",
        entry_bg="#0D2040",
        entry_fg="#E8F4FF",
        entry_insert="#FFE500",
    )


def _build_naruto_theme() -> Theme:
    return Theme(
        bg="#1A1000",
        panel_bg="#2A1E00",
        border="#FF6600",
        title_fg="#FF6600",
        text_fg="#FF9900",
        text_secondary="#FFCC88",
        button_start_bg="#CC4400",
        button_start_fg="white",
        font_family="Arial",
        icon="🍃",
        entry_bg="#2A1800",
        entry_fg="#FFCC88",
        entry_insert="#FF6600",
    )


def _build_jojo_theme() -> Theme:
    return Theme(
        bg="#150A1F",
        panel_bg="#22103A",
        border="#C77DFF",
        title_fg="#C77DFF",
        text_fg="#E9D5FF",
        text_secondary="#B89BD9",
        button_start_bg="#9D4EDD",
        button_start_fg="white",
        font_family="Arial",
        icon="⭐",
        entry_bg="#1C0E30",
        entry_fg="#E9D5FF",
        entry_insert="#C77DFF",
    )


def _build_bleach_theme() -> Theme:
    return Theme(
        bg="#0A0A14",
        panel_bg="#12121E",
        border="#6666CC",
        title_fg="#AAAAFF",
        text_fg="#CCCCFF",
        text_secondary="#8888BB",
        button_start_bg="#333388",
        button_start_fg="white",
        font_family="Arial",
        icon="⚔",
        entry_bg="#0F0F20",
        entry_fg="#CCCCFF",
        entry_insert="#AAAAFF",
    )


# ──────────────────────────────────────────────
# Positions (shared across universes)
# ──────────────────────────────────────────────

POSITIONS_STANDARD = ["Captain", "Vice Captain", "Tank", "Duelist", "Healer", "Support", "Traitor"]


# ──────────────────────────────────────────────
# One Piece
# ──────────────────────────────────────────────

_OP_CHARACTERS = [
    "Monkey D. Luffy", "Roronoa Zoro", "Nami", "Sanji","Jinbe", "Nico Robin", "Usopp",
    "Tony Tony Chopper", "Brook", "Franky", "Buggy", "Kuro", "Krieg", "Arlong",
    "Helmeppo", "Koby", "Portgas D. Ace", "Shanks", "Uta", "Nefertari Vivi",
    "Crocodile", "Bentham", "Daz Bonez", "Chaka", "Pell", "Tashigi", "Smoker",
    "Enel", "Gan Fall", "Mont Blanc Noland", "Kalgara", "Ohm", "Shura", "Satori",
    "Holy", "Iceburg", "Rob Lucci", "Kaku", "Kalifa", "Blueno", "Jabra", "Spandam",
    "Gecko Moria", "Absalom", "Perona", "Hogback", "Shimotsuki Ryuma", "Oars",
    "Edward Newgate", "Sakazuki", "Borsalino", "Kuzan", "Marco", "Jozu", "Vista",
    "Sengoku", "Monkey D. Garp", "Boa Hancock", "Shirahoshi",
    "Donquixote Doflamingo", "Donquixote Rosinante", "Rebecca", "Kyros",
    "Diamante", "Trebol", "Pica", "Senor Pink", "Sugar", "Vergo", "Monet",
    "Caesar Clown", "Baby 5", "Buffalo", "Brownbeard", "Bellamy", "Dellinger",
    "Mansherry", "Leo", "Bartolomeo", "Cavendish", "Inuarashi", "Nekomamushi",
    "Carrot", "Pedro", "Bepo", "Charlotte Linlin", "Charlotte Katakuri",
    "Charlotte Perospero", "Charlotte Smoothie", "Charlotte Cracker",
    "Charlotte Pudding", "Vinsmoke Reiju", "Vinsmoke Ichiji", "Vinsmoke Niji",
    "Vinsmoke Yonji", "Kaidou", "Kouzuki Oden", "Kouzuki Momonosuke", "Yamato",
    "Kin'emon", "Denjiro", "Raizo", "Kikunojo", "King", "Queen", "Jack",
    "Vegapunk", "Vegapunk Shaka", "Vegapunk Lilith", "Vegapunk Edison",
    "Vegapunk Pythagoras", "Vegapunk Atlas", "Vegapunk York",
    "Sentomaru", "Issho", "Aramaki",
    "Stussy", "S-Bear", "S-Hawk", "S-Shark", "S-Snake", "Dorry", "Brogy", "Loki",
    "Hajrudin", "Gerd", "Goldberg", "Road", "Oimo", "Kashii", "Stansen", "Jarul",
    "Trafalgar D. Water Law", "Eustass Kid", "Killer", "Basil Hawkins",
    "Scratchmen Apoo", "X Drake", "Jewelry Bonney", "Capone Bege", "Urouge",
    "Gol D. Roger", "Silvers Rayleigh", "Scopper Gaban", "Crocus",
    "Marshall D. Teach", "Jesus Burgess", "Shiryu", "Van Augur", "Joy Boy", "Nika",
    "Jaygarcia Saturn", "Marcus Mars", "Topman Warcury", "Ethanbaron V. Nusjuro",
    "Shepherd Ju Peter", "Figarland Garling",
    "Benn Beckman", "Lucky Roux", "Yasopp", "Monkey D. Dragon",
    "Nerona Imu", "Rocks D. Xebec", "Figarland Shamrock", "Satchels Maffey",
    "Rimoshifu Killingham", "Shepherd Sommers", "Manmayer Gunko", "Harald", "Ryu",
    "Dracule Mihawk", "Candelle", "Zaza", "Douglas Bullet"
]

_OP_SPOILERS_MANGA = {
    "Nerona Imu", "Rocks D. Xebec", "Figarland Shamrock", "Satchels Maffey",
    "Joy Boy", "Nika", "Scopper Gaban", "Rimoshifu Killingham",
    "Shepherd Sommers", "Manmayer Gunko", "Harald", "Candelle", "Zaza",
    "Vegapunk Shaka", "Vegapunk Lilith", "Vegapunk Edison",
    "Vegapunk Pythagoras", "Vegapunk Atlas", "Vegapunk York",
}

_OP_POST_WANO = {
    "Vegapunk", "S-Bear", "S-Hawk", "S-Shark", "S-Snake", "Stussy",
    "Jaygarcia Saturn", "Marcus Mars", "Topman Warcury", "Ethanbaron V. Nusjuro",
    "Shepherd Ju Peter", "Figarland Garling", "Loki",
    "Gerd", "Goldberg", "Road", "Stansen", "Jarul",
    "Nerona Imu", "Rocks D. Xebec", "Figarland Shamrock", "Satchels Maffey",
    "Joy Boy", "Nika", "Scopper Gaban", "Rimoshifu Killingham",
    "Shepherd Sommers", "Manmayer Gunko", "Harald", "Candelle", "Zaza",
    "Vegapunk Shaka", "Vegapunk Lilith", "Vegapunk Edison",
    "Vegapunk Pythagoras", "Vegapunk Atlas", "Vegapunk York",
}

ONEPIECE = Universe(
    key="onepiece",
    name="One Piece",
    api_url="https://onepiece.fandom.com/api.php",
    asset_folder="assets/onepiece",
    characters=_OP_CHARACTERS,
    positions=POSITIONS_STANDARD,
    theme=_build_op_theme(),
    default_filter="manga",
    filters={
        "manga": FilterSet(
            label="📖  Manga  (pool completa)",
            description="Todos os personagens, incluindo arcos exclusivos do mangá.",
            exclude=set(),
        ),
        "anime": FilterSet(
            label="🎥  Anime  (sem spoilers do Mangá)",
            description="Remove personagens exclusivos do mangá.",
            exclude=_OP_SPOILERS_MANGA,
        ),
        "adilson": FilterSet(
            label="🌺  Adilson  (somente até Wano)",
            description="Remove todos os personagens pós-Wano.",
            exclude=_OP_POST_WANO,
        ),
        "teste": FilterSet(
            label="🧪  Teste",
            description="Pool de teste reduzido.",
            exclude=set(_OP_CHARACTERS) - {"Monkey D. Luffy", "Edward Newgate"},
        ),
    },
)


# ──────────────────────────────────────────────
# Invincible
# ──────────────────────────────────────────────

_INV_CHARACTERS = [
    "Invincible", "Omni-Man", "Atom Eve", "William Clockwell", "Amber Bennett",
    "Debbie Grayson", "Cecil Stedman", "Robot", "Rex Splode",
    "Dupli-Kate", "Monster Girl", "Black Samson", "Bulletproof", "Shrinking Rae",
    "Darkwing", "Anissa", "Allen the Alien", "Battle Beast", "Thragg",
    "Conquest", "Angstrom Levy", "Mauler Twins", "Doc Seismic", "Titan",
    "Machine Head", "Kursk", "D.A. Sinclair", "ReAnimen", "Multi-Paul",
    "Flaxan Leader", "Oliver Grayson", "The Immortal",
    "Universa", "Space Racer", "Dinosaurus", "Kregg", "Lucan",
    "Tech Jacket", "Shapesmith", "Paul", "Donald Ferguson",
]

INVINCIBLE = Universe(
    key="invincible",
    name="Invincible",
    api_url="https://amazon-invincible.fandom.com/api.php",
    asset_folder="assets/invencivel",
    characters=_INV_CHARACTERS,
    positions=POSITIONS_STANDARD,
    theme=_build_inv_theme(),
    default_filter="default",
    filters={
        "default": FilterSet(
            label="Pool completa",
            description="Todos os personagens.",
            exclude=set(),
        ),
        "teste": FilterSet(
            label="🧪  Teste",
            description="Pool de teste reduzido.",
            exclude=set(_INV_CHARACTERS) - {"Invincible", "Omni-Man", "Thragg"},
        ),
    },
)


# ──────────────────────────────────────────────
# Naruto
# ──────────────────────────────────────────────

_NARUTO_CHARACTERS = [
    # Konoha — Geração Original
    "Naruto Uzumaki", "Sakura Haruno", "Sasuke Uchiha", "Kakashi Hatake",
    "Rock Lee", "Neji Hyūga", "Tenten", "Might Guy",
    "Shikamaru Nara", "Ino Yamanaka", "Chōji Akimichi", "Asuma Sarutobi",
    "Hinata Hyūga", "Kiba Inuzuka", "Shino Aburame", "Kurenai Yūhi",
    "Iruka Umino", "Konohamaru Sarutobi",
    # Hokages
    "Hashirama Senju", "Tobirama Senju", "Hiruzen Sarutobi",
    "Minato Namikaze", "Tsunade",
    # Sannin & Lendários
    "Jiraiya", "Orochimaru",
    # Clã Uchiha
    "Itachi Uchiha", "Obito Uchiha", "Madara Uchiha", "Fugaku Uchiha",
    "Shisui Uchiha",
    # Clã Hyuga
    "Hiashi Hyūga", "Hanabi Hyūga",
    # Akatsuki
    "Nagato", "Konan", "Kisame Hoshigaki", "Deidara", "Sasori",
    "Hidan", "Kakuzu", "Black Zetsu",
    # Vilões principais
    "Kaguya Ōtsutsuki", "Hagoromo Ōtsutsuki",
    # Outros ninjas de Konoha
    "Anko Mitarashi", "Ibiki Morino", "Yamato", "Sai",
    # Sand Village
    "Gaara", "Temari", "Kankurō", "Chiyo", "Ebizō",
    # Mist Village
    "Zabuza Momochi", "Haku",
    "Mei Terumī", "Ao", "Chōjūrō",
    # Cloud Village
    "Killer B", "A (Fourth Raikage)", "Darui",
    # Stone Village
    "Ōnoki",
    # Grass / outros
    "Kabuto Yakushi",
    # Boruto era (pós-série original)
    "Boruto Uzumaki", "Sarada Uchiha", "Mitsuki", "Kawaki",
    "Himawari Uzumaki", "Shikadai Nara", "Inojin Yamanaka",
    "Chōchō Akimichi", "Metal Lee",
    # Kara / Otsutsuki (Boruto)
    "Isshiki Ōtsutsuki", "Jigen", "Delta", "Koji Kashin",
    "Code", "Ada", "Daemon",
]

_NARUTO_BORUTO_ERA = {
    "Boruto Uzumaki", "Sarada Uchiha", "Mitsuki", "Kawaki",
    "Himawari Uzumaki", "Shikadai Nara", "Inojin Yamanaka",
    "Chōchō Akimichi", "Metal Lee",
    "Isshiki Ōtsutsuki", "Jigen", "Delta", "Koji Kashin",
    "Code", "Ada", "Daemon",
}

NARUTO = Universe(
    key="naruto",
    name="Naruto",
    api_url="https://naruto.fandom.com/api.php",
    asset_folder="assets/naruto",
    characters=_NARUTO_CHARACTERS,
    positions=POSITIONS_STANDARD,
    theme=_build_naruto_theme(),
    default_filter="completo",
    filters={
        "completo": FilterSet(
            label="🍃  Completo  (Naruto + Boruto)",
            description="Todos os personagens, incluindo era Boruto.",
            exclude=set(),
        ),
        "naruto": FilterSet(
            label="🌀  Clássico  (Somente Naruto)",
            description="Remove personagens da era Boruto.",
            exclude=_NARUTO_BORUTO_ERA,
        ),
    },
)


# ──────────────────────────────────────────────
# Bleach
# ──────────────────────────────────────────────

_BLEACH_CHARACTERS = [
    # Substitutas Soul Reapers — Karakura
    "Ichigo Kurosaki", "Orihime Inoue", "Yasutora Sado", "Uryū Ishida",
    "Rukia Kuchiki",
    # 13 Court Guard Squads (Gotei 13)
    "Genryūsai Shigekuni Yamamoto", "Suì-Fēng", "Rōjūrō Ōtoribashi",
    "Retsu Unohana", "Shinji Hirako", "Byakuya Kuchiki",
    "Sajin Komamura", "Shunsui Kyōraku", "Kensei Muguruma",
    "Tōshirō Hitsugaya", "Kenpachi Zaraki", "Mayuri Kurotsuchi",
    "Jūshirō Ukitake",
    # Vice-captains notáveis
    "Renji Abarai", "Momo Hinamori", "Izuru Kira", "Shūhei Hisagi",
    "Rangiku Matsumoto", "Yachiru Kusajishi", "Nemu Kurotsuchi",
    "Isane Kotetsu",
    # Visored
    "Hiyori Sarugaki", "Lisa Yadōmaru", "Love Aikawa",
    "Hachigen Ushōda", "Mashiro Kuna",
    # Arrancar / Espada
    "Sousuke Aizen", "Gin Ichimaru", "Kaname Tōsen",
    "Ulquiorra Cifer", "Grimmjow Jaegerjaquez", "Nnoitra Gilga",
    "Szayelaporro Granz", "Aaroniero Arruruerie", "Zommari Rureaux",
    "Yammy Llargo", "Baraggan Louisenbairn", "Tier Harribel",
    "Coyote Starrk", "Nelliel Tu Odelschwanck",
    "Loly Aivirrne", "Menoly Mallia",
    "Cirucci Sanderwicci", "Dordoni Alessandro Del Socaccio",
    # Fullbringers
    "Kūgo Ginjō", "Riruka Dokugamine", "Shūkurō Tsukishima",
    "Yukio Hans Vorarlberna", "Jackie Tristan", "Giriko Kutsuzawa",
    # Quincy — Wandenreich
    "Yhwach", "Jugram Haschwalth",
    "Askin Nakk Le Vaar", "Bambietta Basterbine", "Bazz-B",
    "Berenice Gabrielli", "BG9", "Cang Du",
    "Driscoll Berci", "Gremmy Thoumeaux", "Jerome Guizbatt",
    "Lille Barro", "Liltotto Lamperd", "Mask De Masculine",
    "Meninas McAllon", "NaNaNa Najahkoop", "Nianzol Weizol",
    "PePe Waccabrada", "Pernida Parnkgjas", "Robert Accutrone",
    "Royd Lloyd", "Loyd Lloyd",
    # Royal Guard / Zero Squad
    "Ichibe'e Hyōsube", "Kirio Hikifune", "Ōetsu Nimaiya",
    "Senjumaru Shutara", "Tenjirō Kirinji",
    # Hollows clássicos
    "Grand Fisher", "Shrieker", "Fishbone D",
    # Outros
    "Kisuke Urahara", "Yoruichi Shihōin", "Tessai Tsukabishi",
    "Kon", "Don Kanonji",
]

_BLEACH_TYBW_ONLY = {
    "Askin Nakk Le Vaar", "Bambietta Basterbine", "Bazz-B",
    "Berenice Gabrielli", "BG9", "Cang Du",
    "Driscoll Berci", "Gremmy Thoumeaux", "Jerome Guizbatt",
    "Lille Barro", "Liltotto Lamperd", "Mask De Masculine",
    "Meninas McAllon", "NaNaNa Najahkoop", "Nianzol Weizol",
    "PePe Waccabrada", "Pernida Parnkgjas", "Robert Accutrone",
    "Royd Lloyd", "Loyd Lloyd",
    "Ichibei Hyosube", "Kirio Hikifune", "Oetsu Nimaiya",
    "Senjumaru Shutara", "Tenjiro Kirinji",
}

BLEACH = Universe(
    key="bleach",
    name="Bleach",
    api_url="https://bleach.fandom.com/api.php",
    asset_folder="assets/bleach",
    characters=_BLEACH_CHARACTERS,
    positions=POSITIONS_STANDARD,
    theme=_build_bleach_theme(),
    default_filter="completo",
    filters={
        "completo": FilterSet(
            label="⚔  Completo  (todas as sagas)",
            description="Todos os personagens, incluindo Thousand-Year Blood War.",
            exclude=set(),
        ),
        "pre_tybw": FilterSet(
            label="🌸  Pré-TYBW  (sem Mil Anos de Sangue)",
            description="Remove personagens exclusivos do arco final.",
            exclude=_BLEACH_TYBW_ONLY,
        ),
        "teste": FilterSet(
            label="🧪  Teste",
            description="Pool de teste reduzido.",
            exclude=set(_BLEACH_CHARACTERS) - {
                "Ichigo Kurosaki", "Sousuke Aizen", "Yhwach",
                "Genryūsai Shigekuni Yamamoto",
            },
        ),
    },
)


# ──────────────────────────────────────────────
# JoJo's Bizarre Adventure (Partes 1-6)
# ──────────────────────────────────────────────

_JOJO_CHARACTERS = [
    # Parte 1 — Phantom Blood
    "Jonathan Joestar", "Dio Brando", "Will A. Zeppeli",
    "Robert E. O. Speedwagon", "Poco", "Dire", "Straizo",
    "Tarkus", "Bruford", "Wang Chan",
    # Parte 2 — Battle Tendency
    "Joseph Joestar", "Caesar Zeppeli", "Lisa Lisa", "Smokey Brown",
    "Rudol von Stroheim", "Kars", "Esidisi", "Wamuu", "Santana",
    # Parte 3 — Stardust Crusaders
    "Jotaro Kujo", "Avdol", "Kakyoin", "Polnareff", "Iggy",
    "Hol Horse", "J. Geil", "Vanilla Ice", "Enya", "N'Doul",
    "Daniel J. D'Arby", "Telence D'Arby",
    "Impostor Captain Tennille", "Devo the Cursed", "Rubber Soul", "Nena",
    "ZZ", "Steely Dan", "Arabia Fats", "Mannish Boy", "Forever", "Cameo",
    "Midler", "Oingo", "Boingo", "Anubis", "Mariah", "Alessi",
    # Parte 4 — Diamond is Unbreakable
    "Josuke", "Koichi", "Okuyasu", "Rohan", "Yoshikage Kira",
    "Yukako", "Shigechi", "Akira Otoishi", "Angelo",
    "Keicho Nijimura", "Toshikazu Hazamada", "Tamami Kobayashi",
    "Ken Oyanagi", "Terunosuke Miyamoto", "Toyohiro Kanedaichi",
    "Masazo Kinoto",
    # Parte 5 — Golden Wind
    "Giorno", "Bucciarati", "Mista", "Narancia", "Abbacchio", "Fugo",
    "Diavolo", "Risotto", "Prosciutto", "Pesci", "Ghiaccio",
    "Cioccolata", "Secco",
    "Polpo", "Mario Zucchero", "Sale", "Formaggio", "Illuso", "Melone",
    "Squalo", "Tiziano", "Carne", "Trish Una",
    # Parte 6 — Stone Ocean
    "Jolyne", "Hermes", "Anasui", "Weather Report", "Foo Fighters",
    "Pucci", "Johngalli A", "Gwess", "Lang Rangler", "Sports Maxx",
    "Rikiel", "Versus",
    "Thunder McQueen", "Miraschon", "Viviano Westwood", "Ungalo", "Kenzo",
    "D an G", "Guccio",
]

JOJO = Universe(
    key="jojo",
    name="JoJo",
    api_url="https://jojo.fandom.com/api.php",
    asset_folder="assets/jojo",
    characters=_JOJO_CHARACTERS,
    positions=POSITIONS_STANDARD,
    theme=_build_jojo_theme(),
    default_filter="classico",
    filters={
        "classico": FilterSet(
            label="⭐  Clássico  (Partes 1-6)",
            description="Draft padrão, sem arena.",
            exclude=set(),
        ),
        "arena": FilterSet(
            label="🏟  Arena  (Partes 1-6)",
            description="Sorteie uma arena que altera o rumo da batalha.",
            exclude=set(),
        ),
        "teste": FilterSet(
            label="🧪  Teste",
            description="Pool de teste reduzido.",
            exclude=set(_JOJO_CHARACTERS) - {
                "Giorno", "Yoshikage Kira", "Diavolo", "Pucci",
                "Joseph Joestar", "Jotaro Kujo", "Dio Brando",
            },
        ),
    },
)


# ──────────────────────────────────────────────
# Jujutsu Kaisen
# ──────────────────────────────────────────────

def _build_jujutsu_theme() -> Theme:
    return Theme(
        bg="#080810",
        panel_bg="#10101E",
        border="#FF6B9D",
        title_fg="#FF6B9D",
        text_fg="#FFD6E8",
        text_secondary="#B89BAD",
        button_start_bg="#C0325A",
        button_start_fg="white",
        font_family="Arial",
        icon="呪",
        entry_bg="#0E0E1A",
        entry_fg="#FFD6E8",
        entry_insert="#FF6B9D",
    )


_JUJUTSU_CHARACTERS = [
    # Protagonistas
    "Yuji Itadori", "Megumi Fushiguro", "Nobara Kugisaki",
    # Professores e feiticeiros de Tokyo
    "Satoru Gojo", "Kento Nanami", "Shoko Ieiri", "Masamichi Yaga",
    # Alunos Tokyo
    "Maki Zenin", "Toge Inumaki", "Panda",
    # Alunos Kyoto
    "Aoi Todo", "Mai Zenin", "Kasumi Miwa", "Noritoshi Kamo",
    "Mechamaru", "Momo Nishimiya",
    # Aliados
    "Yuta Okkotsu", "Mei Mei", "Ui Ui", "Naobito Zenin", "Naoya Zenin", "Choso",
    # Vilões — Maldições
    "Ryomen Sukuna", "Mahito", "Jogo", "Hanami", "Dagon",
    # Vilões — Usuários de Jujutsu
    "Suguru Geto", "Haruta Shigemo", "Toji Fushiguro",
    # Culling Game (parcial)
    "Kirara Hoshi", "Higuruma Hiromi", "Reggie Star", "Remi", "Ryu Ishigori", "Takako Uro",
    "Dhruv Lakdawalla", "Kurourushi",
    # Outros
    "Junpei Yoshino", "Riko Amanai", "Misato Kuroi",
    # Força incerta — comentados até decidir posição no draft
    # "Yuki Tsukumo", "Takaba Fumihiko", "Hajime Kashimo",
    # "Kinji Hakari", "Kenjaku", "Uraume",
]

JUJUTSU = Universe(
    key="jujutsu",
    name="Jujutsu Kaisen",
    api_url="https://jujutsu-kaisen.fandom.com/api.php",
    asset_folder="assets/jujutsu",
    characters=_JUJUTSU_CHARACTERS,
    positions=POSITIONS_STANDARD,
    theme=_build_jujutsu_theme(),
    default_filter="completo",
    filters={
        "completo": FilterSet(
            label="呪  Completo  (Anime até Culling Game)",
            description="Todos os personagens até metade do Jogo do Abate.",
            exclude=set(),
        ),
        "teste": FilterSet(
            label="🧪  Teste",
            description="Pool de teste reduzido.",
            exclude=set(_JUJUTSU_CHARACTERS) - {
                "Satoru Gojo", "Megumi Fushiguro", "Ryomen Sukuna",
                "Higuruma Hiromi", "Yuta Okkotsu",
            },
        ),
    },
    collector_skip={"Ryomen Sukuna"},
)


# ──────────────────────────────────────────────
# Dragon Ball (Z + Super, até o Torneio do Poder + filmes)
# ──────────────────────────────────────────────

def _build_dragonball_theme() -> Theme:
    return Theme(
        bg="#0E1A2B",
        panel_bg="#15263D",
        border="#FF8C1A",
        title_fg="#FF8C1A",
        text_fg="#FFE0B0",
        text_secondary="#9FC0E0",
        button_start_bg="#2E7DD1",
        button_start_fg="white",
        font_family="Arial",
        icon="🐉",
        entry_bg="#10203A",
        entry_fg="#FFE0B0",
        entry_insert="#FF8C1A",
    )


_DRAGONBALL_CHARACTERS = [
    # ─── Dragon Ball clássico ───
    "Bulma", "Chi-Chi", "Yajirobe", "Korin", "Kami", "Mr. Popo",
    "King Piccolo", "Tao Pai Pai", "Pilaf", "Launch",
    "Grandpa Gohan", "Oolong", "Puar", "Ox-King", "Turtle",
    "Fortuneteller Baba", "Bora", "Upa", "Suno", "Nam", "Giran",
    "Bacterian", "Ranfan", "Annin", "Spike the Devil Man", "Mai", "Shu",
    "King Chappa", "Pamput", "Hasky",
    # Exército da Red Ribbon
    "Commander Red", "Staff Officer Black", "General White",
    "General Blue", "Colonel Silver", "Major Metallitron",
    "Ninja Murasaki", "Android 8", "Buyon",
    # Prole do King Piccolo
    "Tambourine", "Cymbal", "Piano", "Drum",

    # ─── Guerreiros Z (heróis) ───
    "Goku", "Vegeta", "Gohan", "Piccolo", "Krillin", "Tien Shinhan", "Yamcha",
    "Chiaotzu", "Master Roshi", "Goten", "Trunks", "Future Trunks", "Gotenks",
    "Vegito", "Android 18", "Android 17", "Android 16", "Majin Buu",
    "Mr. Satan", "Videl", "Dende", "Pan", "Bulla", "Marron", "Bee",

    # ─── Saga dos Saiyajins ───
    "Raditz", "Nappa", "King Kai", "Saibamen", "Bubbles", "Gregory",
    "Princess Snake", "Future Gohan", "King Vegeta", "Tarble",

    # ─── Saga Freeza ───
    "Frieza", "Zarbon", "Dodoria", "Captain Ginyu", "Recoome", "Burter",
    "Jeice", "Guldo", "King Cold", "Nail", "Guru", "Bardock",
    "Cui", "Appule", "Orlen", "Moori", "Cargo",

    # ─── Sagas dos Androides / Cell ───
    "Cell", "Dr. Gero", "Android 19", "Cell Jr.",

    # ─── Saga Majin Boo ───
    "Babidi", "Dabura", "Supreme Kai", "Kibito", "Old Kai", "Uub",
    "Kid Buu", "Super Buu", "Evil Buu", "Good Buu", "Bibidi",
    "Kibito Kai", "Spopovich", "Yamu", "Pui Pui", "Yakon", "Mighty Mask",

    # ─── DBS — Deuses, Anjos e Reis ───
    "Beerus", "Whis", "Jaco", "Zeno", "Future Zeno", "Grand Priest",
    "Monaka", "Gowasu",

    # ─── Torneio dos Universos 6 e 7 ───
    "Hit", "Champa", "Vados", "Cabba", "Frost", "Botamo", "Magetta",

    # ─── Saga do Trunks do Futuro / Goku Black ───
    "Goku Black", "Zamasu", "Fused Zamasu", "Future Mai",

    # ─── Torneio do Poder — Universo 11 (Tropas do Orgulho) ───
    "Jiren", "Toppo", "Dyspo", "Belmod", "Marcarita",
    "Kahseral", "Tupper", "Cocotte", "Vuon", "Zoiray", "Kettle",

    # ─── Torneio do Poder — Universo 6 ───
    "Caulifla", "Kale", "Kefla", "Saonel", "Pirina",

    # ─── Torneio do Poder — Universo 2 ───
    "Ribrianne", "Kakunsa", "Rozie", "Heles", "Pell", "Sour",

    # ─── Torneio do Poder — Universo 3 ───
    "Anilaza", "Paparoni", "Koitsukai", "Borareta", "Panchia",
    "Maji Kayo", "Mosco", "Campari",

    # ─── Torneio do Poder — Universo 4 ───
    "Quitela", "Dercori", "Ganos", "Shantza", "Damon",
    "Caway", "Nink", "Monna", "Cognac",

    # ─── Torneio do Poder — Universo 9 ───
    "Bergamo", "Basil", "Lavender", "Sidra", "Roh",
    "Comfrey", "Sorrel", "Oregano", "Hop", "Chappil",

    # ─── Torneio do Poder — Universo 10 ───
    "Rumsshi", "Obni", "Murichim", "Lilibeu", "Methiop", "Cus",

    # ─── Dragon Ball Super: Super Hero ───
    "Gamma 1", "Gamma 2", "Dr. Hedo", "Magenta", "Carmine", "Cell Max",

    # ─── Dragon Ball GT ───
    "Baby", "Super Android 17", "General Rilldo", "Dr. Myuu",
    "Giru", "Ledgic", "Don Kee", "Sigma Force", "Luud", "Mutchy",
    "Bon Para", "Son Para", "Don Para", "Zoonama",
    # Dragões Sombrios (Shadow Dragons)
    "Syn Shenron", "Haze Shenron", "Rage Shenron",
    "Oceanus Shenron", "Naturon Shenron", "Eis Shenron", "Nuova Shenron",
    "Goku Jr.", "Vegeta Jr.",

    # ─── Dragon Ball Daima ───
    "Glorio", "Panzy", "Gomah", "Degesu", "Dr. Arinsu", "Neva",
    "Tamagami", "Majin Kuu", "Duu", "Marba", "Hybis", "Kadan", "Abura",

    # ─── Filmes ───
    "Broly", "Gogeta", "Cooler", "Turles", "Janemba", "Bojack", "Paragus",
    "Lord Slug", "Garlic Jr.", "Tapion", "Hirudegarn", "Dr. Wheelo",
    "Salza", "Dore", "Neiz", "Android 13", "Android 14",
    "Android 15", "Hatchiyack", "Zangya", "Bido", "Bujin", "Gokua",
    "Cheelai", "Lemo",
]

# Exclusivos de filme — removidos da pool no modo "anime" (sem spoilers de filme).
# GT e Daima NÃO entram aqui: continuam disponíveis no modo "anime".
_DRAGONBALL_MOVIES_ONLY = {
    "Broly", "Gogeta", "Cooler", "Turles", "Janemba", "Bojack", "Paragus",
    "Lord Slug", "Garlic Jr.", "Tapion", "Hirudegarn", "Dr. Wheelo",
    "Salza", "Dore", "Neiz", "Android 13", "Android 14",
    "Android 15", "Hatchiyack", "Zangya", "Bido", "Bujin", "Gokua",
    "Cheelai", "Lemo",
}

DRAGONBALL = Universe(
    key="dragonball",
    name="Dragon Ball",
    api_url="https://dragonball.fandom.com/api.php",
    asset_folder="assets/dragonball",
    characters=_DRAGONBALL_CHARACTERS,
    positions=POSITIONS_STANDARD,
    theme=_build_dragonball_theme(),
    default_filter="completo",
    filters={
        "completo": FilterSet(
            label="🐉  Completo  (Anime até o Torneio do Poder + Filmes)",
            description="Todos os personagens, incluindo Broly e as formas de filme.",
            exclude=set(),
        ),
        "anime": FilterSet(
            label="📺  Anime  (até o Torneio do Poder)",
            description="Só até o fim do anime; remove os exclusivos de filme.",
            exclude=_DRAGONBALL_MOVIES_ONLY,
        ),
        "teste": FilterSet(
            label="🧪  Teste",
            description="Pool de teste reduzido.",
            exclude=set(_DRAGONBALL_CHARACTERS) - {
                "Goku", "Vegeta", "Jiren", "Frieza", "Broly",
            },
        ),
    },
)


# ──────────────────────────────────────────────
# Registry — single source of truth
# ──────────────────────────────────────────────

ALL_UNIVERSES: dict[str, Universe] = {
    "onepiece":   ONEPIECE,
    "bleach":     BLEACH,
    "naruto":     NARUTO,
    "invincible": INVINCIBLE,
    "jojo":       JOJO,
    "jujutsu":    JUJUTSU,
    "dragonball": DRAGONBALL,
}