
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
# Book Flip: please add 
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

# please modify 
#     - Fade + Scale: Subtle zoom effec
#     - Glass Morphism: Frosted content blocks with subtle borders
#     - Progress Bar: Minimal top indicator
#     - improve styling of left and right arrow columns
#     - Improve styling of slider bar
# 
# Add the background image "bkgrnd.jpeg"
# Make the content block 50% transparent
# Make the left and right columns 50% transparent
# make the slide 505 transparent
# please resend the code

#1. Change content black and slider to rgba(0,0,0,.2) to give a frosted glass semi transparent Look
#2. only show one page at a time. it seems like prior page images are visible through current page
#3. please confirm left and right swipes work
#4. please resend code

# Add Smooth cubic-bezier timing for page transitions and for slider appear disapper
# change width of slider to same as content block
# change height of slider bar to 50%
# Ad 10px margin between bottom of slider and bottom of page
# change scroll bar on content block to rgba(0,0,0,.2)
# IMprove typography with Georgia font
# Resend entire code

# Custom scroll bar is not working. Please fix
# add hide / appear for right and left arows.
# have left and right arrows sit inside  a  block similar to the slider bar
# have the  block appear and dissappear like to slider bar
# make the hieght of block be the same as the conten block and its wdith be the same as the slider height and have a 10 px margin from the end of the
# resend entire code 

# Make the right arrow block appear only when the mouse hovers over its area and have it diappear when the mouse leaves its area
# Make the Left arrow block appear only when the mouse hovers over its area and have it dissapper when the mouse leaves its area
# have both left and right arrows centered inside thier blocks
# Make the slider appear only when the mouse hovers over its area and have it dissapper when the mouse leaves its area
# Please resend the entire Code

# reduce the size of the left and right arrows to half its size. DO not change the size of their blocks
# remove borders from the slider, the left arrow block and the right arrow block
# resend the entire code

# whenever there is a new line in the content block replace it with <br><br>
# resend entire code

# replace "thought 1...21" on each page in the content block with the text in the <font .....> ... </font> tags in the content as was before
# resend entire code

# Reduce the gap between the TITLE (that between the font tags) and the start of the rest of the texxt to half what it is now
# moving the slider does not change the page. please fix
# resend entire code

# the gap between the TITLE (that between the font tags) in the content block and the start of the rest of the texxt to half 
# what it is now
# get the image in the content blockto fade and scale and put a dark shadow behind it
# resend the entire code

# Get the image shadow to be more pronounced when mouse hovers on it.
# Put the page number on the top right corner of the content block, juust left of the scroll bar
# Make the font size of the page number 1/2 the size of the test in the content block. use a times roman font. 
# do not display page # for the first page
# Make the labels progress line on the slider bar black
# make the progress line on the top black.
# make the Left and right arrrow black
# resend the entore code

# increase the page number font size by 25%
# change the circle in the slider bar to 2 vertical lines (like a slider button.) Make it black
# add a flag COPY_ENABLE. set default to 1. when set to 1, the function copy_file is called. 
# If COPY_ENABLE Set to 0, then function copy_file is skipped.
# add a flag ARW_DISPLAY. Set default to 1. do nothing. keep current functionality.
# if ARW_DISPLAY set to 0, the arrow blocks do not appear. they remain hidden, However the functionality is maintained.
# resend entire code

# if ARW_DISPLAY set to 0, keep both the arrow blocks and the both arrows hidden on mouse hover, but enable the page change on mouse hover
# make no change to ARW_DISPLAY = 1
# resend entire code

# when arrow ARW_DISPLAY=0 click functionality must work in original arrow positions and original arrow block positions. please fix and resend entire code.

import re
import shutil
import os
import sys
import logging
from pathlib import Path
from html import escape

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('conversion.log'),
        logging.StreamHandler()
    ]
)

# Configuration
CONFIG = {
    'input_path': "/Users/sri/Documents/iCloud-Obsidian/Documents/LIbravault/AA_Journal/MyBooks/Observations of Thoughts.md",
    'output_md': "oot.md",
    'output_html': "oot.html",
    'COPY_ENABLE': 1,  # 1 to enable file copying, 0 to disable
    'ARW_DISPLAY': 1   # 1 to show arrow blocks and arrows, 0 to hide everything (but keep clickable)
}

def validate_config():
    """Validate the configuration dictionary"""
    required_keys = ['input_path', 'output_md', 'output_html', 'COPY_ENABLE', 'ARW_DISPLAY']
    for key in required_keys:
        if key not in CONFIG:
            raise ValueError(f"Missing required config key: {key}")

def copy_file(src, dst):
    """Copy a file from src to dst with error handling."""
    try:
        src_path = Path(src).expanduser().resolve()
        dst_path = Path(dst).expanduser().resolve()
        
        if not src_path.exists():
            raise FileNotFoundError(f"Source file '{src_path}' does not exist")
            
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_path, dst_path)
        logging.info(f"Copied '{src_path}' to '{dst_path}'")
        return True
        
    except Exception as e:
        logging.error(f"Error copying file: {str(e)}")
        return False

# HTML Template with all requested changes
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>Observations of Thought</title>
    <meta name="description" content="Sri Rao - Thoughts from reading, listening and walking in Chicago">
    <meta name="keywords" content="Sri Rao - Thoughts from reading, listening and walking in Chicago">
    <style>
        :root {
            --primary-color: #f09e5a;
            --glass-bg: rgba(0, 0, 0, 0.2);
            --glass-border: rgba(255, 255, 255, 0.1);
            --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            --text-color: #fff;
            --arrow-block-display: ARW_DISPLAY;
            --arrow-visibility: ARW_VISIBILITY;
            --arrow-opacity: ARW_OPACITY;
            --arrow-hover-opacity: ARW_HOVER_OPACITY;
        }

        body {
            background-image: url('bkgrnd.jpeg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: var(--text-color);
            font-family: Georgia, 'Times New Roman', Times, serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            overflow: hidden;
            touch-action: pan-y;
        }

        /* Progress Bar */
        .progress-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: rgba(0,0,0,0.1);
            z-index: 100;
        }

        .progress-bar {
            height: 100%;
            background: #000;
            width: 0%;
            transition: width 0.4s cubic-bezier(0.65, 0, 0.35, 1);
        }

        .page {
            width: 85vw;
            height: 85vh;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0.95);
            opacity: 0;
            overflow-y: auto;
            padding: 40px;
            box-sizing: border-box;
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-radius: 12px;
            border: 1px solid var(--glass-border);
            box-shadow: var(--glass-shadow);
            transition: all 0.6s cubic-bezier(0.65, 0, 0.35, 1);
            z-index: 1;
            display: none;
        }

        /* Page number (top-right corner) */
        .page-number {
            position: absolute;
            top: 20px;
            right: 20px;
            font-family: 'Times New Roman', Times, serif;
            font-size: 0.625em;
            color: rgba(255, 255, 255, 0.7);
            z-index: 3;
        }

        /* Fixed Custom Scrollbar */
        .page::-webkit-scrollbar {
            width: 10px;
        }

        .page::-webkit-scrollbar-track {
            background: transparent;
        }

        .page::-webkit-scrollbar-thumb {
            background-color: rgba(0,0,0,0.2);
            border-radius: 10px;
            border: 2px solid transparent;
            background-clip: content-box;
        }

        .page::-webkit-scrollbar-thumb:hover {
            background-color: rgba(0,0,0,0.3);
        }

        .page.active {
            opacity: 1;
            transform: translate(-50%, -50%) scale(1);
            z-index: 2;
            display: block;
        }

        .page.exit {
            transform: translate(-50%, -50%) scale(0.98);
            opacity: 0;
            display: none;
        }

        .heading-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100%;
            gap: 1rem;
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }

        /* Arrow Containers - Always present but visibility controlled */
        .arrow-container {
            position: fixed;
            top: 50%;
            transform: translateY(-50%);
            height: 85vh;
            width: 40px;
            background: rgba(0,0,0,0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            cursor: pointer;
            opacity: var(--arrow-opacity);
            transition: all 0.3s ease;
            pointer-events: auto;
        }

        .arrow-container.left {
            left: 10px;
        }

        .arrow-container.right {
            right: 10px;
        }

        .arrow-container:hover {
            opacity: var(--arrow-hover-opacity);
        }

        .nav-arrow {
            width: 15px;
            height: 15px;
            border: solid #000;
            border-width: 0 3px 3px 0;
            display: inline-block;
            visibility: var(--arrow-visibility);
        }

        .nav-arrow.left {
            transform: rotate(135deg);
        }

        .nav-arrow.right {
            transform: rotate(-45deg);
        }

        /* Arrow Hover Areas - Always present but visibility controlled */
        .arrow-area {
            position: fixed;
            top: 0;
            height: 100%;
            width: 60px;
            z-index: 9;
            display: flex;
            pointer-events: auto;
        }

        .arrow-area.left {
            left: 0;
        }

        .arrow-area.right {
            right: 0;
        }

        .arrow-area.left:hover ~ .arrow-container.left {
            opacity: var(--arrow-hover-opacity);
        }

        .arrow-area.right:hover ~ .arrow-container.right {
            opacity: var(--arrow-hover-opacity);
        }

        /* Slider Container */
        .slider-container {
            position: fixed;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 85vw;
            height: 40px;
            background: rgba(0,0,0,0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            z-index: 20;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            box-shadow: 0 -5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s cubic-bezier(0.65, 0, 0.35, 1);
            opacity: 0;
            pointer-events: none;
        }

        .slider-area {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 60px;
            z-index: 19;
        }

        .slider-area:hover ~ .slider-container,
        .slider-container:hover {
            opacity: 1;
            pointer-events: auto;
        }

        .slider-wrapper {
            width: 80%;
            position: relative;
            margin: 0 auto;
        }

        .slider {
            width: 100%;
            margin: 10px auto;
            -webkit-appearance: none;
            height: 6px;
            background: rgba(255,255,255,0.2);
            border-radius: 10px;
            outline: none;
            transition: all 0.3s cubic-bezier(0.65, 0, 0.35, 1);
        }

        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 8px;
            height: 20px;
            background: #000;
            cursor: pointer;
            border-radius: 0;
            box-shadow: none;
            transition: all 0.2s cubic-bezier(0.65, 0, 0.35, 1);
        }

        .slider-track {
            position: absolute;
            height: 6px;
            background: #000;
            border-radius: 10px;
            top: 50%;
            transform: translateY(-50%);
            left: 0;
            pointer-events: none;
        }

        /* Content Styles */
        .image-container {
            width: 90%;
            margin: 30px auto;
            overflow: hidden;
            position: relative;
        }

        .image-container img {
            float: left;
            margin: 0 25px 20px 0;
            max-width: 50%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            shape-outside: margin-box;
            transition: all 0.5s cubic-bezier(0.65, 0, 0.35, 1);
            opacity: 0.95;
            transform: scale(0.98);
            filter: drop-shadow(0 4px 12px rgba(0,0,0,0.6));
        }

        .image-container img:hover {
            opacity: 1;
            transform: scale(1);
            box-shadow: 0 15px 35px rgba(0,0,0,0.9);
            filter: drop-shadow(0 8px 20px rgba(0,0,0,0.8));
        }

        .highlight-text {
            color: var(--primary-color);
            font-weight: 600;
            font-size: 1.2em;
            margin-bottom: 0.3em;
            display: inline-block;
            border-bottom: 2px solid var(--primary-color);
            padding-bottom: 3px;
        }

        p {
            margin-bottom: 1.8em;
            text-align: left;
            line-height: 1.7;
            font-size: 1.05em;
        }

        h1 {
            font-size: 2.8em;
            margin: 0 0 10px 0;
            color: #fff;
            font-weight: 700;
        }

        h2 {
            font-size: 1.4em;
            margin: 0;
            font-weight: 400;
            color: rgba(255,255,255,0.8);
        }

        h3 {
            font-size: 1.3em;
            margin: 20px 0;
            font-weight: 300;
            color: rgba(255,255,255,0.7);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.95); }
            to { opacity: 0.95; transform: scale(0.98); }
        }

        .page.active .image-container img {
            animation: fadeIn 0.8s cubic-bezier(0.65, 0, 0.35, 1) forwards;
        }
    </style>
</head>
<body>
    <!-- Progress Bar -->
    <div class="progress-container">
        <div class="progress-bar" id="progress-bar"></div>
    </div>

    <!-- Title Page -->
    <div class="page active" id="page-0">
        <div class="heading-container">
            <h1>Observations of Thought</h1>
            <h2>Listen, Read, Walk</h2>
            <h3>~***~</h3>
        </div>
    </div>
"""

FOOTER_TEMPLATE = """
    <!-- Arrow Hover Areas - Always present -->
    <div class="arrow-area left"></div>
    <div class="arrow-area right"></div>
    
    <!-- Arrow Containers - Always present -->
    <div class="arrow-container left" id="left-arrow-container">
        <div class="nav-arrow left"></div>
    </div>
    <div class="arrow-container right" id="right-arrow-container">
        <div class="nav-arrow right"></div>
    </div>

    <!-- Slider Hover Area -->
    <div class="slider-area"></div>
    
    <!-- Slider Container -->
    <div class="slider-container" id="slider-container">
        <div class="slider-wrapper">
            <div class="slider-track" id="slider-track"></div>
            <input type="range" min="0" max="TOTALPAGES" value="0" class="slider" id="page-slider">
        </div>
        <div class="slider-info">
            <span id="current-page">1</span>/<span id="total-pages">TOTALPAGES</span>
        </div>
    </div>

    <script>
        let currentPage = 0;
        const totalPages = TOTALPAGES;
        const pages = document.querySelectorAll('.page');
        const slider = document.getElementById('page-slider');
        const sliderTrack = document.getElementById('slider-track');
        const progressBar = document.getElementById('progress-bar');
        const currentPageDisplay = document.getElementById('current-page');
        const totalPagesDisplay = document.getElementById('total-pages');
        const leftArrowContainer = document.getElementById('left-arrow-container');
        const rightArrowContainer = document.getElementById('right-arrow-container');
        const sliderContainer = document.getElementById('slider-container');

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            totalPagesDisplay.textContent = totalPages;
            updateSlider();
            updateProgress();
            
            // Add page numbers to all pages except the first
            for (let i = 1; i < pages.length; i++) {
                const pageNumber = document.createElement('div');
                pageNumber.className = 'page-number';
                pageNumber.textContent = i;
                pages[i].appendChild(pageNumber);
            }
            
            // Touch events for swipe
            let touchStartX = 0;
            let touchEndX = 0;
            let touchStartTime = 0;
            
            document.body.addEventListener('touchstart', (e) => {
                touchStartX = e.changedTouches[0].screenX;
                touchStartTime = Date.now();
            }, { passive: true });
            
            document.body.addEventListener('touchend', (e) => {
                touchEndX = e.changedTouches[0].screenX;
                const touchDuration = Date.now() - touchStartTime;
                handleSwipe(touchDuration);
            }, { passive: true });
            
            // Keyboard navigation
            document.addEventListener('keydown', (e) => {
                switch(e.key) {
                    case 'ArrowRight':
                    case 'ArrowDown':
                    case 'PageDown':
                        nextPage();
                        break;
                    case 'ArrowLeft':
                    case 'ArrowUp':
                    case 'PageUp':
                        prevPage();
                        break;
                }
            });

            // Update slider track fill
            slider.addEventListener('input', updateSliderTrack);
            updateSliderTrack();
            
            // Connect slider to page navigation
            slider.addEventListener('change', function() {
                goToPage(parseInt(this.value));
            });
            
            // Arrow click events
            leftArrowContainer.addEventListener('click', prevPage);
            rightArrowContainer.addEventListener('click', nextPage);
        });

        function updateSliderTrack() {
            const value = slider.value;
            const max = slider.max;
            const percent = (value / max) * 100;
            sliderTrack.style.width = `${percent}%`;
        }

        function goToPage(pageNum) {
            if (pageNum < 0 || pageNum >= pages.length) return;
            
            const currentActive = pages[currentPage];
            currentActive.classList.remove('active');
            currentActive.classList.add('exit');
            
            setTimeout(() => {
                currentActive.classList.remove('exit');
                currentPage = pageNum;
                pages[currentPage].classList.add('active');
                updateSlider();
                updateProgress();
            }, 300);
        }

        function nextPage() {
            if (currentPage < totalPages) goToPage(currentPage + 1);
        }

        function prevPage() {
            if (currentPage > 0) goToPage(currentPage - 1);
        }

        function handleSwipe(duration) {
            const distance = touchStartX - touchEndX;
            const absDistance = Math.abs(distance);
            const isFastSwipe = duration < 300 && absDistance > 50;
            const isSlowSwipe = duration >= 300 && absDistance > 100;
            
            if (isFastSwipe || isSlowSwipe) {
                if (distance > 0) {
                    nextPage();
                } else {
                    prevPage();
                }
            }
        }

        function updateSlider() {
            slider.value = currentPage;
            currentPageDisplay.textContent = currentPage + 1;
            updateSliderTrack();
        }

        function updateProgress() {
            const progress = (currentPage / totalPages) * 100;
            progressBar.style.width = `${progress}%`;
        }
    </script>
</body>
</html>
"""

def extract_title(content):
    """Extract title from <font> tags in the content"""
    title_match = re.search(r'<font[^>]*>(.*?)</font>', content)
    if title_match:
        return title_match.group(1).strip()
    return None

def clean_content(content):
    """Clean and format the content block with proper line breaks"""
    # First extract the title if it exists
    title = extract_title(content)
    
    # Remove Obsidian-specific syntax
    content = re.sub(r'\[\[.*?\]\]', '', content)  # Remove wikilinks
    content = re.sub(r'#\w+', '', content)  # Remove tags
    
    # Remove the <font> tags if they exist
    content = re.sub(r'<font[^>]*>.*?</font>', '', content)
    
    # Preserve basic markdown formatting
    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
    content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', content)
    
    # Replace newlines with <br><br>
    content = content.replace('\n', '<br><br>')
    
    return title, content.strip()

def build_page_html(counter, image_filename, title, content):
    """Build HTML for a single page with proper escaping"""
    position = 'right' if counter % 2 else 'left'
    
    # Use the extracted title if available, otherwise use default
    page_title = escape(title) if title else f"Thought {counter}"
    
    return f"""
    <div class="page" id="page-{counter}">
        <div class="image-container {position}">
            <img src="{escape(image_filename)}" alt="Image {counter}">
            <p><span class="highlight-text">{page_title}</span></p>
            <p>{content}</p>
        </div>
    </div>
    """

def process_markdown(content):
    """Process markdown content and return list of page HTMLs."""
    pages = []
    try:
        pattern = re.compile(
            r'!\[\[(?P<image>.*?)\]\](?P<content>.*?)(?=!\[\[|\Z)', 
            re.DOTALL
        )
        
        for counter, match in enumerate(pattern.finditer(content), 1):
            image_filename = match.group('image').strip()
            content_block = match.group('content').strip()
            
            if not image_filename:
                logging.warning(f"Empty image filename at position {counter}")
                continue
                
            title, cleaned_content = clean_content(content_block)
            if not cleaned_content:
                logging.warning(f"Empty content block for image {image_filename}")
                continue
                
            pages.append(build_page_html(counter, image_filename, title, cleaned_content))
            
    except Exception as e:
        logging.error(f"Markdown processing failed: {str(e)}")
        raise
        
    return pages

def build_final_html(pages):
    """Assemble the final HTML document"""
    total_pages = len(pages)
    footer = FOOTER_TEMPLATE.replace('TOTALPAGES', str(total_pages))
    
    # Set arrow display properties based on config
    if CONFIG['ARW_DISPLAY']:
        # Show blocks and arrows with hover effects
        html_template = HTML_TEMPLATE\
            .replace('ARW_DISPLAY', 'flex')\
            .replace('ARW_VISIBILITY', 'visible')\
            .replace('ARW_OPACITY', '0')\
            .replace('ARW_HOVER_OPACITY', '1')
    else:
        # Hide arrows but keep containers clickable
        html_template = HTML_TEMPLATE\
            .replace('ARW_DISPLAY', 'flex')\
            .replace('ARW_VISIBILITY', 'hidden')\
            .replace('ARW_OPACITY', '0')\
            .replace('ARW_HOVER_OPACITY', '0')
    
    return html_template + '\n'.join(pages) + footer

def main():
    try:
        validate_config()
        
        input_path = Path(CONFIG['input_path']).expanduser().resolve()
        output_md = Path(CONFIG['output_md']).expanduser().resolve()
        output_html = Path(CONFIG['output_html']).expanduser().resolve()
        
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
        # Copy the markdown file if enabled
        if CONFIG['COPY_ENABLE']:
            output_md.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(input_path, output_md)
            logging.info(f"Copied {input_path} to {output_md}")
        
        # Process content
        content = input_path.read_text(encoding='utf-8')
        pages = process_markdown(content)
        
        # Generate HTML
        final_html = build_final_html(pages)
        output_html.write_text(final_html, encoding='utf-8')
        logging.info(f"Created {output_html} with {len(pages)} pages")
        
    except Exception as e:
        logging.error(f"Conversion failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()