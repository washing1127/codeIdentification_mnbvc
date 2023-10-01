import kenlm

# 加载已训练的KenLM语言模型
def load_language_model(model_path):
    try:
        language_model = kenlm.LanguageModel(model_path)
        return language_model
    except Exception as e:
        print(f"加载语言模型失败: {e}")
        return None

# 判断文本段落是否包含代码
def contains_code_in_paragraph(paragraph, language_model, threshold=-10.0):
    try:
        # 计算段落的概率得分
        score = language_model.score(paragraph)
        
        # 根据概率得分判断是否包含代码
        return score < threshold
    except Exception as e:
        print(f"判断段落是否包含代码失败: {e}")
        return False

def main():
    # 文件路径
    model_path = "code_language_model.binary"
    ocr_text_path = "ocr_text.txt"

    # 加载语言模型
    language_model = load_language_model(model_path)
    if not language_model:
        return

    try:
        # 读取OCR识别后的文本
        with open(ocr_text_path, 'r', encoding='utf-8') as file:
            ocr_text = file.read()

        # 将文本按段落分割成列表
        paragraphs = ocr_text.split('\n')

        # 遍历每个段落并判断是否包含代码
        for i, paragraph in enumerate(paragraphs):
            if contains_code_in_paragraph(paragraph, language_model):
                print(f"段落 {i+1} 包含代码:\n{paragraph}")
            else:
                print(f"段落 {i+1} 不包含代码:\n{paragraph}")

    except Exception as e:
        print(f"处理文本失败: {e}")

if __name__ == "__main__":
    main()
