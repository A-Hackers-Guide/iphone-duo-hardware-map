# `FPDisparityEstimator_CostLevelParameters`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
f _step;
f _stepLowlight;
f _lambda;
f _lambda_foreground;
f _lambda_background;
```

## Properties

```
@property (Tf,N,V_step) step;
@property (Tf,N,V_stepLowlight) stepLowlight;
@property (Tf,N,V_lambda) lambda;
@property (Tf,N,V_lambda_foreground) lambda_foreground;
@property (Tf,N,V_lambda_background) lambda_background;
```

## Instance methods

```
-[FPDisparityEstimator_CostLevelParameters step];
-[FPDisparityEstimator_CostLevelParameters setStep:];
-[FPDisparityEstimator_CostLevelParameters lambda];
-[FPDisparityEstimator_CostLevelParameters setLambda:];
-[FPDisparityEstimator_CostLevelParameters lambda_background];
-[FPDisparityEstimator_CostLevelParameters lambda_foreground];
-[FPDisparityEstimator_CostLevelParameters setLambda_background:];
-[FPDisparityEstimator_CostLevelParameters setLambda_foreground:];
-[FPDisparityEstimator_CostLevelParameters setStepLowlight:];
-[FPDisparityEstimator_CostLevelParameters stepLowlight];
```
