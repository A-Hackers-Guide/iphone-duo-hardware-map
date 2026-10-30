# `SBBlurItemContainerParameters`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _shouldRasterize;
d _blurRadius;
d _rasterizationScale;
q _inputQuality;
q _inputIntermediateBitDepth;
@"SBFFluidBehaviorSettings" _blurAnimationSettings;
```

## Properties

```
@property (Td,N,V_blurRadius) blurRadius;
@property (TB,R,N,V_shouldRasterize) shouldRasterize;
@property (Td,R,N,V_rasterizationScale) rasterizationScale;
@property (Tq,R,N,V_inputQuality) inputQuality;
@property (Tq,R,N,V_inputIntermediateBitDepth) inputIntermediateBitDepth;
@property (T@"SBFFluidBehaviorSettings",&,N,V_blurAnimationSettings) blurAnimationSettings;
```

## Class methods

```
+[SBBlurItemContainerParameters defaultCrossblurBlurParameters];
```

## Instance methods

```
-[SBBlurItemContainerParameters shouldRasterize];
-[SBBlurItemContainerParameters blurRadius];
-[SBBlurItemContainerParameters rasterizationScale];
-[SBBlurItemContainerParameters setBlurRadius:];
-[SBBlurItemContainerParameters blurAnimationSettings];
-[SBBlurItemContainerParameters initWithBlurRadius:shouldRasterize:rasterizationScale:inputQuality:inputIntermediateBitDepth:blurAnimationSettings:];
-[SBBlurItemContainerParameters inputIntermediateBitDepth];
-[SBBlurItemContainerParameters inputQuality];
-[SBBlurItemContainerParameters setBlurAnimationSettings:];
```
