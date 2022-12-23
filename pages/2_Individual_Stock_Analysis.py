import pandas as pd
import streamlit as st 
import yfinance as yf
from pandas_datareader import data as pdr
from PIL import Image
from nsetools import Nse
nse=Nse()
yf.pdr_override()
im = Image.open("icon.ico")
st.set_page_config(
    page_title="Intraday Stock Analysis",
    page_icon=im,
    layout="wide",
)


all_market=["20MICRONS",
"21STCENMGM",
"3IINFOLTD",
"3MINDIA",
"3PLAND",
"4THDIM",
"5PAISA",
"63MOONS",
"A2ZINFRA",
"AAATECH",
"AAKASH",
"AAREYDRUGS",
"AARON",
"AARTIDRUGS",
"AARTIIND",
"AARTISURF",
"AARVEEDEN",
"AARVI",
"AAVAS",
"ABAN",
"ABB",
"ABBOTINDIA",
"ABCAPITAL",
"ABFRL",
"ABMINTLLTD",
"ABSLAMC",
"ACC",
"ACCELYA",
"ACCURACY",
"ACE",
"ACEINTEG",
"ACI",
"ADANIENT",
"ADANIGREEN",
"ADANIPORTS",
"ADANIPOWER",
"ADANITRANS",
"ADFFOODS",
"ADL",
"ADORWELD",
"ADROITINFO",
"ADSL",
"ADVANIHOTR",
"ADVENZYMES",
"AEGISCHEM",
"AETHER",
"AFFLE",
"AGARIND",
"AGI",
"AGRITECH",
"AGROPHOS",
"AGSTRA",
"AHL",
"AHLADA",
"AHLEAST",
"AHLUCONT",
"AIAENG",
"AIRAN",
"AIROLAM",
"AJANTPHARM",
"AJMERA",
"AJOONI",
"AJRINFRA",
"AKASH",
"AKG",
"AKSHAR",
"AKSHARCHEM",
"AKSHOPTFBR",
"AKZOINDIA",
"ALANKIT",
"ALBERTDAVD",
"ALEMBICLTD",
"ALICON",
"ALKALI",
"ALKEM",
"ALKYLAMINE",
"ALLCARGO",
"ALLSEC",
"ALMONDZ",
"ALOKINDS",
"ALPA",
"ALPHAGEO",
"ALPSINDUS",
"AMARAJABAT",
"AMBER",
"AMBICAAGAR",
"AMBIKCO",
"AMBUJACEM",
"AMDIND",
"AMIORG",
"AMJLAND",
"AMRUTANJAN",
"ANANDRATHI",
"ANANTRAJ",
"ANDHRAPAP",
"ANDHRSUGAR",
"ANDREWYU",
"ANGELONE",
"ANIKINDS",
"ANKITMETAL",
"ANMOL",
"ANTGRAPHIC",
"ANUP",
"ANURAS",
"APARINDS",
"APCL",
"APCOTEXIND",
"APEX",
"APLAPOLLO",
"APLLTD",
"APOLLO",
"APOLLOHOSP",
"APOLLOPIPE",
"APOLLOTYRE",
"APOLSINHOT",
"APTECHT",
"APTUS",
"ARCHIDPLY",
"ARCHIES",
"ARENTERP",
"ARIES",
"ARIHANTCAP",
"ARIHANTSUP",
"ARMANFIN",
"AROGRANITE",
"ARROWGREEN",
"ARSHIYA",
"ARSSINFRA",
"ARTEMISMED",
"ARTNIRMAN",
"ARVEE",
"ARVIND",
"ARVINDFASN",
"ARVSMART",
"ASAHIINDIA",
"ASAHISONG",
"ASAL",
"ASALCBR",
"ASHAPURMIN",
"ASHIANA",
"ASHIMASYN",
"ASHOKA",
"ASHOKLEY",
"ASIANENE",
"ASIANHOTNR",
"ASIANPAINT",
"ASIANTILES",
"ASPINWALL",
"ASTEC",
"ASTERDM",
"ASTRAL",
"ASTRAMICRO",
"ASTRAZEN",
"ASTRON",
"ATFL",
"ATGL",
"ATLANTA",
"ATUL",
"ATULAUTO",
"AUBANK",
"AURIONPRO",
"AUROPHARMA",
"AURUM",
"AUSOMENT",
"AUTOAXLES",
"AUTOIND",
"AVADHSUGAR",
"AVANTIFEED",
"AVROIND",
"AVTNPL",
"AWHCL",
"AWL",
"AXISBANK",
"AXISCADES",
"AXITA",
"AYMSYNTEX",
"BAFNAPH",
"BAGFILMS",
"BAJAJ-AUTO",
"BAJAJCON",
"BAJAJELEC",
"BAJAJFINSV",
"BAJAJHCARE",
"BAJAJHIND",
"BAJAJHLDNG",
"BAJFINANCE",
"BALAJITELE",
"BALAMINES",
"BALAXI",
"BALKRISHNA",
"BALKRISIND",
"BALLARPUR",
"BALMLAWRIE",
"BALPHARMA",
"BALRAMCHIN",
"BANARBEADS",
"BANARISUG",
"BANCOINDIA",
"BANDHANBNK",
"BANG",
"BANKA",
"BANKBARODA",
"BANKINDIA",
"BANSWRAS",
"BARBEQUE",
"BASF",
"BASML",
"BATAINDIA",
"BAYERCROP",
"BBL",
"BBOX",
"BBTC",
"BBTCL",
"BCG",
"BCLIND",
"BCONCEPTS",
"BCP",
"BDL",
"BEARDSELL",
"BECTORFOOD",
"BEDMUTHA",
"BEL",
"BEML",
"BEPL",
"BERGEPAINT",
"BESTAGRO",
"BFINVEST",
"BFUTILITIE",
"BGRENERGY",
"BHAGCHEM",
"BHAGERIA",
"BHAGYANGR",
"BHANDARI",
"BHARATFORG",
"BHARATGEAR",
"BHARATRAS",
"BHARATWIRE",
"BHARTIARTL",
"BHEL",
"BIGBLOC",
"BIKAJI",
"BIL",
"BINDALAGRO",
"BIOCON",
"BIOFILCHEM",
"BIRLACABLE",
"BIRLACORPN",
"BIRLAMONEY",
"BKMINDST",
"BLBLIMITED",
"BLISSGVS",
"BLKASHYAP",
"BLS",
"BLUEDART",
"BLUESTARCO",
"BODALCHEM",
"BOHRAIND",
"BOMDYEING",
"BOROLTD",
"BORORENEW",
"BOSCHLTD",
"BPCL",
"BPL",
"BRIGADE",
"BRITANNIA",
"BRNL",
"BROOKS",
"BSE",
"BSHSL",
"BSL",
"BSOFT",
"BURNPUR",
"BUTTERFLY",
"BVCL",
"BYKE",
"CALSOFT",
"CAMLINFINE",
"CAMPUS",
"CAMS",
"CANBK",
"CANFINHOME",
"CANTABIL",
"CAPACITE",
"CAPLIPOINT",
"CAPTRUST",
"CARBORUNIV",
"CAREERP",
"CARERATING",
"CARTRADE",
"CARYSIL",
"CASTROLIND",
"CCHHL",
"CCL",
"CDSL",
"CEATLTD",
"CELEBRITY",
"CENTENKA",
"CENTEXT",
"CENTRALBK",
"CENTRUM",
"CENTUM",
"CENTURYPLY",
"CENTURYTEX",
"CERA",
"CEREBRAINT",
"CESC",
"CGCL",
"CGPOWER",
"CHALET",
"CHAMBLFERT",
"CHEMBOND",
"CHEMCON",
"CHEMFAB",
"CHEMPLASTS",
"CHENNPETRO",
"CHEVIOT",
"CHOICEIN",
"CHOLAFIN",
"CHOLAHLDNG",
"CIGNITITEC",
"CINELINE",
"CINEVISTA",
"CIPLA",
"CLEAN",
"CLEDUCATE",
"CLNINDIA",
"CLSEL",
"CMICABLES",
"CMSINFO",
"COALINDIA",
"COASTCORP",
"COCHINSHIP",
"COFFEEDAY",
"COFORGE",
"COLPAL",
"COMPINFO",
"COMPUSOFT",
"CONCOR",
"CONFIPET",
"CONSOFINVT",
"CONTROLPR",
"CORALFINAC",
"CORDSCABLE",
"COROMANDEL",
"COSMOFIRST",
"COUNCODOS",
"CRAFTSMAN",
"CREATIVE",
"CREATIVEYE",
"CREDITACC",
"CREST",
"CRISIL",
"CROMPTON",
"CROWN",
"CSBBANK",
"CSLFINANCE",
"CTE",
"CUB",
"CUBEXTUB",
"CUMMINSIND",
"CUPID",
"CYBERMEDIA",
"CYBERTECH",
"CYIENT",
"DAAWAT",
"DABUR",
"DALBHARAT",
"DALMIASUG",
"DAMODARIND",
"DANGEE",
"DATAMATICS",
"DATAPATTNS",
"DBCORP",
"DBL",
"DBOL",
"DBREALTY",
"DBSTOCKBRO",
"DCAL",
"DCBBANK",
"DCI",
"DCM",
"DCMFINSERV",
"DCMNVL",
"DCMSHRIRAM",
"DCMSRIND",
"DCW",
"DCXINDIA",
"DECCANCE",
"DEEPAKFERT",
"DEEPAKNTR",
"DEEPENR",
"DEEPINDS",
"DELHIVERY",
"DELPHIFX",
"DELTACORP",
"DELTAMAGNT",
"DEN",
"DENORA",
"DEVIT",
"DEVYANI",
"DFMFOODS",
"DGCONTENT",
"DHAMPURSUG",
"DHANBANK",
"DHANI",
"DHANUKA",
"DHARMAJ",
"DHARSUGAR",
"DHRUV",
"DHUNINV",
"DIAMONDYD",
"DICIND",
"DIGISPICE",
"DIL",
"DISHTV",
"DIVISLAB",
"DIXON",
"DJML",
"DLF",
"DLINKINDIA",
"DMART",
"DMCC",
"DNAMEDIA",
"DODLA",
"DOLATALGO",
"DOLLAR",
"DONEAR",
"DPABHUSHAN",
"DPSCLTD",
"DPWIRES",
"DRCSYSTEMS",
"DREAMFOLKS",
"DREDGECORP",
"DRREDDY",
"DSSL",
"DTIL",
"DUCON",
"DVL",
"DWARKESH",
"DYCL",
"DYNAMATECH",
"DYNPRO",
"E2E",
"EASEMYTRIP",
"EASTSILK",
"ECLERX",
"EDELWEISS",
"EDUCOMP",
"EICHERMOT",
"EIDPARRY",
"EIFFL",
"EIHAHOTELS",
"EIHOTEL",
"EIMCOELECO",
"EKC",
"ELDEHSG",
"ELECON",
"ELECTCAST",
"ELECTHERM",
"ELGIEQUIP",
"ELGIRUBCO",
"EMAMILTD",
"EMAMIPAP",
"EMAMIREAL",
"EMIL",
"EMKAY",
"EMMBI",
"EMUDHRA",
"ENDURANCE",
"ENERGYDEV",
"ENGINERSIN",
"ENIL",
"EPL",
"EQUIPPP",
"EQUITAS",
"EQUITASBNK",
"ERIS",
"EROSMEDIA",
"ESABINDIA",
"ESCORTS",
"ESSARSHPNG",
"ESSENTIA",
"ESTER",
"ETHOSLTD",
"EUROTEXIND",
"EVEREADY",
"EVERESTIND",
"EXCEL",
"EXCELINDUS",
"EXIDEIND",
"EXPLEOSOL",
"EXXARO",
"FACT",
"FAIRCHEMOR",
"FAZE3Q",
"FCL",
"FCONSUMER",
"FCSSOFT",
"FDC",
"FEDERALBNK",
"FEL",
"FELDVR",
"FIBERWEB",
"FIEMIND",
"FILATEX",
"FINCABLES",
"FINEORG",
"FINOPB",
"FINPIPE",
"FIVESTAR",
"FLEXITUFF",
"FLFL",
"FLUOROCHEM",
"FMGOETZE",
"FMNL",
"FOCUS",
"FOODSIN",
"FORCEMOT",
"FORTIS",
"FOSECOIND",
"FSC",
"FSL",
"FUSION",
"GABRIEL",
"GAEL",
"GAIL",
"GAL",
"GALAXYSURF",
"GALLANTT",
"GANDHITUBE",
"GANECOS",
"GANESHBE",
"GANESHHOUC",
"GANGAFORGE",
"GANGESSECU",
"GARFIBRES",
"GATEWAY",
"GATI",
"GAYAHWS",
"GAYAPROJ",
"GEECEE",
"GEEKAYWIRE",
"GENCON",
"GENESYS",
"GENUSPAPER",
"GENUSPOWER",
"GEOJITFSL",
"GEPIL",
"GESHIP",
"GET&D",
"GFLLIMITED",
"GHCL",
"GICHSGFIN",
"GICRE",
"GILLANDERS",
"GILLETTE",
"GINNIFILA",
"GIPCL",
"GKWLIMITED",
"GLAND",
"GLAXO",
"GLENMARK",
"GLFL",
"GLOBAL",
"GLOBALVECT",
"GLOBE",
"GLOBUSSPR",
"GLS",
"GMBREW",
"GMDCLTD",
"GMMPFAUDLR",
"GMRINFRA",
"GMRP&UI",
"GNA",
"GNFC",
"GOACARBON",
"GOCLCORP",
"GOCOLORS",
"GODFRYPHLP",
"GODHA",
"GODREJAGRO",
"GODREJCP",
"GODREJIND",
"GODREJPROP",
"GOENKA",
"GOKEX",
"GOKUL",
"GOKULAGRO",
"GOLDENTOBC",
"GOLDIAM",
"GOLDTECH",
"GOODLUCK",
"GOODYEAR",
"GOYALALUM",
"GPIL",
"GPPL",
"GPTINFRA",
"GRANULES",
"GRAPHITE",
"GRASIM",
"GRAUWEIL",
"GRAVITA",
"GREAVESCOT",
"GREENLAM",
"GREENPANEL",
"GREENPLY",
"GREENPOWER",
"GRINDWELL",
"GRINFRA",
"GRMOVER",
"GROBTEA",
"GRPLTD",
"GRSE",
"GRWRHITECH",
"GSCLCEMENT",
"GSFC",
"GSPL",
"GSS",
"GTL",
"GTLINFRA",
"GTPL",
"GUFICBIO",
"GUJALKALI",
"GUJAPOLLO",
"GUJGASLTD",
"GUJRAFFIA",
"GULFOILLUB",
"GULFPETRO",
"GULPOLY",
"GVKPIL",
"HAL",
"HAPPSTMNDS",
"HARDWYN",
"HARIOMPIPE",
"HARRMALAYA",
"HARSHA",
"HATHWAY",
"HATSUN",
"HATSUN-RE",
"HAVELLS",
"HAVISHA",
"HBLPOWER",
"HBSL",
"HCC",
"HCG",
"HCL-INSYS",
"HCLTECH",
"HDFC",
"HDFCAMC",
"HDFCBANK",
"HDFCLIFE",
"HDIL",
"HEADSUP",
"HECPROJECT",
"HEG",
"HEIDELBERG",
"HEMIPROP",
"HERANBA",
"HERCULES",
"HERITGFOOD",
"HEROMOTOCO",
"HESTERBIO",
"HEXATRADEX",
"HFCL",
"HGINFRA",
"HGS",
"HIKAL",
"HIL",
"HILTON",
"HIMATSEIDE",
"HINDALCO",
"HINDCOMPOS",
"HINDCON",
"HINDCOPPER",
"HINDMOTORS",
"HINDOILEXP",
"HINDPETRO",
"HINDUNILVR",
"HINDWAREAP",
"HINDZINC",
"HIRECT",
"HISARMETAL",
"HITECH",
"HITECHCORP",
"HITECHGEAR",
"HLEGLAS",
"HLVLTD",
"HMT",
"HMVL",
"HNDFDS",
"HOMEFIRST",
"HONAUT",
"HONDAPOWER",
"HOVS",
"HPAL",
"HPIL",
"HPL",
"HSCL",
"HTMEDIA",
"HUBTOWN",
"HUDCO",
"HUHTAMAKI",
"HYBRIDFIN",
"IBREALEST",
"IBULHSGFIN",
"ICDSLTD",
"ICEMAKE",
"ICICIBANK",
"ICICIGI",
"ICICIPRULI",
"ICIL",
"ICRA",
"IDBI",
"IDEA",
"IDFC",
"IDFCFIRSTB",
"IEX",
"IFBAGRO",
"IFBIND",
"IFCI",
"IFGLEXPOR",
"IGARASHI",
"IGL",
"IGPL",
"IIFL",
"IIFLSEC",
"IIFLWAM",
"IITL",
"IL&FSENGG",
"IL&FSTRANS",
"IMAGICAA",
"IMFA",
"IMPAL",
"INCREDIBLE",
"INDBANK",
"INDHOTEL",
"INDIACEM",
"INDIAGLYCO",
"INDIAMART",
"INDIANB",
"INDIANCARD",
"INDIANHUME",
"INDIGO",
"INDIGOPNTS",
"INDLMETER",
"INDNIPPON",
"INDOAMIN",
"INDOBORAX",
"INDOCO",
"INDORAMA",
"INDOSTAR",
"INDOTECH",
"INDOTHAI",
"INDOWIND",
"INDRAMEDCO",
"INDSWFTLAB",
"INDSWFTLTD",
"INDTERRAIN",
"INDUSINDBK",
"INDUSTOWER",
"INEOSSTYRO",
"INFIBEAM",
"INFOBEAN",
"INFOMEDIA",
"INFY",
"INGERRAND",
"INOXGREEN",
"INOXLEISUR",
"INOXWIND",
"INSECTICID",
"INSPIRISYS",
"INTELLECT",
"INTENTECH",
"INTLCONV",
"INVENTURE",
"IOB",
"IOC",
"IOLCP",
"IONEXCHANG",
"IPCALAB",
"IPL",
"IRB",
"IRCON",
"IRCTC",
"IRFC",
"IRIS",
"IRISDOREME",
"ISEC",
"ISFT",
"ISGEC",
"ISMTLTD",
"ITC",
"ITDC",
"ITDCEM",
"ITI",
"IVC",
"IVP",
"IWEL",
"IZMO",
"J&KBANK",
"JAGRAN",
"JAGSNPHARM",
"JAIBALAJI",
"JAICORPLTD",
"JAIPURKURT",
"JAMNAAUTO",
"JASH",
"JAYAGROGN",
"JAYBARMARU",
"JAYNECOIND",
"JAYSREETEA",
"JBCHEPHARM",
"JBFIND",
"JBMA",
"JCHAC",
"JETAIRWAYS",
"JETFREIGHT",
"JHS",
"JINDALPHOT",
"JINDALPOLY",
"JINDALSAW",
"JINDALSTEL",
"JINDRILL",
"JINDWORLD",
"JISLDVREQS",
"JISLJALEQS",
"JITFINFRA",
"JKCEMENT",
"JKIL",
"JKLAKSHMI",
"JKPAPER",
"JKTYRE",
"JMA",
"JMCPROJECT",
"JMFINANCIL",
"JOCIL",
"JPASSOCIAT",
"JPOLYINVST",
"JPPOWER",
"JSL",
"JSLHISAR",
"JSWENERGY",
"JSWHL",
"JSWISPL",
"JSWSTEEL",
"JTEKTINDIA",
"JTLIND",
"JUBLFOOD",
"JUBLINDS",
"JUBLINGREA",
"JUBLPHARMA",
"JUSTDIAL",
"JWL",
"JYOTHYLAB",
"JYOTISTRUC",
"KABRAEXTRU",
"KAJARIACER",
"KAKATCEM",
"KALPATPOWR",
"KALYANI",
"KALYANIFRG",
"KALYANKJIL",
"KAMATHOTEL",
"KAMDHENU",
"KANANIIND",
"KANORICHEM",
"KANPRPLA",
"KANSAINER",
"KAPSTON",
"KARMAENG",
"KARURVYSYA",
"KAUSHALYA",
"KAVVERITEL",
"KAYA",
"KAYNES",
"KBCGLOBAL",
"KCP",
"KCPSUGIND",
"KDDL",
"KEC",
"KECL",
"KEEPLEARN",
"KEI",
"KELLTONTEC",
"KENNAMET",
"KERNEX",
"KESORAMIND",
"KEYFINSERV",
"KHADIM",
"KHAICHEM",
"KHAITANLTD",
"KHANDSE",
"KICL",
"KILITCH",
"KIMS",
"KINGFA",
"KIOCL",
"KIRIINDUS",
"KIRLFER",
"KIRLOSBROS",
"KIRLOSENG",
"KIRLOSIND",
"KITEX",
"KKCL",
"KMSUGAR",
"KNRCON",
"KOHINOOR",
"KOKUYOCMLN",
"KOLTEPATIL",
"KOPRAN",
"KOTAKBANK",
"KOTARISUG",
"KOTHARIPET",
"KOTHARIPRO",
"KOVAI",
"KPIGREEN",
"KPITTECH",
"KPRMILL",
"KRBL",
"KREBSBIO",
"KRIDHANINF",
"KRISHANA",
"KRITI",
"KRITIKA",
"KRITINUT",
"KRSNAA",
"KSB",
"KSCL",
"KSHITIJPOL",
"KSL",
"KSOLVES",
"KTKBANK",
"KUANTUM",
"L&TFH",
"LAGNAM",
"LAKPRE",
"LALPATHLAB",
"LAMBODHARA",
"LANCER",
"LANDMARK",
"LAOPALA",
"LASA",
"LATENTVIEW",
"LAURUSLABS",
"LAXMICOT",
"LAXMIMACH",
"LCCINFOTEC",
"LEMONTREE",
"LFIC",
"LGBBROSLTD",
"LGBFORGE",
"LIBAS",
"LIBERTSHOE",
"LICHSGFIN",
"LICI",
"LIKHITHA",
"LINC",
"LINCOLN",
"LINDEINDIA",
"LODHA",
"LOKESHMACH",
"LOTUSEYE",
"LOVABLE",
"LOYALTEX",
"LPDC",
"LSIL",
"LT",
"LTIM",
"LTTS",
"LUMAXIND",
"LUMAXTECH",
"LUPIN",
"LUXIND",
"LXCHEM",
"LYKALABS",
"LYPSAGEMS",
"M&M",
"M&MFIN",
"MAANALU",
"MACPOWER",
"MADHAV",
"MADHUCON",
"MADRASFERT",
"MAGADSUGAR",
"MAGNUM",
"MAHABANK",
"MAHAPEXLTD",
"MAHASTEEL",
"MAHEPC",
"MAHESHWARI",
"MAHINDCIE",
"MAHLIFE",
"MAHLOG",
"MAHSCOOTER",
"MAHSEAMLES",
"MAITHANALL",
"MALLCOM",
"MALUPAPER",
"MANAKALUCO",
"MANAKCOAT",
"MANAKSIA",
"MANAKSTEEL",
"MANALIPETC",
"MANAPPURAM",
"MANGALAM",
"MANGCHEFER",
"MANGLMCEM",
"MANINDS",
"MANINFRA",
"MANORAMA",
"MANORG",
"MANUGRAPH",
"MANYAVAR",
"MAPMYINDIA",
"MARALOVER",
"MARATHON",
"MARICO",
"MARINE",
"MARKSANS",
"MARSHALL",
"MARUTI",
"MASFIN",
"MASKINVEST",
"MASTEK",
"MATRIMONY",
"MAWANASUG",
"MAXHEALTH",
"MAXIND",
"MAXVIL",
"MAYURUNIQ",
"MAZDA",
"MAZDOCK",
"MBAPL",
"MBECL",
"MBLINFRA",
"MCDOWELL-N",
"MCL",
"MCLEODRUSS",
"MCX",
"MEDANTA",
"MEDICAMEQ",
"MEDICO",
"MEDPLUS",
"MEGASOFT",
"MEGASTAR",
"MELSTAR",
"MENONBE",
"MEP",
"MERCATOR",
"METALFORGE",
"METROBRAND",
"METROPOLIS",
"MFL",
"MFSL",
"MGEL",
"MGL",
"MHLXMIRU",
"MHRIL",
"MIDHANI",
"MINDACORP",
"MINDTECK",
"MIRCELECTR",
"MIRZAINT",
"MITCON",
"MITTAL",
"MMFL",
"MMP",
"MMTC",
"MODIRUBBER",
"MODISONLTD",
"MOHITIND",
"MOIL",
"MOKSH",
"MOL",
"MOLDTECH",
"MOLDTKPAC",
"MONARCH",
"MONTECARLO",
"MORARJEE",
"MOREPENLAB",
"MOTHERSON",
"MOTILALOFS",
"MOTOGENFIN",
"MPHASIS",
"MPSLTD",
"MRF",
"MRO-TEK",
"MRPL",
"MSPL",
"MSTCLTD",
"MSUMI",
"MTARTECH",
"MTEDUCARE",
"MTNL",
"MUKANDLTD",
"MUKTAARTS",
"MUNJALAU",
"MUNJALSHOW",
"MURUDCERA",
"MUTHOOTCAP",
"MUTHOOTFIN",
"NACLIND",
"NAGREEKCAP",
"NAGREEKEXP",
"NAHARCAP",
"NAHARINDUS",
"NAHARPOLY",
"NAHARSPING",
"NAM-INDIA",
"NARMADA",
"NATCOPHARM",
"NATHBIOGEN",
"NATIONALUM",
"NATNLSTEEL",
"NAUKRI",
"NAVA",
"NAVINFLUOR",
"NAVKARCORP",
"NAVNETEDUL",
"NAZARA",
"NBCC",
"NBIFIN",
"NCC",
"NCLIND",
"NDGL",
"NDL",
"NDRAUTO",
"NDTV",
"NECCLTD",
"NECLIFE",
"NELCAST",
"NELCO",
"NEOGEN",
"NESCO",
"NESTLEIND",
"NETWORK18",
"NEULANDLAB",
"NEWGEN",
"NEXTMEDIA",
"NFL",
"NGIL",
"NGLFINE",
"NH",
"NHPC",
"NIACL",
"NIBL",
"NIITLTD",
"NILAINFRA",
"NILASPACES",
"NILKAMAL",
"NIPPOBATRY",
"NIRAJ",
"NIRAJISPAT",
"NITCO",
"NITINSPIN",
"NITIRAJ",
"NKIND",
"NLCINDIA",
"NMDC",
"NOCIL",
"NOIDATOLL",
"NORBTEAEXP",
"NOVARTIND",
"NRAIL",
"NRBBEARING",
"NSIL",
"NTPC",
"NUCLEUS",
"NURECA",
"NUVOCO",
"NXTDIGITAL",
"NYKAA",
"OAL",
"OBCL",
"OBEROIRLTY",
"OCCL",
"OFSS",
"OIL",
"OILCOUNTUB",
"OLECTRA",
"OMAXAUTO",
"OMAXE",
"OMINFRAL",
"OMKARCHEM",
"ONELIFECAP",
"ONEPOINT",
"ONGC",
"ONMOBILE",
"ONWARDTEC",
"OPTIEMUS",
"ORBTEXP",
"ORCHPHARMA",
"ORICONENT",
"ORIENTABRA",
"ORIENTALTL",
"ORIENTBELL",
"ORIENTCEM",
"ORIENTELEC",
"ORIENTHOT",
"ORIENTLTD",
"ORIENTPPR",
"ORISSAMINE",
"ORTINLAB",
"OSIAHYPER",
"OSWALAGRO",
"PAGEIND",
"PAISALO",
"PALASHSECU",
"PALREDTEC",
"PANACEABIO",
"PANACHE",
"PANAMAPET",
"PANSARI",
"PAR",
"PARACABLES",
"PARADEEP",
"PARAGMILK",
"PARAS",
"PARASPETRO",
"PARSVNATH",
"PASUPTAC",
"PATANJALI",
"PATELENG",
"PATINTLOG",
"PAYTM",
"PCBL",
"PCJEWELLER",
"PDMJEPAPER",
"PDSL",
"PEARLPOLY",
"PEL",
"PENIND",
"PENINLAND",
"PERSISTENT",
"PETRONET",
"PFC",
"PFIZER",
"PFOCUS",
"PFS",
"PGEL",
"PGHH",
"PGHL",
"PGIL",
"PHOENIXLTD",
"PIDILITIND",
"PIIND",
"PILANIINVS",
"PILITA",
"PIONDIST",
"PIONEEREMB",
"PITTIENG",
"PIXTRANS",
"PKTEA",
"PLASTIBLEN",
"PNB",
"PNBGILTS",
"PNBHOUSING",
"PNC",
"PNCINFRA",
"PODDARHOUS",
"PODDARMENT",
"POKARNA",
"POLICYBZR",
"POLYCAB",
"POLYMED",
"POLYPLEX",
"PONNIERODE",
"POONAWALLA",
"POWERGRID",
"POWERINDIA",
"POWERMECH",
"PPAP",
"PPL",
"PPLPHARMA",
"PRAENG",
"PRAJIND",
"PRAKASH",
"PRAKASHSTL",
"PRAXIS",
"PRECAM",
"PRECOT",
"PRECWIRE",
"PREMEXPLN",
"PREMIER",
"PREMIERPOL",
"PRESSMN",
"PRESTIGE",
"PRICOLLTD",
"PRIMESECU",
"PRINCEPIPE",
"PRITI",
"PRITIKAUTO",
"PRIVISCL",
"PROZONINTU",
"PRSMJOHNSN",
"PRUDENT",
"PSB",
"PSPPROJECT",
"PTC",
"PTL",
"PUNJABCHEM",
"PURVA",
"PVP",
"PVR",
"QUESS",
"QUICKHEAL",
"RADAAN",
"RADHIKAJWE",
"RADICO",
"RADIOCITY",
"RAILTEL",
"RAIN",
"RAINBOW",
"RAJESHEXPO",
"RAJMET",
"RAJRATAN",
"RAJSREESUG",
"RAJTV",
"RALLIS",
"RAMANEWS",
"RAMAPHO",
"RAMASTEEL",
"RAMCOCEM",
"RAMCOIND",
"RAMCOSYS",
"RAMKY",
"RAMRAT",
"RANASUG",
"RANEENGINE",
"RANEHOLDIN",
"RATEGAIN",
"RATNAMANI",
"RAYMOND",
"RBA",
"RBL",
"RBLBANK",
"RCF",
"RECLTD",
"REDINGTON",
"REFEX",
"REGENCERAM",
"RELAXO",
"RELCHEMQ",
"RELIANCE",
"RELIGARE",
"RELINFRA",
"REMSONSIND",
"RENUKA",
"REPCOHOME",
"REPL",
"REPRO",
"RESPONIND",
"REVATHI",
"RGL",
"RHFL",
"RHIM",
"RICOAUTO",
"RIIL",
"RITCO",
"RITES",
"RKDL",
"RKEC",
"RKFORGE",
"RMCL",
"RML",
"RNAVAL",
"ROHLTD",
"ROLEXRINGS",
"ROLLT",
"ROLTA",
"ROML",
"ROSSARI",
"ROSSELLIND",
"ROTO",
"ROUTE",
"RPGLIFE",
"RPOWER",
"RPPINFRA",
"RPPL",
"RPSGVENT",
"RSSOFTWARE",
"RSWM",
"RSWM-RE",
"RSYSTEMS",
"RTNINDIA",
"RTNPOWER",
"RUBYMILLS",
"RUCHINFRA",
"RUCHIRA",
"RUPA",
"RUSHIL",
"RUSTOMJEE",
"RVHL",
"RVNL",
"S&SPOWER",
"SABEVENTS",
"SADBHAV",
"SADBHIN",
"SAFARI",
"SAGARDEEP",
"SAGCEM",
"SAIL",
"SAKAR",
"SAKHTISUG",
"SAKSOFT",
"SAKUMA",
"SALASAR",
"SALONA",
"SALSTEEL",
"SALZERELEC",
"SAMBHAAV",
"SANDESH",
"SANDHAR",
"SANGAMIND",
"SANGHIIND",
"SANGHVIMOV",
"SANGINITA",
"SANOFI",
"SANSERA",
"SANWARIA",
"SAPPHIRE",
"SARDAEN",
"SAREGAMA",
"SARLAPOLY",
"SARVESHWAR",
"SASKEN",
"SASTASUNDR",
"SATHAISPAT",
"SATIA",
"SATIN",
"SATINDLTD",
"SBC",
"SBCL",
"SBICARD",
"SBILIFE",
"SBIN",
"SCAPDVR",
"SCHAEFFLER",
"SCHAND",
"SCHNEIDER",
"SCI",
"SCPL",
"SDBL",
"SEAMECLTD",
"SECURCRED",
"SECURKLOUD",
"SEJALLTD",
"SELAN",
"SEPC",
"SEPOWER",
"SEQUENT",
"SERVOTECH",
"SESHAPAPER",
"SETCO",
"SETUINFRA",
"SFL",
"SGIL",
"SGL",
"SHAHALLOYS",
"SHAILY",
"SHAKTIPUMP",
"SHALBY",
"SHALPAINTS",
"SHANKARA",
"SHANTI",
"SHANTIGEAR",
"SHARDACROP",
"SHARDAMOTR",
"SHAREINDIA",
"SHEMAROO",
"SHILPAMED",
"SHIVALIK",
"SHIVAMAUTO",
"SHIVAMILLS",
"SHIVATEX",
"SHK",
"SHOPERSTOP",
"SHRADHA",
"SHREDIGCEM",
"SHREECEM",
"SHREEPUSHK",
"SHREERAMA",
"SHRENIK",
"SHREYANIND",
"SHREYAS",
"SHRIPISTON",
"SHRIRAMFIN",
"SHRIRAMPPS",
"SHYAMCENT",
"SHYAMMETL",
"SHYAMTEL",
"SICAL",
"SIEMENS",
"SIGACHI",
"SIGIND",
"SIKKO",
"SIL",
"SILGO",
"SILINV",
"SILLYMONKS",
"SILVERTUC",
"SIMBHALS",
"SIMPLEXINF",
"SINTERCOM",
"SINTEX",
"SIRCA",
"SIS",
"SITINET",
"SIYSIL",
"SJS",
"SJVN",
"SKFINDIA",
"SKIPPER",
"SKMEGGPROD",
"SMARTLINK",
"SMCGLOBAL",
"SMLISUZU",
"SMLT",
"SMSLIFE",
"SMSPHARMA",
"SNOWMAN",
"SOBHA",
"SOFTTECH",
"SOLARA",
"SOLARINDS",
"SOMANYCERA",
"SOMATEX",
"SOMICONVEY",
"SONACOMS",
"SONAMCLOCK",
"SONATSOFTW",
"SOTL",
"SOUTHBANK",
"SOUTHWEST",
"SPAL",
"SPANDANA",
"SPARC",
"SPCENET",
"SPECIALITY",
"SPENCERS",
"SPIC",
"SPICEJET",
"SPLIL",
"SPLPETRO",
"SPMLINFRA",
"SPORTKING",
"SPTL",
"SREEL",
"SRF",
"SRHHYPOLTD",
"SRPL",
"SSWL",
"STAR",
"STARCEMENT",
"STARHEALTH",
"STARPAPER",
"STARTECK",
"STCINDIA",
"STEELCAS",
"STEELCITY",
"STEELXIND",
"STEL",
"STERTOOLS",
"STLTECH",
"STOVEKRAFT",
"STYLAMIND",
"SUBCAPCITY",
"SUBEXLTD",
"SUBROS",
"SUDARSCHEM",
"SUKHJITS",
"SULA",
"SUMEETINDS",
"SUMICHEM",
"SUMIT",
"SUMMITSEC",
"SUNCLAYLTD",
"SUNDARAM",
"SUNDARMFIN",
"SUNDARMHLD",
"SUNDRMBRAK",
"SUNDRMFAST",
"SUNFLAG",
"SUNPHARMA",
"SUNTECK",
"SUNTV",
"SUPERHOUSE",
"SUPERSPIN",
"SUPRAJIT",
"SUPREMEENG",
"SUPREMEIND",
"SUPREMEINF",
"SUPRIYA",
"SURANASOL",
"SURANAT&P",
"SURYALAXMI",
"SURYAROSNI",
"SURYODAY",
"SUTLEJTEX",
"SUULD",
"SUVEN",
"SUVENPHAR",
"SUVIDHAA",
"SUZLON",
"SVPGLOB",
"SWANENERGY",
"SWARAJENG",
"SWELECTES",
"SWSOLAR",
"SYMPHONY",
"SYNCOMF",
"SYNGENE",
"SYRMA",
"TAINWALCHM",
"TAJGVK",
"TAKE",
"TALBROAUTO",
"TANLA",
"TANTIACONS",
"TARAPUR",
"TARC",
"TARMAT",
"TARSONS",
"TASTYBITE",
"TATACHEM",
"TATACOFFEE",
"TATACOMM",
"TATACONSUM",
"TATAELXSI",
"TATAINVEST",
"TATAMETALI",
"TATAMOTORS",
"TATAMTRDVR",
"TATAPOWER",
"TATASTEEL",
"TATASTLLP",
"TATVA",
"TBZ",
"TCI",
"TCIEXP",
"TCNSBRANDS",
"TCPLPACK",
"TCS",
"TDPOWERSYS",
"TEAMLEASE",
"TECHIN",
"TECHM",
"TECHNOE",
"TEGA",
"TEJASNET",
"TEMBO",
"TERASOFT",
"TEXINFRA",
"TEXMOPIPES",
"TEXRAIL",
"TFCILTD",
"TFL",
"TGBHOTELS",
"THANGAMAYL",
"THEINVEST",
"THEMISMED",
"THERMAX",
"THOMASCOOK",
"THOMASCOTT",
"THYROCARE",
"TI",
"TIDEWATER",
"TIIL",
"TIINDIA",
"TIJARIA",
"TIL",
"TIMESGTY",
"TIMETECHNO",
"TIMKEN",
"TINPLATE",
"TIPSFILMS",
"TIPSINDLTD",
"TIRUMALCHM",
"TIRUPATIFL",
"TITAN",
"TMB",
"TNPETRO",
"TNPL",
"TNTELE",
"TOKYOPLAST",
"TORNTPHARM",
"TORNTPOWER",
"TOTAL",
"TOUCHWOOD",
"TPLPLASTEH",
"TRACXN",
"TREEHOUSE",
"TREJHARA",
"TRENT",
"TRF",
"TRIDENT",
"TRIGYN",
"TRIL",
"TRITURBINE",
"TRIVENI",
"TRU",
"TTKHLTCARE",
"TTKPRESTIG",
"TTL",
"TTML",
"TV18BRDCST",
"TVSELECT",
"TVSMOTOR",
"TVSSRICHAK",
"TVTODAY",
"TVVISION",
"TWL",
"UBL",
"UCALFUEL",
"UCOBANK",
"UDAICEMENT",
"UFLEX",
"UFO",
"UGARSUGAR",
"UGROCAP",
"UJAAS",
"UJJIVAN",
"UJJIVANSFB",
"ULTRACEMCO",
"UMAEXPORTS",
"UMANGDAIRY",
"UMESLTD",
"UNICHEMLAB",
"UNIDT",
"UNIENTER",
"UNIINFO",
"UNIONBANK",
"UNIPARTS",
"UNITECH",
"UNITEDPOLY",
"UNITEDTEA",
"UNIVASTU",
"UNIVCABLES",
"UNIVPHOTO",
"UNOMINDA",
"UPL",
"URJA",
"USHAMART",
"UTIAMC",
"UTTAMSUGAR",
"V2RETAIL",
"VADILALIND",
"VAIBHAVGBL",
"VAISHALI",
"VAKRANGEE",
"VALIANTORG",
"VARDHACRLC",
"VARDMNPOLY",
"VARROC",
"VASCONEQ",
"VASWANI",
"VBL",
"VCL",
"VEDL",
"VENKEYS",
"VENUSPIPES",
"VENUSREM",
"VERANDA",
"VERTOZ",
"VESUVIUS",
"VETO",
"VGUARD",
"VHL",
"VIDHIING",
"VIJAYA",
"VIJIFIN",
"VIKASECO",
"VIKASLIFE",
"VIKASPROP",
"VIKASWSP",
"VIMTALABS",
"VINATIORGA",
"VINDHYATEL",
"VINEETLAB",
"VINNY",
"VINYLINDIA",
"VIPCLOTHNG",
"VIPIND",
"VIPULLTD",
"VISAKAIND",
"VISASTEEL",
"VISESHINFO",
"VISHAL",
"VISHNU",
"VISHWARAJ",
"VIVIDHA",
"VIVIMEDLAB",
"VLSFINANCE",
"VMART",
"VOLTAMP",
"VOLTAS",
"VRLLOG",
"VSSL",
"VSTIND",
"VSTTILLERS",
"VTL",
"WABAG",
"WALCHANNAG",
"WANBURY",
"WATERBASE",
"WEALTH",
"WEBELSOLAR",
"WEIZMANIND",
"WELCORP",
"WELENT",
"WELINV",
"WELSPUNIND",
"WENDT",
"WESTLIFE",
"WEWIN",
"WFL",
"WHEELS",
"WHIRLPOOL",
"WILLAMAGOR",
"WINDLAS",
"WINDMACHIN",
"WINPRO",
"WIPL",
"WIPRO",
"WOCKPHARMA",
"WONDERLA",
"WORTH",
"WSTCSTPAPR",
"XCHANGING",
"XELPMOC",
"XPROINDIA",
"YAARI",
"YESBANK",
"YUKEN",
"ZEEL",
"ZEELEARN",
"ZEEMEDIA",
"ZENITHEXPO",
"ZENITHSTL",
"ZENSARTECH",
"ZENTEC",
"ZFCVINDIA",
"ZIMLAB",
"ZODIAC",
"ZODIACLOTH",
"ZOMATO",
"ZOTA",
"ZUARI",
"ZUARIIND",
"ZYDUSLIFE",
"ZYDUSWELL",]

import plotly.graph_objects as go


dropdown=st.selectbox('Pick your desired asset',all_market)
ycode=dropdown+".NS"
if len(dropdown)>0:
    df=pdr.get_data_yahoo(ycode,period='1d',interval='1m')

 
st.markdown('---')



ab=nse.get_quote(dropdown)
ab['% Price Change']=ab['pChange']+"%"
ab['Last Traded Price']="₹"+str(ab['lastPrice'])
ab['Company Name']=ab['companyName']
ab['Price Change']="₹"+str(ab['change'])
ab['Open']="₹"+str(ab['open'])
ab["Today's High"]="₹"+str(ab['dayHigh'])
ab["Today's Low"]="₹"+str(ab['dayLow'])
ab['Total Traded Value(in Lakhs)']="₹"+str(ab['totalTradedValue'])
ab['No. of shares Traded']=ab['totalTradedVolume']
ab['52 Week High']="₹"+str(ab['high52'])
ab['52 Week Low']="₹"+str(ab['low52'])
required_data=['Company Name','Last Traded Price','Price Change','% Price Change','Open',"Today's High","Today's Low",'Total Traded Value(in Lakhs)','No. of shares Traded','52 Week High','52 Week Low']



#st.sidebar.image(im, width=200)
st.sidebar.markdown(f'# {dropdown} Stock Price Analysis')
for i in required_data:
    st.sidebar.write(f'{i} : {ab[i]}') 

st.sidebar.markdown('---')
st.sidebar.write('Developed by Siddharth Kumar')
st.sidebar.write('Contact at mm21b061@smail.iitm.ac.in ')

from plotly.subplots import make_subplots
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
               vertical_spacing=0.03, subplot_titles=(f'{dropdown}', 'Volume'), 
               row_width=[0.2, 0.7])

# Plot OHLC on 1st row
fig.add_trace(go.Candlestick(x=df.index, open=df["Open"], high=df["High"],
                low=df["Low"], close=df["Close"], name="OHLC"), 
                row=1, col=1
)

# Bar trace for volumes on 2nd row without legend
fig.add_trace(go.Bar(x=df.index, y=df['Volume'], showlegend=False), row=2, col=1)

# Do not show OHLC's rangeslider plot 
fig.update(layout_xaxis_rangeslider_visible=False)

st.plotly_chart(fig)
