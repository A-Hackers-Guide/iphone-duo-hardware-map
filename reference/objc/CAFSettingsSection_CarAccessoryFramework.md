# `CAFSettingsSection`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 10 properties, 20 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleSectionNameCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleFooterCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) sortOrderCharacteristic;
@property (T@"NSString",R,N) identifier;
@property (T@"NSString",R,N) userVisibleSectionName;
@property (TB,R,N) hasUserVisibleSectionName;
@property (T@"NSString",R,N) userVisibleFooter;
@property (TB,R,N) hasUserVisibleFooter;
@property (TC,R,N) sortOrder;
```

## Class methods

```
+[CAFSettingsSection serviceIdentifier];
+[CAFSettingsSection observerProtocol];
```

## Instance methods

```
-[CAFSettingsSection sortOrder];
-[CAFSettingsSection identifier];
-[CAFSettingsSection removeObserver:];
-[CAFSettingsSection addObserver:];
-[CAFSettingsSection registerObserver:];
-[CAFSettingsSection name];
-[CAFSettingsSection unregisterObserver:];
-[CAFSettingsSection registeredForIdentifier];
-[CAFSettingsSection registeredForSortOrder];
-[CAFSettingsSection registeredForUserVisibleFooter];
-[CAFSettingsSection registeredForUserVisibleSectionName];
-[CAFSettingsSection userVisibleFooter];
-[CAFSettingsSection userVisibleSectionName];
-[CAFSettingsSection userVisibleFooterCharacteristic];
-[CAFSettingsSection _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSettingsSection hasUserVisibleFooter];
-[CAFSettingsSection hasUserVisibleSectionName];
-[CAFSettingsSection identifierCharacteristic];
-[CAFSettingsSection sortOrderCharacteristic];
-[CAFSettingsSection userVisibleSectionNameCharacteristic];
```
