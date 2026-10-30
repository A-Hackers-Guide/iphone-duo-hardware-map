# `SBThermalController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFThermalBlockProvider`
- 16 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _samplingToken;
i _hotToken;
Q _hotLevel;
i _coldToken;
Q _coldLevel;
i _sunToken;
Q _sunLevel;
q _level;
B _inSunlight;
@"NSHashTable" _observers;
@"SBExternalWifiDefaults" _networkDefaults;
@"SBThermalDefaults" _thermalDefaults;
@"SBSecurityDefaults" _securityDefaults;
@"SBTelephonyManager" _telephonyManager;
@"SBWiFiManager" _wifiManager;
@"SBSceneManager" _sceneManager;
```

## Properties

```
@property (Tq,R,N,V_level) level;
@property (TB,R,N,GisInSunlight,V_inSunlight) inSunlight;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBThermalController logThermalEvent:];
```

## Instance methods

```
-[SBThermalController dealloc];
-[SBThermalController level];
-[SBThermalController isThermalBlocked];
-[SBThermalController description];
-[SBThermalController initWithSceneManager:];
-[SBThermalController addThermalObserver:];
-[SBThermalController removeThermalObserver:];
-[SBThermalController startListeningForThermalEventsWithTelephonyManager:wifiManager:];
-[SBThermalController _isBlocked];
-[SBThermalController _respondToCurrentThermalCondition];
-[SBThermalController _setBlocked:];
-[SBThermalController _updateThermalJetsamCPUSamplingState];
-[SBThermalController isInSunlight];
```
