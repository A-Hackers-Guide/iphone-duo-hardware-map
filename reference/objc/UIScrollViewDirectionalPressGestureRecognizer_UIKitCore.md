# `UIScrollViewDirectionalPressGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRepeatingPressGestureRecognizer`
- 4 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _hasBeenModified;
@"UIView" _originalView;
@"UIScrollView" _scrollView;
q _activePressType;
```

## Properties

```
@property (T@"UIScrollView",W,N,V_scrollView) scrollView;
@property (Tq,R,N,V_activePressType) activePressType;
```

## Instance methods

```
-[UIScrollViewDirectionalPressGestureRecognizer _shouldReceivePress:];
-[UIScrollViewDirectionalPressGestureRecognizer setAllowedTouchTypes:];
-[UIScrollViewDirectionalPressGestureRecognizer setAllowedPressTypes:];
-[UIScrollViewDirectionalPressGestureRecognizer scrollView];
-[UIScrollViewDirectionalPressGestureRecognizer reset];
-[UIScrollViewDirectionalPressGestureRecognizer setScrollView:];
-[UIScrollViewDirectionalPressGestureRecognizer initWithTarget:action:];
-[UIScrollViewDirectionalPressGestureRecognizer setEnabled:];
-[UIScrollViewDirectionalPressGestureRecognizer activePressType];
-[UIScrollViewDirectionalPressGestureRecognizer _addToViewIfAllowed:];
-[UIScrollViewDirectionalPressGestureRecognizer _resetToOriginalViewIfAllowed];
-[UIScrollViewDirectionalPressGestureRecognizer _setEnabledIfAllowed:];
```
