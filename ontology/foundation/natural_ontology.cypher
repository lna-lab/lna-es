// LNA-ES v3.0 Natural Ontology - Comprehensive Nature System  
// Covering natural phenomena, seasons, weather, and ecosystem concepts
// Enhanced with Japanese nature appreciation (四季, 自然観)

// ========================================
// CORE NATURAL DOMAINS (Level 0)
// ========================================

MERGE (:Natural {name_en: 'SEASONS', name_ja: '季節', level: 0, core: true})
MERGE (:Natural {name_en: 'WEATHER', name_ja: '天候', level: 0, core: true})
MERGE (:Natural {name_en: 'CELESTIAL', name_ja: '天体', level: 0, core: true})
MERGE (:Natural {name_en: 'LANDSCAPE', name_ja: '風景', level: 0, core: true})
MERGE (:Natural {name_en: 'FLORA', name_ja: '植物', level: 0, core: true})
MERGE (:Natural {name_en: 'FAUNA', name_ja: '動物', level: 0, core: true})
MERGE (:Natural {name_en: 'ELEMENTS', name_ja: '自然要素', level: 0, core: true});

// ========================================
// SEASONS (四季 - SHIKI)
// ========================================

// Level 1 - Four Seasons
MERGE (:Natural {name_en: 'Spring', name_ja: '春', level: 1})
MERGE (:Natural {name_en: 'Summer', name_ja: '夏', level: 1})
MERGE (:Natural {name_en: 'Autumn', name_ja: '秋', level: 1})
MERGE (:Natural {name_en: 'Winter', name_ja: '冬', level: 1})
MERGE (:Natural {name_en: 'Seasonal Transition', name_ja: '季節の変わり目', level: 1});

// Level 2 - Spring (春) Specifics
MERGE (:Natural {name_en: 'Cherry Blossoms', name_ja: '桜', level: 2})
MERGE (:Natural {name_en: 'New Growth', name_ja: '新緑', level: 2})
MERGE (:Natural {name_en: 'Spring Rain', name_ja: '春雨', level: 2})
MERGE (:Natural {name_en: 'Warm Breeze', name_ja: '春風', level: 2})
MERGE (:Natural {name_en: 'Budding Trees', name_ja: '若葉', level: 2})
MERGE (:Natural {name_en: 'Plum Blossoms', name_ja: '梅', level: 2})
MERGE (:Natural {name_en: 'Morning Mist', name_ja: '春霞', level: 2});

// Level 2 - Summer (夏) Specifics  
MERGE (:Natural {name_en: 'Intense Heat', name_ja: '炎暑', level: 2})
MERGE (:Natural {name_en: 'Cicada Song', name_ja: '蝉の声', level: 2})
MERGE (:Natural {name_en: 'Thunderstorm', name_ja: '夕立', level: 2})
MERGE (:Natural {name_en: 'Lush Greenery', name_ja: '青葉', level: 2})
MERGE (:Natural {name_en: 'Ocean Waves', name_ja: '海の波', level: 2})
MERGE (:Natural {name_en: 'Fireworks', name_ja: '花火', level: 2})
MERGE (:Natural {name_en: 'Bamboo Forest', name_ja: '竹林', level: 2});

// Level 2 - Autumn (秋) Specifics
MERGE (:Natural {name_en: 'Falling Leaves', name_ja: '落ち葉', level: 2})
MERGE (:Natural {name_en: 'Harvest Moon', name_ja: '満月', level: 2})
MERGE (:Natural {name_en: 'Crimson Maple', name_ja: '紅葉', level: 2})
MERGE (:Natural {name_en: 'Cool Wind', name_ja: '涼風', level: 2})
MERGE (:Natural {name_en: 'Persimmon Tree', name_ja: '柿の木', level: 2})
MERGE (:Natural {name_en: 'Migrating Birds', name_ja: '渡り鳥', level: 2})
MERGE (:Natural {name_en: 'Morning Frost', name_ja: '朝霜', level: 2});

// Level 2 - Winter (冬) Specifics
MERGE (:Natural {name_en: 'Snow Fall', name_ja: '雪', level: 2})
MERGE (:Natural {name_en: 'Bare Trees', name_ja: '枯れ木', level: 2})
MERGE (:Natural {name_en: 'Frozen Stream', name_ja: '氷河', level: 2})
MERGE (:Natural {name_en: 'North Wind', name_ja: '北風', level: 2})
MERGE (:Natural {name_en: 'Evergreen Pine', name_ja: '松', level: 2})
MERGE (:Natural {name_en: 'Winter Solstice', name_ja: '冬至', level: 2})
MERGE (:Natural {name_en: 'Silent Forest', name_ja: '静寂の森', level: 2});

// ========================================
// WEATHER (天候)
// ========================================

// Level 1 - Weather Categories
MERGE (:Natural {name_en: 'Precipitation', name_ja: '降水', level: 1})
MERGE (:Natural {name_en: 'Wind Patterns', name_ja: '風向', level: 1})
MERGE (:Natural {name_en: 'Cloud Formation', name_ja: '雲の形成', level: 1})
MERGE (:Natural {name_en: 'Atmospheric Pressure', name_ja: '気圧', level: 1})
MERGE (:Natural {name_en: 'Temperature Change', name_ja: '気温変化', level: 1});

// Level 2 - Precipitation Types
MERGE (:Natural {name_en: 'Gentle Rain', name_ja: '小雨', level: 2})
MERGE (:Natural {name_en: 'Heavy Downpour', name_ja: '大雨', level: 2})
MERGE (:Natural {name_en: 'Drizzle', name_ja: '霧雨', level: 2})
MERGE (:Natural {name_en: 'Snow Flurries', name_ja: '粉雪', level: 2})
MERGE (:Natural {name_en: 'Hail Storm', name_ja: '雹', level: 2})
MERGE (:Natural {name_en: 'Morning Dew', name_ja: '朝露', level: 2});

// Level 2 - Wind Types
MERGE (:Natural {name_en: 'Gentle Breeze', name_ja: 'そよ風', level: 2})
MERGE (:Natural {name_en: 'Strong Gale', name_ja: '強風', level: 2})
MERGE (:Natural {name_en: 'Typhoon Wind', name_ja: '台風', level: 2})
MERGE (:Natural {name_en: 'Mountain Wind', name_ja: '山風', level: 2})
MERGE (:Natural {name_en: 'Sea Breeze', name_ja: '海風', level: 2});

// ========================================
// CELESTIAL (天体)
// ========================================

// Level 1 - Celestial Bodies
MERGE (:Natural {name_en: 'Sun', name_ja: '太陽', level: 1})
MERGE (:Natural {name_en: 'Moon', name_ja: '月', level: 1})
MERGE (:Natural {name_en: 'Stars', name_ja: '星', level: 1})
MERGE (:Natural {name_en: 'Planets', name_ja: '惑星', level: 1})
MERGE (:Natural {name_en: 'Sky Phenomena', name_ja: '空の現象', level: 1});

// Level 2 - Solar Phenomena
MERGE (:Natural {name_en: 'Sunrise', name_ja: '日の出', level: 2})
MERGE (:Natural {name_en: 'Sunset', name_ja: '日没', level: 2})
MERGE (:Natural {name_en: 'Noon Sun', name_ja: '真昼の太陽', level: 2})
MERGE (:Natural {name_en: 'Solar Eclipse', name_ja: '日食', level: 2})
MERGE (:Natural {name_en: 'Sun Rays', name_ja: '日光', level: 2});

// Level 2 - Lunar Phenomena
MERGE (:Natural {name_en: 'Full Moon', name_ja: '満月', level: 2})
MERGE (:Natural {name_en: 'New Moon', name_ja: '新月', level: 2})
MERGE (:Natural {name_en: 'Crescent Moon', name_ja: '三日月', level: 2})
MERGE (:Natural {name_en: 'Lunar Eclipse', name_ja: '月食', level: 2})
MERGE (:Natural {name_en: 'Moonlight', name_ja: '月光', level: 2});

// Level 2 - Stellar Phenomena
MERGE (:Natural {name_en: 'Milky Way', name_ja: '天の川', level: 2})
MERGE (:Natural {name_en: 'Shooting Star', name_ja: '流れ星', level: 2})
MERGE (:Natural {name_en: 'Constellation', name_ja: '星座', level: 2})
MERGE (:Natural {name_en: 'Starry Night', name_ja: '星空', level: 2});

// ========================================
// LANDSCAPE (風景)
// ========================================

// Level 1 - Terrain Types
MERGE (:Natural {name_en: 'Mountains', name_ja: '山', level: 1})
MERGE (:Natural {name_en: 'Valleys', name_ja: '谷', level: 1})
MERGE (:Natural {name_en: 'Rivers', name_ja: '川', level: 1})
MERGE (:Natural {name_en: 'Lakes', name_ja: '湖', level: 1})
MERGE (:Natural {name_en: 'Forests', name_ja: '森', level: 1})
MERGE (:Natural {name_en: 'Plains', name_ja: '平原', level: 1})
MERGE (:Natural {name_en: 'Coastlines', name_ja: '海岸', level: 1});

// Level 2 - Mountain Features
MERGE (:Natural {name_en: 'Mountain Peak', name_ja: '山頂', level: 2})
MERGE (:Natural {name_en: 'Mountain Pass', name_ja: '峠', level: 2})
MERGE (:Natural {name_en: 'Rocky Cliff', name_ja: '断崖', level: 2})
MERGE (:Natural {name_en: 'Mountain Stream', name_ja: '山の小川', level: 2})
MERGE (:Natural {name_en: 'Alpine Meadow', name_ja: '高原', level: 2});

// Level 2 - Water Features
MERGE (:Natural {name_en: 'Waterfall', name_ja: '滝', level: 2})
MERGE (:Natural {name_en: 'Rapids', name_ja: '急流', level: 2})
MERGE (:Natural {name_en: 'Still Pond', name_ja: '静かな池', level: 2})
MERGE (:Natural {name_en: 'River Delta', name_ja: '河口', level: 2})
MERGE (:Natural {name_en: 'Hot Spring', name_ja: '温泉', level: 2});

// ========================================
// FLORA (植物)
// ========================================

// Level 1 - Plant Categories
MERGE (:Natural {name_en: 'Trees', name_ja: '木', level: 1})
MERGE (:Natural {name_en: 'Flowers', name_ja: '花', level: 1})
MERGE (:Natural {name_en: 'Grasses', name_ja: '草', level: 1})
MERGE (:Natural {name_en: 'Mosses', name_ja: '苔', level: 1})
MERGE (:Natural {name_en: 'Vines', name_ja: '蔦', level: 1})
MERGE (:Natural {name_en: 'Shrubs', name_ja: '低木', level: 1});

// Level 2 - Specific Trees
MERGE (:Natural {name_en: 'Cherry Tree', name_ja: '桜の木', level: 2})
MERGE (:Natural {name_en: 'Pine Tree', name_ja: '松の木', level: 2})
MERGE (:Natural {name_en: 'Bamboo Grove', name_ja: '竹やぶ', level: 2})
MERGE (:Natural {name_en: 'Maple Tree', name_ja: 'もみじ', level: 2})
MERGE (:Natural {name_en: 'Willow Tree', name_ja: '柳', level: 2})
MERGE (:Natural {name_en: 'Cedar Tree', name_ja: '杉', level: 2});

// Level 2 - Specific Flowers
MERGE (:Natural {name_en: 'Iris Flower', name_ja: 'あやめ', level: 2})
MERGE (:Natural {name_en: 'Chrysanthemum', name_ja: '菊', level: 2})
MERGE (:Natural {name_en: 'Lotus Blossom', name_ja: '蓮の花', level: 2})
MERGE (:Natural {name_en: 'Morning Glory', name_ja: '朝顔', level: 2})
MERGE (:Natural {name_en: 'Camellia', name_ja: '椿', level: 2});

// ========================================
// FAUNA (動物)
// ========================================

// Level 1 - Animal Categories
MERGE (:Natural {name_en: 'Birds', name_ja: '鳥', level: 1})
MERGE (:Natural {name_en: 'Mammals', name_ja: '哺乳類', level: 1})
MERGE (:Natural {name_en: 'Insects', name_ja: '昆虫', level: 1})
MERGE (:Natural {name_en: 'Fish', name_ja: '魚', level: 1})
MERGE (:Natural {name_en: 'Reptiles', name_ja: '爬虫類', level: 1})
MERGE (:Natural {name_en: 'Amphibians', name_ja: '両生類', level: 1});

// Level 2 - Specific Birds
MERGE (:Natural {name_en: 'Crane', name_ja: '鶴', level: 2})
MERGE (:Natural {name_en: 'Sparrow', name_ja: 'すずめ', level: 2})
MERGE (:Natural {name_en: 'Swallow', name_ja: 'つばめ', level: 2})
MERGE (:Natural {name_en: 'Nightingale', name_ja: 'うぐいす', level: 2})
MERGE (:Natural {name_en: 'Hawk', name_ja: '鷹', level: 2});

// Level 2 - Specific Mammals
MERGE (:Natural {name_en: 'Deer', name_ja: '鹿', level: 2})
MERGE (:Natural {name_en: 'Fox', name_ja: '狐', level: 2})
MERGE (:Natural {name_en: 'Bear', name_ja: '熊', level: 2})
MERGE (:Natural {name_en: 'Rabbit', name_ja: 'うさぎ', level: 2})
MERGE (:Natural {name_en: 'Wild Boar', name_ja: '猪', level: 2});

// Level 2 - Specific Insects
MERGE (:Natural {name_en: 'Cicada', name_ja: '蝉', level: 2})
MERGE (:Natural {name_en: 'Butterfly', name_ja: '蝶', level: 2})
MERGE (:Natural {name_en: 'Dragonfly', name_ja: 'とんぼ', level: 2})
MERGE (:Natural {name_en: 'Cricket', name_ja: 'こおろぎ', level: 2})
MERGE (:Natural {name_en: 'Firefly', name_ja: 'ほたる', level: 2});

// ========================================
// ELEMENTS (自然要素)
// ========================================

// Level 1 - Classical Elements
MERGE (:Natural {name_en: 'Fire', name_ja: '火', level: 1})
MERGE (:Natural {name_en: 'Water', name_ja: '水', level: 1})
MERGE (:Natural {name_en: 'Earth', name_ja: '土', level: 1})
MERGE (:Natural {name_en: 'Air', name_ja: '風', level: 1})
MERGE (:Natural {name_en: 'Wood', name_ja: '木', level: 1})
MERGE (:Natural {name_en: 'Metal', name_ja: '金', level: 1});

// Level 2 - Element Manifestations
// Fire manifestations
MERGE (:Natural {name_en: 'Lightning', name_ja: '稲妻', level: 2})
MERGE (:Natural {name_en: 'Wildfire', name_ja: '山火事', level: 2})
MERGE (:Natural {name_en: 'Volcano', name_ja: '火山', level: 2})
MERGE (:Natural {name_en: 'Sunlight', name_ja: '太陽光', level: 2});

// Water manifestations
MERGE (:Natural {name_en: 'Ocean', name_ja: '大海', level: 2})
MERGE (:Natural {name_en: 'Stream', name_ja: '小川', level: 2})
MERGE (:Natural {name_en: 'Mist', name_ja: '霧', level: 2})
MERGE (:Natural {name_en: 'Ice', name_ja: '氷', level: 2});

// Earth manifestations  
MERGE (:Natural {name_en: 'Rock', name_ja: '岩', level: 2})
MERGE (:Natural {name_en: 'Sand', name_ja: '砂', level: 2})
MERGE (:Natural {name_en: 'Clay', name_ja: '粘土', level: 2})
MERGE (:Natural {name_en: 'Crystal', name_ja: '水晶', level: 2});

// ========================================
// JAPANESE NATURE CONCEPTS
// ========================================

// Level 2 - Cultural Nature Appreciation
MERGE (:Natural {name_en: 'Mono no Aware', name_ja: 'もののあはれ', level: 2, cultural: 'japanese'})
MERGE (:Natural {name_en: 'Wabi-Sabi', name_ja: '侘寂', level: 2, cultural: 'japanese'})
MERGE (:Natural {name_en: 'Shinrin-yoku', name_ja: '森林浴', level: 2, cultural: 'japanese'})
MERGE (:Natural {name_en: 'Hanami', name_ja: '花見', level: 2, cultural: 'japanese'})
MERGE (:Natural {name_en: 'Tsukimi', name_ja: '月見', level: 2, cultural: 'japanese'})
MERGE (:Natural {name_en: 'Yukimi', name_ja: '雪見', level: 2, cultural: 'japanese'});

// ========================================
// Create indexes for better performance
// ========================================

CREATE INDEX natural_name_en IF NOT EXISTS FOR (n:Natural) ON (n.name_en);
CREATE INDEX natural_level IF NOT EXISTS FOR (n:Natural) ON (n.level);
CREATE INDEX natural_core IF NOT EXISTS FOR (n:Natural) ON (n.core);
CREATE INDEX natural_cultural IF NOT EXISTS FOR (n:Natural) ON (n.cultural);

// ========================================
// Create hierarchical relationships
// ========================================

// SEASONS hierarchy
MATCH (core:Natural {name_en: 'SEASONS'})
MATCH (spring:Natural {name_en: 'Spring'})
MATCH (summer:Natural {name_en: 'Summer'})
MATCH (autumn:Natural {name_en: 'Autumn'})
MATCH (winter:Natural {name_en: 'Winter'})
MATCH (transition:Natural {name_en: 'Seasonal Transition'})
MERGE (core)-[:CONTAINS]->(spring)
MERGE (core)-[:CONTAINS]->(summer)
MERGE (core)-[:CONTAINS]->(autumn)
MERGE (core)-[:CONTAINS]->(winter)
MERGE (core)-[:CONTAINS]->(transition);

// Spring specific hierarchy
MATCH (spring:Natural {name_en: 'Spring'})
MATCH (cherry:Natural {name_en: 'Cherry Blossoms'})
MATCH (growth:Natural {name_en: 'New Growth'})
MATCH (rain:Natural {name_en: 'Spring Rain'})
MATCH (breeze:Natural {name_en: 'Warm Breeze'})
MERGE (spring)-[:CONTAINS]->(cherry)
MERGE (spring)-[:CONTAINS]->(growth)
MERGE (spring)-[:CONTAINS]->(rain)
MERGE (spring)-[:CONTAINS]->(breeze);

// WEATHER hierarchy
MATCH (core:Natural {name_en: 'WEATHER'})
MATCH (precipitation:Natural {name_en: 'Precipitation'})
MATCH (wind:Natural {name_en: 'Wind Patterns'})
MATCH (clouds:Natural {name_en: 'Cloud Formation'})
MATCH (pressure:Natural {name_en: 'Atmospheric Pressure'})
MATCH (temp:Natural {name_en: 'Temperature Change'})
MERGE (core)-[:CONTAINS]->(precipitation)
MERGE (core)-[:CONTAINS]->(wind)
MERGE (core)-[:CONTAINS]->(clouds)
MERGE (core)-[:CONTAINS]->(pressure)
MERGE (core)-[:CONTAINS]->(temp);

// CELESTIAL hierarchy
MATCH (core:Natural {name_en: 'CELESTIAL'})
MATCH (sun:Natural {name_en: 'Sun'})
MATCH (moon:Natural {name_en: 'Moon'})
MATCH (stars:Natural {name_en: 'Stars'})
MATCH (planets:Natural {name_en: 'Planets'})
MATCH (sky:Natural {name_en: 'Sky Phenomena'})
MERGE (core)-[:CONTAINS]->(sun)
MERGE (core)-[:CONTAINS]->(moon)
MERGE (core)-[:CONTAINS]->(stars)
MERGE (core)-[:CONTAINS]->(planets)
MERGE (core)-[:CONTAINS]->(sky);

// FLORA hierarchy
MATCH (core:Natural {name_en: 'FLORA'})
MATCH (trees:Natural {name_en: 'Trees'})
MATCH (flowers:Natural {name_en: 'Flowers'})
MATCH (grasses:Natural {name_en: 'Grasses'})
MATCH (mosses:Natural {name_en: 'Mosses'})
MATCH (vines:Natural {name_en: 'Vines'})
MATCH (shrubs:Natural {name_en: 'Shrubs'})
MERGE (core)-[:CONTAINS]->(trees)
MERGE (core)-[:CONTAINS]->(flowers)
MERGE (core)-[:CONTAINS]->(grasses)
MERGE (core)-[:CONTAINS]->(mosses)
MERGE (core)-[:CONTAINS]->(vines)
MERGE (core)-[:CONTAINS]->(shrubs);

// ========================================
// Verification Query
// ========================================
// Run this to verify node creation:
// MATCH (n:Natural) RETURN n.level, count(n) ORDER BY n.level;