# `MLPredictionOptions`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 15 instance variables, 17 properties, 39 instance methods, 2 class methods

## Instance variables

```
B _usesCPUOnly;
B _enablePixelBufferDirectBinding;
I _aneQoS;
@"NSDictionary" _outputBackings;
Q _parentSignpostID;
Q _classifyTopK;
@"NSDictionary" _automaticOutputBackingMode;
@"MLInferenceFrameDataSerialization" _inferenceFrameDataSerialization;
Q _maxComputationBatchSize;
@"NSString" _e5rtStreamReuseExpectation;
@"NSDictionary" _inputDirectBindingExpectations;
@"NSDictionary" _outputDirectBindingExpectations;
@"NSArray" _waitSyncPoints;
@"MLPredictionSyncPoint" _completionSyncPoint;
@"NSString" _aneExecutionPriority;
```

## Properties

```
@property (TQ,N,V_parentSignpostID) parentSignpostID;
@property (TB,R,N) hasDirectBindingExpectations;
@property (TQ,V_classifyTopK) classifyTopK;
@property (TB,R,N) predictionUsesCPU;
@property (T@"NSDictionary",C,N,V_automaticOutputBackingMode) automaticOutputBackingMode;
@property (T@"MLInferenceFrameDataSerialization",C,N,V_inferenceFrameDataSerialization) inferenceFrameDataSerialization;
@property (TQ,V_maxComputationBatchSize) maxComputationBatchSize;
@property (T@"NSString",&,N,V_e5rtStreamReuseExpectation) e5rtStreamReuseExpectation;
@property (TB,N,V_enablePixelBufferDirectBinding) enablePixelBufferDirectBinding;
@property (T@"NSDictionary",C,N,V_inputDirectBindingExpectations) inputDirectBindingExpectations;
@property (T@"NSDictionary",C,N,V_outputDirectBindingExpectations) outputDirectBindingExpectations;
@property (T@"NSArray",C,N,V_waitSyncPoints) waitSyncPoints;
@property (T@"MLPredictionSyncPoint",&,N,V_completionSyncPoint) completionSyncPoint;
@property (TI,N,V_aneQoS) aneQoS;
@property (T@"NSString",N,V_aneExecutionPriority) aneExecutionPriority;
@property (TB,N,V_usesCPUOnly) usesCPUOnly;
@property (T@"NSDictionary",C,N,V_outputBackings) outputBackings;
```

## Class methods

```
+[MLPredictionOptions supportsSecureCoding];
+[MLPredictionOptions defaultOptions];
```

## Instance methods

```
-[MLPredictionOptions parentSignpostID];
-[MLPredictionOptions setUsesCPUOnly:];
-[MLPredictionOptions enablePixelBufferDirectBinding];
-[MLPredictionOptions aneExecutionPriority];
-[MLPredictionOptions waitSyncPoints];
-[MLPredictionOptions classifyTopK];
-[MLPredictionOptions setAneExecutionPriority:];
-[MLPredictionOptions init];
-[MLPredictionOptions validateExpectationsWithDirectlyBoundInputs:outputs:error:];
-[MLPredictionOptions outputBackings];
-[MLPredictionOptions setCompletionSyncPoint:];
-[MLPredictionOptions usesCPUOnly];
-[MLPredictionOptions aneQoS];
-[MLPredictionOptions hasDirectBindingExpectations];
-[MLPredictionOptions setClassifyTopK:];
-[MLPredictionOptions setE5rtStreamReuseExpectation:];
-[MLPredictionOptions automaticOutputBackingMode];
-[MLPredictionOptions initWithUsesCPUOnly:];
-[MLPredictionOptions encodeWithCoder:];
-[MLPredictionOptions inferenceFrameDataSerialization];
-[MLPredictionOptions outputDirectBindingExpectations];
-[MLPredictionOptions setEnablePixelBufferDirectBinding:];
-[MLPredictionOptions e5rtStreamReuseExpectation];
-[MLPredictionOptions completionSyncPoint];
-[MLPredictionOptions setMaxComputationBatchSize:];
-[MLPredictionOptions initWithCoder:];
-[MLPredictionOptions _validateDirectBindingExpectations:directlyBoundFeatureNames:unexpectedDirectBindings:unexpectedCopyBindings:];
-[MLPredictionOptions inputDirectBindingExpectations];
-[MLPredictionOptions setAneQoS:];
-[MLPredictionOptions setParentSignpostID:];
-[MLPredictionOptions copyWithZone:];
-[MLPredictionOptions setOutputBackings:];
-[MLPredictionOptions setOutputDirectBindingExpectations:];
-[MLPredictionOptions maxComputationBatchSize];
-[MLPredictionOptions setWaitSyncPoints:];
-[MLPredictionOptions setInputDirectBindingExpectations:];
-[MLPredictionOptions predictionUsesCPU];
-[MLPredictionOptions setInferenceFrameDataSerialization:];
-[MLPredictionOptions setAutomaticOutputBackingMode:];
```
