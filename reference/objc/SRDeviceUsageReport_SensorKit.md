# `SRDeviceUsageReport`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `SRSampling`, `NSCopying`
- 15 instance variables, 22 properties, 44 instance methods, 3 class methods

## Instance variables

```
d _duration;
q _totalScreenWakes;
q _totalUnlocks;
d _totalUnlockDuration;
@"NSString" _version;
@"NSMutableDictionary" _mutableApplicationUsageByCategory;
@"NSMutableDictionary" _mutableNotificationUsageByCategory;
@"NSMutableDictionary" _mutableWebUsageByCategory;
@"NSMutableArray" __mutableMotionActivities;
@"NSMutableArray" __mutableActivityLevels;
@"NSMutableDictionary" __reportApplicationIdentifierByBundleIdentifier;
d _startTime;
d _totalScreenWakeDuration;
d __totalChargingDuration;
d __firstAppLaunchTimeRelativeToInterval;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_mutableApplicationUsageByCategory) mutableApplicationUsageByCategory;
@property (T@"NSMutableDictionary",&,V_mutableNotificationUsageByCategory) mutableNotificationUsageByCategory;
@property (T@"NSMutableDictionary",&,V_mutableWebUsageByCategory) mutableWebUsageByCategory;
@property (T@"NSMutableArray",&,V__mutableMotionActivities) _mutableMotionActivities;
@property (T@"NSMutableArray",&,V__mutableActivityLevels) _mutableActivityLevels;
@property (T@"NSMutableDictionary",&,V__reportApplicationIdentifierByBundleIdentifier) _reportApplicationIdentifierByBundleIdentifier;
@property (Td,V_startTime) startTime;
@property (Td,V_duration) duration;
@property (Tq,V_totalScreenWakes) totalScreenWakes;
@property (Td,V_totalScreenWakeDuration) totalScreenWakeDuration;
@property (Tq,V_totalUnlocks) totalUnlocks;
@property (Td,V_totalUnlockDuration) totalUnlockDuration;
@property (Td,V__totalChargingDuration) _totalChargingDuration;
@property (T@"NSString",C,N,V_version) version;
@property (Td,V__firstAppLaunchTimeRelativeToInterval) _firstAppLaunchTimeRelativeToInterval;
@property (T@"NSDictionary",R,C) applicationUsageByCategory;
@property (T@"NSDictionary",R,C) notificationUsageByCategory;
@property (T@"NSDictionary",R,C) webUsageByCategory;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRDeviceUsageReport supportsSecureCoding];
+[SRDeviceUsageReport initialize];
+[SRDeviceUsageReport deviceUsageReportWithInterval:];
```

## Instance methods

```
-[SRDeviceUsageReport startTime];
-[SRDeviceUsageReport dealloc];
-[SRDeviceUsageReport version];
-[SRDeviceUsageReport duration];
-[SRDeviceUsageReport setStartTime:];
-[SRDeviceUsageReport encodeWithCoder:];
-[SRDeviceUsageReport description];
-[SRDeviceUsageReport initWithCoder:];
-[SRDeviceUsageReport setVersion:];
-[SRDeviceUsageReport setDuration:];
-[SRDeviceUsageReport copyWithZone:];
-[SRDeviceUsageReport isEqual:];
-[SRDeviceUsageReport binarySampleRepresentation];
-[SRDeviceUsageReport initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRDeviceUsageReport sr_dictionaryRepresentation];
-[SRDeviceUsageReport setTotalUnlockDuration:];
-[SRDeviceUsageReport setTotalUnlocks:];
-[SRDeviceUsageReport totalUnlockDuration];
-[SRDeviceUsageReport totalUnlocks];
-[SRDeviceUsageReport _activityLevels];
-[SRDeviceUsageReport _firstAppLaunchTimeRelativeToInterval];
-[SRDeviceUsageReport _motionActivities];
-[SRDeviceUsageReport _mutableActivityLevels];
-[SRDeviceUsageReport _mutableMotionActivities];
-[SRDeviceUsageReport _reportApplicationIdentifierByBundleIdentifier];
-[SRDeviceUsageReport _totalChargingDuration];
-[SRDeviceUsageReport applicationUsageByCategory];
-[SRDeviceUsageReport mutableApplicationUsageByCategory];
-[SRDeviceUsageReport mutableNotificationUsageByCategory];
-[SRDeviceUsageReport mutableWebUsageByCategory];
-[SRDeviceUsageReport notificationUsageByCategory];
-[SRDeviceUsageReport setMutableApplicationUsageByCategory:];
-[SRDeviceUsageReport setMutableNotificationUsageByCategory:];
-[SRDeviceUsageReport setMutableWebUsageByCategory:];
-[SRDeviceUsageReport setTotalScreenWakeDuration:];
-[SRDeviceUsageReport setTotalScreenWakes:];
-[SRDeviceUsageReport set_firstAppLaunchTimeRelativeToInterval:];
-[SRDeviceUsageReport set_mutableActivityLevels:];
-[SRDeviceUsageReport set_mutableMotionActivities:];
-[SRDeviceUsageReport set_reportApplicationIdentifierByBundleIdentifier:];
-[SRDeviceUsageReport set_totalChargingDuration:];
-[SRDeviceUsageReport totalScreenWakeDuration];
-[SRDeviceUsageReport totalScreenWakes];
-[SRDeviceUsageReport webUsageByCategory];
```
