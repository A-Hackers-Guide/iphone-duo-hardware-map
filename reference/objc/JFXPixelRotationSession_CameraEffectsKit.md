# `JFXPixelRotationSession`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 10 instance methods, 5 class methods

## Instance variables

```
^{OpaqueVTPixelRotationSession=} _imageRotationSession;
B _mirror;
i _rotationCardinalAngle;
@"JFXPixelBufferPool" _pixelBufferPool;
```

## Properties

```
@property (T@"JFXPixelBufferPool",&,N,V_pixelBufferPool) pixelBufferPool;
@property (Ti,R,N,V_rotationCardinalAngle) rotationCardinalAngle;
@property (TB,R,N,V_mirror) mirror;
```

## Class methods

```
+[JFXPixelRotationSession JFX_rotateFrameSet:toOrientation:pixelRotationSession:];
+[JFXPixelRotationSession rotateFrameSet:by:mirror:pixelRotationSession:];
+[JFXPixelRotationSession rotateFrameSetToDeviceOrientation:pixelRotationSession:];
+[JFXPixelRotationSession rotateFrameSetToUIOrientation:pixelRotationSession:];
+[JFXPixelRotationSession toVTRotation:];
```

## Instance methods

```
-[JFXPixelRotationSession setPixelBufferPool:];
-[JFXPixelRotationSession pixelBufferPool];
-[JFXPixelRotationSession mirror];
-[JFXPixelRotationSession dealloc];
-[JFXPixelRotationSession createRotatedPixelBuffer:using:];
-[JFXPixelRotationSession JT_releaseImageRotationSession];
-[JFXPixelRotationSession createRotatedFrameSet:];
-[JFXPixelRotationSession createRotatedPixelBuffer:];
-[JFXPixelRotationSession initWithRotation:mirror:];
-[JFXPixelRotationSession rotationCardinalAngle];
```
