// Vercel Analytics integration for IVIA-AF Book
(function() {
  'use strict';

  // Wait for Vercel Analytics to load
  function waitForVercelAnalytics() {
    return new Promise((resolve) => {
      if (typeof window.va !== 'undefined') {
        resolve();
      } else {
        const checkInterval = setInterval(() => {
          if (typeof window.va !== 'undefined') {
            clearInterval(checkInterval);
            resolve();
          }
        }, 100);
        
        // Timeout after 5 seconds
        setTimeout(() => {
          clearInterval(checkInterval);
          console.warn('⚠️ Vercel Analytics not loaded within 5 seconds');
          resolve(); // Continue anyway
        }, 5000);
      }
    });
  }

  // Track page view with Vercel Analytics
  async function trackPageView() {
    try {
      await waitForVercelAnalytics();
      
      const page = window.location.pathname;
      const referrer = document.referrer;
      
      // Track page view
      if (typeof window.va === 'function') {
        window.va('pageview', {
          url: page,
          referrer: referrer
        });
        console.log('📊 Page tracked:', page);
      } else {
        console.log('📊 Page view (Vercel Analytics not available):', page);
      }
    } catch (error) {
      console.error('❌ Error tracking page view:', error);
    }
  }

  // Track external link clicks
  async function trackExternalLinks() {
    try {
      await waitForVercelAnalytics();
      
      document.addEventListener('click', (event) => {
        const link = event.target.closest('a');
        if (link && link.hostname !== window.location.hostname) {
          if (typeof window.va === 'function') {
            window.va('event', {
              name: 'external_link_click',
              data: {
                url: link.href,
                text: link.textContent,
                page: window.location.pathname
              }
            });
            console.log('🔗 External link clicked:', link.href);
          }
        }
      });
    } catch (error) {
      console.error('❌ Error tracking external links:', error);
    }
  }

  // Initialize tracking
  document.addEventListener('DOMContentLoaded', () => {
    trackPageView();
    trackExternalLinks();
  });

  // Also track on page load for single-page apps
  window.addEventListener('load', () => {
    if (typeof window.va === 'function') {
      window.va('pageview', {
        url: window.location.pathname,
        referrer: document.referrer
      });
    }
  });

})(); 