# `CAMBurstYUVImage`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
* Ybuffer;
* Cbuffer;
i width;
i height;
i bytesPerRow;
^{__CFData=} dataPtr;
^{__CVBuffer=} pixelBuffer;
^{__IOSurface=} ioSurf;
```

## Properties

```
@property (Ti,Vwidth) width;
@property (Ti,Vheight) height;
@property (Ti,VbytesPerRow) bytesPerRow;
@property (T*,VYbuffer) Ybuffer;
@property (T*,VCbuffer) Cbuffer;
```

## Instance methods

```
-[CAMBurstYUVImage pixelBuffer];
-[CAMBurstYUVImage bytesPerRow];
-[CAMBurstYUVImage dealloc];
-[CAMBurstYUVImage setHeight:];
-[CAMBurstYUVImage setBytesPerRow:];
-[CAMBurstYUVImage setWidth:];
-[CAMBurstYUVImage width];
-[CAMBurstYUVImage height];
-[CAMBurstYUVImage Cbuffer];
-[CAMBurstYUVImage Ybuffer];
-[CAMBurstYUVImage initWithIOSurface:maxDimension:];
-[CAMBurstYUVImage convertRGBAToYUV420:rgbaBytesPerRow:];
-[CAMBurstYUVImage initWithCGImage:maxDimension:];
-[CAMBurstYUVImage initWithCIImage:ctx:maxDimension:];
-[CAMBurstYUVImage setCbuffer:];
-[CAMBurstYUVImage setYbuffer:];
```
