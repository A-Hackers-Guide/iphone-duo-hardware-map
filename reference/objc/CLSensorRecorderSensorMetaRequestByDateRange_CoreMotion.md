# `CLSensorRecorderSensorMetaRequestByDateRange`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
i _dataType;
d _startTime;
d _endTime;
```

## Properties

```
@property (Td,V_startTime) startTime;
@property (Td,V_endTime) endTime;
@property (Ti,V_dataType) dataType;
```

## Class methods

```
+[CLSensorRecorderSensorMetaRequestByDateRange supportsSecureCoding];
```

## Instance methods

```
-[CLSensorRecorderSensorMetaRequestByDateRange endTime];
-[CLSensorRecorderSensorMetaRequestByDateRange setEndTime:];
-[CLSensorRecorderSensorMetaRequestByDateRange setDataType:];
-[CLSensorRecorderSensorMetaRequestByDateRange startTime];
-[CLSensorRecorderSensorMetaRequestByDateRange setStartTime:];
-[CLSensorRecorderSensorMetaRequestByDateRange encodeWithCoder:];
-[CLSensorRecorderSensorMetaRequestByDateRange dataType];
-[CLSensorRecorderSensorMetaRequestByDateRange initWithCoder:];
```
