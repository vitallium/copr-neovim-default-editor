Name: neovim-default-editor
Version: 0.1.1
Release: 1%{?dist}
Summary: Set neovim as the default editor

License: Neovim and MIT
BuildArch: noarch

Source0: neovim-default-editor.sh
Source1: neovim-default-editor.csh
Source2: neovim-default-editor.fish

Conflicts: system-default-editor
# conflict with nano-default-editor which doesn't provide system-default-editor
# remove after F33 is EOL
Conflicts: nano-default-editor < 5.3-3
Conflicts: vim-default-editor
Provides: system-default-editor
Requires: neovim

%description
This package contains files needed to set Neovim as the default editor.

%install
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
install -p -m644 %{SOURCE0} %{buildroot}/%{_sysconfdir}/profile.d/neovim-default-editor.sh
install -p -m644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/profile.d/neovim-default-editor.csh
mkdir -p %{buildroot}/%{_datadir}/fish/vendor_conf.d/
install -p -m644 %{SOURCE2} %{buildroot}/%{_datadir}/fish/vendor_conf.d/neovim-default-editor.fish
mkdir -p %{buildroot}/%{_datadir}/fish/vendor_functions.d/

%files
%dir %{_datadir}/fish/vendor_conf.d
%{_datadir}/fish/vendor_conf.d/neovim-default-editor.fish
%config(noreplace) %{_sysconfdir}/profile.d/neovim-default-editor.*


%changelog
* Sun Jun 26 2022 Vitaly Slobodin <vitaliy.slobodin@gmail.com> - 0.1.1
- Initial version
