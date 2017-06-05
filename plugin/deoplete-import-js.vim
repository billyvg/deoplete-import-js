" Borrowed from https://github.com/wokalski/autocomplete-flow
if exists('g:loaded_deoplete_import_js')
  finish
endif

let g:loaded_deoplete_import_js = 1

let local_bin = finddir('node_modules', '.;') . '/.bin/importjs'
if matchstr(local_bin, "^\/\\w") == ''
    let local_bin= getcwd() . "/" . local_bin
endif

if executable(local_bin)
  let g:deoplete_import_js#bin = local_bin
else
  let g:deoplete_import_js#bin = 'importjs'
endif
