# `CAFFuelRemainingRange`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFDistanceDisplay`
- 0 instance variables, 3 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) hiddenCharacteristic;
@property (TB,R,N) hidden;
@property (TB,R,N) hasHidden;
```

## Class methods

```
+[CAFFuelRemainingRange serviceIdentifier];
+[CAFFuelRemainingRange observerProtocol];
```

## Instance methods

```
-[CAFFuelRemainingRange removeObserver:];
-[CAFFuelRemainingRange addObserver:];
-[CAFFuelRemainingRange registerObserver:];
-[CAFFuelRemainingRange name];
-[CAFFuelRemainingRange unregisterObserver:];
-[CAFFuelRemainingRange hidden];
-[CAFFuelRemainingRange hasHidden];
-[CAFFuelRemainingRange registeredForHidden];
-[CAFFuelRemainingRange _characteristicDidUpdate:fromGroupUpdate:];
-[CAFFuelRemainingRange hiddenCharacteristic];
```
