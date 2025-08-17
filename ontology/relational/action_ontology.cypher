// Golden AGI Action Ontology - Node Creation Script
// Based on lexical semantics (WordNet categories):contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6} 
// and speech act theory for communication verbs:contentReference[oaicite:7]{index=7}.
// This script creates all action nodes with proper properties.

// Clear existing action nodes (optional - uncomment if needed)
// MATCH (a:Action) DETACH DELETE a;

// ========================================
// CORE ACTIONS (Level 0)
// ========================================

MERGE (:Action {name_en: 'MOVEMENT',    name_ja: '移動',   level: 0, core: true})
MERGE (:Action {name_en: 'CHANGE',      name_ja: '変化',   level: 0, core: true})
MERGE (:Action {name_en: 'PHYSICAL_ACT', name_ja: '行為',   level: 0, core: true})
MERGE (:Action {name_en: 'COMMUNICATION', name_ja: '発話', level: 0, core: true})
MERGE (:Action {name_en: 'COGNITION',   name_ja: '認知',   level: 0, core: true})
MERGE (:Action {name_en: 'PERCEPTION',  name_ja: '知覚',   level: 0, core: true})
MERGE (:Action {name_en: 'EMOTION_ACT',  name_ja: '感情',   level: 0, core: true})
MERGE (:Action {name_en: 'SOCIAL_ACT',   name_ja: '社会的', level: 0, core: true})
MERGE (:Action {name_en: 'POSSESSION',  name_ja: '所有',   level: 0, core: true});

// ========================================
// MOVEMENT ACTIONS
// ========================================

// Level 1 - Categories
MERGE (:Action {name_en: 'Self Movement',   name_ja: '自身の移動', level: 1})
MERGE (:Action {name_en: 'Object Movement', name_ja: '物体の移動', level: 1})

// Level 2 - Specific Actions
// Self Movement subcategory
MERGE (:Action {name_en: 'Go',      name_ja: '行く',   level: 2})
MERGE (:Action {name_en: 'Come',    name_ja: '来る',   level: 2})
MERGE (:Action {name_en: 'Arrive',  name_ja: '到着する', level: 2})
MERGE (:Action {name_en: 'Leave',   name_ja: '去る',   level: 2})
MERGE (:Action {name_en: 'Return',  name_ja: '戻る',   level: 2})
MERGE (:Action {name_en: 'Run',     name_ja: '走る',   level: 2})
MERGE (:Action {name_en: 'Walk',    name_ja: '歩く',   level: 2})
MERGE (:Action {name_en: 'Fly',     name_ja: '飛ぶ',   level: 2})
MERGE (:Action {name_en: 'Swim',    name_ja: '泳ぐ',   level: 2})

// Object Movement subcategory
MERGE (:Action {name_en: 'Carry',   name_ja: '運ぶ',   level: 2})
MERGE (:Action {name_en: 'Bring',   name_ja: '持ってくる', level: 2})
MERGE (:Action {name_en: 'Take (away)', name_ja: '持っていく', level: 2})
MERGE (:Action {name_en: 'Push',    name_ja: '押す',   level: 2})
MERGE (:Action {name_en: 'Pull',    name_ja: '引く',   level: 2})
MERGE (:Action {name_en: 'Throw',   name_ja: '投げる', level: 2})

// ========================================
// CHANGE/TRANSFORMATION ACTIONS
// ========================================

// Level 1 - Categories
MERGE (:Action {name_en: 'Begin/Appear',    name_ja: '発生・出現', level: 1})
MERGE (:Action {name_en: 'Increase/Grow',   name_ja: '増大・成長', level: 1})
MERGE (:Action {name_en: 'Transform/Change',name_ja: '変化・変身', level: 1})
MERGE (:Action {name_en: 'Decrease/Decline',name_ja: '減少・衰退', level: 1})
MERGE (:Action {name_en: 'End/Disappear',   name_ja: '終了・消滅', level: 1})

// Level 2 - Specific Actions
// Begin/Appear subcategory
MERGE (:Action {name_en: 'Be born',   name_ja: '生まれる',   level: 2})
MERGE (:Action {name_en: 'Begin',     name_ja: '始まる',     level: 2})
MERGE (:Action {name_en: 'Appear',    name_ja: '現れる',     level: 2})
MERGE (:Action {name_en: 'Emerge',    name_ja: '出現する',   level: 2})

// Increase/Grow subcategory
MERGE (:Action {name_en: 'Grow',      name_ja: '成長する',   level: 2})
MERGE (:Action {name_en: 'Increase',  name_ja: '増える',     level: 2})
MERGE (:Action {name_en: 'Expand',    name_ja: '拡大する',   level: 2})
MERGE (:Action {name_en: 'Rise',      name_ja: '上昇する',   level: 2})

// Transform/Change subcategory
MERGE (:Action {name_en: 'Change',    name_ja: '変わる',     level: 2})
MERGE (:Action {name_en: 'Become',    name_ja: '～になる',   level: 2})
MERGE (:Action {name_en: 'Turn into', name_ja: '変身する',   level: 2})
MERGE (:Action {name_en: 'Develop (into)', name_ja: '発展する', level: 2})

// Decrease/Decline subcategory
MERGE (:Action {name_en: 'Diminish',  name_ja: '減少する',   level: 2})
MERGE (:Action {name_en: 'Decline',   name_ja: '衰退する',   level: 2})
MERGE (:Action {name_en: 'Shrink',    name_ja: '縮小する',   level: 2})
MERGE (:Action {name_en: 'Weaken',    name_ja: '弱まる',     level: 2})

// End/Disappear subcategory
MERGE (:Action {name_en: 'End',       name_ja: '終わる',     level: 2})
MERGE (:Action {name_en: 'Disappear', name_ja: '消える',     level: 2})
MERGE (:Action {name_en: 'Die',       name_ja: '死ぬ',       level: 2})
MERGE (:Action {name_en: 'Destroy (collapse)', name_ja: '崩壊する', level: 2})

// ========================================
// PHYSICAL ACTIONS (General Acts)
// ========================================

// Level 1 - Categories
MERGE (:Action {name_en: 'Manipulation/Contact', name_ja: '操作・接触', level: 1})
MERGE (:Action {name_en: 'Creation/Production',  name_ja: '創造・生産', level: 1})
MERGE (:Action {name_en: 'Destruction/Harm',     name_ja: '破壊・加害', level: 1})
MERGE (:Action {name_en: 'Consumption/Use',      name_ja: '消費・使用', level: 1})
MERGE (:Action {name_en: 'Self-Care/Grooming',   name_ja: '自己ケア',   level: 1})

// Level 2 - Specific Actions
// Manipulation/Contact subcategory
MERGE (:Action {name_en: 'Touch',     name_ja: '触れる',     level: 2})
MERGE (:Action {name_en: 'Grab/Take hold', name_ja: 'つかむ', level: 2})
MERGE (:Action {name_en: 'Hit/Strike', name_ja: '殴る',      level: 2})
MERGE (:Action {name_en: 'Pick up',   name_ja: '拾う',       level: 2})
MERGE (:Action {name_en: 'Put down',  name_ja: '置く',       level: 2})
MERGE (:Action {name_en: 'Use (an object)', name_ja: '使う', level: 2})

// Creation/Production subcategory
MERGE (:Action {name_en: 'Make/Create', name_ja: '作る',     level: 2})
MERGE (:Action {name_en: 'Build/Construct', name_ja: '建設する', level: 2})
MERGE (:Action {name_en: 'Write/Compose', name_ja: '書く・作曲する', level: 2})
MERGE (:Action {name_en: 'Cook/Prepare', name_ja: '料理する', level: 2})

// Destruction/Harm subcategory
MERGE (:Action {name_en: 'Break',     name_ja: '壊す',       level: 2})
MERGE (:Action {name_en: 'Cut',       name_ja: '切る',       level: 2})
MERGE (:Action {name_en: 'Kill',      name_ja: '殺す',       level: 2})
MERGE (:Action {name_en: 'Shoot',     name_ja: '撃つ',       level: 2})

// Consumption/Use subcategory
MERGE (:Action {name_en: 'Eat',       name_ja: '食べる',     level: 2})
MERGE (:Action {name_en: 'Drink',     name_ja: '飲む',       level: 2})
MERGE (:Action {name_en: 'Consume (use up)', name_ja: '消費する', level: 2})
MERGE (:Action {name_en: 'Spend (money/resource)', name_ja: '使い果たす', level: 2})

// Self-Care/Grooming subcategory
MERGE (:Action {name_en: 'Wash/Clean', name_ja: '洗う',      level: 2})
MERGE (:Action {name_en: 'Wash (laundry)', name_ja: '洗濯する', level: 2})
MERGE (:Action {name_en: 'Dress (oneself)', name_ja: '着替える', level: 2})
MERGE (:Action {name_en: 'Sleep',     name_ja: '眠る',       level: 2})

// ========================================
// COMMUNICATION ACTIONS (Speech Acts)
// ========================================

// Level 1 - Categories
MERGE (:Action {name_en: 'Inform/Assert (Representative)', name_ja: '伝達・主張', level: 1})
MERGE (:Action {name_en: 'Request/Command (Directive)',    name_ja: '依頼・命令', level: 1})
MERGE (:Action {name_en: 'Promise/Commit (Commissive)',    name_ja: '約束・宣誓', level: 1})
MERGE (:Action {name_en: 'Express Emotion (Expressive)',   name_ja: '感情表出',   level: 1})
MERGE (:Action {name_en: 'Declare/Official Act (Declarative)', name_ja: '宣言・宣告', level: 1})

// Level 2 - Specific Actions
// Inform/Assert subcategory
MERGE (:Action {name_en: 'Say/Tell',  name_ja: '言う',       level: 2})
MERGE (:Action {name_en: 'Explain',   name_ja: '説明する',   level: 2})
MERGE (:Action {name_en: 'Claim/Assert', name_ja: '主張する', level: 2})
MERGE (:Action {name_en: 'Report',    name_ja: '報告する',   level: 2})

// Request/Command subcategory
MERGE (:Action {name_en: 'Ask/Request', name_ja: '頼む',     level: 2})
MERGE (:Action {name_en: 'Order/Command', name_ja: '命令する', level: 2})
MERGE (:Action {name_en: 'Invite',    name_ja: '誘う',       level: 2})
MERGE (:Action {name_en: 'Beg/Plead', name_ja: '懇願する',   level: 2})

// Promise/Commit subcategory
MERGE (:Action {name_en: 'Promise',   name_ja: '約束する',   level: 2})
MERGE (:Action {name_en: 'Swear (oath)', name_ja: '誓う',    level: 2})
MERGE (:Action {name_en: 'Agree (to do)', name_ja: '同意する', level: 2})
MERGE (:Action {name_en: 'Guarantee', name_ja: '保証する',   level: 2})

// Express Emotion subcategory
MERGE (:Action {name_en: 'Apologize', name_ja: '謝る',       level: 2})
MERGE (:Action {name_en: 'Thank',     name_ja: '感謝する',   level: 2})
MERGE (:Action {name_en: 'Praise/Compliment', name_ja: '褒める', level: 2})
MERGE (:Action {name_en: 'Blame',     name_ja: '非難する',   level: 2})

// Declare/Official Act subcategory
MERGE (:Action {name_en: 'Declare (announce)', name_ja: '宣言する', level: 2})
MERGE (:Action {name_en: 'Proclaim',  name_ja: '布告する',   level: 2})
MERGE (:Action {name_en: 'Resign',    name_ja: '辞任する',   level: 2})
MERGE (:Action {name_en: 'Appoint',   name_ja: '任命する',   level: 2})

// ========================================
// COGNITION ACTIONS (Mental processes)
// ========================================

// Level 1 - Categories
MERGE (:Action {name_en: 'Thought/Reasoning', name_ja: '思考・推論', level: 1})
MERGE (:Action {name_en: 'Knowledge/Belief',  name_ja: '知識・信念', level: 1})
MERGE (:Action {name_en: 'Decision/Intention',name_ja: '決定・意図', level: 1})
MERGE (:Action {name_en: 'Memory/Recall',     name_ja: '記憶',       level: 1})
MERGE (:Action {name_en: 'Imagination',       name_ja: '想像',       level: 1})

// Level 2 - Specific Actions
// Thought/Reasoning subcategory
MERGE (:Action {name_en: 'Think',     name_ja: '考える',     level: 2})
MERGE (:Action {name_en: 'Consider',  name_ja: '検討する',   level: 2})
MERGE (:Action {name_en: 'Plan',      name_ja: '計画する',   level: 2})
MERGE (:Action {name_en: 'Solve (a problem)', name_ja: '解決する', level: 2})

// Knowledge/Belief subcategory
MERGE (:Action {name_en: 'Know',      name_ja: '知っている', level: 2})
MERGE (:Action {name_en: 'Understand',name_ja: '理解する',   level: 2})
MERGE (:Action {name_en: 'Realize',   name_ja: '悟る',       level: 2})
MERGE (:Action {name_en: 'Believe/Trust', name_ja: '信じる', level: 2})

// Decision/Intention subcategory
MERGE (:Action {name_en: 'Decide/Choose', name_ja: '決める',   level: 2})
MERGE (:Action {name_en: 'Choose/Select', name_ja: '選ぶ',     level: 2})
MERGE (:Action {name_en: 'Intend/Plan to', name_ja: '～つもりだ', level: 2})
MERGE (:Action {name_en: 'Agree (consent)', name_ja: '同意する',   level: 2})

// Memory/Recall subcategory
MERGE (:Action {name_en: 'Remember',  name_ja: '思い出す',   level: 2})
MERGE (:Action {name_en: 'Forget',    name_ja: '忘れる',     level: 2})
MERGE (:Action {name_en: 'Remind (oneself)', name_ja: '思い出させる', level: 2})

// Imagination subcategory
MERGE (:Action {name_en: 'Imagine',   name_ja: '想像する',   level: 2})
MERGE (:Action {name_en: 'Dream',     name_ja: '夢見る',     level: 2})
MERGE (:Action {name_en: 'Wonder (ponder)', name_ja: '思案する', level: 2})

// ========================================
// PERCEPTION ACTIONS (Sensory processes)
// ========================================

// Level 1 - Categories
MERGE (:Action {name_en: 'Vision (Seeing)',   name_ja: '視覚',   level: 1})
MERGE (:Action {name_en: 'Hearing (Listening)', name_ja: '聴覚', level: 1})
MERGE (:Action {name_en: 'Touch (Feeling)',   name_ja: '触覚',   level: 1})
MERGE (:Action {name_en: 'Taste (Tasting)',   name_ja: '味覚',   level: 1})
MERGE (:Action {name_en: 'Smell (Olfaction)', name_ja: '嗅覚',   level: 1})

// Level 2 - Specific Actions
// Vision subcategory
MERGE (:Action {name_en: 'See',       name_ja: '見る（見える）', level: 2})
MERGE (:Action {name_en: 'Look (at)', name_ja: '見る（見つめる）', level: 2})
MERGE (:Action {name_en: 'Watch/Observe', name_ja: '観察する', level: 2})

// Hearing subcategory
MERGE (:Action {name_en: 'Hear',      name_ja: '聞く（聞こえる）', level: 2})
MERGE (:Action {name_en: 'Listen (to)', name_ja: '聞く（耳を傾ける）', level: 2})

// Touch subcategory
MERGE (:Action {name_en: 'Feel (touch)', name_ja: '手で感じる',   level: 2})
MERGE (:Action {name_en: 'Touch (contact)', name_ja: '触る',     level: 2})

// Taste subcategory
MERGE (:Action {name_en: 'Taste',     name_ja: '味わう',     level: 2})

// Smell subcategory
MERGE (:Action {name_en: 'Smell',     name_ja: '嗅ぐ',       level: 2})

// ========================================
// EMOTION ACTIONS (Feeling processes)
// ========================================

// Level 1 - Categories
MERGE (:Action {name_en: 'Love/Affection', name_ja: '愛・好意',   level: 1})
MERGE (:Action {name_en: 'Joy/Happiness',  name_ja: '喜び',       level: 1})
MERGE (:Action {name_en: 'Surprise/Amazement', name_ja: '驚き',   level: 1})
MERGE (:Action {name_en: 'Fear/Terror',    name_ja: '恐れ',       level: 1})
MERGE (:Action {name_en: 'Anger/Rage',     name_ja: '怒り',       level: 1})
MERGE (:Action {name_en: 'Sadness/Grief',  name_ja: '悲しみ',     level: 1})
MERGE (:Action {name_en: 'Dislike/Hate',   name_ja: '嫌悪・憎しみ', level: 1})
MERGE (:Action {name_en: 'Disgust/Revulsion', name_ja: '嫌悪感',   level: 1})

// Level 2 - Specific Actions
// Love/Affection subcategory
MERGE (:Action {name_en: 'Love',      name_ja: '愛する',     level: 2})
MERGE (:Action {name_en: 'Like',      name_ja: '好む',       level: 2})
MERGE (:Action {name_en: 'Adore',     name_ja: '崇拝する',   level: 2})

// Joy/Happiness subcategory
MERGE (:Action {name_en: 'Rejoice',   name_ja: '喜ぶ',       level: 2})
MERGE (:Action {name_en: 'Laugh (with joy)', name_ja: '笑う', level: 2})
MERGE (:Action {name_en: 'Celebrate', name_ja: '祝う',       level: 2})

// Surprise/Amazement subcategory
MERGE (:Action {name_en: 'Be surprised', name_ja: '驚く',    level: 2})
MERGE (:Action {name_en: 'Amaze (someone)', name_ja: '驚かす', level: 2})

// Fear/Terror subcategory
MERGE (:Action {name_en: 'Fear',      name_ja: '恐れる',     level: 2})
MERGE (:Action {name_en: 'Dread',     name_ja: 'ひどく恐れる', level: 2})
MERGE (:Action {name_en: 'Panic',     name_ja: 'パニックになる', level: 2})

// Anger/Rage subcategory
MERGE (:Action {name_en: 'Get angry', name_ja: '怒る',       level: 2})
MERGE (:Action {name_en: 'Resent',    name_ja: '憤慨する',   level: 2})
MERGE (:Action {name_en: 'Revolt (become indignant)', name_ja: '憤る', level: 2})

// Sadness/Grief subcategory
MERGE (:Action {name_en: 'Grieve/Lament', name_ja: '悲しむ', level: 2})
MERGE (:Action {name_en: 'Cry/Weep',  name_ja: '泣く',       level: 2})
MERGE (:Action {name_en: 'Regret',    name_ja: '後悔する',   level: 2})

// Dislike/Hate subcategory
MERGE (:Action {name_en: 'Hate/Detest', name_ja: '憎む',     level: 2})
MERGE (:Action {name_en: 'Dislike',   name_ja: '嫌う',       level: 2})
MERGE (:Action {name_en: 'Envy',      name_ja: '羨む',       level: 2})

// Disgust/Revulsion subcategory
MERGE (:Action {name_en: 'Feel disgust', name_ja: '嫌悪する', level: 2})
MERGE (:Action {name_en: 'Be disgusted', name_ja: 'むかつく', level: 2})

// ========================================
// SOCIAL ACTIONS (Interpersonal interactions)
// ========================================

// Level 1 - Categories
MERGE (:Action {name_en: 'Cooperation/Help', name_ja: '協力・助力', level: 1})
MERGE (:Action {name_en: 'Conflict/Attack',  name_ja: '闘争・攻撃', level: 1})
MERGE (:Action {name_en: 'Group/Organization', name_ja: '集団・組織行動', level: 1})
MERGE (:Action {name_en: 'Leadership/Authority', name_ja: '指導・権威', level: 1})

// Level 2 - Specific Actions
// Cooperation/Help subcategory
MERGE (:Action {name_en: 'Help/Assist', name_ja: '助ける',   level: 2})
MERGE (:Action {name_en: 'Cooperate',   name_ja: '協力する', level: 2})
MERGE (:Action {name_en: 'Share',       name_ja: '共有する', level: 2})
MERGE (:Action {name_en: 'Support (someone)', name_ja: '支援する', level: 2})

// Conflict/Attack subcategory
MERGE (:Action {name_en: 'Fight',      name_ja: '戦う',       level: 2})
MERGE (:Action {name_en: 'Attack',     name_ja: '攻撃する',   level: 2})
MERGE (:Action {name_en: 'Compete',    name_ja: '競争する',   level: 2})
MERGE (:Action {name_en: 'Argue/Quarrel', name_ja: '口論する', level: 2})

// Group/Organization subcategory
MERGE (:Action {name_en: 'Meet/Gather', name_ja: '集まる・会う', level: 2})
MERGE (:Action {name_en: 'Join (group)', name_ja: '参加する',   level: 2})
MERGE (:Action {name_en: 'Invite (into group)', name_ja: '招待する', level: 2})
MERGE (:Action {name_en: 'Celebrate (together)', name_ja: '共に祝う', level: 2})

// Leadership/Authority subcategory
MERGE (:Action {name_en: 'Lead/Guide',  name_ja: '導く',     level: 2})
MERGE (:Action {name_en: 'Command (leadership)', name_ja: '率いる', level: 2})
MERGE (:Action {name_en: 'Obey/Follow', name_ja: '従う',     level: 2})
MERGE (:Action {name_en: 'Represent (on behalf of)', name_ja: '代表する', level: 2})

// ========================================
// POSSESSION/TRANSACTION ACTIONS
// ========================================

// Level 1 - Categories
MERGE (:Action {name_en: 'Giving/Providing', name_ja: '提供・譲渡', level: 1})
MERGE (:Action {name_en: 'Obtaining/Receiving', name_ja: '獲得・受領', level: 1})
MERGE (:Action {name_en: 'Exchange/Trade',   name_ja: '交換・取引',   level: 1})

// Level 2 - Specific Actions
// Giving/Providing subcategory
MERGE (:Action {name_en: 'Give',      name_ja: '与える',     level: 2})
MERGE (:Action {name_en: 'Offer',     name_ja: '提供する',   level: 2})
MERGE (:Action {name_en: 'Sell',      name_ja: '売る',       level: 2})
MERGE (:Action {name_en: 'Lend',      name_ja: '貸す',       level: 2})

// Obtaining/Receiving subcategory
MERGE (:Action {name_en: 'Get/Obtain', name_ja: '手に入れる', level: 2})
MERGE (:Action {name_en: 'Receive',    name_ja: '受け取る',   level: 2})
MERGE (:Action {name_en: 'Buy/Purchase', name_ja: '買う',     level: 2})
MERGE (:Action {name_en: 'Steal',      name_ja: '盗む',       level: 2})

// Exchange/Trade subcategory
MERGE (:Action {name_en: 'Trade/Exchange', name_ja: '交換する', level: 2})
MERGE (:Action {name_en: 'Swap',       name_ja: '交換する (スワップ)', level: 2})
MERGE (:Action {name_en: 'Pay',        name_ja: '支払う',     level: 2})
MERGE (:Action {name_en: 'Borrow',     name_ja: '借りる',     level: 2})

// ========================================
// Add indexes for better performance (optional)
// ========================================

CREATE INDEX action_name_en IF NOT EXISTS FOR (a:Action) ON (a.name_en);
CREATE INDEX action_level   IF NOT EXISTS FOR (a:Action) ON (a.level);
CREATE INDEX action_core    IF NOT EXISTS FOR (a:Action) ON (a.core);

// ========================================
// Verification Query (example)
// ========================================
// MATCH (a:Action) RETURN a.level, count(a) ORDER BY a.level;
