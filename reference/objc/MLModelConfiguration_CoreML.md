# `MLModelConfiguration`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 29 instance variables, 32 properties, 79 instance methods, 2 class methods

## Instance variables

```
q _experimentalMLE5EngineUsage;
B _usePrecompiledE5Bundle;
q _experimentalMLE5BNNSGraphBackendUsage;
q _experimentalMLE5BNNSGraphBackendUsageMultiSegment;
@"NSDictionary" _e5rtDynamicCallableFunctions;
@"NSDictionary" _e5rtMutableMILWeightURLs;
Q _e5rtComputeDeviceTypeMask;
@"NSString" _e5rtCustomANECompilerOptions;
B _serializesMILTextForDebugging;
B _specializationUsesMPSGraphExecutable;
q _experimentalMLProgramEncryptedCacheUsage;
B _allowBackgroundGPUComputeSetting;
B _trainWithMLCompute;
B _useWatchSPIForScribble;
B _allowLowPrecisionAccumulationOnGPU;
B _enableTestVectorMode;
B _usePreloadedKey;
B _allowsInstrumentation;
B _preparesLazily;
@"NSString" _modelDisplayName;
q _computeUnits;
@"MLOptimizationHints" _optimizationHints;
@"NSString" _functionName;
q _predictionConcurrencyHint;
@"<MTLDevice>" _preferredMetalDevice;
@"NSDictionary" _parameters;
@"NSURL" _rootModelURL;
q _profilingOptions;
@"NSString" _parentModelName;
```

## Properties

```
@property (Tq,N) experimentalMLE5EngineUsage;
@property (TB,N) usePrecompiledE5Bundle;
@property (Tq,N) experimentalMLE5BNNSGraphBackendUsage;
@property (Tq,N) experimentalMLE5BNNSGraphBackendUsageMultiSegment;
@property (T@"NSDictionary",C,N) e5rtDynamicCallableFunctions;
@property (T@"NSDictionary",C,N) e5rtMutableMILWeightURLs;
@property (TQ,N) e5rtComputeDeviceTypeMask;
@property (T@"NSString",C,N) e5rtCustomANECompilerOptions;
@property (TB,N) serializesMILTextForDebugging;
@property (TB,N) specializationUsesMPSGraphExecutable;
@property (Tq,N) experimentalMLProgramEncryptedCacheUsage;
@property (TB,V_allowBackgroundGPUComputeSetting) allowBackgroundGPUComputeSetting;
@property (T@"NSString",C,N,V_functionName) functionName;
@property (Tq,N,V_predictionConcurrencyHint) predictionConcurrencyHint;
@property (TB,V_trainWithMLCompute) trainWithMLCompute;
@property (TB,N,V_useWatchSPIForScribble) useWatchSPIForScribble;
@property (TB,N) allowFloat16AccumulationOnGPU;
@property (TB,V_allowLowPrecisionAccumulationOnGPU) allowLowPrecisionAccumulationOnGPU;
@property (TB,N) allowBackgroundGPUCompute;
@property (T@"<MTLDevice>",&,N) preferredMTLDevice;
@property (T@"<MTLDevice>",&,N,V_preferredMetalDevice) preferredMetalDevice;
@property (TB,N,V_enableTestVectorMode) enableTestVectorMode;
@property (T@"NSDictionary",&,V_parameters) parameters;
@property (T@"NSURL",&,V_rootModelURL) rootModelURL;
@property (Tq,N,V_profilingOptions) profilingOptions;
@property (TB,N,V_usePreloadedKey) usePreloadedKey;
@property (T@"NSString",&,N,V_parentModelName) parentModelName;
@property (TB,N,V_allowsInstrumentation) allowsInstrumentation;
@property (TB,N,V_preparesLazily) preparesLazily;
@property (T@"NSString",C,V_modelDisplayName) modelDisplayName;
@property (Tq,V_computeUnits) computeUnits;
@property (T@"MLOptimizationHints",C,N,V_optimizationHints) optimizationHints;
```

## Class methods

```
+[MLModelConfiguration supportsSecureCoding];
+[MLModelConfiguration defaultConfiguration];
```

## Instance methods

```
-[MLModelConfiguration preferredMetalDevice];
-[MLModelConfiguration setExperimentalMLE5BNNSGraphBackendUsageMultiSegment:];
-[MLModelConfiguration preparesLazily];
-[MLModelConfiguration setAllowsInstrumentation:];
-[MLModelConfiguration setEnableTestVectorMode:];
-[MLModelConfiguration computeUnits];
-[MLModelConfiguration setFunctionName:];
-[MLModelConfiguration functionName];
-[MLModelConfiguration parameters];
-[MLModelConfiguration setExperimentalMLProgramEncryptedCacheUsage:];
-[MLModelConfiguration setTrainWithMLCompute:];
-[MLModelConfiguration initWithComputeUnits:];
-[MLModelConfiguration rootModelURL];
-[MLModelConfiguration setUsePrecompiledE5Bundle:];
-[MLModelConfiguration setComputeUnits:];
-[MLModelConfiguration setSpecializationUsesMPSGraphExecutable:];
-[MLModelConfiguration allowsInstrumentation];
-[MLModelConfiguration e5rtMutableMILWeightURLs];
-[MLModelConfiguration setParameters:];
-[MLModelConfiguration init];
-[MLModelConfiguration setExperimentalMLE5BNNSGraphBackendUsage:];
-[MLModelConfiguration e5rtDynamicCallableFunctions];
-[MLModelConfiguration setModelDisplayName:];
-[MLModelConfiguration parentModelName];
-[MLModelConfiguration experimentalMLProgramEncryptedCacheUsage];
-[MLModelConfiguration setAllowBackgroundGPUComputeSetting:];
-[MLModelConfiguration setProfilingOptions:];
-[MLModelConfiguration setAllowBackgroundGPUCompute:];
-[MLModelConfiguration setPreparesLazily:];
-[MLModelConfiguration setE5rtCustomANECompilerOptions:];
-[MLModelConfiguration setPredictionConcurrencyHint:];
-[MLModelConfiguration e5rtCustomANECompilerOptions];
-[MLModelConfiguration setAllowLowPrecisionAccumulationOnGPU:];
-[MLModelConfiguration setAllowFloat16AccumulationOnGPU:];
-[MLModelConfiguration setExperimentalMLE5EngineUsage:];
-[MLModelConfiguration setSerializesMILTextForDebugging:];
-[MLModelConfiguration neuralEngineCompilerOptions];
-[MLModelConfiguration e5rtComputeDeviceTypeMask];
-[MLModelConfiguration allowFloat16AccumulationOnGPU];
-[MLModelConfiguration experimentalMLProgramEncryptedCacheUsageToString:];
-[MLModelConfiguration setUsePreloadedKey:];
-[MLModelConfiguration setRootModelURL:];
-[MLModelConfiguration experimentalMLE5BNNSGraphBackendUsage];
-[MLModelConfiguration optimizationHints];
-[MLModelConfiguration specializationUsesMPSGraphExecutable];
-[MLModelConfiguration allowBackgroundGPUCompute];
-[MLModelConfiguration trainWithMLCompute];
-[MLModelConfiguration encodeWithCoder:];
-[MLModelConfiguration experimentalMLE5EngineUsage];
-[MLModelConfiguration setE5rtComputeDeviceTypeMask:];
-[MLModelConfiguration experimentalMLE5EngineUsageToString:];
-[MLModelConfiguration hash];
-[MLModelConfiguration useWatchSPIForScribble];
-[MLModelConfiguration setE5rtMutableMILWeightURLs:];
-[MLModelConfiguration description];
-[MLModelConfiguration predictionConcurrencyHint];
-[MLModelConfiguration setUseWatchSPIForScribble:];
-[MLModelConfiguration initWithCoder:];
-[MLModelConfiguration setPreferredMetalDevice:];
-[MLModelConfiguration experimentalMLE5BNNSGraphBackendUsageMultiSegment];
-[MLModelConfiguration usesCompileTimeMPSGraphTypeInferenceForModelVersion:];
-[MLModelConfiguration profilingOptions];
-[MLModelConfiguration usePrecompiledE5Bundle];
-[MLModelConfiguration setOptimizationHints:];
-[MLModelConfiguration allowBackgroundGPUComputeSetting];
-[MLModelConfiguration copyWithZone:];
-[MLModelConfiguration bnnsGraphBackendUsageToString:];
-[MLModelConfiguration setPreferredMTLDevice:];
-[MLModelConfiguration serializesMILTextForDebugging];
-[MLModelConfiguration isEqual:];
-[MLModelConfiguration setParentModelName:];
-[MLModelConfiguration isEqualToModelConfiguration:];
-[MLModelConfiguration enableTestVectorMode];
-[MLModelConfiguration computeUnitsToString:];
-[MLModelConfiguration modelDisplayName];
-[MLModelConfiguration allowLowPrecisionAccumulationOnGPU];
-[MLModelConfiguration setE5rtDynamicCallableFunctions:];
-[MLModelConfiguration preferredMTLDevice];
-[MLModelConfiguration usePreloadedKey];
```
