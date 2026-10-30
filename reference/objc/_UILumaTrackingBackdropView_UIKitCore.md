# `_UILumaTrackingBackdropView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"<_UILumaTrackingBackdropViewDelegate>" _delegate;
@"<_UILumaTrackingBackdropViewGroupDelegate>" _groupDelegate;
Q _backgroundLuminanceLevel;
{?="minimum"d"maximum"d} _transitionBoundaries;
B _paused;
```

## Properties

```
@property (T@"<_UILumaTrackingBackdropViewDelegate>",R,W,N,V_delegate) delegate;
@property (T{?=dd},N,V_transitionBoundaries) transitionBoundaries;
@property (TQ,R,N) backgroundLuminanceLevel;
@property (TB,N,GisPaused,V_paused) paused;
```

## Class methods

```
+[_UILumaTrackingBackdropView layerClass];
```

## Instance methods

```
-[_UILumaTrackingBackdropView isPaused];
-[_UILumaTrackingBackdropView transitionBoundaries];
-[_UILumaTrackingBackdropView setTransitionBoundaries:];
-[_UILumaTrackingBackdropView unpauseAfterSeedingWithLumaLevel:];
-[_UILumaTrackingBackdropView _backdropLayer];
-[_UILumaTrackingBackdropView setPaused:];
-[_UILumaTrackingBackdropView delegate];
-[_UILumaTrackingBackdropView initWithTransitionBoundaries:delegate:frame:];
-[_UILumaTrackingBackdropView backdropLayer:didChangeLuma:];
-[_UILumaTrackingBackdropView backgroundLuminanceLevel];
```
