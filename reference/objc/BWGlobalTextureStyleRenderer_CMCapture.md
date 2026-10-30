# `BWGlobalTextureStyleRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 2 instance variables, 8 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"BWSmartStyleRendererConfiguration" _configuration;
@"CMITextureStylesProcessor" _globalTextureStylesProcessor;
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
+[BWGlobalTextureStyleRenderer initialize];
+[BWGlobalTextureStyleRenderer requiredSharedMetalAllocatorBackendSizeWithProcessorVersion:];
```

## Instance methods

```
-[BWGlobalTextureStyleRenderer displayName];
-[BWGlobalTextureStyleRenderer dealloc];
-[BWGlobalTextureStyleRenderer initWithConfiguration:];
-[BWGlobalTextureStyleRenderer type];
-[BWGlobalTextureStyleRenderer adjustsMetadata];
-[BWGlobalTextureStyleRenderer isMetalRenderer];
-[BWGlobalTextureStyleRenderer adjustMetadataOfSampleBuffer:];
-[BWGlobalTextureStyleRenderer isPassThroughRenderer];
-[BWGlobalTextureStyleRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWGlobalTextureStyleRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWGlobalTextureStyleRenderer supportsAnimation];
-[BWGlobalTextureStyleRenderer waitForMetalCompletion];
```
