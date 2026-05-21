
return {
  -- Mason: Gestor de servidores LSP
  {
    "williamboman/mason.nvim",
    cmd = "Mason",
    config = true,
  },
  {
    "williamboman/mason-lspconfig.nvim",
    dependencies = { "mason.nvim" },
    opts = {
      ensure_installed = {
        "pyright",        -- Python
        "lua_ls",         -- Lua
        "rust_analyzer",  -- Rust
        "ts_ls",          -- TypeScript
        "html",
        "cssls",
        "jsonls",
        "marksman",       -- Markdown
      },
    },
  },
  -- nvim-lspconfig
  {
    "neovim/nvim-lspconfig",
    dependencies = { "mason-lspconfig.nvim" },
    config = function()
      local capabilities = require('cmp_nvim_lsp').default_capabilities()
      
      require("mason-lspconfig").setup_handlers({
        function(server_name)
          require("lspconfig")[server_name].setup({
            capabilities = capabilities,
          })
        end,
      })

      -- Keybindings LSP
      vim.keymap.set('n', '<leader>e', vim.diagnostic.open_float, { desc = "Diagnósticos" })
      vim.keymap.set('n', '[d', vim.diagnostic.goto_prev, { desc = "Diag anterior" })
      vim.keymap.set('n', ']d', vim.diagnostic.goto_next, { desc = "Diag siguiente" })
      vim.keymap.set('n', '<leader>q', vim.diagnostic.setloclist, { desc = "Lista de diagnósticos" })
    end,
  },
}
