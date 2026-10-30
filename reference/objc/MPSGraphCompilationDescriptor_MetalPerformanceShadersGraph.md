# `MPSGraphCompilationDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 44 instance variables, 44 properties, 105 instance methods, 1 class methods

## Instance variables

```
B _enableShapeShifterCache;
Q _shapeShifterCacheThreads;
B _disableShapeFolding;
Q _shapeShifterTILevel;
B _enableParallelEncode;
B _enableMemrefBufferization;
B _enableShapeShifter;
B _enableShapeShifterControlFlow;
B _waitForCompilationCompletion;
B _useANELLIR;
B _enableANEFWToFWSignal;
B _enableANELateLatch;
B _enableANECHWRankPromotion;
B _printANEPlacementAnalysis;
B _enableMLIRDiagnostics;
B _enableShapeEquivalence;
B _verifyTypeInference;
B _enableANECValidationWorkflow;
B _enableCompileResourcesForPackage;
B _useCallablesHash;
B _includeDebugInfo;
B _writeDebugInfo;
B _addUniqueIdToMLIRLocations;
Q _optimizationLevel;
@? _compilationCompletionHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
Q _optimizationProfile;
@"NSDictionary" _callables;
Q _reducedPrecisionFastMath;
Q _compilerOptions;
Q _aneCompilerSpatialSplitting;
Q _preferredDevice;
Q _allowedComputeDevices;
@"NSString" _entryFunctionName;
@"MPSGraphExecutableConstantData" _constantData;
Q _maximumNumberOfParallelEncodingRegions;
Q _minimumNumberOfOpsInParallelRegion;
Q _layoutConversionPassConfig;
q _minimumLayoutConversionCountToEnable;
@"NSDictionary" _inputShapeRanges;
Q _dumpModuleFlag;
@"NSString" _dumpModulePath;
Q _aneBondedCompileMode;
Q _aneMaxRegions;
```

## Properties

```
@property (TB,N) enableShapeShifterCache;
@property (TQ,N) shapeShifterCacheThreads;
@property (TB,N) disableShapeFolding;
@property (TQ,N) shapeShifterTILevel;
@property (TB,N) enableShapeShifterControlFlow;
@property (TB,N,V_useANELLIR) useANELLIR;
@property (TQ,V_compilerOptions) compilerOptions;
@property (TQ,V_aneCompilerSpatialSplitting) aneCompilerSpatialSplitting;
@property (TB,V_enableANEFWToFWSignal) enableANEFWToFWSignal;
@property (TB,V_enableANELateLatch) enableANELateLatch;
@property (TB,V_enableANECHWRankPromotion) enableANECHWRankPromotion;
@property (TB,V_printANEPlacementAnalysis) printANEPlacementAnalysis;
@property (TQ,N,V_preferredDevice) preferredDevice;
@property (TQ,N,V_allowedComputeDevices) allowedComputeDevices;
@property (T@"NSString",&,V_entryFunctionName) entryFunctionName;
@property (T@"MPSGraphExecutableConstantData",&,V_constantData) constantData;
@property (TB,N,V_enableParallelEncode) enableParallelEncode;
@property (TB,N,V_enableMemrefBufferization) enableMemrefBufferization;
@property (TQ,V_maximumNumberOfParallelEncodingRegions) maximumNumberOfParallelEncodingRegions;
@property (TQ,V_minimumNumberOfOpsInParallelRegion) minimumNumberOfOpsInParallelRegion;
@property (TB,N,V_enableMLIRDiagnostics) enableMLIRDiagnostics;
@property (TB,N,V_enableShapeEquivalence) enableShapeEquivalence;
@property (TB,N,V_enableShapeShifter) enableShapeShifter;
@property (TB,N,V_verifyTypeInference) verifyTypeInference;
@property (TB,N,V_enableANECValidationWorkflow) enableANECValidationWorkflow;
@property (TQ,N,V_layoutConversionPassConfig) layoutConversionPassConfig;
@property (Tq,N,V_minimumLayoutConversionCountToEnable) minimumLayoutConversionCountToEnable;
@property (TB,N,V_enableCompileResourcesForPackage) enableCompileResourcesForPackage;
@property (TB,V_useCallablesHash) useCallablesHash;
@property (T@"NSDictionary",C,V_inputShapeRanges) inputShapeRanges;
@property (TQ,N,V_dumpModuleFlag) dumpModuleFlag;
@property (T@"NSString",&,N,V_dumpModulePath) dumpModulePath;
@property (TQ,V_aneBondedCompileMode) aneBondedCompileMode;
@property (TQ,V_aneMaxRegions) aneMaxRegions;
@property (TB,N,V_includeDebugInfo) includeDebugInfo;
@property (TB,N,V_writeDebugInfo) writeDebugInfo;
@property (TB,N,V_addUniqueIdToMLIRLocations) addUniqueIdToMLIRLocations;
@property (TQ,N,V_optimizationLevel) optimizationLevel;
@property (TB,N,V_waitForCompilationCompletion) waitForCompilationCompletion;
@property (T@?,C,V_compilationCompletionHandler) compilationCompletionHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,V_dispatchQueue) dispatchQueue;
@property (TQ,N,V_optimizationProfile) optimizationProfile;
@property (T@"NSDictionary",&,V_callables) callables;
@property (TQ,V_reducedPrecisionFastMath) reducedPrecisionFastMath;
```

## Class methods

```
+[MPSGraphCompilationDescriptor descriptorWithDictionary:];
```

## Instance methods

```
-[MPSGraphCompilationDescriptor toDictionary];
-[MPSGraphCompilationDescriptor dispatchQueue];
-[MPSGraphCompilationDescriptor debugDescription];
-[MPSGraphCompilationDescriptor init];
-[MPSGraphCompilationDescriptor setDispatchQueue:];
-[MPSGraphCompilationDescriptor setOptimizationLevel:];
-[MPSGraphCompilationDescriptor optimizationLevel];
-[MPSGraphCompilationDescriptor isEqualTo:];
-[MPSGraphCompilationDescriptor hash];
-[MPSGraphCompilationDescriptor copyWithZone:];
-[MPSGraphCompilationDescriptor isEqual:];
-[MPSGraphCompilationDescriptor preferredDevice];
-[MPSGraphCompilationDescriptor compilerOptions];
-[MPSGraphCompilationDescriptor disableTypeInference];
-[MPSGraphCompilationDescriptor enableGPUQuantOps];
-[MPSGraphCompilationDescriptor setAllowedComputeDevices:];
-[MPSGraphCompilationDescriptor setCallables:];
-[MPSGraphCompilationDescriptor setCompilationCompletionHandler:];
-[MPSGraphCompilationDescriptor setCompilerOptions:];
-[MPSGraphCompilationDescriptor setEnableANECValidationWorkflow:];
-[MPSGraphCompilationDescriptor setEnableParallelEncode:];
-[MPSGraphCompilationDescriptor setEntryFunctionName:];
-[MPSGraphCompilationDescriptor setPreferredDevice:];
-[MPSGraphCompilationDescriptor setReducedPrecisionFastMath:];
-[MPSGraphCompilationDescriptor setWaitForCompilationCompletion:];
-[MPSGraphCompilationDescriptor setAneBondedCompileMode:];
-[MPSGraphCompilationDescriptor setEnableANEFWToFWSignal:];
-[MPSGraphCompilationDescriptor setEnableANELateLatch:];
-[MPSGraphCompilationDescriptor setOptimizationProfile:];
-[MPSGraphCompilationDescriptor includeDebugInfo];
-[MPSGraphCompilationDescriptor setIncludeDebugInfo:];
-[MPSGraphCompilationDescriptor setAneCompilerSpatialSplitting:];
-[MPSGraphCompilationDescriptor addUniqueIdToMLIRLocations];
-[MPSGraphCompilationDescriptor allowedComputeDevices];
-[MPSGraphCompilationDescriptor aneBondedCompileMode];
-[MPSGraphCompilationDescriptor aneCompilerSpatialSplitting];
-[MPSGraphCompilationDescriptor aneMaxRegions];
-[MPSGraphCompilationDescriptor callables];
-[MPSGraphCompilationDescriptor compilationCompletionHandler];
-[MPSGraphCompilationDescriptor constantData];
-[MPSGraphCompilationDescriptor convertLayoutToNHWC];
-[MPSGraphCompilationDescriptor disableAutoLayoutConversion];
-[MPSGraphCompilationDescriptor disableGPUQuantOps];
-[MPSGraphCompilationDescriptor disableShapeFolding];
-[MPSGraphCompilationDescriptor dumpModuleFlag];
-[MPSGraphCompilationDescriptor dumpModulePath];
-[MPSGraphCompilationDescriptor enableANECHWRankPromotion];
-[MPSGraphCompilationDescriptor enableANECValidationWorkflow];
-[MPSGraphCompilationDescriptor enableANEFWToFWSignal];
-[MPSGraphCompilationDescriptor enableANELateLatch];
-[MPSGraphCompilationDescriptor enableCompileResourcesForPackage];
-[MPSGraphCompilationDescriptor enableDevicePlacement];
-[MPSGraphCompilationDescriptor enableFileBackedConstants];
-[MPSGraphCompilationDescriptor enableLayoutConversion:dataChannelsLast:weightsChannelsLast:];
-[MPSGraphCompilationDescriptor enableMLIRDiagnostics];
-[MPSGraphCompilationDescriptor enableMemrefBufferization];
-[MPSGraphCompilationDescriptor enableParallelEncode];
-[MPSGraphCompilationDescriptor enableShapeEquivalence];
-[MPSGraphCompilationDescriptor enableShapeShifter];
-[MPSGraphCompilationDescriptor enableShapeShifterCache];
-[MPSGraphCompilationDescriptor enableShapeShifterControlFlow];
-[MPSGraphCompilationDescriptor entryFunctionName];
-[MPSGraphCompilationDescriptor getNamedAttrArray:deviceDescriptor:];
-[MPSGraphCompilationDescriptor inputShapeRanges];
-[MPSGraphCompilationDescriptor isEqualForModuleTo:];
-[MPSGraphCompilationDescriptor layoutConversionPassConfig];
-[MPSGraphCompilationDescriptor maximumNumberOfParallelEncodingRegions];
-[MPSGraphCompilationDescriptor minimumLayoutConversionCountToEnable];
-[MPSGraphCompilationDescriptor minimumNumberOfOpsInParallelRegion];
-[MPSGraphCompilationDescriptor optimizationProfile];
-[MPSGraphCompilationDescriptor printANEPlacementAnalysis];
-[MPSGraphCompilationDescriptor reducedPrecisionFastMath];
-[MPSGraphCompilationDescriptor setAddUniqueIdToMLIRLocations:];
-[MPSGraphCompilationDescriptor setAneMaxRegions:];
-[MPSGraphCompilationDescriptor setConstantData:];
-[MPSGraphCompilationDescriptor setDisableShapeFolding:];
-[MPSGraphCompilationDescriptor setDumpModuleFlag:];
-[MPSGraphCompilationDescriptor setDumpModulePath:];
-[MPSGraphCompilationDescriptor setEnableANECHWRankPromotion:];
-[MPSGraphCompilationDescriptor setEnableCompileResourcesForPackage:];
-[MPSGraphCompilationDescriptor setEnableMLIRDiagnostics:];
-[MPSGraphCompilationDescriptor setEnableMemrefBufferization:];
-[MPSGraphCompilationDescriptor setEnableShapeEquivalence:];
-[MPSGraphCompilationDescriptor setEnableShapeShifter:];
-[MPSGraphCompilationDescriptor setEnableShapeShifterCache:];
-[MPSGraphCompilationDescriptor setEnableShapeShifterControlFlow:];
-[MPSGraphCompilationDescriptor setInputShapeRanges:];
-[MPSGraphCompilationDescriptor setLayoutConversionPassConfig:];
-[MPSGraphCompilationDescriptor setMaximumNumberOfParallelEncodingRegions:];
-[MPSGraphCompilationDescriptor setMinimumLayoutConversionCountToEnable:];
-[MPSGraphCompilationDescriptor setMinimumNumberOfOpsInParallelRegion:];
-[MPSGraphCompilationDescriptor setPrintANEPlacementAnalysis:];
-[MPSGraphCompilationDescriptor setShapeShifterCacheThreads:];
-[MPSGraphCompilationDescriptor setShapeShifterTILevel:];
-[MPSGraphCompilationDescriptor setUseANELLIR:];
-[MPSGraphCompilationDescriptor setUseCallablesHash:];
-[MPSGraphCompilationDescriptor setVerifyTypeInference:];
-[MPSGraphCompilationDescriptor setWriteDebugInfo:];
-[MPSGraphCompilationDescriptor shapeShifterCacheThreads];
-[MPSGraphCompilationDescriptor shapeShifterTILevel];
-[MPSGraphCompilationDescriptor useANELLIR];
-[MPSGraphCompilationDescriptor useCallablesHash];
-[MPSGraphCompilationDescriptor verifyTypeInference];
-[MPSGraphCompilationDescriptor waitForCompilationCompletion];
-[MPSGraphCompilationDescriptor writeDebugInfo];
```
