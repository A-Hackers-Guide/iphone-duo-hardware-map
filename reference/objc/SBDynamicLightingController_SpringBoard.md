# `SBDynamicLightingController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightCoordinatorObserver`, `SBFThermalConditionObserver`
- 8 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"SBBacklightCoordinator" _backlightCoordinator;
@"NSOperationQueue" _queue;
@"NSObject<OS_dispatch_queue>" _underlyingUpdateQueue;
@"SBThermalController" _thermalController;
@"LSSAssertion" _disableSpecularsForHomeScreenDefaultAssertion;
@"LSSAssertion" _pauseDynamicLightingAssertion;
@"LSSAssertion" _lowPowerDynamicLightingAssertion;
@"LSSAssertion" _criticalThermalLevelDynamicLightingAssertion;
```

## Properties

```
@property (T@"LSSAssertion",R,N,V_pauseDynamicLightingAssertion) pauseDynamicLightingAssertion;
@property (T@"LSSAssertion",R,N,V_lowPowerDynamicLightingAssertion) lowPowerDynamicLightingAssertion;
@property (T@"LSSAssertion",R,N,V_criticalThermalLevelDynamicLightingAssertion) criticalThermalLevelDynamicLightingAssertion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDynamicLightingController dealloc];
-[SBDynamicLightingController didChangeThermalLevel:];
-[SBDynamicLightingController thermalBlockStatusChanged:];
-[SBDynamicLightingController backlightCoordinator:didUpdateAggregateBacklightState:fromSource:];
-[SBDynamicLightingController backlightCoordinator:willUpdateAggregateBacklightState:fromSource:];
-[SBDynamicLightingController criticalThermalLevelDynamicLightingAssertion];
-[SBDynamicLightingController didChangePowerMode:];
-[SBDynamicLightingController disableEffectsForReason:];
-[SBDynamicLightingController initWithBacklightCoordinator:thermalController:];
-[SBDynamicLightingController lowPowerDynamicLightingAssertion];
-[SBDynamicLightingController pauseDynamicLightingAssertion];
```
