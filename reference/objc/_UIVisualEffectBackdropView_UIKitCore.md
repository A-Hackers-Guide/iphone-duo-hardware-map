# `_UIVisualEffectBackdropView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIVisualEffectSubview`
- 1 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"_UIVisualEffectViewBackdropCaptureGroup" _captureGroup;
```

## Properties

```
@property (Tq,N) renderMode;
@property (T@"_UIVisualEffectViewBackdropCaptureGroup",&,N) captureGroup;
@property (T@"CABackdropLayer",R,N) backdropLayer;
```

## Class methods

```
+[_UIVisualEffectBackdropView layerClass];
```

## Instance methods

```
-[_UIVisualEffectBackdropView backdropLayer];
-[_UIVisualEffectBackdropView applyIdentityFilterEffects];
-[_UIVisualEffectBackdropView willMoveToWindow:];
-[_UIVisualEffectBackdropView renderMode];
-[_UIVisualEffectBackdropView setCaptureGroup:];
-[_UIVisualEffectBackdropView isTransparentFocusItem];
-[_UIVisualEffectBackdropView _shouldAnimatePropertyWithKey:];
-[_UIVisualEffectBackdropView captureGroup];
-[_UIVisualEffectBackdropView applyRequestedFilterEffects];
-[_UIVisualEffectBackdropView setRenderMode:];
-[_UIVisualEffectBackdropView _applyScaleHintAsRequested:];
-[_UIVisualEffectBackdropView removeFromCurrentCaptureGroup];
```
