# `BWSmartStyleReversibilityRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 7 instance variables, 8 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"<CMISmartStyleProcessor>" _smartStyleProcessor;
@"BWSmartStyleRendererConfiguration" _configuration;
# _smartStyleProcessorInputOutputClass;
# _smartStyleClass;
^{opaqueCMFormatDescription=} _coefficientsFormatDescription;
^{opaqueCMFormatDescription=} _smartStyleStyledThumbnailFormatDescription;
^{opaqueCMFormatDescription=} _reverseCoefficientsFormatDescription;
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
+[BWSmartStyleReversibilityRenderer initialize];
+[BWSmartStyleReversibilityRenderer requiredSharedMetalAllocatorBackendSizeWithProcessorVersion:];
```

## Instance methods

```
-[BWSmartStyleReversibilityRenderer displayName];
-[BWSmartStyleReversibilityRenderer dealloc];
-[BWSmartStyleReversibilityRenderer initWithConfiguration:];
-[BWSmartStyleReversibilityRenderer type];
-[BWSmartStyleReversibilityRenderer adjustsMetadata];
-[BWSmartStyleReversibilityRenderer isMetalRenderer];
-[BWSmartStyleReversibilityRenderer adjustMetadataOfSampleBuffer:];
-[BWSmartStyleReversibilityRenderer isPassThroughRenderer];
-[BWSmartStyleReversibilityRenderer prepareForProcessingType:];
-[BWSmartStyleReversibilityRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWSmartStyleReversibilityRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWSmartStyleReversibilityRenderer supportsAnimation];
-[BWSmartStyleReversibilityRenderer waitForMetalCompletion];
```
