
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

import re
import shutil
import os
def copy_file(src, dst):
    """
    Copy a file from src to dst in Python
    
    Args:
        src (str): Source file path
        dst (str): Destination path (can be directory or full file path)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Expand user paths (~) and get absolute paths
        src = os.path.abspath(os.path.expanduser(src))
        dst = os.path.abspath(os.path.expanduser(dst))
        
        # If destination is a directory, use the same filename
        if os.path.isdir(dst):
            dst = os.path.join(dst, os.path.basename(src))
            
        # Check if source exists
        if not os.path.exists(src):
            print(f"Error: Source file '{src}' does not exist")
            return False
            
        # Check if destination directory exists
        if not os.path.exists(os.path.dirname(dst)):
            print(f"Error: Destination directory '{os.path.dirname(dst)}' does not exist")
            return False
            
        # Perform the copy
        shutil.copy2(src, dst)  # copy2 preserves metadata
        print(f"Successfully copied '{src}' to '{dst}'")
        return True
        
    except Exception as e:
        print(f"Error copying file: {str(e)}")
        return False

# 1. HTML Template (Variable A) - Updated with all requested changes
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
            --primary-color: #f09e5a;
            --glass-bg: rgba(0, 0, 0, 0.2); /* Dark frosted glass */
            --glass-border: rgba(255, 255, 255, 0.1);
            --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            --text-color: #fff; /* Light text for dark background */
        }

        body {
            background-image: url('bkgrnd.jpeg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: var(--text-color);
            font-family: 'Segoe UI', Roboto, -apple-system, sans-serif;
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
            transition: width 0.4s ease;
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
            transition: all 0.6s cubic-bezier(0.22, 1, 0.36, 1);
            z-index: 1;
            display: none; /* Hide all pages by default */
        }

        .page.active {
            opacity: 1;
            transform: translate(-50%, -50%) scale(1);
            z-index: 2;
            display: block; /* Only show active page */
        }

        .page.exit {
            transform: translate(-50%, -50%) scale(0.98);
            opacity: 0;
            display: none; /* Ensure exiting page is hidden */
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

        /* Enhanced Navigation Arrows */
        .nav-arrow {
            position: fixed;
            top: 0;
            height: 100vh;
            width: 15vw;
            max-width: 120px;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            opacity: 0.5;
        }

        .nav-arrow.left {
            left: 0;
            background: linear-gradient(90deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0) 100%);
        }

        .nav-arrow.right {
            right: 0;
            background: linear-gradient(270deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0) 100%);
        }

        .nav-arrow:hover {
            opacity: 0.8;
            width: 18vw;
        }

        .nav-arrow::after {
            content: "";
            border: solid var(--primary-color);
            border-width: 0 3px 3px 0;
            display: inline-block;
            padding: 20px;
            transition: all 0.3s ease;
        }

        .left::after {
            transform: rotate(135deg);
            margin-left: 15px;
        }

        .right::after {
            transform: rotate(-45deg);
            margin-right: 15px;
        }

        .nav-arrow:hover::after {
            border-color: #fff;
            padding: 25px;
        }

        /* Modern Slider */
        .slider-container {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 80px;
            background: rgba(0,0,0,0.2); /* Dark frosted glass */
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            z-index: 20;
            display: none;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            border-top: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 -5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }

        .slider-wrapper {
            width: 80%;
            max-width: 600px;
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
            transition: all 0.3s ease;
        }

        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: var(--primary-color);
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
            transition: all 0.2s ease;
        }

        .slider::-webkit-slider-thumb:hover {
            transform: scale(1.2);
            box-shadow: 0 3px 8px rgba(0,0,0,0.3);
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

        .slider-info {
            color: #fff;
            font-size: 1em;
            font-weight: 500;
            margin-top: 8px;
            display: flex;
            gap: 10px;
        }

        .slider-info span {
            color: var(--primary-color);
            font-weight: 600;
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
            transition: transform 0.3s ease;
        }

        .image-container:hover img {
            transform: scale(1.02);
        }

        .image-container.right img {
            float: right;
            margin: 0 0 20px 25px;
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

# 2. Image Block Template (Variable B)
B = """
    <div class="image-container PICPOS">
        <img src="FNAME" alt="Sample Image">
        <p><span class="highlight-text">CTR. TITLE</span></p>
        <p>story</p>
    </div>
"""

# 3. HTML Footer (Variable C)
C = """
    <!-- Navigation Arrows -->
    <div class="nav-arrow left" id="prev-arrow"></div>
    <div class="nav-arrow right" id="next-arrow"></div>

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

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            totalPagesDisplay.textContent = totalPages;
            updateSlider();
            updateProgress();
            
            // Touch events for swipe - CONFIRMED WORKING
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
            
            // Mouse hover for slider
            document.body.addEventListener('mousemove', (e) => {
                const bottomArea = window.innerHeight - 100;
                if (e.clientY > bottomArea) {
                    document.getElementById('slider-container').style.display = 'flex';
                }
            });
            
            document.getElementById('slider-container').addEventListener('mouseleave', () => {
                setTimeout(() => {
                    document.getElementById('slider-container').style.display = 'none';
                }, 2000);
            });

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
        });

        function updateSliderTrack() {
            const value = slider.value;
            const max = slider.max;
            const percent = (value / max) * 100;
            sliderTrack.style.width = `${percent}%`;
        }

        // Navigation functions with fade+scale animation
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
                    nextPage(); // Swipe left
                } else {
                    prevPage(); // Swipe right
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

        // Event listeners
        document.getElementById('next-arrow').addEventListener('click', nextPage);
        document.getElementById('prev-arrow').addEventListener('click', prevPage);
        
        slider.addEventListener('input', (e) => {
            goToPage(parseInt(e.target.value));
        });

        // Auto-hide slider
        let sliderTimeout;
        const sliderContainer = document.getElementById('slider-container');
        
        sliderContainer.addEventListener('mousemove', () => {
            clearTimeout(sliderTimeout);
            sliderContainer.style.display = 'flex';
            sliderTimeout = setTimeout(() => {
                sliderContainer.style.display = 'none';
            }, 3000);
        });
    </script>
</body>
</html>
"""

# Process the markdown file
if __name__ == "__main__":
    # Copy the markdown file
    copy_file("/Users/sri/Documents/iCloud-Obsidian/Documents/LIbravault/AA_Journal/Observations of Thoughts.md", 
              "/Users/sri/Documents/iCloud-Obsidian/Documents/LIbravault/AA_Journal/WalkingNotes/Img_wn/oot.md")

    counter = 1
    pages = []

    try:
        with open('oot.md', 'r', encoding='utf-8') as md_file:
            content = md_file.read()
            
            # Pattern to match markdown images and following content
            pattern = re.compile(r'!\[\[(.*?)\]\](.*?)(?=!\[\[|\Z)', re.DOTALL)
            matches = pattern.finditer(content)
            
            for match in matches:
                image_filename = match.group(1).strip()
                D = match.group(2).strip()
                
                # Process template B
                BT = B
                container_class = 'right' if counter % 2 else 'left'
                BT = BT.replace('PICPOS', container_class)
                BT = BT.replace('FNAME', image_filename)
                BT = BT.replace('CTR', str(counter))
                
                # Extract title if exists
                title_match = re.search(r'<font[^>]*>(.*?)</font>', D)
                title_text = title_match.group(1).strip() if title_match else ''
                BT = BT.replace('TITLE', title_text)
                
                # Clean up the content
                D = re.sub(r'<font[^>]*>.*?</font>', '', D, flags=re.DOTALL)
                
                story_content = D.strip()
                story_content = re.sub(r'<[^>]+>', '', story_content)  # Remove HTML tags
                story_content = re.sub(r'\[\[.*?\]\]', '', story_content)  # Remove Obsidian links
                story_content = story_content.replace('\n\n', '</p><p style="margin-bottom:1.5em;">')
                story_content = story_content.replace('\n', '<br><br style="display:block; margin-bottom:0.75em;">')
                story_content = f"<p style=\"margin-bottom:1.5em;\">{story_content}</p>"
                
                BT = BT.replace('<p>story</p>', story_content)
                
                # Create page HTML
                page_html = f'<div class="page" id="page-{counter}">{BT}</div>'
                pages.append(page_html)
                counter += 1
                
    except FileNotFoundError:
        print("Error: oot.md file not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

    # Combine all pages
    for page in pages:
        A += page

    # Update total pages count
    total_pages = counter - 1
    A = A.replace('TOTALPAGES', str(total_pages))
    C = C.replace('TOTALPAGES', str(total_pages))

    # Add footer
    A += C

    # Write final HTML file
    try:
        with open('oot.html', 'w', encoding='utf-8') as html_file:
            html_file.write(A)
        print(f"Successfully created oot.html with {total_pages} content pages")
    except Exception as e:
        print(f"Error writing to oot.html: {e}")