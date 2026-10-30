# `CLFindMyAccessoryAccelerometerSlopeModeConfiguration`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 5 class methods

## Instance variables

```
C _sampleCount;
C _sampleRate;
f _threshold;
```

## Properties

```
@property (Tf,N,V_threshold) threshold;
@property (TC,N,V_sampleCount) sampleCount;
@property (TC,N,V_sampleRate) sampleRate;
```

## Class methods

```
+[CLFindMyAccessoryAccelerometerSlopeModeConfiguration supportsSecureCoding];
+[CLFindMyAccessoryAccelerometerSlopeModeConfiguration maximumSampleCount];
+[CLFindMyAccessoryAccelerometerSlopeModeConfiguration minimumSampleCount];
+[CLFindMyAccessoryAccelerometerSlopeModeConfiguration maximumThreshold];
+[CLFindMyAccessoryAccelerometerSlopeModeConfiguration minimumThreshold];
```

## Instance methods

```
-[CLFindMyAccessoryAccelerometerSlopeModeConfiguration sampleRate];
-[CLFindMyAccessoryAccelerometerSlopeModeConfiguration setSampleCount:];
-[CLFindMyAccessoryAccelerometerSlopeModeConfiguration setThreshold:];
-[CLFindMyAccessoryAccelerometerSlopeModeConfiguration setSampleRate:];
-[CLFindMyAccessoryAccelerometerSlopeModeConfiguration threshold];
-[CLFindMyAccessoryAccelerometerSlopeModeConfiguration sampleCount];
-[CLFindMyAccessoryAccelerometerSlopeModeConfiguration encodeWithCoder:];
-[CLFindMyAccessoryAccelerometerSlopeModeConfiguration initWithCoder:];
-[CLFindMyAccessoryAccelerometerSlopeModeConfiguration initWithThreshold:sampleCount:sampleRate:];
```
