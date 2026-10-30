# `PLSpringBoardAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 22 instance variables, 22 properties, 59 instance methods, 16 class methods

## Instance variables

```
B _autoLockIsNil;
B _deviceIsCharging;
@"PLNSNotificationOperatorComposition" _notificationSBScreenTimeTrackingChanged;
@"PLCFNotificationOperatorComposition" _notificationSBLockTrackingChanged;
@"PLCFNotificationOperatorComposition" _notificationSBBlankTrackingChanged;
@"PLNSNotificationOperatorComposition" _notificationSBWallpaperTrackingChanged;
@"PLNSNotificationOperatorComposition" _notificationSBAutoLockTimerFiredNotification;
@"PLTimer" _dailyWallpaperPoll;
@"PLEntryNotificationOperatorComposition" _displayOnNotification;
@"PLEntryNotificationOperatorComposition" _displayOffNotification;
@"PLEntryNotificationOperatorComposition" _receivedPushNotification;
@"PLXPCListenerOperatorComposition" _userNotificationRequestEvent;
@"PLXPCListenerOperatorComposition" _userNotificationTriggerEvent;
@"PLXPCListenerOperatorComposition" _bulletinBoardNotificationPublishEvent;
@"PLMonotonicTimer" _autolockEnergyPeriodicTimer;
@"NSDate" _lastEligibleAutolockEnergyComputationDate;
@"AWAttentionAwarenessClient" _attentionAwarenessClient;
d _lastUserEventMediaTime;
@"NSDictionary" _screenNumberToName;
@"PLEntryNotificationOperatorComposition" _deviceChargingStateNotification;
@"PLEntry" _lastSBEntry;
@"PLEntry" _lastReceivedPushEntry;
```

## Properties

```
@property (T@"PLNSNotificationOperatorComposition",R,V_notificationSBScreenTimeTrackingChanged) notificationSBScreenTimeTrackingChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationSBLockTrackingChanged) notificationSBLockTrackingChanged;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationSBBlankTrackingChanged) notificationSBBlankTrackingChanged;
@property (T@"PLNSNotificationOperatorComposition",R,V_notificationSBWallpaperTrackingChanged) notificationSBWallpaperTrackingChanged;
@property (T@"PLNSNotificationOperatorComposition",R,V_notificationSBAutoLockTimerFiredNotification) notificationSBAutoLockTimerFiredNotification;
@property (T@"PLTimer",&,V_dailyWallpaperPoll) dailyWallpaperPoll;
@property (TB,V_autoLockIsNil) autoLockIsNil;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayOnNotification) displayOnNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_displayOffNotification) displayOffNotification;
@property (T@"PLEntryNotificationOperatorComposition",&,V_receivedPushNotification) receivedPushNotification;
@property (T@"PLXPCListenerOperatorComposition",R,V_userNotificationRequestEvent) userNotificationRequestEvent;
@property (T@"PLXPCListenerOperatorComposition",R,V_userNotificationTriggerEvent) userNotificationTriggerEvent;
@property (T@"PLXPCListenerOperatorComposition",R,V_bulletinBoardNotificationPublishEvent) bulletinBoardNotificationPublishEvent;
@property (T@"PLMonotonicTimer",&,V_autolockEnergyPeriodicTimer) autolockEnergyPeriodicTimer;
@property (T@"NSDate",&,V_lastEligibleAutolockEnergyComputationDate) lastEligibleAutolockEnergyComputationDate;
@property (T@"AWAttentionAwarenessClient",&,V_attentionAwarenessClient) attentionAwarenessClient;
@property (Td,V_lastUserEventMediaTime) lastUserEventMediaTime;
@property (T@"NSDictionary",&,V_screenNumberToName) screenNumberToName;
@property (TB,V_deviceIsCharging) deviceIsCharging;
@property (T@"PLEntryNotificationOperatorComposition",&,V_deviceChargingStateNotification) deviceChargingStateNotification;
@property (T@"PLEntry",&,V_lastSBEntry) lastSBEntry;
@property (T@"PLEntry",&,N,V_lastReceivedPushEntry) lastReceivedPushEntry;
```

## Class methods

```
+[PLSpringBoardAgent entryEventPointDefinitions];
+[PLSpringBoardAgent entryEventForwardDefinitions];
+[PLSpringBoardAgent entryEventBackwardDefinitions];
+[PLSpringBoardAgent load];
+[PLSpringBoardAgent defaults];
+[PLSpringBoardAgent isEnabled];
+[PLSpringBoardAgent entryAggregateDefinitions];
+[PLSpringBoardAgent entryEventForwardDefinitionLock];
+[PLSpringBoardAgent entryAggregateDefinitionBulletins];
+[PLSpringBoardAgent entryAggregateDefinitionNotifications];
+[PLSpringBoardAgent entryEventForwardDefinitionBlank];
+[PLSpringBoardAgent entryEventForwardDefinitionScreen];
+[PLSpringBoardAgent entryEventForwardDefinitionWallpaper];
+[PLSpringBoardAgent entryEventPointAutoLock];
+[PLSpringBoardAgent entryEventPointBulletins];
+[PLSpringBoardAgent entryEventPointLocalRemoteNotifications];
```

## Instance methods

```
-[PLSpringBoardAgent currentMediaTime];
-[PLSpringBoardAgent displayOnNotification];
-[PLSpringBoardAgent init];
-[PLSpringBoardAgent dealloc];
-[PLSpringBoardAgent initOperatorDependancies];
-[PLSpringBoardAgent setDisplayOnNotification:];
-[PLSpringBoardAgent displayOffNotification];
-[PLSpringBoardAgent log];
-[PLSpringBoardAgent setDisplayOffNotification:];
-[PLSpringBoardAgent attentionAwarenessClient];
-[PLSpringBoardAgent setAttentionAwarenessClient:];
-[PLSpringBoardAgent setAutolockEnergyPeriodicTimer:];
-[PLSpringBoardAgent stopAutolockEnergyPeriodicTimer];
-[PLSpringBoardAgent deviceChargingStateNotification];
-[PLSpringBoardAgent setLastSBEntry:];
-[PLSpringBoardAgent addAccountingEvent:];
-[PLSpringBoardAgent addCountsAndDurationsFor:toEntry:];
-[PLSpringBoardAgent autoLockIsNil];
-[PLSpringBoardAgent autolockEnergyPeriodicTimer];
-[PLSpringBoardAgent bulletinBoardNotificationPublishEvent];
-[PLSpringBoardAgent closeLastOpenEventsWithStopDate:];
-[PLSpringBoardAgent computeAutolockEnergyWithNow:];
-[PLSpringBoardAgent dailyWallpaperPoll];
-[PLSpringBoardAgent deviceIsCharging];
-[PLSpringBoardAgent fetchSBWallpaperForType:];
-[PLSpringBoardAgent handleChargingStateChange:];
-[PLSpringBoardAgent lastEligibleAutolockEnergyComputationDate];
-[PLSpringBoardAgent lastReceivedPushEntry];
-[PLSpringBoardAgent lastSBEntry];
-[PLSpringBoardAgent lastUserEventMediaTime];
-[PLSpringBoardAgent logBulletinAggregate:];
-[PLSpringBoardAgent logBulletinPerEvent:];
-[PLSpringBoardAgent logMailNotification:];
-[PLSpringBoardAgent logNotification:];
-[PLSpringBoardAgent notificationSBAutoLockTimerFiredNotification];
-[PLSpringBoardAgent notificationSBBlankTrackingChanged];
-[PLSpringBoardAgent notificationSBLockTrackingChanged];
-[PLSpringBoardAgent notificationSBScreenTimeTrackingChanged];
-[PLSpringBoardAgent notificationSBWallpaperTrackingChanged];
-[PLSpringBoardAgent receivedPushNotification];
-[PLSpringBoardAgent resetAutoLockIsNil];
-[PLSpringBoardAgent screenLock:];
-[PLSpringBoardAgent screenNumberToName];
-[PLSpringBoardAgent setAutoLockIsNil:];
-[PLSpringBoardAgent setDailyWallpaperPoll:];
-[PLSpringBoardAgent setDeviceChargingStateNotification:];
-[PLSpringBoardAgent setDeviceIsCharging:];
-[PLSpringBoardAgent setLastEligibleAutolockEnergyComputationDate:];
-[PLSpringBoardAgent setLastReceivedPushEntry:];
-[PLSpringBoardAgent setLastUserEventMediaTime:];
-[PLSpringBoardAgent setReceivedPushNotification:];
-[PLSpringBoardAgent setScreenNumberToName:];
-[PLSpringBoardAgent setUpScreenNumberDictionary];
-[PLSpringBoardAgent settingsChangedNotification:];
-[PLSpringBoardAgent startAttentionAwarenessClient];
-[PLSpringBoardAgent startAutolockEnergyPeriodicTimer];
-[PLSpringBoardAgent stopAttentionAwarenessClient];
-[PLSpringBoardAgent userNotificationRequestEvent];
-[PLSpringBoardAgent userNotificationTriggerEvent];
```
