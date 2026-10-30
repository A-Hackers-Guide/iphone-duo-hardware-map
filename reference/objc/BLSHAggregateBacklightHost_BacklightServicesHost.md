# `BLSHAggregateBacklightHost`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightHostObserving`, `BLSHBacklightHostInternalTelemetrySource`, `BLSBacklightProxy`, `BLSHBacklightHostObservable_Private`
- 12 instance variables, 17 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _backlightHosts;
@"NSMapTable" _lock_observers;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
q _lock_backlightState;
q _lock_willTransitionBacklightState;
q _lock_displayMode;
q _lock_targetDisplayMode;
q _lock_flipbookState;
B _lock_alwaysOnEnabled;
Q _lock_aggregateStateChangeTimestamp;
B _deviceSupportsAlwaysOn;
@"<BLSDisplay>" _display;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<BLSHBacklightHostTelemetryDelegate>",W) internalTelemetryDelegate;
@property (T@"<BLSHBacklightHostTelemetryDelegate>",W) telemetryDelegate;
@property (Tq,R,N) backlightDisplayMode;
@property (TQ,R,N) backlightStateChangeTimestamp;
@property (T@"NSString",R,C,N) backlightStateDescription;
@property (Tq,R,N) backlightState;
@property (Tq,R,N) flipbookState;
@property (TB,R,N,GisTransitioning) transitioning;
@property (TB,R,N,GisAlwaysOnEnabled) alwaysOnEnabled;
@property (TB,R,N) deviceSupportsAlwaysOn;
@property (T@"<BLSDisplay>",R,N,V_display) display;
@property (Tq,R,N) settledBacklightState;
@property (Tq,R,N) targetBacklightDisplayMode;
```

## Class methods

```
+[BLSHAggregateBacklightHost aggregateHostWithBacklightHosts:];
```

## Instance methods

```
-[BLSHAggregateBacklightHost backlight:didCompleteUpdateToState:forEvents:abortedEvents:];
-[BLSHAggregateBacklightHost setTelemetryDelegate:];
-[BLSHAggregateBacklightHost backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:];
-[BLSHAggregateBacklightHost display];
-[BLSHAggregateBacklightHost deviceSupportsAlwaysOn];
-[BLSHAggregateBacklightHost backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:];
-[BLSHAggregateBacklightHost setInternalTelemetryDelegate:];
-[BLSHAggregateBacklightHost backlightStateChangeTimestamp];
-[BLSHAggregateBacklightHost isAlwaysOnEnabled];
-[BLSHAggregateBacklightHost backlightDisplayMode];
-[BLSHAggregateBacklightHost internalTelemetryDelegate];
-[BLSHAggregateBacklightHost removeObserver:];
-[BLSHAggregateBacklightHost isTransitioning];
-[BLSHAggregateBacklightHost telemetryDelegate];
-[BLSHAggregateBacklightHost performChangeRequest:];
-[BLSHAggregateBacklightHost dealloc];
-[BLSHAggregateBacklightHost flipbookState];
-[BLSHAggregateBacklightHost backlightStateDescription];
-[BLSHAggregateBacklightHost addObserver:];
-[BLSHAggregateBacklightHost backlightState];
-[BLSHAggregateBacklightHost backlight:performingEvent:];
-[BLSHAggregateBacklightHost backlight:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:];
-[BLSHAggregateBacklightHost settledBacklightState];
-[BLSHAggregateBacklightHost targetBacklightDisplayMode];
-[BLSHAggregateBacklightHost observesDeactivation];
-[BLSHAggregateBacklightHost observesPerformingAllEvents];
-[BLSHAggregateBacklightHost backlight:didChangeAlwaysOnEnabled:];
-[BLSHAggregateBacklightHost backlight:didCompleteUpdateToFlipbookState:forEvents:abortedEvents:];
-[BLSHAggregateBacklightHost observesActivation];
-[BLSHAggregateBacklightHost backlightHost:willTransitionToState:forEvent:];
-[BLSHAggregateBacklightHost addObserver:forBacklight:];
-[BLSHAggregateBacklightHost observesDidUpdateVisualContents];
-[BLSHAggregateBacklightHost observesBlankingChanges];
-[BLSHAggregateBacklightHost observesUpdateToDisplayMode];
```
