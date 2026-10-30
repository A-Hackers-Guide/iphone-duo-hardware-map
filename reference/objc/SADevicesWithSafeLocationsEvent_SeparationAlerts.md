# `SADevicesWithSafeLocationsEvent`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OSLogCoding`, `TAEventProtocol`
- 3 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _devices;
@"NSDictionary" _safeLocations;
@"NSDate" _date;
```

## Properties

```
@property (T@"NSDictionary",R,C,N,V_devices) devices;
@property (T@"NSDictionary",R,C,N,V_safeLocations) safeLocations;
@property (T@"NSDate",R,C,N,V_date) date;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SADevicesWithSafeLocationsEvent supportsSecureCoding];
```

## Instance methods

```
-[SADevicesWithSafeLocationsEvent date];
-[SADevicesWithSafeLocationsEvent devices];
-[SADevicesWithSafeLocationsEvent getDate];
-[SADevicesWithSafeLocationsEvent descriptionDictionary];
-[SADevicesWithSafeLocationsEvent encodeWithCoder:];
-[SADevicesWithSafeLocationsEvent description];
-[SADevicesWithSafeLocationsEvent initWithCoder:];
-[SADevicesWithSafeLocationsEvent copyWithZone:];
-[SADevicesWithSafeLocationsEvent isEqual:];
-[SADevicesWithSafeLocationsEvent safeLocations];
-[SADevicesWithSafeLocationsEvent encodeWithOSLogCoder:options:maxLength:];
-[SADevicesWithSafeLocationsEvent initWithDevices:safeLocationUUIDs:date:];
```
