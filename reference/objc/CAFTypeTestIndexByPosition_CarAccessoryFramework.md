# `CAFTypeTestIndexByPosition`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 10 properties, 15 instance methods, 3 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (T@"CAFInt32Characteristic",R,N) testInt32Characteristic;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (Ti,N) testInt32;
@property (T@"CAFInt32Range",R,N) testInt32Range;
@property (TB,R,N) hasTestInt32;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFTypeTestIndexByPosition serviceIdentifier];
+[CAFTypeTestIndexByPosition indexBy];
+[CAFTypeTestIndexByPosition observerProtocol];
```

## Instance methods

```
-[CAFTypeTestIndexByPosition removeObserver:];
-[CAFTypeTestIndexByPosition addObserver:];
-[CAFTypeTestIndexByPosition registerObserver:];
-[CAFTypeTestIndexByPosition name];
-[CAFTypeTestIndexByPosition unregisterObserver:];
-[CAFTypeTestIndexByPosition hasTestInt32];
-[CAFTypeTestIndexByPosition registeredForTestInt32];
-[CAFTypeTestIndexByPosition registeredForVehicleLayoutKey];
-[CAFTypeTestIndexByPosition setTestInt32:];
-[CAFTypeTestIndexByPosition testInt32];
-[CAFTypeTestIndexByPosition vehicleLayoutKey];
-[CAFTypeTestIndexByPosition _characteristicDidUpdate:fromGroupUpdate:];
-[CAFTypeTestIndexByPosition testInt32Characteristic];
-[CAFTypeTestIndexByPosition testInt32Range];
-[CAFTypeTestIndexByPosition vehicleLayoutKeyCharacteristic];
```
