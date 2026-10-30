# `CAFButtonSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerSetting`
- 0 instance variables, 5 properties, 14 instance methods, 2 class methods

## Properties

```
@property (T@"CAFButtonActionCharacteristic",R,N) buttonActionCharacteristic;
@property (T@"CAFSettingNotificationEntryCharacteristic",R,N) notificationInfoCharacteristic;
@property (TC,N) buttonAction;
@property (T@"CAFSettingNotificationEntry",R,N) notificationInfo;
@property (TB,R,N) hasNotificationInfo;
```

## Class methods

```
+[CAFButtonSetting serviceIdentifier];
+[CAFButtonSetting observerProtocol];
```

## Instance methods

```
-[CAFButtonSetting removeObserver:];
-[CAFButtonSetting notificationInfo];
-[CAFButtonSetting addObserver:];
-[CAFButtonSetting registerObserver:];
-[CAFButtonSetting name];
-[CAFButtonSetting unregisterObserver:];
-[CAFButtonSetting buttonAction];
-[CAFButtonSetting setButtonAction:];
-[CAFButtonSetting registeredForButtonAction];
-[CAFButtonSetting registeredForNotificationInfo];
-[CAFButtonSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFButtonSetting buttonActionCharacteristic];
-[CAFButtonSetting hasNotificationInfo];
-[CAFButtonSetting notificationInfoCharacteristic];
```
