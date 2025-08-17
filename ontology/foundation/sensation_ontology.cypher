// LNA-ES v3.0 Sensation Ontology - Complete Sensory Experience System
// Covering all five senses and complex perceptual experiences
// Designed for Japanese literary and aesthetic analysis

// ========================================
// CORE SENSORY MODALITIES (Level 0)
// ========================================

MERGE (:Sensation {name_en: 'VISUAL', name_ja: '視覚', level: 0, core: true})
MERGE (:Sensation {name_en: 'AUDITORY', name_ja: '聴覚', level: 0, core: true})
MERGE (:Sensation {name_en: 'TACTILE', name_ja: '触覚', level: 0, core: true})
MERGE (:Sensation {name_en: 'GUSTATORY', name_ja: '味覚', level: 0, core: true})
MERGE (:Sensation {name_en: 'OLFACTORY', name_ja: '嗅覚', level: 0, core: true})
MERGE (:Sensation {name_en: 'KINESTHETIC', name_ja: '運動感覚', level: 0, core: true});

// ========================================
// VISUAL SENSATIONS
// ========================================

// Level 1 - Categories
MERGE (:Sensation {name_en: 'Light Quality', name_ja: '光の質', level: 1})
MERGE (:Sensation {name_en: 'Color Perception', name_ja: '色の知覚', level: 1})
MERGE (:Sensation {name_en: 'Movement Visual', name_ja: '視覚的動き', level: 1})
MERGE (:Sensation {name_en: 'Depth Perception', name_ja: '奥行き知覚', level: 1})
MERGE (:Sensation {name_en: 'Pattern Recognition', name_ja: 'パターン認識', level: 1})
MERGE (:Sensation {name_en: 'Visual Texture', name_ja: '視覚的質感', level: 1});

// Level 2 - Specific Visual Experiences
// Light Quality
MERGE (:Sensation {name_en: 'Bright', name_ja: '明るい', level: 2})
MERGE (:Sensation {name_en: 'Dim', name_ja: '薄暗い', level: 2})
MERGE (:Sensation {name_en: 'Glowing', name_ja: '輝く', level: 2})
MERGE (:Sensation {name_en: 'Sparkling', name_ja: 'きらめく', level: 2})
MERGE (:Sensation {name_en: 'Shadowy', name_ja: '影がある', level: 2})
MERGE (:Sensation {name_en: 'Dazzling', name_ja: 'まばゆい', level: 2});

// Color Perception
MERGE (:Sensation {name_en: 'Vivid Colors', name_ja: '鮮やかな色', level: 2})
MERGE (:Sensation {name_en: 'Muted Tones', name_ja: '落ち着いた色調', level: 2})
MERGE (:Sensation {name_en: 'Warm Hues', name_ja: '暖色', level: 2})
MERGE (:Sensation {name_en: 'Cool Tones', name_ja: '寒色', level: 2})
MERGE (:Sensation {name_en: 'Transparent', name_ja: '透明な', level: 2})
MERGE (:Sensation {name_en: 'Opaque', name_ja: '不透明な', level: 2});

// Visual Movement
MERGE (:Sensation {name_en: 'Flowing', name_ja: '流れる', level: 2})
MERGE (:Sensation {name_en: 'Swaying', name_ja: '揺れる', level: 2})
MERGE (:Sensation {name_en: 'Fluttering', name_ja: 'ひらひら', level: 2})
MERGE (:Sensation {name_en: 'Spinning', name_ja: '回転する', level: 2})
MERGE (:Sensation {name_en: 'Wavering', name_ja: 'ゆらめく', level: 2});

// ========================================
// AUDITORY SENSATIONS
// ========================================

// Level 1 - Categories
MERGE (:Sensation {name_en: 'Sound Volume', name_ja: '音量', level: 1})
MERGE (:Sensation {name_en: 'Sound Pitch', name_ja: '音の高さ', level: 1})
MERGE (:Sensation {name_en: 'Sound Texture', name_ja: '音の質感', level: 1})
MERGE (:Sensation {name_en: 'Musical Quality', name_ja: '音楽的質', level: 1})
MERGE (:Sensation {name_en: 'Natural Sounds', name_ja: '自然音', level: 1})
MERGE (:Sensation {name_en: 'Rhythmic Pattern', name_ja: 'リズムパターン', level: 1});

// Level 2 - Specific Auditory Experiences
// Sound Volume
MERGE (:Sensation {name_en: 'Loud', name_ja: '大きい', level: 2})
MERGE (:Sensation {name_en: 'Quiet', name_ja: '静かな', level: 2})
MERGE (:Sensation {name_en: 'Whisper', name_ja: 'ささやき', level: 2})
MERGE (:Sensation {name_en: 'Thunderous', name_ja: '雷鳴のような', level: 2})
MERGE (:Sensation {name_en: 'Gentle', name_ja: '優しい', level: 2});

// Sound Pitch  
MERGE (:Sensation {name_en: 'High Pitched', name_ja: '高い音', level: 2})
MERGE (:Sensation {name_en: 'Low Pitched', name_ja: '低い音', level: 2})
MERGE (:Sensation {name_en: 'Shrill', name_ja: '甲高い', level: 2})
MERGE (:Sensation {name_en: 'Deep', name_ja: '深い音', level: 2});

// Sound Texture
MERGE (:Sensation {name_en: 'Smooth Sound', name_ja: 'なめらかな音', level: 2})
MERGE (:Sensation {name_en: 'Rough Sound', name_ja: 'ざらざらした音', level: 2})
MERGE (:Sensation {name_en: 'Clear Tone', name_ja: '澄んだ音', level: 2})
MERGE (:Sensation {name_en: 'Muffled', name_ja: 'こもった音', level: 2})
MERGE (:Sensation {name_en: 'Resonant', name_ja: '響く', level: 2})
MERGE (:Sensation {name_en: 'Hollow', name_ja: '空洞的な', level: 2});

// Natural Sounds
MERGE (:Sensation {name_en: 'Wind Sound', name_ja: '風の音', level: 2})
MERGE (:Sensation {name_en: 'Water Flowing', name_ja: '水の流れ', level: 2})
MERGE (:Sensation {name_en: 'Bird Song', name_ja: '鳥のさえずり', level: 2})
MERGE (:Sensation {name_en: 'Rustling Leaves', name_ja: '葉のささやき', level: 2});

// ========================================
// TACTILE SENSATIONS
// ========================================

// Level 1 - Categories
MERGE (:Sensation {name_en: 'Surface Texture', name_ja: '表面の質感', level: 1})
MERGE (:Sensation {name_en: 'Temperature', name_ja: '温度', level: 1})
MERGE (:Sensation {name_en: 'Pressure', name_ja: '圧力', level: 1})
MERGE (:Sensation {name_en: 'Vibration', name_ja: '振動', level: 1})
MERGE (:Sensation {name_en: 'Pain Sensation', name_ja: '痛覚', level: 1})
MERGE (:Sensation {name_en: 'Comfort', name_ja: '快適感', level: 1});

// Level 2 - Specific Tactile Experiences
// Surface Texture
MERGE (:Sensation {name_en: 'Smooth', name_ja: 'なめらか', level: 2})
MERGE (:Sensation {name_en: 'Rough', name_ja: 'ざらざら', level: 2})
MERGE (:Sensation {name_en: 'Soft', name_ja: '柔らかい', level: 2})
MERGE (:Sensation {name_en: 'Hard', name_ja: '硬い', level: 2})
MERGE (:Sensation {name_en: 'Sticky', name_ja: 'べたべた', level: 2})
MERGE (:Sensation {name_en: 'Slippery', name_ja: 'つるつる', level: 2})
MERGE (:Sensation {name_en: 'Fuzzy', name_ja: 'ふわふわ', level: 2})
MERGE (:Sensation {name_en: 'Grainy', name_ja: 'ざらめ状', level: 2});

// Temperature
MERGE (:Sensation {name_en: 'Hot', name_ja: '熱い', level: 2})
MERGE (:Sensation {name_en: 'Warm', name_ja: '暖かい', level: 2})
MERGE (:Sensation {name_en: 'Cool', name_ja: '涼しい', level: 2})
MERGE (:Sensation {name_en: 'Cold', name_ja: '冷たい', level: 2})
MERGE (:Sensation {name_en: 'Burning', name_ja: '火傷するような', level: 2})
MERGE (:Sensation {name_en: 'Freezing', name_ja: '凍るような', level: 2});

// Pressure
MERGE (:Sensation {name_en: 'Light Touch', name_ja: '軽いタッチ', level: 2})
MERGE (:Sensation {name_en: 'Firm Pressure', name_ja: 'しっかりした圧力', level: 2})
MERGE (:Sensation {name_en: 'Gentle Caress', name_ja: '優しい愛撫', level: 2})
MERGE (:Sensation {name_en: 'Tight Grip', name_ja: 'きつい握り', level: 2});

// ========================================
// GUSTATORY SENSATIONS
// ========================================

// Level 1 - Categories  
MERGE (:Sensation {name_en: 'Basic Tastes', name_ja: '基本味', level: 1})
MERGE (:Sensation {name_en: 'Complex Flavors', name_ja: '複雑な風味', level: 1})
MERGE (:Sensation {name_en: 'Taste Intensity', name_ja: '味の強さ', level: 1})
MERGE (:Sensation {name_en: 'Aftertaste', name_ja: '後味', level: 1});

// Level 2 - Specific Gustatory Experiences
// Basic Tastes
MERGE (:Sensation {name_en: 'Sweet', name_ja: '甘い', level: 2})
MERGE (:Sensation {name_en: 'Sour', name_ja: '酸っぱい', level: 2})
MERGE (:Sensation {name_en: 'Salty', name_ja: '塩辛い', level: 2})
MERGE (:Sensation {name_en: 'Bitter', name_ja: '苦い', level: 2})
MERGE (:Sensation {name_en: 'Umami', name_ja: 'うま味', level: 2})
MERGE (:Sensation {name_en: 'Spicy', name_ja: '辛い', level: 2});

// Complex Flavors
MERGE (:Sensation {name_en: 'Rich Flavor', name_ja: '濃厚な味', level: 2})
MERGE (:Sensation {name_en: 'Delicate Taste', name_ja: '繊細な味', level: 2})
MERGE (:Sensation {name_en: 'Refreshing', name_ja: 'さっぱり', level: 2})
MERGE (:Sensation {name_en: 'Aromatic', name_ja: '香ばしい', level: 2})
MERGE (:Sensation {name_en: 'Astringent', name_ja: '渋い', level: 2});

// ========================================
// OLFACTORY SENSATIONS
// ========================================

// Level 1 - Categories
MERGE (:Sensation {name_en: 'Natural Scents', name_ja: '自然の香り', level: 1})
MERGE (:Sensation {name_en: 'Artificial Fragrances', name_ja: '人工的な香り', level: 1})
MERGE (:Sensation {name_en: 'Food Aromas', name_ja: '食べ物の香り', level: 1})
MERGE (:Sensation {name_en: 'Scent Intensity', name_ja: '香りの強さ', level: 1});

// Level 2 - Specific Olfactory Experiences
// Natural Scents
MERGE (:Sensation {name_en: 'Floral', name_ja: '花の香り', level: 2})
MERGE (:Sensation {name_en: 'Woody', name_ja: '木の香り', level: 2})
MERGE (:Sensation {name_en: 'Ocean Breeze', name_ja: '海風', level: 2})
MERGE (:Sensation {name_en: 'Forest Fresh', name_ja: '森林の香り', level: 2})
MERGE (:Sensation {name_en: 'Rain Scent', name_ja: '雨の匂い', level: 2});

// Food Aromas
MERGE (:Sensation {name_en: 'Savory', name_ja: '香ばしい', level: 2})
MERGE (:Sensation {name_en: 'Sweet Aroma', name_ja: '甘い香り', level: 2})
MERGE (:Sensation {name_en: 'Spice Fragrance', name_ja: 'スパイスの香り', level: 2})
MERGE (:Sensation {name_en: 'Fresh Herbs', name_ja: 'ハーブの香り', level: 2});

// ========================================
// KINESTHETIC SENSATIONS
// ========================================

// Level 1 - Categories
MERGE (:Sensation {name_en: 'Body Position', name_ja: '身体位置', level: 1})
MERGE (:Sensation {name_en: 'Movement Quality', name_ja: '動きの質', level: 1})
MERGE (:Sensation {name_en: 'Balance', name_ja: 'バランス', level: 1})
MERGE (:Sensation {name_en: 'Effort', name_ja: '努力感', level: 1});

// Level 2 - Specific Kinesthetic Experiences
// Movement Quality
MERGE (:Sensation {name_en: 'Graceful', name_ja: '優雅な', level: 2})
MERGE (:Sensation {name_en: 'Clumsy', name_ja: 'ぎこちない', level: 2})
MERGE (:Sensation {name_en: 'Fluid Motion', name_ja: '流れるような', level: 2})
MERGE (:Sensation {name_en: 'Jerky Movement', name_ja: 'ぎくしゃく', level: 2})
MERGE (:Sensation {name_en: 'Rhythmic', name_ja: 'リズミカル', level: 2});

// Balance
MERGE (:Sensation {name_en: 'Stable', name_ja: '安定した', level: 2})
MERGE (:Sensation {name_en: 'Unsteady', name_ja: '不安定な', level: 2})
MERGE (:Sensation {name_en: 'Centered', name_ja: '中心の取れた', level: 2})
MERGE (:Sensation {name_en: 'Off-Balance', name_ja: 'バランスを崩した', level: 2});

// ========================================
// JAPANESE-SPECIFIC SENSORY CONCEPTS
// ========================================

// Level 2 - Cultural Sensory Experiences
MERGE (:Sensation {name_en: 'Sabi (Rustic Beauty)', name_ja: '寂', level: 2, cultural: 'japanese'})
MERGE (:Sensation {name_en: 'Wabi (Humble Simplicity)', name_ja: '侘', level: 2, cultural: 'japanese'})
MERGE (:Sensation {name_en: 'Mono no Aware (Pathos)', name_ja: 'もののあはれ', level: 2, cultural: 'japanese'})
MERGE (:Sensation {name_en: 'Shibui (Subtle Refinement)', name_ja: '渋い', level: 2, cultural: 'japanese'})
MERGE (:Sensation {name_en: 'Ikigai (Life Purpose Feel)', name_ja: '生きがい', level: 2, cultural: 'japanese'});

// ========================================
// SYNESTHETIC EXPERIENCES
// ========================================

// Level 2 - Cross-Sensory Experiences
MERGE (:Sensation {name_en: 'Color-Sound', name_ja: '色音感覚', level: 2, type: 'synesthetic'})
MERGE (:Sensation {name_en: 'Texture-Taste', name_ja: '質感味覚', level: 2, type: 'synesthetic'})
MERGE (:Sensation {name_en: 'Movement-Music', name_ja: '動き音楽感覚', level: 2, type: 'synesthetic'})
MERGE (:Sensation {name_en: 'Temperature-Emotion', name_ja: '温度感情', level: 2, type: 'synesthetic'});

// ========================================
// Create indexes for better performance
// ========================================

CREATE INDEX sensation_name_en IF NOT EXISTS FOR (s:Sensation) ON (s.name_en);
CREATE INDEX sensation_level IF NOT EXISTS FOR (s:Sensation) ON (s.level);
CREATE INDEX sensation_core IF NOT EXISTS FOR (s:Sensation) ON (s.core);
CREATE INDEX sensation_cultural IF NOT EXISTS FOR (s:Sensation) ON (s.cultural);
CREATE INDEX sensation_type IF NOT EXISTS FOR (s:Sensation) ON (s.type);

// ========================================
// Create hierarchical relationships
// ========================================

// VISUAL hierarchy
MATCH (core:Sensation {name_en: 'VISUAL'})
MATCH (light:Sensation {name_en: 'Light Quality'})
MATCH (color:Sensation {name_en: 'Color Perception'})
MATCH (movement:Sensation {name_en: 'Movement Visual'})
MATCH (depth:Sensation {name_en: 'Depth Perception'})
MATCH (pattern:Sensation {name_en: 'Pattern Recognition'})
MATCH (texture:Sensation {name_en: 'Visual Texture'})
MERGE (core)-[:CONTAINS]->(light)
MERGE (core)-[:CONTAINS]->(color)
MERGE (core)-[:CONTAINS]->(movement)
MERGE (core)-[:CONTAINS]->(depth)
MERGE (core)-[:CONTAINS]->(pattern)
MERGE (core)-[:CONTAINS]->(texture);

// AUDITORY hierarchy
MATCH (core:Sensation {name_en: 'AUDITORY'})
MATCH (volume:Sensation {name_en: 'Sound Volume'})
MATCH (pitch:Sensation {name_en: 'Sound Pitch'})
MATCH (sound_texture:Sensation {name_en: 'Sound Texture'})
MATCH (musical:Sensation {name_en: 'Musical Quality'})
MATCH (natural:Sensation {name_en: 'Natural Sounds'})
MATCH (rhythm:Sensation {name_en: 'Rhythmic Pattern'})
MERGE (core)-[:CONTAINS]->(volume)
MERGE (core)-[:CONTAINS]->(pitch)
MERGE (core)-[:CONTAINS]->(sound_texture)
MERGE (core)-[:CONTAINS]->(musical)
MERGE (core)-[:CONTAINS]->(natural)
MERGE (core)-[:CONTAINS]->(rhythm);

// TACTILE hierarchy
MATCH (core:Sensation {name_en: 'TACTILE'})
MATCH (surface:Sensation {name_en: 'Surface Texture'})
MATCH (temp:Sensation {name_en: 'Temperature'})
MATCH (pressure:Sensation {name_en: 'Pressure'})
MATCH (vibration:Sensation {name_en: 'Vibration'})
MATCH (pain:Sensation {name_en: 'Pain Sensation'})
MATCH (comfort:Sensation {name_en: 'Comfort'})
MERGE (core)-[:CONTAINS]->(surface)
MERGE (core)-[:CONTAINS]->(temp)
MERGE (core)-[:CONTAINS]->(pressure)
MERGE (core)-[:CONTAINS]->(vibration)
MERGE (core)-[:CONTAINS]->(pain)
MERGE (core)-[:CONTAINS]->(comfort);

// Add level 2 relationships for visual light quality
MATCH (light:Sensation {name_en: 'Light Quality'})
MATCH (bright:Sensation {name_en: 'Bright'})
MATCH (dim:Sensation {name_en: 'Dim'})
MATCH (glowing:Sensation {name_en: 'Glowing'})
MATCH (sparkling:Sensation {name_en: 'Sparkling'})
MERGE (light)-[:CONTAINS]->(bright)
MERGE (light)-[:CONTAINS]->(dim)
MERGE (light)-[:CONTAINS]->(glowing)
MERGE (light)-[:CONTAINS]->(sparkling);

// ========================================
// Verification Query
// ========================================
// Run this to verify node creation:
// MATCH (s:Sensation) RETURN s.level, count(s) ORDER BY s.level;