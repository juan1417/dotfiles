return {
  "nvim-treesitter/nvim-treesitter",
  build = ":TSUpdate",
  event = { "BufReadPre", "BufNewFile" },
  opts = {
    ensure_installed = { "lua", "python", "javascript", "typescript", "html", "css", "json", "markdown", "bash" },
    highlight = { enable = true },
    indent = { enable = true },
  },
}
