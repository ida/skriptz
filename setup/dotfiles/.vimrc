" Show always currently opened filename in window-title:
autocmd BufEnter * let &titlestring = ' ' . expand("%:t") " Prepare window-title of filename-var... 
set title           " .. and set it.

" Spaces sanity:
set shiftwidth=4    " How many spaces long shall a tab be in general? 
set softtabstop=4   " Especially when editing.
set tabstop=4       " Especially when reading.
set expandtab       " Force tabs to always be spaces. 
set smartindent     " Preserve indent when breaking the line.

