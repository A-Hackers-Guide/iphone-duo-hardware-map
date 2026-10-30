# `BWNoiseReductionAndFusionProcessorInput` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 14 properties, 23 instance methods, 1 class methods

## Properties

```
@property (T@"BWStillImageSettings",R,N) stillImageSettings;
@property (T@"FigCaptureStillImageSettings",R,N) settings;
@property (T@"BWStillImageCaptureSettings",R,N) captureSettings;
@property (T@"BWStillImageCaptureStreamSettings",R,N) captureStreamSettings;
@property (TB,R,N) isMaster;
@property (T@"NSString",R,N) portType;
@property (Ti,R,N) receivedFrames;
@property (TB,R,N) receivedAllFrames;
@property (T^{opaqueCMSampleBuffer=},R,N) referenceFrame;
@property (T^{opaqueCMSampleBuffer=},R,N) evMinusReferenceFrame;
@property (T^{opaqueCMSampleBuffer=},R,N) errorRecoveryFrame;
@property (Ti,N) fusionMode;
@property (TB,N) emitErrorRecoveryFrame;
@property (TI,N) remainingProcessingCount;
```

## Class methods

```
+[BWNoiseReductionAndFusionProcessorInput new];
```

## Instance methods

```
-[BWNoiseReductionAndFusionProcessorInput fusionMode];
-[BWNoiseReductionAndFusionProcessorInput evMinusReferenceFrame];
-[BWNoiseReductionAndFusionProcessorInput stillImageSettings];
-[BWNoiseReductionAndFusionProcessorInput portType];
-[BWNoiseReductionAndFusionProcessorInput setRemainingProcessingCount:];
-[BWNoiseReductionAndFusionProcessorInput init];
-[BWNoiseReductionAndFusionProcessorInput settings];
-[BWNoiseReductionAndFusionProcessorInput referenceFrame];
-[BWNoiseReductionAndFusionProcessorInput receivedAllFrames];
-[BWNoiseReductionAndFusionProcessorInput setFusionMode:];
-[BWNoiseReductionAndFusionProcessorInput captureStreamSettings];
-[BWNoiseReductionAndFusionProcessorInput stopAdaptiveBracketingWithGroup:];
-[BWNoiseReductionAndFusionProcessorInput remainingProcessingCount];
-[BWNoiseReductionAndFusionProcessorInput receivedFrames];
-[BWNoiseReductionAndFusionProcessorInput addFrame:];
-[BWNoiseReductionAndFusionProcessorInput errorRecoveryFrame];
-[BWNoiseReductionAndFusionProcessorInput captureSettings];
-[BWNoiseReductionAndFusionProcessorInput isMaster];
-[BWNoiseReductionAndFusionProcessorInput addBypassedProcessorType:forBufferTypes:];
-[BWNoiseReductionAndFusionProcessorInput addOutputSampleBufferRouter:forBufferTypes:];
-[BWNoiseReductionAndFusionProcessorInput emitErrorRecoveryFrame];
-[BWNoiseReductionAndFusionProcessorInput outputSampleBufferRouterForBufferType:];
-[BWNoiseReductionAndFusionProcessorInput setEmitErrorRecoveryFrame:];
```
