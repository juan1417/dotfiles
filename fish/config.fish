source /usr/share/cachyos-fish-config/cachyos-config.fish

# overwrite greeting
# potentially disabling fastfetch
#function fish_greeting
#    # smth smth
#end
set -gx GTK_THEME vimix-dark-beryl
set -gx QT_QPA_PLATFORMTHEME qt5ct
alias wofi="env GTK_THEME=vimix-dark-beryl wofi --style ~/.config/wofi/style.css"
