# `VTFrameProcessorFrame`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"VEFrame" _veFrame;
^{__CVBuffer=} _buffer;
{?="value"q"timescale"i"flags"I"epoch"q} _presentationTimeStamp;
```

## Properties

```
@property (T^{__CVBuffer=},R,N,V_buffer) buffer;
@property (T{?=qiIq},R,N,V_presentationTimeStamp) presentationTimeStamp;
```

## Instance methods

```
-[VTFrameProcessorFrame buffer];
-[VTFrameProcessorFrame dealloc];
-[VTFrameProcessorFrame presentationTimeStamp];
-[VTFrameProcessorFrame veFrame];
-[VTFrameProcessorFrame initWithBuffer:presentationTimeStamp:];
```
