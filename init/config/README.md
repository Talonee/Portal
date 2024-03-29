__General terminal theme:__ https://github.com/catppuccin/catppuccin

__Download nerd font (Caskaydia Cove):__ https://www.nerdfonts.com/font-downloads

__Replicate bashbunni's Tmux Setup:__ https://www.youtube.com/watch?v=78FjNkrPn5Y
 - `nvim ~/.tmux.conf` to simply edit plugins. Very simple. Then \<prefix\>+I to reload.

__Replicate bashbunni's Neovim Setup:__ https://www.youtube.com/watch?v=ZvhzrltuA9U&list=PL3PYGQRVAjrMxP5HK45CTnR7Yv-QYR1Qp&index=1
 - Where she does :PlugInstall, run :PackerUpdate and :PackerSync instead.

__More Neovim customization:__
 - `nvim ~/.config/nvim/after/plugin/plugins.lua` to install new plugins
 - `nvim ~/.config/nvim/init.lua` to ensure custom.lua is referenced
 - `nvim ~/.config/nvim/lua/me/custom.lua` to modify plugins' setup
 - `nvim ./keymap.lua` to modify keymaps
 - `nvim ./options.lua` to modify neovim's setting like `set (no)relativenumber` to adjust line counts
 
__Download gradient timer:__ https://github.com/caarlos0/timer

__Download oh-my-zsh:__ https://ohmyz.sh/#install

__Install zsh-syntax-highlighting:__ https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md 
 - Download catppuccin's theme: https://github.com/catppuccin/zsh-syntax-highlighting
 - Follow instructions, then in .zshrc, add the following lines in this order:
   * `source ~/.zsh/catppuccin_mocha-zsh-syntax-highlighting.zsh` 
   * `plugins=(git zsh-syntax-highlighting)`

__Download spotify-tui & dracula theme:__ 
 - https://github.com/Rigellute/spotify-tui#configuration
 - https://draculatheme.com/spotify-tui

__Setup Spotify:__
 - Download Rust + Cargo for spotifyd: 
   * https://doc.rust-lang.org/cargo/getting-started/installation.html
 - Connect Spotify's API & set theme in configuration file:
   * https://github.com/Rigellute/spotify-tui
   * https://github.com/catppuccin/spotify-tui
 - Follow Ubuntu installation guide:
   * https://spotifyd.github.io/spotifyd/installation/Ubuntu.html
   * Exchange `cargo build --release` for `cargo build --release --no-default-features --features alsa_backend,dbus_keyring,dbus_mpris`
   * Afterward, run `cargo install --path . --locked`
 - Load `~/.config/spotifyd/spotifyd.config` to auto-login & understanding how to set/retrieve passphrase:
   * https://spotifyd.github.io/spotifyd/config/File.html
   * https://www.chucknemeth.com/linux/security/keyring/secret-tool
 - Run Spotify
   * Activate spotifyd daemon `spotifyd`.
   	* Try `spotifyd -u USERNAME -p PASSWORD` if failure to authenticate.
	* Run `spotifyd --no-daemon` to troubleshoot login issues.
   * Activate Spotify API `spt` -> `d` -> Select `Spotify@hostname`
