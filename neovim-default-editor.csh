# Ensure nvim (neovim) is set as EDITOR if it isn't already set

if ( ! ($?EDITOR) ) then
    setenv EDITOR "/usr/bin/nvim"
endif
