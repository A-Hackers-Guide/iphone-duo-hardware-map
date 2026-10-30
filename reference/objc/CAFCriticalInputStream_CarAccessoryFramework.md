# `CAFCriticalInputStream`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 4 properties, 12 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) inputStreamUIDCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"NSString",R,N) inputStreamUID;
@property (TB,R,N) on;
```

## Class methods

```
+[CAFCriticalInputStream serviceIdentifier];
+[CAFCriticalInputStream observerProtocol];
```

## Instance methods

```
-[CAFCriticalInputStream on];
-[CAFCriticalInputStream removeObserver:];
-[CAFCriticalInputStream addObserver:];
-[CAFCriticalInputStream registerObserver:];
-[CAFCriticalInputStream name];
-[CAFCriticalInputStream unregisterObserver:];
-[CAFCriticalInputStream registeredForOn];
-[CAFCriticalInputStream inputStreamUID];
-[CAFCriticalInputStream registeredForInputStreamUID];
-[CAFCriticalInputStream _characteristicDidUpdate:fromGroupUpdate:];
-[CAFCriticalInputStream inputStreamUIDCharacteristic];
-[CAFCriticalInputStream onCharacteristic];
```
