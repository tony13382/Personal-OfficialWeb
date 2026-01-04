/**
 * Text Formatting Utilities
 * Mirrors Python's string_formator function
 */

/**
 * Converts backtick-wrapped text to highlighted spans
 *
 * Transforms text with backticks into HTML with highlighted spans.
 * Uses the 'text-highlight' CSS class for styling.
 *
 * @param text - Input text with optional backtick-wrapped sections
 * @returns HTML string with highlighted spans
 *
 * @example
 * formatHighlight("Hello `world`")
 * // Returns: "Hello <span class='text-highlight'>world</span>"
 *
 * @example
 * formatHighlight("Use `npm install` to install packages")
 * // Returns: "Use <span class='text-highlight'>npm install</span> to install packages"
 *
 * @example
 * formatHighlight("Multiple `highlights` in `one` sentence")
 * // Returns: "Multiple <span class='text-highlight'>highlights</span> in <span class='text-highlight'>one</span> sentence"
 */
export function formatHighlight(text: string): string {
  const parts = text.split('`')
  return parts
    .map((part, i) =>
      i % 2 === 0
        ? part
        : `<span class="text-highlight">${part}</span>`
    )
    .join('')
}

/**
 * Escapes HTML special characters to prevent XSS
 *
 * @param text - Text to escape
 * @returns Escaped text safe for HTML insertion
 */
export function escapeHtml(text: string): string {
  const htmlEscapes: Record<string, string> = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;',
  }

  return text.replace(/[&<>"']/g, (char) => htmlEscapes[char])
}

/**
 * Safely formats text with highlight, escaping HTML except highlight spans
 *
 * @param text - Input text with optional backtick-wrapped sections
 * @returns Safely formatted HTML string
 *
 * @example
 * safeFormatHighlight("Use `<script>` tags")
 * // Returns: "Use <span class='text-highlight'>&lt;script&gt;</span> tags"
 */
export function safeFormatHighlight(text: string): string {
  const parts = text.split('`')
  return parts
    .map((part, i) =>
      i % 2 === 0
        ? escapeHtml(part)
        : `<span class="text-highlight">${escapeHtml(part)}</span>`
    )
    .join('')
}
