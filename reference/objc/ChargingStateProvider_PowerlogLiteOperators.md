# `ChargingStateProvider`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 11 properties, 45 instance methods, 3 class methods

## Instance variables

```
i _chargingIconographyStateNotifyToken;
i _powerSourceNotifyToken;
i _uisocChangeToken;
i _chargeToFullNotifyToken;
i _chargingStatusOverrideNotifyToken;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSHashTable" _delegates;
B _isLowPowerModeEnabled;
B _isExternallyConnected;
B _isEoc;
B _isPaused;
B _isSlowCharger;
s _chargingState;
i _uisocLevel;
@"<ChargingStateProviderDelegate>" _delegate;
@"NSNumber" _timeEstimateTo80;
@"NSNumber" _timeEstimateToLimit;
@"BIBatteryAnalysisClient" _chargeTimeEstimateClient;
```

## Properties

```
@property (T@"BIBatteryAnalysisClient",&,V_chargeTimeEstimateClient) chargeTimeEstimateClient;
@property (T@"<ChargingStateProviderDelegate>",W,N,V_delegate) delegate;
@property (TB,V_isLowPowerModeEnabled) isLowPowerModeEnabled;
@property (TB,V_isExternallyConnected) isExternallyConnected;
@property (Ti,V_uisocLevel) uisocLevel;
@property (TB,V_isEoc) isEoc;
@property (TB,V_isPaused) isPaused;
@property (TB,V_isSlowCharger) isSlowCharger;
@property (Ts,V_chargingState) chargingState;
@property (T@"NSNumber",&,V_timeEstimateTo80) timeEstimateTo80;
@property (T@"NSNumber",&,V_timeEstimateToLimit) timeEstimateToLimit;
```

## Class methods

```
+[ChargingStateProvider isChargingStatusOverrideEngaged];
+[ChargingStateProvider chargingIconStateDictionary];
+[ChargingStateProvider isChargingIconographySupported];
```

## Instance methods

```
-[ChargingStateProvider setIsLowPowerModeEnabled:];
-[ChargingStateProvider isLowPowerModeEnabled];
-[ChargingStateProvider _refreshTimeEstimates];
-[ChargingStateProvider isPaused];
-[ChargingStateProvider debugDescription];
-[ChargingStateProvider chargingStateChanged];
-[ChargingStateProvider refreshChargeLevel];
-[ChargingStateProvider init];
-[ChargingStateProvider refreshTimeEstimates];
-[ChargingStateProvider overrideTypeWithOriginal:];
-[ChargingStateProvider isMCLEnabled];
-[ChargingStateProvider dealloc];
-[ChargingStateProvider setIsPaused:];
-[ChargingStateProvider areBatteryGaugingAndMCLEnabledWithOverrideStateArray:];
-[ChargingStateProvider computeStates];
-[ChargingStateProvider setUisocLevel:];
-[ChargingStateProvider setChargeTimeEstimateClient:];
-[ChargingStateProvider chargeLevelChanged];
-[ChargingStateProvider setDelegate:];
-[ChargingStateProvider setTimeEstimateToLimit:];
-[ChargingStateProvider isEoc];
-[ChargingStateProvider refreshLowPowerMode];
-[ChargingStateProvider timeEstimateTo80];
-[ChargingStateProvider refreshData];
-[ChargingStateProvider setIsSlowCharger:];
-[ChargingStateProvider isSlowCharger];
-[ChargingStateProvider isExternallyConnected];
-[ChargingStateProvider delegate];
-[ChargingStateProvider didUpdateEstimateFor:newEstimate:error:];
-[ChargingStateProvider setTimeEstimateTo80:];
-[ChargingStateProvider refreshChargingState];
-[ChargingStateProvider refreshPowerSource];
-[ChargingStateProvider timeEstimateToLimit];
-[ChargingStateProvider setIsEoc:];
-[ChargingStateProvider getChargingState];
-[ChargingStateProvider uisocLevel];
-[ChargingStateProvider refreshTimeEstimateForTarget:slowChargerSignal:];
-[ChargingStateProvider chargeTimeEstimateClient];
-[ChargingStateProvider getMostApplicableState:isPaused:];
-[ChargingStateProvider powerSourceChanged];
-[ChargingStateProvider stateCalculation];
-[ChargingStateProvider setChargingState:];
-[ChargingStateProvider lowPowerModeChanged];
-[ChargingStateProvider setIsExternallyConnected:];
-[ChargingStateProvider chargingState];
```
