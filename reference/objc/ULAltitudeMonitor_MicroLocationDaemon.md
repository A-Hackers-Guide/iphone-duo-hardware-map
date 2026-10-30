# `ULAltitudeMonitor`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ULEventMonitor`
- Protocols: `ULAltitudeProviderDelegate`
- 1 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"ULAltitudeProvider" _altitudeProvider;
```

## Properties

```
@property (T@"ULAltitudeProvider",&,N,V_altitudeProvider) altitudeProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULAltitudeMonitor isAltitudeAvailable];
```

## Instance methods

```
-[ULAltitudeMonitor stopMonitoring:];
-[ULAltitudeMonitor init];
-[ULAltitudeMonitor dealloc];
-[ULAltitudeMonitor startMonitoring:];
-[ULAltitudeMonitor _calculateIsUpToDateForAltitudeTimestamp:];
-[ULAltitudeMonitor altitudeProvider];
-[ULAltitudeMonitor didReceiveAltitudeErrorWithSender:altitudeStatus:error:date:];
-[ULAltitudeMonitor didReceiveAltitudeProviderWithSender:isAvailable:];
-[ULAltitudeMonitor didReceiveAltitudeUpdateWithSender:altitudeStatus:uuid:];
-[ULAltitudeMonitor setAltitudeProvider:];
```
