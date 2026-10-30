# `BWSkinTextureStyleRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 3 instance variables, 8 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"BWSmartStyleRendererConfiguration" _configuration;
@"CMITextureStylesProcessor" _skinTextureStylesProcessor;
@"NSString" _fileName;
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
+[BWSkinTextureStyleRenderer initialize];
+[BWSkinTextureStyleRenderer requiredSharedMetalAllocatorBackendSizeWithProcessorVersion:];
```

## Instance methods

```
-[BWSkinTextureStyleRenderer displayName];
-[BWSkinTextureStyleRenderer dealloc];
-[BWSkinTextureStyleRenderer initWithConfiguration:];
-[BWSkinTextureStyleRenderer type];
-[BWSkinTextureStyleRenderer adjustsMetadata];
-[BWSkinTextureStyleRenderer isMetalRenderer];
-[BWSkinTextureStyleRenderer adjustMetadataOfSampleBuffer:];
-[BWSkinTextureStyleRenderer isPassThroughRenderer];
-[BWSkinTextureStyleRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWSkinTextureStyleRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWSkinTextureStyleRenderer supportsAnimation];
-[BWSkinTextureStyleRenderer waitForMetalCompletion];
```
