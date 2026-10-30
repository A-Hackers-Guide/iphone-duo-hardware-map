# `AVCaptureSystemPressureState`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"AVCaptureSystemPressureStateInternal" _internal;
```

## Properties

```
@property (T@"NSString",R) level;
@property (TQ,R) factors;
```

## Class methods

```
+[AVCaptureSystemPressureState initialize];
```

## Instance methods

```
-[AVCaptureSystemPressureState factors];
-[AVCaptureSystemPressureState initWithFigLevel:factors:recommendedFrameRateRangeForPortrait:recommendedFrameRateRangeForPhotoMode:];
-[AVCaptureSystemPressureState debugDescription];
-[AVCaptureSystemPressureState init];
-[AVCaptureSystemPressureState dealloc];
-[AVCaptureSystemPressureState figLevel];
-[AVCaptureSystemPressureState level];
-[AVCaptureSystemPressureState spiDebugDescription];
-[AVCaptureSystemPressureState description];
-[AVCaptureSystemPressureState recommendedFrameRateRangeForPortrait];
-[AVCaptureSystemPressureState isEqual:];
-[AVCaptureSystemPressureState recommendedFrameRateRangeForPhotoMode];
```
