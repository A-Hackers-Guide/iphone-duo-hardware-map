# `JFXImageAVSampleBufferView`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `JFXImageViewRendering`
- 6 instance variables, 11 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _flipX;
B _flipY;
B _enableDebugDrawing;
@"JTImage" _jtImage;
q _renderingType;
@"UILabel" _hdrBadgeDebug;
```

## Properties

```
@property (T@"AVSampleBufferDisplayLayer",R,N) sampleBufferDisplayLayer;
@property (T@"UILabel",&,N,V_hdrBadgeDebug) hdrBadgeDebug;
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

## Class methods

```
+[JFXImageAVSampleBufferView layerClass];
```

## Instance methods

```
-[JFXImageAVSampleBufferView setContentMode:];
-[JFXImageAVSampleBufferView initWithCoder:];
-[JFXImageAVSampleBufferView initWithFrame:];
-[JFXImageAVSampleBufferView sampleBufferDisplayLayer];
-[JFXImageAVSampleBufferView flipX];
-[JFXImageAVSampleBufferView renderingType];
-[JFXImageAVSampleBufferView JFXImageAVSampleBufferView_commonInit];
-[JFXImageAVSampleBufferView createCMSampleBufferFromJTImage];
-[JFXImageAVSampleBufferView jtImage];
-[JFXImageAVSampleBufferView drawSampleBufferToLayer:];
-[JFXImageAVSampleBufferView enableDebugDrawing];
-[JFXImageAVSampleBufferView flipY];
-[JFXImageAVSampleBufferView hdrBadgeDebug];
-[JFXImageAVSampleBufferView setEnableDebugDrawing:];
-[JFXImageAVSampleBufferView setFlipX:];
-[JFXImageAVSampleBufferView setFlipY:];
-[JFXImageAVSampleBufferView setHdrBadgeDebug:];
-[JFXImageAVSampleBufferView setJtImage:];
-[JFXImageAVSampleBufferView setRenderingType:];
-[JFXImageAVSampleBufferView updateDebugDrawing];
```
