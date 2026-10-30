# `BWSmartStyleRenderingProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWSmartStyleRenderingProcessorControllerInputUpdatesDelegate`
- 13 instance variables, 4 properties, 10 instance methods, 5 class methods

## Instance variables

```
@"BWSmartStyleRenderingProcessorControllerConfiguration" _configuration;
@"<CMISmartStyleProcessor>" _smartStyleProcessor;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{opaqueCMFormatDescription=} _smartStyleLinearThumbnailFormatDescription;
^{opaqueCMFormatDescription=} _smartStyleStyledThumbnailFormatDescription;
^{opaqueCMFormatDescription=} _smallLightMapFormatDescription;
^{opaqueCMFormatDescription=} _coefficientsFormatDescription;
^{opaqueCMFormatDescription=} _reverseCoefficientsFormatDescription;
^{opaqueCMFormatDescription=} _personSegmentationFormatDescription;
^{opaqueCMFormatDescription=} _skinSegmentationFormatDescription;
^{opaqueCMFormatDescription=} _skySegmentationFormatDescription;
# _smartStyleClass;
# _smartStyleProcessorInputOutputClass;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWSmartStyleRenderingProcessorController linearYUVIntermediateThumbnailDimensionsForUseCase:];
+[BWSmartStyleRenderingProcessorController linearYUVPixelFormat];
+[BWSmartStyleRenderingProcessorController pixelBufferAttributesForSmallLightMap:aspectRatio:];
+[BWSmartStyleRenderingProcessorController pixelBufferAttributesWithCapacityForLearntCoefficients:aspectRatio:];
+[BWSmartStyleRenderingProcessorController usesCustomProcessingFlow];
```

## Instance methods

```
-[BWSmartStyleRenderingProcessorController inputAddFrameFailed:];
-[BWSmartStyleRenderingProcessorController process];
-[BWSmartStyleRenderingProcessorController dealloc];
-[BWSmartStyleRenderingProcessorController reset];
-[BWSmartStyleRenderingProcessorController initWithConfiguration:];
-[BWSmartStyleRenderingProcessorController prepare];
-[BWSmartStyleRenderingProcessorController metalImageBufferProcessor];
-[BWSmartStyleRenderingProcessorController requestForInput:delegate:errOut:];
-[BWSmartStyleRenderingProcessorController input:addFrame:];
-[BWSmartStyleRenderingProcessorController updateSmartStyleProcessorConfigurationIfNeededForApplyOnly:aspectRatio:];
```
