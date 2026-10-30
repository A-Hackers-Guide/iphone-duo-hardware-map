# `SASingleDeviceRecord`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 26 instance variables, 27 properties, 59 instance methods, 1 class methods

## Instance variables

```
B _isConnected;
B _isConnectionTypeLeash;
B _isBatteryCriticallyLow;
B _hasSurfacedNotification;
@"NSUUID" _uuid;
@"SADevice" _device;
Q _withYouStatus;
Q _notificationState;
@"SAAdvertisement" _latestNOAdvertisement;
@"SAAdvertisement" _latestWildAdvertisement;
@"NSDate" _latestCaseAdvertisementDate;
@"NSDate" _lastWithYouDate;
@"NSDate" _lastCompanionDisconnectionDate;
Q _currentScenarioClass;
Q _currentMonitoringSessionState;
Q _monitoringSessionStateAtTimeOfFirstAdv;
@"NSMutableArray" _uuidsOfRelatedDevices;
@"NSDate" _firstAdvertisementAfterScenarioTransition;
@"NSDate" _currentScenarioTime;
@"CLCircularRegion" _lastWithYouLocation;
@"NSDate" _advertisingStartDateForHELE;
Q _currentBudPosition;
@"<SAAnalyticsServiceProtocol>" _analytics;
@"<SATimeServiceProtocol>" _clock;
q _relationStatus;
q _maintenanceStatus;
```

## Properties

```
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (T@"SADevice",&,N,V_device) device;
@property (TQ,N,V_withYouStatus) withYouStatus;
@property (TB,R,N,V_isConnected) isConnected;
@property (TB,R,N,V_isConnectionTypeLeash) isConnectionTypeLeash;
@property (TB,R,N,V_isBatteryCriticallyLow) isBatteryCriticallyLow;
@property (TQ,N,V_notificationState) notificationState;
@property (T@"SAAdvertisement",R,N) latestAdvertisement;
@property (T@"SAAdvertisement",R,N,V_latestNOAdvertisement) latestNOAdvertisement;
@property (T@"SAAdvertisement",R,N,V_latestWildAdvertisement) latestWildAdvertisement;
@property (T@"NSDate",R,N,V_latestCaseAdvertisementDate) latestCaseAdvertisementDate;
@property (T@"NSDate",R,N,V_lastWithYouDate) lastWithYouDate;
@property (T@"NSDate",R,N,V_lastCompanionDisconnectionDate) lastCompanionDisconnectionDate;
@property (TQ,R,N,V_currentScenarioClass) currentScenarioClass;
@property (TQ,N,V_currentMonitoringSessionState) currentMonitoringSessionState;
@property (TQ,R,N,V_monitoringSessionStateAtTimeOfFirstAdv) monitoringSessionStateAtTimeOfFirstAdv;
@property (T@"NSMutableArray",&,N,V_uuidsOfRelatedDevices) uuidsOfRelatedDevices;
@property (TB,N,V_hasSurfacedNotification) hasSurfacedNotification;
@property (T@"NSDate",R,N,V_firstAdvertisementAfterScenarioTransition) firstAdvertisementAfterScenarioTransition;
@property (T@"NSDate",R,N,V_currentScenarioTime) currentScenarioTime;
@property (T@"CLCircularRegion",C,N,V_lastWithYouLocation) lastWithYouLocation;
@property (T@"NSDate",C,N,V_advertisingStartDateForHELE) advertisingStartDateForHELE;
@property (TQ,N,V_currentBudPosition) currentBudPosition;
@property (T@"<SAAnalyticsServiceProtocol>",&,N,V_analytics) analytics;
@property (T@"<SATimeServiceProtocol>",&,N,V_clock) clock;
@property (Tq,N,V_relationStatus) relationStatus;
@property (Tq,N,V_maintenanceStatus) maintenanceStatus;
```

## Class methods

```
+[SASingleDeviceRecord supportsSecureCoding];
```

## Instance methods

```
-[SASingleDeviceRecord clock];
-[SASingleDeviceRecord analytics];
-[SASingleDeviceRecord setClock:];
-[SASingleDeviceRecord isConnected];
-[SASingleDeviceRecord setAnalytics:];
-[SASingleDeviceRecord setDevice:];
-[SASingleDeviceRecord uuid];
-[SASingleDeviceRecord device];
-[SASingleDeviceRecord setConnectionState:];
-[SASingleDeviceRecord encodeWithCoder:];
-[SASingleDeviceRecord initWithCoder:];
-[SASingleDeviceRecord notificationState];
-[SASingleDeviceRecord setNotificationState:];
-[SASingleDeviceRecord initWithDevice:clock:analytics:];
-[SASingleDeviceRecord setAdvertisingStartDateForHELE:];
-[SASingleDeviceRecord lastWithYouDate];
-[SASingleDeviceRecord advertisingStartDateForHELE];
-[SASingleDeviceRecord currentBudPosition];
-[SASingleDeviceRecord currentMonitoringSessionState];
-[SASingleDeviceRecord currentScenarioClass];
-[SASingleDeviceRecord currentScenarioTime];
-[SASingleDeviceRecord firstAdvertisementAfterScenarioTransition];
-[SASingleDeviceRecord hasSurfacedNotification];
-[SASingleDeviceRecord initWithConnectionEvent:clock:analytics:];
-[SASingleDeviceRecord insertRelatedDevice:];
-[SASingleDeviceRecord isBatteryCriticallyLow];
-[SASingleDeviceRecord isConnectionTypeLeash];
-[SASingleDeviceRecord lastCompanionDisconnectionDate];
-[SASingleDeviceRecord lastWithYouLocation];
-[SASingleDeviceRecord latestAdvertisement];
-[SASingleDeviceRecord latestCaseAdvertisementDate];
-[SASingleDeviceRecord latestNOAdvertisement];
-[SASingleDeviceRecord latestWildAdvertisement];
-[SASingleDeviceRecord maintenanceStatus];
-[SASingleDeviceRecord monitoringSessionStateAtTimeOfFirstAdv];
-[SASingleDeviceRecord publishAnalyticsForFirstAdv:scenario:];
-[SASingleDeviceRecord purgeAdvertisementTransparencyData:];
-[SASingleDeviceRecord relationStatus];
-[SASingleDeviceRecord resetRelatedDevices];
-[SASingleDeviceRecord setCurrentBudPosition:];
-[SASingleDeviceRecord setCurrentMonitoringSessionState:];
-[SASingleDeviceRecord setHasSurfacedNotification:];
-[SASingleDeviceRecord setLastWithYouLocation:];
-[SASingleDeviceRecord setMaintenanceStatus:];
-[SASingleDeviceRecord setRelationStatus:];
-[SASingleDeviceRecord setUuidsOfRelatedDevices:];
-[SASingleDeviceRecord setWithYouStatus:];
-[SASingleDeviceRecord updateAdvertisingStartDateForHELE:];
-[SASingleDeviceRecord updateCurrentScenarioClass:];
-[SASingleDeviceRecord updateFirstAdvertisementAfterScenarioTransition:];
-[SASingleDeviceRecord updateLastCompanionDisconnectionDate:];
-[SASingleDeviceRecord updateLastWithYouDate:];
-[SASingleDeviceRecord updateLatestAdvertisement:];
-[SASingleDeviceRecord updateLatestCaseAdvertisementDate:];
-[SASingleDeviceRecord updateMaintenanceStatus:];
-[SASingleDeviceRecord updateRelationStatus:];
-[SASingleDeviceRecord updateWithYouStatus:];
-[SASingleDeviceRecord uuidsOfRelatedDevices];
-[SASingleDeviceRecord withYouStatus];
```
