#!/usr/bin/env python3
import csv
import os

# Paths
CSV_FILE = "blog/posts.csv"
ENGLISH_LISTING = "blog.html"
THAI_LISTING = "th/blog.html"
ENGLISH_POSTS_DIR = "blog"
THAI_POSTS_DIR = "th/blog"

# ===== LISTING TEMPLATE (Your existing one) =====
LISTING_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog · Janishammer</title>
    <meta name="description" content="Real stories about building businesses, learning from failure, and finding the path forward.">
    <script src="https://assets.janishammer.com/js/injector-core.js"></script>
    <script src="https://assets.janishammer.com/js/injector-config.js"></script>
    <style>
        .blog-header {{
            text-align: center;
            padding: 4rem 2rem 2rem;
        }}
        .blog-header h1 {{
            font-size: 3rem;
            color: white;
            text-shadow: 2px 4px 12px rgba(0,0,0,0.5);
            margin-bottom: 1rem;
        }}
        .blog-header p {{
            font-size: 1.2rem;
            color: rgba(255,255,255,0.9);
            max-width: 600px;
            margin: 0 auto;
        }}
        .blog-grid {{
            max-width: 1280px;
            margin: 2rem auto;
            padding: 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 2rem;
        }}
        .blog-card {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 24px;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            text-decoration: none;
            color: inherit;
            display: block;
            border: 1px solid rgba(255,255,255,0.2);
        }}
        .blog-card:hover {{
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            background: white;
        }}
        .blog-card-img {{
            width: 100%;
            height: 200px;
            overflow: hidden;
        }}
        .blog-card-img img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }}
        .blog-card:hover .blog-card-img img {{
            transform: scale(1.05);
        }}
        .blog-card-content {{
            padding: 1.5rem;
        }}
        .blog-card-category {{
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #E34C26;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}
        .blog-card-title {{
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
            color: #2C3E50;
            line-height: 1.3;
        }}
        .blog-card-excerpt {{
            font-size: 0.9rem;
            color: #666;
            line-height: 1.5;
        }}
        @media (max-width: 768px) {{
            .blog-header h1 {{ font-size: 2rem; }}
            .blog-grid {{ grid-template-columns: 1fr; padding: 1rem; }}
        }}
    </style>
</head>
<body>
    <div class="blog-header">
        <h1>Stories from the journey</h1>
        <p>Real lessons from building businesses, failing fast, and finding what works.</p>
    </div>
    <div class="blog-grid">
        {cards}
    </div>
</body>
</html>"""

# ===== POST TEMPLATE =====
POST_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} · Janishammer Blog</title>
    <meta name="description" content="{excerpt}">
    <script src="https://assets.janishammer.com/js/injector-core.js"></script>
    <script src="https://assets.janishammer.com/js/injector-config.js"></script>
    <style>
        .post-container {{
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 32px;
            border: 1px solid rgba(255,255,255,0.2);
        }}
        .post-header {{
            text-align: center;
            margin-bottom: 2rem;
        }}
        .post-category {{
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #E34C26;
            font-weight: 600;
        }}
        .post-title {{
            font-size: 2.5rem;
            color: #2C3E50;
            margin: 1rem 0;
            line-height: 1.2;
        }}
        .post-meta {{
            color: #888;
            font-size: 0.9rem;
        }}
        .post-feature-img {{
            width: 100%;
            border-radius: 24px;
            margin: 1.5rem 0;
        }}
        .post-content {{
            font-size: 1.1rem;
            line-height: 1.7;
            color: #333;
        }}
        .post-content p {{
            margin-bottom: 1.2rem;
        }}
        .post-nav {{
            display: flex;
            justify-content: space-between;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(0,0,0,0.1);
        }}
        .post-nav a {{
            text-decoration: none;
            color: #E34C26;
            font-weight: 600;
        }}
        .back-to-blog {{
            text-align: center;
            margin-top: 2rem;
        }}
        .back-to-blog a {{
            display: inline-block;
            background: #E34C26;
            color: white;
            padding: 0.75rem 2rem;
            border-radius: 40px;
            text-decoration: none;
            font-weight: 600;
        }}
        @media (max-width: 768px) {{
            .post-container {{ padding: 1.5rem; margin: 1rem; }}
            .post-title {{ font-size: 1.8rem; }}
        }}
    </style>
</head>
<body>
    <div class="post-container">
        <div class="post-header">
            <div class="post-category">{category}</div>
            <h1 class="post-title">{title}</h1>
            <div class="post-meta">By Janis · 3 min read</div>
        </div>
        <img class="post-feature-img" src="{image_url}" alt="{title}">
        <div class="post-content">
            {content_paragraphs}
        </div>
        <div class="post-nav">
            <a href="{prev_link}">← Previous</a>
            <a href="{next_link}">Next →</a>
        </div>
        <div class="back-to-blog">
            <a href="../blog.html">← Back to Blog</a>
        </div>
    </div>
</body>
</html>"""

def main():
    print("📖 Generating blog from CSV...")
    
    # Create directories if they don't exist
    os.makedirs(ENGLISH_POSTS_DIR, exist_ok=True)
    os.makedirs(THAI_POSTS_DIR, exist_ok=True)
    os.makedirs("th", exist_ok=True)
    
    # Read posts from CSV
    posts = []
    with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            posts.append(row)
    
    # Generate individual post pages
    for i, post in enumerate(posts):
        slug = post['slug']
        
        # ===== ENGLISH VERSION =====
        content_html = post['content'].replace('\n\n', '</p><p>')
        content_html = '<p>' + content_html + '</p>'
        
        prev_link = f"{posts[i-1]['slug']}.html" if i > 0 else '#'
        next_link = f"{posts[i+1]['slug']}.html" if i < len(posts)-1 else '#'
        
        post_html = POST_TEMPLATE.format(
            title=post['title'],
            excerpt=post['excerpt'],
            category=post['category'],
            image_url=post['image_url'],
            content_paragraphs=content_html,
            prev_link=prev_link,
            next_link=next_link
        )
        
        output_file = f"{ENGLISH_POSTS_DIR}/{slug}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(post_html)
        print(f"✅ Generated English post: {output_file}")
        
        # ===== THAI VERSION =====
        if post.get('title_th') and post.get('content_th'):
            content_th_html = post['content_th'].replace('\n\n', '</p><p>')
            content_th_html = '<p>' + content_th_html + '</p>'
            
            thai_excerpt = post.get('excerpt_th', post['excerpt'])
            
            post_th_html = POST_TEMPLATE.format(
                title=post['title_th'],
                excerpt=thai_excerpt,
                category=post['category'],
                image_url=post['image_url'],
                content_paragraphs=content_th_html,
                prev_link=f"{posts[i-1]['slug']}.html" if i > 0 else '#',
                next_link=f"{posts[i+1]['slug']}.html" if i < len(posts)-1 else '#'
            )
            
            output_th_file = f"{THAI_POSTS_DIR}/{slug}.html"
            with open(output_th_file, 'w', encoding='utf-8') as f:
                f.write(post_th_html)
            print(f"✅ Generated Thai post: {output_th_file}")
    
    # Generate English listing page (blog.html)
    cards = []
    for post in posts:
        card = f"""
        <a href="blog/{post['slug']}.html" class="blog-card">
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
    with open(ENGLISH_LISTING, 'w', encoding='utf-8') as f:
        f.write(listing_html)
    print(f"✅ Generated English listing: {ENGLISH_LISTING}")
    
    # Generate Thai listing page (th/blog.html)
    thai_cards = []
    for post in posts:
        if post.get('title_th'):
            thai_excerpt = post.get('excerpt_th', post['excerpt'])
            thai_card = f"""
            <a href="blog/{post['slug']}.html" class="blog-card">
                <div class="blog-card-img">
                    <img src="{post['image_url']}" alt="{post['title_th']}">
                </div>
                <div class="blog-card-content">
                    <div class="blog-card-category">{post['category']}</div>
                    <h3 class="blog-card-title">{post['title_th']}</h3>
                    <p class="blog-card-excerpt">{thai_excerpt}</p>
                </div>
            </a>"""
            thai_cards.append(thai_card)
    
    if thai_cards:
        thai_listing_html = LISTING_TEMPLATE.format(cards='\n'.join(thai_cards))
        with open(THAI_LISTING, 'w', encoding='utf-8') as f:
            f.write(thai_listing_html)
        print(f"✅ Generated Thai listing: {THAI_LISTING}")
    
    print("🎉 Blog generation complete!")

if __name__ == "__main__":
    main()
