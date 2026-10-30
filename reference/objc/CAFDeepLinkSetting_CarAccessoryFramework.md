# `CAFDeepLinkSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerSetting`
- 0 instance variables, 14 properties, 25 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) userVisibleValueCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) contentURLActionCharacteristic;
@property (T@"CAFUserVisibleDetailedDescriptionCharacteristic",R,N) userVisibleDetailedDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFSettingNotificationEntryCharacteristic",R,N) notificationInfoCharacteristic;
@property (T@"NSString",R,N) userVisibleValue;
@property (TB,R,N) hasUserVisibleValue;
@property (T@"NSString",R,N) contentURLAction;
@property (T@"CAFUserVisibleDetailedDescription",R,N) userVisibleDetailedDescription;
@property (TB,R,N) hasUserVisibleDetailedDescription;
@property (T@"NSString",R,N) userVisibleDescription;
@property (TB,R,N) hasUserVisibleDescription;
@property (T@"CAFSettingNotificationEntry",R,N) notificationInfo;
@property (TB,R,N) hasNotificationInfo;
```

## Class methods

```
+[CAFDeepLinkSetting serviceIdentifier];
+[CAFDeepLinkSetting observerProtocol];
```

## Instance methods

```
-[CAFDeepLinkSetting removeObserver:];
-[CAFDeepLinkSetting notificationInfo];
-[CAFDeepLinkSetting addObserver:];
-[CAFDeepLinkSetting registerObserver:];
-[CAFDeepLinkSetting name];
-[CAFDeepLinkSetting unregisterObserver:];
-[CAFDeepLinkSetting contentURLAction];
-[CAFDeepLinkSetting registeredForContentURLAction];
-[CAFDeepLinkSetting registeredForNotificationInfo];
-[CAFDeepLinkSetting registeredForUserVisibleDescription];
-[CAFDeepLinkSetting registeredForUserVisibleDetailedDescription];
-[CAFDeepLinkSetting registeredForUserVisibleValue];
-[CAFDeepLinkSetting userVisibleDescription];
-[CAFDeepLinkSetting userVisibleDetailedDescription];
-[CAFDeepLinkSetting userVisibleValue];
-[CAFDeepLinkSetting hasUserVisibleValue];
-[CAFDeepLinkSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFDeepLinkSetting contentURLActionCharacteristic];
-[CAFDeepLinkSetting hasNotificationInfo];
-[CAFDeepLinkSetting hasUserVisibleDescription];
-[CAFDeepLinkSetting hasUserVisibleDetailedDescription];
-[CAFDeepLinkSetting notificationInfoCharacteristic];
-[CAFDeepLinkSetting userVisibleDescriptionCharacteristic];
-[CAFDeepLinkSetting userVisibleDetailedDescriptionCharacteristic];
-[CAFDeepLinkSetting userVisibleValueCharacteristic];
```
