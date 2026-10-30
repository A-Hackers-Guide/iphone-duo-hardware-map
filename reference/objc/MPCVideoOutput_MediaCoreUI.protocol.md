# `MPCVideoOutput` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MediaCoreUI.framework/MediaCoreUI`](../userland/System__Library__PrivateFrameworks__MediaCoreUI.framework__MediaCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 17 properties, 32 instance methods, 0 class methods

## Properties

```
@property (T@"<MPCVideoOutputDelegate>",W,N) videoOutputDelegate;
@property (T@"UIViewController",R,N) playerViewController;
@property (T@"AVPlayerLayer",R,N) playerLayer;
@property (TB,N) showsPlaybackControls;
@property (T{CGSize=dd},R,N) presentationSize;
@property (T@"NSString",C,N) videoGravity;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) videoBounds;
@property (TB,R,N,GisReadyForDisplay) readyForDisplay;
@property (TB,N) videoEnabled;
@property (TB,R,N,GisExternalPlaybackActive) externalPlaybackActive;
@property (TB,R,N,GisPictureInPictureActive) pictureInPictureActive;
@property (TB,N) allowsPictureInPicturePlayback;
@property (TB,N) canStartPictureInPictureAutomaticallyFromInline;
@property (T@"NSArray",C,N) customControlItems;
@property (TB,N) allowsVideoFrameAnalysis;
@property (TB,N) hidesVideoPlayerBackground;
@property (TB,N) exitsFullScreenWhenPlaybackEnds;
```

## Instance methods

```
-[MPCVideoOutput allowsPictureInPicturePlayback];
-[MPCVideoOutput videoEnabled];
-[MPCVideoOutput isPictureInPictureActive];
-[MPCVideoOutput playerLayer];
-[MPCVideoOutput setAllowsVideoFrameAnalysis:];
-[MPCVideoOutput setVideoEnabled:];
-[MPCVideoOutput isReadyForDisplay];
-[MPCVideoOutput setHidesVideoPlayerBackground:];
-[MPCVideoOutput setCanStartPictureInPictureAutomaticallyFromInline:];
-[MPCVideoOutput setAllowsPictureInPicturePlayback:];
-[MPCVideoOutput isExternalPlaybackActive];
-[MPCVideoOutput videoBounds];
-[MPCVideoOutput setCustomControlItems:];
-[MPCVideoOutput showsPlaybackControls];
-[MPCVideoOutput exitFullScreenWithCompletion:];
-[MPCVideoOutput hidesVideoPlayerBackground];
-[MPCVideoOutput presentationSize];
-[MPCVideoOutput customControlItems];
-[MPCVideoOutput videoGravity];
-[MPCVideoOutput videoOutputDelegate];
-[MPCVideoOutput stopPictureInPicture];
-[MPCVideoOutput setExitsFullScreenWhenPlaybackEnds:];
-[MPCVideoOutput showFullScreenPresentationFromView:completion:];
-[MPCVideoOutput setVideoOutputDelegate:];
-[MPCVideoOutput setVideoGravity:];
-[MPCVideoOutput allowsVideoFrameAnalysis];
-[MPCVideoOutput setShowsPlaybackControls:];
-[MPCVideoOutput exitsFullScreenWhenPlaybackEnds];
-[MPCVideoOutput setVideoEnabled:reason:];
-[MPCVideoOutput playerViewController];
-[MPCVideoOutput enterFullScreenWithCompletion:];
-[MPCVideoOutput canStartPictureInPictureAutomaticallyFromInline];
```
