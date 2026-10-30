# `FPDisparityEstimator_RegularizationParameters`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
f _alpha;
f _beta;
f _gain;
f _offset;
f _segmentation_bias_foreground;
f _segmentation_bias_background;
```

## Properties

```
@property (Tf,N,V_alpha) alpha;
@property (Tf,N,V_beta) beta;
@property (Tf,N,V_gain) gain;
@property (Tf,N,V_offset) offset;
@property (Tf,N,V_segmentation_bias_foreground) segmentation_bias_foreground;
@property (Tf,N,V_segmentation_bias_background) segmentation_bias_background;
```

## Instance methods

```
-[FPDisparityEstimator_RegularizationParameters gain];
-[FPDisparityEstimator_RegularizationParameters setAlpha:];
-[FPDisparityEstimator_RegularizationParameters alpha];
-[FPDisparityEstimator_RegularizationParameters setOffset:];
-[FPDisparityEstimator_RegularizationParameters setGain:];
-[FPDisparityEstimator_RegularizationParameters offset];
-[FPDisparityEstimator_RegularizationParameters setBeta:];
-[FPDisparityEstimator_RegularizationParameters beta];
-[FPDisparityEstimator_RegularizationParameters segmentation_bias_background];
-[FPDisparityEstimator_RegularizationParameters segmentation_bias_foreground];
-[FPDisparityEstimator_RegularizationParameters setSegmentation_bias_background:];
-[FPDisparityEstimator_RegularizationParameters setSegmentation_bias_foreground:];
```
