# `CFXViewfinderFlipTransition`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"UIView" _viewfinderView;
@"CAMSnapshotView" __frontSnapshotView;
@"CAMSnapshotView" __backSnapshotView;
@"CAMSnapshotView" __targetSnapshotView;
Q __currentAnimationID;
```

## Properties

```
@property (T@"UIView",W,N,V_viewfinderView) viewfinderView;
@property (T@"CAMSnapshotView",&,N,S_setFrontSnapshotView:,V__frontSnapshotView) _frontSnapshotView;
@property (T@"CAMSnapshotView",&,N,S_setBackSnapshotView:,V__backSnapshotView) _backSnapshotView;
@property (T@"CAMSnapshotView",&,N,S_setTargetSnapshotView:,V__targetSnapshotView) _targetSnapshotView;
@property (TQ,N,S_setCurrentAnimationID:,V__currentAnimationID) _currentAnimationID;
```

## Instance methods

```
-[CFXViewfinderFlipTransition viewfinderView];
-[CFXViewfinderFlipTransition _backSnapshotTargetRadiansForDirection:frontSnapshotRadians:];
-[CFXViewfinderFlipTransition _backSnapshotView];
-[CFXViewfinderFlipTransition _cleanupFromFlipTransition];
-[CFXViewfinderFlipTransition _currentAnimationID];
-[CFXViewfinderFlipTransition _frontSnapshotTargetRadiansForDirection:fromRadians:];
-[CFXViewfinderFlipTransition _frontSnapshotView];
-[CFXViewfinderFlipTransition _getCurrentRadians:targetRadians:forDirection:withAnimation:onFrontSnapshotLayer:];
-[CFXViewfinderFlipTransition _setBackSnapshotView:];
-[CFXViewfinderFlipTransition _setCurrentAnimationID:];
-[CFXViewfinderFlipTransition _setFrontSnapshotView:];
-[CFXViewfinderFlipTransition _setTargetSnapshotView:];
-[CFXViewfinderFlipTransition _snapshotFlipAnimationFromValue:toValue:];
-[CFXViewfinderFlipTransition _targetSnapshotView];
-[CFXViewfinderFlipTransition completeTransitionToLivePreviewWithCompletionHandler:];
-[CFXViewfinderFlipTransition performFlipTransitionWithDirection:completionHandler:];
-[CFXViewfinderFlipTransition setViewfinderView:];
-[CFXViewfinderFlipTransition initWithViewfinderView:];
```
