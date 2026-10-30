# `SAPersistenceStore`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _monitoringSessionRecord;
@"NSDate" _persistenceTimestamp;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_monitoringSessionRecord) monitoringSessionRecord;
@property (T@"NSDate",&,N,V_persistenceTimestamp) persistenceTimestamp;
```

## Class methods

```
+[SAPersistenceStore supportsSecureCoding];
```

## Instance methods

```
-[SAPersistenceStore encodeWithCoder:];
-[SAPersistenceStore initWithCoder:];
-[SAPersistenceStore isEqual:];
-[SAPersistenceStore monitoringSessionRecord];
-[SAPersistenceStore persistenceTimestamp];
-[SAPersistenceStore setMonitoringSessionRecord:];
-[SAPersistenceStore setPersistenceTimestamp:];
```
