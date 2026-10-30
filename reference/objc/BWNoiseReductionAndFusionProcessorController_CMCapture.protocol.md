# `BWNoiseReductionAndFusionProcessorController` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 8 instance methods, 1 class methods

## Properties

```
@property (Ti,R,N) progressiveLowLightFusionBatchSize;
```

## Class methods

```
+[BWNoiseReductionAndFusionProcessorController new];
```

## Instance methods

```
-[BWNoiseReductionAndFusionProcessorController init];
-[BWNoiseReductionAndFusionProcessorController progressiveLowLightFusionBatchSize];
-[BWNoiseReductionAndFusionProcessorController finishProcessingCurrentInputNow];
-[BWNoiseReductionAndFusionProcessorController initWithConfiguration:];
-[BWNoiseReductionAndFusionProcessorController adaptiveBracketingParametersForDigitalFlashMode:frameStatistics:stationary:sphereOffsetEnabled:detectedObjects:];
-[BWNoiseReductionAndFusionProcessorController cancelProcessing];
-[BWNoiseReductionAndFusionProcessorController adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderForPortType:];
-[BWNoiseReductionAndFusionProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processOriginalImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:inferencesAvailable:];
```
