-- lua/plugins/explorer.lua
return {
  "nvim-neo-tree/neo-tree.nvim",
  branch = "v3.x",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-tree/nvim-web-devicons", -- iconos
    "MunifTanjim/nui.nvim",        -- UI components
  },
  cmd = "Neotree",                 -- Carga solo cuando escribas :Neotree
  keys = {
    { "<leader>e", "<cmd>Neotree toggle<cr>", desc = "Toggle NeoTree" },
  },
  opts = {
    window = {
      position = "left",
      width = 35,
      auto_clean = true,           -- Cierra automáticamente si no hay buffers
    },
    filesystem = {
      follow_current_file = { enabled = true }, -- Sigue el archivo activo
      use_libuv_file_watcher = true,           -- Actualización en tiempo real
      window = {
        mappings = {
          ["<cr>"] = "open",
          ["o"]      = "open",
          ["s"]      = "open_split",
          ["v"]      = "open_vsplit",
          ["d"]      = "delete",
          ["r"]      = "rename",
          ["y"]      = "copy_to_clipboard",
          ["x"]      = "cut_to_clipboard",
          ["p"]      = "paste_from_clipboard",
          ["<leader>e"] = "close_window",
        },
      },
    },
    buffers = {
      follow_current_file = { enabled = true },
    },
    git_status = {
      window = {
        position = "right",
        width = 35,
      },
    },
  },
}
