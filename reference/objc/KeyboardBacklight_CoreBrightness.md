# `KeyboardBacklight`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`, `CBHIDServiceProtocol`
- 57 instance variables, 36 properties, 125 instance methods, 1 class methods

## Instance variables

```
B _muted;
B _keyboardAvailable;
B _manualAdjust;
B _saturated;
B _dimmed;
B _suspend;
B _suspendDimming;
B _userActive;
B _displayOn;
B _clamshellClosed;
f _previousLevelPercentage;
i _numOfBacklightUpdateRetries;
i _currentFadeSpeed;
B _currentEnableState;
f _currentLevel;
f _currentBrightness;
@"HIDDevice" _device;
@"HIDElement" _levelElement;
@"HIDElement" _levelFadeSpeedElement;
@"HIDElement" _enableElement;
@"HIDElement" _enableFadeSpeedElement;
@"NSMutableArray" _alsServiceClients;
Q _activityNotificationHandle;
@"NSMutableDictionary" _properties;
@"NSObject<OS_dispatch_source>" _forceLuxUpdateTimer;
@"NSObject<OS_dispatch_source>" _backlightUpdateTimer;
@"HIDElement" _enableAuthenticationElement;
B _backlightUpdateInProgress;
{mach_timebase_info="numer"I"denom"I} _clockInfo;
i _backlightUpdateFrequency;
Q _lastBacklightUpdate;
Q _backlightUpdateType;
i _turnOnBacklightDelayMS;
B _forceDelayToTurnOnBacklight;
@"NSObject<OS_dispatch_source>" _rampTimer;
{Ramp="start"f"target"f"current"f"startTime"d"duration"d} _ramp;
^{IONotificationPort=} _deviceManagementArrivalNotificationPort;
I _deviceManagementArrivalIterator;
B _builtIn;
B _autoAdjust;
B _hysteresisOn;
i _dimTime;
f _ambientOffset;
f _ambientHighThreshold;
f _ambientLowThreshold;
f _levelPercentage;
f _levelMin;
f _levelMax;
f _levelOff;
i _color;
I _levelUnit;
I _unitExponent;
f _ambientSlope;
f _currentLux;
f _previousLevel;
Q _keyboardID;
@"NSMutableDictionary" _keyboardSpecificPreferences;
```

## Properties

```
@property (Ti,V_dimTime) dimTime;
@property (Tf,V_ambientOffset) ambientOffset;
@property (Tf,R,V_ambientHighThreshold) ambientHighThreshold;
@property (Tf,R,V_ambientLowThreshold) ambientLowThreshold;
@property (TB) userActive;
@property (TB) keyboardAvailable;
@property (T@"HIDDevice",V_device) device;
@property (TB) manualAdjust;
@property (TB,V_autoAdjust) autoAdjust;
@property (Tf,V_levelPercentage) levelPercentage;
@property (Tf,V_levelMin) levelMin;
@property (Tf,V_levelMax) levelMax;
@property (Tf,V_levelOff) levelOff;
@property (Ti,V_color) color;
@property (TI,V_levelUnit) levelUnit;
@property (TI,V_unitExponent) unitExponent;
@property (Tf,R,V_ambientSlope) ambientSlope;
@property (Tf,R) maxUserLevel;
@property (Tf,V_currentLux) currentLux;
@property (TB,V_hysteresisOn) hysteresisOn;
@property (TB) muted;
@property (T@"NSMutableDictionary",&,V_keyboardSpecificPreferences) keyboardSpecificPreferences;
@property (Tf,V_previousLevel) previousLevel;
@property (TB,R) suppressed;
@property (TB) saturated;
@property (TB) suspend;
@property (Tf) brightness;
@property (TB,V_builtIn) builtIn;
@property (TB) dimmed;
@property (TB) clamshellClosed;
@property (TQ,V_keyboardID) keyboardID;
@property (TB,R) supportsAuthentication;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[KeyboardBacklight getHashIDForDevice:];
```

## Instance methods

```
-[KeyboardBacklight setMuted:];
-[KeyboardBacklight copyPropertyForKey:];
-[KeyboardBacklight setProperty:forKey:];
-[KeyboardBacklight setColor:];
-[KeyboardBacklight handleEvent:];
-[KeyboardBacklight addHIDServiceClient:];
-[KeyboardBacklight initWithQueue:];
-[KeyboardBacklight removeHIDServiceClient:];
-[KeyboardBacklight setBacklightLevel:];
-[KeyboardBacklight setDevice:];
-[KeyboardBacklight suspend];
-[KeyboardBacklight timerRoutine:];
-[KeyboardBacklight device];
-[KeyboardBacklight setBrightness:];
-[KeyboardBacklight stop];
-[KeyboardBacklight unitExponent];
-[KeyboardBacklight dealloc];
-[KeyboardBacklight setCurrentLux:];
-[KeyboardBacklight start];
-[KeyboardBacklight brightness];
-[KeyboardBacklight sendNotificationForKey:withValue:];
-[KeyboardBacklight level];
-[KeyboardBacklight handleNotificationForKey:withProperty:];
-[KeyboardBacklight color];
-[KeyboardBacklight setDimmed:];
-[KeyboardBacklight setBuiltIn:];
-[KeyboardBacklight setUserActive:];
-[KeyboardBacklight description];
-[KeyboardBacklight builtIn];
-[KeyboardBacklight supportsAuthentication];
-[KeyboardBacklight currentLux];
-[KeyboardBacklight dimmed];
-[KeyboardBacklight userActive];
-[KeyboardBacklight copyPropertyForKey:withParameter:];
-[KeyboardBacklight muted];
-[KeyboardBacklight saturated];
-[KeyboardBacklight suppressed];
-[KeyboardBacklight toggleMute];
-[KeyboardBacklight KBAuthenticationHandler:];
-[KeyboardBacklight KBAutoBrightnessSuspendPropertyHandler:];
-[KeyboardBacklight KBBacklightLevelPropertyHandler:];
-[KeyboardBacklight KBClamshellUpdateHandler:];
-[KeyboardBacklight KBIdleDimPropertyHandler:];
-[KeyboardBacklight KBSuspendDimmingPropertyHandler:];
-[KeyboardBacklight KBUserActivityUpdateHandler:];
-[KeyboardBacklight dimTime];
-[KeyboardBacklight getKeyboardBacklightPreferences];
-[KeyboardBacklight levelPercentage];
-[KeyboardBacklight setKeyboardSpecificPreferences:];
-[KeyboardBacklight KBAutoBrightnessEnablePropertyHandler:];
-[KeyboardBacklight KBAvailabilityUpdateHandler:];
-[KeyboardBacklight KBBrightnessPropertyHandler:];
-[KeyboardBacklight KBDisplayBrightnessFactorPropertyHandler:];
-[KeyboardBacklight KBIdleDimTimeHandler:];
-[KeyboardBacklight KBUpdateFrequencyHandler:];
-[KeyboardBacklight KBUserOffsetPropertyHandler:];
-[KeyboardBacklight brightnessUpdateReasonToString:];
-[KeyboardBacklight clamshellClosed];
-[KeyboardBacklight setKBPreferenceBacklightMaxUser];
-[KeyboardBacklight ambientHighThreshold];
-[KeyboardBacklight ambientLowThreshold];
-[KeyboardBacklight ambientOffset];
-[KeyboardBacklight ambientSlope];
-[KeyboardBacklight autoAdjust];
-[KeyboardBacklight calculateLevelPercentageAtAmbient:];
-[KeyboardBacklight cancelScheduledBacklightUpdate];
-[KeyboardBacklight commitCurrentBrightness];
-[KeyboardBacklight currentLuxToAmbient];
-[KeyboardBacklight didUpdateBacklightLevel:brightness:result:error:];
-[KeyboardBacklight endKeyDim];
-[KeyboardBacklight forceBacklightUpdateRoutine];
-[KeyboardBacklight forceLuxUpdate];
-[KeyboardBacklight forceLuxUpdateRoutine];
-[KeyboardBacklight getCurrentLux];
-[KeyboardBacklight handleDeviceManagementArrival:];
-[KeyboardBacklight handleLuxUpdate:];
-[KeyboardBacklight handlePMUserActivityStateChanged:];
-[KeyboardBacklight hysteresisOn];
-[KeyboardBacklight initWithQueue:device:];
-[KeyboardBacklight initWithQueue:device:ambientOffset:];
-[KeyboardBacklight keyboardAvailable];
-[KeyboardBacklight keyboardID];
-[KeyboardBacklight keyboardSpecificPreferences];
-[KeyboardBacklight levelMax];
-[KeyboardBacklight levelMin];
-[KeyboardBacklight levelOff];
-[KeyboardBacklight levelUnit];
-[KeyboardBacklight manualAdjust];
-[KeyboardBacklight maxUserLevel];
-[KeyboardBacklight newElementsArray];
-[KeyboardBacklight previousLevel];
-[KeyboardBacklight rampToBrightness:withDuration:];
-[KeyboardBacklight resetKeyDimTimeout];
-[KeyboardBacklight retrieveKeyboardBacklightElements];
-[KeyboardBacklight scheduleBacklightUpdate:];
-[KeyboardBacklight sendSuppressedNotification];
-[KeyboardBacklight setAmbientOffset:];
-[KeyboardBacklight setAutoAdjust:];
-[KeyboardBacklight setBrightness:withFadeSpeed:commit:];
-[KeyboardBacklight setClamshellClosed:];
-[KeyboardBacklight setDimTime:];
-[KeyboardBacklight setHysteresisOn:];
-[KeyboardBacklight setKeyboardAvailable:];
-[KeyboardBacklight setKeyboardID:];
-[KeyboardBacklight setLevelMax:];
-[KeyboardBacklight setLevelMin:];
-[KeyboardBacklight setLevelOff:];
-[KeyboardBacklight setLevelPercentage:];
-[KeyboardBacklight setLevelUnit:];
-[KeyboardBacklight setManualAdjust:];
-[KeyboardBacklight setPreviousLevel:];
-[KeyboardBacklight setSaturated:];
-[KeyboardBacklight setSuspend:];
-[KeyboardBacklight setUnitExponent:];
-[KeyboardBacklight startKBDeviceManagementServiceLookup];
-[KeyboardBacklight startRamp];
-[KeyboardBacklight stopKBDeviceManagementServiceLookup];
-[KeyboardBacklight stopRamp];
-[KeyboardBacklight storeKeyboardBacklightPreferences];
-[KeyboardBacklight timeToNextBacklightUpdate];
-[KeyboardBacklight updateAmbientOffset];
-[KeyboardBacklight updateAuthentication:];
-[KeyboardBacklight updateBacklightDevice];
-[KeyboardBacklight updateBacklightDeviceWithFadeSpeed:commit:reason:];
-[KeyboardBacklight updateBacklightDeviceWithReason:];
```
