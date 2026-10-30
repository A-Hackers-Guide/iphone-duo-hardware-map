# `ImageBufferProcessor` (protocol)

- Image: [`/System/Library/VideoProcessors/MetalFilter.bundle/MetalFilter`](../userland/System__Library__VideoProcessors__MetalFilter.bundle__MetalFilter.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",&,N) tuningParameters;
@property (T@"NSDictionary",&,N) cameraInfoByPortType;
```

## Instance methods

```
-[ImageBufferProcessor resetState];
-[ImageBufferProcessor tuningParameters];
-[ImageBufferProcessor finishProcessing];
-[ImageBufferProcessor purgeResources];
-[ImageBufferProcessor setCameraInfoByPortType:];
-[ImageBufferProcessor prewarm];
-[ImageBufferProcessor prepareToProcess:];
-[ImageBufferProcessor setup];
-[ImageBufferProcessor cameraInfoByPortType];
-[ImageBufferProcessor setTuningParameters:];
-[ImageBufferProcessor process];
-[ImageBufferProcessor prewarmWithTuningParameters:];
```
