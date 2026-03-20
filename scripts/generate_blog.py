#!/usr/bin/env python3
import csv
import os

# Paths
BLOG_DIR = "blog"
THAI_BLOG_DIR = "th/blog"
CSV_FILE = f"{BLOG_DIR}/posts.csv"

# HTML Templates (same as before — no changes needed to the templates)
LISTING_TEMPLATE = """..."""  # Same as your current template
POST_TEMPLATE = """..."""      # Same as your current template

def main():
    print("📖 Generating blog from CSV...")
    
    # Create Thai directory if it doesn't exist
    os.makedirs(THAI_BLOG_DIR, exist_ok=True)
    
    # Read posts from CSV
    posts = []
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            posts.append(row)
    
    # Generate individual post pages (English + Thai)
    for i, post in enumerate(posts):
        slug = post['slug']
        
        # ===== ENGLISH VERSION =====
        content_html = post['content'].replace('\n\n', '</p><p>')
        content_html = '<p>' + content_html + '</p>'
        
        prev_link = posts[i-1]['slug'] + '.html' if i > 0 else '#'
        next_link = posts[i+1]['slug'] + '.html' if i < len(posts)-1 else '#'
        
        post_html = POST_TEMPLATE.format(
            title=post['title'],
            excerpt=post['excerpt'],
            category=post['category'],
            image_url=post['image_url'],
            content_paragraphs=content_html,
            prev_link=prev_link,
            next_link=next_link
        )
        
        # English file
        output_file = f"{BLOG_DIR}/{slug}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(post_html)
        print(f"✅ Generated English: {output_file}")
        
        # ===== THAI VERSION =====
        if post.get('title_th') and post.get('content_th'):
            content_th_html = post['content_th'].replace('\n\n', '</p><p>')
            content_th_html = '<p>' + content_th_html + '</p>'
            
            post_th_html = POST_TEMPLATE.format(
                title=post['title_th'],
                excerpt=post['excerpt_th'] if post.get('excerpt_th') else post['excerpt'],
                category=post['category'],
                image_url=post['image_url'],
                content_paragraphs=content_th_html,
                prev_link=f"../{posts[i-1]['slug']}.html" if i > 0 else '#',
                next_link=f"../{posts[i+1]['slug']}.html" if i < len(posts)-1 else '#'
            )
            
            output_th_file = f"{THAI_BLOG_DIR}/{slug}.html"
            with open(output_th_file, 'w', encoding='utf-8') as f:
                f.write(post_th_html)
            print(f"✅ Generated Thai: {output_th_file}")
    
    # Generate English listing page
    cards = []
    for post in posts:
        card = f"""
        <a href="{post['slug']}.html" class="blog-card">
            <div class="blog-card-img">
                <img src="{post['image_url']}" alt="{post['title']}">
            </div>
            <div class="blog-card-content">
                <div class="blog-card-category">{post['category']}</div>
                <h3 class="blog-card-title">{post['title']}</h3>
                <p class="blog-card-excerpt">{post['excerpt']}</p>
            </div>
        </a>"""
        cards.append(card)
    
    listing_html = LISTING_TEMPLATE.format(cards='\n'.join(cards))
    with open(f"{BLOG_DIR}/index.html", 'w', encoding='utf-8') as f:
        f.write(listing_html)
    print(f"✅ Generated {BLOG_DIR}/index.html")
    
    # Generate Thai listing page
    thai_cards = []
    for post in posts:
        if post.get('title_th'):
            thai_card = f"""
            <a href="{post['slug']}.html" class="blog-card">
                <div class="blog-card-img">
                    <img src="{post['image_url']}" alt="{post['title_th']}">
                </div>
                <div class="blog-card-content">
                    <div class="blog-card-category">{post['category']}</div>
                    <h3 class="blog-card-title">{post['title_th']}</h3>
                    <p class="blog-card-excerpt">{post.get('excerpt_th', post['excerpt'])}</p>
                </div>
            </a>"""
            thai_cards.append(thai_card)
    
    if thai_cards:
        thai_listing_html = LISTING_TEMPLATE.format(cards='\n'.join(thai_cards))
        with open(f"{THAI_BLOG_DIR}/index.html", 'w', encoding='utf-8') as f:
            f.write(thai_listing_html)
        print(f"✅ Generated {THAI_BLOG_DIR}/index.html")
    
    print("🎉 Blog generation complete!")

if __name__ == "__main__":
    main()
