# `CAMViewfinderFlipTransition`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"<CAMViewfinderTransitionable>" __transitionableViewfinder;
@"CAMSnapshotView" __frontSnapshotView;
@"CAMSnapshotView" __backSnapshotView;
@"CAMSnapshotView" __targetSnapshotView;
Q __currentAnimationID;
```

## Properties

```
@property (T@"<CAMViewfinderTransitionable>",R,W,N,V__transitionableViewfinder) _transitionableViewfinder;
@property (T@"CAMSnapshotView",&,N,S_setFrontSnapshotView:,V__frontSnapshotView) _frontSnapshotView;
@property (T@"CAMSnapshotView",&,N,S_setBackSnapshotView:,V__backSnapshotView) _backSnapshotView;
@property (T@"CAMSnapshotView",&,N,S_setTargetSnapshotView:,V__targetSnapshotView) _targetSnapshotView;
@property (TQ,N,S_setCurrentAnimationID:,V__currentAnimationID) _currentAnimationID;
```

## Instance methods

```
-[CAMViewfinderFlipTransition _backSnapshotTargetRadiansForDirection:frontSnapshotRadians:];
-[CAMViewfinderFlipTransition _backSnapshotView];
-[CAMViewfinderFlipTransition _cleanupFromFlipTransition];
-[CAMViewfinderFlipTransition _currentAnimationID];
-[CAMViewfinderFlipTransition _frontSnapshotTargetRadiansForDirection:fromRadians:];
-[CAMViewfinderFlipTransition _frontSnapshotView];
-[CAMViewfinderFlipTransition _getCurrentRadians:targetRadians:forDirection:withAnimation:onFrontSnapshotLayer:];
-[CAMViewfinderFlipTransition _setBackSnapshotView:];
-[CAMViewfinderFlipTransition _setCurrentAnimationID:];
-[CAMViewfinderFlipTransition _setFrontSnapshotView:];
-[CAMViewfinderFlipTransition _setTargetSnapshotView:];
-[CAMViewfinderFlipTransition _snapshotFlipAnimationFromValue:toValue:];
-[CAMViewfinderFlipTransition _targetSnapshotView];
-[CAMViewfinderFlipTransition _transitionableViewfinder];
-[CAMViewfinderFlipTransition completeTransitionToLivePreviewWithCompletionHandler:];
-[CAMViewfinderFlipTransition initWithTransitionableViewfinder:];
-[CAMViewfinderFlipTransition performFlipTransitionWithDirection:completionHandler:];
```
