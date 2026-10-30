# `UIPDFViewTouchHandler`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIResponder`
- Protocols: `UIGestureRecognizerDelegate`
- 15 instance variables, 5 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"UIPDFPageView" _pdfPageView;
@"UITapGestureRecognizer" _doubleTapRecognizer;
@"UITapGestureRecognizer" _singleTapRecognizer;
@"UILongPressGestureRecognizer" _briefPressRecognizer;
@"UILongPressGestureRecognizer" _longPressRecognizer;
@"UITapGestureRecognizer" _twoFingerTapRecognizer;
@"UIMenuController" _menuController;
@"UIPDFSelectionController" _selectionController;
@"UIPDFMagnifierController" _magnifyController;
B _trackingSelection;
B _showMagnifier;
B _showLoupe;
B _firstTouch;
B _useDelegateForLinks;
B _allowMenu;
```

## Properties

```
@property (TB,V_allowMenu) allowMenu;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPDFViewTouchHandler releaseViewManager];
```

## Instance methods

```
-[UIPDFViewTouchHandler selectAll:];
-[UIPDFViewTouchHandler gestureRecognizer:shouldReceiveTouch:];
-[UIPDFViewTouchHandler initWithView:];
-[UIPDFViewTouchHandler dealloc];
-[UIPDFViewTouchHandler resignFirstResponder];
-[UIPDFViewTouchHandler gestureRecognizerShouldBegin:];
-[UIPDFViewTouchHandler copy:];
-[UIPDFViewTouchHandler gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIPDFViewTouchHandler nextResponder];
-[UIPDFViewTouchHandler canBecomeFirstResponder];
-[UIPDFViewTouchHandler canPerformAction:withSender:];
-[UIPDFViewTouchHandler allowMenu];
-[UIPDFViewTouchHandler briefPressRecognized:];
-[UIPDFViewTouchHandler delegateGesture:kind:];
-[UIPDFViewTouchHandler disableRecognizers];
-[UIPDFViewTouchHandler doubleTapRecognized:];
-[UIPDFViewTouchHandler enableRecognizers];
-[UIPDFViewTouchHandler hideMenu];
-[UIPDFViewTouchHandler longPressRecognized:];
-[UIPDFViewTouchHandler setAllowMenu:];
-[UIPDFViewTouchHandler setFirstTouch];
-[UIPDFViewTouchHandler showMenu];
-[UIPDFViewTouchHandler singleTapRecognized:];
-[UIPDFViewTouchHandler twoFingerTapRecognized:];
```
