# `BWSmartStyleTargetRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 8 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"<CMISmartStyleProcessor>" _smartStyleProcessor;
@"BWSmartStyleRendererConfiguration" _configuration;
# _smartStyleProcessorInputOutputClass;
# _smartStyleClass;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{opaqueCMFormatDescription=} _targetFormatDescription;
^{opaqueCMFormatDescription=} _smartStyleLinearThumbnailFormatDescription;
^{opaqueCMFormatDescription=} _smallLightMapFormatDescription;
```

## Properties

```
@property (T@"NSString",R,C,N) displayName;
@property (Ts,R,N) type;
@property (TB,R,N) supportsAnimation;
@property (TB,R,N) adjustsMetadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWSmartStyleTargetRenderer initialize];
```

## Instance methods

```
-[BWSmartStyleTargetRenderer displayName];
-[BWSmartStyleTargetRenderer dealloc];
-[BWSmartStyleTargetRenderer initWithConfiguration:];
-[BWSmartStyleTargetRenderer type];
-[BWSmartStyleTargetRenderer adjustsMetadata];
-[BWSmartStyleTargetRenderer isMetalRenderer];
-[BWSmartStyleTargetRenderer adjustMetadataOfSampleBuffer:];
-[BWSmartStyleTargetRenderer isPassThroughRenderer];
-[BWSmartStyleTargetRenderer prepareForProcessingType:];
-[BWSmartStyleTargetRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWSmartStyleTargetRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWSmartStyleTargetRenderer supportsAnimation];
-[BWSmartStyleTargetRenderer waitForMetalCompletion];
```
