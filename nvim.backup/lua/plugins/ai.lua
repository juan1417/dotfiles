-- ~/.config/nvim/lua/plugins/ai.lua
return {
  -- Codeium (gratis, sin API key, excelente autocompletado)
  {
    "Exafunction/codeium.nvim",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "hrsh7th/nvim-cmp",
    },
    config = function()
      require("codeium").setup({
        enable_chat = true,
      })

      -- Keybindings para Codeium
      vim.keymap.set('i', '<C-g>', function()
        return vim.fn['codeium#Accept']()
      end, { expr = true, silent = true })
      vim.keymap.set('i', '<C-j>', function()
        return vim.fn['codeium#Next']()
      end, { expr = true, silent = true })
      vim.keymap.set('i', '<C-k>', function()
        return vim.fn['codeium#Prev']()
      end, { expr = true, silent = true })
      vim.keymap.set('i', '<C-x>', function()
        return vim.fn['codeium#Clear']()
      end, { expr = true, silent = true })

      -- Chat de Codeium
      vim.keymap.set('n', '<leader>ai', ':Codeium Chat<CR>', { desc = "Abrir Chat IA" })
    end,
  },

  -- Alternativa: Continue (soporta múltiples modelos)
  -- {
  --   "continue-nvim/continue.nvim",
  --   dependencies = { "nvim-lua/plenary.nvim" },
  --   config = function()
  --     require("continue").setup({
  --       -- Configuración para Ollama local o APIs
  --     })
  --   end,
  -- }
}
