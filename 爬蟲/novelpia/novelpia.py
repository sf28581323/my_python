from playwright.sync_api import sync_playwright
import time
import os
import requests
from urllib.parse import urlparse
import random

# 建立儲存圖片的資料夾
SAVE_DIR = "novel_content"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
if not os.path.exists(os.path.join(SAVE_DIR, "images")):
    os.makedirs(os.path.join(SAVE_DIR, "images"))

def random_sleep(min_seconds=1, max_seconds=3):
    time.sleep(random.uniform(min_seconds, max_seconds))

def download_image(url, filename):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
            'Referer': 'https://novelpia.com/',
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Accept-Language': 'ko-KR,ko;q=0.9',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"iOS"'
        }
        response = requests.get(url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"下載圖片時發生錯誤: {str(e)}")
        return False

try:
    with sync_playwright() as p:
        # 使用 iPhone 13 Pro Max 的設定
        iphone_13 = p.devices['iPhone 13 Pro Max']
        
        # 啟動瀏覽器
        print("正在啟動瀏覽器...")
        try:
            browser = p.chromium.launch(headless=False)
        except Exception as e:
            print("啟動瀏覽器失敗，請確認是否已執行 'playwright install'")
            print(f"錯誤訊息: {str(e)}")
            raise
        
        # 建立新的上下文
        context = browser.new_context(
            **iphone_13,
            locale='ko-KR',
            timezone_id='Asia/Seoul',
            geolocation={'latitude': 37.5665, 'longitude': 126.9780},
            permissions=['geolocation']
        )
        
        # 建立新頁面
        page = context.new_page()
        
        # 設定 User Agent
        page.set_extra_http_headers({
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1'
        })
        
        # 先進行登入
        print("正在進行登入...")
        page.goto("https://novelpia.com/login", wait_until="networkidle")
        random_sleep(3, 5)
        
        # 處理可能出現的廣告視窗
        try:
            print("正在檢查廣告視窗...")
            # 縮短等待時間
            random_sleep(1, 2)
            
            # 使用更精確的選擇器列表
            selectors = [
                '[class*="close"]',
                '[class*="Close"]',
                'button[class*="close"]',
                'button[class*="Close"]',
                'img[src*="close"]',
                'img[src*="Close"]'
            ]
            
            # 縮短超時時間並加快處理速度
            for selector in selectors:
                try:
                    elements = page.query_selector_all(selector)
                    for element in elements:
                        if element.is_visible():
                            try:
                                element.click(timeout=3000)
                                random_sleep(0.5, 1)
                                break
                            except:
                                continue
                except:
                    continue
            
            # 使用更簡單的 JavaScript 來關閉廣告
            page.evaluate("""() => {
                ['modal', 'popup', 'dialog', 'overlay', 'backdrop'].forEach(className => {
                    document.querySelectorAll(`[class*="${className}"]`).forEach(el => el.remove());
                });
            }""")
            
        except Exception as e:
            print(f"處理廣告視窗時發生錯誤: {str(e)}")
        
        # 等待登入表單載入並輸入帳號密碼
        try:
            print("準備登入流程...")
            
            # 點擊底部導航欄的內書架按鈕
            try:
                print("等待頁面完全載入...")
                random_sleep(2, 3)
                
                # 點擊底部導航欄的內書架按鈕
                mybook_button = page.wait_for_selector('.bt-nv-menu >> text=내서재', state="visible", timeout=5000)
                if mybook_button:
                    print("找到內書架按鈕")
                    mybook_button.click()
                    random_sleep(2, 3)
                    
                    # 等待登入表單出現
                    print("等待登入表單出現...")
                    login_form = page.wait_for_selector('input[name="email"]', state="visible", timeout=10000)
                    if not login_form:
                        raise Exception("無法找到登入表單")
                    print("找到登入表單")
                    
                    # 輸入電子郵件
                    email_input = page.locator('input[name="email"]')
                    if email_input:
                        print("找到電子郵件輸入框")
                        email_input.fill("")
                        random_sleep(0.5, 1)
                        email_input.type("帳號", delay=50)
                    
                    random_sleep(0.5, 1)
                    
                    # 輸入密碼
                    password_input = page.locator('input[name="wd"]')
                    if password_input:
                        print("找到密碼輸入框")
                        password_input.fill("")
                        random_sleep(0.5, 1)
                        password_input.type("密碼", delay=50)
                    
                    random_sleep(0.5, 1)
                    
                    # 點擊登入按鈕
                    login_button = page.locator('button[type="submit"]')
                    if login_button:
                        print("找到登入按鈕")
                        login_button.click()
                    
                    random_sleep(2, 3)
                    
            except Exception as e:
                print(f"點擊內書架按鈕時發生錯誤: {str(e)}")
                page.screenshot(path="mybook_button_error.png")
                raise
            
        except Exception as e:
            print(f"登入過程發生錯誤: {str(e)}")
            try:
                page.screenshot(path="login_error.png")
                print("已保存錯誤截圖至 login_error.png")
            except:
                print("無法保存錯誤截圖")
            raise
        
        # 訪問目標網頁
        print("正在訪問目標頁面...")
        try:
            # 使用 domcontentloaded 事件
            page.goto("目標頁面連結", wait_until="domcontentloaded", timeout=60000)
            
            # 等待頁面主要內容出現
            print("等待頁面載入...")
            random_sleep(3, 5)
            
            # 等待內容載入
            print("等待內容載入...")
            try:
                # 等待一段時間讓內容完全載入
                random_sleep(5, 7)
                
                # 先點擊頁面中央以顯示控制項
                print("點擊頁面中央...")
                page.mouse.click(page.viewport_size["width"] / 2, 
                               page.viewport_size["height"] / 2)
                random_sleep(2, 3)
                
                # 等待並點擊滾動模式按鈕
                print("設置閱讀器模式...")
                try:
                    scroll_btn = page.wait_for_selector('#viewer_1_btn', timeout=5000)
                    if scroll_btn:
                        scroll_btn.click()
                        print("已切換到滾動模式")
                        random_sleep(1, 2)
                except:
                    print("無法找到滾動模式按鈕")
                
                # 等待並點擊圖片顯示按鈕
                try:
                    img_btn = page.wait_for_selector('#img_on_btn', timeout=5000)
                    if img_btn:
                        img_btn.click()
                        print("已開啟圖片顯示")
                        random_sleep(1, 2)
                except:
                    print("無法找到圖片顯示按鈕")
                
                # 等待內容載入
                print("等待內容載入完成...")
                random_sleep(3, 5)
                
                # 使用 JavaScript 直接獲取內容
                content_data = page.evaluate("""() => {
                    // 獲取小說內容區域
                    const viewer = document.querySelector('#novel_viewer');
                    if (!viewer) return { text: '', images: [] };
                    
                    // 移除不需要的元素
                    const elementsToRemove = viewer.querySelectorAll('script, style, .bottom_banner_wrapper, .viewer_bottom');
                    elementsToRemove.forEach(el => el.remove());
                    
                    // 獲取文字內容
                    const textContent = viewer.textContent
                        .split('\\n')
                        .map(line => line.trim())
                        .filter(line => {
                            // 只保留有實際內容的行
                            return line && 
                                   !line.includes('function') &&
                                   !line.includes('script') &&
                                   !line.includes('$.cookie') &&
                                   !line.includes('const') &&
                                   !line.includes('var') &&
                                   !line.includes('PLUS') &&
                                   !line.includes('커버보기') &&
                                   !/^[A-Za-z0-9+/=]+$/.test(line);
                        })
                        .join('\\n\\n');
                    
                    // 獲取圖片
                    const images = Array.from(viewer.querySelectorAll('img'))
                        .map(img => img.src)
                        .filter(src => src && src.endsWith('.file'));
                    
                    return {
                        text: textContent,
                        images: images
                    };
                }""")

                # 如果第一次沒有獲取到內容，等待後重試
                if not content_data['text']:
                    print("等待內容載入中...")
                    page.wait_for_selector('#novel_text', state='visible', timeout=10000)
                    random_sleep(3, 5)
                    
                    # 再次嘗試獲取內容
                    content_data = page.evaluate("""() => {
                        const novelText = document.querySelector('#novel_text');
                        if (!novelText) return { text: '', images: [] };
                        
                        const textContent = novelText.textContent
                            .split('\\n')
                            .map(line => line.trim())
                            .filter(line => {
                                return line && 
                                       !line.includes('function') &&
                                       !line.includes('script') &&
                                       !line.includes('css') &&
                                       !line.includes('margin') &&
                                       !line.includes('padding') &&
                                       !/^[A-Za-z0-9+/=]+$/.test(line);
                            })
                            .join('\\n\\n');

                        const images = Array.from(document.querySelectorAll('#novel_box img'))
                            .map(img => img.src)
                            .filter(src => src && src.endsWith('.file'));

                        return {
                            text: textContent,
                            images: images
                        };
                    }""")
                
                if not content_data['text']:
                    raise Exception("無法獲取文字內容")
                
                content = content_data['text']
                print("已擷取文字內容")
                
                # 下載圖片
                print("正在下載圖片...")
                image_paths = []
                
                for i, img_url in enumerate(content_data['images']):
                    try:
                        # 確保 URL 是完整的
                        if img_url.startswith('//'):
                            img_url = 'https:' + img_url
                        
                        # 從 URL 判斷副檔名
                        ext = os.path.splitext(urlparse(img_url).path)[1]
                        if ext == '.file':
                            ext = '.jpg'  # 將 .file 轉換為 .jpg
                        
                        filename = os.path.join(SAVE_DIR, "images", f"image_{i+1}{ext}")
                        if download_image(img_url, filename):
                            print(f"已下載圖片 {i+1}: {filename}")
                            image_paths.append(f"[圖片{i+1}] {filename}")
                        random_sleep(1, 2)
                    except Exception as e:
                        print(f"下載圖片 {i+1} 時發生錯誤: {str(e)}")

            except Exception as e:
                print(f"等待內容元素時發生錯誤: {str(e)}")
                try:
                    page.screenshot(path="content_error.png")
                except:
                    print("無法保存錯誤截圖")
                raise
            
        except Exception as e:
            print(f"訪問目標頁面時發生錯誤: {str(e)}")
            page.screenshot(path="page_error.png")
            raise
        
        # 儲存內容
        print("正在儲存內容...")
        with open(os.path.join(SAVE_DIR, "content.txt"), "w", encoding="utf-8") as file:
            file.write(content + "\n\n")
            if image_paths:
                file.write("\n--- 圖片列表 ---\n")
                file.write("\n".join(image_paths))
        
        print(f"所有內容已成功儲存至 {SAVE_DIR} 資料夾")
        
        # 關閉瀏覽器
        browser.close()

except Exception as e:
    print(f"發生錯誤: {str(e)}")
    import traceback
    print("錯誤詳情:")
    print(traceback.format_exc())