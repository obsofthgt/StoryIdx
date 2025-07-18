
import re
import shutil
import os



#Add the background image "bkgrnd.jpeg"
##Make the content block 50% transparent
#Make the left and right columns 50% transparent
#make the slide 505 transparent
#please resend the code

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

import re
import shutil
import os
import sys

# Configuration
CONFIG = {
    'input_path': "/Users/sri/Documents/iCloud-Obsidian/Documents/LIbravault/AA_Journal/Observations of Thoughts.md",
    'output_md': "oot.md",
    'output_html': "oot.html"
}

def copy_file(src, dst):
    """Copy a file from src to dst with error handling."""
    try:
        src = os.path.abspath(os.path.expanduser(src))
        dst = os.path.abspath(os.path.expanduser(dst))
        
        if not os.path.exists(src):
            raise FileNotFoundError(f"Source file '{src}' does not exist")
            
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        
        shutil.copy2(src, dst)  # copy2 preserves metadata
        print(f"Copied '{src}' to '{dst}'")
        return True
        
    except Exception as e:
        print(f"Error copying file: {str(e)}", file=sys.stderr)
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
            background: var(--primary-color);
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

        /* Arrow Containers */
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
            display: none;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s cubic-bezier(0.65, 0, 0.35, 1);
            cursor: pointer;
        }

        .arrow-container.left {
            left: 10px;
        }

        .arrow-container.right {
            right: 10px;
        }

        .arrow-container:hover {
            background: rgba(0,0,0,0.3);
        }

        .nav-arrow {
            width: 30px;
            height: 30px;
            border: solid var(--primary-color);
            border-width: 0 3px 3px 0;
            display: inline-block;
            transition: all 0.3s cubic-bezier(0.65, 0, 0.35, 1);
        }

        .nav-arrow.left {
            transform: rotate(135deg);
            margin-right: 5px;
        }

        .nav-arrow.right {
            transform: rotate(-45deg);
            margin-left: 5px;
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
            display: none;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 -5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s cubic-bezier(0.65, 0, 0.35, 1);
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
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: var(--primary-color);
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
            transition: all 0.2s cubic-bezier(0.65, 0, 0.35, 1);
        }

        .slider-track {
            position: absolute;
            height: 6px;
            background: var(--primary-color);
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
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            shape-outside: margin-box;
            transition: transform 0.3s cubic-bezier(0.65, 0, 0.35, 1);
        }

        .highlight-text {
            color: var(--primary-color);
            font-weight: 600;
            font-size: 1.2em;
            margin-bottom: 1.5em;
            display: inline-block;
            border-bottom: 2px solid var(--primary-color);
            padding-bottom: 5px;
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

IMAGE_BLOCK_TEMPLATE = """
    <div class="image-container PICPOS">
        <img src="FNAME" alt="Sample Image">
        <p><span class="highlight-text">CTR. TITLE</span></p>
        <p>story</p>
    </div>
"""

FOOTER_TEMPLATE = """
    <!-- Arrow Containers -->
    <div class="arrow-container left" id="left-arrow-container">
        <div class="nav-arrow left"></div>
    </div>
    <div class="arrow-container right" id="right-arrow-container">
        <div class="nav-arrow right"></div>
    </div>

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
            
            // Mouse movement detection for UI elements
            document.body.addEventListener('mousemove', (e) => {
                const bottomArea = window.innerHeight - 100;
                const sideArea = 100;
                
                // Show slider when mouse near bottom
                if (e.clientY > bottomArea) {
                    showUIElements();
                }
                // Show arrows when mouse near sides
                else if (e.clientX < sideArea || e.clientX > window.innerWidth - sideArea) {
                    showUIElements();
                }
            });
            
            // Auto-hide UI elements
            let uiTimeout;
            function showUIElements() {
                clearTimeout(uiTimeout);
                sliderContainer.style.display = 'flex';
                leftArrowContainer.style.display = 'flex';
                rightArrowContainer.style.display = 'flex';
                
                uiTimeout = setTimeout(() => {
                    sliderContainer.style.display = 'none';
                    leftArrowContainer.style.display = 'none';
                    rightArrowContainer.style.display = 'none';
                }, 3000);
            }

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

def process_markdown(content):
    """Process markdown content and return list of page HTMLs."""
    pages = []
    pattern = re.compile(r'!\[\[(.*?)\]\](.*?)(?=!\[\[|\Z)', re.DOTALL)
    
    for counter, match in enumerate(pattern.finditer(content), 1):
        image_filename = match.group(1).strip()
        content_block = match.group(2).strip()
        
        # Process image block
        page_html = IMAGE_BLOCK_TEMPLATE.replace('PICPOS', 'right' if counter % 2 else 'left')
        page_html = page_html.replace('FNAME', image_filename)
        page_html = page_html.replace('CTR', str(counter))
        
        # Extract and clean content
        title_match = re.search(r'<font[^>]*>(.*?)</font>', content_block)
        if title_match:
            page_html = page_html.replace('TITLE', title_match.group(1).strip())
            content_block = re.sub(r'<font[^>]*>.*?</font>', '', content_block)
            
        # Clean and format content
        cleaned_content = re.sub(r'<[^>]+>|\[\[.*?\]\]', '', content_block)
        cleaned_content = cleaned_content.replace('\n\n', '</p><p>')
        page_html = page_html.replace('<p>story</p>', f'<p>{cleaned_content}</p>')
        
        pages.append(f'<div class="page" id="page-{counter}">{page_html}</div>')
    
    return pages

def main():
    # Copy source file
    if not copy_file(CONFIG['input_path'], CONFIG['output_md']):
        sys.exit(1)
        
    # Read and process content
    try:
        with open(CONFIG['output_md'], 'r', encoding='utf-8') as f:
            pages = process_markdown(f.read())
    except Exception as e:
        print(f"Error processing markdown: {e}", file=sys.stderr)
        sys.exit(1)
        
    # Generate final HTML
    total_pages = len(pages)
    final_html = (
        HTML_TEMPLATE + 
        ''.join(pages) + 
        FOOTER_TEMPLATE.replace('TOTALPAGES', str(total_pages)))
    
    # Write output
    try:
        with open(CONFIG['output_html'], 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Created {CONFIG['output_html']} with {total_pages} pages")
    except Exception as e:
        print(f"Error writing HTML: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()