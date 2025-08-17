// Golden AGI Emotion Ontology - Node Creation Script
// Based on Lina's advice and Plutchik's emotion wheel
// This script creates all emotion nodes with proper properties

// Clear existing emotion nodes (optional - uncomment if needed)
// MATCH (e:Emotion) DETACH DELETE e;

// ========================================
// CORE EMOTIONS (Level 0)
// ========================================

MERGE (:Emotion {name_en: 'HAPPY', name_ja: '幸せ', level: 0, core: true})
MERGE (:Emotion {name_en: 'SURPRISE', name_ja: '驚き', level: 0, core: true})
MERGE (:Emotion {name_en: 'FEAR', name_ja: '恐れ', level: 0, core: true})
MERGE (:Emotion {name_en: 'ANGER', name_ja: '怒り', level: 0, core: true})
MERGE (:Emotion {name_en: 'DISGUST', name_ja: '嫌悪', level: 0, core: true})
MERGE (:Emotion {name_en: 'SAD', name_ja: '悲しみ', level: 0, core: true});

// ========================================
// HAPPY EMOTIONS
// ========================================

// Level 1 - Categories
MERGE (:Emotion {name_en: 'Peaceful', name_ja: '穏やか', level: 1})
MERGE (:Emotion {name_en: 'Powerful', name_ja: '力強い', level: 1})
MERGE (:Emotion {name_en: 'Accepted', name_ja: '受け入れられた', level: 1})
MERGE (:Emotion {name_en: 'Proud', name_ja: '誇らしい', level: 1})
MERGE (:Emotion {name_en: 'Interested', name_ja: '興味がある', level: 1})
MERGE (:Emotion {name_en: 'Joyful', name_ja: '喜びに満ちた', level: 1});

// Level 2 - Specific Emotions
// Peaceful subcategory
MERGE (:Emotion {name_en: 'Loving', name_ja: '愛おしい', level: 2})
MERGE (:Emotion {name_en: 'Hopeful', name_ja: '希望に満ちた', level: 2})
MERGE (:Emotion {name_en: 'Sensitive', name_ja: '感受性の強い', level: 2})
MERGE (:Emotion {name_en: 'Playful', name_ja: '遊び心のある', level: 2});

// Powerful subcategory
MERGE (:Emotion {name_en: 'Courageous', name_ja: '勇敢な', level: 2})
MERGE (:Emotion {name_en: 'Provocative', name_ja: '刺激的な', level: 2});

// Accepted subcategory
MERGE (:Emotion {name_en: 'Fulfilled', name_ja: '満たされた', level: 2})
MERGE (:Emotion {name_en: 'Respected', name_ja: '尊敬された', level: 2});

// Proud subcategory
MERGE (:Emotion {name_en: 'Confident', name_ja: '自信がある', level: 2})
MERGE (:Emotion {name_en: 'Important', name_ja: '重要だと感じる', level: 2});

// Interested subcategory
MERGE (:Emotion {name_en: 'Inquisitive', name_ja: '探求心がある', level: 2})
MERGE (:Emotion {name_en: 'Amused', name_ja: '面白い', level: 2});

// Joyful subcategory
MERGE (:Emotion {name_en: 'Ecstatic', name_ja: '有頂天', level: 2})
MERGE (:Emotion {name_en: 'Liberated', name_ja: '解放された', level: 2})
MERGE (:Emotion {name_en: 'Energetic', name_ja: 'エネルギッシュな', level: 2})
MERGE (:Emotion {name_en: 'Eager', name_ja: '熱望している', level: 2});

// ========================================
// SURPRISE EMOTIONS
// ========================================

// Level 1 - Categories
MERGE (:Emotion {name_en: 'Excited', name_ja: '興奮した', level: 1})
MERGE (:Emotion {name_en: 'Amazed', name_ja: '感嘆した', level: 1})
MERGE (:Emotion {name_en: 'Confused', name_ja: '混乱した', level: 1})
MERGE (:Emotion {name_en: 'Startled', name_ja: 'びっくりした', level: 1});

// Level 2 - Specific Emotions
// Excited subcategory
MERGE (:Emotion {name_en: 'Awe', name_ja: '畏敬', level: 2})
MERGE (:Emotion {name_en: 'Astonished', name_ja: '驚愕した', level: 2});

// Amazed subcategory
MERGE (:Emotion {name_en: 'Perplexed', name_ja: '困惑した', level: 2})
MERGE (:Emotion {name_en: 'Disillusioned', name_ja: '幻滅した', level: 2});

// Confused subcategory
MERGE (:Emotion {name_en: 'Dismayed', name_ja: '狼狽した', level: 2})
MERGE (:Emotion {name_en: 'Shocked', name_ja: '衝撃を受けた', level: 2});

// Startled subcategory
MERGE (:Emotion {name_en: 'Terrified', name_ja: '恐ろしい', level: 2})
MERGE (:Emotion {name_en: 'Frightened', name_ja: 'おびえた', level: 2});

// ========================================
// FEAR EMOTIONS
// ========================================

// Level 1 - Categories
MERGE (:Emotion {name_en: 'Scared', name_ja: '怖い', level: 1})
MERGE (:Emotion {name_en: 'Anxious', name_ja: '不安', level: 1})
MERGE (:Emotion {name_en: 'Insecure', name_ja: '自信がない', level: 1})
MERGE (:Emotion {name_en: 'Submissive', name_ja: '従順', level: 1})
MERGE (:Emotion {name_en: 'Rejected', name_ja: '拒絶された', level: 1})
MERGE (:Emotion {name_en: 'Humiliated', name_ja: '屈辱を受けた', level: 1});

// Level 2 - Specific Emotions
// Scared subcategory
MERGE (:Emotion {name_en: 'Overwhelmed', name_ja: '圧倒された', level: 2})
MERGE (:Emotion {name_en: 'Worried', name_ja: '心配な', level: 2});

// Anxious subcategory
MERGE (:Emotion {name_en: 'Inadequate', name_ja: '不十分だと感じる', level: 2})
MERGE (:Emotion {name_en: 'Inferior', name_ja: '劣等感', level: 2});

// Insecure subcategory (note: this node is also under ANGER)
MERGE (:Emotion {name_en: 'Worthless', name_ja: '価値がない', level: 2})
MERGE (:Emotion {name_en: 'Insignificant', name_ja: '取るに足らない', level: 2});

// Submissive subcategory
// Note: Rejected and Humiliated are already created as Level 1

// Rejected subcategory (when treated as Level 1)
MERGE (:Emotion {name_en: 'Alienated', name_ja: '疎外された', level: 2})
MERGE (:Emotion {name_en: 'Disrespected', name_ja: '軽蔑された', level: 2});

// Humiliated subcategory (when treated as Level 1)
MERGE (:Emotion {name_en: 'Ridiculed', name_ja: '嘲笑された', level: 2})
MERGE (:Emotion {name_en: 'Embarrassed', name_ja: '恥ずかしい', level: 2});

// ========================================
// ANGER EMOTIONS
// ========================================

// Level 1 - Categories
MERGE (:Emotion {name_en: 'Hurt', name_ja: '傷ついた', level: 1})
MERGE (:Emotion {name_en: 'Threatened', name_ja: '脅かされた', level: 1})
MERGE (:Emotion {name_en: 'Hateful', name_ja: '憎い', level: 1})
MERGE (:Emotion {name_en: 'Mad', name_ja: '腹が立つ', level: 1})
MERGE (:Emotion {name_en: 'Aggressive', name_ja: '攻撃的', level: 1})
MERGE (:Emotion {name_en: 'Frustrated', name_ja: '不満', level: 1});

// Level 2 - Specific Emotions
// Hurt subcategory
MERGE (:Emotion {name_en: 'Devastated', name_ja: '打ちのめされた', level: 2});
// Note: Insecure is already created under FEAR

// Threatened subcategory
MERGE (:Emotion {name_en: 'Jealous', name_ja: '嫉妬した', level: 2})
MERGE (:Emotion {name_en: 'Resentful', name_ja: '憤慨した', level: 2});

// Hateful subcategory
MERGE (:Emotion {name_en: 'Violated', name_ja: '侵害された', level: 2})
MERGE (:Emotion {name_en: 'Furious', name_ja: '激怒した', level: 2});

// Mad subcategory
MERGE (:Emotion {name_en: 'Enraged', name_ja: '憤激した', level: 2})
MERGE (:Emotion {name_en: 'Provoked', name_ja: '挑発された', level: 2});

// Aggressive subcategory
MERGE (:Emotion {name_en: 'Hostile', name_ja: '敵意のある', level: 2})
MERGE (:Emotion {name_en: 'Infuriated', name_ja: '激高した', level: 2});

// Frustrated subcategory
MERGE (:Emotion {name_en: 'Irritated', name_ja: 'イライラする', level: 2})
MERGE (:Emotion {name_en: 'Withdrawn', name_ja: '引きこもった', level: 2});

// ========================================
// DISGUST EMOTIONS
// ========================================

// Level 1 - Categories
MERGE (:Emotion {name_en: 'Critical', name_ja: '批判的', level: 1})
MERGE (:Emotion {name_en: 'Distant', name_ja: 'よそよそしい', level: 1})
MERGE (:Emotion {name_en: 'Disapproval', name_ja: '不満', level: 1})
MERGE (:Emotion {name_en: 'Disappointed', name_ja: 'がっかりした', level: 1})
MERGE (:Emotion {name_en: 'Awful', name_ja: 'ひどい', level: 1})
MERGE (:Emotion {name_en: 'Avoidance', name_ja: '回避', level: 1});

// Level 2 - Specific Emotions
// Critical subcategory
MERGE (:Emotion {name_en: 'Suspicious', name_ja: '疑い深い', level: 2})
MERGE (:Emotion {name_en: 'Skeptical', name_ja: '懐疑的', level: 2});

// Distant subcategory
MERGE (:Emotion {name_en: 'Sarcastic', name_ja: '皮肉な', level: 2})
MERGE (:Emotion {name_en: 'Judgmental', name_ja: '批判的な', level: 2});

// Disapproval subcategory
MERGE (:Emotion {name_en: 'Loathing', name_ja: '嫌悪', level: 2})
MERGE (:Emotion {name_en: 'Repugnant', name_ja: '不快な', level: 2});

// Disappointed subcategory
MERGE (:Emotion {name_en: 'Revolted', name_ja: '反感を持つ', level: 2})
MERGE (:Emotion {name_en: 'Revulsion', name_ja: '強い嫌悪', level: 2});

// Awful subcategory
MERGE (:Emotion {name_en: 'Detestable', name_ja: '忌まわしい', level: 2})
MERGE (:Emotion {name_en: 'Aversion', name_ja: '嫌悪感', level: 2});

// Avoidance subcategory
MERGE (:Emotion {name_en: 'Hesitant', name_ja: 'ためらい', level: 2})
MERGE (:Emotion {name_en: 'Remorseful', name_ja: '後悔', level: 2});

// ========================================
// SAD EMOTIONS
// ========================================

// Level 1 - Categories
MERGE (:Emotion {name_en: 'Guilty', name_ja: '罪悪感', level: 1})
MERGE (:Emotion {name_en: 'Abandoned', name_ja: '見捨てられた', level: 1})
MERGE (:Emotion {name_en: 'Despair', name_ja: '絶望', level: 1})
MERGE (:Emotion {name_en: 'Depressed', name_ja: '落ち込んだ', level: 1})
MERGE (:Emotion {name_en: 'Lonely', name_ja: '孤独', level: 1})
MERGE (:Emotion {name_en: 'Bored', name_ja: '退屈', level: 1});

// Level 2 - Specific Emotions
// Guilty subcategory
MERGE (:Emotion {name_en: 'Ashamed', name_ja: '恥じている', level: 2})
MERGE (:Emotion {name_en: 'Ignored', name_ja: '無視された', level: 2});

// Abandoned subcategory (when treated as Level 1)
MERGE (:Emotion {name_en: 'Victimized', name_ja: '犠牲になった', level: 2})
MERGE (:Emotion {name_en: 'Powerless', name_ja: '無力な', level: 2});

// Despair subcategory
MERGE (:Emotion {name_en: 'Vulnerable', name_ja: '傷つきやすい', level: 2});
// Note: Inferior is already created under FEAR

// Depressed subcategory
MERGE (:Emotion {name_en: 'Empty', name_ja: '空虚な', level: 2});
// Note: Abandoned is already created as Level 1

// Lonely subcategory
MERGE (:Emotion {name_en: 'Isolated', name_ja: '孤立した', level: 2})
MERGE (:Emotion {name_en: 'Apathetic', name_ja: '無関心な', level: 2});

// Bored subcategory
MERGE (:Emotion {name_en: 'Indifferent', name_ja: '無関心な', level: 2})
MERGE (:Emotion {name_en: 'Inspired', name_ja: 'ひらめいた', level: 2});

// ========================================
// Add indexes for better performance
// ========================================

CREATE INDEX emotion_name_en IF NOT EXISTS FOR (e:Emotion) ON (e.name_en);
CREATE INDEX emotion_level IF NOT EXISTS FOR (e:Emotion) ON (e.level);
CREATE INDEX emotion_core IF NOT EXISTS FOR (e:Emotion) ON (e.core);

// ========================================
// Verification Query
// ========================================
// Run this to verify node creation:
// MATCH (e:Emotion) RETURN e.level, count(e) ORDER BY e.level;