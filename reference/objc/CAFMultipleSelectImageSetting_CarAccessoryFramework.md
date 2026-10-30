# `CAFMultipleSelectImageSetting`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAutomakerSetting`
- 0 instance variables, 12 properties, 24 instance methods, 2 class methods

## Properties

```
@property (T@"CAFArrayCharacteristic",R,N) indicesUserVisibleValueCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) listUserVisibleValueCharacteristic;
@property (T@"CAFArrayCharacteristic",R,N) imagesCharacteristic;
@property (T@"CAFUserVisibleDetailedDescriptionCharacteristic",R,N) userVisibleDetailedDescriptionCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleDescriptionCharacteristic;
@property (T@"NSArray",C,N) indicesUserVisibleValue;
@property (T@"NSArray",R,N) listUserVisibleValue;
@property (T@"NSArray",R,N) images;
@property (T@"CAFUserVisibleDetailedDescription",R,N) userVisibleDetailedDescription;
@property (TB,R,N) hasUserVisibleDetailedDescription;
@property (T@"NSString",R,N) userVisibleDescription;
@property (TB,R,N) hasUserVisibleDescription;
```

## Class methods

```
+[CAFMultipleSelectImageSetting serviceIdentifier];
+[CAFMultipleSelectImageSetting observerProtocol];
```

## Instance methods

```
-[CAFMultipleSelectImageSetting removeObserver:];
-[CAFMultipleSelectImageSetting images];
-[CAFMultipleSelectImageSetting addObserver:];
-[CAFMultipleSelectImageSetting registerObserver:];
-[CAFMultipleSelectImageSetting name];
-[CAFMultipleSelectImageSetting unregisterObserver:];
-[CAFMultipleSelectImageSetting indicesUserVisibleValue];
-[CAFMultipleSelectImageSetting listUserVisibleValue];
-[CAFMultipleSelectImageSetting registeredForImageList];
-[CAFMultipleSelectImageSetting registeredForIndicesUserVisibleValue];
-[CAFMultipleSelectImageSetting registeredForListUserVisibleValue];
-[CAFMultipleSelectImageSetting registeredForUserVisibleDescription];
-[CAFMultipleSelectImageSetting registeredForUserVisibleDetailedDescription];
-[CAFMultipleSelectImageSetting setIndicesUserVisibleValue:];
-[CAFMultipleSelectImageSetting userVisibleDescription];
-[CAFMultipleSelectImageSetting userVisibleDetailedDescription];
-[CAFMultipleSelectImageSetting _characteristicDidUpdate:fromGroupUpdate:];
-[CAFMultipleSelectImageSetting hasUserVisibleDescription];
-[CAFMultipleSelectImageSetting hasUserVisibleDetailedDescription];
-[CAFMultipleSelectImageSetting imagesCharacteristic];
-[CAFMultipleSelectImageSetting indicesUserVisibleValueCharacteristic];
-[CAFMultipleSelectImageSetting listUserVisibleValueCharacteristic];
-[CAFMultipleSelectImageSetting userVisibleDescriptionCharacteristic];
-[CAFMultipleSelectImageSetting userVisibleDetailedDescriptionCharacteristic];
```
