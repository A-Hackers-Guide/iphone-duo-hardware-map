# `WiFiAnalyticsAWDSlowWiFiNotification`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 33 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _actionField;
I _recoveryAction;
I _recoveryReason;
I _userInput;
B _facetimeCallInProgress;
{?="timestamp"b1"actionField"b1"recoveryAction"b1"recoveryReason"b1"userInput"b1"facetimeCallInProgress"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasActionField;
@property (TI,N,V_actionField) actionField;
@property (TB,N) hasRecoveryAction;
@property (TI,N,V_recoveryAction) recoveryAction;
@property (TB,N) hasRecoveryReason;
@property (TI,N,V_recoveryReason) recoveryReason;
@property (TB,N) hasUserInput;
@property (TI,N,V_userInput) userInput;
@property (TB,N) hasFacetimeCallInProgress;
@property (TB,N,V_facetimeCallInProgress) facetimeCallInProgress;
```

## Instance methods

```
-[WiFiAnalyticsAWDSlowWiFiNotification hasTimestamp];
-[WiFiAnalyticsAWDSlowWiFiNotification setHasTimestamp:];
-[WiFiAnalyticsAWDSlowWiFiNotification setTimestamp:];
-[WiFiAnalyticsAWDSlowWiFiNotification writeTo:];
-[WiFiAnalyticsAWDSlowWiFiNotification userInput];
-[WiFiAnalyticsAWDSlowWiFiNotification mergeFrom:];
-[WiFiAnalyticsAWDSlowWiFiNotification timestamp];
-[WiFiAnalyticsAWDSlowWiFiNotification setUserInput:];
-[WiFiAnalyticsAWDSlowWiFiNotification hash];
-[WiFiAnalyticsAWDSlowWiFiNotification copyTo:];
-[WiFiAnalyticsAWDSlowWiFiNotification description];
-[WiFiAnalyticsAWDSlowWiFiNotification readFrom:];
-[WiFiAnalyticsAWDSlowWiFiNotification copyWithZone:];
-[WiFiAnalyticsAWDSlowWiFiNotification isEqual:];
-[WiFiAnalyticsAWDSlowWiFiNotification dictionaryRepresentation];
-[WiFiAnalyticsAWDSlowWiFiNotification hasUserInput];
-[WiFiAnalyticsAWDSlowWiFiNotification hasRecoveryReason];
-[WiFiAnalyticsAWDSlowWiFiNotification recoveryReason];
-[WiFiAnalyticsAWDSlowWiFiNotification setHasRecoveryReason:];
-[WiFiAnalyticsAWDSlowWiFiNotification setRecoveryReason:];
-[WiFiAnalyticsAWDSlowWiFiNotification setActionField:];
-[WiFiAnalyticsAWDSlowWiFiNotification actionField];
-[WiFiAnalyticsAWDSlowWiFiNotification facetimeCallInProgress];
-[WiFiAnalyticsAWDSlowWiFiNotification hasActionField];
-[WiFiAnalyticsAWDSlowWiFiNotification hasFacetimeCallInProgress];
-[WiFiAnalyticsAWDSlowWiFiNotification hasRecoveryAction];
-[WiFiAnalyticsAWDSlowWiFiNotification recoveryAction];
-[WiFiAnalyticsAWDSlowWiFiNotification setFacetimeCallInProgress:];
-[WiFiAnalyticsAWDSlowWiFiNotification setHasActionField:];
-[WiFiAnalyticsAWDSlowWiFiNotification setHasFacetimeCallInProgress:];
-[WiFiAnalyticsAWDSlowWiFiNotification setHasRecoveryAction:];
-[WiFiAnalyticsAWDSlowWiFiNotification setHasUserInput:];
-[WiFiAnalyticsAWDSlowWiFiNotification setRecoveryAction:];
```
