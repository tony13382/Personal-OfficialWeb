#!/usr/bin/env python3
"""
將 app/pages/project/*.py 專案文件轉換為 portfolio-astro/src/content/projects/*.mdx 格式
"""

import os
import sys
import importlib.util
from pathlib import Path
from datetime import datetime
import re


class ProjectConverter:
    """專案文件轉換器"""

    # 顏色主題映射
    COLOR_THEME_MAP = {
        'red': 'red',
        'orange': 'orange',
        'yellow': 'yellow',
        'green': 'green',
        'blue': 'blue',
        'purple': 'purple',
        'pink': 'pink',
    }

    # Bootstrap icon 映射到實際 icon 名稱
    ICON_MAP = {
        'bi-github': 'bi-github',
        'bi-cloud': 'bi-cloud',
        'bi-building': 'bi-building',
        'bi-phone': 'bi-phone',
        'bi-phone-fill': 'Smartphone',
        'bi-window-sidebar': 'bi-window-sidebar',
        'bi-file-earmark-arrow-down': 'bi-file-earmark-arrow-down',
        'bi-keyboard': 'Keyboard',
        'bi-hdd-network': 'Server',
        'bi-line': 'MessageCircle',
        'bi-arrow-repeat': 'RefreshCw',
        'bi-send': 'Send',
        'bi-database-down': 'Database',
        'bi-crosshair2': 'bi-crosshair2',
        'bi-fire': 'bi-fire',
        'bi-share-fill': 'bi-share-fill',
        'bi-flag-fill': 'bi-flag-fill',
        'bi-headphones': 'bi-headphones',
        'bi-image-fill': 'bi-image-fill',
        'bi-pencil-fill': 'bi-pencil-fill',
        'bi-mic': 'bi-mic',
        'bi-stars': 'bi-stars',
        'bi-music-note-list': 'bi-music-note-list',
        'bi-file-earmark-music': 'bi-file-earmark-music',
        'bi-box-arrow-right': 'bi-box-arrow-right',
        'bi-collection': 'bi-collection',
        'bi-wallet': 'bi-wallet',
    }

    def __init__(self, source_dir, target_dir):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)

    def load_project_page(self, py_file):
        """動態載入 Python 文件並獲取 page 對象"""
        spec = importlib.util.spec_from_file_location("project_module", py_file)
        module = importlib.util.module_from_spec(spec)

        # 加入系統路徑以便導入
        sys.path.insert(0, str(self.source_dir.parent.parent))

        try:
            spec.loader.exec_module(module)
            return module.page
        except Exception as e:
            print(f"Error loading {py_file}: {e}")
            return None
        finally:
            sys.path.pop(0)

    def convert_date(self, date_str):
        """轉換日期格式 從 YYYY/MM 到 YYYY-MM-DD"""
        if not date_str:
            return None
        # 處理 YYYY/MM 格式
        if '/' in date_str:
            parts = date_str.split('/')
            if len(parts) == 2:
                return f"{parts[0]}-{parts[1].zfill(2)}-01"
        return date_str

    def get_theme_name(self, color_set):
        """從 colorSet 獲取主題名稱"""
        if hasattr(color_set, 'name'):
            return color_set.name
        # 如果無法取得，預設返回 'blue'
        return 'blue'

    def escape_yaml_string(self, text):
        """轉義 YAML 字符串中的特殊字符"""
        if not text:
            return ''
        # 如果包含冒號、換行符或特殊字符，需要引號
        if ':' in text or '\n' in text or '<br>' in text:
            return text.replace('"', '\\"')
        return text

    def convert_to_frontmatter(self, page):
        """轉換 ProjectPage 到 YAML frontmatter"""
        lines = ['---']

        # 基本資訊
        lines.append(f'title: {page.title}')
        lines.append(f'description: {self.escape_yaml_string(page.description)}')
        if hasattr(page, 'subdescription') and page.subdescription:
            lines.append(f'subdescription: "{self.escape_yaml_string(page.subdescription)}"')

        # 時間與狀態
        start_date = self.convert_date(page.startdate)
        lines.append(f'startDate: {start_date}')

        if hasattr(page, 'enddate') and page.enddate:
            end_date = self.convert_date(page.enddate)
            lines.append(f'endDate: {end_date}')

        if hasattr(page, 'status'):
            lines.append(f'status: {page.status}')

        # 主題與視覺
        theme = self.get_theme_name(page.colorSet)
        lines.append(f'theme: {theme}')

        if hasattr(page, 'cover'):
            lines.append(f'cover: {page.cover}')

        if hasattr(page, 'pin'):
            lines.append(f'pin: {str(page.pin).lower()}')

        # 分類與標籤
        if hasattr(page, 'skill_types') and page.skill_types:
            skill_types_str = ', '.join(page.skill_types)
            lines.append(f'skillTypes: [{skill_types_str}]')

        if hasattr(page, 'tags') and page.tags:
            tags_str = ', '.join(page.tags)
            lines.append(f'tags: [{tags_str}]')

        # Links
        if hasattr(page, 'description_links') and page.description_links:
            lines.append('links:')
            for link in page.description_links:
                lines.append(f'  - content: {link.content}')
                lines.append(f'    href: {link.href}')
                if hasattr(link, 'icon') and link.icon:
                    lines.append(f'    icon: {link.icon}')
                if hasattr(link, 'open_in_tab'):
                    lines.append(f'    openInTab: {str(link.open_in_tab).lower()}')

        # Scores
        if hasattr(page, 'scores') and page.scores:
            lines.append('scores:')
            for score in page.scores:
                lines.append(f'  - title: {score.title}')
                lines.append(f'    award: {score.award}')
                if hasattr(score, 'category') and score.category:
                    lines.append(f'    category: {score.category}')

        # Tools
        if hasattr(page, 'tools') and page.tools:
            lines.append('tools:')
            for tool in page.tools:
                lines.append(f'  - name: {tool.name}')
                lines.append(f'    description: {tool.description}')

        # SEO (基於現有資料生成)
        if page.title and page.description:
            lines.append('seo:')
            lines.append(f'  metaTitle: {page.title} - 呂亮進的專案作品')
            lines.append(f'  metaDescription: {self.escape_yaml_string(page.description)[:150]}')
            if hasattr(page, 'cover'):
                lines.append(f'  ogImage: {page.cover}')

        lines.append('---')
        return '\n'.join(lines)

    def convert_element_to_mdx(self, element, indent=0):
        """轉換元素為 MDX 格式"""
        indent_str = '  ' * indent

        element_type = type(element).__name__

        # Card 元素
        if element_type == 'Card':
            lines = [f'{indent_str}<Card>']

            # Header
            if hasattr(element, 'header') and element.header:
                lines.append(f'{indent_str}  <CardHeader>')
                header_content = self.convert_element_to_mdx(element.header, indent + 2)
                lines.append(header_content)
                lines.append(f'{indent_str}  </CardHeader>')

            # Body
            if hasattr(element, 'body') and element.body:
                lines.append(f'{indent_str}  <CardContent>')
                if isinstance(element.body, list):
                    for item in element.body:
                        content = self.convert_element_to_mdx(item, indent + 2)
                        lines.append(content)
                else:
                    content = self.convert_element_to_mdx(element.body, indent + 2)
                    lines.append(content)
                lines.append(f'{indent_str}  </CardContent>')

            lines.append(f'{indent_str}</Card>')
            return '\n'.join(lines)

        # Text 元素
        elif element_type == 'Text':
            content = element.content

            # 處理標題
            if hasattr(element, 'type'):
                if element.type == 'h2':
                    return f'{indent_str}## {content}'
                elif element.type == 'h3':
                    return f'{indent_str}### {content}'
                elif element.type == 'h4':
                    return f'{indent_str}#### {content}'

            # 處理 Bold
            if hasattr(element, 'bold') and element.bold:
                content = f'**{content}**'

            return f'{indent_str}<p>{content}</p>'

        # Image 元素
        elif element_type == 'Image':
            src = element.src if hasattr(element, 'src') else ''
            alt = element.alt if hasattr(element, 'alt') else ''
            allow_pop = 'true' if (hasattr(element, 'allow_pop') and element.allow_pop) else 'false'

            return f'''{indent_str}<ImageWithLightbox
{indent_str}  src="{src}"
{indent_str}  allowPop={{{allow_pop}}}
{indent_str}  client:load
{indent_str}/>'''

        # Youtube 元素
        elif element_type == 'Youtube':
            embed_url = element.embed_url if hasattr(element, 'embed_url') else ''
            return f'''{indent_str}<Youtube
{indent_str}  embedUrl="{embed_url}"
{indent_str}  client:visible
{indent_str}/>'''

        # UiImageCarousel 元素
        elif element_type == 'UiImageCarousel':
            images = element.images if hasattr(element, 'images') else []
            images_str = ',\n' + indent_str + '      '.join([f'"{img}"' for img in images])
            return f'''{indent_str}<UiImageCarousel
{indent_str}  images={{[
{indent_str}      {images_str}
{indent_str}    ]}}
{indent_str}    client:load
{indent_str}/>'''

        # IconBlock 元素
        elif element_type == 'IconBlock':
            title = element.title if hasattr(element, 'title') else ''
            subtitle = element.subtitle if hasattr(element, 'subtitle') else ''
            icon_original = element.icon if hasattr(element, 'icon') else ''
            icon = self.ICON_MAP.get(icon_original, icon_original)
            href = element.src if hasattr(element, 'src') else ''

            if href:
                return f'''{indent_str}<IconBlock
{indent_str}  title="{title}"
{indent_str}  subtitle="{subtitle}"
{indent_str}  href="{href}"
{indent_str}  icon="{icon}"
{indent_str}  client:visible
{indent_str}/>'''
            else:
                return f'{indent_str}<IconBlock title="{title}" icon="{icon}" />'

        # ListStr 元素
        elif element_type == 'ListStr':
            items = element.items if hasattr(element, 'items') else []
            lines = []
            for item in items:
                lines.append(f'{indent_str}- {item}')
            return '\n'.join(lines)

        # ListDiv 元素
        elif element_type == 'ListDiv':
            children = element.children if hasattr(element, 'children') else []
            lines = [f'{indent_str}<div className="flex flex-col gap-4">']
            for child in children:
                content = self.convert_element_to_mdx(child, indent + 1)
                lines.append(content)
            lines.append(f'{indent_str}</div>')
            return '\n'.join(lines)

        # DivBar 元素
        elif element_type == 'DivBar':
            return f'{indent_str}<hr className="my-4" />'

        # Html 元素
        elif element_type == 'Html':
            html_content = element.html if hasattr(element, 'html') else ''
            return f'{indent_str}{html_content}'

        # 預設處理
        else:
            return f'{indent_str}<!-- Unsupported element: {element_type} -->'

    def convert_children_to_mdx(self, children):
        """轉換 children 列表為 MDX 內容"""
        if not children:
            return ''

        lines = []
        for child in children:
            content = self.convert_element_to_mdx(child)
            lines.append(content)
            lines.append('')  # 空行分隔

        return '\n'.join(lines)

    def convert_project(self, py_file):
        """轉換單個專案文件"""
        print(f"Converting {py_file.name}...")

        # 載入專案頁面
        page = self.load_project_page(py_file)
        if not page:
            print(f"  ✗ Failed to load page object")
            return False

        # 生成 MDX 內容
        try:
            # Frontmatter
            frontmatter = self.convert_to_frontmatter(page)

            # Import statements
            imports = """
import { Card, CardHeader, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Youtube } from '@/components/react/Youtube'
import { IconBlock } from '@/components/react/IconBlock'
import { ImageWithLightbox } from '@/components/react/ImageWithLightbox'
import { UiImageCarousel } from '@/components/react/UiImageCarousel'
"""

            # Body content
            body = ''
            if hasattr(page, 'children'):
                body = self.convert_children_to_mdx(page.children)

            # 組合完整內容
            mdx_content = frontmatter + '\n' + imports + '\n' + body

            # 輸出文件名稱
            output_filename = py_file.stem.replace('_', '-') + '.mdx'
            if py_file.stem == 'mindReader':
                output_filename = 'mind-reader.mdx'
            elif py_file.stem == 'noDrinkNoDrunk':
                output_filename = 'no-drink-no-drunk.mdx'
            elif py_file.stem == 'notionAsDb':
                output_filename = 'notion-as-db.mdx'
            elif py_file.stem == 'oneDayLover':
                output_filename = 'one-day-lover.mdx'
            elif py_file.stem == 'pincakeAi':
                output_filename = 'pincake-ai.mdx'
            elif py_file.stem == 'trelloFinder':
                output_filename = 'trello-finder.mdx'
            elif py_file.stem == 'stockCalc':
                output_filename = 'stock-calc.mdx'
            elif py_file.stem == 'hsCloudMeetingManage':
                output_filename = 'hs-cloud-meeting-manage.mdx'
            elif py_file.stem == 'hsVmi':
                output_filename = 'hs-vmi.mdx'
            elif py_file.stem == 'digitalOcean':
                output_filename = 'digital-ocean.mdx'
            elif py_file.stem == 'jobAnalytics2020':
                output_filename = 'job-analytics-2020.mdx'

            output_path = self.target_dir / output_filename

            # 寫入文件
            output_path.write_text(mdx_content, encoding='utf-8')
            print(f"  ✓ Created {output_filename}")
            return True

        except Exception as e:
            print(f"  ✗ Error: {e}")
            import traceback
            traceback.print_exc()
            return False

    def convert_all(self):
        """轉換所有專案文件"""
        # 確保目標目錄存在
        self.target_dir.mkdir(parents=True, exist_ok=True)

        # 獲取所有 .py 文件（排除 __init__.py）
        py_files = [
            f for f in self.source_dir.glob('*.py')
            if f.name != '__init__.py'
        ]

        print(f"Found {len(py_files)} project files to convert\n")

        success_count = 0
        for py_file in py_files:
            if self.convert_project(py_file):
                success_count += 1

        print(f"\n{'='*50}")
        print(f"Conversion complete: {success_count}/{len(py_files)} files converted successfully")


def main():
    # 設定路徑
    source_dir = Path(__file__).parent / 'app' / 'pages' / 'project'
    target_dir = Path(__file__).parent / 'portfolio-astro' / 'src' / 'content' / 'projects'

    converter = ProjectConverter(source_dir, target_dir)
    converter.convert_all()


if __name__ == '__main__':
    main()
