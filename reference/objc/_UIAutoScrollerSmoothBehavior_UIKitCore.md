# `_UIAutoScrollerSmoothBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIAutoScrollBehavior`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"CAMediaTimingFunction" _speedTimingFunction;
{?="useStaticInsets"b1} _behaviorFlags;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _staticInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _dynamicAutoScrollInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _touchInsets;
```

## Properties

```
@property (T{UIEdgeInsets=dddd},N,V_touchInsets) touchInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIAutoScrollerSmoothBehavior autoScrollEnded:];
-[_UIAutoScrollerSmoothBehavior beginDelayForAutoScroller:];
-[_UIAutoScrollerSmoothBehavior offsetForAutoScroller:timeDelta:];
-[_UIAutoScrollerSmoothBehavior init];
-[_UIAutoScrollerSmoothBehavior setTouchInsets:];
-[_UIAutoScrollerSmoothBehavior _layoutAreaViewsWithCurrentNonScrollingArea:inScrollView:];
-[_UIAutoScrollerSmoothBehavior autoScrollStarted:];
-[_UIAutoScrollerSmoothBehavior _removeAreaViews];
-[_UIAutoScrollerSmoothBehavior touchInsets];
```
