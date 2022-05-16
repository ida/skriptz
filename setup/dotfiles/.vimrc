" Good overview:
" http://www.worldtimzone.com/res/vi.html


" Enable suggesting language-specific autocompletions:
filetype plugin on
set omnifunc=syntaxcomplete#Complete


" KEY-MAPPINGS

" http://learnvimscriptthehardway.stevelosh.com/chapters/04.html

" Save file when pressing Strg+x and return to edit-mode:
inoremap <c-x> <Esc>:w<CR>i<right>


" When pressing Strg+d in editmode, switch to normalmode,
" cut line with 'dd' and switch back to editmode ("delete line"):
inoremap <c-d> <esc>ddi

" When pressing Strg+s in editmode, save file and
" switch back to insertion-mode:
" inoremap <c-s> <esc><esc>:w<CR>

" Exit insertion-mode, when double-hitting 'k',
" thereby go into normal-mode:
inoremap kk <Esc>




" AUTOCOMPLETIONS

inoremap pdb    from pdb import set_trace; set_trace()

" http://vim.wikia.com/wiki/Automatically_append_closing_characters
" if you quickly press Enter after the open brace (to begin a code block),
" the closing brace will be inserted on the line below the cursor. If you
" quickly press the open brace key again after the open brace, nothing
" extra will be inserted—you will just get a single open brace. Finally,
" if you quickly type an open and close brace, Vim will not do anything special.

inoremap "      ""<Left>
inoremap "<CR>  "<CR>"<Esc>O
inoremap """     "
inoremap ""     ""

inoremap '      ''<Left>
inoremap '<CR>  '<CR>''<Esc>O
inoremap '''     '
inoremap ''     ''

inoremap {      {}<Left>
inoremap {<CR>  {<CR>}<Esc>O
inoremap {{     {
inoremap {}     {}

inoremap [      []<Left>
inoremap [<CR>  [<CR>]<Esc>O
inoremap [[     [
inoremap []     []

inoremap (      ()<Left>
inoremap (<CR>  (<CR>)<Esc>O
inoremap ((     (
inoremap ()     ()

" Do these replacements only in js-files:
autocmd Filetype javascript inoremap devv <Esc>Odev(`<CR>`)<Esc>O
autocmd Filetype javascript inoremap funn function() {<CR>}<Esc>O
autocmd Filetype javascript inoremap fori for(var i=0; i < items.length; i++) {<CR>}<Esc>O
autocmd Filetype javascript inoremap forj for(var j=0; j < jtems.length; j++) {<CR>}<Esc>O
autocmd Filetype javascript inoremap kel  else {<CR>}<Esc>O
autocmd Filetype javascript inoremap keli else if(27) {<CR>}<Esc>O
autocmd Filetype javascript inoremap kif  if(42) {<CR>}<Esc>O
autocmd Filetype javascript inoremap kon  <Esc>Oconsole.debug()<Left>
" autocmd Filetype javascript inoremap kon  <Esc>Oconsole.debug(<CR>)<Esc>O



" SPACES

set shiftwidth=4    " How many spaces long shall a tab be in general? 
set softtabstop=4   " Especially when editing.
set tabstop=4       " Especially when reading.
set expandtab       " Force tabs to always be spaces. 
set smartindent     " Preserve indent when breaking the line.

" Two spaces indents for css, html, js and json-files:
autocmd Filetype html setlocal ts=2 sts=2 sw=2
autocmd Filetype javascript setlocal ts=2 sts=2 sw=2
autocmd Filetype json setlocal ts=2 sts=2 sw=2
autocmd Filetype css setlocal ts=2 sts=2 sw=2

" Remove trailing spaces in js-files right before saving:
autocmd BufWritePre *.js :%s/\s\+$//e
" Also for Python scripts:
autocmd BufWritePre *.py :%s/\s\+$//e




" COPY AND PASTE
" Do ':set paste' on pasting and ':set nopaste' after pasting.
" https://unix.stackexchange.com/questions/199203/why-does-vim-indent-pasted-code-incorrectly
function! WrapForScreen(s)
  if exists('$TMUX') || match($TERM, "screen")==-1
    return a:s
  endif

  let screen_start = "\<Esc>P"
  let screen_end = "\<Esc>\\"

  return screen_start . a:s . screen_end
endfunction


let &t_SI .= WrapForScreen("\<Esc>[?2004h")
let &t_EI .= WrapForScreen("\<Esc>[?2004l")

inoremap <special> <expr> <Esc>[200~ XTermPasteBegin()

function! XTermPasteBegin()
  set pastetoggle=<Esc>[201~
  set paste
  return ""
endfunction


" SYNTAX-HIGHLIGHTNING

syntax on

" Make less-files behave like js-files for syntax-highlighting:
au BufNewFile,BufRead *.less set filetype=javascript
" Make sass-files behave like css-files:
au BufNewFile,BufRead *.scss set filetype=css



" WINDOW-TITLE

" Show always currently opened filename in window-title:
" Prepare window-title of filename-var... 
autocmd BufEnter * let &titlestring = ' ' . expand("%:t") 
set title           " .. and set it.



" END-OF-FILE-SYMBOL:

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



" AFTER-SAVE-HOOKS

" When saving SASS-files, execute 'sas' defined in '.bash_aliases':
autocmd BufWritePost *.scss !sas <afile>
" When saving PYJS-files, execute 'pytojs' defined in '.bash_aliases':
autocmd BufWritePost *.pyjs !pytojs <afile>



" MISCELLANEOUS

" Make sure using :! for starting a shell-cmd of vim's lastline
" always works, activate interactive mode:
set shellcmdflag=-ic

