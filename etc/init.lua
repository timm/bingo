-- Essential Neovim settings for a clean and efficient workflow
vim.opt.termguicolors = true    -- Enable true color support
vim.opt.tabstop = 2             -- Number of spaces a <Tab> counts for
vim.opt.shiftwidth = 2          -- Number of spaces to use for each step of (auto)indent
vim.opt.expandtab = true        -- Use spaces instead of tabs
vim.opt.softtabstop = 2         -- Number of spaces <BS> and <Tab> use in insert mode
vim.opt.number = true           -- Show current line number
vim.opt.relativenumber = true   -- Show relative line numbers
vim.opt.mouse = "a"             -- Enable mouse support in all modes
vim.opt.undofile = true         -- Enable persistent undo
vim.opt.undodir = os.getenv("HOME") .. "/.nvim/undodir" -- Directory for undo files (create this directory: mkdir -p ~/.nvim/undodir)
vim.opt.ignorecase = true       -- Ignore case in search patterns
vim.opt.smartcase = true        -- Override 'ignorecase' if search pattern contains uppercase
vim.opt.incsearch = true        -- Highlight matches as you type
vim.opt.cursorline = true       -- Highlight the current line
vim.opt.swapfile = false        -- Do not create swap files
vim.opt.backup = false          -- Do not create backup files
vim.opt.errorbells = false      -- No sound effects for errors
vim.opt.visualbell = true       -- Use visual bell instead of sound
vim.opt.wildmenu = true         -- Enhanced command-line completion menu
vim.opt.wildmode = "list:longest,full" -- How wildmenu behaves
vim.opt.smartindent = true      -- Smart auto-indenting
vim.opt.wrap = false            -- Do not wrap lines
vim.opt.title = true            -- Set terminal title

-- Bootstrap lazy.nvim plugin manager
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- latest stable release
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- Load plugins using lazy.nvim
require("lazy").setup({
  -- Catppuccin colorscheme (already handled by Makefile, but added here for consistency with lazy.nvim)
  -- If you prefer lazy.nvim to manage it, remove the Makefile cloning step for catppuccin.
  { "catppuccin/nvim", name = "catppuccin", priority = 1000 },

  -- File explorer
  {
    "nvim-tree/nvim-tree.lua",
    version = "*",
    lazy = false,
    config = function()
      require("nvim-tree").setup {}
    end,
  },

  -- Fuzzy finder
  {
    "nvim-telescope/telescope.nvim",
    branch = "master",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
      require("telescope").setup {}
    end,
  },

  -- Git integration (shows diffs in sign column)
  {
    "lewis6991/gitsigns.nvim",
    config = function()
      require("gitsigns").setup {}
    end,
  },

  -- Status line
  {
    "nvim-lualine/lualine.nvim",
    dependencies = { "nvim-tree/nvim-tree.lua" }, -- Lualine often integrates with NvimTree
    config = function()
      require("lualine").setup {
        options = {
          theme = "auto", -- Automatically pick a theme, or set 'catppuccin'
        },
        sections = {
          lualine_x = { "filetype", "branch", "diff" }, -- Example: show filetype, git branch, and diffs
        },
        -- Configure the tabline to show buffers
        tabline = {
          lualine_a = { "buffers" }, -- Show buffers in the left section of the tabline
          lualine_b = {},
          lualine_c = {},
          lualine_x = {},
          lualine_y = {},
          lualine_z = { "tabs" }, -- Show tabs in the right section (if you use Neovim tabs)
        },
      }
    end,
  },

  -- Commenting plugin
  {
    "preservim/nerdcommenter",
    lazy = false, -- Load this eagerly as it's a utility
  },
})

-- Load and setup Catppuccin colorscheme (ensure this is called after lazy.nvim setup)
require("catppuccin").setup({
    -- To set a specific Catppuccin style (e.g., 'mocha', 'latte', 'frappe', 'macchiato'),
    -- uncomment the 'flavour' line below and set your desired style.
    flavour = "mocha",
})
vim.cmd.colorscheme "catppuccin"

-- The autocmd for NvimTree opening behavior is removed as per your request to revert.

-- Keybindings for plugins (optional, but recommended for usability)
vim.keymap.set("n", "<C-n>", ":NvimTreeToggle<CR>", { desc = "Toggle NvimTree" })
vim.keymap.set("n", "<leader>ff", "<cmd>Telescope find_files<cr>", { desc = "Find files" })
vim.keymap.set("n", "<leader>fg", "<cmd>Telescope live_grep<cr>", { desc = "Live Grep" })
vim.keymap.set("n", "<leader>c", ":NERDCommenterComment<CR>", { desc = "Comment/Uncomment line(s)" }) -- For NERDCommenter

