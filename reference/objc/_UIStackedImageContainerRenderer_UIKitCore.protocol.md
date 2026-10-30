# `_UIStackedImageContainerRenderer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T@"<UINamedLayerStack>",&,N) layerStack;
@property (T@"_UIStackedImageConfiguration",&,N) configuration;
@property (T@"UIView",&,N) maskedOverlayView;
@property (T@"UIView",&,N) unmaskedOverlayView;
@property (TQ,N) rendererControlState;
@property (T{CGPoint=dd},N) focusDirection;
```

## Instance methods

```
-[_UIStackedImageContainerRenderer setConfiguration:];
-[_UIStackedImageContainerRenderer configuration];
-[_UIStackedImageContainerRenderer focusDirection];
-[_UIStackedImageContainerRenderer layerStack];
-[_UIStackedImageContainerRenderer maskedOverlayView];
-[_UIStackedImageContainerRenderer rendererControlState];
-[_UIStackedImageContainerRenderer setFocusDirection:];
-[_UIStackedImageContainerRenderer setFocusDirection:animated:];
-[_UIStackedImageContainerRenderer setLayerStack:];
-[_UIStackedImageContainerRenderer setMaskedOverlayView:];
-[_UIStackedImageContainerRenderer setRendererControlState:];
-[_UIStackedImageContainerRenderer setRendererControlState:animated:focusAnimationCoordinator:];
-[_UIStackedImageContainerRenderer setUnmaskedOverlayView:];
-[_UIStackedImageContainerRenderer unmaskedOverlayView];
-[_UIStackedImageContainerRenderer viewForBackgroundEffects];
```
