# `CAFVent`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 23 properties, 33 instance methods, 5 class methods

## Properties

```
@property (T@"CAFArrayCharacteristic",R,N) combinationsCharacteristic;
@property (T@"CAFUInt32Characteristic",R,N) currentIndexCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) autoModeCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (T@"NSArray",R,N) combinations;
@property (TI,N) currentIndex;
@property (T@"CAFUInt32Range",R,N) currentIndexRange;
@property (TB,R,N) currentIndexDisabled;
@property (TB,R,N) currentIndexInvalid;
@property (TB,R,N) currentIndexRestricted;
@property (TB,R,N) autoMode;
@property (TB,R,N) hasAutoMode;
@property (TB,N) on;
@property (TB,R,N) hasOn;
@property (TB,R,N) onDisabled;
@property (TB,R,N) onInvalid;
@property (TB,R,N) onRestricted;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFVent serviceIdentifier];
+[CAFVent autoGroupTimer];
+[CAFVent indexBy];
+[CAFVent observerProtocol];
+[CAFVent typeComparator];
```

## Instance methods

```
-[CAFVent on];
-[CAFVent removeObserver:];
-[CAFVent addObserver:];
-[CAFVent setOn:];
-[CAFVent registerObserver:];
-[CAFVent currentIndex];
-[CAFVent name];
-[CAFVent unregisterObserver:];
-[CAFVent setCurrentIndex:];
-[CAFVent combinations];
-[CAFVent registeredForOn];
-[CAFVent autoMode];
-[CAFVent currentIndexDisabled];
-[CAFVent currentIndexInvalid];
-[CAFVent currentIndexRestricted];
-[CAFVent hasAutoMode];
-[CAFVent hasOn];
-[CAFVent onDisabled];
-[CAFVent onInvalid];
-[CAFVent onRestricted];
-[CAFVent registeredForAutoMode];
-[CAFVent registeredForCurrentIndex];
-[CAFVent registeredForVehicleLayoutKey];
-[CAFVent registeredForVentCombinations];
-[CAFVent vehicleLayoutKey];
-[CAFVent _characteristicDidUpdate:fromGroupUpdate:];
-[CAFVent autoModeCharacteristic];
-[CAFVent combinationsCharacteristic];
-[CAFVent currentIndexCharacteristic];
-[CAFVent currentIndexRange];
-[CAFVent onCharacteristic];
-[CAFVent typeCompare:];
-[CAFVent vehicleLayoutKeyCharacteristic];
```
