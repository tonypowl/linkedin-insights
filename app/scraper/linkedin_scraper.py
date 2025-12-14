from playwright.sync_api import sync_playwright #using playwright to scrape
import re

def scrape_linkedin_page(page_id: str):
    url = f"https://www.linkedin.com/company/{page_id}/"

    data = {
        "page_id": page_id,
        "name": None,
        "url": url,
        "industry": None,
        "followers": None,
        "description": None,
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=60000)
        page.wait_for_timeout(3000)

        #page name
        try:
            data["name"] = page.locator("h1").first.inner_text().strip()
        except:
            pass

        #description
        try:
            data["description"] = page.locator("section").inner_text().strip()
        except:
            pass

        #followers(text into number)
        try:
            text = page.locator("text=followers").first.inner_text()
            match = re.search(r"([\d,]+)", text)
            if match:
                data["followers"] = int(match.group(1).replace(",", ""))
        except:
            pass

        browser.close()

    return data

def scrape_linkedin_posts(page_id: str, limit: int = 5):
    posts = []

    url = f"https://www.linkedin.com/company/{page_id}/posts/"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=60000)
        page.wait_for_timeout(3000)

        for _ in range(2):
            page.mouse.wheel(0, 2000)
            page.wait_for_timeout(2000)

        post_elements = page.query_selector_all("div.feed-shared-update-v2")

        for post in post_elements[:limit]:
            try:
                text = post.inner_text()
                posts.append({
                    "page_id": page_id,
                    "content": text.strip()
                })
            except:
                continue

        browser.close()
    return posts

