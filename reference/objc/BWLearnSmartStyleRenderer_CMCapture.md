# `BWLearnSmartStyleRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 5 instance variables, 8 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"<CMISmartStyleProcessor>" _smartStyleProcessor;
@"BWSmartStyleRendererConfiguration" _configuration;
# _smartStyleProcessorInputOutputClass;
# _smartStyleClass;
^{opaqueCMFormatDescription=} _coefficientsFormatDescription;
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
+[BWLearnSmartStyleRenderer initialize];
+[BWLearnSmartStyleRenderer requiredSharedMetalAllocatorBackendSizeWithProcessorVersion:];
```

## Instance methods

```
-[BWLearnSmartStyleRenderer displayName];
-[BWLearnSmartStyleRenderer dealloc];
-[BWLearnSmartStyleRenderer initWithConfiguration:];
-[BWLearnSmartStyleRenderer type];
-[BWLearnSmartStyleRenderer adjustsMetadata];
-[BWLearnSmartStyleRenderer isMetalRenderer];
-[BWLearnSmartStyleRenderer adjustMetadataOfSampleBuffer:];
-[BWLearnSmartStyleRenderer isPassThroughRenderer];
-[BWLearnSmartStyleRenderer prepareForProcessingType:];
-[BWLearnSmartStyleRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWLearnSmartStyleRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWLearnSmartStyleRenderer supportsAnimation];
-[BWLearnSmartStyleRenderer waitForMetalCompletion];
```
