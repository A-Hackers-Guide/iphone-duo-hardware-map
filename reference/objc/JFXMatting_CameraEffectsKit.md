# `JFXMatting`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 6 instance methods, 9 class methods

## Instance variables

```
{CGSize="width"d"height"d} _colorBufferSize;
q _cameraLocation;
B _ready;
```

## Properties

```
@property (TB,N,V_ready) ready;
```

## Class methods

```
+[JFXMatting postNotification:];
+[JFXMatting canMatteWithANE];
+[JFXMatting _defaultMatteGeneratorPrefersDepth];
+[JFXMatting defaultMatteGenerator:];
+[JFXMatting defaultMatteGeneratorClass];
+[JFXMatting defaultMatteGeneratorPrefersDepth];
+[JFXMatting depthDataForCVPixelBuffer:];
+[JFXMatting isCVASegMattingSPIWorking];
+[JFXMatting mattingDepthInputSize];
```

## Instance methods

```
-[JFXMatting ready];
-[JFXMatting setReady:];
-[JFXMatting alphaMatteForFrameSet:mattingPerfState:completionHandler:];
-[JFXMatting initForFrameSet:];
-[JFXMatting isValidForCameraFrameSet:];
-[JFXMatting requestMattingStatus];
```
