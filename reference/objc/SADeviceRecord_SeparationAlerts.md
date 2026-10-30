# `SADeviceRecord`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `SAWithYouDetectorClientProtocol`
- 4 instance variables, 4 properties, 53 instance methods, 1 class methods

## Instance variables

```
@"<SAAnalyticsServiceProtocol>" _analytics;
@"NSMutableDictionary" _deviceRecord;
@"TALocationLite" _lastLocation;
@"<SATimeServiceProtocol>" _clock;
```

## Properties

```
@property (T@"<SAAnalyticsServiceProtocol>",&,N,V_analytics) analytics;
@property (T@"NSMutableDictionary",&,N,V_deviceRecord) deviceRecord;
@property (T@"TALocationLite",&,N,V_lastLocation) lastLocation;
@property (T@"<SATimeServiceProtocol>",&,N,V_clock) clock;
```

## Class methods

```
+[SADeviceRecord supportsSecureCoding];
```

## Instance methods

```
-[SADeviceRecord clock];
-[SADeviceRecord analytics];
-[SADeviceRecord setClock:];
-[SADeviceRecord deviceRecord];
-[SADeviceRecord setLastLocation:];
-[SADeviceRecord ingestTAEvent:];
-[SADeviceRecord setAnalytics:];
-[SADeviceRecord lastLocation];
-[SADeviceRecord setDeviceRecord:];
-[SADeviceRecord updatedWithYouStatusFrom:to:forDeviceWithUUID:];
-[SADeviceRecord getLatestAdvertisement:];
-[SADeviceRecord didForceUpdateWithYouStatus];
-[SADeviceRecord hasSurfacedNotificationFor:];
-[SADeviceRecord encodeWithCoder:];
-[SADeviceRecord initWithCoder:];
-[SADeviceRecord updateLocation:];
-[SADeviceRecord getDeviceNotificationState:];
-[SADeviceRecord isConnected:];
-[SADeviceRecord getAdvertisingStartDateForHELE:];
-[SADeviceRecord getLatestCaseAdvertisementDate:];
-[SADeviceRecord _updateAdvertisingStartDateForHELE:];
-[SADeviceRecord _updateAllRelatedDevices];
-[SADeviceRecord _updateConnectionStateOnConnectionEvent:];
-[SADeviceRecord _updateDeviceRecordOnDeviceUpdateEvent:];
-[SADeviceRecord _updateLatestAdvertisement:];
-[SADeviceRecord _updateLatestCaseAdvertisementDate:];
-[SADeviceRecord _updateSingleDeviceRecordForDevice:];
-[SADeviceRecord getAllUUIDs];
-[SADeviceRecord getLastCompanionDisconnectionDate:];
-[SADeviceRecord getLastWithYouDate:];
-[SADeviceRecord getLastWithYouLocation:];
-[SADeviceRecord getLatestNOAdvertisement:];
-[SADeviceRecord getLatestWildAdvertisement:];
-[SADeviceRecord getMaintenanceStatus:];
-[SADeviceRecord getMonitoringSessionState:];
-[SADeviceRecord getRelatedDevices:];
-[SADeviceRecord getRelationStatus:];
-[SADeviceRecord getSADevice:];
-[SADeviceRecord getScenarioClass:];
-[SADeviceRecord getWithYouStatus:];
-[SADeviceRecord hasDisconnectedDevices];
-[SADeviceRecord initWithClock:analytics:];
-[SADeviceRecord isBatteryCriticallyLow:];
-[SADeviceRecord isConnectionTypeLeash:];
-[SADeviceRecord purgeAllAdvertisementTransparencyData:];
-[SADeviceRecord resetAllWithYouStatus];
-[SADeviceRecord updateLastWithYouDate:forDeviceWithUUID:];
-[SADeviceRecord updateLastWithYouLocation:forDeviceWithUUID:];
-[SADeviceRecord updateLatestAdvertisement:forDeviceWithUUID:];
-[SADeviceRecord updateMaintenanceStatus:forDeviceWithUUID:];
-[SADeviceRecord updateMonitoringSessionState:forDeviceWithUUID:];
-[SADeviceRecord updateRelationStatus:forDeviceWithUUID:];
-[SADeviceRecord updateScenario:forDeviceWithUUID:];
```
