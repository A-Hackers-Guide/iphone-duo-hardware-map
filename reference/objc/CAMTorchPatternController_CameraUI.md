# `CAMTorchPatternController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
B __performing;
d _stepInterval;
@"CUCaptureController" __captureController;
@"CAMTorchPattern" __currentPattern;
d __startTime;
@"CADisplayLink" __displayLink;
```

## Properties

```
@property (T@"CUCaptureController",R,N,V__captureController) _captureController;
@property (TB,N,G_isPerforming,S_setPerforming:,V__performing) _performing;
@property (T@"CAMTorchPattern",R,N,V__currentPattern) _currentPattern;
@property (Td,R,N,V__startTime) _startTime;
@property (T@"CADisplayLink",R,N,V__displayLink) _displayLink;
@property (Td,N,V_stepInterval) stepInterval;
```

## Instance methods

```
-[CAMTorchPatternController _startTime];
-[CAMTorchPatternController _captureController];
-[CAMTorchPatternController displayLinkFired:];
-[CAMTorchPatternController _displayLink];
-[CAMTorchPatternController blink];
-[CAMTorchPatternController _currentPattern];
-[CAMTorchPatternController _setPerforming:];
-[CAMTorchPatternController _applyTorchLevel:];
-[CAMTorchPatternController _isPerforming];
-[CAMTorchPatternController _resetTorchLevel];
-[CAMTorchPatternController doubleBlink];
-[CAMTorchPatternController initWithCaptureController:];
-[CAMTorchPatternController setStepInterval:];
-[CAMTorchPatternController startPerformingPattern:];
-[CAMTorchPatternController stepInterval];
-[CAMTorchPatternController stopPerformingPattern];
```
