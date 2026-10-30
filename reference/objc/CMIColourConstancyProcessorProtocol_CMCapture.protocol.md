# `CMIColourConstancyProcessorProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MetalImageBufferProcessor`
- 0 instance variables, 9 properties, 19 instance methods, 0 class methods

## Properties

```
@property (T@"<CMIColourConstancyProcessorDelegate>",W,N) delegate;
@property (T^{__CVBuffer=},&,N) outputImagePixelBuffer;
@property (T^{__CVBuffer=},&,N) outputLinearRGBPixelBuffer;
@property (T@"NSMutableDictionary",&,N) outputImageMetadata;
@property (T@"NSMutableDictionary",&,N) confidenceMapMetadata;
@property (T^{__CVBuffer=},&,N) outputColourAccuracyConfidenceImagePixelBuffer;
@property (Tf,N) outputCenterWeightedMeanColourAccuracyConfidenceLevel;
@property (TB,N) clippingRecoveryEnabled;
@property (TB,N) saturationBoostEnabled;
```

## Instance methods

```
-[CMIColourConstancyProcessorProtocol setDelegate:];
-[CMIColourConstancyProcessorProtocol delegate];
-[CMIColourConstancyProcessorProtocol addFrame:metadata:frameType:frameParams:];
-[CMIColourConstancyProcessorProtocol clippingRecoveryEnabled];
-[CMIColourConstancyProcessorProtocol confidenceMapMetadata];
-[CMIColourConstancyProcessorProtocol outputCenterWeightedMeanColourAccuracyConfidenceLevel];
-[CMIColourConstancyProcessorProtocol outputColourAccuracyConfidenceImagePixelBuffer];
-[CMIColourConstancyProcessorProtocol outputImageMetadata];
-[CMIColourConstancyProcessorProtocol outputImagePixelBuffer];
-[CMIColourConstancyProcessorProtocol outputLinearRGBPixelBuffer];
-[CMIColourConstancyProcessorProtocol saturationBoostEnabled];
-[CMIColourConstancyProcessorProtocol setClippingRecoveryEnabled:];
-[CMIColourConstancyProcessorProtocol setConfidenceMapMetadata:];
-[CMIColourConstancyProcessorProtocol setOutputCenterWeightedMeanColourAccuracyConfidenceLevel:];
-[CMIColourConstancyProcessorProtocol setOutputColourAccuracyConfidenceImagePixelBuffer:];
-[CMIColourConstancyProcessorProtocol setOutputImageMetadata:];
-[CMIColourConstancyProcessorProtocol setOutputImagePixelBuffer:];
-[CMIColourConstancyProcessorProtocol setOutputLinearRGBPixelBuffer:];
-[CMIColourConstancyProcessorProtocol setSaturationBoostEnabled:];
```
