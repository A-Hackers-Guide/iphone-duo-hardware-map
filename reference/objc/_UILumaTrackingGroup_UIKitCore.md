# `_UILumaTrackingGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UILumaTrackingBackdropViewGroupDelegate`
- 9 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<_UILumaTrackingGroupDelegate>" _delegate;
Q _backgroundLuminanceLevel;
{?="minimum"d"maximum"d} _transitionBoundaries;
d _minimumDifference;
@"NSArray" _lumaViews;
@"NSMutableArray" _lumaValues;
@"NSMapTable" _outliers;
{?="scheduledUpdate"b1} _lumaTrackingGroupFlags;
B _paused;
```

## Properties

```
@property (T{?=dd},N,V_transitionBoundaries) transitionBoundaries;
@property (Td,N,V_minimumDifference) minimumDifference;
@property (TQ,R,N,V_backgroundLuminanceLevel) backgroundLuminanceLevel;
@property (TB,N,GisPaused,V_paused) paused;
```

## Instance methods

```
-[_UILumaTrackingGroup isPaused];
-[_UILumaTrackingGroup transitionBoundaries];
-[_UILumaTrackingGroup setTransitionBoundaries:];
-[_UILumaTrackingGroup unpauseAfterSeedingWithLumaLevel:];
-[_UILumaTrackingGroup setPaused:];
-[_UILumaTrackingGroup backgroundLuminanceLevel];
-[_UILumaTrackingGroup _updateLumaValue];
-[_UILumaTrackingGroup backgroundLumaView:didChangeLuma:];
-[_UILumaTrackingGroup initWithTransitionBoundaries:minimumDifference:delegate:views:];
-[_UILumaTrackingGroup minimumDifference];
-[_UILumaTrackingGroup setMinimumDifference:];
```
