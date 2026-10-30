# `IOAccessoryLdcmHealthClass`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 13 instance variables, 13 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _isHealthy;
I _version;
Q _leakagePassedCount;
Q _dryCount;
Q _wetCount;
Q _overVoltageCount;
Q _outOfProfileCount;
Q _lastSeenTimestamp;
Q _rsvd0;
Q _rsvd1;
Q _rsvd2;
Q _rsvd3;
Q _overVoltageTimestamp;
```

## Properties

```
@property (TI,V_version) version;
@property (TB,V_isHealthy) isHealthy;
@property (TQ,V_leakagePassedCount) leakagePassedCount;
@property (TQ,V_dryCount) dryCount;
@property (TQ,V_wetCount) wetCount;
@property (TQ,V_overVoltageCount) overVoltageCount;
@property (TQ,V_outOfProfileCount) outOfProfileCount;
@property (TQ,V_lastSeenTimestamp) lastSeenTimestamp;
@property (TQ,V_rsvd0) rsvd0;
@property (TQ,V_rsvd1) rsvd1;
@property (TQ,V_rsvd2) rsvd2;
@property (TQ,V_rsvd3) rsvd3;
@property (TQ,V_overVoltageTimestamp) overVoltageTimestamp;
```

## Class methods

```
+[IOAccessoryLdcmHealthClass supportsSecureCoding];
```

## Instance methods

```
-[IOAccessoryLdcmHealthClass init];
-[IOAccessoryLdcmHealthClass version];
-[IOAccessoryLdcmHealthClass encodeWithCoder:];
-[IOAccessoryLdcmHealthClass initWithCoder:];
-[IOAccessoryLdcmHealthClass setVersion:];
-[IOAccessoryLdcmHealthClass lastSeenTimestamp];
-[IOAccessoryLdcmHealthClass setLastSeenTimestamp:];
-[IOAccessoryLdcmHealthClass dryCount];
-[IOAccessoryLdcmHealthClass isHealthy];
-[IOAccessoryLdcmHealthClass leakagePassedCount];
-[IOAccessoryLdcmHealthClass outOfProfileCount];
-[IOAccessoryLdcmHealthClass overVoltageCount];
-[IOAccessoryLdcmHealthClass overVoltageTimestamp];
-[IOAccessoryLdcmHealthClass rsvd0];
-[IOAccessoryLdcmHealthClass rsvd1];
-[IOAccessoryLdcmHealthClass rsvd2];
-[IOAccessoryLdcmHealthClass rsvd3];
-[IOAccessoryLdcmHealthClass setDryCount:];
-[IOAccessoryLdcmHealthClass setIsHealthy:];
-[IOAccessoryLdcmHealthClass setLeakagePassedCount:];
-[IOAccessoryLdcmHealthClass setOutOfProfileCount:];
-[IOAccessoryLdcmHealthClass setOverVoltageCount:];
-[IOAccessoryLdcmHealthClass setOverVoltageTimestamp:];
-[IOAccessoryLdcmHealthClass setRsvd0:];
-[IOAccessoryLdcmHealthClass setRsvd1:];
-[IOAccessoryLdcmHealthClass setRsvd2:];
-[IOAccessoryLdcmHealthClass setRsvd3:];
-[IOAccessoryLdcmHealthClass setWetCount:];
-[IOAccessoryLdcmHealthClass wetCount];
```
