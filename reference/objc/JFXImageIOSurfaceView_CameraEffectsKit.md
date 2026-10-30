# `JFXImageIOSurfaceView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `JFXImageViewRendering`
- 5 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _flipX;
B _flipY;
B _enableDebugDrawing;
@"JTImage" _jtImage;
q _renderingType;
```

## Properties

```
@property (T@"JTImage",&,N,V_jtImage) jtImage;
@property (Tq,R,N,V_renderingType) renderingType;
@property (TB,N,V_flipX) flipX;
@property (TB,N,V_flipY) flipY;
@property (TB,N,V_enableDebugDrawing) enableDebugDrawing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[JFXImageIOSurfaceView initWithCoder:];
-[JFXImageIOSurfaceView initWithFrame:];
-[JFXImageIOSurfaceView flipX];
-[JFXImageIOSurfaceView renderingType];
-[JFXImageIOSurfaceView JFXImageIOSurfaceView_commonInit];
-[JFXImageIOSurfaceView jtImage];
-[JFXImageIOSurfaceView enableDebugDrawing];
-[JFXImageIOSurfaceView flipY];
-[JFXImageIOSurfaceView setEnableDebugDrawing:];
-[JFXImageIOSurfaceView setFlipX:];
-[JFXImageIOSurfaceView setFlipY:];
-[JFXImageIOSurfaceView setJtImage:];
-[JFXImageIOSurfaceView setRenderingType:];
-[JFXImageIOSurfaceView updateDebugDrawing];
```
