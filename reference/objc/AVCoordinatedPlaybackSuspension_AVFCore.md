# `AVCoordinatedPlaybackSuspension`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSString" _reason;
@"AVPlaybackCoordinator" _coordinator;
^{OpaqueFigTimelineCoordinatorSuspension=} _figSuspension;
@"NSDate" _beginDate;
@"AVCoordinatedPlaybackSuspension" _interstitialSuspension;
^{OpaqueFigSimpleMutex=} _iVarMutex;
```

## Properties

```
@property (T@"NSString",R,N,V_reason) reason;
@property (T@"NSDate",R,N,V_beginDate) beginDate;
```

## Instance methods

```
-[AVCoordinatedPlaybackSuspension beginDate];
-[AVCoordinatedPlaybackSuspension dealloc];
-[AVCoordinatedPlaybackSuspension end];
-[AVCoordinatedPlaybackSuspension reason];
-[AVCoordinatedPlaybackSuspension _figSuspension];
-[AVCoordinatedPlaybackSuspension _removeSuspension];
-[AVCoordinatedPlaybackSuspension _setInterstitialSuspension:];
-[AVCoordinatedPlaybackSuspension endProposingNewTime:];
-[AVCoordinatedPlaybackSuspension initWithCoordinator:reason:];
```
