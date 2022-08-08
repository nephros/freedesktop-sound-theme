Name:          freedesktop-sound-theme
Version:       0.8
Release:       1
License:       Public Domain
Group:         Unspecified
Summary:       Freedesktop.org sound theme
Source:        %{name}-%{version}.tar.gz
Source1:       stereo.index
BuildArch:     noarch
Requires:      sound-theme-freedesktop

%define themename freedesktop
%define themedir %{_datadir}/sounds/%{themename}
#%%define stereodir %%{themedir}/stereo

%description
Makes sounds from the Freedesktop.org sound theme available as ring- and other tones.

These audio files are actually already installed, this just adds a config file which makes them visible.

%prep

%install
install -D -m 644 %{SOURCE1} %{buildroot}%{themedir}/stereo.index

%build

%files
%defattr(-,root,root,-)
%{themedir}/stereo.index


%postun -p /bin/sh
    systemctl --no-reload preset --user --global restart ambienced >/dev/null 2>&1 || : 


%post -p /bin/sh
if [ $1 -eq 1 ] ; then 
        # Initial installation 
        systemctl --no-reload preset --user --global restart ambienced >/dev/null 2>&1 || : 
fi 

%changelog

