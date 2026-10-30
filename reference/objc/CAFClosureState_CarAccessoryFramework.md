# `CAFClosureState`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- Protocols: `CAFPositionedRequired`
- 0 instance variables, 9 properties, 13 instance methods, 3 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) latchStateCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) vehicleLayoutKeyCharacteristic;
@property (TB,R,N) latchState;
@property (TB,R,N) latchStateInvalid;
@property (T@"NSString",R,N) vehicleLayoutKey;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAFClosureState serviceIdentifier];
+[CAFClosureState indexBy];
+[CAFClosureState observerProtocol];
```

## Instance methods

```
-[CAFClosureState removeObserver:];
-[CAFClosureState addObserver:];
-[CAFClosureState registerObserver:];
-[CAFClosureState name];
-[CAFClosureState unregisterObserver:];
-[CAFClosureState latchState];
-[CAFClosureState registeredForLatchState];
-[CAFClosureState registeredForVehicleLayoutKey];
-[CAFClosureState vehicleLayoutKey];
-[CAFClosureState _characteristicDidUpdate:fromGroupUpdate:];
-[CAFClosureState latchStateCharacteristic];
-[CAFClosureState latchStateInvalid];
-[CAFClosureState vehicleLayoutKeyCharacteristic];
```
