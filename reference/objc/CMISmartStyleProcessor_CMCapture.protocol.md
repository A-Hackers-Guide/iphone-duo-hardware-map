# `CMISmartStyleProcessor` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MetalImageBufferProcessor`
- 0 instance variables, 8 properties, 19 instance methods, 16 class methods

## Properties

```
@property (T@"NSString",C,N) instanceLabel;
@property (T@"<CMISmartStyleProcessorBaseConfiguration>",&,N) configuration;
@property (T@"<CMISmartStyleProcessorInputOutput>",&,N) inputOutput;
@property (TB,N) shouldFlushCVMTLTextureCacheAfterProcessing;
@property (T@"<CMISmartStyleProcessorUtilities>",R,N) utilities;
@property (T@"<MTLTexture>",R,N) outputIntegratedStyleCoefficientsTexture;
@property (TB,N) useLiveMetalAllocations;
@property (TB,N) useSemanticSRLByDefault;
```

## Class methods

```
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStills];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStills3x4];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStillsReversibility];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStillsReversibility3x4];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStreaming];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStreamingAccelerated];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStreamingAcceleratedSquareAspectRatio];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStreamingAcceleratedSquareAspectRatioWithFilterType:];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStreamingAcceleratedWithFilterType:];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStreamingSquareAspectRatio];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStreamingSquareAspectRatioWithFilterType:];
+[CMISmartStyleProcessor getDefaultProcessorConfigurationForStreamingWithFilterType:];
+[CMISmartStyleProcessor getRequiredFilteredCoefficientsPixelBufferPoolSizeForFilterType:];
+[CMISmartStyleProcessor getRequiredInputBufferSizeForFilterType:];
+[CMISmartStyleProcessor getRequiredMemorySizeForProcessingType:];
+[CMISmartStyleProcessor getSmartStyleCoefficientsFilterType:];
```

## Instance methods

```
-[CMISmartStyleProcessor initWithOptionalMetalCommandQueue:];
-[CMISmartStyleProcessor utilities];
-[CMISmartStyleProcessor setUseSemanticSRLByDefault:];
-[CMISmartStyleProcessor setShouldFlushCVMTLTextureCacheAfterProcessing:];
-[CMISmartStyleProcessor setConfiguration:];
-[CMISmartStyleProcessor useSemanticSRLByDefault];
-[CMISmartStyleProcessor instanceLabel];
-[CMISmartStyleProcessor useLiveMetalAllocations];
-[CMISmartStyleProcessor configuration];
-[CMISmartStyleProcessor setInstanceLabel:];
-[CMISmartStyleProcessor shouldFlushCVMTLTextureCacheAfterProcessing];
-[CMISmartStyleProcessor setUseLiveMetalAllocations:];
-[CMISmartStyleProcessor setInputOutput:];
-[CMISmartStyleProcessor initWithOptionalMetalCommandQueue:ispSMGProcessingSession:];
-[CMISmartStyleProcessor initWithOptionalMetalCommandQueue:ispSTENProcessingSession:];
-[CMISmartStyleProcessor inputOutput];
-[CMISmartStyleProcessor outputIntegratedStyleCoefficientsTexture];
-[CMISmartStyleProcessor copyStatsForOtherEffectsTo:];
-[CMISmartStyleProcessor waitForSchedule];
```
