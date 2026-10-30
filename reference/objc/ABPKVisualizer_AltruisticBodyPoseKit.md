# `ABPKVisualizer`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
^{__CVPixelBufferPool=} _pixelBufferPoolBGRA;
^{__CVPixelBufferPool=} _pixelBufferPoolYUV;
_highConfidenceColor;
_mediumConfidenceColor;
_lowConfidenceColor;
^{OpaqueVTPixelTransferSession=} _pixelTransferSession;
```

## Class methods

```
+[ABPKVisualizer _drawRectOfSize:posx:posy:pImage:red:green:blue:];
```

## Instance methods

```
-[ABPKVisualizer init];
-[ABPKVisualizer dealloc];
-[ABPKVisualizer drawBoundingBox:withColor:OnImage:andGenerateOverlayImage:];
-[ABPKVisualizer drawFaceBbox:detectedBodies2d:confidences:skeletonDefinition:overlayImage:color:];
-[ABPKVisualizer drawFaceBboxEdgewithJoints:withSkeletonDefinition:fromPostion:toPosition:OnImage:color:];
-[ABPKVisualizer drawLineFromPoint:ToPoint:withThickness:withColor:OnImage:];
-[ABPKVisualizer generateStickFigureImageFrom:detectedBodies2d:confidences:skeletonDefinition:overlayImage:color:faceOnly:];
-[ABPKVisualizer jointInImageDimensions:imageDimensions:];
-[ABPKVisualizer overlayJoints:withSkeletonDefinition:confidences:OnImage:color:faceOnly:];
```
