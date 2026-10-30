# `CAFStaticSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerSetting`
- 0 instance variables, 11 properties, 21 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) userVisibleValueCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) childrenSettingsIdentifiersCharacteristic;
@property (T@"CAFUserVisibleDetailedDescriptionCharacteristic",R,N) userVisibleDetailedDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"NSString",R,N) userVisibleValue;
@property (T@"NSArray",R,N) childrenSettingsIdentifiers;
@property (TB,R,N) hasChildrenSettingsIdentifiers;
@property (T@"CAFUserVisibleDetailedDescription",R,N) userVisibleDetailedDescription;
@property (TB,R,N) hasUserVisibleDetailedDescription;
@property (T@"NSString",R,N) userVisibleDescription;
@property (TB,R,N) hasUserVisibleDescription;
```

## Class methods

```
+[CAFStaticSetting serviceIdentifier];
+[CAFStaticSetting observerProtocol];
```

## Instance methods

```
-[CAFStaticSetting removeObserver:];
-[CAFStaticSetting addObserver:];
-[CAFStaticSetting registerObserver:];
-[CAFStaticSetting name];
-[CAFStaticSetting unregisterObserver:];
-[CAFStaticSetting childrenSettingsIdentifiers];
-[CAFStaticSetting registeredForChildrenSettingsIdentifiers];
-[CAFStaticSetting registeredForUserVisibleDescription];
-[CAFStaticSetting registeredForUserVisibleDetailedDescription];
-[CAFStaticSetting registeredForUserVisibleValue];
-[CAFStaticSetting userVisibleDescription];
-[CAFStaticSetting userVisibleDetailedDescription];
-[CAFStaticSetting userVisibleValue];
-[CAFStaticSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFStaticSetting childrenSettingsIdentifiersCharacteristic];
-[CAFStaticSetting hasChildrenSettingsIdentifiers];
-[CAFStaticSetting hasUserVisibleDescription];
-[CAFStaticSetting hasUserVisibleDetailedDescription];
-[CAFStaticSetting userVisibleDescriptionCharacteristic];
-[CAFStaticSetting userVisibleDetailedDescriptionCharacteristic];
-[CAFStaticSetting userVisibleValueCharacteristic];
```
