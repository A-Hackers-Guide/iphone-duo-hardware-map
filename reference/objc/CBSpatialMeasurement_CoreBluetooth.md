# `CBSpatialMeasurement`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`
- 11 instance variables, 11 properties, 25 instance methods, 0 class methods

## Instance variables

```
I _flags;
d _distanceMeters;
d _distanceError;
@"NSError" _error;
d _horizontalAngle;
d _horizontalError;
@"NSString" _identifier;
d _verticalAngle;
d _verticalError;
Q _timestampTicks;
d _ptsScore;
```

## Properties

```
@property (Td,N,V_horizontalAngle) horizontalAngle;
@property (Td,N,V_horizontalError) horizontalError;
@property (Td,N,V_verticalAngle) verticalAngle;
@property (Td,N,V_verticalError) verticalError;
@property (Td,N,V_distanceMeters) distanceMeters;
@property (Td,N,V_distanceError) distanceError;
@property (T@"NSError",C,N,V_error) error;
@property (TI,N,V_flags) flags;
@property (T@"NSString",C,N,V_identifier) identifier;
@property (Td,N,V_ptsScore) ptsScore;
@property (TQ,N,V_timestampTicks) timestampTicks;
```

## Instance methods

```
-[CBSpatialMeasurement encodeWithXPCObject:];
-[CBSpatialMeasurement setError:];
-[CBSpatialMeasurement initWithXPCObject:error:];
-[CBSpatialMeasurement setFlags:];
-[CBSpatialMeasurement flags];
-[CBSpatialMeasurement identifier];
-[CBSpatialMeasurement error];
-[CBSpatialMeasurement setIdentifier:];
-[CBSpatialMeasurement description];
-[CBSpatialMeasurement horizontalError];
-[CBSpatialMeasurement horizontalAngle];
-[CBSpatialMeasurement distanceError];
-[CBSpatialMeasurement distanceMeters];
-[CBSpatialMeasurement ptsScore];
-[CBSpatialMeasurement setDistanceError:];
-[CBSpatialMeasurement setDistanceMeters:];
-[CBSpatialMeasurement setHorizontalAngle:];
-[CBSpatialMeasurement setHorizontalError:];
-[CBSpatialMeasurement setPtsScore:];
-[CBSpatialMeasurement setTimestampTicks:];
-[CBSpatialMeasurement setVerticalAngle:];
-[CBSpatialMeasurement setVerticalError:];
-[CBSpatialMeasurement timestampTicks];
-[CBSpatialMeasurement verticalAngle];
-[CBSpatialMeasurement verticalError];
```
