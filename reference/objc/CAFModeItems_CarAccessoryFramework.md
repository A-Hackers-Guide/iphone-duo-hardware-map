# `CAFModeItems`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 10 properties, 19 instance methods, 0 class methods

## Properties

```
@property (T@"CAFArrayCharacteristic",R,N) identifiersCharacteristic;
@property (T@"CAFUInt32Characteristic",R,N) currentIndexCharacteristic;
@property (T@"CAFUInt32Characteristic",R,N) defaultIndexCharacteristic;
@property (T@"NSArray",R,N) identifiers;
@property (TI,R,N) currentIndex;
@property (T@"CAFUInt32Range",R,N) currentIndexRange;
@property (TB,R,N) currentIndexInvalid;
@property (TI,R,N) defaultIndex;
@property (T@"CAFUInt32Range",R,N) defaultIndexRange;
@property (TB,R,N) hasDefaultIndex;
```

## Instance methods

```
-[CAFModeItems identifiers];
-[CAFModeItems removeObserver:];
-[CAFModeItems addObserver:];
-[CAFModeItems registerObserver:];
-[CAFModeItems currentIndex];
-[CAFModeItems name];
-[CAFModeItems unregisterObserver:];
-[CAFModeItems defaultIndex];
-[CAFModeItems hasDefaultIndex];
-[CAFModeItems currentIndexInvalid];
-[CAFModeItems registeredForCurrentIndex];
-[CAFModeItems _characteristicDidUpdate:fromGroupUpdate:];
-[CAFModeItems currentIndexCharacteristic];
-[CAFModeItems currentIndexRange];
-[CAFModeItems defaultIndexCharacteristic];
-[CAFModeItems defaultIndexRange];
-[CAFModeItems identifiersCharacteristic];
-[CAFModeItems registeredForDefaultIndex];
-[CAFModeItems registeredForIdentifiers];
```
