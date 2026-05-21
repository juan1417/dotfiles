-- lua/core/keymaps.lua
local map = vim.keymap.set

-- Leader
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Navegación y edición
map("n", "<leader>q", "<cmd>q<cr>", { desc = "Cerrar ventana" })
map("n", "<leader>w", "<cmd>w<cr>", { desc = "Guardar" })
map("n", "<leader>n", "<cmd>enew<cr>", { desc = "Nuevo buffer" })
map("i", "jj", "<Esc>", { desc = "Salir a modo normal" })

-- Split & ventanas
map("n", "<leader>sv", "<cmd>vsplit<cr>", { desc = "División vertical" })
map("n", "<leader>sh", "<cmd>split<cr>", { desc = "División horizontal" })
map("n", "<leader>sm", "<cmd>wincmd w<cr>", { desc = "Mover foco entre ventanas" })

-- Búsqueda (si usas Telescope más adelante)
map("n", "<leader>ff", "<cmd>Telescope find_files<cr>", { desc = "Buscar archivos" })
map("n", "<leader>fg", "<cmd>Telescope live_grep<cr>", { desc = "Buscar texto" })
map("n", "<leader>fb", "<cmd>Telescope buffers<cr>", { desc = "Buffers abiertos" })

-- Explorador (se dispara desde el plugin)
map("n", "<leader>e", "<cmd>Neotree toggle<cr>", { desc = "Abrir/cerrar explorador" })
map("n", "<leader>E", "<cmd>Neotree focus<cr>", { desc = "Focus en explorador" })
