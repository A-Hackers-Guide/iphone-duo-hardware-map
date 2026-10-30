# `BWDeepFusionProcessorInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 12 instance variables, 10 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"<BWDeepFusionProcessorInputDelegate>" _delegate;
@"NSDictionary" _evZeroReferenceFrameAttachments;
{?="value"q"timescale"i"flags"I"epoch"q} _evZeroReferenceFramePTS;
@"NSMutableArray" _inputBuffers;
B _allInferencesDelivered;
@"NSArray" _providedInferenceAttachedMedia;
@"NSDictionary" _inferenceAttachedMediaMetadata;
B _processInferenceInputImage;
B _processQuadraForEnhancedResolutionInferenceInputImage;
B _onlyApplyingSemanticStyle;
B _processSmartStyleRenderingInput;
i _fusionMode;
```

## Properties

```
@property (T@"NSArray",R,N,V_inputBuffers) inputBuffers;
@property (T@"<BWDeepFusionProcessorInputDelegate>",&,N,V_delegate) delegate;
@property (Ti,N,V_fusionMode) fusionMode;
@property (T@"NSDictionary",C,N,V_evZeroReferenceFrameAttachments) evZeroReferenceFrameAttachments;
@property (T{?=qiIq},N,V_evZeroReferenceFramePTS) evZeroReferenceFramePTS;
@property (T@"NSArray",&,N,V_providedInferenceAttachedMedia) providedInferenceAttachedMedia;
@property (TB,R,N,V_processInferenceInputImage) processInferenceInputImage;
@property (TB,R,N,V_processQuadraForEnhancedResolutionInferenceInputImage) processQuadraForEnhancedResolutionInferenceInputImage;
@property (TB,R,N,V_onlyApplyingSemanticStyle) onlyApplyingSemanticStyle;
@property (TB,R,N,V_processSmartStyleRenderingInput) processSmartStyleRenderingInput;
```

## Class methods

```
+[BWDeepFusionProcessorInput inputForOnlyApplyingSemanticStyleWithSettings:portType:];
```

## Instance methods

```
-[BWDeepFusionProcessorInput fusionMode];
-[BWDeepFusionProcessorInput dealloc];
-[BWDeepFusionProcessorInput setDelegate:];
-[BWDeepFusionProcessorInput setFusionMode:];
-[BWDeepFusionProcessorInput delegate];
-[BWDeepFusionProcessorInput description];
-[BWDeepFusionProcessorInput processSmartStyleRenderingInput];
-[BWDeepFusionProcessorInput evZeroReferenceFrameAttachments];
-[BWDeepFusionProcessorInput addBuffer:metadata:bufferType:captureFrameFlags:];
-[BWDeepFusionProcessorInput addBuffer:metadata:bufferType:captureFrameFlags:lscGainMap:lscGainMapParameters:];
-[BWDeepFusionProcessorInput allInferencesDelivered];
-[BWDeepFusionProcessorInput beginProcessingCachedBuffersIfWaiting];
-[BWDeepFusionProcessorInput evZeroReferenceFramePTS];
-[BWDeepFusionProcessorInput initWithSettings:portType:processInferenceInputImage:processQuadraForEnhancedResolutionInferenceInputImage:processSmartStyleRenderingInput:];
-[BWDeepFusionProcessorInput inputBuffers];
-[BWDeepFusionProcessorInput onlyApplyingSemanticStyle];
-[BWDeepFusionProcessorInput processInferenceInputImage];
-[BWDeepFusionProcessorInput processQuadraForEnhancedResolutionInferenceInputImage];
-[BWDeepFusionProcessorInput providedInferenceAttachedMedia];
-[BWDeepFusionProcessorInput releaseInputPixelBuffers];
-[BWDeepFusionProcessorInput setEvZeroReferenceFrameAttachments:];
-[BWDeepFusionProcessorInput setEvZeroReferenceFramePTS:];
-[BWDeepFusionProcessorInput setProvidedInferenceAttachedMedia:];
```
