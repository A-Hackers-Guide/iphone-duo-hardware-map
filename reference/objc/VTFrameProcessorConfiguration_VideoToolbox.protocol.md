# `VTFrameProcessorConfiguration` (protocol)

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 5 instance methods, 1 class methods

## Properties

```
@property (T@"NSArray",R,N) frameSupportedPixelFormats;
@property (T@"NSDictionary",R,N) sourcePixelBufferAttributes;
@property (T@"NSDictionary",R,N) destinationPixelBufferAttributes;
@property (Tq,?,R,N) nextFrameCount;
@property (Tq,?,R,N) previousFrameCount;
@property (class, TB,R,N,GisSupported) supported;
@property (class, T{?=ii},?,R,N) maximumDimensions;
@property (class, T{?=ii},?,R,N) minimumDimensions;
```

## Class methods

```
+[VTFrameProcessorConfiguration isSupported];
```

## Instance methods

```
-[VTFrameProcessorConfiguration destinationPixelBufferAttributes];
-[VTFrameProcessorConfiguration frameSupportedPixelFormats];
-[VTFrameProcessorConfiguration sourcePixelBufferAttributes];
-[VTFrameProcessorConfiguration nextFrameCount];
-[VTFrameProcessorConfiguration previousFrameCount];
```
