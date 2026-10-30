# `CLSensorRecorderSensorMeta`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _movement;
I _offset;
I _dataSize;
i _dataType;
Q _identifier;
d _startTime;
Q _timestamp;
Q _dataIdentifier;
```

## Properties

```
@property (TQ,V_identifier) identifier;
@property (Td,V_startTime) startTime;
@property (TQ,V_timestamp) timestamp;
@property (TQ,V_dataIdentifier) dataIdentifier;
@property (TI,V_offset) offset;
@property (TI,V_dataSize) dataSize;
@property (Ti,V_dataType) dataType;
@property (TB,V_movement) movement;
```

## Class methods

```
+[CLSensorRecorderSensorMeta supportsSecureCoding];
```

## Instance methods

```
-[CLSensorRecorderSensorMeta setTimestamp:];
-[CLSensorRecorderSensorMeta setDataType:];
-[CLSensorRecorderSensorMeta identifier];
-[CLSensorRecorderSensorMeta startTime];
-[CLSensorRecorderSensorMeta timestamp];
-[CLSensorRecorderSensorMeta setDataSize:];
-[CLSensorRecorderSensorMeta setIdentifier:];
-[CLSensorRecorderSensorMeta setStartTime:];
-[CLSensorRecorderSensorMeta encodeWithCoder:];
-[CLSensorRecorderSensorMeta dataType];
-[CLSensorRecorderSensorMeta description];
-[CLSensorRecorderSensorMeta initWithCoder:];
-[CLSensorRecorderSensorMeta setOffset:];
-[CLSensorRecorderSensorMeta dataSize];
-[CLSensorRecorderSensorMeta offset];
-[CLSensorRecorderSensorMeta movement];
-[CLSensorRecorderSensorMeta initWithDataType:];
-[CLSensorRecorderSensorMeta dataIdentifier];
-[CLSensorRecorderSensorMeta setDataIdentifier:];
-[CLSensorRecorderSensorMeta setMovement:];
```
