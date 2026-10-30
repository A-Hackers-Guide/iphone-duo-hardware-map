# `BWStreamingCVAFilterRendererAnimator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
{?="simulatedAperture"f} _currentFrame;
i _mostRecentEffectStatus;
@"BWRamp" _simulatedApertureRamp;
B _overCaptureEnabled;
```

## Properties

```
@property (TB,R,N,GisDepthAvailable) depthAvailable;
```

## Class methods

```
+[BWStreamingCVAFilterRendererAnimator initialize];
```

## Instance methods

```
-[BWStreamingCVAFilterRendererAnimator init];
-[BWStreamingCVAFilterRendererAnimator dealloc];
-[BWStreamingCVAFilterRendererAnimator initWithEffectStatus:overCaptureEnabled:];
-[BWStreamingCVAFilterRendererAnimator isDepthAvailable];
-[BWStreamingCVAFilterRendererAnimator simulateNextFrameWithEffectStatus:portraitStability:clientSuppliedSimulatedAperture:];
```
