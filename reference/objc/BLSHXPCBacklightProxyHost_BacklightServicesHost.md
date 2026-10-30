# `BLSHXPCBacklightProxyHost`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightHostObserving`, `BLSXPCBacklightProxyHostInterface`, `BSInvalidatable`
- 16 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"<BLSBacklightProxy>" _localBacklightProxy;
@"<BLSXPCBacklightProxyClientInterface>" _lock_observingClient;
@"BLSDisplayReference" _display;
@"RBSProcessMonitor" _processMonitor;
@"BLSXPCBacklightProxyObserverMask" _lock_observingMask;
i _clientPid;
I _entitlements;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_clientIsTaskScheduled;
B _lock_stateIsStale;
B _lock_valid;
B _lock_observingDidCompleteUpdateToState;
B _lock_observingDidChangeAlwaysOnEnabled;
B _lock_observingActivatingWithEvent;
B _lock_observingDeactivatingWithEvent;
B _lock_observingPerformingEvent;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHXPCBacklightProxyHost backlight:didCompleteUpdateToState:forEvents:abortedEvents:];
-[BLSHXPCBacklightProxyHost deviceSupportsAlwaysOn];
-[BLSHXPCBacklightProxyHost isAlwaysOnEnabled];
-[BLSHXPCBacklightProxyHost backlight:deactivatingWithEvent:];
-[BLSHXPCBacklightProxyHost isTransitioning];
-[BLSHXPCBacklightProxyHost performChangeRequest:];
-[BLSHXPCBacklightProxyHost dealloc];
-[BLSHXPCBacklightProxyHost getBacklightState];
-[BLSHXPCBacklightProxyHost backlight:activatingWithEvent:];
-[BLSHXPCBacklightProxyHost initWithLocalBacklightProxy:peer:display:];
-[BLSHXPCBacklightProxyHost invalidate];
-[BLSHXPCBacklightProxyHost backlight:performingEvent:];
-[BLSHXPCBacklightProxyHost nowObservingWithMask:completion:];
-[BLSHXPCBacklightProxyHost observesDeactivation];
-[BLSHXPCBacklightProxyHost observesPerformingAllEvents];
-[BLSHXPCBacklightProxyHost description];
-[BLSHXPCBacklightProxyHost backlight:didChangeAlwaysOnEnabled:];
-[BLSHXPCBacklightProxyHost getFlipbookState];
-[BLSHXPCBacklightProxyHost observesActivation];
```
