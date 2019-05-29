local u = mw.ustring.char

-- UTF-8 encoded strings for some commonly-used diacritics
local GRAVE     = u(0x0300)
local ACUTE     = u(0x0301)
local CIRC      = u(0x0302)
local TILDE     = u(0x0303)
local MACRON    = u(0x0304)
local BREVE     = u(0x0306)
local DOTABOVE  = u(0x0307)
local DIAER     = u(0x0308)
local CARON     = u(0x030C)
local DGRAVE    = u(0x030F)
local INVBREVE  = u(0x0311)
local DOTBELOW  = u(0x0323)
local RINGBELOW = u(0x0325)
local CEDILLA   = u(0x0327)
local OGONEK    = u(0x0328)

-- Puncuation to be used for standardChars field
local PUNCTUATION = ' !#$%&*+,-./:;<=>?@^_`|~\'()'

local Cyrl = {"Cyrl"}
local Latn = {"Latn"}
local LatnArab = {"Latn", "Arab"}

local m = {}

m["aa"] = {
	"Afar",
	"Q27811",
	"cus",
	otherNames = {"Qafar"},
	scripts = Latn,
}

m["ab"] = {
	"Abkhaz",
	"Q5111",
	"cau-abz",
	otherNames = {"Abkhazian", "Abxazo"},
	scripts = {"Cyrl", "Geor", "Latn"},
	translit_module = "ab-translit",
	override_translit = true,
	entry_name = {
		from = {GRAVE, ACUTE},
		to   = {}} ,
}

m["ae"] = {
	"Avestan",
	"Q29572",
	"ira-cen",
	otherNames = {"Zend", "Old Bactrian"},
	scripts = {"Avst", "Gujr"},
	translit_module = "Avst-translit",
	wikipedia_article = "Avestan",
}

m["af"] = {
	"Afrikaans",
	"Q14196",
	"gmw",
	scripts = LatnArab,
	ancestors = {"nl"},
	sort_key = {
		from = {"[äáâà]", "[ëéêè]", "[ïíîì]", "[öóôò]", "[üúûù]", "[ÿýŷỳ]", "^-", "'"},
		to   = {"a"	 , "e"	, "i"	, "o"	, "u"  , "y" }} ,
}

m["ak"] = {
	"Akan",
	"Q28026",
	"alv-kwa",
	otherNames = {"Twi-Fante", "Twi", "Fante", "Fanti", "Asante", "Akuapem"},
	scripts = Latn,
}

m["am"] = {
	"Amharic",
	"Q28244",
	"sem-eth",
	scripts = {"Ethi"},
	translit_module = "Ethi-translit",
}

m["an"] = {
	"Aragonese",
	"Q8765",
	"roa-ibe",
	scripts = Latn,
	ancestors = {"roa-oan"},
}

m["ar"] = {
	"Arabic",
	"Q13955",
	"sem-arb",
	otherNames = {"Modern Standard Arabic", "Standard Arabic", "Literary Arabic", "Classical Arabic"},
	scripts = {"Arab", "Brai"},
	-- alif waṣl to alif, remove diacritics
	entry_name = {
		from = {u(0x0671), u(0x064B), u(0x064C), u(0x064D), u(0x064E), u(0x064F), u(0x0650), u(0x0651), u(0x0652), u(0x0670), u(0x0640)},
		to   = {u(0x0627)}},
	translit_module = "ar-translit",
	standardChars = "ء-غف-ْٰٱ" .. PUNCTUATION .. "٠-٩،؛؟٫٬ـ",
}

m["as"] = {
	"Assamese",
	otherNames = {"Asamiya"},
	"Q29401",
	"inc",
	scripts = {"as-Beng"},
	ancestors = {"inc-mas"},
	translit_module = "as-translit",
}

m["av"] = {
	"Avar",
	"Q29561",
	"cau-nec",
	otherNames = {"Avaric"},
	scripts = Cyrl,
	ancestors = {"oav"},
	translit_module = "av-translit",
	override_translit = true,
	entry_name = {
		from = {GRAVE, ACUTE},
		to   = {}} ,
}

m["ay"] = {
	"Aymara",
	"Q4627",
	"sai-aym",
	otherNames = {"Southern Aymara", "Central Aymara"},
	scripts = Latn,
}

m["az"] = {
	"Azerbaijani",
	"Q9292",
	"trk-ogz",
	otherNames = {"Azeri", "Azari", "Azeri Turkic", "Azerbaijani Turkic", "North Azerbaijani", "South Azerbaijani", "Afshar", "Afshari", "Afshar Azerbaijani", "Afchar", "Qashqa'i", "Qashqai", "Kashkay", "Sonqor"},
	scripts = {"Latn", "Cyrl", "fa-Arab"},
	ancestors = {"trk-oat"},
}

m["ba"] = {
	"Bashkir",
	"Q13389",
	"trk-kip",
	scripts = Cyrl,
	translit_module = "ba-translit",
	override_translit = true,
}

m["be"] = {
	"Belarusian",
	"Q9091",
	"zle",
	otherNames = {"Belorussian", "Belarusan", "Bielorussian", "Byelorussian", "Belarussian", "White Russian"},
	scripts = Cyrl,
	ancestors = {"orv"},
	translit_module = "be-translit",
	sort_key = {
		from = {"Ё", "ё"},
		to   = {"Е" , "е"}},
	entry_name = {
		from = {"Ѐ", "ѐ", GRAVE, ACUTE},
		to   = {"Е", "е"}},
}

m["bg"] = {
	"Bulgarian",
	"Q7918",
	"zls",
	scripts = {"Cyrl"},
	ancestors = {"cu"},
	translit_module = "bg-translit",
	entry_name = {
		from = {"Ѐ", "ѐ", "Ѝ", "ѝ", GRAVE, ACUTE},
		to   = {"Е", "е", "И", "и"}},
}

m["bh"] = {
	"Bihari",
	"Q135305",
	"inc",
	scripts = {"Deva"},
	ancestors = {"inc-mgd"},
}

m["bi"] = {
	"Bislama",
	"Q35452",
	"crp",
	scripts = Latn,
	ancestors = {"en"},
}

m["bm"] = {
	"Bambara",
	"Q33243",
	"dmn-man",
	otherNames = {"Bamanankan"},
	scripts = Latn,
}

m["bn"] = {
	"Bengali",
	"Q9610",
	"inc",
	otherNames = {"Bangla"},
	scripts = {"Beng", "Newa"},
	ancestors = {"inc-mbn"},
	translit_module = "bn-translit",
}

m["bo"] = {
	"Tibetan",
	"Q34271",
	"tbq",
	otherNames = {"Ü", "Dbus", "Lhasa", "Lhasa Tibetan", "Amdo Tibetan", "Amdo", "Panang", "Khams", "Khams Tibetan", "Khamba", "Tseku", "Dolpo", "Humla", "Limi", "Lhomi", "Shing Saapa", "Mugom", "Mugu", "Nubri", "Walungge", "Gola", "Thudam", "Lowa", "Loke", "Mustang", "Tichurong"}, -- and "Gyalsumdo", "Lower Manang"? "Kyirong"?
	scripts = {"Tibt"}, -- sometimes Deva?
	ancestors = {"xct"},
	translit_module = "bo-translit",
	override_translit = true,
}

m["br"] = {
	"Breton",
	"Q12107",
	"cel-bry",
	scripts = Latn,
	ancestors = {"xbm"},
}

m["ca"] = {
	"Catalan",
	"Q7026",
	"roa",
	otherNames = {"Valencian"},
	scripts = Latn,
	ancestors = {"roa-oca"},
	sort_key = {
		from = {"à", "[èé]", "[íï]", "[òó]", "[úü]", "ç", "l·l"},
		to   = {"a", "e"   , "i"   , "o"   , "u"   , "c", "ll" }} ,
}

m["ce"] = {
	"Chechen",
	"Q33350",
	"cau-nkh",
	scripts = Cyrl,
	translit_module = "ce-translit",
	override_translit = true,
	entry_name = {
		from = {MACRON},
		to   = {}},
}

m["ch"] = {
	"Chamorro",
	"Q33262",
	"poz-sus",
	otherNames = {"Chamoru"},
	scripts = Latn,
}

m["co"] = {
	"Corsican",
	"Q33111",
	"roa-itd",
	otherNames = {"Corsu"},
	scripts = Latn,
}

m["cr"] = {
	"Cree",
	"Q33390",
	"alg",
	scripts = {"Cans", "Latn"},
	translit_module = "cr-translit",
}

m["cs"] = {
	"Czech",
	"Q9056",
	"zlw",
	scripts = Latn,
	ancestors = {"zlw-ocs"},
	sort_key = {
		from = {"á", "é", "í", "ó", "[úů]", "ý"},
		to   = {"a", "e", "i", "o", "u"   , "y"}} ,
}

m["cu"] = {
	"Old Church Slavonic",
	"Q35499",
	"zls",
	otherNames = {"Old Church Slavic"},
	scripts = {"Cyrs", "Glag"},
	translit_module = "Cyrs-Glag-translit",
	entry_name = {
		from = {u(0x0484)}, -- kamora
		to   = {}},
	sort_key = {
		from = {"оу", "є"},
		to   = {"у" , "е"}} ,
}

m["cv"] = {
	"Chuvash",
	"Q33348",
	"trk-ogr",
	scripts = Cyrl,
	translit_module = "cv-translit",
	override_translit = true,
}

m["cy"] = {
	"Welsh",
	"Q9309",
	"cel-bry",
	scripts = Latn,
	ancestors = {"wlm"},
	sort_key = {
		from = {"[âáàä]", "ch", "dd", "[êéèë]", "ff", "ngh", "[îíìï]", "ll", "[ôóòö]", "ph", "rh", "th", "[ûúùü]", "[ŵẃẁẅ]", "[ŷýỳÿ]", "'"},
		to   = {"a"	    , "c~", "d~", "e"	  , "f~", "g~h", "i"	  , "l~", "o"	  , "p~", "r~", "t~", "u"	  , "w"     , "y"	       }} ,
	standardChars = "A-IL-PR-UWYa-il-pr-uwy0-9ÂâÊêÎîÔôÛûŴŵŶŷ" .. PUNCTUATION,
}

m["da"] = {
	"Danish",
	"Q9035",
	"gmq",
	scripts = Latn,
	ancestors = {"gmq-oda"},
}

m["de"] = {
	"German",
	"Q188",
	"gmw",
	otherNames = {"High German", "New High German", "Deutsch"},
	scripts = {"Latn", "Latf"},
	ancestors = {"gmh"},
	sort_key = {
		from = {"[äàáâå]", "[ëèéê]", "[ïìíî]", "[öòóô]", "[üùúû]", "ß" },
		to   = {"a"	  , "e"	 , "i"	 , "o"	 , "u"	 , "ss"}} ,
	standardChars = "A-Za-z0-9ÄäÖöÜüß" .. PUNCTUATION,
}

m["dv"] = {
	"Dhivehi",
	"Q32656",
	"inc",
	otherNames = {"Divehi", "Mahal", "Mahl", "Maldivian"},
	scripts = {"Thaa"},
	ancestors = {"pmh"},	-- or Helu?
	translit_module = "dv-translit",
	override_translit = true,
}

m["dz"] = {
	"Dzongkha",
	"Q33081",
	"tbq",
	scripts = {"Tibt"},
	ancestors = {"xct"},
	translit_module = "bo-translit",
	override_translit = true,
}

m["ee"] = {
	"Ewe",
	"Q30005",
	"alv-von",
	scripts = Latn,
}

m["el"] = {
	"Greek",
	"Q9129",
	"grk",
	otherNames = {"Modern Greek", "Neo-Hellenic"},
	scripts = {"Grek", "Brai"},
	ancestors = {"grc"},
	translit_module = "el-translit",
	override_translit = true,
	sort_key = {  -- Keep this synchronized with grc, cpg, pnt
		from = {"[ᾳάᾴὰᾲᾶᾷἀᾀἄᾄἂᾂἆᾆἁᾁἅᾅἃᾃἇᾇ]", "[έὲἐἔἒἑἕἓ]", "[ῃήῄὴῂῆῇἠᾐἤᾔἢᾒἦᾖἡᾑἥᾕἣᾓἧᾗ]", "[ίὶῖἰἴἲἶἱἵἳἷϊΐῒῗ]", "[όὸὀὄὂὁὅὃ]", "[ύὺῦὐὔὒὖὑὕὓὗϋΰῢῧ]", "[ῳώῴὼῲῶῷὠᾠὤᾤὢᾢὦᾦὡᾡὥᾥὣᾣὧᾧ]", "ῥ", "ς"},
		to   = {"α"						, "ε"		 , "η"						, "ι"				, "ο"		 , "υ"				, "ω"						, "ρ", "σ"}} ,
	standardChars = "ͺ;΄-ώϜϝ" .. PUNCTUATION .. "ἀ-῾",
}

m["en"] = {
	"English",
	"Q1860",
	"gmw",
	otherNames = {"Modern English", "New English", "Hawaiian Creole English", "Hawai'ian Creole English", "Hawaiian Creole", "Hawai'ian Creole", "Polari", "Yinglish"}, -- all but the first three are names of subsumed dialects which once had codes
	scripts = {"Latn", "Brai", "Shaw", "Dsrt"}, -- entries in Shaw or Dsrt might require prior discussion
	ancestors = {"enm"},
	sort_key = {
		from = {"[äàáâåā]", "[ëèéêē]", "[ïìíîī]", "[öòóôō]", "[üùúûū]", "æ" , "œ" , "[çč]", "ñ", "'"},
		to   = {"a"       , "e"      , "i"      , "o"      , "u"      , "ae", "oe", "c"   , "n"}},
	wikimedia_codes = {"en", "simple"},
	standardChars = "A-Za-z0-9" .. PUNCTUATION .. u(0x2800) .. "-" .. u(0x28FF),
}

m["eo"] = {
	"Esperanto",
	"Q143",
	"art",
	scripts = Latn,
	sort_key = {
		from = {"[áà]", "[éè]", "[íì]", "[óò]", "[úù]", "[ĉ]", "[ĝ]", "[ĥ]", "[ĵ]", "[ŝ]", "[ŭ]"},
		to   = {"a"	   , "e"  , "i"  , "o"  , "u", "cĉ", "gĉ", "hĉ", "jĉ", "sĉ", "uĉ"}} ,
}

m["es"] = {
	"Spanish",
	"Q1321",
	"roa-ibe",
	otherNames = {"Castilian", "Amazonian Spanish", "Amazonic Spanish", "Loreto-Ucayali Spanish"},
	scripts = {"Latn", "Brai"},
	ancestors = {"osp"},
	sort_key = {
		from = {"á", "é", "í", "ó", "[úü]", "ç", "ñ"},
		to   = {"a", "e", "i", "o", "u"   , "c", "n"}},
	standardChars = "A-VXYZa-vxyz0-9ÁáÉéÍíÓóÚúÑñ¿¡" .. PUNCTUATION,
}

m["et"] = {
	"Estonian",
	"Q9072",
	"fiu-fin",
	scripts = Latn,
}

m["eu"] = {
	"Basque",
	"Q8752",
	"euq",
	otherNames = {"Euskara"},
	scripts = Latn,
}

m["fa"] = {
	"Persian",
	"Q9168",
	"ira-swi",
	otherNames = {"Farsi", "New Persian", "Modern Persian", "Western Persian", "Iranian Persian", "Eastern Persian", "Dari", "Aimaq", "Aimak", "Aymaq", "Eimak"},
	scripts = {"fa-Arab"},
	ancestors = {"pal"}, -- "ira-mid"
	entry_name = {
		from = {u(0x064E), u(0x064F), u(0x0650), u(0x0651), u(0x0652)},
		to   = {}} ,
}

m["ff"] = {
	"Fula",
	"Q33454",
	"alv-sng",
	otherNames = {"Adamawa Fulfulde", "Bagirmi Fulfulde", "Borgu Fulfulde", "Central-Eastern Niger Fulfulde", "Fulani", "Fulfulde", "Maasina Fulfulde", "Nigerian Fulfulde", "Pular", "Pulaar", "Western Niger Fulfulde"}, -- Maasina, etc are dialects, subsumed into this code
	scripts = {"Latn", "Adlm"},
}

m["fi"] = {
	"Finnish",
	"Q1412",
	"fiu-fin",
	otherNames = {"Suomi", "Botnian"},
	scripts = Latn,
	entry_name = {
		from = {"ˣ"},  -- Used to indicate gemination of the next consonant
		to   = {}},
	sort_key = {
		from = {"[áàâã]", "[éèêẽ]", "[íìîĩ]", "[óòôõ]", "[úùûũ]", "[ýỳŷüű]", "[øõő]", "æ" , "œ" , "[čç]", "š", "ž", "ß" , "[':]"},
		to   = {"a"	 , "e"	 , "i"	 , "o"	 , "u"	 ,  "y"	 , "ö"	, "ae", "oe", "c"   , "s", "z", "ss"}} ,
}

m["fj"] = {
	"Fijian",
	"Q33295",
	"poz-occ",
	scripts = Latn,
}

m["fo"] = {
	"Faroese",
	"Q25258",
	"gmq",
	scripts = Latn,
	ancestors = {"non"},
}

m["fr"] = {
	"French",
	"Q150",
	"roa-oil",
	otherNames = {"Modern French"},
	scripts = {"Latn", "Brai"},
	ancestors = {"frm"},
	sort_key = {
		from = {"[áàâä]", "[éèêë]", "[íìîï]", "[óòôö]", "[úùûü]", "[ýỳŷÿ]", "ç", "æ" , "œ" , "'"},
		to   = {"a"	 , "e"	 , "i"	 , "o"	 , "u"	 , "y"	 , "c", "ae", "oe"}},
	standardChars = "A-Za-z0-9ÀÂÇÉÈÊËÎÏÔŒÛÙÜàâçéèêëîïôœûùü«»" .. PUNCTUATION,
}

m["fy"] = {
	"West Frisian",
	"Q27175",
	"gmw-fri",
	otherNames = {"Western Frisian", "Frisian"},
	scripts = Latn,
	ancestors = {"ofs"},
	sort_key = {
		from = {"[àáâä]", "[èéêë]", "[ìíîïyỳýŷÿ]", "[òóôö]", "[ùúûü]", "æ", "[ /.-]"},
		to   = {"a"	 , "e"	, "i"	, "o"	, "u", "ae"}} ,
	standardChars = "A-PR-WYZa-pr-wyz0-9Ææâäàéêëèïìôöòúûüùỳ" .. PUNCTUATION,
}

m["ga"] = {
	"Irish",
	"Q9142",
	"cel-gae",
	otherNames = {"Irish Gaelic"},
	scripts = Latn,
	ancestors = {"mga"},
	sort_key = {
		from = {"á", "é", "í", "ó", "ú", "ý", "ḃ" , "ċ" , "ḋ" , "ḟ" , "ġ" , "ṁ" , "ṗ" , "ṡ" , "ṫ" },
		to   = {"a", "e", "i", "o", "u", "y", "bh", "ch", "dh", "fh", "gh", "mh", "ph", "sh", "th"}} ,
	standardChars = "A-IL-PR-Ua-il-pr-u0-9ÁáÉéÍíÓóÚú" .. PUNCTUATION,
}

m["gd"] = {
	"Scottish Gaelic",
	"Q9314",
	"cel-gae",
	otherNames = {"Gàidhlig", "Highland Gaelic", "Scots Gaelic", "Scottish"},
	scripts = Latn,
	ancestors = {"mga"},
	sort_key = {
		from = {"[áà]", "[éè]", "[íì]", "[óò]", "[úù]", "[ýỳ]"},
		to   = {"a"   , "e"   , "i"   , "o"   , "u"   , "y"   }} ,
	standardChars = "A-IL-PR-Ua-il-pr-u0-9ÀàÈèÌìÒòÙù" .. PUNCTUATION,
}

m["gl"] = {
	"Galician",
	"Q9307",
	"roa-ibe",
	scripts = Latn,
	ancestors = {"roa-opt"},
	sort_key = {
		from = {"á", "é", "í", "ó", "ú"},
		to   = {"a", "e", "i", "o", "u"}} ,
}

m["gn"] = {
	"Guaraní",
	"Q35876",
	"tup-gua",
	scripts = Latn,
}

m["gu"] = {
	"Gujarati",
	"Q5137",
	"inc",
	scripts = {"Gujr"},
	ancestors = {"inc-mgu"},
	translit_module = "gu-translit",
}

m["gv"] = {
	"Manx",
	"Q12175",
	"cel-gae",
	otherNames = {"Manx Gaelic"},
	scripts = Latn,
	ancestors = {"mga"},
	sort_key = {
		from = {"ç", "-"},
		to   = {"c"}} ,
	standardChars = "A-WYÇa-wyç0-9" .. PUNCTUATION,
}

m["ha"] = {
	"Hausa",
	"Q56475",
	"cdc-wst",
	scripts = LatnArab,
    sort_key = {
		from = {"ɓ",   "ɗ",   "ƙ",  "'y", "ƴ",  "'" },
		to   = {"b~" , "d~"	, "k~", "y~", "y~", ""  }},
    entry_name = {
		from = {"R̃", "r̃", "À", "à", "È", "è", "Ì", "ì", "Ò", "ò", "Ù", "ù", "Â", "â", "Ê", "ê", "Î", "î", "Ô", "ô", "Û", "û", "Ā", "ā", "Ē", "ē", "Ī", "ī", "Ō", "ō", "Ū", "ū", "Á", "á", "É", "é", "Í", "í", "Ó", "ó", "Ú", "ú", "Ā̀", "ā̀", "Ḕ", "ḕ", "Ī̀", "ī̀", "Ṑ", "ṑ", "Ū̀", "ū̀", GRAVE, ACUTE},
		to   = {"R", "r", "A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "A", "a", "E", "e", "I", "i", "O", "o", "U", "u", "A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}},
}

m["he"] = {
	"Hebrew",
	"Q9288",
	"sem-can",
	otherNames = {"Ivrit"},
	scripts = {"Hebr", "Phnx", "Brai"},
	entry_name = {
		from = {"[" .. u(0x0591) .. "-" .. u(0x05BD) .. u(0x05BF) .. "-" .. u(0x05C5) .. u(0x05C7) .. "]"},
		to   = {}} ,
}

m["hi"] = {
	"Hindi",
	"Q1568",
	"inc",
	otherNames = {"Hindavi", "Khariboli", "Khari Boli", "Manak Hindi"},
	scripts = {"Deva", "Kthi", "Newa"},
	ancestors = {"inc-ohi"},
	translit_module = "hi-translit",
}

m["ho"] = {
	"Hiri Motu",
	"Q33617",
	"crp",
	otherNames = {"Pidgin Motu", "Police Motu"},
	scripts = Latn,
	ancestors = {"meu"},
}

m["ht"] = {
	"Haitian Creole",
	"Q33491",
	"crp",
	otherNames = {"Creole", "Haitian", "Kreyòl"},
	scripts = Latn,
}

m["hu"] = {
	"Hungarian",
	"Q9067",
	"urj-ugr",
	otherNames = {"Magyar"},
	scripts = {"Latn", "Hung"},
	ancestors = {"ohu"},
	sort_key = {
		from = {"á", "é", "í", "ó", "ú", "ő", "ű"},
		to   = {"a", "e", "i", "o", "u", "ö", "ü"}} ,
}

m["hy"] = {
	"Armenian",
	"Q8785",
	"hyx",
	otherNames = {"Modern Armenian", "Eastern Armenian", "Western Armenian"},
	scripts = {"Armn", "Brai"},
	ancestors = {"axm"},
	translit_module = "Armn-translit",
	override_translit = true,
	sort_key = {
		from = {"ու", "և", "եւ"},
		to   = {"ւ", "եվ", "եվ"}},
	entry_name = {
		from = {"՞", "՜", "՛", "՟", "և", "<sup>յ</sup>", "<sup>ի</sup>"},
		to   = {"", "", "", "", "եւ", "յ", "ի"}} ,
}

m["hz"] = {
	"Herero",
	"Q33315",
	"bnt",
	scripts = Latn,
}

m["ia"] = {
	"Interlingua",
	"Q35934",
	"art",
	scripts = Latn,
}

m["id"] = {
	"Indonesian",
	"Q9240",
	"poz-mly",
	scripts = Latn,
	ancestors = {"ms"},
}

m["ie"] = {
	"Interlingue",
	"Q35850",
	"art",
	otherNames = {"Occidental"},
	scripts = Latn,
}

m["ig"] = {
	"Igbo",
	"Q33578",
	"nic-bco",
	scripts = Latn,
}

m["ii"] = {
	"Sichuan Yi",
	"Q34235",
	"tbq-lol",
	otherNames = {"Nuosu", "Nosu", "Northern Yi", "Liangshan Yi"},
	scripts = {"Yiii"},
	translit_module = "ii-translit",
}

m["ik"] = {
	"Inupiak",
	"Q27183",
	"esx-inu",
	otherNames = {"Inupiaq", "Iñupiaq", "Inupiatun"},
	scripts = Latn,
}

m["io"] = {
	"Ido",
	"Q35224",
	"art",
	scripts = Latn,
}

m["is"] = {
	"Icelandic",
	"Q294",
	"gmq",
	scripts = Latn,
	ancestors = {"non"},
}

m["it"] = {
	"Italian",
	"Q652",
	"roa-itd",
	scripts = Latn,
	sort_key = {
		from = {"[àáâäå]", "[èéêë]", "[ìíîï]", "[òóôö]", "[ùúûü]"},
		to   = {"a"	  , "e"	 , "i"	 , "o"	 , "u"	 }} ,
}

m["iu"] = {
	"Inuktitut",
	"Q29921",
	"esx-inu",
	otherNames = {"Eastern Canadian Inuktitut", "Eastern Canadian Inuit", "Western Canadian Inuktitut", "Western Canadian Inuit", "Western Canadian Inuktun", "Inuinnaq", "Inuinnaqtun", "Inuvialuk", "Inuvialuktun", "Nunavimmiutit", "Nunatsiavummiut", "Aivilimmiut", "Natsilingmiut", "Kivallirmiut", "Siglit", "Siglitun"},
	scripts = {"Cans", "Latn"},
	translit_module = "iu-translit",
	override_translit = true,
}

m["ja"] = {
	"Japanese",
	"Q5287",
	"jpx",
	otherNames = {"Modern Japanese", "Nipponese", "Nihongo"},
	scripts = {"Jpan", "Brai"},
	ancestors = {"ojp"},
	--[=[
	-- Handled by jsort function in [[Module:ja]].
	sort_key = {
		from = {"[ぁァア]", "[ぃィイ]", "[ぅゔゥウヴ]", "[ぇェエ]", "[ぉォオ]", "[がゕカガヵ]", "[ぎキギ]", "[ぐクグㇰ]", "[げゖケゲヶ]", "[ごコゴ]", "[ざサザ]", "[じシジㇱ]", "[ずスズㇲ]", "[ぜセゼ]", "[ぞソゾ]", "[だタダ]", "[ぢチヂ]", "[っづッツヅ]", "[でテデ]", "[どトドㇳ]", "ナ", "ニ", "[ヌㇴ]", "ネ", "ノ", "[ばぱハバパㇵ]", "[びぴヒビピㇶ]", "[ぶぷフブプㇷ]", "[べぺヘベペㇸ]", "[ぼぽホボポㇹ]", "マ", "ミ", "[ムㇺ]", "メ", "モ", "[ゃャヤ]", "[ゅュユ]", "[ょョヨ]", "[ラㇻ]", "[リㇼ]", "[ルㇽ]", "[レㇾ]", "[ロㇿ]", "[ゎヮワヷ]", "[ヰヸ]", "[ヱヹ]", "[ヲヺ]", "ン", "[゙゚゛゜ゝゞ・ヽヾ]", "𛀀"},
		to   = {"あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", "た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "ゐ", "ゑ", "を", "ん", "", "え"}},
	--]=]
}

m["jv"] = {
	"Javanese",
	"Q33549",
	"poz-sus",
	scripts = {"Latn", "Java"},
	translit_module = "jv-translit",
	ancestors = {"kaw"},
	link_tr = true,
}

m["ka"] = {
	"Georgian",
	"Q8108",
	"ccs-gzn",
	otherNames = {"Kartvelian", "Judeo-Georgian", "Kivruli", "Gruzinic"},
	scripts = {"Geor", "Geok", "Hebr"}, -- Hebr is used to write Judeo-Georgian
	ancestors = {"oge"},
	translit_module = "Geor-translit",
	override_translit = true,
	entry_name = {
		from = {"̂"},
		to   = {""}},
}

m["kg"] = {
	"Kongo",
	"Q33702",
	"bnt",
	otherNames = {"Kikongo", "Koongo", "Laari", "San Salvador Kongo", "Yombe"},
	scripts = Latn,
}

m["ki"] = {
	"Kikuyu",
	"Q33587",
	"bnt",
	otherNames = {"Gikuyu", "Gĩkũyũ"},
	scripts = Latn,
}

m["kj"] = {
	"Kwanyama",
	"Q1405077",
	"bnt",
	otherNames = {"Kuanyama", "Oshikwanyama"},
	scripts = Latn,
}

m["kk"] = {
	"Kazakh",
	"Q9252",
	"trk-kip",
	scripts = {"Cyrl", "Latn", "kk-Arab"},
	translit_module = "kk-translit",
	override_translit = true,
}

m["kl"] = {
	"Greenlandic",
	"Q25355",
	"esx-inu",
	otherNames = {"Kalaallisut"},
	scripts = Latn,
}

m["km"] = {
	"Khmer",
	"Q9205",
	"mkh",
	otherNames = {"Cambodian"},
	scripts = {"Khmr"},
	ancestors = {"mkh-mkm"},
	translit_module = "km-translit",
}

m["kn"] = {
	"Kannada",
	"Q33673",
	"dra",
	scripts = {"Knda"},
	ancestors = {"dra-mkn"},
	translit_module = "kn-translit",
}

m["ko"] = {
	"Korean",
	"Q9176",
	"qfa-kor",
	otherNames = {"Modern Korean"},
	scripts = {"Kore", "Brai"},
	ancestors = {"okm"},
	translit_module = "ko-translit",
}

m["kr"] = {
	"Kanuri",
	"Q36094",
	"ssa-sah",
	otherNames = {"Kanembu", "Bilma Kanuri", "Central Kanuri", "Manga Kanuri", "Tumari Kanuri"},
	scripts = LatnArab,
	sort_key = {
		from = {"ny", "ǝ", "sh"},
		to   = {"n~", "e~", "s~"}} , -- the sortkey and entry_name are only for standard Kanuri; when dialectal entries get added, someone will have to work out how the dialects should be represented orthographically
	entry_name = {
		from = {"À", "à", "È", "è", "Ǝ̀", "ǝ̀", "Ì", "ì", "Ò", "ò", "Ù", "ù", "Â", "â", "Ê", "ê", "Ǝ̂", "ǝ̂", "Î", "î", "Ô", "ô", "Û", "û", "Ă", "ă", "Ĕ", "ĕ", "Ǝ̆", "ǝ̆", "Ĭ", "ĭ", "Ŏ", "ŏ", "Ŭ", "ŭ", "Á", "á", "É", "é", "Ǝ́", "ǝ́", "Í", "í", "Ó", "ó", "Ú", "ú", GRAVE, ACUTE},
		to   = {"A", "a", "E", "e", "Ǝ", "ǝ", "I", "i", "O", "o", "U", "u", "A", "a", "E", "e", "Ǝ", "ǝ", "I", "i", "O", "o", "U", "u", "A", "a", "E", "e", "Ǝ", "ǝ", "I", "i", "O", "o", "U", "u", "A", "a", "E", "e", "Ǝ", "ǝ", "I", "i", "O", "o", "U", "u"}},
}

m["ks"] = {
	"Kashmiri",
	otherNames = {"Koshur"},
	"Q33552",
	"inc-dar",
	scripts = {"ks-Arab", "Deva", "Shrd", "Latn"},
	translit_module = "translit-redirect",
	ancestors = {"inc-dar-pro"},
}

m["ku"] = {
	"Kurdish",
	"Q36368",
	"ira-nwi",
	scripts = {"Latn", "ku-Arab", "Armn", "Cyrl"},
	translit_module = "translit-redirect",
}

-- "kv" IS TREATED AS "koi", "kpv", SEE WT:LT

m["kw"] = {
	"Cornish",
	"Q25289",
	"cel-bry",
	scripts = Latn,
	ancestors = {"cnx"},
}

m["ky"] = {
	"Kyrgyz",
	"Q9255",
	"trk-kip",
	otherNames = {"Kirghiz", "Kirgiz"},
	scripts = {"Cyrl", "Latn", "Arab"},
	translit_module = "ky-translit",
	override_translit = true,
}

m["la"] = {
	"Latin",
	"Q397",
	"itc",
	scripts = Latn,
	ancestors = {"itc-ola"},
	entry_name = {remove_diacritics = MACRON..BREVE..DIAER},
	standardChars = "A-Za-zÆæŒœĀ-ăĒ-ĕĪ-ĭŌ-ŏŪ-ŭȲȳ" .. MACRON .. BREVE .. PUNCTUATION,
}

m["lb"] = {
	"Luxembourgish",
	"Q9051",
	"gmw",
	scripts = Latn,
	ancestors = {"gmh"},
}

m["lg"] = {
	"Luganda",
	"Q33368",
	"bnt",
	otherNames = {"Ganda", "Oluganda"},
	scripts = Latn,
	entry_name = {
		from = {"á", "Á", "é", "É", "í", "Í", "ó", "Ó", "ú", "Ú", "ń", "Ń", "ḿ", "Ḿ", "â", "Â", "ê", "Ê", "î", "Î", "ô", "Ô", "û", "Û" },
		to   = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "n", "N", "m", "M", "a", "A", "e", "E", "i", "I", "o", "O", "u", "U",}},
	sort_key = {
		from = {"ŋ"},
		to   = {"n"}} ,
}

m["li"] = {
	"Limburgish",
	"Q102172",
	"gmw",
	otherNames = {"Limburgan", "Limburgian", "Limburgic"},
	scripts = Latn,
	ancestors = {"dum"},
}

m["ln"] = {
	"Lingala",
	"Q36217",
	"bnt",
	otherNames = {"Ngala"},
	scripts = Latn,
}

m["lo"] = {
	"Lao",
	"Q9211",
	"tai-swe",
	otherNames = {"Laotian"},
	scripts = {"Laoo"},
	translit_module = "lo-translit",
	sort_key = {
		from = {"%p", "[່-ໍ]", "ຼ", "ຽ", "ໜ", "ໝ", "([ເແໂໃໄ])([ກ-ຮ])"},
		to   = {"", "", "ລ", "ຍ", "ຫນ", "ຫມ", "%2%1"}},
}

m["lt"] = {
	"Lithuanian",
	"Q9083",
	"bat",
	scripts = Latn,
	ancestors = {"olt"},
	entry_name = {
		from = {"[áãà]", "[ÁÃÀ]", "[éẽè]", "[ÉẼÈ]", "[íĩì]", "[ÍĨÌ]", "[ýỹ]", "[ÝỸ]", "ñ", "[óõò]", "[ÓÕÒ]", "[úũù]", "[ÚŨÙ]", ACUTE, GRAVE, TILDE},
		to   = {"a",       "A",     "e",     "E",     "i",     "I",     "y",   "Y",   "n",   "o",    "O",     "u",      "U"}} ,
}

m["lu"] = {
	"Luba-Katanga",
	"Q36157",
	"bnt",
	scripts = Latn,
}

m["lv"] = {
	"Latvian",
	"Q9078",
	"bat",
	otherNames = {"Lettish", "Lett"},
	scripts = Latn,
	entry_name = {
		-- This attempts to convert vowels with tone marks to vowels either with
		-- or without macrons. Specifically, there should be no macrons if the
		-- vowel is part of a diphthong (including resonant diphthongs such
		-- pìrksts -> pirksts not #pīrksts). What we do is first convert the
		-- vowel + tone mark to a vowel + tilde in a decomposed fashion,
		-- then remove the tilde in diphthongs, then convert the remaining
		-- vowel + tilde sequences to macroned vowels, then delete any other
		-- tilde. We leave already-macroned vowels alone: Both e.g. ar and ār
		-- occur before consonants. FIXME: This still might not be sufficient.
		from = {"Ȩ", "ȩ", "[ÂÃÀ]", "[âãà]", "[ÊẼÈ]", "[êẽè]", "[ÎĨÌ]", "[îĩì]", "[ÔÕÒ]", "[ôõò]", "[ÛŨÙ]", "[ûũù]", "[ÑǸ]", "[ñǹ]", "[" .. CIRC .. TILDE ..GRAVE .."]", "([aAeEiIoOuU])" .. TILDE .."?([lrnmuiLRNMUI])" .. TILDE .. "?([^aAeEiIoOuUāĀēĒīĪūŪ])", "([aAeEiIoOuU])" .. TILDE .."?([lrnmuiLRNMUI])" .. TILDE .."?$", "([iI])" .. TILDE .. "?([eE])" .. TILDE .. "?", "A" .. TILDE, "a" .. TILDE, "E" .. TILDE, "e" .. TILDE, "I" .. TILDE, "i" .. TILDE, "U" .. TILDE, "u" .. TILDE, TILDE},
		to   = {"E", "e", "A" .. TILDE, "a" .. TILDE, "E" .. TILDE, "e" .. TILDE, "I" .. TILDE, "i" .. TILDE, "O", "o", "U" .. TILDE, "u" .. TILDE, "N", "n", TILDE, "%1%2%3", "%1%2", "%1%2", "Ā", "ā", "Ē", "ē", "Ī", "ī", "Ū", "ū", ""}},
}

m["mg"] = {
	"Malagasy",
	"Q7930",
	"poz-bre",
	otherNames = {"Betsimisaraka Malagasy", "Betsimisaraka", "Northern Betsimisaraka Malagasy", "Northern Betsimisaraka", "Southern Betsimisaraka Malagasy", "Southern Betsimisaraka", "Bara Malagasy", "Bara", "Masikoro Malagasy", "Masikoro", "Antankarana", "Antankarana Malagasy", "Plateau Malagasy", "Sakalava", "Tandroy Malagasy", "Tandroy", "Tanosy", "Tanosy Malagasy", "Tesaka", "Tsimihety", "Tsimihety Malagasy", "Bushi", "Shibushi", "Kibushi"},
	scripts = Latn,
}

m["mh"] = {
	"Marshallese",
	"Q36280",
	"poz-mic",
	scripts = Latn,
	sort_key = {
		from = {"ā" , "ļ" , "m̧" , "ņ" , "n̄"  , "o̧" , "ō"  , "ū" },
		to   = {"a~", "l~", "m~", "n~", "n~~", "o~", "o~~", "u~"}} ,
}

m["mi"] = {
	"Maori",
	"Q36451",
	"poz-pep",
	otherNames = {"Māori"},
	scripts = Latn,
}

m["mk"] = {
	"Macedonian",
	"Q9296",
	"zls",
	scripts = Cyrl,
	translit_module = "mk-translit",
	entry_name = {
		from = {ACUTE},
		to   = {}},
}

m["ml"] = {
	"Malayalam",
	"Q36236",
	"dra",
	scripts = {"Mlym"},
	translit_module = "ml-translit",
	override_translit = true,
}

m["mn"] = {
	"Mongolian",
	"Q9246",
	"xgn",
	otherNames = {"Khalkha Mongolian"},
	scripts = {"Cyrl", "Mong", "Soyo", "Zanb"}, -- entries in Soyo or Zanb might require prior discussion
	ancestors = {"cmg"},
	translit_module = "mn-translit",
	override_translit = true,
}

-- "mo" IS TREATED AS "ro", SEE WT:LT

m["mr"] = {
	"Marathi",
	"Q1571",
	"inc",
	scripts = {"Deva", "Modi"},
	ancestors = {"omr"},
	translit_module = "mr-translit",
}

m["ms"] = {
	"Malay",
	"Q9237",
	"poz-mly",
	otherNames = {"Malaysian", "Standard Malay"},
	scripts = {"Latn", "ms-Arab"},
}

m["mt"] = {
	"Maltese",
	"Q9166",
	"sem-arb",
	scripts = Latn,
	ancestors = {"sqr"},
}

m["my"] = {
	"Burmese",
	"Q9228",
	"tbq-brm",
	otherNames = {"Myanmar"},
	scripts = {"Mymr"},
	ancestors = {"obr"},
	translit_module = "my-translit",
	override_translit = true,
}

m["na"] = {
	"Nauruan",
	"Q13307",
	"poz-mic",
	otherNames = {"Nauru"},
	scripts = Latn,
}

m["nb"] = {
	"Norwegian Bokmål",
	"Q25167",
	"gmq",
	otherNames = {"Bokmål"},
	scripts = Latn,
	ancestors = {"gmq-mno"},
	wikimedia_codes = {"no"},
}

m["nd"] = {
	"Northern Ndebele",
	"Q35613",
	"bnt-ngu",
	otherNames = {"North Ndebele"},
	scripts = Latn,
	entry_name = {
		from = {"[āàáâǎ]", "[ēèéêě]", "[īìíîǐ]", "[ōòóôǒ]", "[ūùúûǔ]", "ḿ", "[ǹńň]", MACRON, ACUTE, GRAVE, CIRC, CARON},
		to   = {"a"      , "e"      , "i"      , "o"      , "u"      , "m", "n"    }},
}

m["ne"] = {
	"Nepali",
	"Q33823",
	"inc-pah",
	otherNames = {"Nepalese"},
	scripts = {"Deva", "Newa"},
	translit_module = "ne-translit",
	ancestors = {"psu"},
}

m["ng"] = {
	"Ndonga",
	"Q33900",
	"bnt",
	scripts = Latn,
}

m["nl"] = {
	"Dutch",
	"Q7411",
	"gmw",
	otherNames = {"Netherlandic", "Flemish"},
	scripts = Latn,
	ancestors = {"dum"},
	sort_key = {
		from = {"[äáâå]", "[ëéê]", "[ïíî]", "[öóô]", "[üúû]", "ç", "ñ", "^-"},
		to   = {"a"	 , "e"	, "i"	, "o"	, "u"	, "c", "n"}} ,
	standardChars = "A-Za-z0-9" .. PUNCTUATION .. u(0x2800) .. "-" .. u(0x28FF),
}

m["nn"] = {
	"Norwegian Nynorsk",
	"Q25164",
	"gmq",
	otherNames = {"New Norwegian", "Nynorsk"},
	scripts = Latn,
	ancestors = {"gmq-mno"},
}

m["no"] = {
	"Norwegian",
	"Q9043",
	"gmq",
	scripts = Latn,
	ancestors = {"gmq-mno"},
}

m["nr"] = {
	"Southern Ndebele",
	"Q36785",
	"bnt-ngu",
	otherNames = {"South Ndebele"},
	scripts = Latn,
	entry_name = {
		from = {"[āàáâǎ]", "[ēèéêě]", "[īìíîǐ]", "[ōòóôǒ]", "[ūùúûǔ]", "ḿ", "[ǹńň]", MACRON, ACUTE, GRAVE, CIRC, CARON},
		to   = {"a"      , "e"      , "i"      , "o"      , "u"      , "m", "n"    }},
}

m["nv"] = {
	"Navajo",
	"Q13310",
	"apa",
	otherNames = {"Navaho", "Diné bizaad"},
	scripts = {"nv-Latn"},
	sort_key = {
		from = {"[áą]", "[éę]", "[íį]", "[óǫ]", "ń", "^n([djlt])", "ł" , "[ʼ’']", ACUTE},
		to   = {"a"   , "e"   , "i"   , "o"   , "n", "ni%1"	  , "l~"}}, -- the tilde is used to guarantee that ł will always be sorted after all other words with l
}

m["ny"] = {
	"Chichewa",
	"Q33273",
	"bnt",
	otherNames = {"Chicheŵa", "Chinyanja", "Nyanja", "Chewa", "Cicewa", "Cewa", "Cinyanja"},
	scripts = Latn,
	entry_name = {
		from = {"ŵ", "Ŵ", "á", "Á", "é", "É", "í", "Í", "ó", "Ó", "ú", "Ú", "ń", "Ń", "ḿ", "Ḿ" },
		to   = {"w", "W", "a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "n", "N", "m", "M"}},
	sort_key = {
		from = {"ng'"},
		to   = {"ng"}} ,
}

m["oc"] = {
	"Occitan",
	"Q14185",
	"roa",
	otherNames = {"Provençal", "Auvergnat", "Auvernhat", "Gascon", "Languedocien", "Lengadocian", "Shuadit", "Chouhadite", "Chouhadit", "Chouadite", "Chouadit", "Shuhadit", "Judeo-Provençal", "Judeo-Provencal", "Judeo-Comtadin"},
	scripts = {"Latn", "Hebr"},
	ancestors = {"pro"},
	sort_key = {
		from = {"[àá]", "[èé]", "[íï]", "[òó]", "[úü]", "ç", "([lns])·h"},
		to   = {"a"   , "e"   , "i"   , "o"   , "u"   , "c", "%1h"	  }} ,
}

m["oj"] = {
	"Ojibwe",
	"Q33875",
	"alg",
	otherNames = {"Chippewa", "Ojibway", "Ojibwemowin", "Southwestern Ojibwa"},
	scripts = {"Cans", "Latn"},
}

m["om"] = {
	"Oromo",
	"Q33864",
	"cus",
	otherNames = {"Orma", "Borana-Arsi-Guji Oromo", "West Central Oromo"},
	scripts = {"Latn", "Ethi"},
}

m["or"] = {
	"Oriya",
	"Q33810",
	"inc",
	otherNames = {"Odia", "Oorya"},
	scripts = {"Orya"},
	ancestors = {"inc-mor"},
	translit_module = "or-translit",
}

m["os"] = {
	"Ossetian",
	"Q33968",
	"xsc",
	otherNames = {"Ossete", "Ossetic", "Digor", "Iron"},
	scripts = {"Cyrl", "Geor", "Latn"},
	ancestors = {"oos"},
	translit_module = "os-translit",
	override_translit = true,
	entry_name = {
		from = {GRAVE, ACUTE},
		to   = {}} ,
}

m["pa"] = {
	"Punjabi",
	"Q58635",
	"inc",
	otherNames = {"Panjabi"},
	scripts = {"Guru", "pa-Arab", "Deva"},
	ancestors = {"psu"},
	translit_module = "translit-redirect",
	entry_name = {
		from = {u(0x064B), u(0x064C), u(0x064D), u(0x064E), u(0x064F), u(0x0650), u(0x0651), u(0x0652)},
		to   = {}} ,
}

m["pi"] = {
	"Pali",
	"Q36727",
	"inc-old",
	scripts = {"Latn", "Brah", "Deva", "Beng", "Sinh", "Mymr", "Thai", "Lana", "Laoo", "Khmr"},
	ancestors = {"sa"},
	sort_key = {
		from = {"ā", "ī", "ū", "ḍ", "ḷ", "[ṁṃ]", "[ṇñṅ]", "ṭ", "([เโ])([ก-ฮ])", "([ເໂ])([ກ-ຮ])", "ᩔ", "ᩕ", "ᩖ", "ᩘ", "([ᨭ-ᨱ])ᩛ", "([ᨷ-ᨾ])ᩛ", "ᩤ", u(0xFE00), u(0x200D)},
		to   = {"a", "i", "u", "d", "l", "m"   , "n"	, "t", "%2%1", "%2%1", "ᩈ᩠ᩈ", "᩠ᩁ", "᩠ᩃ", "ᨦ᩠", "%1᩠ᨮ", "%1᩠ᨻ", "ᩣ"}} ,
	entry_name = {
		from = {u(0xFE00)},
		to   = {}},
}

m["pl"] = {
	"Polish",
	"Q809",
	"zlw-lch",
	scripts = Latn,
	ancestors = {"zlw-opl"},
	sort_key = {
		from = {"[Ąą]", "[Ćć]", "[Ęę]", "[Łł]", "[Ńń]", "[Óó]", "[Śś]", "[Żż]", "[Źź]"},
		to   = {
			"a" .. u(0x10FFFF),
			"c" .. u(0x10FFFF),
			"e" .. u(0x10FFFF),
			"l" .. u(0x10FFFF),
			"n" .. u(0x10FFFF),
			"o" .. u(0x10FFFF),
			"s" .. u(0x10FFFF),
			"z" .. u(0x10FFFF),
			"z" .. u(0x10FFFE)}} ,
}

m["ps"] = {
	"Pashto",
	"Q58680",
	"ira-pat",
	otherNames = {"Pashtun", "Pushto", "Pashtu", "Central Pashto", "Northern Pashto", "Southern Pashto", "Pukhto", "Pakhto", "Pakkhto", "Afghani"},
	scripts = {"ps-Arab"},
	ancestors = {"ira-pat-pro"},
}

m["pt"] = {
	"Portuguese",
	"Q5146",
	"roa-ibe",
	otherNames = {"Modern Portuguese"},
	scripts = {"Latn", "Brai"},
	ancestors = {"roa-opt"},
	sort_key = {
		from = {"[àãáâä]", "[èẽéêë]", "[ìĩíï]", "[òóôõö]", "[üúùũ]", "ç", "ñ"},
		to   = {"a"	  , "e"	  , "i"	 , "o"	  , "u"	 , "c", "n"}} ,
}

m["qu"] = {
	"Quechua",
	"Q5218",
	"qwe",
	scripts = Latn,
}

m["rm"] = {
	"Romansch",
	"Q13199",
	"roa-rhe",
	otherNames = {"Romansh", "Rumantsch", "Romanche"},
	scripts = Latn,
}

m["ro"] = {
	"Romanian",
	"Q7913",
	"roa-eas",
	otherNames = {"Daco-Romanian", "Roumanian", "Rumanian"},
	scripts = {"Latn", "Cyrl"},
	sort_key = {
        from = {"ă" , "â"  , "î" , "ș" , "ț" },
        to   = {"a~", "a~~", "i~", "s~", "t~"}},
}

m["ru"] = {
	"Russian",
	"Q7737",
	"zle",
	scripts = {"Cyrl", "Brai"},
	translit_module = "ru-translit",
	sort_key = {
		from = {"ё"},
		to   = {"е" .. mw.ustring.char(0x10FFFF)}},
	entry_name = {
		from = {"Ѐ", "ѐ", "Ѝ", "ѝ", GRAVE, ACUTE},
		to   = {"Е", "е", "И", "и"}},
	standardChars = "ЁІА-яёі0-9—" .. PUNCTUATION,
}

m["rw"] = {
	"Rwanda-Rundi",
	"Q33573",
	"bnt",
	otherNames = {"Rwanda", "Kinyarwanda", "Rundi", "Kirundi", "Ha", "Giha", "Hangaza", "Vinza", "Shubi", "Subi"},
	scripts = Latn,
}

m["sa"] = {
	"Sanskrit",
	"Q11059",
	"inc-old",
	scripts = {"Deva", "Bali", "as-Beng", "Beng", "Bhks", "Brah", "Gran", "Gujr", "Guru", "Java", "Khar", "Khmr", "Knda", "Lana", "Laoo", "Mlym", "Mymr", "Newa", "Orya", "Saur", "Shrd", "Sidd", "Sinh", "Taml", "Telu", "Thai", "Tibt", "Tirh"},
	sort_key = {
		from = {"ā", "ī", "ū", "ḍ", "ḷ", "[ṁṃ]", "[ṇñṅ]", "ṭ", "([เโไ])([ก-ฮ])", "([ເໂໄ])([ກ-ຮ])", "ᩔ", "ᩕ", "ᩖ", "ᩘ", "([ᨭ-ᨱ])ᩛ", "([ᨷ-ᨾ])ᩛ", "ᩤ", u(0xFE00), u(0x200D)},
		to   = {"a", "i", "u", "d", "l", "m"   , "n"	, "t", "%2%1", "%2%1", "ᩈ᩠ᩈ", "᩠ᩁ", "᩠ᩃ", "ᨦ᩠", "%1᩠ᨮ", "%1᩠ᨻ", "ᩣ"}} ,
	entry_name = {
		from = {u(0xFE00)},
		to   = {}},
	translit_module = "translit-redirect",
}

m["sc"] = {
	"Sardinian",
	"Q33976",
	"roa",
	otherNames = {"Campidanese", "Campidanese Sardinian", "Logudorese", "Logudorese Sardinian", "Nuorese", "Nuorese Sardinian"},
	scripts = Latn,
}

m["sd"] = {
	"Sindhi",
	"Q33997",
	"inc",
	scripts = {"sd-Arab", "Deva", "Sind", "Khoj"},
	entry_name = {
		from = {u(0x0671), u(0x064B), u(0x064C), u(0x064D), u(0x064E), u(0x064F), u(0x0650), u(0x0651), u(0x0652), u(0x0670), u(0x0640)},
		to   = {u(0x0627)}},
	ancestors = {"psu"},
}

m["se"] = {
	"Northern Sami",
	"Q33947",
	"smi",
	otherNames = {"North Sami", "Northern Saami", "North Saami"},
	scripts = Latn,
	entry_name = {
		from = {"ạ", "[ēẹ]", "ī", "[ōọ]", "ū", "ˈ"},
		to   = {"a", "e"   , "i", "o"   , "u"} },
	sort_key = {
		from = {"á" , "č" , "đ" , "ŋ" , "š" , "ŧ" , "ž" },
		to   = {"a²", "c²", "d²", "n²", "s²", "t²", "z²"} },
	standardChars = "A-PR-VZa-pr-vz0-9ÁáČčĐđŊŋŠšŦŧŽž" .. PUNCTUATION,
}

m["sg"] = {
	"Sango",
	"Q33954",
	"crp",
	scripts = Latn,
}

m["sh"] = {
	"Serbo-Croatian",
	"Q9301",
	"zls",
	otherNames = {"BCS", "Croato-Serbian", "Serbocroatian", "Bosnian", "Croatian", "Montenegrin", "Serbian"},
	scripts = {"Latn", "Cyrl"},
	entry_name = {
		from = {"[ȀÀȂÁĀÃ]", "[ȁàȃáāã]", "[ȄÈȆÉĒẼ]", "[ȅèȇéēẽ]", "[ȈÌȊÍĪĨ]", "[ȉìȋíīĩ]", "[ȌÒȎÓŌÕ]", "[ȍòȏóōõ]", "[ȐȒŔ]", "[ȑȓŕ]", "[ȔÙȖÚŪŨ]", "[ȕùȗúūũ]", "Ѐ", "ѐ", "[ӢЍ]", "[ӣѝ]", "[Ӯ]", "[ӯ]", GRAVE, ACUTE, DGRAVE, INVBREVE, MACRON, TILDE},
		to   = {"A"	  , "a"	  , "E"	  , "e"	  , "I"	  , "i"	  , "O"	  , "o"	  , "R"	, "r"	, "U"	  , "u"	  , "Е", "е", "И"   , "и", "У", "у"   }},
	wikimedia_codes = {"sh", "bs", "hr", "sr"},
}

m["si"] = {
	"Sinhalese",
	"Q13267",
	"inc",
	otherNames = {"Singhalese", "Sinhala"},
	scripts = {"Sinh"},
	ancestors = {"elu-prk"},
	translit_module = "si-translit",
	override_translit = true,
}

m["sk"] = {
	"Slovak",
	"Q9058",
	"zlw",
	scripts = Latn,
	sort_key = {
		from = {"[áä]", "é", "í", "[óô]", "ú", "ý", "ŕ", "ĺ", "[" .. DIAER .. ACUTE .. CIRC .. "]"},
		to   = {"a"   , "e", "i", "o"   , "u", "y", "r", "l", ""}} ,
}

m["sl"] = {
	"Slovene",
	"Q9063",
	"zls",
	otherNames = {"Slovenian"},
	scripts = Latn,
	entry_name = {
		from = {"[ÁÀÂȂȀ]", "[áàâȃȁ]", "[ÉÈÊȆȄỆẸ]", "[éèêȇȅệẹə]", "[ÍÌÎȊȈ]", "[íìîȋȉ]", "[ÓÒÔȎȌỘỌ]", "[óòôȏȍộọ]", "[ŔȒȐ]", "[ŕȓȑ]", "[ÚÙÛȖȔ]", "[úùûȗȕ]", "ł", GRAVE, ACUTE, DGRAVE, INVBREVE, CIRC, DOTBELOW},
		to   = {"A"	  , "a"	  , "E"		, "e"		 , "I"	  , "i"	  , "O"		, "o"		, "R"	, "r"	, "U"	  , "u"	  , "l"}} ,
}

m["sm"] = {
	"Samoan",
	"Q34011",
	"poz-pnp",
	scripts = Latn,
}

m["sn"] = {
	"Shona",
	"Q34004",
	"bnt",
	scripts = Latn,
	entry_name = {
        from = {ACUTE},
        to = {}} ,
}

m["so"] = {
	"Somali",
	"Q13275",
	"cus",
	scripts = {"Latn", "Arab", "Osma"},
	entry_name = {
		from = {"[ÁÀÂ]", "[áàâ]", "[ÉÈÊ]", "[éèê]", "[ÍÌÎ]", "[íìî]", "[ÓÒÔ]", "[óòô]", "[ÚÙÛ]", "[úùû]", "[ÝỲ]", "[ýỳ]"},
		to   = {"A"	  , "a"	  , "E"	, "e" , "I"	  , "i"	  , "O"	, "o"	, "U"  , "u", "Y", "y"}} ,
}

m["sq"] = {
	"Albanian",
	"Q8748",
	"sqj",
	otherNames = {"Tosk", "Gheg", "Arvanitika", "Arbëreshë", "Arbëresh"},
	scripts = {"Latn", "Grek", "Elba"},
	sort_key = {
		from = { '[âãä]', '[ÂÃÄ]', '[êẽë]', '[ÊẼË]', 'ĩ', 'Ĩ', 'õ', 'Õ', 'ũ', 'Ũ', 'ỹ', 'Ỹ', 'ç', 'Ç' },
		to   = {     'a',     'A',     'e',     'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y', 'c', 'C' } } ,
}

m["ss"] = {
	"Swazi",
	"Q34014",
	"bnt-ngu",
	otherNames = {"Swati"},
	scripts = Latn,
	entry_name = {
		from = {"[āàáâǎ]", "[ēèéêě]", "[īìíîǐ]", "[ōòóôǒ]", "[ūùúûǔ]", "ḿ", "[ǹńň]", MACRON, ACUTE, GRAVE, CIRC, CARON},
		to   = {"a"      , "e"      , "i"      , "o"      , "u"      , "m", "n"    }},
}

m["st"] = {
	"Sotho",
	"Q34340",
	"bnt-sts",
	otherNames = {"Sesotho", "Southern Sesotho", "Southern Sotho"},
	scripts = Latn,
	entry_name = {
		from = {"[āàáâǎ]", "[ēèéêě]", "[īìíîǐ]", "[ōòóôǒ]", "[ūùúûǔ]", "ḿ", "[ǹńň]", MACRON, ACUTE, GRAVE, CIRC, CARON},
		to   = {"a"      , "e"      , "i"      , "o"      , "u"      , "m", "n"    }},
}

m["su"] = {
	"Sundanese",
	"Q34002",
	"poz-msa",
	scripts = {"Latn", "Sund"},
	translit_module = "su-translit",
}

m["sv"] = {
	"Swedish",
	"Q9027",
	"gmq",
	scripts = Latn,
	ancestors = {"gmq-osw"},
}

m["sw"] = {
	"Swahili",
	"Q7838",
	"bnt",
	otherNames = {"Settler Swahili", "KiSetla", "KiSettla", "Setla", "Settla", "Kitchen Swahili", "Kihindi", "Indian Swahili", "KiShamba", "Kishamba", "Field Swahili", "Kibabu", "Asian Swahili", "Kimanga", "Arab Swahili", "Kitvita", "Army Swahili"},
	scripts = LatnArab,
	sort_key = {
		from = {"ng'", "^-"},
		to   = {"ngz"}} ,
}

m["ta"] = {
	"Tamil",
	"Q5885",
	"dra",
	scripts = {"Taml"},
	ancestors = {"oty"},
	translit_module = "ta-translit",
	override_translit = true,
}

m["te"] = {
	"Telugu",
	"Q8097",
	"dra",
	scripts = {"Telu"},
	translit_module = "te-translit",
	override_translit = true,
}

m["tg"] = {
	"Tajik",
	"Q9260",
	"ira-swi",
	otherNames = {"Tadjik", "Tadzhik", "Tajiki", "Tajik Persian", "Tajiki Persian"},
	scripts = {"Cyrl", "fa-Arab", "Latn"},
	ancestors = {"pal"}, -- same as "fa", see WT:T:AFA
	translit_module = "tg-translit",
	override_translit = true,
	sort_key = {
		from = {"Ё", "ё"},
		to   = {"Е" , "е"}} ,
	entry_name = {
		from = {ACUTE},
		to   = {}} ,
}

m["th"] = {
	"Thai",
	"Q9217",
	"tai-swe",
	otherNames = {"Siamese", "Central Thai"},
	scripts = {"Thai", "Brai"},
	translit_module = "th-translit",
	sort_key = {
		from = {"%p", "[็-๎]", "([เแโใไ])([ก-ฮ])"},
		to   = {"", "", "%2%1"}},
}

m["ti"] = {
	"Tigrinya",
	"Q34124",
	"sem-eth",
	otherNames = {"Tigrigna"},
	scripts = {"Ethi"},
	translit_module = "Ethi-translit",
}

m["tk"] = {
	"Turkmen",
	"Q9267",
	"trk-ogz",
	scripts = {"Latn", "Cyrl"},
	entry_name = {
		from = {"ā", "ē", "ī", "ō", "ū", "ȳ", "ȫ", "ǖ", MACRON},
		to   = {"a", "e", "i", "o", "u", "y", "ö", "ü", ""}},
	ancestors = {"trk-ogz-pro"},
}

m["tl"] = {
	"Tagalog",
	"Q34057",
	"phi",
	scripts = {"Latn", "Tglg"},
	entry_name = {
		from = {"[áàâ]", "[éèê]", "[íìî]", "[óòô]", "[úùû]", ACUTE, GRAVE, CIRC},
		to   = {"a"    , "e"    , "i"    , "o"    , "u"    }},
}

m["tn"] = {
	"Tswana",
	"Q34137",
	"bnt-sts",
	otherNames = {"Setswana"},
	scripts = Latn,
}

m["to"] = {
	"Tongan",
	"Q34094",
	"poz-pol",
	scripts = Latn,
	sort_key = {
		from = {"ā", "ē", "ī", "ō", "ū", MACRON},
		to   = {"a", "e", "i", "o", "u", ""}},
	entry_name = {
		from = {"á", "é", "í", "ó", "ú", ACUTE},
		to   = {"a", "e", "i", "o", "u", ""}},
}

m["tr"] = {
	"Turkish",
	"Q256",
	"trk-ogz",
	scripts = Latn,
	ancestors = {"ota"},
}

m["ts"] = {
	"Tsonga",
	"Q34327",
	"bnt",
	scripts = Latn,
}

m["tt"] = {
	"Tatar",
	"Q25285",
	"trk-kip",
	scripts = {"Cyrl", "Latn", "tt-Arab"},
	translit_module = "tt-translit",
	override_translit = true,
}

-- "tw" IS TREATED AS "ak", SEE WT:LT

m["ty"] = {
	"Tahitian",
	"Q34128",
	"poz-pep",
	scripts = Latn,
}

m["ug"] = {
	"Uyghur",
	"Q13263",
	"trk",
	otherNames = {"Uigur", "Uighur", "Uygur"},
	scripts = {"ug-Arab", "Latn", "Cyrl"},
	ancestors = {"chg"},
	translit_module = "ug-translit",
	override_translit = true,
}

m["uk"] = {
	"Ukrainian",
	"Q8798",
	"zle",
	scripts = Cyrl,
	ancestors = {"orv"},
	translit_module = "uk-translit",
	entry_name = {
		from = {"Ѐ", "ѐ", "Ѝ", "ѝ", GRAVE, ACUTE},
		to   = {"Е", "е", "И", "и"}},
	standardChars = "ЄІЇА-ЩЫЬЮ-щыьюяєії" .. PUNCTUATION,
} 
m["ur"] = {
	"Urdu",
	"Q1617",
	"inc",
	scripts = {"ur-Arab"},
	ancestors = {"inc-sap"},
	entry_name = {
		from = {u(0x064B), u(0x064C), u(0x064D), u(0x064E), u(0x064F), u(0x0650), u(0x0651), u(0x0652)},
		to   = {}} ,
}

m["uz"] = {
	"Uzbek",
	"Q9264",
	"trk",
	otherNames = {"Northern Uzbek", "Southern Uzbek"},
	scripts = {"Latn", "Cyrl", "fa-Arab"},
	ancestors = {"chg"},
}

m["ve"] = {
	"Venda",
	"Q32704",
	"bnt",
	scripts = Latn,
}

m["vi"] = {
	"Vietnamese",
	"Q9199",
	"mkh-vie",
	otherNames = {"Annamese", "Annamite"},
	scripts = {"Latn", "Hani"},
	ancestors = {"mkh-mvi"},
	sort_key = "vi-sortkey",
}

m["vo"] = {
	"Volapük",
	"Q36986",
	"art",
	scripts = Latn,
}

m["wa"] = {
	"Walloon",
	"Q34219",
	"roa-oil",
	otherNames = {"Liégeois", "Namurois", "Wallo-Picard", "Wallo-Lorrain"},
	scripts = Latn,
	ancestors = {"fro"},
	sort_key = {
		from = {"[áàâäå]", "[éèêë]", "[íìîï]", "[óòôö]", "[úùûü]", "[ýỳŷÿ]", "ç", "'"},
		to   = {"a"	  , "e"	 , "i"	 , "o"	 , "u"	 , "y"	 , "c"}} ,
}

m["wo"] = {
	"Wolof",
	"Q34257",
	"alv-sng",
	otherNames = {"Gambian Wolof"}, -- the subsumed dialect 'wof'
	scripts = LatnArab,
}

m["xh"] = {
	"Xhosa",
	"Q13218",
	"bnt-ngu",
	scripts = Latn,
	entry_name = {
		from = {"[āàáâǎ]", "[ēèéêě]", "[īìíîǐ]", "[ōòóôǒ]", "[ūùúûǔ]", "ḿ", "[ǹńň]", MACRON, ACUTE, GRAVE, CIRC, CARON},
		to   = {"a"      , "e"      , "i"      , "o"      , "u"      , "m", "n"    }},
}

m["yi"] = {
	"Yiddish",
	"Q8641",
	"gmw",
	scripts = {"Hebr"},
	ancestors = {"gmh"},
	sort_key = {
		from = {"[אַאָ]", "בּ", "[וֹוּ]", "יִ", "ײַ", "פֿ"},
		to = {"א", "ב", "ו", "י",	"יי", "פ"}} ,
	translit_module = "yi-translit",
}

m["yo"] = {
	"Yoruba",
	"Q34311",
	"alv-von",
	scripts = Latn,
}

m["za"] = {
	"Zhuang",
	"Q13216",
	"tai",
	otherNames = {"Standard Zhuang", "Dai Zhuang", "Wenma Zhuang", "Wenma Thu", "Wenma", "Nong Zhuang", "Youjiang Zhuang", "Yongbei Zhuang", "Yang Zhuang", "Yongnan Zhuang", "Zuojiang Zhuang", "Central Hongshuihe Zhuang", "Eastern Hongshuihe Zhuang", "Guibei Zhuang", "Minz Zhuang", "Guibian Zhuang", "Liujiang Zhuang", "Lianshan Zhuang", "Liuqian Zhuang", "Qiubei Zhuang", "Chongzuo Zhuang", "Shangsi Zhuang"},
	scripts = {"Latn", "Hani"},
}

m["zh"] = {
	"Chinese",
	"Q7850",
	"zhx",
	scripts = {"Hani", "Brai", "Nshu"},
	ancestors = {"ltc"},
	sort_key = "zh-sortkey",
}

m["zu"] = {
	"Zulu",
	"Q10179",
	"bnt-ngu",
	otherNames = {"isiZulu"},
	scripts = Latn,
	entry_name = {
                from = {"[āàáâǎ]", "[ēèéêě]", "[īìíîǐ]", "[ōòóôǒ]", "[ūùúûǔ]", "ḿ", "[ǹńň]", MACRON, ACUTE, GRAVE, CIRC, CARON},
                to   = {"a"      , "e"      , "i"      , "o"      , "u"      , "m", "n"    }},
}

