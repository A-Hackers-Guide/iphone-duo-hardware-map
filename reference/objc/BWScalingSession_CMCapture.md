# `BWScalingSession`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{OpaqueVTPixelRotationSession=} _rotationSession;
i _rotationSessionDegrees;
^{OpaqueVTPixelTransferSession=} _transferSession;
@"BWPixelBufferPool" _intermediateBufferPool;
{?="width"i"height"i} _intermediateBufferPoolDimensions;
```

## Instance methods

```
-[BWScalingSession init];
-[BWScalingSession dealloc];
-[BWScalingSession invalidate];
-[BWScalingSession _ensurePixelTransferSession];
-[BWScalingSession _newIntermediatePoolWithDimensions:pixelFormat:];
-[BWScalingSession scalePixelBuffer:rect:exifOrientation:intoPixelBuffer:rect:];
-[BWScalingSession scalePixelBuffer:rect:intoPixelBuffer:rect:];
```
