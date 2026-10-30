# `CAFAutomakerApp`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 4 properties, 12 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) appClipIdentifierCharacteristic;
@property (T@"NSString",R,N) identifier;
@property (T@"NSString",R,N) appClipIdentifier;
```

## Class methods

```
+[CAFAutomakerApp serviceIdentifier];
+[CAFAutomakerApp observerProtocol];
```

## Instance methods

```
-[CAFAutomakerApp identifier];
-[CAFAutomakerApp removeObserver:];
-[CAFAutomakerApp addObserver:];
-[CAFAutomakerApp registerObserver:];
-[CAFAutomakerApp name];
-[CAFAutomakerApp unregisterObserver:];
-[CAFAutomakerApp appClipIdentifier];
-[CAFAutomakerApp registeredForAppClipIdentifier];
-[CAFAutomakerApp registeredForIdentifier];
-[CAFAutomakerApp appClipIdentifierCharacteristic];
-[CAFAutomakerApp _characteristicDidUpdate:fromGroupUpdate:];
-[CAFAutomakerApp identifierCharacteristic];
```
