# `UITextLoupeSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 18 instance methods, 3 class methods

## Instance variables

```
B _invalidated;
B _isHidingStatusBar;
@"UITextGestureTuning" _gestureTuning;
@"UIView" _interactionView;
@"UIWindow" _containerWindow;
@"UIView<_UITextLoupeView>" _loupeView;
@"<_UITextLoupeSessionDelegate>" _delegate;
```

## Properties

```
@property (T@"UIView",W,N,V_interactionView) interactionView;
@property (T@"UIWindow",W,N,V_containerWindow) containerWindow;
@property (T@"UIView<_UITextLoupeView>",&,N,V_loupeView) loupeView;
@property (T@"UITextGestureTuning",&,N,V_gestureTuning) gestureTuning;
@property (T@"<_UITextLoupeSessionDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[UITextLoupeSession _beginLoupeSessionAtPoint:fromSelectionWidgetView:inView:orientation:];
+[UITextLoupeSession _makeLoupeViewForSourceView:selectionWidget:orientation:];
+[UITextLoupeSession beginLoupeSessionAtPoint:fromSelectionWidgetView:inView:];
```

## Instance methods

```
-[UITextLoupeSession containerWindow];
-[UITextLoupeSession gestureTuning];
-[UITextLoupeSession setModelPosition:];
-[UITextLoupeSession dealloc];
-[UITextLoupeSession invalidate];
-[UITextLoupeSession setDelegate:];
-[UITextLoupeSession delegate];
-[UITextLoupeSession interactionView];
-[UITextLoupeSession _invalidateAnimated:];
-[UITextLoupeSession _locationInContainerCoordinateSpace:];
-[UITextLoupeSession _moveToPoint:withCaretRect:selectionWidget:trackingCaret:];
-[UITextLoupeSession _updateStatusBarVisibility];
-[UITextLoupeSession loupeView];
-[UITextLoupeSession moveToPoint:withCaretRect:trackingCaret:];
-[UITextLoupeSession setContainerWindow:];
-[UITextLoupeSession setGestureTuning:];
-[UITextLoupeSession setInteractionView:];
-[UITextLoupeSession setLoupeView:];
```
