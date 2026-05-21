vim.g.mapleader = " "
vim.g.maplocalleader = ","

vim.o.number = true
vim.o.relativenumber = false
vim.o.clipboard = "unnamedplus"
vim.o.smartcase = true
vim.o.ignorecase = true
vim.o.termguicolors = true
vim.o.cursorline = true
vim.o.mouse = "a"
vim.o.splitbelow = true
vim.o.splitright = true

-- Indentación
vim.o.tabstop = 4
vim.o.shiftwidth = 4
vim.o.expandtab = true
vim.o.autoindent = true

-- Forzar transparencia en Neovim
vim.api.nvim_create_autocmd("ColorScheme", {
  pattern = "*",
  callback = function()
    local none = "NONE"
    vim.api.nvim_set_hl(0, "Normal",    { bg = none })
    vim.api.nvim_set_hl(0, "NormalNC",  { bg = none })
    vim.api.nvim_set_hl(0, "NonText",   { bg = none })
    vim.api.nvim_set_hl(0, "SignColumn",{ bg = none })
    vim.api.nvim_set_hl(0, "LineNr",    { bg = none })
    vim.api.nvim_set_hl(0, "WinBar",    { bg = none })
    vim.api.nvim_set_hl(0, "StatusLine",{ bg = none })
  end,
})
