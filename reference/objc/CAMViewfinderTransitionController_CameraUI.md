# `CAMViewfinderTransitionController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<CAMViewfinderTransitionable>" _target;
@"CAMViewfinderOpenAndCloseTransition" __openAndCloseTransition;
@"CAMViewfinderFlipTransition" __flipTransition;
```

## Properties

```
@property (T@"CAMViewfinderOpenAndCloseTransition",&,N,S_setOpenAndCloseTransition:,V__openAndCloseTransition) _openAndCloseTransition;
@property (T@"CAMViewfinderFlipTransition",&,N,S_setFlipTransition:,V__flipTransition) _flipTransition;
@property (T@"<CAMViewfinderTransitionable>",W,N,V_target) target;
```

## Instance methods

```
-[CAMViewfinderTransitionController setTarget:];
-[CAMViewfinderTransitionController target];
-[CAMViewfinderTransitionController _flipTransition];
-[CAMViewfinderTransitionController _openAndCloseTransition];
-[CAMViewfinderTransitionController _setFlipTransition:];
-[CAMViewfinderTransitionController _setOpenAndCloseTransition:];
-[CAMViewfinderTransitionController closeAndRotateWithDirection:withCompletionHandler:];
-[CAMViewfinderTransitionController closeWithBlur:animated:withCompletionHandler:];
-[CAMViewfinderTransitionController closeWithSiriContinuationVideoPreviewSnapshotWithCompletionHandler:];
-[CAMViewfinderTransitionController handleApplicationDidEnterBackground];
-[CAMViewfinderTransitionController openForReason:animated:withCompletionHandler:];
```
