// Golden AGI Food Culture Ontology - Node Creation Script
// Based on Lina's advice and comprehensive food culture classification research
// This script creates all food culture concept nodes with English/Japanese names and hierarchical levels

// Clear existing food culture nodes (optional - uncomment if needed)
// MATCH (n:FoodCulture) DETACH DELETE n;

// ========================================
// CORE CATEGORIES (Level 0)
// ========================================

MERGE (:FoodCulture {name_en: 'CULINARY CULTURE',   name_ja: '文化系',     level: 0, core: true})
MERGE (:FoodCulture {name_en: 'HISTORICAL CONTEXT', name_ja: '歴史系',     level: 0, core: true})
MERGE (:FoodCulture {name_en: 'REGIONAL CUISINE',   name_ja: '国籍系',     level: 0, core: true})
MERGE (:FoodCulture {name_en: 'COOKING METHODS',    name_ja: '調理系',     level: 0, core: true})
MERGE (:FoodCulture {name_en: 'ACADEMIC FIELDS',    name_ja: '学問系',     level: 0, core: true})
MERGE (:FoodCulture {name_en: 'TASTE PROFILES',     name_ja: '味覚表現',   level: 0, core: true})
MERGE (:FoodCulture {name_en: 'RELIGIOUS TABOOS',   name_ja: '宗教的タブー', level: 0, core: true})
MERGE (:FoodCulture {name_en: 'HEALTH & ETHICS',    name_ja: '健康・倫理', level: 0, core: true});

// ========================================
// CULINARY CULTURE CATEGORY (Examples of Cuisines by Culture/Style)
// ========================================

// Level 1 - Cultural Cuisine Types
MERGE (:FoodCulture {name_en: 'Chinese Cuisine',   name_ja: '中華料理',   level: 1})
MERGE (:FoodCulture {name_en: 'French Cuisine',    name_ja: 'フランス料理', level: 1})
MERGE (:FoodCulture {name_en: 'Japanese Cuisine',  name_ja: '和食',       level: 1})
MERGE (:FoodCulture {name_en: 'African Cuisine',   name_ja: 'アフリカ料理', level: 1})
MERGE (:FoodCulture {name_en: 'Asian Cuisine',     name_ja: 'アジア料理',  level: 1});

// ========================================
// HISTORICAL CONTEXT CATEGORY (Eras/Periods of Food Culture)
// ========================================

// Level 1 - Historical Era Contexts
MERGE (:FoodCulture {name_en: 'FUTURISTIC',   name_ja: '未来',   level: 1})
MERGE (:FoodCulture {name_en: 'CONTEMPORARY', name_ja: '現代',   level: 1})
MERGE (:FoodCulture {name_en: 'MODERN',       name_ja: '近代',   level: 1})
MERGE (:FoodCulture {name_en: 'MEDIEVAL',     name_ja: '中世',   level: 1})
MERGE (:FoodCulture {name_en: 'PRIMITIVE',    name_ja: '原始的', level: 1})
MERGE (:FoodCulture {name_en: 'ANIMALISTIC',  name_ja: '動物的', level: 1});

// ========================================
// REGIONAL CUISINE CATEGORY (National/Regional Cuisines)
// ========================================

// Level 1 - Regional/National Cuisine Types
MERGE (:FoodCulture {name_en: 'Japanese Home Cooking', name_ja: '日本の家庭料理', level: 1})
MERGE (:FoodCulture {name_en: 'Japanese (Washoku)',    name_ja: '和食',         level: 1})
MERGE (:FoodCulture {name_en: 'French',                name_ja: 'フレンチ',     level: 1})
MERGE (:FoodCulture {name_en: 'Western',               name_ja: '洋食',         level: 1})
MERGE (:FoodCulture {name_en: 'Chinese',               name_ja: '中華',         level: 1})
MERGE (:FoodCulture {name_en: 'African',               name_ja: 'アフリカン',   level: 1})
MERGE (:FoodCulture {name_en: 'Italian',               name_ja: 'イタリア料理', level: 1})
MERGE (:FoodCulture {name_en: 'Spanish',               name_ja: 'スペイン料理', level: 1})
MERGE (:FoodCulture {name_en: 'Indian',                name_ja: 'インド料理',   level: 1})
MERGE (:FoodCulture {name_en: 'Ethnic (Fusion)',       name_ja: 'エスニック料理', level: 1})
MERGE (:FoodCulture {name_en: 'Pan-Asian',             name_ja: 'アジア料理',    level: 1})
MERGE (:FoodCulture {name_en: 'Eastern European',      name_ja: '東欧料理',     level: 1})
MERGE (:FoodCulture {name_en: 'Western European',      name_ja: '西欧料理',     level: 1})
MERGE (:FoodCulture {name_en: 'Northern European',     name_ja: '北欧料理',     level: 1})
MERGE (:FoodCulture {name_en: 'Amazonian',             name_ja: 'アマゾン料理', level: 1});

// ========================================
// COOKING METHODS CATEGORY (Techniques, Preparation, Tools, etc.)
// ========================================

// Level 1 - Cooking Techniques (Heat-based methods)
MERGE (:FoodCulture {name_en: 'Grilling/Roasting', name_ja: '焼く',   level: 1})
MERGE (:FoodCulture {name_en: 'Simmering/Boiling', name_ja: '煮る',   level: 1})
MERGE (:FoodCulture {name_en: 'Steaming',         name_ja: '蒸す',   level: 1})
MERGE (:FoodCulture {name_en: 'Deep Frying',      name_ja: '揚げる', level: 1})
MERGE (:FoodCulture {name_en: 'Boiling (Blanch)', name_ja: '茹でる', level: 1})

// Level 1 - Food Preparation Techniques
MERGE (:FoodCulture {name_en: 'Filleting/Butchering', name_ja: '捌く',       level: 1})
MERGE (:FoodCulture {name_en: 'Chopping/Mincing',     name_ja: '刻む',       level: 1})
MERGE (:FoodCulture {name_en: 'Kneading/Mixing',      name_ja: '捏ねる',     level: 1})
MERGE (:FoodCulture {name_en: 'Crushing/Mashing',     name_ja: '潰す',       level: 1})
MERGE (:FoodCulture {name_en: 'Cracking (eggs etc.)', name_ja: '割る',       level: 1})
MERGE (:FoodCulture {name_en: 'Stirring/Mixing',      name_ja: '混ぜる',     level: 1})
MERGE (:FoodCulture {name_en: 'Stretching (dough)',   name_ja: '伸ばす',     level: 1})
MERGE (:FoodCulture {name_en: 'Rubbing/Massaging',    name_ja: '揉む',       level: 1})
MERGE (:FoodCulture {name_en: 'Piercing/Skewering',   name_ja: '刺す',       level: 1})
MERGE (:FoodCulture {name_en: 'Marinating (seasoning blend in)', name_ja: '馴染ませる', level: 1})
MERGE (:FoodCulture {name_en: 'Soaking (flavor absorption)',    name_ja: '染み込ませる', level: 1})
MERGE (:FoodCulture {name_en: 'Kneading/Refining (paste)',      name_ja: '練る',       level: 1})

// Level 1 - Fermentation & Brewing
MERGE (:FoodCulture {name_en: 'Brewing',   name_ja: '醸す',   level: 1})
MERGE (:FoodCulture {name_en: 'Fermenting', name_ja: '発酵する', level: 1})

// Level 1 - Garnishing & Plating Techniques
MERGE (:FoodCulture {name_en: 'Garnishing/Decorating', name_ja: '飾る',   level: 1})
MERGE (:FoodCulture {name_en: 'Sprinkling (to season)', name_ja: 'ふりかける', level: 1})
MERGE (:FoodCulture {name_en: 'Adding on the Side',    name_ja: '添える',  level: 1})
MERGE (:FoodCulture {name_en: 'Plating/Serving',       name_ja: '盛る',    level: 1})
MERGE (:FoodCulture {name_en: 'Topping/Placing on',    name_ja: '乗せる',  level: 1})
MERGE (:FoodCulture {name_en: 'Coating/Wrapping',      name_ja: '纏わせる', level: 1})

// Level 1 - Units & Measurements
MERGE (:FoodCulture {name_en: 'Tablespoon',      name_ja: '大さじ',   level: 1})
MERGE (:FoodCulture {name_en: 'Teaspoon',        name_ja: '小さじ',   level: 1})
MERGE (:FoodCulture {name_en: 'Suitable Amount', name_ja: '適量',     level: 1})
MERGE (:FoodCulture {name_en: 'Approximate (to taste)', name_ja: '適当', level: 1})
MERGE (:FoodCulture {name_en: 'Measurement Units',     name_ja: '計量単位', level: 1})

// Level 1 - Temperature Settings
MERGE (:FoodCulture {name_en: 'Low Heat',    name_ja: '弱火',   level: 1})
MERGE (:FoodCulture {name_en: 'Medium Heat', name_ja: '中火',   level: 1})
MERGE (:FoodCulture {name_en: 'High Heat',   name_ja: '強火',   level: 1})
MERGE (:FoodCulture {name_en: 'Temperature Expressions', name_ja: '温度表現', level: 1})

// Level 1 - Cooking Utensils & Tools
MERGE (:FoodCulture {name_en: 'Kitchen Knife', name_ja: '包丁',   level: 1})
MERGE (:FoodCulture {name_en: 'Frying Pan',    name_ja: 'フライパン', level: 1})
MERGE (:FoodCulture {name_en: 'Cooking Pot',   name_ja: '鍋',     level: 1})
MERGE (:FoodCulture {name_en: 'Cooking Utensils', name_ja: '調理器具', level: 1});

// ========================================
// ACADEMIC FIELDS CATEGORY (Sciences related to Food & Cooking)
// ========================================

// Food and cooking involve various sciences (e.g., molecular gastronomy applies chemistry and "culinary physics" to cuisine)

// Level 1 - Academic Disciplines
MERGE (:FoodCulture {name_en: 'Culinary Science', name_ja: '料理学',   level: 1})
MERGE (:FoodCulture {name_en: 'Physics (Heat & Mechanics)',  name_ja: '物理学',   level: 1})
MERGE (:FoodCulture {name_en: 'Nutrition Science', name_ja: '栄養学',   level: 1})
MERGE (:FoodCulture {name_en: 'Chemistry (Food Chemistry)', name_ja: '化学',     level: 1})
MERGE (:FoodCulture {name_en: 'Ergonomics (Human Engineering)', name_ja: '人間工学', level: 1})

// ========================================
// TASTE PROFILES CATEGORY (Basic Taste Expressions)
// ========================================

// Five basic tastes are commonly defined as sweet, sour, salty, bitter, and umami. Here we include those plus spicy and astringent.

// Level 1 - Taste Categories
MERGE (:FoodCulture {name_en: 'Sweet (Sweetness)',   name_ja: '甘味',   level: 1})
MERGE (:FoodCulture {name_en: 'Sour (Sourness)',     name_ja: '酸味',   level: 1})
MERGE (:FoodCulture {name_en: 'Salty (Saltiness)',   name_ja: '塩味',   level: 1})
MERGE (:FoodCulture {name_en: 'Bitter (Bitterness)', name_ja: '苦味',   level: 1})
MERGE (:FoodCulture {name_en: 'Umami (Savory)',      name_ja: '旨味',   level: 1})
MERGE (:FoodCulture {name_en: 'Spicy (Pungent)',     name_ja: '辛味',   level: 1})
MERGE (:FoodCulture {name_en: 'Astringent',          name_ja: '渋味',   level: 1});

// ========================================
// RELIGIOUS TABOOS CATEGORY (Dietary Restrictions by Religion)
// ========================================

// Many religions impose dietary laws or taboos that forbid certain foods.

// Level 1 - Major Religious Food Taboos
MERGE (:FoodCulture {name_en: 'Islamic (Halal/Haram)', name_ja: 'イスラム教の食のタブー', level: 1})
MERGE (:FoodCulture {name_en: 'Jewish (Kosher Laws)',  name_ja: 'ユダヤ教の食のタブー',   level: 1})
MERGE (:FoodCulture {name_en: 'Hindu (No Beef, etc.)', name_ja: 'ヒンドゥー教の食のタブー', level: 1})
MERGE (:FoodCulture {name_en: 'Buddhist (Vegetarian)', name_ja: '仏教の食のタブー',       level: 1});

// ========================================
// HEALTH & ETHICS CATEGORY (Dietary Choices for Health/Ethical Reasons)
// ========================================

// People adopt diets like vegetarian or vegan for health, environmental, ethical, or religious reasons.

// Level 1 - Health/Ethical Dietary Practices
MERGE (:FoodCulture {name_en: 'Vegetarianism', name_ja: '菜食主義',     level: 1})
MERGE (:FoodCulture {name_en: 'Veganism',      name_ja: '完全菜食主義', level: 1})
MERGE (:FoodCulture {name_en: 'Organic Food',  name_ja: 'オーガニック食品', level: 1})
MERGE (:FoodCulture {name_en: 'Fair Trade Food', name_ja: 'フェアトレード', level: 1})
MERGE (:FoodCulture {name_en: 'Sustainable Food', name_ja: '持続可能な食品', level: 1})
MERGE (:FoodCulture {name_en: 'Local (Locavore)', name_ja: '地産地消',   level: 1});

// ========================================
// Add indexes for better performance (optional)
// ========================================

CREATE INDEX food_name_en IF NOT EXISTS FOR (f:FoodCulture) ON (f.name_en);
CREATE INDEX food_level   IF NOT EXISTS FOR (f:FoodCulture) ON (f.level);
CREATE INDEX food_core    IF NOT EXISTS FOR (f:FoodCulture) ON (f.core);

// ========================================
// Verification Query
// ========================================
// MATCH (n:FoodCulture) RETURN n.level, count(n) ORDER BY n.level;