# `CLSmootherAltitudeSample`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 7 instance methods, 3 class methods

## Instance variables

```
d _timestamp;
d _altitude;
d _verticalAccuracy;
```

## Properties

```
@property (Td,R,N,V_timestamp) timestamp;
@property (Td,R,N,V_altitude) altitude;
@property (Td,R,N,V_verticalAccuracy) verticalAccuracy;
```

## Class methods

```
+[CLSmootherAltitudeSample supportsSecureCoding];
+[CLSmootherAltitudeSample samplesFromPackedBytes:length:];
+[CLSmootherAltitudeSample packedDataFromSamples:];
```

## Instance methods

```
-[CLSmootherAltitudeSample altitude];
-[CLSmootherAltitudeSample timestamp];
-[CLSmootherAltitudeSample verticalAccuracy];
-[CLSmootherAltitudeSample encodeWithCoder:];
-[CLSmootherAltitudeSample initWithCoder:];
-[CLSmootherAltitudeSample copyWithZone:];
-[CLSmootherAltitudeSample initWithTimestamp:altitude:verticalAccuracy:];
```
