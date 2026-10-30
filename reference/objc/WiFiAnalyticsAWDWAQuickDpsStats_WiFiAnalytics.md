# `WiFiAnalyticsAWDWAQuickDpsStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 14 instance variables, 26 properties, 63 instance methods, 0 class methods

## Instance variables

```
Q _quickDpsTimeSincePreviousTriggerMinutes;
I _awdlActivityThreshold;
I _ccaThreshold;
I _probabilityThreshold;
I _rssiThreshold;
I _screenOffThreshold;
I _screenOnThreshold;
I _stallProbability;
i _suppressedReason;
B _isDpsValidationDisabled;
B _quickDpsResetRecommendation;
B _screenStateOn;
B _stallPrediction;
{?="quickDpsTimeSincePreviousTriggerMinutes"b1"awdlActivityThreshold"b1"ccaThreshold"b1"probabilityThreshold"b1"rssiThreshold"b1"screenOffThreshold"b1"screenOnThreshold"b1"stallProbability"b1"suppressedReason"b1"isDpsValidationDisabled"b1"quickDpsResetRecommendation"b1"screenStateOn"b1"stallPrediction"b1} _has;
```

## Properties

```
@property (TB,N) hasScreenStateOn;
@property (TB,N,V_screenStateOn) screenStateOn;
@property (TB,N) hasQuickDpsResetRecommendation;
@property (TB,N,V_quickDpsResetRecommendation) quickDpsResetRecommendation;
@property (TB,N) hasStallPrediction;
@property (TB,N,V_stallPrediction) stallPrediction;
@property (TB,N) hasStallProbability;
@property (TI,N,V_stallProbability) stallProbability;
@property (TB,N) hasProbabilityThreshold;
@property (TI,N,V_probabilityThreshold) probabilityThreshold;
@property (TB,N) hasCcaThreshold;
@property (TI,N,V_ccaThreshold) ccaThreshold;
@property (TB,N) hasRssiThreshold;
@property (TI,N,V_rssiThreshold) rssiThreshold;
@property (TB,N) hasScreenOnThreshold;
@property (TI,N,V_screenOnThreshold) screenOnThreshold;
@property (TB,N) hasScreenOffThreshold;
@property (TI,N,V_screenOffThreshold) screenOffThreshold;
@property (TB,N) hasSuppressedReason;
@property (Ti,N,V_suppressedReason) suppressedReason;
@property (TB,N) hasIsDpsValidationDisabled;
@property (TB,N,V_isDpsValidationDisabled) isDpsValidationDisabled;
@property (TB,N) hasAwdlActivityThreshold;
@property (TI,N,V_awdlActivityThreshold) awdlActivityThreshold;
@property (TB,N) hasQuickDpsTimeSincePreviousTriggerMinutes;
@property (TQ,N,V_quickDpsTimeSincePreviousTriggerMinutes) quickDpsTimeSincePreviousTriggerMinutes;
```

## Instance methods

```
-[WiFiAnalyticsAWDWAQuickDpsStats setRssiThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats rssiThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats writeTo:];
-[WiFiAnalyticsAWDWAQuickDpsStats mergeFrom:];
-[WiFiAnalyticsAWDWAQuickDpsStats hash];
-[WiFiAnalyticsAWDWAQuickDpsStats copyTo:];
-[WiFiAnalyticsAWDWAQuickDpsStats description];
-[WiFiAnalyticsAWDWAQuickDpsStats readFrom:];
-[WiFiAnalyticsAWDWAQuickDpsStats copyWithZone:];
-[WiFiAnalyticsAWDWAQuickDpsStats isEqual:];
-[WiFiAnalyticsAWDWAQuickDpsStats dictionaryRepresentation];
-[WiFiAnalyticsAWDWAQuickDpsStats probabilityThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats StringAsSuppressedReason:];
-[WiFiAnalyticsAWDWAQuickDpsStats hasCcaThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats setQuickDpsResetRecommendation:];
-[WiFiAnalyticsAWDWAQuickDpsStats stallPrediction];
-[WiFiAnalyticsAWDWAQuickDpsStats awdlActivityThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats ccaThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats hasAwdlActivityThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats hasIsDpsValidationDisabled];
-[WiFiAnalyticsAWDWAQuickDpsStats hasProbabilityThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats hasQuickDpsResetRecommendation];
-[WiFiAnalyticsAWDWAQuickDpsStats hasQuickDpsTimeSincePreviousTriggerMinutes];
-[WiFiAnalyticsAWDWAQuickDpsStats hasRssiThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats hasScreenOffThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats hasScreenOnThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats hasScreenStateOn];
-[WiFiAnalyticsAWDWAQuickDpsStats hasStallPrediction];
-[WiFiAnalyticsAWDWAQuickDpsStats hasStallProbability];
-[WiFiAnalyticsAWDWAQuickDpsStats hasSuppressedReason];
-[WiFiAnalyticsAWDWAQuickDpsStats isDpsValidationDisabled];
-[WiFiAnalyticsAWDWAQuickDpsStats quickDpsResetRecommendation];
-[WiFiAnalyticsAWDWAQuickDpsStats quickDpsTimeSincePreviousTriggerMinutes];
-[WiFiAnalyticsAWDWAQuickDpsStats screenOffThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats screenOnThreshold];
-[WiFiAnalyticsAWDWAQuickDpsStats screenStateOn];
-[WiFiAnalyticsAWDWAQuickDpsStats setAwdlActivityThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setCcaThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasAwdlActivityThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasCcaThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasIsDpsValidationDisabled:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasProbabilityThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasQuickDpsResetRecommendation:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasQuickDpsTimeSincePreviousTriggerMinutes:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasRssiThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasScreenOffThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasScreenOnThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasScreenStateOn:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasStallPrediction:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasStallProbability:];
-[WiFiAnalyticsAWDWAQuickDpsStats setHasSuppressedReason:];
-[WiFiAnalyticsAWDWAQuickDpsStats setIsDpsValidationDisabled:];
-[WiFiAnalyticsAWDWAQuickDpsStats setProbabilityThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setQuickDpsTimeSincePreviousTriggerMinutes:];
-[WiFiAnalyticsAWDWAQuickDpsStats setScreenOffThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setScreenOnThreshold:];
-[WiFiAnalyticsAWDWAQuickDpsStats setScreenStateOn:];
-[WiFiAnalyticsAWDWAQuickDpsStats setStallPrediction:];
-[WiFiAnalyticsAWDWAQuickDpsStats setStallProbability:];
-[WiFiAnalyticsAWDWAQuickDpsStats setSuppressedReason:];
-[WiFiAnalyticsAWDWAQuickDpsStats stallProbability];
-[WiFiAnalyticsAWDWAQuickDpsStats suppressedReason];
-[WiFiAnalyticsAWDWAQuickDpsStats suppressedReasonAsString:];
```
