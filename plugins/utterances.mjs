// Minimal MyST plugin that inserts a <div id="myst-utterances"> at the end of each page.
// It also lets you override defaults via project frontmatter.

const DEFAULTS = {
    repo: "IVIA-AF/livre",
    issueTerm: "pathname",
    theme: "github-light",
    label: "💬 comments",
  };
  
  const addCommentsContainer = {
    name: "add-utterances-container",
    doc: "Append a placeholder div for Utterances to every document.",
    stage: "document",
    plugin: (_, utils) => (tree, file) => {
      // Allow page-level opts via frontmatter: comments: {repo, issueTerm, theme, label, enabled}
      const fm = (file?.data?.frontmatter ?? {});
      const cfg = Object.assign(
        {},
        DEFAULTS,
        (fm.comments ?? {})
      );
      if (cfg.enabled === false) return;
  
      // If the page already has a container, skip
      const existing = utils.selectAll('container[id="myst-utterances"]', tree);
      if (existing.length) return;
  
      // Create a placeholder container with data-* attributes
      const container = {
        type: "container",
        kind: "div",
        id: "myst-utterances",
        // The theme reads these off the element
        data: {
          repo: String(cfg.repo),
          issueTerm: String(cfg.issueTerm),
          theme: String(cfg.theme),
          label: String(cfg.label),
        },
        // optional heading shown above comments; remove if you don't want it
        children: [
          { type: "thematicBreak" },
          { type: "paragraph", children: [{ type: "strong", children: [{ type: "text", value: "Commentaires" }] }] },
        ],
      };
  
      // Append to the end of the document
      if (!tree.children) tree.children = [];
      tree.children.push(container);
    },
  };

  const addUtterancesScript = {
    name: "add-utterances-script",
    doc: "Add the Utterances client script to the page.",
    stage: "document",
    plugin: (_, utils) => (tree, file) => {
      // Allow page-level opts via frontmatter: comments: {repo, issueTerm, theme, label, enabled}
      const fm = (file?.data?.frontmatter ?? {});
      const cfg = Object.assign(
        {},
        DEFAULTS,
        (fm.comments ?? {})
      );
      if (cfg.enabled === false) return;

      // Add a simple script that loads Utterances
      const scriptBlock = {
        type: "html",
        value: `<script src="https://utteranc.es/client.js" repo="${cfg.repo}" issue-term="${cfg.issueTerm}" theme="${cfg.theme}" label="${cfg.label}" crossorigin="anonymous" async></script>`
      };

      // Append the script to the end of the document
      if (!tree.children) tree.children = [];
      tree.children.push(scriptBlock);
    },
  };
  
  const plugin = {
    name: "myst-utterances",
    transforms: [addCommentsContainer, addUtterancesScript],
  };
  
  export default plugin;