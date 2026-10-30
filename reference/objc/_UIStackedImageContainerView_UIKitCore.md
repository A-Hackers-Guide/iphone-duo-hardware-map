# `_UIStackedImageContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 11 properties, 43 instance methods, 1 class methods

## Instance variables

```
@"UIMotionEffectGroup" _stackMotionEffects;
B _installsMotionEffectsWhenFocused;
@"UIImage" _stackImage;
@"NSObject<UINamedLayerStack>" _constructedStackImage;
@"_UIStackedImageConfiguration" _config;
```

## Properties

```
@property (T@"UIImage",&,N,V_stackImage) stackImage;
@property (T@"NSObject<UINamedLayerStack>",&,N,V_constructedStackImage) constructedStackImage;
@property (T@"UIView",&,N) imageOverlayView;
@property (T@"UIView",&,N) maskedOverlayView;
@property (T@"UIView",&,N) unmaskedOverlayView;
@property (T@"_UIStackedImageConfiguration",C,N,V_config) config;
@property (TB,N,GisPressed) pressed;
@property (TB,N,GisStackFocused) stackFocused;
@property (TQ,N) controlState;
@property (TB,N,V_installsMotionEffectsWhenFocused) installsMotionEffectsWhenFocused;
@property (T{CGPoint=dd},N) focusDirection;
```

## Class methods

```
+[_UIStackedImageContainerView layerClass];
```

## Instance methods

```
-[_UIStackedImageContainerView config];
-[_UIStackedImageContainerView setConfig:];
-[_UIStackedImageContainerView dealloc];
-[_UIStackedImageContainerView setBounds:];
-[_UIStackedImageContainerView isPressed];
-[_UIStackedImageContainerView setFrame:];
-[_UIStackedImageContainerView initWithFrame:];
-[_UIStackedImageContainerView setPressed:];
-[_UIStackedImageContainerView _updateFocusDirection:animated:];
-[_UIStackedImageContainerView _applyKeyPathsAndRelativeValues:forMotionEffect:];
-[_UIStackedImageContainerView _focusedFrameGuide];
-[_UIStackedImageContainerView _focusedFrameGuideCreateIfNecessary:];
-[_UIStackedImageContainerView _imageContainerLayer];
-[_UIStackedImageContainerView _installMotionEffects];
-[_UIStackedImageContainerView _preferredConfigurationForFocusAnimation:inContext:];
-[_UIStackedImageContainerView _renderer];
-[_UIStackedImageContainerView _setStackFocused:animated:focusAnimationCoordinator:];
-[_UIStackedImageContainerView _uninstallMotionEffects];
-[_UIStackedImageContainerView _updateContainerLayerImages];
-[_UIStackedImageContainerView _updateFocusedFrameGuideConstraintsIfApplicable];
-[_UIStackedImageContainerView _updateGlassMaterialsWithControlState:focusDirection:animated:focusAnimationCoordinator:];
-[_UIStackedImageContainerView _viewForBackgroundEffects];
-[_UIStackedImageContainerView constructedStackImage];
-[_UIStackedImageContainerView controlState];
-[_UIStackedImageContainerView focusDirection];
-[_UIStackedImageContainerView imageOverlayView];
-[_UIStackedImageContainerView installsMotionEffectsWhenFocused];
-[_UIStackedImageContainerView isStackFocused];
-[_UIStackedImageContainerView maskedOverlayView];
-[_UIStackedImageContainerView setConstructedStackImage:];
-[_UIStackedImageContainerView setControlState:];
-[_UIStackedImageContainerView setControlState:animated:];
-[_UIStackedImageContainerView setControlState:animated:focusAnimationCoordinator:];
-[_UIStackedImageContainerView setFocusDirection:];
-[_UIStackedImageContainerView setImageOverlayView:];
-[_UIStackedImageContainerView setInstallsMotionEffectsWhenFocused:];
-[_UIStackedImageContainerView setMaskedOverlayView:];
-[_UIStackedImageContainerView setStackFocused:];
-[_UIStackedImageContainerView setStackFocused:withFocusAnimationCoordinator:];
-[_UIStackedImageContainerView setStackImage:];
-[_UIStackedImageContainerView setUnmaskedOverlayView:];
-[_UIStackedImageContainerView stackImage];
-[_UIStackedImageContainerView unmaskedOverlayView];
```
