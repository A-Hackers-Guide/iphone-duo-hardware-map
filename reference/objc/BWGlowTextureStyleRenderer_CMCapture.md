# `BWGlowTextureStyleRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 4 instance variables, 8 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"BWSmartStyleRendererConfiguration" _configuration;
^{opaqueCMFormatDescription=} _outputFormatDescription;
# _smartStyleClass;
@"CMITextureStylesProcessor" _glowTextureStylesProcessor;
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
+[BWGlowTextureStyleRenderer initialize];
+[BWGlowTextureStyleRenderer requiredSharedMetalAllocatorBackendSizeWithProcessorVersion:];
```

## Instance methods

```
-[BWGlowTextureStyleRenderer displayName];
-[BWGlowTextureStyleRenderer dealloc];
-[BWGlowTextureStyleRenderer initWithConfiguration:];
-[BWGlowTextureStyleRenderer type];
-[BWGlowTextureStyleRenderer adjustsMetadata];
-[BWGlowTextureStyleRenderer isMetalRenderer];
-[BWGlowTextureStyleRenderer adjustMetadataOfSampleBuffer:];
-[BWGlowTextureStyleRenderer isPassThroughRenderer];
-[BWGlowTextureStyleRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWGlowTextureStyleRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWGlowTextureStyleRenderer supportsAnimation];
-[BWGlowTextureStyleRenderer waitForMetalCompletion];
```
