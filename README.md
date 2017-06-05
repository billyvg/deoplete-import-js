# deoplete-import-js

A deoplete source for [import-js](https://github.com/Galooshi/import-js)

Autocompletes js modules and auto-adds import statements for corresponding module Edit
Add topics

![example](https://raw.githubusercontent.com/billyvg/deoplete-import-js/master/example.gif)

## Installation

### Dependencies
* [deoplete](https://github.com/Shougo/deoplete.nvim)
* [vim-import-js](https://github.com/Galooshi/vim-import-js)
  * [import-js](https://github.com/Galooshi/import-js)

### Example Installation via `vim-plug`
```viml
call plug#begin('~/.vim/plugged')
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
  Plug 'Galooshi/vim-import-js', { 'do': 'npm install -g import-js' }
  Plug 'billyvg/deoplete-import-js'
call plug#end()
```

## Configuration

```viml
let g:deoplete_import_js#bin = 'importjs'
```
