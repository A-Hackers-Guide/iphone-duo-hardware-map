# `FPDisparityEstimator_CostParameters`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 20 properties, 41 instance methods, 0 class methods

## Instance variables

```
I _nView;
f _microlensSpatialOffset;
f _foregroundPush;
f _backgroundPush;
I _rigidWindowSupport;
f _costMapAntialiasingStrength;
f _costEpsilon;
f _lensFieldCurvatureA0;
f _lensFieldCurvatureA1;
f _lensFieldCurvatureA2;
f _lensFieldCurvatureA3;
f _lensFieldCurvatureA4;
f _circleOfConfusionGain;
f _circleOfConfusionOffset;
f _radialExponent;
f _radialGain;
f _radialMin;
f _AGCLow;
f _AGCHigh;
@"NSArray" _correctionCoefficientsWeights;
```

## Properties

```
@property (TI,N,V_nView) nView;
@property (Tf,N,V_microlensSpatialOffset) microlensSpatialOffset;
@property (Tf,N,V_foregroundPush) foregroundPush;
@property (Tf,N,V_backgroundPush) backgroundPush;
@property (TI,N,V_rigidWindowSupport) rigidWindowSupport;
@property (Tf,N,V_costMapAntialiasingStrength) costMapAntialiasingStrength;
@property (Tf,N,V_costEpsilon) costEpsilon;
@property (Tf,N,V_lensFieldCurvatureA0) lensFieldCurvatureA0;
@property (Tf,N,V_lensFieldCurvatureA1) lensFieldCurvatureA1;
@property (Tf,N,V_lensFieldCurvatureA2) lensFieldCurvatureA2;
@property (Tf,N,V_lensFieldCurvatureA3) lensFieldCurvatureA3;
@property (Tf,N,V_lensFieldCurvatureA4) lensFieldCurvatureA4;
@property (Tf,N,V_circleOfConfusionGain) circleOfConfusionGain;
@property (Tf,N,V_circleOfConfusionOffset) circleOfConfusionOffset;
@property (Tf,N,V_radialExponent) radialExponent;
@property (Tf,N,V_radialGain) radialGain;
@property (Tf,N,V_radialMin) radialMin;
@property (Tf,N,V_AGCLow) AGCLow;
@property (Tf,N,V_AGCHigh) AGCHigh;
@property (T@"NSArray",&,N,V_correctionCoefficientsWeights) correctionCoefficientsWeights;
```

## Instance methods

```
-[FPDisparityEstimator_CostParameters description];
-[FPDisparityEstimator_CostParameters AGCHigh];
-[FPDisparityEstimator_CostParameters AGCLow];
-[FPDisparityEstimator_CostParameters setCostEpsilon:];
-[FPDisparityEstimator_CostParameters setCostMapAntialiasingStrength:];
-[FPDisparityEstimator_CostParameters backgroundPush];
-[FPDisparityEstimator_CostParameters circleOfConfusionGain];
-[FPDisparityEstimator_CostParameters circleOfConfusionOffset];
-[FPDisparityEstimator_CostParameters correctionCoefficientsWeights];
-[FPDisparityEstimator_CostParameters costEpsilon];
-[FPDisparityEstimator_CostParameters costMapAntialiasingStrength];
-[FPDisparityEstimator_CostParameters foregroundPush];
-[FPDisparityEstimator_CostParameters lensFieldCurvatureA0];
-[FPDisparityEstimator_CostParameters lensFieldCurvatureA1];
-[FPDisparityEstimator_CostParameters lensFieldCurvatureA2];
-[FPDisparityEstimator_CostParameters lensFieldCurvatureA3];
-[FPDisparityEstimator_CostParameters lensFieldCurvatureA4];
-[FPDisparityEstimator_CostParameters microlensSpatialOffset];
-[FPDisparityEstimator_CostParameters nView];
-[FPDisparityEstimator_CostParameters radialExponent];
-[FPDisparityEstimator_CostParameters radialGain];
-[FPDisparityEstimator_CostParameters radialMin];
-[FPDisparityEstimator_CostParameters rigidWindowSupport];
-[FPDisparityEstimator_CostParameters setAGCHigh:];
-[FPDisparityEstimator_CostParameters setAGCLow:];
-[FPDisparityEstimator_CostParameters setBackgroundPush:];
-[FPDisparityEstimator_CostParameters setCircleOfConfusionGain:];
-[FPDisparityEstimator_CostParameters setCircleOfConfusionOffset:];
-[FPDisparityEstimator_CostParameters setCorrectionCoefficientsWeights:];
-[FPDisparityEstimator_CostParameters setForegroundPush:];
-[FPDisparityEstimator_CostParameters setLensFieldCurvatureA0:];
-[FPDisparityEstimator_CostParameters setLensFieldCurvatureA1:];
-[FPDisparityEstimator_CostParameters setLensFieldCurvatureA2:];
-[FPDisparityEstimator_CostParameters setLensFieldCurvatureA3:];
-[FPDisparityEstimator_CostParameters setLensFieldCurvatureA4:];
-[FPDisparityEstimator_CostParameters setMicrolensSpatialOffset:];
-[FPDisparityEstimator_CostParameters setNView:];
-[FPDisparityEstimator_CostParameters setRadialExponent:];
-[FPDisparityEstimator_CostParameters setRadialGain:];
-[FPDisparityEstimator_CostParameters setRadialMin:];
-[FPDisparityEstimator_CostParameters setRigidWindowSupport:];
```
