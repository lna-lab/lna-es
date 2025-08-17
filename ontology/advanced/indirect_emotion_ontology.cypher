// Golden AGI Indirect Emotion Ontology
// Based on psychology and embodied cognition research:
// - Laban Movement Analysis (8 Efforts) - Shafir et al., 2016
// - Body postures and basic emotions - Ross & Flack et al., 2017
// - Physiological indicators - Romanczyk & Gillis 2006
// Structure: Body Domain (Level 0) → Body Cue (Level 1) → Specific Examples (Level 2)
// Connects to existing Emotion nodes via SUGGESTS relationships

// ========================================
// BODY DOMAINS (Level 0)
// ========================================

MERGE (:BodyDomain {name_en: 'POSTURE', name_ja: '姿勢', level: 0, core: true});
MERGE (:BodyDomain {name_en: 'GESTURE', name_ja: 'ジェスチャー', level: 0, core: true});
MERGE (:BodyDomain {name_en: 'MOVEMENT_EFFORT', name_ja: '動作エフォート', level: 0, core: true});
MERGE (:BodyDomain {name_en: 'PHYSIOLOGICAL', name_ja: '生理反応', level: 0, core: true});

// ========================================
// POSTURE (Level 1 categories)
// ========================================

MERGE (:BodyCue {name_en: 'Open Posture', name_ja: '開放姿勢', level: 1, domain: 'POSTURE'});
MERGE (:BodyCue {name_en: 'Closed Posture', name_ja: '閉鎖姿勢', level: 1, domain: 'POSTURE'});
MERGE (:BodyCue {name_en: 'Leaning Forward', name_ja: '前傾', level: 1, domain: 'POSTURE'});
MERGE (:BodyCue {name_en: 'Leaning Back', name_ja: '後傾', level: 1, domain: 'POSTURE'});
MERGE (:BodyCue {name_en: 'Slumped', name_ja: '肩が落ちた', level: 1, domain: 'POSTURE'});
MERGE (:BodyCue {name_en: 'Arms Akimbo', name_ja: '両手腰', level: 1, domain: 'POSTURE'});
MERGE (:BodyCue {name_en: 'Shrinking', name_ja: '身を縮める', level: 1, domain: 'POSTURE'});
MERGE (:BodyCue {name_en: 'Puffed Chest', name_ja: '胸を張る', level: 1, domain: 'POSTURE'});

// Level 2 - Specific posture examples
MERGE (:BodyCue {name_en: 'Chest Open, Shoulders Back', name_ja: '胸を開く', level: 2, parent: 'Open Posture'});
MERGE (:BodyCue {name_en: 'Arms Crossed, Torso Turned', name_ja: '腕組み＋体を逸らす', level: 2, parent: 'Closed Posture'});
MERGE (:BodyCue {name_en: 'Forward Incline & Head Tilt', name_ja: '前のめり＋首傾け', level: 2, parent: 'Leaning Forward'});
MERGE (:BodyCue {name_en: 'Chin Down, Shoulders Forward', name_ja: 'うつむき＋肩を前に', level: 2, parent: 'Slumped'});

// ========================================
// GESTURE (Level 1)
// ========================================

MERGE (:BodyCue {name_en: 'Clenched Fists', name_ja: '拳を握る', level: 1, domain: 'GESTURE'});
MERGE (:BodyCue {name_en: 'Open Palms', name_ja: '手のひらを見せる', level: 1, domain: 'GESTURE'});
MERGE (:BodyCue {name_en: 'Self-Hug', name_ja: '自分を抱く', level: 1, domain: 'GESTURE'});
MERGE (:BodyCue {name_en: 'Face Touching', name_ja: '顔に触れる', level: 1, domain: 'GESTURE'});
MERGE (:BodyCue {name_en: 'Finger Pointing', name_ja: '指差し', level: 1, domain: 'GESTURE'});
MERGE (:BodyCue {name_en: 'Covering Mouth', name_ja: '口を覆う', level: 1, domain: 'GESTURE'});
MERGE (:BodyCue {name_en: 'Hand on Heart', name_ja: '胸に手を当てる', level: 1, domain: 'GESTURE'});
MERGE (:BodyCue {name_en: 'Fidgeting', name_ja: 'そわそわ動く', level: 1, domain: 'GESTURE'});

// Additional Japanese gestures
MERGE (:BodyCue {name_en: 'Deep Bow', name_ja: '深いお辞儀', level: 1, domain: 'GESTURE'});
MERGE (:BodyCue {name_en: 'Face Averting', name_ja: '顔を背ける', level: 1, domain: 'GESTURE'});
MERGE (:BodyCue {name_en: 'Hand Wringing', name_ja: '手を揉む', level: 1, domain: 'GESTURE'});

// ========================================
// MOVEMENT EFFORT (Laban 8 Efforts) Level 1
// Based on Shafir et al., 2016 emotion-effort mappings
// ========================================

MERGE (:BodyCue {name_en: 'Punch', name_ja: 'パンチ', level: 1, domain: 'MOVEMENT_EFFORT'});
MERGE (:BodyCue {name_en: 'Slash', name_ja: 'スラッシュ', level: 1, domain: 'MOVEMENT_EFFORT'});
MERGE (:BodyCue {name_en: 'Press', name_ja: 'プレス', level: 1, domain: 'MOVEMENT_EFFORT'});
MERGE (:BodyCue {name_en: 'Wring', name_ja: 'リング', level: 1, domain: 'MOVEMENT_EFFORT'});
MERGE (:BodyCue {name_en: 'Flick', name_ja: 'フリック', level: 1, domain: 'MOVEMENT_EFFORT'});
MERGE (:BodyCue {name_en: 'Dab', name_ja: 'ダブ', level: 1, domain: 'MOVEMENT_EFFORT'});
MERGE (:BodyCue {name_en: 'Glide', name_ja: 'グライド', level: 1, domain: 'MOVEMENT_EFFORT'});
MERGE (:BodyCue {name_en: 'Float', name_ja: 'フロート', level: 1, domain: 'MOVEMENT_EFFORT'});

// ========================================
// PHYSIOLOGICAL (Level 1)
// ========================================

MERGE (:BodyCue {name_en: 'Sweating', name_ja: '発汗', level: 1, domain: 'PHYSIOLOGICAL'});
MERGE (:BodyCue {name_en: 'Rapid Heartbeat', name_ja: '心拍増加', level: 1, domain: 'PHYSIOLOGICAL'});
MERGE (:BodyCue {name_en: 'Pupil Dilation', name_ja: '瞳孔拡大', level: 1, domain: 'PHYSIOLOGICAL'});
MERGE (:BodyCue {name_en: 'Blushing', name_ja: '顔が赤くなる', level: 1, domain: 'PHYSIOLOGICAL'});
MERGE (:BodyCue {name_en: 'Trembling', name_ja: '震え', level: 1, domain: 'PHYSIOLOGICAL'});
MERGE (:BodyCue {name_en: 'Tears', name_ja: '涙', level: 1, domain: 'PHYSIOLOGICAL'});

// Additional physiological responses
MERGE (:BodyCue {name_en: 'Pallor', name_ja: '顔面蒼白', level: 1, domain: 'PHYSIOLOGICAL'});
MERGE (:BodyCue {name_en: 'Voice Tremor', name_ja: '声の震え', level: 1, domain: 'PHYSIOLOGICAL'});
MERGE (:BodyCue {name_en: 'Goosebumps', name_ja: '鳥肌', level: 1, domain: 'PHYSIOLOGICAL'});

// ========================================
// RELATIONSHIPS: BodyCue → Emotion
// strength: 0-1 (empirical confidence)
// ========================================

// First ensure core emotions exist
MATCH (anger:Emotion {name_en: 'ANGER'})
MATCH (fear:Emotion {name_en: 'FEAR'})
MATCH (sad:Emotion {name_en: 'SAD'})
MATCH (happy:Emotion {name_en: 'HAPPY'})
MATCH (disgust:Emotion {name_en: 'DISGUST'})
MATCH (surprise:Emotion {name_en: 'SURPRISE'})

// ---- POSTURE → EMOTION
MATCH (p1:BodyCue {name_en: 'Open Posture'})
MERGE (p1)-[:SUGGESTS {strength: 0.8}]->(happy);

MATCH (p2:BodyCue {name_en: 'Closed Posture'})
MERGE (p2)-[:SUGGESTS {strength: 0.7}]->(disgust);
MERGE (p2)-[:SUGGESTS {strength: 0.6}]->(fear);

MATCH (p3:BodyCue {name_en: 'Leaning Forward'})
MERGE (p3)-[:SUGGESTS {strength: 0.6}]->(happy);
MERGE (p3)-[:SUGGESTS {strength: 0.4}]->(anger);

MATCH (p5:BodyCue {name_en: 'Slumped'})
MERGE (p5)-[:SUGGESTS {strength: 0.8}]->(sad);

MATCH (p6:BodyCue {name_en: 'Arms Akimbo'})
MERGE (p6)-[:SUGGESTS {strength: 0.8}]->(anger);

MATCH (p7:BodyCue {name_en: 'Shrinking'})
MERGE (p7)-[:SUGGESTS {strength: 0.9}]->(fear);

MATCH (p8:BodyCue {name_en: 'Puffed Chest'})
MERGE (p8)-[:SUGGESTS {strength: 0.7}]->(happy);

// ---- GESTURE → EMOTION
MATCH (g1:BodyCue {name_en: 'Clenched Fists'})
MERGE (g1)-[:SUGGESTS {strength: 0.9}]->(anger);

MATCH (g2:BodyCue {name_en: 'Open Palms'})
MERGE (g2)-[:SUGGESTS {strength: 0.8}]->(happy);

MATCH (g3:BodyCue {name_en: 'Self-Hug'})
MERGE (g3)-[:SUGGESTS {strength: 0.8}]->(sad);
MERGE (g3)-[:SUGGESTS {strength: 0.6}]->(fear);

MATCH (g4:BodyCue {name_en: 'Face Touching'})
MERGE (g4)-[:SUGGESTS {strength: 0.6}]->(fear);

MATCH (g5:BodyCue {name_en: 'Finger Pointing'})
MERGE (g5)-[:SUGGESTS {strength: 0.7}]->(anger);

MATCH (g6:BodyCue {name_en: 'Covering Mouth'})
MERGE (g6)-[:SUGGESTS {strength: 0.7}]->(surprise);
MERGE (g6)-[:SUGGESTS {strength: 0.5}]->(fear);

MATCH (g7:BodyCue {name_en: 'Hand on Heart'})
MERGE (g7)-[:SUGGESTS {strength: 0.8}]->(happy);

MATCH (g8:BodyCue {name_en: 'Fidgeting'})
MERGE (g8)-[:SUGGESTS {strength: 0.7}]->(fear);

// ---- MOVEMENT EFFORT → EMOTION (Laban)
MATCH (e1:BodyCue {name_en: 'Punch'})
MERGE (e1)-[:SUGGESTS {strength: 0.9}]->(anger);

MATCH (e2:BodyCue {name_en: 'Slash'})
MERGE (e2)-[:SUGGESTS {strength: 0.8}]->(anger);

MATCH (e3:BodyCue {name_en: 'Press'})
MERGE (e3)-[:SUGGESTS {strength: 0.7}]->(happy);

MATCH (e4:BodyCue {name_en: 'Wring'})
MERGE (e4)-[:SUGGESTS {strength: 0.8}]->(sad);

MATCH (e5:BodyCue {name_en: 'Flick'})
MERGE (e5)-[:SUGGESTS {strength: 0.7}]->(surprise);

MATCH (e6:BodyCue {name_en: 'Dab'})
MERGE (e6)-[:SUGGESTS {strength: 0.7}]->(happy);

MATCH (e7:BodyCue {name_en: 'Glide'})
MERGE (e7)-[:SUGGESTS {strength: 0.8}]->(happy);

MATCH (e8:BodyCue {name_en: 'Float'})
MERGE (e8)-[:SUGGESTS {strength: 0.9}]->(happy);

// ---- PHYSIOLOGICAL → EMOTION
MATCH (v1:BodyCue {name_en: 'Sweating'})
MERGE (v1)-[:SUGGESTS {strength: 0.6}]->(fear);
MERGE (v1)-[:SUGGESTS {strength: 0.4}]->(anger);

MATCH (v2:BodyCue {name_en: 'Rapid Heartbeat'})
MERGE (v2)-[:SUGGESTS {strength: 0.6}]->(fear);
MERGE (v2)-[:SUGGESTS {strength: 0.5}]->(anger);

MATCH (v3:BodyCue {name_en: 'Pupil Dilation'})
MERGE (v3)-[:SUGGESTS {strength: 0.5}]->(surprise);
MERGE (v3)-[:SUGGESTS {strength: 0.4}]->(fear);

MATCH (v4:BodyCue {name_en: 'Blushing'})
MERGE (v4)-[:SUGGESTS {strength: 0.5}]->(happy);
MERGE (v4)-[:SUGGESTS {strength: 0.5}]->(sad);

MATCH (v5:BodyCue {name_en: 'Trembling'})
MERGE (v5)-[:SUGGESTS {strength: 0.7}]->(fear);
MERGE (v5)-[:SUGGESTS {strength: 0.5}]->(anger);

MATCH (v6:BodyCue {name_en: 'Tears'})
MERGE (v6)-[:SUGGESTS {strength: 0.9}]->(sad);
MERGE (v6)-[:SUGGESTS {strength: 0.3}]->(happy);

// Additional physiological mappings
MATCH (v7:BodyCue {name_en: 'Pallor'})
MERGE (v7)-[:SUGGESTS {strength: 0.8}]->(fear);

MATCH (v8:BodyCue {name_en: 'Voice Tremor'})
MERGE (v8)-[:SUGGESTS {strength: 0.7}]->(fear);
MERGE (v8)-[:SUGGESTS {strength: 0.6}]->(sad);

// ========================================
// INDEXES
// ========================================

CREATE INDEX bodycue_name_en IF NOT EXISTS FOR (b:BodyCue) ON (b.name_en);
CREATE INDEX bodycue_domain IF NOT EXISTS FOR (b:BodyCue) ON (b.domain);
CREATE INDEX bodycue_level IF NOT EXISTS FOR (b:BodyCue) ON (b.level);
CREATE INDEX suggests_strength IF NOT EXISTS FOR ()-[r:SUGGESTS]-() ON (r.strength);

// ========================================
// VERIFICATION QUERY
// ========================================
// Example: Find emotions suggested by "Clenched Fists" gesture
// MATCH (:BodyCue {name_en: 'Clenched Fists'})-[:SUGGESTS]->(e:Emotion)
// RETURN e.name_en, e.name_ja, e.level;

// ========================================
// REFERENCES
// ========================================
// - Shafir et al. (2016). Emotion regulation through movement: Laban movement analysis
// - Ross & Flack (2017). Body postures and recognition of discrete emotions
// - Romanczyk & Gillis (2006). Physiological indicators of arousal
// - Additional body language research from psychology literature