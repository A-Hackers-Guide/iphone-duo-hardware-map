# `CAFAutomakerStatusItem`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 15 properties, 27 instance methods, 0 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) symbolNameCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) sortOrderCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) disabledCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (T@"NSString",R,N) identifier;
@property (T@"NSString",R,N) userVisibleLabel;
@property (TB,R,N) hasUserVisibleLabel;
@property (T@"NSString",R,N) symbolName;
@property (TC,R,N) sortOrder;
@property (TB,R,N) disabled;
@property (TB,R,N) hasDisabled;
@property (TB,R,N) hidden;
@property (TB,R,N) hasHidden;
```

## Instance methods

```
-[CAFAutomakerStatusItem sortOrder];
-[CAFAutomakerStatusItem disabled];
-[CAFAutomakerStatusItem identifier];
-[CAFAutomakerStatusItem removeObserver:];
-[CAFAutomakerStatusItem symbolName];
-[CAFAutomakerStatusItem addObserver:];
-[CAFAutomakerStatusItem registerObserver:];
-[CAFAutomakerStatusItem hasDisabled];
-[CAFAutomakerStatusItem name];
-[CAFAutomakerStatusItem unregisterObserver:];
-[CAFAutomakerStatusItem hidden];
-[CAFAutomakerStatusItem hasHidden];
-[CAFAutomakerStatusItem registeredForDisabled];
-[CAFAutomakerStatusItem registeredForHidden];
-[CAFAutomakerStatusItem registeredForIdentifier];
-[CAFAutomakerStatusItem registeredForSortOrder];
-[CAFAutomakerStatusItem registeredForSymbolName];
-[CAFAutomakerStatusItem registeredForUserVisibleLabel];
-[CAFAutomakerStatusItem userVisibleLabel];
-[CAFAutomakerStatusItem _characteristicDidUpdate:fromGroupUpdate:];
-[CAFAutomakerStatusItem disabledCharacteristic];
-[CAFAutomakerStatusItem hasUserVisibleLabel];
-[CAFAutomakerStatusItem hiddenCharacteristic];
-[CAFAutomakerStatusItem identifierCharacteristic];
-[CAFAutomakerStatusItem sortOrderCharacteristic];
-[CAFAutomakerStatusItem symbolNameCharacteristic];
-[CAFAutomakerStatusItem userVisibleLabelCharacteristic];
```
