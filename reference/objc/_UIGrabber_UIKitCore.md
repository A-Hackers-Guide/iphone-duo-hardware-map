# `_UIGrabber`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `_UILumaTrackingBackdropViewDelegate`
- 5 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
B __lumaTrackingEnabled;
B __blurEnabled;
@"UIVisualEffectView" __visualEffectView;
@"_UILumaTrackingBackdropView" __lumaTrackingBackdropView;
Q __backgroundLuminanceLevel;
```

## Properties

```
@property (T@"UIVisualEffectView",R,N,V__visualEffectView) _visualEffectView;
@property (T@"_UILumaTrackingBackdropView",R,N,V__lumaTrackingBackdropView) _lumaTrackingBackdropView;
@property (TQ,N,S_setBackgroundLuminanceLevel:,V__backgroundLuminanceLevel) _backgroundLuminanceLevel;
@property (TB,N,S_setLumaTrackingEnabled:,V__lumaTrackingEnabled) _lumaTrackingEnabled;
@property (TB,N,G_isBlurEnabled,S_setBlurEnabled:,V__blurEnabled) _blurEnabled;
```

## Instance methods

```
-[_UIGrabber _controlEventsForActionTriggered];
-[_UIGrabber backgroundLumaView:didTransitionToLevel:];
-[_UIGrabber pointerInteraction:styleForRegion:];
-[_UIGrabber _intrinsicSizeWithinSize:];
-[_UIGrabber layoutSubviews];
-[_UIGrabber hitTest:withEvent:];
-[_UIGrabber sizeThatFits:];
-[_UIGrabber pointerInteraction:regionForRequest:defaultRegion:];
-[_UIGrabber _setBlurEnabled:];
-[_UIGrabber initWithCoder:];
-[_UIGrabber initWithFrame:];
-[_UIGrabber _backgroundLuminanceLevel];
-[_UIGrabber _isBlurEnabled];
-[_UIGrabber _lumaTrackingBackdropView];
-[_UIGrabber _lumaTrackingEnabled];
-[_UIGrabber _setBackgroundLuminanceLevel:];
-[_UIGrabber _setLumaTrackingEnabled:];
-[_UIGrabber _visualEffectView];
```
