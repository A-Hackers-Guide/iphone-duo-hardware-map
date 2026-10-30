# `CAFSingleSelectImageSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerSetting`
- 0 instance variables, 13 properties, 25 instance methods, 2 class methods

## Properties

```
@property (T@"CAFUInt8Characteristic",R,N) currentUserVisibleValueCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) listUserVisibleValueCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) imagesCharacteristic;
@property (T@"CAFUserVisibleDetailedDescriptionCharacteristic",R,N) userVisibleDetailedDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (TC,N) currentUserVisibleValue;
@property (T@"CAFUInt8Range",R,N) currentUserVisibleValueRange;
@property (T@"NSArray",R,N) listUserVisibleValue;
@property (T@"NSArray",R,N) images;
@property (T@"CAFUserVisibleDetailedDescription",R,N) userVisibleDetailedDescription;
@property (TB,R,N) hasUserVisibleDetailedDescription;
@property (T@"NSString",R,N) userVisibleDescription;
@property (TB,R,N) hasUserVisibleDescription;
```

## Class methods

```
+[CAFSingleSelectImageSetting serviceIdentifier];
+[CAFSingleSelectImageSetting observerProtocol];
```

## Instance methods

```
-[CAFSingleSelectImageSetting removeObserver:];
-[CAFSingleSelectImageSetting images];
-[CAFSingleSelectImageSetting addObserver:];
-[CAFSingleSelectImageSetting registerObserver:];
-[CAFSingleSelectImageSetting name];
-[CAFSingleSelectImageSetting unregisterObserver:];
-[CAFSingleSelectImageSetting currentUserVisibleValue];
-[CAFSingleSelectImageSetting listUserVisibleValue];
-[CAFSingleSelectImageSetting registeredForCurrentUserVisibleValue];
-[CAFSingleSelectImageSetting registeredForImageList];
-[CAFSingleSelectImageSetting registeredForListUserVisibleValue];
-[CAFSingleSelectImageSetting registeredForUserVisibleDescription];
-[CAFSingleSelectImageSetting registeredForUserVisibleDetailedDescription];
-[CAFSingleSelectImageSetting setCurrentUserVisibleValue:];
-[CAFSingleSelectImageSetting userVisibleDescription];
-[CAFSingleSelectImageSetting userVisibleDetailedDescription];
-[CAFSingleSelectImageSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFSingleSelectImageSetting currentUserVisibleValueCharacteristic];
-[CAFSingleSelectImageSetting currentUserVisibleValueRange];
-[CAFSingleSelectImageSetting hasUserVisibleDescription];
-[CAFSingleSelectImageSetting hasUserVisibleDetailedDescription];
-[CAFSingleSelectImageSetting imagesCharacteristic];
-[CAFSingleSelectImageSetting listUserVisibleValueCharacteristic];
-[CAFSingleSelectImageSetting userVisibleDescriptionCharacteristic];
-[CAFSingleSelectImageSetting userVisibleDetailedDescriptionCharacteristic];
```
