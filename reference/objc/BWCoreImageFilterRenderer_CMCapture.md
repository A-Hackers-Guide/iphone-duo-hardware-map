# `BWCoreImageFilterRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWFilterRenderer`
- 8 instance variables, 10 properties, 13 instance methods, 4 class methods

## Instance variables

```
B _usingDepth;
i _portraitRenderQuality;
f _inputRenderQuality;
@"NSObject<OS_dispatch_queue>" _renderingQueue;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
@"CIContext" _renderingQueueContext;
@"<MTLCommandQueue>" _metalCommandQueue;
B _hairnetEnabled;
```

## Properties

```
@property (TB,R,N,V_usingDepth) usingDepth;
@property (T@"CIContext",&,N,V_renderingQueueContext) renderingQueueContext;
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
+[BWCoreImageFilterRenderer initialize];
+[BWCoreImageFilterRenderer context:deferredPhotoProcessorEnabled:allocatorBackend:mtlCommandQueue:err:];
+[BWCoreImageFilterRenderer prewarmCoreImageSDOFRenderingFilter];
+[BWCoreImageFilterRenderer prewarmPortraitFilterVersion:semanticStyleFilters:];
```

## Instance methods

```
-[BWCoreImageFilterRenderer displayName];
-[BWCoreImageFilterRenderer dealloc];
-[BWCoreImageFilterRenderer type];
-[BWCoreImageFilterRenderer adjustsMetadata];
-[BWCoreImageFilterRenderer adjustMetadataOfSampleBuffer:];
-[BWCoreImageFilterRenderer initForRenderingWithDepth:context:portraitRenderQuality:hairnetEnabled:metalCommandQueue:figThreadPriority:];
-[BWCoreImageFilterRenderer isPassThroughRenderer];
-[BWCoreImageFilterRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWCoreImageFilterRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWCoreImageFilterRenderer renderingQueueContext];
-[BWCoreImageFilterRenderer setRenderingQueueContext:];
-[BWCoreImageFilterRenderer supportsAnimation];
-[BWCoreImageFilterRenderer usingDepth];
```
