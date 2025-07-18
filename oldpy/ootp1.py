
import re
import shutil
import os

# Process the markdown file
# Now open file "oot.md" as read
# 1. Set counter = 1
# 2. Start a while loop to quit after reached end of file of "oot.md".     
# 
# - Only Read the block of text between two occurrences of "![[" and next "![[" in file "oot.md" or EOF whichever comes first and place into variable D. 
#     variable D should only contains the block of text starting at ![[ and stopping before the next ![[. Skips any content before the first ![[
# - Copy variable B to BT
# - If counter is even replace the string PICPOS in BT with "image-container-L", if counter is odd replace the string PICPOS in BT with "image-container-R"
# - Replace the string FNAME in BT with the image file name found between "![[" and "]]" in variable D. 
# - Remove "![[image file]]" from D
# - Replace the string CTR in BT with the value of counter. 
# - Replace the string TITLE in BT with the text found inside the font tag e.g <font color ….> text </font> tags in variable D
# - Remove the font tags and its text from variable D
# - Replace the string "story" in BT with the text remaining in variable D 
# - Set A = A + BT
# - Increment counter
# - Go to top of loop. 
# 
# 4. Once EOF is reached and the loop is exited then set A = A + C
# 5. Finally write the variable A into "oot.html". Overwrite "oot.html" if file exists. 

# CHanges:
# Title Page as First Page: Added a dedicated page-0 with your title content
# Pagination System:
#     - Each image/text block now lives in its own full-screen .page div
#     - Only one page visible at a time with smooth transitions
#     - Navigation Arrows:
#     - Appear when hovering over left/right 20% of screen
#     - Clicking arrows navigates between pages
#     - Visual arrow indicators using CSS triangles
#     - Swipe Gestures:
#     - Touchstart/touchend event listeners
#     - Left swipe = next page, Right swipe = previous page
#    -  50px threshold for swipe detection
# Dynamic Slider:
#     - Appears when mouse enters bottom 1/8 of screen
#     - Black background with opacity
#     - Shows current page/total pages
#     - Can drag to specific pages
#     - Auto-updates during navigation
#     - Responsive Design:
#     - Works on both mobile (touch) and desktop (mouse)
#     - Prevents accidental zooming with viewport meta tag
#     - Visual Improvements:
# Consistent 1.5em spacing between paragraphs
# Better floating image handling
# Smooth opacity transitions between pages
# The code maintains all your original content processing while adding the new navigation features. 
# The slider and page count are automatically calculated based on the number of entries found in your markdown file.
# 
# CHANGES:
#     - add Down key, right key and page down key for next page. 
#     - add up key, left key and page up key for prev page.
#     - Changed slider background to rgba(0,0,0,0.5)
#     - Added backdrop-filter: blur(5px) for frosted glass effect
# CHANGES:
# Combined Transitions:
# Book Flip: 
#     - 3D rotation on the Y-axis
#     - Fade + Scale: Subtle zoom effect
#     - Parallax: Background moves at different speed
# Visual Elements:
#     - Glass Morphism: Frosted content blocks with subtle borders
#     - Progress Bar: Minimal top indicator
#     - Responsive Images: Hover effects and proper scaling
# Performance Optimized:
#     - Hardware-accelerated transforms (transform: translateZ(0))
#     - Smooth cubic-bezier timing functions
#     - Backface visibility handling
# Enhanced Readability:
#     - Improved typography with Georgia font
#     - Consistent spacing system
#     - Mobile-responsive designimport re

def copy_file(src, dst):
    try:
        src = os.path.abspath(os.path.expanduser(src))
        dst = os.path.abspath(os.path.expanduser(dst))
        
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
            
        if not os.path.exists(src):
            print(f"Error: Source file '{src}' does not exist")
            return False
            
        if not os.path.exists(os.path.dirname(dst)):
            print(f"Error: Destination directory '{os.path.dirname(dst)}' does not exist")
            return False
            
        shutil.copy2(src, dst)
        print(f"Successfully copied '{src}' to '{dst}'")
        return True
        
    except Exception as e:
        print(f"Error copying file: {str(e)}")
        return False

A = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>Observations of Thought</title>
    <meta name="description" content="Sri Rao - Thoughts from reading, listening and walking in Chicago">
    <meta name="keywords" content="Sri Rao - Thoughts from reading, listening and walking in Chicago">
    <style>
        :root {
            --primary-accent: #f09e5a;
            --secondary-accent: #6d8b74;
            --text-color: #eae6ef;
            --bg-overlay: rgba(40, 40, 50, 0.4);
        }

        body {
            background-image: url('Bkgrnd.jpeg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center center;
            color: var(--text-color);
            font-family: 'Georgia', serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            overflow: hidden;
            touch-action: pan-y;
            perspective: 1000px;
        }

        /* Progress Indicator */
        .progress-bar {
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            background: var(--primary-accent);
            z-index: 100;
            transition: width 0.4s ease;
        }

        /* Page Transitions */
        .page {
            width: 100vw;
            height: 100vh;
            position: absolute;
            top: 0;
            left: 0;
            opacity: 0;
            overflow-y: auto;
            padding: 20px;
            box-sizing: border-box;
            transform-style: preserve-3d;
            transform-origin: left center;
            transition: all 0.8s cubic-bezier(0.22, 1, 0.36, 1);
            transform: translateX(10px) rotateY(5deg) scale(0.98);
            backface-visibility: hidden;
        }

        .page.active {
            opacity: 1;
            transform: translateX(0) rotateY(0deg) scale(1);
            z-index: 2;
        }

        .page.prev {
            transform: translateX(-5%) rotateY(-5deg);
        }

        /* Content Blocks */
        .content-block {
            background: var(--bg-overlay);
            backdrop-filter: blur(6px);
            border-radius: 12px;
            padding: 2em;
            margin: 1.5em auto;
            max-width: 800px;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            transform: translateZ(0);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .content-block:hover {
            transform: translateZ(10px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.2);
        }

        /* Navigation Arrows */
        .nav-arrow {
            position: fixed;
            top: 0;
            height: 100vh;
            width: 10vw;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: all 0.3s ease;
            cursor: pointer;
            backdrop-filter: blur(5px);
            background: rgba(0,0,0,0.1);
        }

        .nav-arrow.left {
            left: 0;
        }

        .nav-arrow.right {
            right: 0;
        }

        .nav-arrow:hover {
            opacity: 1;
            background: rgba(0,0,0,0.2);
        }

        .nav-arrow::after {
            content: "";
            border: solid rgba(255,255,255,0.9);
            border-width: 0 4px 4px 0;
            display: inline-block;
            padding: 15px;
            transition: all 0.2s ease;
        }

        .left::after {
            transform: rotate(135deg) scale(1.2);
            margin-left: 10px;
        }

        .right::after {
            transform: rotate(-45deg) scale(1.2);
            margin-right: 10px;
        }

        .nav-arrow:hover::after {
            border-color: var(--primary-accent);
        }

        /* Permanent Bottom Slider */
        .bottom-slider {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 80px;
            background: rgba(0,0,0,0.3);
            z-index: 20;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            backdrop-filter: blur(5px);
            border-top: 1px solid rgba(255,255,255,0.1);
            padding: 10px 0;
        }

        .slider {
            width: 90%;
            margin: 5px auto;
            -webkit-appearance: none;
            height: 6px;
            background: rgba(255,255,255,0.3);
            border-radius: 3px;
            outline: none;
        }

        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: var(--primary-accent);
            cursor: pointer;
            border: 2px solid white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .slider-info {
            color: white;
            font-size: 1.1em;
            margin-top: 8px;
            font-weight: 500;
        }

        /* Typography */
        .highlight-text {
            color: var(--primary-accent);
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 1.5em;
        }

        p {
            margin-bottom: 1.5em;
            text-align: left;
            line-height: 1.7;
        }

        /* Images */
        .image-container {
            width: 60%;
            margin: 1.5em auto;
            overflow: hidden;
            display: flex;
            justify-content: center;
        }

        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            object-fit: contain;
        }

        .image-container:hover img {
            transform: scale(1.02);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        /* Responsive Adjustments */
        @media (max-width: 768px) {
            .content-block {
                padding: 1.5em;
                margin: 1em auto;
            }
            
            .image-container {
                width: 80%;
                margin: 1em auto;
            }
            
            .nav-arrow {
                width: 15vw;
            }
            
            .bottom-slider {
                height: 70px;
            }
        }
    </style>
</head>
<body>
    <!-- Progress Indicator -->
    <div class="progress-bar" id="progress-bar"></div>

    <!-- Title Page -->
    <div class="page active" id="page-0">
        <div class="content-block" style="text-align: center; background: rgba(30,30,40,0.6);">
            <h1 style="font-size: 2.5em; margin: 0;">Observations of Thought</h1>
            <h2 style="font-size: 1.2em; margin: 0.5em 0;">Listen, Read, Walk</h2>
            <h3 style="font-size: 1.3em; margin: 0;">~***~</h3>
        </div>
    </div>
"""

B = """
    <div class="content-block">
        <div class="image-container">
            <img src="FNAME" alt="Sample Image">
        </div>
        <p><span class="highlight-text">CTR. TITLE</span></p>
        <p>story</p>
    </div>
"""

C = """
    <!-- Navigation Arrows -->
    <div class="nav-arrow left" id="prev-arrow"></div>
    <div class="nav-arrow right" id="next-arrow"></div>

    <!-- Permanent Bottom Slider -->
    <div class="bottom-slider">
        <input type="range" min="0" max="TOTALPAGES" value="0" class="slider" id="page-slider">
        <div class="slider-info">Page <span id="current-page">1</span> of <span id="total-pages">TOTALPAGES</span></div>
    </div>

    <script>
        let currentPage = 0;
        const totalPages = TOTALPAGES;
        const pages = document.querySelectorAll('.page');
        const progressBar = document.getElementById('progress-bar');
        const pageSlider = document.getElementById('page-slider');
        
        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            updateProgress();
            setupEventListeners();
            updateSlider();
        });

        function setupEventListeners() {
            // Navigation arrows
            document.getElementById('next-arrow').addEventListener('click', nextPage);
            document.getElementById('prev-arrow').addEventListener('click', prevPage);
            
            // Slider input
            pageSlider.addEventListener('input', (e) => {
                goToPage(parseInt(e.target.value));
            });
            
            // Keyboard navigation
            document.addEventListener('keydown', (e) => {
                switch(e.key) {
                    case 'ArrowRight': case 'ArrowDown': case 'PageDown': nextPage(); break;
                    case 'ArrowLeft': case 'ArrowUp': case 'PageUp': prevPage(); break;
                }
            });
            
            // Touch swipe
            let touchStartX = 0;
            document.addEventListener('touchstart', (e) => touchStartX = e.touches[0].clientX);
            document.addEventListener('touchend', (e) => {
                const touchEndX = e.changedTouches[0].clientX;
                if (touchStartX - touchEndX > 50) nextPage();
                if (touchEndX - touchStartX > 50) prevPage();
            });
        }

        function goToPage(pageNum) {
            if (pageNum < 0 || pageNum > totalPages) return;
            
            // Update page transitions
            pages[currentPage].classList.remove('active');
            pages[currentPage].classList.add('prev');
            
            currentPage = pageNum;
            
            pages[currentPage].classList.add('active');
            pages[currentPage].classList.remove('prev');
            
            updateProgress();
            updateSlider();
        }

        function nextPage() { 
            if (currentPage < totalPages) goToPage(currentPage + 1); 
        }
        
        function prevPage() { 
            if (currentPage > 0) goToPage(currentPage - 1); 
        }
        
        function updateProgress() {
            progressBar.style.width = `${(currentPage / totalPages) * 100}%`;
        }
        
        function updateSlider() {
            pageSlider.value = currentPage;
            document.getElementById('current-page').textContent = currentPage + 1;
            document.getElementById('total-pages').textContent = totalPages;
        }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    copy_file("/Users/sri/Documents/iCloud-Obsidian/Documents/LIbravault/AA_Journal/Observations of Thoughts.md", 
              "/Users/sri/Documents/iCloud-Obsidian/Documents/LIbravault/AA_Journal/WalkingNotes/Img_wn/oot.md")

    counter = 1
    pages = []

    try:
        with open('oot.md', 'r', encoding='utf-8') as md_file:
            content = md_file.read()
            pattern = re.compile(r'!\[\[(.*?)\]\](.*?)(?=!\[\[|\Z)', re.DOTALL)
            
            for match in pattern.finditer(content):
                image_filename = match.group(1).strip()
                D = match.group(2).strip()
                
                BT = B.replace('FNAME', image_filename)
                BT = BT.replace('CTR', str(counter))
                
                title_match = re.search(r'<font[^>]*>(.*?)</font>', D)
                title_text = title_match.group(1).strip() if title_match else ''
                BT = BT.replace('TITLE', title_text)
                
                D = re.sub(r'<font[^>]*>.*?</font>', '', D, flags=re.DOTALL)
                story_content = D.strip()
                story_content = re.sub(r'<[^>]+>', '', story_content)
                story_content = re.sub(r'\[\[.*?\]\]', '', story_content)
                story_content = story_content.replace('\n\n', '</p><p style="margin-bottom:1.5em;">')
                story_content = story_content.replace('\n', '<br style="display:block; margin-bottom:0.75em;">')
                story_content = f"<p style=\"margin-bottom:1.5em;\">{story_content}</p>"
                
                BT = BT.replace('<p>story</p>', story_content)
                pages.append(f'<div class="page" id="page-{counter}">{BT}</div>')
                counter += 1
                
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

    A += ''.join(pages)
    total_pages = counter - 1
    A = A.replace('TOTALPAGES', str(total_pages))
    C = C.replace('TOTALPAGES', str(total_pages))

    try:
        with open('oot.html', 'w', encoding='utf-8') as html_file:
            html_file.write(A + C)
        print(f"Created oot.html with {total_pages} pages")
    except Exception as e:
        print(f"Error writing file: {e}")