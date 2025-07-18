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
      }
    });
  }

  // Track page view with Vercel Analytics
  async function trackPageView() {
    await waitForVercelAnalytics();
    
    const page = window.location.pathname;
    const referrer = document.referrer;
    
    // Track page view
    window.va('pageview', {
      url: page,
      referrer: referrer
    });
    
    console.log('📊 Page tracked:', page);
  }

  // Track external link clicks
  async function trackExternalLinks() {
    await waitForVercelAnalytics();
    
    document.addEventListener('click', (event) => {
      const link = event.target.closest('a');
      if (link && link.hostname !== window.location.hostname) {
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
    });
  }

  // Initialize tracking
  document.addEventListener('DOMContentLoaded', () => {
    trackPageView();
    trackExternalLinks();
  });

})(); 