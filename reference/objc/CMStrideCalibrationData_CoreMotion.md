# `CMStrideCalibrationData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
q _state;
d _kValue;
d _begin;
d _end;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (Td,N,V_kValue) kValue;
@property (Td,N,V_begin) begin;
@property (Td,N,V_end) end;
```

## Class methods

```
+[CMStrideCalibrationData supportsSecureCoding];
```

## Instance methods

```
-[CMStrideCalibrationData setState:];
-[CMStrideCalibrationData begin];
-[CMStrideCalibrationData setBegin:];
-[CMStrideCalibrationData end];
-[CMStrideCalibrationData setEnd:];
-[CMStrideCalibrationData encodeWithCoder:];
-[CMStrideCalibrationData description];
-[CMStrideCalibrationData initWithCoder:];
-[CMStrideCalibrationData copyWithZone:];
-[CMStrideCalibrationData state];
-[CMStrideCalibrationData initWithBegin:end:state:kValue:];
-[CMStrideCalibrationData kValue];
-[CMStrideCalibrationData setKValue:];
```
