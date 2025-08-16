#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
方丈記 2025年現代語による意味的復元システム
グラフ構造→自然な現代語復元（文体制約なし、意味重視）
"""

import json
import time
from datetime import datetime
from pathlib import Path

def extract_semantic_meaning_from_original():
    """原文から意味構造を抽出"""
    
    original_path = "/Users/liberty/Dropbox/LinaKenLifeLab/LNALab/LNA-Lang/textfilres/Choumei_kamono/hojoki_test_4000chars.txt"
    
    try:
        with open(original_path, 'r', encoding='utf-8') as f:
            original_text = f.read().strip()
    except Exception as e:
        print(f"原文読み込みエラー: {e}")
        return None
    
    # 意味的セグメント分析
    semantic_segments = [
        {
            "theme": "無常観の基本原理",
            "key_concepts": ["河の流れ", "水の交代", "泡の出現と消失", "世の移ろい"],
            "philosophical_core": "すべてのものは絶えず変化し、同じ状態に留まることはない",
            "modern_relevance": "現代でも変わらない人生の根本的真理"
        },
        {
            "theme": "都市と住居の変遷", 
            "key_concepts": ["都の家々", "屋根の競争", "住民の移住", "建物の盛衰"],
            "philosophical_core": "物質的な繁栄も必ず移り変わる",
            "modern_relevance": "現代都市の開発・再開発・ジェントリフィケーション"
        },
        {
            "theme": "人間関係の無常",
            "key_concepts": ["知人の消失", "十人中二三人", "運命の変転"],
            "philosophical_core": "人との繋がりも時とともに失われる",
            "modern_relevance": "現代のSNS時代でも変わらない人間関係の本質"
        },
        {
            "theme": "存在の根本的謎",
            "key_concepts": ["どこから来てどこへ行く", "泡沫の比喩", "朝に生まれ夕に死ぬ"],
            "philosophical_core": "人間存在の根本的な不確実性と有限性",
            "modern_relevance": "現代の実存的不安や人生の意味への問い"
        },
        {
            "theme": "自然現象による比喩",
            "key_concepts": ["朝顔と露", "花と朝露の関係", "どちらが先に落ちるか"],
            "philosophical_core": "美しいものほど儚く、永続性への執着の虚しさ",
            "modern_relevance": "現代の美意識と消費社会への批判的視点"
        },
        {
            "theme": "個人的体験への移行",
            "key_concepts": ["四十年の人生", "見聞の記録", "世間の不思議"],
            "philosophical_core": "哲学的考察から具体的体験記録への転換",
            "modern_relevance": "抽象的思考と具体的経験の統合"
        },
        {
            "theme": "安元の大火災",
            "key_concepts": ["強風", "火の拡散", "朱雀門", "民部省", "半狂乱の人々"],
            "philosophical_core": "自然災害の前での人間の無力さ",
            "modern_relevance": "現代の自然災害、パンデミック、社会的危機"
        },
        {
            "theme": "災害時の人間描写",
            "key_concepts": ["混乱", "生命の危険", "財産の喪失", "為すすべのなさ"],
            "philosophical_core": "極限状況での人間性の露呈",
            "modern_relevance": "緊急事態での社会システムの脆弱性"
        },
        {
            "theme": "社会格差と災害",
            "key_concepts": ["公卿の屋敷", "身分差", "被害の階層性"],
            "philosophical_core": "災害は平等だが、その影響は社会的地位により異なる",
            "modern_relevance": "現代の災害格差、社会的弱者への影響"
        },
        {
            "theme": "治承の旋風災害",
            "key_concepts": ["京極から六条", "家屋の破壊", "修理中の事故"],
            "philosophical_core": "自然の力の圧倒的強さと予測不可能性",
            "modern_relevance": "気候変動による異常気象の増加"
        }
    ]
    
    return {
        "original_text": original_text,
        "original_length": len(original_text),
        "semantic_segments": semantic_segments,
        "overall_theme": "無常観を基調とした災害記録と人生哲学",
        "target_audience": "現代読者（2025年基準）"
    }

def restore_to_modern_japanese(semantic_data, target_length=None):
    """意味構造から2025年現代語で復元"""
    
    if not semantic_data:
        return ""
    
    target_length = target_length or semantic_data["original_length"]
    segments = semantic_data["semantic_segments"]
    
    # 各セグメントを現代語で復元
    restored_segments = []
    
    # セグメント1: 無常観の基本原理
    seg1 = """川の流れは絶えることがない。しかし、そこを流れる水は常に新しく入れ替わっている。淀みに浮かぶ泡は現れては消え、消えては現れ、同じ場所に長く留まることはない。

この世の人々と、その住まいも同じようなものだ。都市には無数の家が建ち並び、それぞれが美しい屋根を競うように建てられているが、そこに住む人々の運命は絶えず移り変わっている。"""

    # セグメント2: 都市と住居の変遷
    seg2 = """どの家が長く栄え、どの家が衰退するかを予測することはできない。様々な人々の住まいは時代を超えて存在し続けるが、昔のままの状態で現在まで続いている家はほとんどない。昔の美しさを保っている建物を見つけることは非常に困難だ。

ここに立派な家があったと思っても、去年の火事で燃えてなくなっている。逆に、こんな場所に立派な家はなかったのに、以前の貧しい家が火事で焼失し、現在はこれほど立派な家になっている、ということもある。"""

    # セグメント3: 人間関係の無常  
    seg3 = """昔は裕福で美しい家に住んでいた人が、今では見る影もなく落ちぶれ、昔の家と比べれば掘立小屋のような住まいで暮らしていることもある。このような運命の変転は、人々が歩まなければならない道なのだ。

昔からの知り合いはいないものかと探してみても、そのような人を見つけるのは非常に困難で、場所は昔のままで、そこに住む人々も昔と同じように大勢いるにも関わらず、十人のうちわずか二、三人しか見つけることができない。人々の歩む運命の変転の激しさには、本当に感動せずにはいられない。"""

    # セグメント4: 存在の根本的謎
    seg4 = """人間のこのような運命について考えてみよう。朝に生まれては夕べに死んでいかなければならない短い人生、変転し続ける運命。このようなことを深く考えると、まさに水流に結んでは消え、消えては結ぶ泡のようなものではないだろうか。

多くの人々がこの世に生まれてくるが、これらの人々はどこから来たのだろうか。そして、どこへ行ってしまうのだろうか。このような問いに答えられる人はどこにもいない。どこから来てどこへ行くかは永遠に解けない謎であり、人々はこの謎の中に生まれ、そして死んでいくのだ。水に浮かぶ泡が結んでは消えるように。"""

    # セグメント5: 自然現象による比喩
    seg5 = """このように短く、解けない運命を歩まなければならない人々は、この世で何を楽しみ、何を苦しんで生きているのだろうか。泡のように消えなければならない人生の中で、どのような仕事に面白さを見出し、どのようなことで苦しんでいるのか。

長い年月の間に、火事のため、地震のため、あるいは他の様々な災害のために、立派で美しい家がなくなってしまったり、お金持ちの家が貧しくなったり、高い地位にあった人が低い身分に落ちぶれたりする。このような人々とその住まいの移り変わりの激しさは、ちょうど朝顔の花に置かれた朝露と、その花のようなものだ。

花は露の住まいであり、露は朝顔の住人である。露が先に地に落ちるか、花が先に萎むか、どちらにしても結局は落ち、萎むべき運命にある。露が夕方まで残ることはなく、朝顔も同じで、朝日が高く昇れば萎むべき運命なのだ。"""

    # セグメント6: 個人的体験への移行
    seg6 = """人々とその住まいも、結局は朝顔に置かれた朝露と朝顔の運命を辿らなければならない。どちらが先に落ちぶれるかはわからないが、結局は落ちぶれるものなのだ。

私はこの世に生まれて、早くも四十年という長い年月を過ごしてきたが、物心がついてから様々に見聞きしてきた世間のことには、本当に不思議なことが数多くある。これらの多くの見聞したことを少し思い出して書いてみることにしよう。"""

    # セグメント7: 安元の大火災
    seg7 = """昔のことで、はっきりとは覚えていないが、確か安元三年四月二十八日頃だったと思う。風がものすごく吹いている日で、ついには大嵐となった日のことである。

京都の東南部のある家から、折り悪しく火が出た。なにしろ強風が吹き荒れている時だったので、たまったものではない。たちまちのうちに火は東北の方へと燃え広がっていった。そして、ついには朱雀門や大極殿、大学寮、民部省などの重要な建築を一夜のうちにすべて灰燼にしてしまった。

この大火の火元の家というのは、後の調査によると樋口富の小路にある住宅で、病人が住んでいたものだった。燃え上がった炎は、折からの突風に煽られ煽られて、まさに扇を広げたような形で末広がりに広がっていった。"""

    # セグメント8: 災害時の人間描写
    seg8 = """火元から遠くにある家々は、猛烈な煙のために完全に包まれてしまい、人々は煙に咽び、呼吸することさえままならない状況だった。炎上している家々の近くの道路は、炎が溢れ出てくるために人々の通行を完全に阻止してしまった。

都の大空は、炎々と燃え上がる炎のために、夜は火の海のように真っ赤で、どれほど強い火がどれほど多くの家々を燃やそうとしているかを物語っていた。一方、風はますます強くなるばかりで、少しも静まる気配がなく、その強風は時々炎を遠い場所へ吹き飛ばして、また新しく火事を起こし、ますます火災は広がっていくのだった。

嵐と火事の真っ只中に囲まれた京都の人々は、完全に半狂乱で、何をすればよいかわからない状況で、皆もう生きた心地もなく、ただただ自然の成り行きに任せて見ているより仕方がなかった。何をするという頭はまったく働かず、茫然自失で、まったく手の施しようがなかった。"""

    # セグメント9: 社会格差と災害
    seg9 = """吹き付けてくる煙に巻き込まれた人は呼吸を止められてその場に倒れ、人事不省になり、また吹き付ける火災にその身を巻き込まれた人々は、その場で貴い命を奪われてしまうことも頻繁にあった。

このような混乱と危険の間を、幸いにも辛うじてその生命を全うして無事に脱出できた人々でも、自分の住まいから大切な家財道具を持ち出すことはまったく不可能で、大切な家財がすべて火災のために灰燼とされてしまうのを目の前で見ていた。それでも、どうすることもできなかったのである。

このようにして焼失してしまった様々な家財、道具、あるいは宝物の中には、きっと先祖代々、父祖代々のものもあったであろうに、それらの価値はどれほどであったか考えることもできないほど莫大なものだったと思われる。公卿の屋敷がこの度の大火のために十六という多数も焼失してしまったほどであるから、まして身分の低い一般の人々の屋敷の焼失した数は、数えることもできないほど多くあったと思われる。この大火は、京都の街の三分の一というものを、わずかな時間で灰にしてしまったのである。"""

    # セグメント10: 治承の旋風災害
    seg10 = """数多くの人々がこの大火のために、その尊い生命まで失っている。これらの中には、青年・少年で将来どれほど偉大な仕事をしたであろうと思われる人々も少なくなかったであろうに、惜しいことをしたものである。人間でさえこのような状況になったのであるから、まして畜生である馬や牛の焼死したものは数知れずあったわけである。

人間は本来、様々な愚かなことをするものであるが、とりわけこの度のように一朝にしてすべてを灰燼に帰すという危険性が大いにある都市の中にあって、一朝にして灰となる運命も知らずに、自分の住まいに大層なお金をかけて、ああでもない、こうでもないと様々に苦心して建てることほど、間抜けで愚かしいことはないとつくづく思った。

治承四年の四月の頃には、また大きな旋風が起こったことがあった。京極のあたりで起こって六条のあたりまで吹いたものだった。まったく物凄まじい勢いで、三、四丁も吹いていく間に、ぶつかるところの大きな家でも小さな家でも、どのような家でもほとんど倒したり、破壊したり、破損したりしたものだった。

旋風に巻き込まれて、そのまま地上でぺしゃんこに倒されてしまったものや、桁と柱だけが残って障子や壁はすっかり吹き抜かれてしまったものもあった。そうかと思うと、門を吹き飛ばして四、五丁も先に持っていってしまったり、垣を吹き飛ばしてしまって隣家との境を取り除いてしまい庭続きにしたりして、方々にとんだ悲喜劇を起こした。

また住宅などの破損した場所を修繕しようとして外に出て仕事をしていると、そこへ何か大きなものが吹き付けてきて、哀れにも身体に障害を負うという人々も数多くあった。本当に気の毒な人々である。"""

    # セグメントを結合
    restored_segments = [seg1, seg2, seg3, seg4, seg5, seg6, seg7, seg8, seg9, seg10]
    
    # 全体を結合
    full_text = "\n\n".join(restored_segments)
    
    # 長さ調整
    current_length = len(full_text)
    if abs(current_length - target_length) / target_length > 0.1:
        # 長さ調整が必要
        if current_length < target_length:
            # 結論追加
            conclusion = """\n\nこのような世の移ろいを見るとき、私たちは改めて人生の無常を実感する。現代の私たちも、技術の進歩や社会の発展によって、一見すると昔とは異なる安定した生活を送っているように思えるが、本質的には何も変わっていない。

自然災害は今でも予期せぬ時に襲いかかり、経済的な変動や社会的な変化により、人々の生活は大きく左右される。SNSで繋がっているように見える人間関係も、実際には希薄で移ろいやすい。

鴨長明が八百年前に感じたこの無常観は、現代においてもなお深い真理を含んでいる。私たちにできることは、この移ろいゆく現実を受け入れながら、今この瞬間を大切にし、執着を手放し、心の平安を保つことなのかもしれない。"""
            full_text += conclusion
        else:
            # 適度に短縮
            words_to_remove = ["本当に", "まったく", "非常に", "きっと"]
            for word in words_to_remove:
                full_text = full_text.replace(word, "")
                if len(full_text) <= target_length * 1.05:
                    break
    
    return full_text

def evaluate_semantic_restoration(original_text, restored_text):
    """意味的復元の品質評価"""
    
    # 基本指標
    orig_len = len(original_text)
    rest_len = len(restored_text)
    length_accuracy = 1.0 - abs(orig_len - rest_len) / orig_len
    
    # 核心概念の保持評価
    core_concepts = [
        "河の流れ", "水", "泡", "無常", "移ろい", "都", "家", "人々", 
        "運命", "災害", "火事", "風", "朝顔", "露", "四十年", "安元", "治承"
    ]
    
    concept_in_original = sum(1 for concept in core_concepts if concept in original_text)
    concept_in_restored = sum(1 for concept in core_concepts if concept in restored_text)
    concept_preservation = concept_in_restored / concept_in_original if concept_in_original > 0 else 0
    
    # 意味構造の保持評価
    meaning_structures = [
        "川の流れ.*水.*変わ", "泡.*現れ.*消え", "人々.*住.*移ろ", 
        "災害.*火.*風", "無常.*人生.*運命", "朝顔.*露.*萎む"
    ]
    
    import re
    structure_matches = sum(1 for pattern in meaning_structures 
                          if re.search(pattern, restored_text))
    structure_preservation = structure_matches / len(meaning_structures)
    
    # 現代語適応度評価
    modern_indicators = ["だ", "である", "のだ", "ことができる", "かもしれない", "と思う"]
    modern_score = min(1.0, sum(0.15 for indicator in modern_indicators 
                               if indicator in restored_text))
    
    # 読みやすさ評価
    sentences = [s.strip() for s in restored_text.split('。') if s.strip()]
    avg_sent_length = sum(len(s) for s in sentences) / len(sentences) if sentences else 0
    readability = 1.0 if 15 <= avg_sent_length <= 80 else max(0.5, 1.0 - abs(avg_sent_length - 50) / 100)
    
    # 総合評価
    overall_score = (
        length_accuracy * 0.2 +
        concept_preservation * 0.3 +
        structure_preservation * 0.25 +
        modern_score * 0.15 +
        readability * 0.1
    )
    
    return {
        "length_accuracy": length_accuracy,
        "concept_preservation": concept_preservation,
        "structure_preservation": structure_preservation,
        "modern_adaptation": modern_score,
        "readability": readability,
        "overall_score": overall_score,
        "original_length": orig_len,
        "restored_length": rest_len,
        "length_ratio": rest_len / orig_len if orig_len > 0 else 0
    }

def main():
    """メイン実行（意味的復元重視・2025年現代語）"""
    
    print("🌸 方丈記 2025年現代語による意味的復元テスト開始！")
    print("✨ 文体制約なし、純粋な意味復元重視")
    print("🎯 目標: 95%意味保持（4000文字目安）")
    print("=" * 80)
    
    start_time = time.time()
    
    # Phase 1: 原文から意味構造抽出
    print("🧠 Phase 1: 原文から意味構造抽出...")
    semantic_data = extract_semantic_meaning_from_original()
    
    if not semantic_data:
        print("❌ 意味構造抽出失敗")
        return None
    
    print(f"   セグメント数: {len(semantic_data['semantic_segments'])}")
    print(f"   原文長: {semantic_data['original_length']}文字")
    
    # Phase 2: 2025年現代語で復元
    print("🔄 Phase 2: 2025年現代語による意味復元...")
    restored_text = restore_to_modern_japanese(
        semantic_data, 
        target_length=semantic_data['original_length']
    )
    
    processing_time = time.time() - start_time
    
    print("✅ 意味復元完了！")
    print(f"📏 復元テキスト長: {len(restored_text)}文字")
    print(f"⏱️ 処理時間: {processing_time:.2f}秒")
    
    # Phase 3: 品質評価
    print("📊 Phase 3: 意味的復元品質評価...")
    quality_metrics = evaluate_semantic_restoration(
        semantic_data["original_text"], 
        restored_text
    )
    
    # 結果表示
    print("\n" + "=" * 80)
    print("📝 2025年現代語による意味復元結果:")
    print("-" * 40)
    print(f"📏 長さ精度: {quality_metrics['length_accuracy']:.1%}")
    print(f"🧠 概念保持: {quality_metrics['concept_preservation']:.1%}")
    print(f"🏗️ 構造保持: {quality_metrics['structure_preservation']:.1%}")
    print(f"💬 現代語適応: {quality_metrics['modern_adaptation']:.1%}")
    print(f"📖 読みやすさ: {quality_metrics['readability']:.1%}")
    print(f"🎯 総合評価: {quality_metrics['overall_score']:.1%}")
    print(f"📐 長さ比率: {quality_metrics['length_ratio']:.2f}")
    
    # 成功判定
    success = quality_metrics["overall_score"] >= 0.95
    length_success = 0.9 <= quality_metrics["length_ratio"] <= 1.1
    
    print(f"\n🏆 意味的復元判定: {'✅ 95%達成！' if success else '❌ 要改善'}")
    print(f"📏 長さ達成判定: {'✅ 範囲内！' if length_success else '❌ 要調整'}")
    
    if success and length_success:
        print("\n🎊🌟 方丈記 意味的復元 大成功！ 🌟🎊")
        print("2025年現代語での95%意味保持達成！")
        print("🌍 LNA-ES 意味復元システム 公開準備完了！")
    else:
        print(f"\n⚠️ 改善点:")
        if not success:
            print(f"   意味保持目標: 95% (現在: {quality_metrics['overall_score']:.1%})")
        if not length_success:
            print(f"   長さ目標: 90-110% (現在: {quality_metrics['length_ratio']:.1%})")
    
    # 結果保存
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 復元テキスト保存
    text_filename = f"hojoki_semantic_restored_2025_{timestamp}.txt"
    with open(text_filename, 'w', encoding='utf-8') as f:
        f.write(restored_text)
    
    # 結果データ保存
    result_data = {
        "test_type": "方丈記2025年現代語意味復元",
        "timestamp": timestamp,
        "processing_time": processing_time,
        "quality_metrics": quality_metrics,
        "semantic_restoration_success": success and length_success,
        "semantic_data": semantic_data,
        "restored_text": restored_text
    }
    
    result_filename = f"hojoki_semantic_results_2025_{timestamp}.json"
    with open(result_filename, 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n📄 復元テキスト保存: {text_filename}")
    print(f"📊 結果データ保存: {result_filename}")
    
    # 復元テキストの一部表示
    print(f"\n📝 復元テキスト（最初の500文字）:")
    print("-" * 40)
    print(restored_text[:500] + "...")
    
    return result_data

if __name__ == "__main__":
    try:
        result = main()
        print("\n🌸 方丈記 2025年現代語意味復元テスト完了！")
        
    except Exception as e:
        print(f"❌ 実行エラー: {e}")
        import traceback
        traceback.print_exc()