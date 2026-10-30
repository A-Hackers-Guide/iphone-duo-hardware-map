# `UIKeyboardCameraOverlayPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardCameraBasePresentationController`
- 8 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSLayoutConstraint" _topLayoutConstraint;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"UIKeyboardCameraGrabberView" _grabberView;
d _keyboardCameraNormalHeight;
d _keyboardCameraFullScreenHeight;
d _keyboardCameraHeight;
d _panningStartingHeight;
B _isLandscape;
```

## Instance methods

```
-[UIKeyboardCameraOverlayPresentationController presentationTransitionDidEnd:];
-[UIKeyboardCameraOverlayPresentationController _handlePan:];
-[UIKeyboardCameraOverlayPresentationController updatesGuideDuringRotation];
-[UIKeyboardCameraOverlayPresentationController viewWillTransitionToSize:withTransitionCoordinator:];
-[UIKeyboardCameraOverlayPresentationController frameOfPresentedViewInContainerView];
-[UIKeyboardCameraOverlayPresentationController dismissalTransitionWillBegin];
-[UIKeyboardCameraOverlayPresentationController dismissalTransitionDidEnd:];
-[UIKeyboardCameraOverlayPresentationController presentationTransitionWillBegin];
-[UIKeyboardCameraOverlayPresentationController _installGrabber];
-[UIKeyboardCameraOverlayPresentationController _determinePortraitHeights];
```
