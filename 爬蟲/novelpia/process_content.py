def process_novel_content(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到開始和結束的標記
    start_marker = "소설 내용을 불러오고 있습니다."
    end_marker = "다음화 보기"
    
    # 找到標記的位置
    start_pos = content.find(start_marker)
    if start_pos == -1:
        print("找不到開始標記")
        return
    
    end_pos = content.find(end_marker, start_pos)
    if end_pos == -1:
        print("找不到結束標記")
        return
    
    # 擷取內容（不包含標記本身）
    start_pos = start_pos + len(start_marker)
    extracted_content = content[start_pos:end_pos].strip()
    
    # 進一步清理內容
    lines = extracted_content.split('\n')
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        # 只保留非空行且不包含特定字串的行
        if line and not any(x in line for x in ['$.cookie', 'function', 'PLUS', '커버보기']):
            cleaned_lines.append(line)
    
    # 寫入新檔案
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(cleaned_lines))
    
    print(f"已成功處理內容並儲存至 {output_file}")

# 執行處理
input_file = "novel_content/content.txt"
output_file = "novel_content/processed_content.txt"
process_novel_content(input_file, output_file) 