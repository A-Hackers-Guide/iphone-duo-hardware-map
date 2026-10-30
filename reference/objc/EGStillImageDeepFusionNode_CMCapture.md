# `EGStillImageDeepFusionNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGStillImageProcessorControllerDelegateNode`
- Protocols: `BWDeepFusionProcessorControllerDelegate`
- 14 instance variables, 13 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"EGInput" _processorInput;
@"NSArray" _sbufInputs;
@"EGInput" _inferencesDeliveredInput;
@"EGInput" _referenceFrameInput;
@"EGStillImageOutput" _sbufOutput;
@"EGStillImageOutput" _quadraForEnhancedResolutionInferenceInputImageOutput;
@"EGStillImageOutput" _inferenceInputImageOutput;
@"EGStillImageOutput" _sbufForEarlyEmissionOutput;
@"BWStillImageSettings" _stillImageSettings;
@"BWPhotonicEngineNodeConfiguration" _nodeConfiguration;
@"BWPhotonicEngineNodeResourceCoordinator" _resourceCoordinator;
@"NSString" _portType;
B _deepZoomEnabled;
@"BWDeepFusionProcessorInput" _deepFusionProcessorInput;
```

## Properties

```
@property (T@"EGInput",R,N,V_processorInput) processorInput;
@property (T@"NSArray",R,N,V_sbufInputs) sbufInputs;
@property (T@"EGInput",R,N,V_inferencesDeliveredInput) inferencesDeliveredInput;
@property (T@"EGInput",R,N,V_referenceFrameInput) referenceFrameInput;
@property (T@"EGOutput",R,N,V_sbufOutput) sbufOutput;
@property (T@"EGOutput",R,N,V_quadraForEnhancedResolutionInferenceInputImageOutput) quadraForEnhancedResolutionInferenceInputImageOutput;
@property (T@"EGOutput",R,N,V_inferenceInputImageOutput) inferenceInputImageOutput;
@property (T@"EGOutput",R,N,V_sbufForEarlyEmissionOutput) sbufForEarlyEmissionOutput;
@property (TB,N,V_deepZoomEnabled) deepZoomEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EGStillImageDeepFusionNode initialize];
```

## Instance methods

```
-[EGStillImageDeepFusionNode processorController:didFinishProcessingInput:err:];
-[EGStillImageDeepFusionNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[EGStillImageDeepFusionNode dealloc];
-[EGStillImageDeepFusionNode processorController:willAddBuffer:metadata:bufferType:processorInput:];
-[EGStillImageDeepFusionNode processorController:didSelectFusionMode:processorInput:];
-[EGStillImageDeepFusionNode deepZoomEnabled];
-[EGStillImageDeepFusionNode inferenceInputImageOutput];
-[EGStillImageDeepFusionNode inferencesDeliveredInput];
-[EGStillImageDeepFusionNode initWithName:stillImageSettings:nodeConfiguration:resourceCoordinator:numSbufInputs:processSmartStyleRenderingInput:processQuadraForEnhancedResolution:processInferenceInputImage:portType:delegate:];
-[EGStillImageDeepFusionNode processorInput];
-[EGStillImageDeepFusionNode quadraForEnhancedResolutionInferenceInputImageOutput];
-[EGStillImageDeepFusionNode queueManagedReceiveData:fromInput:];
-[EGStillImageDeepFusionNode referenceFrameInput];
-[EGStillImageDeepFusionNode sbufForEarlyEmissionOutput];
-[EGStillImageDeepFusionNode sbufInputs];
-[EGStillImageDeepFusionNode sbufOutput];
-[EGStillImageDeepFusionNode setDeepZoomEnabled:];
```
