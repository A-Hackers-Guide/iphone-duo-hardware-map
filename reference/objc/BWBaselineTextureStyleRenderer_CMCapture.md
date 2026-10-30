# `BWBaselineTextureStyleRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 2 instance variables, 8 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"BWSmartStyleRendererConfiguration" _configuration;
@"CMITextureStylesProcessor" _baselineTextureStylesProcessor;
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
+[BWBaselineTextureStyleRenderer initialize];
+[BWBaselineTextureStyleRenderer requiredSharedMetalAllocatorBackendSizeWithProcessorVersion:];
```

## Instance methods

```
-[BWBaselineTextureStyleRenderer displayName];
-[BWBaselineTextureStyleRenderer dealloc];
-[BWBaselineTextureStyleRenderer initWithConfiguration:];
-[BWBaselineTextureStyleRenderer type];
-[BWBaselineTextureStyleRenderer adjustsMetadata];
-[BWBaselineTextureStyleRenderer isMetalRenderer];
-[BWBaselineTextureStyleRenderer adjustMetadataOfSampleBuffer:];
-[BWBaselineTextureStyleRenderer isPassThroughRenderer];
-[BWBaselineTextureStyleRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWBaselineTextureStyleRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWBaselineTextureStyleRenderer supportsAnimation];
-[BWBaselineTextureStyleRenderer waitForMetalCompletion];
```
