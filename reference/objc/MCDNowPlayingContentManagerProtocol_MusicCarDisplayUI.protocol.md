# `MCDNowPlayingContentManagerProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 9 properties, 18 instance methods, 0 class methods

## Properties

```
@property (TB,N) limitedUI;
@property (Tq,R,N) playerState;
@property (T@"MPModelSong",R,N) currentPlayingSong;
@property (T@"MPModelPlaylistEntry",R,N) currentPlayingPlaylistEntry;
@property (T@"MPModelPlaylist",R,N) currentPlayingPlaylist;
@property (T@"MPModelRadioStation",R,N) currentPlayingRadioStation;
@property (T#,W,N) tableCellClass;
@property (T@"NSString",R,C,N) nowPlayingBundleID;
@property (TB,N) shouldHideBackButton;
```

## Instance methods

```
-[MCDNowPlayingContentManagerProtocol reloadData];
-[MCDNowPlayingContentManagerProtocol limitedUI];
-[MCDNowPlayingContentManagerProtocol setLimitedUI:];
-[MCDNowPlayingContentManagerProtocol playerState];
-[MCDNowPlayingContentManagerProtocol shouldHideBackButton];
-[MCDNowPlayingContentManagerProtocol viewWillDisappear];
-[MCDNowPlayingContentManagerProtocol tableCellClass];
-[MCDNowPlayingContentManagerProtocol nowPlayingBundleID];
-[MCDNowPlayingContentManagerProtocol beginRequestObservation];
-[MCDNowPlayingContentManagerProtocol currentPlayingPlaylist];
-[MCDNowPlayingContentManagerProtocol currentPlayingPlaylistEntry];
-[MCDNowPlayingContentManagerProtocol currentPlayingRadioStation];
-[MCDNowPlayingContentManagerProtocol currentPlayingSong];
-[MCDNowPlayingContentManagerProtocol endRequestObservation];
-[MCDNowPlayingContentManagerProtocol initWithDelegate:dataSource:bundleID:];
-[MCDNowPlayingContentManagerProtocol setShouldHideBackButton:];
-[MCDNowPlayingContentManagerProtocol setTableCellClass:];
-[MCDNowPlayingContentManagerProtocol updateNoContentViewFrameIfNeeded];
```
