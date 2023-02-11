General terminal theme: https://github.com/catppuccin/catppuccin

Download nerd font (Caskaydia Cove): https://www.nerdfonts.com/font-downloads

Replicate bashbunni's Tmux Setup: https://www.youtube.com/watch?v=78FjNkrPn5Y

Replicate bashbunni's Neovim Setup: https://www.youtube.com/watch?v=ZvhzrltuA9U&list=PL3PYGQRVAjrMxP5HK45CTnR7Yv-QYR1Qp&index=1
 - Where she does :PlugInstall, run :PackerUpdate and :PackerSync instead.

Download gradient timer: https://github.com/caarlos0/timer

Download oh-my-zsh: https://ohmyz.sh/#install

Download spotify-tui & dracula theme: 
 - https://github.com/Rigellute/spotify-tui#configuration
 - https://draculatheme.com/spotify-tui

Setup Spotify:
 - Download Rust + Cargo for spotifyd: 
   * https://doc.rust-lang.org/cargo/getting-started/installation.html
 - Connect Spotify's API & set theme in configuration file:
   * https://github.com/Rigellute/spotify-tui
   * https://github.com/catppuccin/spotify-tui
 - Follow Ubuntu installation guide:
   * https://spotifyd.github.io/spotifyd/installation/Ubuntu.html
   * Exchange `cargo build --release` for `cargo build --release --no-default-features --features alsa_backend,dbus_keyring,dbus_mpris`
   * Afterward, run `cargo install --path . --locked`
 - Load `spotifyd.config` to auto-login & understanding how to set/retrieve passphrase:
   * https://spotifyd.github.io/spotifyd/config/File.html
   * https://www.chucknemeth.com/linux/security/keyring/secret-tool
 - **Run Spotify**
   * Activate spotifyd daemon `spotifyd`.
   	* Try `spotifyd -u USERNAME -p PASSWORD` if failure to authenticate.
	* Run `spotifyd --no-daemon` to troubleshoot login issues.
   * Activate Spotify API `spt` -> `d` -> Select `Spotify@hostname`
