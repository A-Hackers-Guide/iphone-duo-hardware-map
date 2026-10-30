# `CAFHistoricalNotification`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 27 properties, 48 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleFullDescriptionCharacteristic;
@property (T@"CAFMeasurementCharacteristic",R,N) timestampCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) symbolNameCharacteristic;
@property (T@"CAFNotificationSeverityCharacteristic",R,N) notificationSeverityCharacteristic;
@property (T@"CAFHistoricalNotificationUserActionsCharacteristic",R,N) historicalNotificationUserActionsCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) userDismissibleCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) userActionCharacteristic;
@property (T@"NSString",R,N) userVisibleLabel;
@property (T@"NSString",R,N) userVisibleDescription;
@property (T@"NSString",R,N) userVisibleFullDescription;
@property (TB,R,N) hasUserVisibleFullDescription;
@property (T@"NSMeasurement",R,N) timestamp;
@property (T@"CAFUInt64Range",R,N) timestampRange;
@property (T@"CAFMeasurementRange",R,N) timestampMeasurementRange;
@property (T@"NSString",C,N) symbolName;
@property (TC,N) notificationSeverity;
@property (T@"CAFHistoricalNotificationUserActions",R,N) historicalNotificationUserActions;
@property (TB,R,N) hasHistoricalNotificationUserActions;
@property (TB,N) userDismissible;
@property (TB,R,N) hasUserDismissible;
@property (TB,N) hidden;
@property (TC,N) userAction;
@property (T@"CAFUInt8Range",R,N) userActionRange;
@property (TB,R,N) hasUserAction;
```

## Class methods

```
+[CAFHistoricalNotification serviceIdentifier];
+[CAFHistoricalNotification observerProtocol];
```

## Instance methods

```
-[CAFHistoricalNotification setHidden:];
-[CAFHistoricalNotification removeObserver:];
-[CAFHistoricalNotification setSymbolName:];
-[CAFHistoricalNotification symbolName];
-[CAFHistoricalNotification timestamp];
-[CAFHistoricalNotification userAction];
-[CAFHistoricalNotification addObserver:];
-[CAFHistoricalNotification registerObserver:];
-[CAFHistoricalNotification name];
-[CAFHistoricalNotification unregisterObserver:];
-[CAFHistoricalNotification hidden];
-[CAFHistoricalNotification setUserAction:];
-[CAFHistoricalNotification userDismissible];
-[CAFHistoricalNotification setUserDismissible:];
-[CAFHistoricalNotification hasUserAction];
-[CAFHistoricalNotification hasUserDismissible];
-[CAFHistoricalNotification historicalNotificationUserActions];
-[CAFHistoricalNotification notificationSeverity];
-[CAFHistoricalNotification registeredForHidden];
-[CAFHistoricalNotification registeredForHistoricalNotificationUserActions];
-[CAFHistoricalNotification registeredForNotificationSeverity];
-[CAFHistoricalNotification registeredForSymbolName];
-[CAFHistoricalNotification registeredForTimestamp];
-[CAFHistoricalNotification registeredForUserAction];
-[CAFHistoricalNotification registeredForUserDismissible];
-[CAFHistoricalNotification registeredForUserVisibleDescription];
-[CAFHistoricalNotification registeredForUserVisibleFullDescription];
-[CAFHistoricalNotification registeredForUserVisibleLabel];
-[CAFHistoricalNotification setNotificationSeverity:];
-[CAFHistoricalNotification userVisibleDescription];
-[CAFHistoricalNotification userVisibleFullDescription];
-[CAFHistoricalNotification userVisibleLabel];
-[CAFHistoricalNotification userActionRange];
-[CAFHistoricalNotification _characteristicDidUpdate:fromGroupUpdate:];
-[CAFHistoricalNotification hasHistoricalNotificationUserActions];
-[CAFHistoricalNotification hasUserVisibleFullDescription];
-[CAFHistoricalNotification hiddenCharacteristic];
-[CAFHistoricalNotification historicalNotificationUserActionsCharacteristic];
-[CAFHistoricalNotification notificationSeverityCharacteristic];
-[CAFHistoricalNotification symbolNameCharacteristic];
-[CAFHistoricalNotification timestampCharacteristic];
-[CAFHistoricalNotification timestampMeasurementRange];
-[CAFHistoricalNotification timestampRange];
-[CAFHistoricalNotification userActionCharacteristic];
-[CAFHistoricalNotification userDismissibleCharacteristic];
-[CAFHistoricalNotification userVisibleDescriptionCharacteristic];
-[CAFHistoricalNotification userVisibleFullDescriptionCharacteristic];
-[CAFHistoricalNotification userVisibleLabelCharacteristic];
```
