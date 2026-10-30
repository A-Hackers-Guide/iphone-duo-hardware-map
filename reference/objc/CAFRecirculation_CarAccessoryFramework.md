# `CAFRecirculation`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 8 properties, 17 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) autoModeCharacteristic;
@property (TB,N) on;
@property (TB,R,N) onDisabled;
@property (TB,R,N) onInvalid;
@property (TB,R,N) onRestricted;
@property (TB,R,N) autoMode;
@property (TB,R,N) hasAutoMode;
```

## Class methods

```
+[CAFRecirculation serviceIdentifier];
+[CAFRecirculation observerProtocol];
```

## Instance methods

```
-[CAFRecirculation on];
-[CAFRecirculation removeObserver:];
-[CAFRecirculation addObserver:];
-[CAFRecirculation setOn:];
-[CAFRecirculation registerObserver:];
-[CAFRecirculation name];
-[CAFRecirculation unregisterObserver:];
-[CAFRecirculation registeredForOn];
-[CAFRecirculation autoMode];
-[CAFRecirculation hasAutoMode];
-[CAFRecirculation onDisabled];
-[CAFRecirculation onInvalid];
-[CAFRecirculation onRestricted];
-[CAFRecirculation registeredForAutoMode];
-[CAFRecirculation _characteristicDidUpdate:fromGroupUpdate:];
-[CAFRecirculation autoModeCharacteristic];
-[CAFRecirculation onCharacteristic];
```
