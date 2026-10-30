# `JFXDepthAsMatte`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXMatting`
- 3 instance variables, 0 properties, 3 instance methods, 2 class methods

## Instance variables

```
^{__CVPixelBufferPool=} _rotatedFBufferPool;
^{__CVPixelBufferPool=} _scaledUpFBufferPool;
^{__CVPixelBufferPool=} _alphaPool;
```

## Class methods

```
+[JFXDepthAsMatte _defaultMatteGeneratorPrefersDepth];
+[JFXDepthAsMatte mattingDepthInputSize];
```

## Instance methods

```
-[JFXDepthAsMatte dealloc];
-[JFXDepthAsMatte alphaMatteForFrameSet:mattingPerfState:completionHandler:];
-[JFXDepthAsMatte initForFrameSet:];
```
