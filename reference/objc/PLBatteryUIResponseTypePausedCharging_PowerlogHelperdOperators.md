# `PLBatteryUIResponseTypePausedCharging`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 29 instance variables, 33 properties, 73 instance methods, 0 class methods

## Instance variables

```
B _wasCameraStreaming;
B _wasTLCWithCameraStreaming;
B _isFixedCharge;
B _isCharging;
B _externalConnected;
i _intervalStateSmartCharging;
i _intervalStateCEC;
i _intervalStateTLC;
i _intervalStateFixedCharging;
i _intervalStateChargingSpeed;
i _pausedChargingState;
@"PLBatteryUIResponderService" _responderService;
@"PLEntry" _lastSmartChargingEntry;
@"PowerUISmartChargeClient" _smartChargingClient;
@"NSDate" _smartChargingDeadline;
@"PowerUISmartChargeClient" _cleanEnergyChargingClient;
@"NSDate" _cleanEnergyChargingDeadline;
@"PLEntry" _lastCameraStreamingEntry;
@"PLEntry" _lastTLCWithCameraStreamingEntry;
@"PLEntry" _lastEntry;
@"NSDate" _start;
@"NSDate" _end;
@"PLCoreStorage" _storage;
@"NSNumber" _fixedChargingLimit;
@"NSNumber" _currentChargeLevel;
@"PLEntry" _lastConnectedEntry;
@"NSString" _chargingStateIntervalsEntryKey;
@"NSMutableDictionary" _resultDictionary;
{_PLTimeIntervalRange="location"d"length"d} _range;
```

## Properties

```
@property (T@"PLEntry",&,V_lastSmartChargingEntry) lastSmartChargingEntry;
@property (Ti,V_intervalStateSmartCharging) intervalStateSmartCharging;
@property (T@"PowerUISmartChargeClient",&,V_smartChargingClient) smartChargingClient;
@property (T@"NSDate",&,V_smartChargingDeadline) smartChargingDeadline;
@property (T@"PowerUISmartChargeClient",&,V_cleanEnergyChargingClient) cleanEnergyChargingClient;
@property (Ti,V_intervalStateCEC) intervalStateCEC;
@property (T@"NSDate",&,V_cleanEnergyChargingDeadline) cleanEnergyChargingDeadline;
@property (T@"PLEntry",&,V_lastCameraStreamingEntry) lastCameraStreamingEntry;
@property (TB,V_wasCameraStreaming) wasCameraStreaming;
@property (T@"PLEntry",&,V_lastTLCWithCameraStreamingEntry) lastTLCWithCameraStreamingEntry;
@property (TB,V_wasTLCWithCameraStreaming) wasTLCWithCameraStreaming;
@property (T@"PLEntry",&,V_lastEntry) lastEntry;
@property (Ti,V_intervalStateTLC) intervalStateTLC;
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (T{_PLTimeIntervalRange=dd},V_range) range;
@property (T@"PLCoreStorage",&,V_storage) storage;
@property (TB,V_isFixedCharge) isFixedCharge;
@property (Ti,V_intervalStateFixedCharging) intervalStateFixedCharging;
@property (T@"NSNumber",&,V_fixedChargingLimit) fixedChargingLimit;
@property (Ti,V_intervalStateChargingSpeed) intervalStateChargingSpeed;
@property (TB,V_isCharging) isCharging;
@property (TB,V_externalConnected) externalConnected;
@property (T@"NSNumber",&,V_currentChargeLevel) currentChargeLevel;
@property (T@"PLEntry",&,V_lastConnectedEntry) lastConnectedEntry;
@property (T@"NSString",&,V_chargingStateIntervalsEntryKey) chargingStateIntervalsEntryKey;
@property (Ti,V_pausedChargingState) pausedChargingState;
@property (T@"NSMutableDictionary",&,V_resultDictionary) resultDictionary;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypePausedCharging isCharging];
-[PLBatteryUIResponseTypePausedCharging configure:];
-[PLBatteryUIResponseTypePausedCharging dependencies];
-[PLBatteryUIResponseTypePausedCharging range];
-[PLBatteryUIResponseTypePausedCharging setIsCharging:];
-[PLBatteryUIResponseTypePausedCharging start];
-[PLBatteryUIResponseTypePausedCharging end];
-[PLBatteryUIResponseTypePausedCharging setRange:];
-[PLBatteryUIResponseTypePausedCharging getState:];
-[PLBatteryUIResponseTypePausedCharging coalesce];
-[PLBatteryUIResponseTypePausedCharging storage];
-[PLBatteryUIResponseTypePausedCharging setEnd:];
-[PLBatteryUIResponseTypePausedCharging result];
-[PLBatteryUIResponseTypePausedCharging setStart:];
-[PLBatteryUIResponseTypePausedCharging setStorage:];
-[PLBatteryUIResponseTypePausedCharging run];
-[PLBatteryUIResponseTypePausedCharging resultDictionary];
-[PLBatteryUIResponseTypePausedCharging setLastEntry:];
-[PLBatteryUIResponseTypePausedCharging configureState:];
-[PLBatteryUIResponseTypePausedCharging lastTLCWithCameraStreamingEntry];
-[PLBatteryUIResponseTypePausedCharging setCleanEnergyChargingDeadline:];
-[PLBatteryUIResponseTypePausedCharging configureTLCWithCameraStreaming];
-[PLBatteryUIResponseTypePausedCharging getChargingData];
-[PLBatteryUIResponseTypePausedCharging chargingStateIntervalsEntryKey];
-[PLBatteryUIResponseTypePausedCharging cleanEnergyChargingClient];
-[PLBatteryUIResponseTypePausedCharging cleanEnergyChargingDeadline];
-[PLBatteryUIResponseTypePausedCharging configureCameraStreaming];
-[PLBatteryUIResponseTypePausedCharging currentChargeLevel];
-[PLBatteryUIResponseTypePausedCharging externalConnected];
-[PLBatteryUIResponseTypePausedCharging fixedChargingLimit];
-[PLBatteryUIResponseTypePausedCharging getCameraStreamingState];
-[PLBatteryUIResponseTypePausedCharging getTLCWithCameraStreamingState];
-[PLBatteryUIResponseTypePausedCharging intervalStateCEC];
-[PLBatteryUIResponseTypePausedCharging intervalStateChargingSpeed];
-[PLBatteryUIResponseTypePausedCharging intervalStateFixedCharging];
-[PLBatteryUIResponseTypePausedCharging intervalStateSmartCharging];
-[PLBatteryUIResponseTypePausedCharging intervalStateTLC];
-[PLBatteryUIResponseTypePausedCharging isFixedCharge];
-[PLBatteryUIResponseTypePausedCharging lastCameraStreamingEntry];
-[PLBatteryUIResponseTypePausedCharging lastConnectedEntry];
-[PLBatteryUIResponseTypePausedCharging lastEntry];
-[PLBatteryUIResponseTypePausedCharging lastSmartChargingEntry];
-[PLBatteryUIResponseTypePausedCharging pausedChargingState];
-[PLBatteryUIResponseTypePausedCharging responderService];
-[PLBatteryUIResponseTypePausedCharging setChargingPausedStates];
-[PLBatteryUIResponseTypePausedCharging setChargingStateIntervalsEntryKey:];
-[PLBatteryUIResponseTypePausedCharging setCleanEnergyChargingClient:];
-[PLBatteryUIResponseTypePausedCharging setCurrentChargeLevel:];
-[PLBatteryUIResponseTypePausedCharging setCurrentlyChargingStates];
-[PLBatteryUIResponseTypePausedCharging setExternalConnected:];
-[PLBatteryUIResponseTypePausedCharging setFixedChargingLimit:];
-[PLBatteryUIResponseTypePausedCharging setIntervalStateCEC:];
-[PLBatteryUIResponseTypePausedCharging setIntervalStateChargingSpeed:];
-[PLBatteryUIResponseTypePausedCharging setIntervalStateFixedCharging:];
-[PLBatteryUIResponseTypePausedCharging setIntervalStateSmartCharging:];
-[PLBatteryUIResponseTypePausedCharging setIntervalStateTLC:];
-[PLBatteryUIResponseTypePausedCharging setIsFixedCharge:];
-[PLBatteryUIResponseTypePausedCharging setLastCameraStreamingEntry:];
-[PLBatteryUIResponseTypePausedCharging setLastConnectedEntry:];
-[PLBatteryUIResponseTypePausedCharging setLastSmartChargingEntry:];
-[PLBatteryUIResponseTypePausedCharging setLastTLCWithCameraStreamingEntry:];
-[PLBatteryUIResponseTypePausedCharging setPausedChargingState:];
-[PLBatteryUIResponseTypePausedCharging setResponderService:];
-[PLBatteryUIResponseTypePausedCharging setResultDictionary:];
-[PLBatteryUIResponseTypePausedCharging setSmartChargingClient:];
-[PLBatteryUIResponseTypePausedCharging setSmartChargingDeadline:];
-[PLBatteryUIResponseTypePausedCharging setTerminatedChargingStates];
-[PLBatteryUIResponseTypePausedCharging setWasCameraStreaming:];
-[PLBatteryUIResponseTypePausedCharging setWasTLCWithCameraStreaming:];
-[PLBatteryUIResponseTypePausedCharging smartChargingClient];
-[PLBatteryUIResponseTypePausedCharging smartChargingDeadline];
-[PLBatteryUIResponseTypePausedCharging wasCameraStreaming];
-[PLBatteryUIResponseTypePausedCharging wasTLCWithCameraStreaming];
```
