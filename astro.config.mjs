// @ts-check
import { defineConfig } from 'astro/config';

import react from '@astrojs/react';
import tailwindcss from '@tailwindcss/vite';

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://lianglu.uk',
  integrations: [react(), mdx(), sitemap()],

  vite: {
    plugins: [tailwindcss()],
    build: {
      rollupOptions: {
        output: {
          manualChunks: {
            // React core
            'vendor-react': ['react', 'react-dom'],
            // UI components
            'vendor-radix': [
              '@radix-ui/react-accordion',
              '@radix-ui/react-dialog',
              '@radix-ui/react-separator',
              '@radix-ui/react-slot',
              '@radix-ui/react-tabs',
              '@radix-ui/react-tooltip'
            ],
            // Carousel
            'vendor-carousel': ['embla-carousel-react', 'embla-carousel-autoplay'],
            // Icons
            'vendor-icons': ['@phosphor-icons/react', 'lucide-react']
          }
        }
      }
    }
  }
});
