# `ULOdometryMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- Protocols: `ULOdometryProviderDelegate`
- 2 instance variables, 6 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"ULOdometryProvider" _odometryProvider;
q _sourceType;
```

## Properties

```
@property (T@"ULOdometryProvider",&,N,V_odometryProvider) odometryProvider;
@property (Tq,R,N,V_sourceType) sourceType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULOdometryMonitor isCMOdometryAvailable];
+[ULOdometryMonitor isNPDROdometryAvailable];
```

## Instance methods

```
-[ULOdometryMonitor stopMonitoring:];
-[ULOdometryMonitor init];
-[ULOdometryMonitor sourceType];
-[ULOdometryMonitor didReceiveOdometryUpdateWithSender:odometryStatus:uuid:];
-[ULOdometryMonitor requestNPDRUpdate];
-[ULOdometryMonitor didReceiveOdometryErrorWithSender:odometryStatus:error:date:];
-[ULOdometryMonitor didReceiveOdometryTimestampWithSender:timestamp:];
-[ULOdometryMonitor _calculateIsUpToDateForOdometryTimestamp:];
-[ULOdometryMonitor didReceiveOdometryProviderWithSender:isAvailable:];
-[ULOdometryMonitor odometryProvider];
-[ULOdometryMonitor setOdometryProvider:];
-[ULOdometryMonitor startMonitoring:];
-[ULOdometryMonitor injectOdometryFrame:];
```
