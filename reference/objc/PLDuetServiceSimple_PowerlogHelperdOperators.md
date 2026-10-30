# `PLDuetServiceSimple`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLDuetServiceImpl`
- 4 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _isCharging;
@"NSMutableDictionary" _bundleIDToState;
@"PLXPCListenerOperatorComposition" _resetListener;
@"PLEntryNotificationOperatorComposition" _chargingListener;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_bundleIDToState) bundleIDToState;
@property (T@"PLXPCListenerOperatorComposition",&,V_resetListener) resetListener;
@property (T@"PLEntryNotificationOperatorComposition",&,V_chargingListener) chargingListener;
@property (TB,V_isCharging) isCharging;
```

## Instance methods

```
-[PLDuetServiceSimple isCharging];
-[PLDuetServiceSimple setIsCharging:];
-[PLDuetServiceSimple init];
-[PLDuetServiceSimple bundleIDToState];
-[PLDuetServiceSimple didReceiveReset];
-[PLDuetServiceSimple didReceiveStopEventWithPayload:];
-[PLDuetServiceSimple capUtilizationInSeconds:withUpperBoundInError:withCapInError:withCappedUpperBound:];
-[PLDuetServiceSimple chargingListener];
-[PLDuetServiceSimple didReceiveStartEventWithPayload:];
-[PLDuetServiceSimple initOperatorDependancies:];
-[PLDuetServiceSimple numCPUSecondsForBundleID:];
-[PLDuetServiceSimple numCPUSecondsForPid:];
-[PLDuetServiceSimple resetListener];
-[PLDuetServiceSimple setBundleIDToState:];
-[PLDuetServiceSimple setChargingListener:];
-[PLDuetServiceSimple setResetListener:];
```
