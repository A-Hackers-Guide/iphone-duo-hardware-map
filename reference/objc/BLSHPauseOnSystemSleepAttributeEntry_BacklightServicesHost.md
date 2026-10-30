# `BLSHPauseOnSystemSleepAttributeEntry`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHLocalAssertionAttributeHandlerEntry`, `SWSystemSleepObserver`
- 6 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_invalidated;
B _lock_paused;
@"BLSAttribute" _attribute;
@"<BLSAssertionServiceResponding>" _assertion;
@"<BLSHAssertionAttributeHandlerService>" _service;
```

## Properties

```
@property (T@"BLSAttribute",R,W,N,V_attribute) attribute;
@property (T@"<BLSAssertionServiceResponding>",R,W,N,V_assertion) assertion;
@property (T@"<BLSHAssertionAttributeHandlerService>",R,W,N,V_service) service;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHPauseOnSystemSleepAttributeEntry activateForAttribute:fromAssertion:forService:attributeHandler:];
```

## Instance methods

```
-[BLSHPauseOnSystemSleepAttributeEntry systemSleepMonitor:prepareForSleepWithCompletion:];
-[BLSHPauseOnSystemSleepAttributeEntry assertion];
-[BLSHPauseOnSystemSleepAttributeEntry systemSleepMonitorWillWakeFromSleep:];
-[BLSHPauseOnSystemSleepAttributeEntry invalidate];
-[BLSHPauseOnSystemSleepAttributeEntry service];
-[BLSHPauseOnSystemSleepAttributeEntry attribute];
-[BLSHPauseOnSystemSleepAttributeEntry systemSleepMonitorSleepRequestAborted:];
-[BLSHPauseOnSystemSleepAttributeEntry systemSleepMonitor:sleepRequestedWithResult:];
-[BLSHPauseOnSystemSleepAttributeEntry initForAttribute:fromAssertion:forService:];
-[BLSHPauseOnSystemSleepAttributeEntry reactivateIfPossible];
```
