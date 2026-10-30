# `_TtC11MediaCoreUI29NowPlayingVideoPlayerDelegate`

- Image: [`/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI`](../userland/System__Library__PrivateFrameworks__MediaCoreUI.framework__MediaCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MPCVideoOutputDelegate`
- 8 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
_$syyScMYccSg becomeFirstResponder;
Combine.CurrentValueSubject _$sySb Swift.Never isVideoFullscreenSubject;
Combine.CurrentValueSubject _$sySb Swift.Never isVideoObscuringContentSubject;
_$sSh -> Combine.AnyCancellable subscriptions;
MediaCoreUI.NowPlayingViewModel @unowned type viewModel;
MediaCoreUI.NowPlayingVideoPlayerDelegate.ObservableState observableState;
MediaCoreUI.VideoEnablementContext ? previousVideoEnablementContext;
Combine.AnyCancellable ? presentationSizeSubscription;
```

## Instance methods

```
-[_TtC11MediaCoreUI29NowPlayingVideoPlayerDelegate init];
-[_TtC11MediaCoreUI29NowPlayingVideoPlayerDelegate videoOutput:failedToStartPictureInPictureWithError:];
-[_TtC11MediaCoreUI29NowPlayingVideoPlayerDelegate videoOutput:willBeginFullScreenPresentationWithAnimationCoordinator:];
-[_TtC11MediaCoreUI29NowPlayingVideoPlayerDelegate videoOutput:willEndFullScreenPresentationWithAnimationCoordinator:];
-[_TtC11MediaCoreUI29NowPlayingVideoPlayerDelegate videoOutputDidStartPictureInPicture:];
-[_TtC11MediaCoreUI29NowPlayingVideoPlayerDelegate videoOutputDidStopPictureInPicture:];
-[_TtC11MediaCoreUI29NowPlayingVideoPlayerDelegate videoOutputWillStartPictureInPicture:];
-[_TtC11MediaCoreUI29NowPlayingVideoPlayerDelegate videoOutputWillStopPictureInPicture:];
```
