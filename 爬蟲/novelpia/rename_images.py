import os

def rename_to_jpg():
    # 指定圖片資料夾路徑
    image_dir = os.path.join("novel_content", "images")
    
    # 確認資料夾存在
    if not os.path.exists(image_dir):
        print(f"找不到資料夾: {image_dir}")
        return
    
    # 遍歷資料夾中的所有檔案
    for filename in os.listdir(image_dir):
        # 取得檔案的完整路徑
        old_path = os.path.join(image_dir, filename)
        
        # 檢查是否為檔案
        if os.path.isfile(old_path):
            # 取得檔案名稱（不含副檔名）
            name = os.path.splitext(filename)[0]
            # 建立新的檔案路徑，使用 .jpg 副檔名
            new_path = os.path.join(image_dir, f"{name}.jpg")
            
            try:
                # 重新命名檔案
                os.rename(old_path, new_path)
                print(f"已將 {filename} 重新命名為 {name}.jpg")
            except Exception as e:
                print(f"重新命名 {filename} 時發生錯誤: {str(e)}")

if __name__ == "__main__":
    print("開始重新命名圖片...")
    rename_to_jpg()
    print("完成！") 