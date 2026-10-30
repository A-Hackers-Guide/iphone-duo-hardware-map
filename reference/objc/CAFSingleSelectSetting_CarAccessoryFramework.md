# `CAFSingleSelectSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerSetting`
- 0 instance variables, 14 properties, 26 instance methods, 2 class methods

## Properties

```
@property (T@"CAFSelectSettingEntryListCharacteristic",R,N) selectSettingEntryListCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) selectedEntryIndexCharacteristic;
@property (T@"CAFUserVisibleDetailedDescriptionCharacteristic",R,N) userVisibleDetailedDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFSelectSettingNotificationEntryListCharacteristic",R,N) selectSettingEntryListNotificationInfoCharacteristic;
@property (T@"CAFSelectSettingEntryList",R,N) selectSettingEntryList;
@property (TC,N) selectedEntryIndex;
@property (T@"CAFUInt8Range",R,N) selectedEntryIndexRange;
@property (T@"CAFUserVisibleDetailedDescription",R,N) userVisibleDetailedDescription;
@property (TB,R,N) hasUserVisibleDetailedDescription;
@property (T@"NSString",R,N) userVisibleDescription;
@property (TB,R,N) hasUserVisibleDescription;
@property (T@"CAFSelectSettingNotificationEntryList",R,N) selectSettingEntryListNotificationInfo;
@property (TB,R,N) hasSelectSettingEntryListNotificationInfo;
```

## Class methods

```
+[CAFSingleSelectSetting serviceIdentifier];
+[CAFSingleSelectSetting observerProtocol];
```

## Instance methods

```
-[CAFSingleSelectSetting removeObserver:];
-[CAFSingleSelectSetting addObserver:];
-[CAFSingleSelectSetting registerObserver:];
-[CAFSingleSelectSetting name];
-[CAFSingleSelectSetting unregisterObserver:];
-[CAFSingleSelectSetting registeredForSelectedEntryIndex];
-[CAFSingleSelectSetting registeredForSelectSettingEntryList];
-[CAFSingleSelectSetting registeredForSelectSettingEntryListNotificationInfo];
-[CAFSingleSelectSetting registeredForUserVisibleDescription];
-[CAFSingleSelectSetting registeredForUserVisibleDetailedDescription];
-[CAFSingleSelectSetting selectSettingEntryList];
-[CAFSingleSelectSetting selectSettingEntryListNotificationInfo];
-[CAFSingleSelectSetting selectedEntryIndex];
-[CAFSingleSelectSetting setSelectedEntryIndex:];
-[CAFSingleSelectSetting userVisibleDescription];
-[CAFSingleSelectSetting userVisibleDetailedDescription];
-[CAFSingleSelectSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSingleSelectSetting hasSelectSettingEntryListNotificationInfo];
-[CAFSingleSelectSetting hasUserVisibleDescription];
-[CAFSingleSelectSetting hasUserVisibleDetailedDescription];
-[CAFSingleSelectSetting selectSettingEntryListCharacteristic];
-[CAFSingleSelectSetting selectSettingEntryListNotificationInfoCharacteristic];
-[CAFSingleSelectSetting selectedEntryIndexCharacteristic];
-[CAFSingleSelectSetting selectedEntryIndexRange];
-[CAFSingleSelectSetting userVisibleDescriptionCharacteristic];
-[CAFSingleSelectSetting userVisibleDetailedDescriptionCharacteristic];
```
