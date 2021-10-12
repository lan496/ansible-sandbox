if &compatible
  set nocompatible
endif

scriptencoding utf-8
set encoding=utf-8

filetype plugin indent on

" Turn on syntax highlighting.
syntax enable

" Disable the default Vim startup message.
set shortmess+=I

" display
set number
set ruler
set cursorline
set cursorcolumn
set laststatus=2
set cmdheight=2
set showmatch
set helpheight=999
set list
set listchars=tab:>.,eol:↩,extends:>,precedes:<,trail:_,nbsp:%
set foldmethod=marker
set t_Co=256

" cursor
set backspace=indent,eol,start
set whichwrap=b,s,h,l,<,>,[,]
set scrolloff=8
set sidescrolloff=16
set sidescroll=1

" file
set confirm
set hidden
set autoread
set nobackup
set noswapfile
set ambiwidth=double
set fileencodings=utf-8,euc-jp,sjis,cp932,iso-2022-jp

" search and permutate
set hlsearch
set incsearch
set ignorecase
set smartcase
set wrapscan
set gdefault

" tab and indent
set expandtab
set tabstop=2
set shiftwidth=2
set softtabstop=2
set autoindent
set smartindent

set smarttab
set virtualedit=block

"OS"
set clipboard=unnamed,unnamedplus
set mouse=a

" cmd
set wildmenu wildmode=list:longest,full
set wildignore=*.o,*.obj,*.pyc,*.so,*.dll
set history=10000

" Disable audible bell because it's annoying.
set noerrorbells visualbell t_vb=

let g:vim_json_syntax_conceal = 0
let g:tex_conceal = ""
