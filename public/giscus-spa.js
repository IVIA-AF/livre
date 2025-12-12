/**
 * SPA-safe Giscus loader for MyST/React sites
 * Handles React hydration and client-side navigation
 */
(function () {
  const GISCUS_CONTAINER_ID = "giscus-comments";
  const GISCUS_CONFIG = {
    repo: "IVIA-AF/livre",
    repoId: "R_kgDOPKBYSA",
    category: "Commentaire",
    categoryId: "DIC_kwDOPKBYSM4CuxXP",
    mapping: "pathname",
    strict: "0",
    reactionsEnabled: "1",
    emitMetadata: "0",
    inputPosition: "top",
    theme: "light",
    lang: "fr"
  };

  function mountGiscus() {
    const container = document.getElementById(GISCUS_CONTAINER_ID);
    if (!container) return;

    // Clean up any existing Giscus instance to avoid duplicates
    container.innerHTML = "";

    // Create and configure the Giscus script
    const script = document.createElement("script");
    script.src = "https://giscus.app/client.js";
    script.async = true;
    script.crossOrigin = "anonymous";

    // Set all Giscus data attributes
    script.setAttribute("data-repo", GISCUS_CONFIG.repo);
    script.setAttribute("data-repo-id", GISCUS_CONFIG.repoId);
    script.setAttribute("data-category", GISCUS_CONFIG.category);
    script.setAttribute("data-category-id", GISCUS_CONFIG.categoryId);
    script.setAttribute("data-mapping", GISCUS_CONFIG.mapping);
    script.setAttribute("data-strict", GISCUS_CONFIG.strict);
    script.setAttribute("data-reactions-enabled", GISCUS_CONFIG.reactionsEnabled);
    script.setAttribute("data-emit-metadata", GISCUS_CONFIG.emitMetadata);
    script.setAttribute("data-input-position", GISCUS_CONFIG.inputPosition);
    script.setAttribute("data-theme", GISCUS_CONFIG.theme);
    script.setAttribute("data-lang", GISCUS_CONFIG.lang);

    container.appendChild(script);
  }

  // Wait for Remix scripts to load and React to hydrate
  // This ensures React has finished hydrating before we touch the DOM
  function waitForRemixAndMount() {
    // Wait for all Remix entry.client scripts to load
    const remixScripts = document.querySelectorAll('script[src*="entry.client"], script[src*="manifest"]');
    let loadedCount = 0;
    const totalScripts = remixScripts.length;
    
    function tryMount() {
      // Optimized: Reduced delay while maintaining hydration safety
      // Double RAF ensures we're after React's initial render cycle
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          // Reduced from 4s to 1.5s - enough for hydration without being too slow
          setTimeout(() => {
            mountGiscus();
          }, 1500);
        });
      });
    }
    
    if (totalScripts === 0) {
      // No Remix scripts found, wait a bit then mount (reduced from 2s to 1s)
      setTimeout(tryMount, 1000);
      return;
    }
    
    // Track when all Remix scripts are loaded
    remixScripts.forEach(function(script) {
      if (script.complete || script.readyState === 'complete' || script.readyState === 'loaded') {
        loadedCount++;
      } else {
        script.addEventListener('load', function() {
          loadedCount++;
          if (loadedCount >= totalScripts) {
            // All scripts loaded, wait for React hydration
            tryMount();
          }
        });
      }
    });
    
    // If all were already loaded
    if (loadedCount >= totalScripts) {
      tryMount();
    }
    
    // Reduced timeout fallback from 10s to 5s
    setTimeout(function() {
      mountGiscus();
    }, 5000);
  }
  
  // Alias for SPA navigation
  function mountAfterHydration() {
    waitForRemixAndMount();
  }

  // Hook into history API to detect SPA navigations
  function hookHistory() {
    const originalPushState = history.pushState;
    const originalReplaceState = history.replaceState;

    history.pushState = function () {
      originalPushState.apply(this, arguments);
      // Re-mount Giscus after navigation
      mountAfterHydration();
    };

    history.replaceState = function () {
      originalReplaceState.apply(this, arguments);
      // Re-mount Giscus after navigation
      mountAfterHydration();
    };

    // Handle browser back/forward
    window.addEventListener("popstate", mountAfterHydration);
  }

  // Initialize as early as possible
  // Hook history immediately (doesn't depend on DOM)
  hookHistory();
  
  // Start waiting for scripts/hydration based on document state
  if (document.readyState === "loading") {
    // If still loading, wait for DOMContentLoaded
    document.addEventListener("DOMContentLoaded", waitForRemixAndMount);
  } else {
    // DOM already ready, start immediately
    waitForRemixAndMount();
  }
})();

