-- ~/.config/nvim/lua/config/lazy.lua
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable",
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup({
  spec = {
    -- Esta ÚNICA línea importa TODOS los archivos en lua/plugins/
    { import = "plugins" },
    
    -- Plugins sueltos (si los tienes)
    { "tpope/vim-fugitive" },
    { "lewis6991/gitsigns.nvim" },
    { "nvim-lualine/lualine.nvim" },
  },
  defaults = { lazy = true },
  install = { colorscheme = { "tokyonight" } },
  ui = {
    icons = { cmd = "⌨️", keys = "🔑" },
  },
})
