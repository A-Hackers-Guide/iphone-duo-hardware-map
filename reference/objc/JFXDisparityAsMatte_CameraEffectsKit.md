# `JFXDisparityAsMatte`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXMatting`
- 4 instance variables, 0 properties, 2 instance methods, 2 class methods

## Instance variables

```
^{__CVPixelBufferPool=} _fixedPointBufferPool;
^{__CVPixelBufferPool=} _rotatedFPBufferPool;
^{__CVPixelBufferPool=} _scaledUpFPBufferPool;
^{__CVPixelBufferPool=} _alphaMattePool;
```

## Class methods

```
+[JFXDisparityAsMatte _defaultMatteGeneratorPrefersDepth];
+[JFXDisparityAsMatte mattingDepthInputSize];
```

## Instance methods

```
-[JFXDisparityAsMatte alphaMatteForFrameSet:mattingPerfState:completionHandler:];
-[JFXDisparityAsMatte initForFrameSet:];
```
