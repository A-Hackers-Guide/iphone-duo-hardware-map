# `CAFEqualizer`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 12 properties, 23 instance methods, 2 class methods

## Properties

```
@property (T@"CAFEqualizerTypeCharacteristic",R,N) typeCharacteristic;
@property (T@"CAFUInt8Characteristic",R,N) sortOrderCharacteristic;
@property (T@"CAFInt8Characteristic",R,N) valueCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) userVisibleLabelCharacteristic;
@property (TC,R,N) type;
@property (TC,R,N) sortOrder;
@property (Tc,N) value;
@property (T@"CAFInt8Range",R,N) valueRange;
@property (TB,R,N) valueDisabled;
@property (TB,R,N) valueHidden;
@property (T@"NSString",R,N) userVisibleLabel;
@property (TB,R,N) hasUserVisibleLabel;
```

## Class methods

```
+[CAFEqualizer serviceIdentifier];
+[CAFEqualizer observerProtocol];
```

## Instance methods

```
-[CAFEqualizer sortOrder];
-[CAFEqualizer removeObserver:];
-[CAFEqualizer value];
-[CAFEqualizer addObserver:];
-[CAFEqualizer valueRange];
-[CAFEqualizer setValue:];
-[CAFEqualizer type];
-[CAFEqualizer registerObserver:];
-[CAFEqualizer name];
-[CAFEqualizer unregisterObserver:];
-[CAFEqualizer registeredForEqualizerType];
-[CAFEqualizer registeredForEqualizerValue];
-[CAFEqualizer registeredForSortOrder];
-[CAFEqualizer registeredForUserVisibleLabel];
-[CAFEqualizer userVisibleLabel];
-[CAFEqualizer valueDisabled];
-[CAFEqualizer valueHidden];
-[CAFEqualizer _characteristicDidUpdate:fromGroupUpdate:];
-[CAFEqualizer hasUserVisibleLabel];
-[CAFEqualizer sortOrderCharacteristic];
-[CAFEqualizer typeCharacteristic];
-[CAFEqualizer userVisibleLabelCharacteristic];
-[CAFEqualizer valueCharacteristic];
```
