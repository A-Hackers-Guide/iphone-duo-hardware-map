# `BLSXPCBacklightProxy`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSBacklightProxy`, `BLSXPCBacklightProxyClientInterface`, `BSInvalidatable`
- 17 instance variables, 10 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _lock_observers;
@"BSServiceInitiatingConnection" _connection;
@"BLSDisplayReference" _display;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
i _lock_observingDidCompleteUpdateToStateCount;
i _lock_observingEventsArrayCount;
i _lock_observingDidChangeAlwaysOnEnabledCount;
i _lock_observingActivatingWithEventCount;
i _lock_observingDeactivatingWithEventCount;
i _lock_observingPerformingEventCount;
q _lock_backlightState;
B _lock_isBacklightStateCached;
B _lock_isAlwaysOnEnabled;
B _lock_isAlwaysOnEnabledCached;
B _lock_deviceSupportsAlwaysOn;
B _lock_deviceSupportsAlwaysOnCached;
B _lock_invalidated;
```

## Properties

```
@property (Tq,R,N) backlightState;
@property (Tq,R,N) flipbookState;
@property (TB,R,N,GisTransitioning) transitioning;
@property (TB,R,N,GisAlwaysOnEnabled) alwaysOnEnabled;
@property (TB,R,N) deviceSupportsAlwaysOn;
@property (T@"<BLSDisplay>",R,N) display;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSXPCBacklightProxy display];
-[BLSXPCBacklightProxy deviceSupportsAlwaysOn];
-[BLSXPCBacklightProxy performingEvent:];
-[BLSXPCBacklightProxy isAlwaysOnEnabled];
-[BLSXPCBacklightProxy initForDisplay:];
-[BLSXPCBacklightProxy didCompleteUpdateToState:forEvents:abortedEvents:];
-[BLSXPCBacklightProxy removeObserver:];
-[BLSXPCBacklightProxy isTransitioning];
-[BLSXPCBacklightProxy performChangeRequest:];
-[BLSXPCBacklightProxy dealloc];
-[BLSXPCBacklightProxy flipbookState];
-[BLSXPCBacklightProxy addObserver:];
-[BLSXPCBacklightProxy invalidate];
-[BLSXPCBacklightProxy backlightState];
-[BLSXPCBacklightProxy didChangeAlwaysOnEnabled:];
-[BLSXPCBacklightProxy addObserver:forBacklight:];
```
