# `NightModeControl`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 49 instance variables, 1 properties, 49 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSMutableDictionary" _properties;
@"SunriseSunsetProvider" _sunriseSunsetProvider;
i _sunriseSunsetInfoQueryTimeout;
@"NSDictionary" _sunriseSunsetInfo;
@"NSMutableArray" _supportObjs;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_source>" _nextTransitionTimer;
@"NSObject<OS_dispatch_source>" _transitionTimer;
@"CBAnalyticsNightShiftTracker" _modeTracker;
i _algoState;
f _transitionLength;
f _transitionLengthActual;
f _transitionsTimesCoeff;
f _transitionRate;
f _minFactor;
f _maxFactor;
{NMFactorState="rampStartTime"d"factor"f"target"f"start"f"rampLength"f} _factorState;
^{__CFTimeZone=} _currentTimeZone;
d _sunsetAbsolute;
d _sunsetPreviousAbsolute;
d _sunriseAbsolute;
d _sunrisePreviousAbsolute;
d _offTransitionTimeAbsoluteUnrestricted;
d _offTransitionTimeAbsoluteUnrestrictedPrev;
B _transitionTimesValid;
B _isDaylight;
i _currentScheduledTransitionType;
d _displayOffTimestamp;
d _untilNexTransitionTimestamp;
f _inactivityTimeout;
B _checkInactivity;
B _displayOff;
@? _callbackBlock;
{?="active"B"enabled"B"sunSchedulePermitted"B"mode"i"schedule"{?="fromTime"{?="hour"i"minute"i}"toTime"{?="hour"i"minute"i}}"disableFlags"Q"available"B} _status;
{?="fromTime"{?="hour"i"minute"i}"toTime"{?="hour"i"minute"i}} _backupSchedule;
B _statusUpdated;
@"NSString" _currentSunriseKey;
@"NSString" _currentSunsetKey;
@"NSString" _previousSunriseKey;
@"NSString" _previousSunsetKey;
@"NSString" _nextSunriseKey;
@"NSString" _nextSunsetKey;
@"NSString" _isDaylightKey;
i _notifyUserAboutScheduleCounter;
^{__CFUserNotification=} _enableNotification;
B _notificationInProgress;
B _revertToSunriseSunset;
@"NSObject<CBDisplayModeProvider>" _displayModeProvider;
```

## Properties

```
@property (T@"NSObject<CBDisplayModeProvider>",&,N,V_displayModeProvider) displayModeProvider;
```

## Instance methods

```
-[NightModeControl setNightShiftFactorDictionary:];
-[NightModeControl copyPreferenceForKey:user:];
-[NightModeControl setProperty:forKey:];
-[NightModeControl setPreference:forKey:user:];
-[NightModeControl initiateRestrictedMaxTransition];
-[NightModeControl initiateFullMaxTransition];
-[NightModeControl timeZoneChanged];
-[NightModeControl observeValueForKeyPath:ofObject:change:context:];
-[NightModeControl copyStatusDictionaryFromPrefs];
-[NightModeControl transitionTimerHandler];
-[NightModeControl copyLowPowerModeState];
-[NightModeControl updateTransitionTimes:];
-[NightModeControl stop];
-[NightModeControl retrieveSunriseSunsetTimesFromBackup:];
-[NightModeControl updateSunriseSunsetBackup];
-[NightModeControl updateOptionTimestamp:];
-[NightModeControl dealloc];
-[NightModeControl removeSupportObject:];
-[NightModeControl reevaluateCurrentStateWithFactorFadeOption:];
-[NightModeControl scheduleNextTransition:withType:];
-[NightModeControl setMode:];
-[NightModeControl updateTransitionTimesFromSunriseSunset:];
-[NightModeControl updateTransitionTimesFromSchedule:];
-[NightModeControl parseStatusDictionary:intoStruct:shouldUpdatePrefs:];
-[NightModeControl updateStatusDictionaryWithValue:forKey:];
-[NightModeControl cancelTransition];
-[NightModeControl setNightModeFactor:withFadePeriod:];
-[NightModeControl getPropertyForKey:];
-[NightModeControl updateSunriseSunsetInfo:];
-[NightModeControl setDisplayModeProvider:];
-[NightModeControl displayModeProvider];
-[NightModeControl copyDictionaryFromStatus:];
-[NightModeControl cancelSchedule];
-[NightModeControl tearDownAllTimers];
-[NightModeControl copyTimeStringWithHour:minute:second:];
-[NightModeControl setSchedule:];
-[NightModeControl setSunPermitted:];
-[NightModeControl displayAlertInteractive:];
-[NightModeControl enableBlueLightReduction:withOption:];
-[NightModeControl initiateTransitionTo:andRampLength:];
-[NightModeControl reevaluateCurrentState];
-[NightModeControl addSupportObject:];
-[NightModeControl initWithSupportObject:queue:callback:];
-[NightModeControl setNightModeFactor:];
-[NightModeControl initiateFullMinTransition];
-[NightModeControl saveStatusToPrefs:];
-[NightModeControl clockChanged];
-[NightModeControl setAlgoState:];
-[NightModeControl updateLowPowerModeState:];
```
