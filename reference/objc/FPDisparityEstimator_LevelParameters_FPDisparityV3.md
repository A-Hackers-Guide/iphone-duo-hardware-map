# `FPDisparityEstimator_LevelParameters`

- Image: [`/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`](../userland/System__Library__VideoProcessors__FPDisparityV3.bundle__FPDisparityV3.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"FPDisparityEstimator_RegularizationParameters" _regularizationParameters;
@"TVL1_v3_SolverParameters" _solverParameters;
@"HBFGPUParameters" _hbfParameters;
@"FPDisparityEstimator_CostLevelParameters" _costParameters;
```

## Properties

```
@property (T@"FPDisparityEstimator_RegularizationParameters",&,N,V_regularizationParameters) regularizationParameters;
@property (T@"TVL1_v3_SolverParameters",&,N,V_solverParameters) solverParameters;
@property (T@"HBFGPUParameters",&,N,V_hbfParameters) hbfParameters;
@property (T@"FPDisparityEstimator_CostLevelParameters",&,N,V_costParameters) costParameters;
```

## Instance methods

```
-[FPDisparityEstimator_LevelParameters costParameters];
-[FPDisparityEstimator_LevelParameters hbfParameters];
-[FPDisparityEstimator_LevelParameters regularizationParameters];
-[FPDisparityEstimator_LevelParameters setCostParameters:];
-[FPDisparityEstimator_LevelParameters setHbfParameters:];
-[FPDisparityEstimator_LevelParameters setRegularizationParameters:];
-[FPDisparityEstimator_LevelParameters setSolverParameters:];
-[FPDisparityEstimator_LevelParameters solverParameters];
```
