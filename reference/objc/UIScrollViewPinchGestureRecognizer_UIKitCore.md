# `UIScrollViewPinchGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPinchGestureRecognizer`
- Protocols: `_UITransformEventRespondable`
- 4 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
: _scrollViewAction;
b1 _hasParentScrollView;
B _nestedHysteresisEnabled;
```

## Properties

```
@property (T@"UIScrollView",W,N,V_scrollView) scrollView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIScrollViewPinchGestureRecognizer _transformChangedWithEvent:];
-[UIScrollViewPinchGestureRecognizer scrollView];
-[UIScrollViewPinchGestureRecognizer _isGestureType:];
-[UIScrollViewPinchGestureRecognizer setScrollView:];
-[UIScrollViewPinchGestureRecognizer touchesBegan:withEvent:];
-[UIScrollViewPinchGestureRecognizer touchesMoved:withEvent:];
-[UIScrollViewPinchGestureRecognizer initWithTarget:action:];
-[UIScrollViewPinchGestureRecognizer setDelegate:];
-[UIScrollViewPinchGestureRecognizer removeTarget:action:];
```
