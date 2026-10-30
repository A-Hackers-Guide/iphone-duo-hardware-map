# `MCDPlayableContentPlaybackManager`

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MCDNowPlayingContentManager`
- Protocols: `MPRequestResponseControllerDelegate`, `UITableViewDelegate`, `UITableViewDataSource`
- 4 instance variables, 8 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _seeking;
@"MCDPCModel" _model;
q _playingItemIndex;
q _totalItemCount;
```

## Properties

```
@property (TB,N,GisSeeking,V_seeking) seeking;
@property (T@"MCDPCModel",&,N,V_model) model;
@property (Tq,N,V_playingItemIndex) playingItemIndex;
@property (Tq,N,V_totalItemCount) totalItemCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MCDPlayableContentPlaybackManager model];
-[MCDPlayableContentPlaybackManager tableView:numberOfRowsInSection:];
-[MCDPlayableContentPlaybackManager tableView:cellForRowAtIndexPath:];
-[MCDPlayableContentPlaybackManager setModel:];
-[MCDPlayableContentPlaybackManager isSeeking];
-[MCDPlayableContentPlaybackManager _processResponse:error:];
-[MCDPlayableContentPlaybackManager setSeeking:];
-[MCDPlayableContentPlaybackManager tableView:didSelectRowAtIndexPath:];
-[MCDPlayableContentPlaybackManager totalItemCount];
-[MCDPlayableContentPlaybackManager _itemAtIndexPath:];
-[MCDPlayableContentPlaybackManager setTotalItemCount:];
-[MCDPlayableContentPlaybackManager nowPlayingViewController:buttonShouldBeActive:];
-[MCDPlayableContentPlaybackManager nowPlayingViewController:didSendAction:state:];
-[MCDPlayableContentPlaybackManager nowPlayingViewController:shouldDisplayButton:withImage:existingIdentifier:tinted:];
-[MCDPlayableContentPlaybackManager nowPlayingViewControllerAddToLibrary:];
-[MCDPlayableContentPlaybackManager nowPlayingViewControllerCanShowAddToLibrary:];
-[MCDPlayableContentPlaybackManager nowPlayingViewControllerCanShowMore:];
-[MCDPlayableContentPlaybackManager nowPlayingViewControllerIsRightHandDrive:];
-[MCDPlayableContentPlaybackManager nowPlayingViewControllerMore:];
-[MCDPlayableContentPlaybackManager _adjustedIndexPathForPlaybackQueue:];
-[MCDPlayableContentPlaybackManager _alertActionForFeedbackCommand:fallbackTitle:];
-[MCDPlayableContentPlaybackManager _handleHamburgerActionSheet];
-[MCDPlayableContentPlaybackManager _jumpBackwardInterval];
-[MCDPlayableContentPlaybackManager _jumpForwardInterval];
-[MCDPlayableContentPlaybackManager _skipIntervalButtonImageForInterval:size:];
-[MCDPlayableContentPlaybackManager _updateTrackQueueIndex];
-[MCDPlayableContentPlaybackManager playingItemIndex];
-[MCDPlayableContentPlaybackManager setPlayingItemIndex:];
```
