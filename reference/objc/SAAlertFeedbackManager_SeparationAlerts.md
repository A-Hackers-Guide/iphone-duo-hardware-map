# `SAAlertFeedbackManager`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAAlertFeedbackManagerProtocol`
- 16 instance variables, 20 properties, 45 instance methods, 0 class methods

## Instance variables

```
B _feedbackEnabled;
d _backoffInterval;
d _samplingRate;
d _optOutDuration;
@"<SATimeServiceProtocol>" _clock;
@"<SAAnalyticsServiceProtocol>" _analytics;
@"<SAUserNotificationPresenterProtocol>" _notificationPresenter;
@"TADefaults" _defaults;
@"NSDate" _lastFeedbackShownDate;
@"NSDate" _optOutStartDate;
@"NSMutableDictionary" _deviceUUIDtoPendingAlertContent;
@"NSMutableDictionary" _deviceUUIDtoPendingReunionContent;
@"NSMutableDictionary" _deviceUUIDtoFeedbackResponse;
@"NSMutableDictionary" _deviceUUIDtoDeferredAlertInfo;
@"NSDictionary" _cachedConfiguration;
Q _currentVehicularState;
```

## Properties

```
@property (T@"<SATimeServiceProtocol>",&,N,V_clock) clock;
@property (T@"<SAAnalyticsServiceProtocol>",&,N,V_analytics) analytics;
@property (T@"<SAUserNotificationPresenterProtocol>",&,N,V_notificationPresenter) notificationPresenter;
@property (T@"TADefaults",&,N,V_defaults) defaults;
@property (T@"NSDate",&,N,V_lastFeedbackShownDate) lastFeedbackShownDate;
@property (T@"NSDate",&,N,V_optOutStartDate) optOutStartDate;
@property (T@"NSMutableDictionary",&,N,V_deviceUUIDtoPendingAlertContent) deviceUUIDtoPendingAlertContent;
@property (T@"NSMutableDictionary",&,N,V_deviceUUIDtoPendingReunionContent) deviceUUIDtoPendingReunionContent;
@property (T@"NSMutableDictionary",&,N,V_deviceUUIDtoFeedbackResponse) deviceUUIDtoFeedbackResponse;
@property (T@"NSMutableDictionary",&,N,V_deviceUUIDtoDeferredAlertInfo) deviceUUIDtoDeferredAlertInfo;
@property (T@"NSDictionary",&,N,V_cachedConfiguration) cachedConfiguration;
@property (TQ,N,V_currentVehicularState) currentVehicularState;
@property (TB,N,V_feedbackEnabled) feedbackEnabled;
@property (Td,N,V_backoffInterval) backoffInterval;
@property (Td,N,V_samplingRate) samplingRate;
@property (Td,N,V_optOutDuration) optOutDuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SAAlertFeedbackManager setDefaults:];
-[SAAlertFeedbackManager clock];
-[SAAlertFeedbackManager analytics];
-[SAAlertFeedbackManager cachedConfiguration];
-[SAAlertFeedbackManager setClock:];
-[SAAlertFeedbackManager defaults];
-[SAAlertFeedbackManager setNotificationPresenter:];
-[SAAlertFeedbackManager notificationPresenter];
-[SAAlertFeedbackManager ingestTAEvent:];
-[SAAlertFeedbackManager currentVehicularState];
-[SAAlertFeedbackManager setCurrentVehicularState:];
-[SAAlertFeedbackManager setAnalytics:];
-[SAAlertFeedbackManager setCachedConfiguration:];
-[SAAlertFeedbackManager samplingRate];
-[SAAlertFeedbackManager setSamplingRate:];
-[SAAlertFeedbackManager feedbackEnabled];
-[SAAlertFeedbackManager setFeedbackEnabled:];
-[SAAlertFeedbackManager backoffInterval];
-[SAAlertFeedbackManager setBackoffInterval:];
-[SAAlertFeedbackManager optOutStartDate];
-[SAAlertFeedbackManager deviceUUIDtoPendingAlertContent];
-[SAAlertFeedbackManager _evaluateTrialConfiguration];
-[SAAlertFeedbackManager _showDeferredPopUps];
-[SAAlertFeedbackManager _valueForFactor:default:];
-[SAAlertFeedbackManager deviceUUIDtoDeferredAlertInfo];
-[SAAlertFeedbackManager deviceUUIDtoFeedbackResponse];
-[SAAlertFeedbackManager deviceUUIDtoPendingReunionContent];
-[SAAlertFeedbackManager finishFeedbackForDeviceUUID:response:];
-[SAAlertFeedbackManager handleAlertEventForDeviceUUID:deviceName:alertTimestamp:content:legacySuppressed:];
-[SAAlertFeedbackManager handleReunionEventForDeviceUUID:content:];
-[SAAlertFeedbackManager handleVehicularStateChange:];
-[SAAlertFeedbackManager initWithClock:analytics:defaults:notificationPresenter:];
-[SAAlertFeedbackManager lastFeedbackShownDate];
-[SAAlertFeedbackManager optOutDuration];
-[SAAlertFeedbackManager presentFirstPopUpForDeviceUUID:deviceName:timestamp:];
-[SAAlertFeedbackManager presentSecondPopUpForDeviceUUID:];
-[SAAlertFeedbackManager setDeviceUUIDtoDeferredAlertInfo:];
-[SAAlertFeedbackManager setDeviceUUIDtoFeedbackResponse:];
-[SAAlertFeedbackManager setDeviceUUIDtoPendingAlertContent:];
-[SAAlertFeedbackManager setDeviceUUIDtoPendingReunionContent:];
-[SAAlertFeedbackManager setLastFeedbackShownDate:];
-[SAAlertFeedbackManager setOptOutDuration:];
-[SAAlertFeedbackManager setOptOutStartDate:];
-[SAAlertFeedbackManager shouldShowFeedbackForDeviceUUID:];
-[SAAlertFeedbackManager submitPendingReunionIfNeeded:];
```
