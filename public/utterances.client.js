(function () {
    const W = window;
  
    function mountUtterances() {
      const host = document;
      const root = host.querySelector("#myst-utterances");
      if (!root) return;
  
      // If already mounted, do nothing
      if (root.querySelector("iframe.utterances-frame")) return;
  
      // Clear any stale script/iframe
      root.querySelectorAll("script, iframe").forEach((n) => n.remove());
  
      const repo = root.dataset.repo;
      const issueTerm = root.dataset.issueTerm || "pathname";
      const theme = root.dataset.theme || "github-light";
      const label = root.dataset.label || "💬 comments";
  
      const s = host.createElement("script");
      s.src = "https://utteranc.es/client.js";
      s.setAttribute("repo", repo);
      s.setAttribute("issue-term", issueTerm);
      s.setAttribute("label", label);
      s.setAttribute("theme", theme);
      s.crossOrigin = "anonymous";
      s.async = true;
      root.appendChild(s);
    }
  
    // Run on initial load
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", mountUtterances, { once: true });
    } else {
      mountUtterances();
    }
  
    // Re-run on client-side navigations.
    // MyST v2 sites are Remix-based; we don't rely on secret internals:
    // - patch pushState/replaceState and listen to popstate
    const _ps = history.pushState;
    const _rs = history.replaceState;
    function rerun() { setTimeout(mountUtterances, 0); }
    history.pushState = function () { _ps.apply(this, arguments); rerun(); };
    history.replaceState = function () { _rs.apply(this, arguments); rerun(); };
    window.addEventListener("popstate", rerun);
  
    // As a fallback, observe DOM changes (e.g., when page body re-renders)
    const mo = new MutationObserver((muts) => {
      for (const m of muts) {
        if (m.addedNodes && m.addedNodes.length) {
          if (document.querySelector("#myst-utterances")) {
            mountUtterances();
            break;
          }
        }
      }
    });
    mo.observe(document.documentElement, { childList: true, subtree: true });
  })();