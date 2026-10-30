# `BLSHTelemetryService`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHTelemetryServiceSending`
- 2 instance variables, 4 properties, 4 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableDictionary" _lock_powerLogIdentifiersByKey;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHTelemetryService sharedTelemetryService];
```

## Instance methods

```
-[BLSHTelemetryService init];
-[BLSHTelemetryService _powerLogIdentifierForSubsystem:category:];
-[BLSHTelemetryService sendAnalyticsEvent:payloadBuilder:];
-[BLSHTelemetryService sendPowerLogTelemetryWithSubsystem:category:payload:];
```
