# `CLBIO_Calibration`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
f _rotationToTrueNorth_rad;
f _scaleFactor;
```

## Properties

```
@property (Tf,R,N,V_rotationToTrueNorth_rad) rotationToTrueNorth_rad;
@property (Tf,R,N,V_scaleFactor) scaleFactor;
```

## Class methods

```
+[CLBIO_Calibration supportsSecureCoding];
```

## Instance methods

```
-[CLBIO_Calibration scaleFactor];
-[CLBIO_Calibration encodeWithCoder:];
-[CLBIO_Calibration isValid];
-[CLBIO_Calibration initWithCoder:];
-[CLBIO_Calibration copyWithZone:];
-[CLBIO_Calibration isEqual:];
-[CLBIO_Calibration initWithRotationToTrueNorth:scaleFactor:];
-[CLBIO_Calibration rotationToTrueNorth_rad];
```
