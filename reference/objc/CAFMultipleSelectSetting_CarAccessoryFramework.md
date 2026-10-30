# `CAFMultipleSelectSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerSetting`
- 0 instance variables, 10 properties, 21 instance methods, 2 class methods

## Properties

```
@property (T@"CAFSelectSettingEntryListCharacteristic",R,N) selectSettingEntryListCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) selectedEntryIndicesCharacteristic;
@property (T@"CAFUserVisibleDetailedDescriptionCharacteristic",R,N) userVisibleDetailedDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"CAFSelectSettingEntryList",R,N) selectSettingEntryList;
@property (T@"NSArray",C,N) selectedEntryIndices;
@property (T@"CAFUserVisibleDetailedDescription",R,N) userVisibleDetailedDescription;
@property (TB,R,N) hasUserVisibleDetailedDescription;
@property (T@"NSString",R,N) userVisibleDescription;
@property (TB,R,N) hasUserVisibleDescription;
```

## Class methods

```
+[CAFMultipleSelectSetting serviceIdentifier];
+[CAFMultipleSelectSetting observerProtocol];
```

## Instance methods

```
-[CAFMultipleSelectSetting removeObserver:];
-[CAFMultipleSelectSetting addObserver:];
-[CAFMultipleSelectSetting registerObserver:];
-[CAFMultipleSelectSetting name];
-[CAFMultipleSelectSetting unregisterObserver:];
-[CAFMultipleSelectSetting registeredForSelectSettingEntryList];
-[CAFMultipleSelectSetting registeredForSelectedEntryIndices];
-[CAFMultipleSelectSetting registeredForUserVisibleDescription];
-[CAFMultipleSelectSetting registeredForUserVisibleDetailedDescription];
-[CAFMultipleSelectSetting selectSettingEntryList];
-[CAFMultipleSelectSetting selectedEntryIndices];
-[CAFMultipleSelectSetting setSelectedEntryIndices:];
-[CAFMultipleSelectSetting userVisibleDescription];
-[CAFMultipleSelectSetting userVisibleDetailedDescription];
-[CAFMultipleSelectSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFMultipleSelectSetting hasUserVisibleDescription];
-[CAFMultipleSelectSetting hasUserVisibleDetailedDescription];
-[CAFMultipleSelectSetting selectSettingEntryListCharacteristic];
-[CAFMultipleSelectSetting selectedEntryIndicesCharacteristic];
-[CAFMultipleSelectSetting userVisibleDescriptionCharacteristic];
-[CAFMultipleSelectSetting userVisibleDetailedDescriptionCharacteristic];
```
