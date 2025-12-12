// MyST plugin for Utterances comments integration
// Adds Utterances comments to each page using GitHub Issues
// Allows per-page configuration via frontmatter

const DEFAULTS = {
  repo: "IVIA-AF/livre",
  issueTerm: "pathname", // Creates separate issue per page/chapter
  theme: "github-light",
  label: "💬 comments",
};

const addUtterancesComments = {
  name: "add-utterances-comments",
  doc: "Add Utterances comments section to every document.",
  stage: "document",
  plugin: (_, utils) => (tree, file) => {
    // Allow page-level opts via frontmatter: comments: {repo, issueTerm, theme, label, enabled}
    const fm = file?.data?.frontmatter ?? {};
    const cfg = Object.assign({}, DEFAULTS, fm.comments ?? {});
    
    if (cfg.enabled === false) {
      return;
    }

    // Check if Utterances is already added
    const existing = utils.selectAll('html', tree);
    const hasUtterances = existing.some(node => 
      node.value && node.value.includes('utteranc.es')
    );
    
    if (hasUtterances) {
      return;
    }

    // Create HTML block with Utterances container and script
    const utterancesHTML = `
<div class="utterances-container" id="utterances-container" style="
  max-width: 100%; 
  margin: 3rem 0 2rem 0; 
  padding: 2rem; 
  background: #ffffff; 
  border-radius: 8px; 
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); 
  border: 1px solid #e1e5e9; 
  min-height: 200px;
  clear: both;
  overflow: hidden;
">
  <h3 style="
    margin: 0 0 1.5rem 0; 
    color: #333; 
    font-size: 1.3rem; 
    font-weight: 600;
    text-align: center;
    border-bottom: 2px solid #007cba;
    padding-bottom: 0.5rem;
  ">💬 Commentaires</h3>
  
  <script src="https://utteranc.es/client.js"
    repo="${cfg.repo}"
    issue-term="${cfg.issueTerm}"
    theme="${cfg.theme}"
    label="${cfg.label}"
    crossorigin="anonymous"
    async></script>
</div>`;

    const htmlBlock = {
      type: "html",
      value: utterancesHTML,
    };

    // Append to the end of the document
    if (!tree.children) tree.children = [];
    tree.children.push(htmlBlock);
  },
};

const plugin = {
  name: "myst-utterances",
  transforms: [addUtterancesComments],
};

export default plugin;