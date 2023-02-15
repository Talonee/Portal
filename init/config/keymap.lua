local keymap = function(tbl)
	local opts = { noremap = true, silent = true }
	local mode = tbl['mode']
	tbl['mode'] = nil
	local bufnr = tbl['bufnr']
	tbl['bufnr'] = nil

	for k, v in pairs(tbl) do
		if tonumber(k) == nil then
			opts[k] = v
		end
	end

	if bufnr ~= nil then
		vim.api.nvim_buf_set_keymap(bufnr, mode, tbl[1], tbl[2], opts)
	else
		vim.api.nvim_set_keymap(mode, tbl[1], tbl[2], opts)
	end
end

nmap = function(tbl)
	tbl['mode'] = 'n'
	keymap(tbl)
end

imap = function(tbl)
	tbl['mode'] = 'i'
	keymap(tbl)
end


local ok, treesitter = pcall(require, "nvim-treesitter.configs")
if not ok then return end
treesitter.setup { ensure_installed = "all", highlight = { enable = true } }

-- keymaps
nmap { "<C-f>", "<cmd>Telescope current_buffer_fuzzy_find sorting_strategy=ascending prompt_position=top<CR>" }

-- custom key maps
nmap { "<leader>fb", "<cmd>Telescope file_browser<cr>" }
nmap { "<leader>tt", "<cmd>NvimTreeFindFileToggle<cr>" }
nmap { "<leader>tf", "<cmd>NvimTreeFocus<cr>" }
nmap { "<leader>rf", ":RunFile<CR>" }
nmap { "<leader>rc", ":RunClose<CR>" }

-- navigation
nmap { "L", "<cmd>bnext<cr>" }
nmap { "H", "<cmd>bprevious<cr>" }
nmap { "F", "<cmd>HopPattern<cr>" }

-- festivities
nmap { "<leader>;", "<cmd>lua require('duck').hatch('🐤', 3)<cr>" }
nmap { "<leader>:", "<cmd>lua require('duck').hatch('🐢', 3)<cr>" }
nmap { "<leader>'", "<cmd>lua require('duck').cook()<cr>" }
