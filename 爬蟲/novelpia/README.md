# Novelpia 小說爬蟲工具

這個專案是一個用於爬取 [Novelpia](https://novelpia.com/) 網站小說內容的工具。Novelpia 是一個韓國網路小說平台，本工具可以幫助用戶自動登入、爬取指定小說的文字內容和圖片，並進行後續處理。

## 功能特點

- **自動登入**：使用 Playwright 模擬移動設備訪問並自動登入 Novelpia 網站
- **內容爬取**：爬取指定小說的完整文字內容
- **圖片下載**：自動下載小說中的所有圖片
- **內容處理**：清理爬取的內容，去除不必要的標記和文字
- **圖片處理**：將下載的圖片統一重命名為 JPG 格式

## 檔案結構

- `novelpia.py` - 主要爬蟲程式，負責登入網站、爬取內容和下載圖片
- `process_content.py` - 處理爬取的文字內容，清理不必要的標記和文字
- `rename_images.py` - 將下載的圖片統一重命名為 JPG 格式
- `novel_content/` - 存放爬取的內容和圖片的資料夾
  - `content.txt` - 原始爬取的內容
  - `processed_content.txt` - 處理後的內容
  - `images/` - 存放下載的圖片

## 使用需求

- Python 3.7+
- Playwright
- Requests

## 安裝步驟

1. 安裝必要的 Python 套件：

```bash
pip install playwright requests
```

2. 安裝 Playwright 瀏覽器：

```bash
playwright install
```

## 使用方法

### 1. 爬取小說內容

編輯 `novelpia.py` 檔案，修改以下內容：

- 將 `email_input.type("帳號", delay=50)` 中的 "帳號" 替換為您的 Novelpia 帳號
- 將 `password_input.type("密碼", delay=50)` 中的 "密碼" 替換為您的 Novelpia 密碼
- 將 `page.goto("目標頁面連結", wait_until="domcontentloaded", timeout=60000)` 中的 "目標頁面連結" 替換為您要爬取的小說頁面 URL

然後執行：

```bash
python novelpia.py
```

### 2. 處理爬取的內容

執行：

```bash
python process_content.py
```

### 3. 處理下載的圖片

執行：

```bash
python rename_images.py
```

## 注意事項

- 本工具僅供學習和個人使用，請尊重著作權
- 過度頻繁的爬取可能會導致 IP 被封鎖，請適當控制爬取頻率
- 使用前請確保您已閱讀並同意 Novelpia 的服務條款

## 技術細節

- 使用 Playwright 模擬 iPhone 13 Pro Max 訪問網站，避免被檢測為爬蟲
- 使用隨機延遲模擬真實用戶行為
- 自動處理可能出現的廣告視窗
- 使用 JavaScript 直接從頁面提取內容，提高效率
- 圖片下載時添加適當的 User-Agent 和 Referer 頭信息，避免下載失敗

## 可能的問題與解決方案

- 如果登入失敗，請檢查帳號密碼是否正確
- 如果爬取內容為空，可能是網站結構有變化，需要更新選擇器
- 如果圖片下載失敗，可能是網站的防爬蟲機制有更新，需要調整請求頭

## 未來改進

- 添加命令行參數支持，方便指定爬取目標
- 添加多線程支持，提高爬取效率
- 添加錯誤重試機制，提高穩定性
- 添加代理支持，避免 IP 被封鎖 