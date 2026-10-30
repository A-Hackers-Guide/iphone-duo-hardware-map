# `BWFilterRenderer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) displayName;
@property (Ts,R,N) type;
@property (TB,R,N) supportsAnimation;
@property (TB,R,N) adjustsMetadata;
```

## Instance methods

```
-[BWFilterRenderer displayName];
-[BWFilterRenderer type];
-[BWFilterRenderer adjustsMetadata];
-[BWFilterRenderer adjustMetadataOfSampleBuffer:];
-[BWFilterRenderer isPassThroughRenderer];
-[BWFilterRenderer prepareForRenderingWithParameters:inputVideoFormat:inputMediaPropertiesByAttachedMediaKey:];
-[BWFilterRenderer renderUsingParameters:inputPixelBuffer:inputSampleBuffer:processedPixelBuffer:completionHandler:];
-[BWFilterRenderer supportsAnimation];
-[BWFilterRenderer isMetalRenderer];
-[BWFilterRenderer prepareForProcessingType:];
-[BWFilterRenderer waitForMetalCompletion];
```
