# `ImageBufferProcessor` (protocol)

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
