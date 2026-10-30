# `CAMOrientationSeedSampler`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
q seedOrientation;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 seedingStartTimestamp;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 seedingWindowClosed;
```

## Properties

```
@property (Tq,N,VseedOrientation) seedOrientation;
@property (TB,N,R) needsSample;
```

## Class methods

```
+[CAMOrientationSeedSampler desiredUpdateInterval];
```

## Instance methods

```
-[CAMOrientationSeedSampler init];
-[CAMOrientationSeedSampler reset];
-[CAMOrientationSeedSampler seedOrientation];
-[CAMOrientationSeedSampler applyDeviceMotion:];
-[CAMOrientationSeedSampler needsSample];
-[CAMOrientationSeedSampler setSeedOrientation:];
```
