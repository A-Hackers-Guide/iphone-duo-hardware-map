# `CLSensorRecorderSensorDataRequestById`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
i _dataType;
Q _identifier;
Q _metaIdentifier;
```

## Properties

```
@property (TQ,V_identifier) identifier;
@property (TQ,V_metaIdentifier) metaIdentifier;
@property (Ti,V_dataType) dataType;
```

## Class methods

```
+[CLSensorRecorderSensorDataRequestById supportsSecureCoding];
```

## Instance methods

```
-[CLSensorRecorderSensorDataRequestById setDataType:];
-[CLSensorRecorderSensorDataRequestById identifier];
-[CLSensorRecorderSensorDataRequestById setIdentifier:];
-[CLSensorRecorderSensorDataRequestById encodeWithCoder:];
-[CLSensorRecorderSensorDataRequestById dataType];
-[CLSensorRecorderSensorDataRequestById initWithCoder:];
-[CLSensorRecorderSensorDataRequestById metaIdentifier];
-[CLSensorRecorderSensorDataRequestById setMetaIdentifier:];
```
