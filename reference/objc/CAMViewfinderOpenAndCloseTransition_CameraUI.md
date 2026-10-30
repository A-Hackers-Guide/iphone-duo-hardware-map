# `CAMViewfinderOpenAndCloseTransition`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _didEnterBackground;
@"<CAMViewfinderTransitionable>" __transitionableViewfinder;
@"CAMSnapshotView" __snapshotView;
```

## Properties

```
@property (T@"<CAMViewfinderTransitionable>",R,W,N,V__transitionableViewfinder) _transitionableViewfinder;
@property (T@"CAMSnapshotView",&,N,S_setSnapshotView:,V__snapshotView) _snapshotView;
@property (TB,N,V_didEnterBackground) didEnterBackground;
```

## Instance methods

```
-[CAMViewfinderOpenAndCloseTransition didEnterBackground];
-[CAMViewfinderOpenAndCloseTransition _setSnapshotView:];
-[CAMViewfinderOpenAndCloseTransition _snapshotView];
-[CAMViewfinderOpenAndCloseTransition _closeViewfinder:animated:withCompletionHandler:];
-[CAMViewfinderOpenAndCloseTransition _existingSnapshotViewCreateIfNecessary:removedOnCompletion:];
-[CAMViewfinderOpenAndCloseTransition _transitionableViewfinder];
-[CAMViewfinderOpenAndCloseTransition closeAnimated:withCompletionHandler:];
-[CAMViewfinderOpenAndCloseTransition closeWithVideoPreviewSnapshot];
-[CAMViewfinderOpenAndCloseTransition closeWithoutBlurring];
-[CAMViewfinderOpenAndCloseTransition initWithTransitionableViewfinder:];
-[CAMViewfinderOpenAndCloseTransition openAnimated:withCompletionHandler:];
-[CAMViewfinderOpenAndCloseTransition setDidEnterBackground:];
```
