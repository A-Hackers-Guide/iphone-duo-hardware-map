# `SBDeviceApplicationCounterRotatableSceneOverlayView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughView`
- Protocols: `SBDeviceApplicationSceneOverlayView`
- 5 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"_UIDirectionalRotationView" _counterRotationView;
@"UIView" _contentView;
B _contentNeedsCounterRotation;
B _contentViewHasFixedSize;
@"<SBDeviceApplicationCounterRotatableSceneOverlayViewDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBDeviceApplicationCounterRotatableSceneOverlayViewDelegate>",R,W,N,V_delegate) delegate;
@property (T@"UIView",&,N,V_contentView) contentView;
@property (TB,N,V_contentNeedsCounterRotation) contentNeedsCounterRotation;
@property (TB,N,V_contentViewHasFixedSize) contentViewHasFixedSize;
```

## Instance methods

```
-[SBDeviceApplicationCounterRotatableSceneOverlayView setContentView:];
-[SBDeviceApplicationCounterRotatableSceneOverlayView containingSceneWillRotateFromInterfaceOrientation:toInterfaceOrientation:animationSettings:];
-[SBDeviceApplicationCounterRotatableSceneOverlayView layoutSubviews];
-[SBDeviceApplicationCounterRotatableSceneOverlayView contentView];
-[SBDeviceApplicationCounterRotatableSceneOverlayView delegate];
-[SBDeviceApplicationCounterRotatableSceneOverlayView setContentNeedsCounterRotation:];
-[SBDeviceApplicationCounterRotatableSceneOverlayView _createCounterRotationView];
-[SBDeviceApplicationCounterRotatableSceneOverlayView contentNeedsCounterRotation];
-[SBDeviceApplicationCounterRotatableSceneOverlayView contentViewHasFixedSize];
-[SBDeviceApplicationCounterRotatableSceneOverlayView initWithFrame:contentNeedsCounterRotation:delegate:];
-[SBDeviceApplicationCounterRotatableSceneOverlayView setContentViewHasFixedSize:];
```
