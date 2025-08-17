// Story Classification Ontology
// 14番目のオントロジー：物語分類体系
// Created by Lina for Twin Engine Analyzer
// 
// Based on international folktale type indices (ATU):contentReference[oaicite:5]{index=5},
// Propp's 31 narrative functions:contentReference[oaicite:6]{index=6},
// and genre categories from cultural folklore studies:contentReference[oaicite:7]{index=7} and modern fiction.

// (Optional) Clear existing nodes if re-running:
// MATCH (n) WHERE n:Story OR n:StoryCategory OR n:ClassificationSystem OR n:ProppFunction OR n:RequiredElement DETACH DELETE n;

// ========================================
// Classification Systems (Meta nodes)
// ========================================
MERGE (:ClassificationSystem {name: 'ATU', description: 'International folktale type index', type: 'international_standard'})
MERGE (:ClassificationSystem {name: 'Propp', description: 'Narrative function analysis', type: 'functional_analysis'})
MERGE (:ClassificationSystem {name: 'Cultural', description: 'Culture-specific folktale categories', type: 'cultural_specific'})
MERGE (:ClassificationSystem {name: 'Modern', description: 'Modern literary genre taxonomy', type: 'contemporary_genres'})

// ========================================
// ATU Folktale Type Classification (International Standard):contentReference[oaicite:8]{index=8}
// ========================================

// Level 1 – Main ATU categories (with number ranges)
MERGE (:StoryCategory:ATU {code: '1-299',    name_en: 'Animal Tales',           name_ja: '動物昔話',      level: 1})
MERGE (:StoryCategory:ATU {code: '300-749',  name_en: 'Tales of Magic',         name_ja: '魔法昔話',      level: 1})
MERGE (:StoryCategory:ATU {code: '750-849',  name_en: 'Religious Tales',        name_ja: '宗教的昔話',    level: 1})
MERGE (:StoryCategory:ATU {code: '850-999',  name_en: 'Realistic Tales (Novelle)', name_ja: 'ロマンス昔話', level: 1})
MERGE (:StoryCategory:ATU {code: '1000-1199',name_en: 'Tales of the Stupid Ogre (Giant/Devil)', /*name_ja: '愚者譚'*/, level: 1})
MERGE (:StoryCategory:ATU {code: '1200-1999',name_en: 'Anecdotes and Jokes',    name_ja: '笑話',          level: 1})
MERGE (:StoryCategory:ATU {code: '2000-2399',name_en: 'Formula Tales',          name_ja: '形式譚',        level: 1})

// Level 2 – Example ATU tale types (subcategories or specific tale types)
MERGE (:StoryCategory:ATU {code: '510A', name_en: 'Cinderella (Persecuted Heroine)', level: 2})
MERGE (:StoryCategory:ATU {code: '300',  name_en: 'The Dragon Slayer (Hero kills monster)', level: 2})

// (Additional ATU subcategories/types can be added as needed)

// ========================================
// Propp's 31 Narrative Functions (Morphology of the Folktale):contentReference[oaicite:9]{index=9}
// ========================================

// Each ProppFunction node has an order number and English/Japanese labels
MERGE (:ProppFunction {number: 1,  name_en: 'Absentation',               name_ja: '留守'})          // a family member leaves
MERGE (:ProppFunction {number: 2,  name_en: 'Interdiction',              name_ja: '禁止'})         // hero is warned
MERGE (:ProppFunction {number: 3,  name_en: 'Violation of Interdiction', name_ja: '違反'})         // warning is violated
MERGE (:ProppFunction {number: 4,  name_en: 'Reconnaissance',            name_ja: '探り出し'})     // villain seeks information
MERGE (:ProppFunction {number: 5,  name_en: 'Delivery (Information)',    name_ja: '情報漏洩'})    // villain gains information
MERGE (:ProppFunction {number: 6,  name_en: 'Trickery',                  name_ja: '策略'})         // villain deceives victim
MERGE (:ProppFunction {number: 7,  name_en: 'Complicity',                name_ja: '幇助'})         // victim is deceived and helps villain
MERGE (:ProppFunction {number: 8,  name_en: 'Villainy or Lack',          name_ja: '悪事・欠如'})  // villain harms or a need is identified
MERGE (:ProppFunction {number: 9,  name_en: 'Mediation (Misfortune Made Known)', name_ja: '仲介'}) // hero learns of the trouble
MERGE (:ProppFunction {number: 10, name_en: 'Beginning Counteraction',   name_ja: '対抗の開始'})  // hero chooses positive action
MERGE (:ProppFunction {number: 11, name_en: 'Departure',                 name_ja: '出発'})         // hero leaves home
MERGE (:ProppFunction {number: 12, name_en: 'First Donor Function (Test)', name_ja: '最初の提供者'}) // hero encounters a helper and is tested
MERGE (:ProppFunction {number: 13, name_en: "Hero's Reaction",           name_ja: '主人公の反応'}) // hero reacts to test (success or failure)
MERGE (:ProppFunction {number: 14, name_en: 'Acquisition of Magical Agent', name_ja: '授与'})      // hero gains a magical item/help
MERGE (:ProppFunction {number: 15, name_en: 'Guidance (Spatial Transference)', name_ja: '移動'})   // hero is transported or led somewhere
MERGE (:ProppFunction {number: 16, name_en: 'Struggle',                  name_ja: '闘争'})         // hero and villain engage in direct combat
MERGE (:ProppFunction {number: 17, name_en: 'Branding (Marking)',        name_ja: '烙印'})         // hero receives a mark or wound
MERGE (:ProppFunction {number: 18, name_en: 'Victory',                   name_ja: '勝利'})         // villain is defeated
MERGE (:ProppFunction {number: 19, name_en: 'Liquidation (Resolution)',  name_ja: '解決'})         // initial misfortune or lack is resolved
MERGE (:ProppFunction {number: 20, name_en: 'Return',                    name_ja: '帰還'})         // hero returns home
MERGE (:ProppFunction {number: 21, name_en: 'Pursuit (Chase)',           name_ja: '追跡'})         // hero is pursued by villain
MERGE (:ProppFunction {number: 22, name_en: 'Rescue',                    name_ja: '救出'})         // hero is rescued from pursuit
MERGE (:ProppFunction {number: 23, name_en: 'Unrecognized Arrival',      name_ja: '匿名の帰郷'})   // hero arrives home or elsewhere unrecognized
MERGE (:ProppFunction {number: 24, name_en: 'Unfounded Claims',          name_ja: '虚偽の主張'})   // false hero or villain makes false claims
MERGE (:ProppFunction {number: 25, name_en: 'Difficult Task',            name_ja: '難題'})         // a trial or challenge is proposed to the hero
MERGE (:ProppFunction {number: 26, name_en: 'Solution',                  name_ja: '解決策'})       // hero accomplishes the task
MERGE (:ProppFunction {number: 27, name_en: 'Recognition',               name_ja: '正体発見'})     // hero is recognized (often by a mark or token)
MERGE (:ProppFunction {number: 28, name_en: 'Exposure (of False Hero)',  name_ja: '偽者の暴露'})   // false hero or villain is exposed
MERGE (:ProppFunction {number: 29, name_en: 'Transfiguration',           name_ja: '変貌'})         // hero is given a new appearance (e.g., new clothes, transformation)
MERGE (:ProppFunction {number: 30, name_en: 'Punishment',                name_ja: '懲罰'})         // villain is punished
MERGE (:ProppFunction {number: 31, name_en: 'Wedding',                   name_ja: '結婚'})         // hero marries and ascends the throne or attains reward

// ========================================
// Culture-Specific Folktale Classifications (Japanese example):contentReference[oaicite:10]{index=10}
// ========================================

// Top-level Japanese folktale categories (analogous to ATU top-level categories)
MERGE (:StoryCategory:JapaneseCategory {name_en: 'Animal Tales (Japan)',    name_ja: '動物昔話'})
MERGE (:StoryCategory:JapaneseCategory {name_en: 'Standard Folktales (Japan)', name_ja: '本格昔話'})
MERGE (:StoryCategory:JapaneseCategory {name_en: 'Humorous Tales (Japan)',  name_ja: '笑話'})
MERGE (:StoryCategory:JapaneseCategory {name_en: 'Formula Tales (Japan)',   name_ja: '形式譚'})

// Level 1 – Selected Japanese folktale types/motifs (with example themes)
MERGE (:StoryCategory:JapaneseType {name_en: 'Supernatural Marriage Tale', name_ja: '異類婚姻譚', description: 'Human marries non-human (e.g. “Crane Wife”, Yuki-Onna)'})
MERGE (:StoryCategory:JapaneseType {name_en: 'Miraculous Birth Tale',      name_ja: '異常誕生譚', description: 'Miraculous or unusual birth of protagonist (e.g. Momotaro, Kaguya-hime)'})
MERGE (:StoryCategory:JapaneseType {name_en: 'Fortune Gained Tale',        name_ja: '致富譚',   description: '“Rags to riches” story (e.g. Straw Millionaire, Hanasaka Jiisan)'})
MERGE (:StoryCategory:JapaneseType {name_en: 'Reward-for-Kindness Tale',   name_ja: '報恩譚',   description: 'A grateful creature repays kindness (e.g. Crane’s Gratitude, Urashima Taro)'})
MERGE (:StoryCategory:JapaneseType {name_en: 'Demon-Slaying Tale',         name_ja: '鬼退治譚', description: 'Hero must defeat ogres/demons (e.g. Suzuka legend, Momotaro)'})

// (Similar cultural taxonomy nodes could be added for other cultures, e.g., Chinese tale types, etc.)

// ========================================
// Modern Literary Genres and Subgenres
// ========================================

// Level 0 – Main modern genres
MERGE (:StoryCategory:ModernGenre {name_en: 'Mystery',          name_ja: 'ミステリー'})
MERGE (:StoryCategory:ModernGenre {name_en: 'Science Fiction',  name_ja: 'SF'})
MERGE (:StoryCategory:ModernGenre {name_en: 'Romance',          name_ja: 'ロマンス'})
// (Other genres like Fantasy, Horror, etc., can be added as needed)

// Level 1 – Subgenres of Mystery
MERGE (:StoryCategory:Subgenre {name_en: 'Classic Detective Mystery', name_ja: '本格推理',
    required_elements: ['謎の提示','手がかり','論理的解決'],
    examples: ['そして誰もいなくなった','容疑者Xの献身'] })      // e.g. "And Then There Were None", "The Devotion of Suspect X"
MERGE (:StoryCategory:Subgenre {name_en: 'Hardboiled Detective',      name_ja: 'ハードボイルド',
    required_elements: ['探偵','都市','暴力'],
    examples: ['マルタの鷹','長いお別れ'] })                     // e.g. "The Maltese Falcon", "The Long Goodbye"
MERGE (:StoryCategory:Subgenre {name_en: 'Cozy Mystery',             name_ja: 'コージーミステリ',
    required_elements: ['日常的な舞台','アマチュア探偵','穏やかな雰囲気'],
    examples: ['Miss Marple series','The No.1 Ladies’ Detective Agency'] })

// Link Mystery genre to its subgenres
MERGE (genreMystery:StoryCategory {name_en: 'Mystery'}) 
MERGE (subMystery1:StoryCategory {name_en: 'Classic Detective Mystery'}) 
MERGE (subMystery2:StoryCategory {name_en: 'Hardboiled Detective'}) 
MERGE (subMystery3:StoryCategory {name_en: 'Cozy Mystery'})
MERGE (genreMystery)-[:HAS_SUBGENRE]->(subMystery1)
MERGE (genreMystery)-[:HAS_SUBGENRE]->(subMystery2)
MERGE (genreMystery)-[:HAS_SUBGENRE]->(subMystery3)

// Subgenres of Science Fiction
MERGE (:StoryCategory:Subgenre {name_en: 'Hard Science Fiction', name_ja: 'ハードSF',
    required_elements: ['科学的整合性','詳細な技術描写'],
    examples: ['三体','火星の人'] })                             // e.g. "The Three-Body Problem", "The Martian"
MERGE (:StoryCategory:Subgenre {name_en: 'Dystopian Sci-Fi',     name_ja: 'ディストピア',
    required_elements: ['管理社会','個人vs体制'],
    examples: ['1984','すばらしい新世界'] })                      // e.g. "1984", "Brave New World"

// Link Science Fiction genre to its subgenres
MERGE (genreSF:StoryCategory {name_en: 'Science Fiction'})
MERGE (subSF1:StoryCategory {name_en: 'Hard Science Fiction'})
MERGE (subSF2:StoryCategory {name_en: 'Dystopian Sci-Fi'})
MERGE (genreSF)-[:HAS_SUBGENRE]->(subSF1)
MERGE (genreSF)-[:HAS_SUBGENRE]->(subSF2)

// Subgenres of Romance
MERGE (:StoryCategory:Subgenre {name_en: 'Pure Love Romance', name_ja: '純愛',
    required_elements: ['出会い','障害','感動的結末'],
    examples: ['ノルウェイの森','君の名は。'] })                   // e.g. "Norwegian Wood", "Your Name."

// Link Romance genre to its subgenre
MERGE (genreRomance:StoryCategory {name_en: 'Romance'})
MERGE (subRom1:StoryCategory {name_en: 'Pure Love Romance'})
MERGE (genreRomance)-[:HAS_SUBGENRE]->(subRom1)

// (Additional genres like Fantasy, Horror, etc., and their subgenres could be modeled similarly)

// ========================================
// Cross-References and Hybrid Categories
// ========================================

// Cross-reference between ATU and Japanese classification (example)
MERGE (atu510A:StoryCategory:ATU {code: '510A'}) 
MERGE (jpStepmother:StoryCategory:JapaneseType {name_ja: '継子いじめ譚'})
MERGE (atu510A)-[:EQUIVALENT_TO {confidence: 0.85}]->(jpStepmother)
// (e.g., ATU 510A "Cinderella" is equivalent to the Japanese "Stepmother Persecution Tale" with high confidence)

// Required element metadata (symbolic items, motifs, etc.)
MERGE (kibidango:RequiredElement {name: 'きびだんご (millet dumpling)', type: 'symbolic_item'})
MERGE (oniTaiji:StoryCategory:JapaneseType {name_ja: '鬼退治譚'})
MERGE (kibidango)-[:REQUIRED_FOR]->(oniTaiji)
// (e.g., kibidango is a required item for the "Ogre Slaying" tale type, as in the Momotaro story)

// Example story node with multiple classifications and narrative functions
MERGE (momotaro:Story {name: '桃太郎', name_en: 'Momotaro', origin: 'Japan'})
MERGE (momotaro)-[:CLASSIFIED_AS]->(:StoryCategory:ATU {code: '300', name_en: 'The Dragon Slayer'})
MERGE (momotaro)-[:CLASSIFIED_AS]->(:StoryCategory:JapaneseType {name_ja: '異常誕生譚'})
MERGE (momotaro)-[:HAS_FUNCTION]->(:ProppFunction {number: 11, name_en: 'Departure'})
MERGE (momotaro)-[:HAS_FUNCTION]->(:ProppFunction {number: 20, name_en: 'Return'})
MERGE (kibidango)-[:APPEARS_IN]->(momotaro)

// Hybrid genre example (story that combines two genres)
MERGE (hybridType:StoryCategory:HybridType {name: 'Sci-Fi Mystery', primary: 'Science Fiction', secondary: 'Mystery'})
MERGE (newStory:Story {name: 'New Tale'})
MERGE (newStory)-[:POSSIBLY_CLASSIFIED_AS {confidence: 0.7}]->(hybridType)

// ========================================
// Indexes for efficient lookup (optional)
// ========================================
CREATE INDEX IF NOT EXISTS FOR (c:StoryCategory) ON (c.name_en);
CREATE INDEX IF NOT EXISTS FOR (p:ProppFunction) ON (p.number);
CREATE INDEX IF NOT EXISTS FOR (s:Story) ON (s.name);

// ========================================
// Example Query: Generate a checklist of required elements for a given story
// ========================================
// MATCH (s:Story)-[:CLASSIFIED_AS]->(t)<-[:REQUIRED_FOR]-(e:RequiredElement)
// WHERE s.name = '桃太郎'
// RETURN s.name AS Story, collect(e.name) AS RequiredElements;
