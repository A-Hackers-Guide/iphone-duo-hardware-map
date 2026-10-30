# `WiFiLocaleManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiLocationManagerDelegate`
- 20 instance variables, 23 properties, 69 instance methods, 1 class methods

## Instance variables

```
^{__CTServerConnection=} _ctServerConnectionRef;
B _localeCheckSuspended;
C _isWaitingForLocationUpdate;
C _testModeEnabled;
i _localeSource;
i _aggressiveRetryAttemptsRemaining;
i _testMcc;
@"<WiFiLocaleManagerDelegate>" _delegate;
@"NSString" _localeCountryCode;
d _localeTimeout;
d _localeLastUpdatedTime;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_source>" _localeTimer;
@"NSObject<OS_dispatch_source>" _retryTimer;
@"NSDateFormatter" _dateFormatter;
@"WiFiLocationManager" _locationManager;
@"NSString" _testHost11d;
@"NSString" _testPeer;
@"NSString" _testTimeZoneCC;
@"NSString" _testUserDefaults;
```

## Properties

```
@property (TB,V_localeCheckSuspended) localeCheckSuspended;
@property (T@"NSString",&,V_localeCountryCode) localeCountryCode;
@property (Ti,V_localeSource) localeSource;
@property (Td,V_localeTimeout) localeTimeout;
@property (Td,V_localeLastUpdatedTime) localeLastUpdatedTime;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@"NSObject<OS_dispatch_source>",&,V_localeTimer) localeTimer;
@property (T@"NSObject<OS_dispatch_source>",&,V_retryTimer) retryTimer;
@property (Ti,V_aggressiveRetryAttemptsRemaining) aggressiveRetryAttemptsRemaining;
@property (T@"NSDateFormatter",&,V_dateFormatter) dateFormatter;
@property (T@"WiFiLocationManager",&,V_locationManager) locationManager;
@property (TC,V_isWaitingForLocationUpdate) isWaitingForLocationUpdate;
@property (TC,V_testModeEnabled) testModeEnabled;
@property (Ti,V_testMcc) testMcc;
@property (T@"NSString",&,V_testHost11d) testHost11d;
@property (T@"NSString",&,V_testPeer) testPeer;
@property (T@"NSString",&,V_testTimeZoneCC) testTimeZoneCC;
@property (T@"NSString",&,V_testUserDefaults) testUserDefaults;
@property (T@"<WiFiLocaleManagerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[WiFiLocaleManager getStringOfLocaleSource:];
```

## Instance methods

```
-[WiFiLocaleManager setLocationManager:];
-[WiFiLocaleManager didFailWithError:];
-[WiFiLocaleManager locationManager];
-[WiFiLocaleManager getLocaleFromUserDefaults];
-[WiFiLocaleManager getLocaleFromCompanion];
-[WiFiLocaleManager setRetryTimer:];
-[WiFiLocaleManager localeTimer];
-[WiFiLocaleManager setTestModeEnabled:];
-[WiFiLocaleManager init];
-[WiFiLocaleManager getLocaleFromPeer];
-[WiFiLocaleManager applySetCountryCodeExceptions:];
-[WiFiLocaleManager setTestTimeZoneCC:];
-[WiFiLocaleManager localeCountryCode];
-[WiFiLocaleManager getLocaleCountryCode];
-[WiFiLocaleManager isWaitingForLocationUpdate];
-[WiFiLocaleManager didUpdateLocations:];
-[WiFiLocaleManager getRestrictedCountryCodeFromRegionInfo];
-[WiFiLocaleManager dealloc];
-[WiFiLocaleManager setLocaleCountryCode:];
-[WiFiLocaleManager setLocaleTimer:];
-[WiFiLocaleManager getLocaleUsingBoundingBoxes:];
-[WiFiLocaleManager setDateFormatter:];
-[WiFiLocaleManager setLocaleCheckSuspended:];
-[WiFiLocaleManager setTestPeer:];
-[WiFiLocaleManager testModeEnabled];
-[WiFiLocaleManager dateFormatter];
-[WiFiLocaleManager getLocaleUsingGeoLocationCache:];
-[WiFiLocaleManager queue];
-[WiFiLocaleManager setCountryCode:source:];
-[WiFiLocaleManager testHost11d];
-[WiFiLocaleManager testTimeZoneCC];
-[WiFiLocaleManager setLocaleLastUpdatedTime:];
-[WiFiLocaleManager localeCheckSuspended];
-[WiFiLocaleManager didChangeAuthorizationStatus];
-[WiFiLocaleManager retrySetCountryCode:source:];
-[WiFiLocaleManager setDelegate:];
-[WiFiLocaleManager localeLastUpdatedTime];
-[WiFiLocaleManager retryTimer];
-[WiFiLocaleManager getLocaleFromMultiple80211d];
-[WiFiLocaleManager localeTimeout];
-[WiFiLocaleManager getLocaleSource];
-[WiFiLocaleManager determineLocale:];
-[WiFiLocaleManager setLocaleSource:];
-[WiFiLocaleManager delegate];
-[WiFiLocaleManager getLocaleFromMcc];
-[WiFiLocaleManager setAggressiveRetryAttemptsRemaining:];
-[WiFiLocaleManager isLocaleCheckSuspended];
-[WiFiLocaleManager determineAndSetLocale:];
-[WiFiLocaleManager setTestMcc:];
-[WiFiLocaleManager setIsWaitingForLocationUpdate:];
-[WiFiLocaleManager getLocaleFromRemoteClient];
-[WiFiLocaleManager setLocaleTestParams:];
-[WiFiLocaleManager getLocaleFromLocation:];
-[WiFiLocaleManager setTestHost11d:];
-[WiFiLocaleManager isDefaultCountryCode:];
-[WiFiLocaleManager setLocaleTimeout:];
-[WiFiLocaleManager setTestUserDefaults:];
-[WiFiLocaleManager getLocaleUsingReverseGeocoder:];
-[WiFiLocaleManager testUserDefaults];
-[WiFiLocaleManager testMcc];
-[WiFiLocaleManager localeSource];
-[WiFiLocaleManager getLocaleLastUpdatedTime];
-[WiFiLocaleManager testPeer];
-[WiFiLocaleManager shouldDetermineNewLocale];
-[WiFiLocaleManager getRestrictedCountryCodeFromTimezone];
-[WiFiLocaleManager aggressiveRetryAttemptsRemaining];
-[WiFiLocaleManager setQueue:];
-[WiFiLocaleManager getNetworkReachability];
-[WiFiLocaleManager getLocaleFromTimezone];
```
