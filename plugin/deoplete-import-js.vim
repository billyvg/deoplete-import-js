" Borrowed from https://github.com/wokalski/autocomplete-flow
if exists('g:loaded_deoplete_import_js')
  finish
endif

let g:loaded_deoplete_import_js = 1

" use global importjs by default
let g:deoplete_import_js#bin = 'importjs'
