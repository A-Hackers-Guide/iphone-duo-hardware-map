# `SBWakeLogger`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSWakeLoggerProviding`
- 7 instance variables, 11 properties, 20 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _trackingWake;
I _timesyncService;
I _backlightService;
q _homeButtonType;
@"NSMutableDictionary" _wakeSouceToEventDict;
q _activeWakeLoggerSource;
```

## Properties

```
@property (TB,N,V_trackingWake) trackingWake;
@property (Tq,N,V_homeButtonType) homeButtonType;
@property (TI,N,V_timesyncService) timesyncService;
@property (TI,N,V_backlightService) backlightService;
@property (T@"NSMutableDictionary",&,N,V_wakeSouceToEventDict) wakeSouceToEventDict;
@property (Tq,N,V_activeWakeLoggerSource) activeWakeLoggerSource;
@property (T@"NSString",R,C,N) activeWakeSourceDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBWakeLogger sharedInstance];
+[SBWakeLogger sharedInstanceIfExists];
```

## Instance methods

```
-[SBWakeLogger init];
-[SBWakeLogger dealloc];
-[SBWakeLogger homeButtonType];
-[SBWakeLogger setHomeButtonType:];
-[SBWakeLogger timesyncService];
-[SBWakeLogger _lock_wakeDidBegin:];
-[SBWakeLogger activeWakeLoggerSource];
-[SBWakeLogger activeWakeSourceDescription];
-[SBWakeLogger backlightService];
-[SBWakeLogger lockDidBegin];
-[SBWakeLogger setActiveWakeLoggerSource:];
-[SBWakeLogger setBacklightService:];
-[SBWakeLogger setTimesyncService:];
-[SBWakeLogger setTrackingWake:];
-[SBWakeLogger setWakeSouceToEventDict:];
-[SBWakeLogger trackingWake];
-[SBWakeLogger wakeDidBegin:];
-[SBWakeLogger wakeDidEnd];
-[SBWakeLogger wakeMayBegin:withTimestamp:];
-[SBWakeLogger wakeSouceToEventDict];
```
