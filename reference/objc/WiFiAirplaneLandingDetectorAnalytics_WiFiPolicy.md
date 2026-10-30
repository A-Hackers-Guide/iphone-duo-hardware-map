# `WiFiAirplaneLandingDetectorAnalytics`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _hasSubmittedLandingEvent;
i _startReason;
Q _landingDetectionCount;
@"NSDate" _detectorStartTime;
d _cumulativeActiveTime;
d _cumulativeInactiveTime;
d _cumulativeLayoverTime;
@"NSDate" _modeStartTime;
@"NSDate" _lastAnalyticsSubmissionTime;
```

## Properties

```
@property (Ti,N,V_startReason) startReason;
@property (T@"NSDate",&,N,V_detectorStartTime) detectorStartTime;
@property (Td,N,V_cumulativeActiveTime) cumulativeActiveTime;
@property (Td,N,V_cumulativeInactiveTime) cumulativeInactiveTime;
@property (Td,N,V_cumulativeLayoverTime) cumulativeLayoverTime;
@property (TQ,N,V_landingDetectionCount) landingDetectionCount;
@property (T@"NSDate",&,N,V_modeStartTime) modeStartTime;
@property (T@"NSDate",&,N,V_lastAnalyticsSubmissionTime) lastAnalyticsSubmissionTime;
@property (TB,N,V_hasSubmittedLandingEvent) hasSubmittedLandingEvent;
```

## Instance methods

```
-[WiFiAirplaneLandingDetectorAnalytics startReason];
-[WiFiAirplaneLandingDetectorAnalytics setStartReason:];
-[WiFiAirplaneLandingDetectorAnalytics setLastAnalyticsSubmissionTime:];
-[WiFiAirplaneLandingDetectorAnalytics submitAnalyticsEventDictionary:];
-[WiFiAirplaneLandingDetectorAnalytics buildAnalyticsEventDictionary:state:isAssociated:];
-[WiFiAirplaneLandingDetectorAnalytics buildAndSubmitAnalyticsEvent:state:isAssociated:];
-[WiFiAirplaneLandingDetectorAnalytics calculateIdlespan];
-[WiFiAirplaneLandingDetectorAnalytics calculatePoweredOffLifespan];
-[WiFiAirplaneLandingDetectorAnalytics cumulativeActiveTime];
-[WiFiAirplaneLandingDetectorAnalytics cumulativeInactiveTime];
-[WiFiAirplaneLandingDetectorAnalytics cumulativeLayoverTime];
-[WiFiAirplaneLandingDetectorAnalytics detectorStartTime];
-[WiFiAirplaneLandingDetectorAnalytics getCurrentAnalyticsState];
-[WiFiAirplaneLandingDetectorAnalytics hasSubmittedLandingEvent];
-[WiFiAirplaneLandingDetectorAnalytics incrementLandingCount];
-[WiFiAirplaneLandingDetectorAnalytics initWithStartReason:];
-[WiFiAirplaneLandingDetectorAnalytics landingDetectionCount];
-[WiFiAirplaneLandingDetectorAnalytics lastAnalyticsSubmissionTime];
-[WiFiAirplaneLandingDetectorAnalytics modeStartTime];
-[WiFiAirplaneLandingDetectorAnalytics restoreFromPersistence:];
-[WiFiAirplaneLandingDetectorAnalytics setCumulativeActiveTime:];
-[WiFiAirplaneLandingDetectorAnalytics setCumulativeInactiveTime:];
-[WiFiAirplaneLandingDetectorAnalytics setCumulativeLayoverTime:];
-[WiFiAirplaneLandingDetectorAnalytics setDetectorStartTime:];
-[WiFiAirplaneLandingDetectorAnalytics setHasSubmittedLandingEvent:];
-[WiFiAirplaneLandingDetectorAnalytics setLandingDetectionCount:];
-[WiFiAirplaneLandingDetectorAnalytics setModeStartTime:];
-[WiFiAirplaneLandingDetectorAnalytics stateToPersist];
-[WiFiAirplaneLandingDetectorAnalytics submitAltimeterReadingWithAltitude:interval:startReason:state:verticalSpeed:];
-[WiFiAirplaneLandingDetectorAnalytics updateModeTransitionWithCurrentInterval:activeInterval:layoverInterval:inactiveInterval:];
```
