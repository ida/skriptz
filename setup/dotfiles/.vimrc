" Show always currently opened filename in window-title:
" Prepare window-title of filename-var... 
autocmd BufEnter * let &titlestring = ' ' . expand("%:t") 
set title           " .. and set it.

" Spaces sanity:
set shiftwidth=4    " How many spaces long shall a tab be in general? 
set softtabstop=4   " Especially when editing.
set tabstop=4       " Especially when reading.
set expandtab       " Force tabs to always be spaces. 
set smartindent     " Preserve indent when breaking the line.

" Two spaces indents for js- and html-files:
autocmd Filetype html setlocal ts=2 sts=2 sw=2
autocmd Filetype javascript setlocal ts=2 sts=2 sw=2
autocmd Filetype css setlocal ts=2 sts=2 sw=2

" Make less-files behave like js-files for syntax-highlighting:
au BufNewFile,BufRead *.less set filetype=javascript
" Make sass-files behave like css-files, because:
au BufNewFile,BufRead *.scss set filetype=css

" Make sure using ! for starting a shell-cmd, always works,
" activate interactive mode:
set shellcmdflag=-ic

" When saving SASS-files, execute 'sas' defined in '.bash_aliases':
autocmd BufWritePost *.scss !sas <afile>

" When saving PYJS-files, execute 'pytojs' defined in '.bash_aliases':
autocmd BufWritePost *.pyjs !pytojs <afile>

" Make less-files behave like js-files for syntax-highlighting:
au BufNewFile,BufRead *.less set filetype=javascript

" For the EOF-symbol '~', set fg and bg to black, so tilde gets invisible:
highlight NonText ctermfg=Black ctermbg=Black

" http://stackoverflow.com/questions/1294790/change-tilde-color-in-vim
" make eof-symbol (the tilde) have the same color as default-fg-col and
" thereby dissapear visually:
"
" highlight NonText ctermfg=12
"
" Or, set a specific color:
" 
" highlight NonText ctermfg='red'

