# `SecTapToRadar`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 23 instance methods, 5 class methods

## Instance variables

```
@"NSString" _componentID;
@"NSString" _componentName;
@"NSString" _componentVersion;
@"NSString" _reason;
@"NSString" _alert;
@"NSString" _radarDescription;
@"NSString" _radarnumber;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSDate" _created;
```

## Properties

```
@property (T@"NSString",&,V_alert) alert;
@property (T@"NSString",&,V_radarDescription) radarDescription;
@property (T@"NSString",&,V_radarnumber) radarnumber;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@"NSDate",&,V_created) created;
@property (T@"NSString",&,N,V_componentID) componentID;
@property (T@"NSString",&,N,V_componentName) componentName;
@property (T@"NSString",&,N,V_componentVersion) componentVersion;
@property (T@"NSString",&,N,V_reason) reason;
```

## Class methods

```
+[SecTapToRadar triggerTapToRadar:];
+[SecTapToRadar askUserIfTTR:];
+[SecTapToRadar disableTTRsEntirely];
+[SecTapToRadar isRateLimited:];
+[SecTapToRadar keyname:];
```

## Instance methods

```
-[SecTapToRadar alert];
-[SecTapToRadar created];
-[SecTapToRadar trigger];
-[SecTapToRadar componentName];
-[SecTapToRadar queue];
-[SecTapToRadar setReason:];
-[SecTapToRadar setCreated:];
-[SecTapToRadar setAlert:];
-[SecTapToRadar isRateLimited];
-[SecTapToRadar reason];
-[SecTapToRadar setQueue:];
-[SecTapToRadar setRadarnumber:];
-[SecTapToRadar setComponentID:];
-[SecTapToRadar clearRetryTimestamp];
-[SecTapToRadar componentID];
-[SecTapToRadar componentVersion];
-[SecTapToRadar initTapToRadar:description:radar:];
-[SecTapToRadar radarDescription];
-[SecTapToRadar radarnumber];
-[SecTapToRadar setComponentName:];
-[SecTapToRadar setComponentVersion:];
-[SecTapToRadar setRadarDescription:];
-[SecTapToRadar updateRetryTimestamp];
```
