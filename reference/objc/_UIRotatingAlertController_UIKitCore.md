# `_UIRotatingAlertController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIAlertController`
- 6 instance variables, 2 properties, 17 instance methods, 0 class methods

## Instance variables

```
Q _arrowDirections;
B _isRotating;
B _readyToPresentAfterRotation;
@"UIViewController" _presentedViewControllerWhileRotating;
@"<UIPopoverPresentationControllerDelegate>" _popoverPresentationControllerDelegateWhileRotating;
@"<_UIRotatingAlertControllerDelegate>" _rotatingSheetDelegate;
```

## Properties

```
@property (T@"<_UIRotatingAlertControllerDelegate>",W,N,V_rotatingSheetDelegate) rotatingSheetDelegate;
@property (TQ,N,V_arrowDirections) arrowDirections;
```

## Instance methods

```
-[_UIRotatingAlertController init];
-[_UIRotatingAlertController dealloc];
-[_UIRotatingAlertController _canShowWhileLocked];
-[_UIRotatingAlertController presentSheet];
-[_UIRotatingAlertController arrowDirections];
-[_UIRotatingAlertController _didRotateAndLayout];
-[_UIRotatingAlertController _presentingViewControllerDidChange:];
-[_UIRotatingAlertController _presentingViewControllerWillChange:];
-[_UIRotatingAlertController _shouldAbortAdaptationFromTraitCollection:toTraitCollection:withTransitionCoordinator:];
-[_UIRotatingAlertController _updateSheetPositionAfterRotation];
-[_UIRotatingAlertController didRotate:];
-[_UIRotatingAlertController doneWithSheet];
-[_UIRotatingAlertController presentSheetFromRect:];
-[_UIRotatingAlertController rotatingSheetDelegate];
-[_UIRotatingAlertController setArrowDirections:];
-[_UIRotatingAlertController setRotatingSheetDelegate:];
-[_UIRotatingAlertController willRotate:];
```
