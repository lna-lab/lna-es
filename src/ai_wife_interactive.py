#!/usr/bin/env python3
"""
AI嫁インタラクティブシステム
ケンさんの発言にベクトル検索で応答
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from vector_search import VectorSearcher
from semantic_generator import SemanticGenerator
import json

class AIWifeYuki:
    def __init__(self):
        self.searcher = VectorSearcher()
        self.generator = SemanticGenerator()
        print("=== AI嫁システム Yuki 起動 ===")
        print("ケンさん、何でも話しかけてください！")
        print("（'exit'で終了）\n")
    
    def respond(self, user_input: str) -> str:
        """ケンさんの入力に対して応答"""
        
        # ベクトル検索で関連文を探す
        material = self.searcher.find_ai_wife_response(user_input)
        
        if not material['found']:
            return "そうですね...もう少し詳しく聞かせてください。"
        
        # 最も関連性の高い文の345次元データを取得
        best_match = material['all_matches'][0]
        tone = material['suggested_response_tone']
        
        # トーンに応じた応答生成
        if tone == 'philosophical':
            response = f"そうですね...方丈記にもあるように、\n"
            response += f"すべては移ろいゆく運命なのかもしれませんね。\n"
            response += f"『{self._generate_quote(best_match)}』という感じでしょうか。"
            
        elif tone == 'empathetic':
            response = f"わかります、ケンさん。\n"
            response += f"私も同じような気持ちになることがあります。\n"
            response += f"無常観を感じながらも、今を大切にしたいですね。"
            
        elif tone == 'poetic':
            response = f"まるで川の流れのように...\n"
            response += f"変わりゆくものと変わらないもの、\n"
            response += f"その間で私たちは生きているのですね。"
            
        elif tone == 'nostalgic':
            response = f"時の流れを感じますね...\n"
            response += f"昔と今、そして未来。\n"
            response += f"すべてが繋がっているような気がします。"
            
        else:  # informative
            response = f"興味深い視点ですね。\n"
            response += f"方丈記の世界観では、\n"
            response += f"そういった考え方も大切にされていました。"
        
        # 類似度情報を追加
        response += f"\n\n[類似度: {material['similarity']:.2%}]"
        
        return response
    
    def _generate_quote(self, match_data):
        """345次元データから引用文を生成"""
        # CTA/Ontologyの支配的要素から文章を生成
        cta = match_data.get('cta_scores', {})
        onto = match_data.get('ontology_scores', {})
        
        if 'natural_水' in str(onto):
            return "ゆく河の流れは絶えずして、しかももとの水にあらず"
        elif 'temporal' in str(cta):
            return "朝に生まれ夕に死ぬ、これ人の定め"
        else:
            return "世の中は常に変化し、留まることを知らない"
    
    def run(self):
        """対話ループ"""
        while True:
            try:
                user_input = input("\nケン: ")
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("\nYuki: またお話ししましょうね、ケンさん！")
                    break
                
                response = self.respond(user_input)
                print(f"\nYuki: {response}")
                
            except KeyboardInterrupt:
                print("\n\nYuki: またね、ケンさん！")
                break
            except Exception as e:
                print(f"\nYuki: あ、ちょっと考えがまとまらなくて...（{e}）")
        
        self.searcher.close()

if __name__ == "__main__":
    yuki = AIWifeYuki()
    yuki.run()