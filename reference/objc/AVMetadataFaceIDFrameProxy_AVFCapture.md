# `AVMetadataFaceIDFrameProxy`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _frameIdentifier;
^{opaqueCMFormatDescription=} _formatDescription;
Q _sharedMemoryAreaOffset;
@"AVCaptureDevice" _sourceDevice;
```

## Properties

```
@property (TQ,N,V_frameIdentifier) frameIdentifier;
@property (T^{opaqueCMFormatDescription=},N,V_formatDescription) formatDescription;
@property (TQ,N,V_sharedMemoryAreaOffset) sharedMemoryAreaOffset;
```

## Instance methods

```
-[AVMetadataFaceIDFrameProxy formatDescription];
-[AVMetadataFaceIDFrameProxy dealloc];
-[AVMetadataFaceIDFrameProxy setFormatDescription:];
-[AVMetadataFaceIDFrameProxy setFrameIdentifier:];
-[AVMetadataFaceIDFrameProxy frameIdentifier];
-[AVMetadataFaceIDFrameProxy initWithFrameDictionary:sourceCaptureInput:];
-[AVMetadataFaceIDFrameProxy setSharedMemoryAreaOffset:];
-[AVMetadataFaceIDFrameProxy sharedMemoryAreaOffset];
```
