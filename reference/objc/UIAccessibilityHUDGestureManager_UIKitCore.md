# `UIAccessibilityHUDGestureManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegatePrivate`
- 8 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"<UIAccessibilityHUDGestureDelegate>" _delegate;
@"UIViewController" _viewControllerDisplayingHUD;
@"_UIAccessibilityHUDLongPressGestureRecognizer" _recognizer;
@"_UIAccessibilityHUDGateGestureRecognizer" _gateRecognizer;
@"NSMutableArray" _subscribedConcurrentGestureRecognizers;
B _delegateDirectlyShowsHUD;
B _isInvalidated;
```

## Properties

```
@property (T@"UIGestureRecognizer",R,N) _recognizer;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIAccessibilityHUDGestureManager initWithView:delegate:];
-[UIAccessibilityHUDGestureManager _invalidate];
-[UIAccessibilityHUDGestureManager dealloc];
-[UIAccessibilityHUDGestureManager view];
-[UIAccessibilityHUDGestureManager _gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIAccessibilityHUDGestureManager gestureRecognizerShouldBegin:];
-[UIAccessibilityHUDGestureManager _gestureRecognizer:canCancelGestureRecognizer:];
-[UIAccessibilityHUDGestureManager _backOff];
-[UIAccessibilityHUDGestureManager _bestViewControllerForView];
-[UIAccessibilityHUDGestureManager _clearButtonItemGestureSubscriptions];
-[UIAccessibilityHUDGestureManager _concurrentGestureRecognizerFired:];
-[UIAccessibilityHUDGestureManager _didToggleLargeContentViewer:];
-[UIAccessibilityHUDGestureManager _dismissAccessibilityHUD];
-[UIAccessibilityHUDGestureManager _gestureRecognizerChanged:];
-[UIAccessibilityHUDGestureManager _openGate];
-[UIAccessibilityHUDGestureManager _recognizer];
-[UIAccessibilityHUDGestureManager _setRecognizersEnabled:];
-[UIAccessibilityHUDGestureManager _showAccessibilityHUDItem:];
-[UIAccessibilityHUDGestureManager _subscribedConcurrentGestureRecognizers];
```
