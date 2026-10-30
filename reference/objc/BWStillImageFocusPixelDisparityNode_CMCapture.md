# `BWStillImageFocusPixelDisparityNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"BWStillImageNodeConfiguration" _nodeConfiguration;
@"BWSensorConfiguration" _sensorConfiguration;
@"FigFocusPixelDisparityGenerator" _focusPixelDisparityGenerator;
^{opaqueCMFormatDescription=} _disparityFormatDescription;
{?="columns"[4]} _identityExtrinsicMatrix;
f _pixelSizeInMm;
B _depthIsAlwaysHighQuality;
f _defaultZoomFactor;
f _currentZoomFactorForFocusPixelDisparityGenerator;
```

## Class methods

```
+[BWStillImageFocusPixelDisparityNode initialize];
```

## Instance methods

```
-[BWStillImageFocusPixelDisparityNode prepareForCurrentConfigurationToBecomeLive];
-[BWStillImageFocusPixelDisparityNode renderSampleBuffer:forInput:];
-[BWStillImageFocusPixelDisparityNode dealloc];
-[BWStillImageFocusPixelDisparityNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWStillImageFocusPixelDisparityNode nodeSubType];
-[BWStillImageFocusPixelDisparityNode handleNodeError:forInput:];
-[BWStillImageFocusPixelDisparityNode nodeType];
-[BWStillImageFocusPixelDisparityNode initWithNodeConfiguration:sensorConfiguration:disparityMapWidth:disparityMapHeight:depthIsAlwaysHighQuality:defaultZoomFactor:];
```
