# `CAFCameraGeneral`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 4 properties, 13 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) userDismissibleCharacteristic;
@property (TB,N) on;
@property (TB,R,N) userDismissible;
```

## Class methods

```
+[CAFCameraGeneral serviceIdentifier];
+[CAFCameraGeneral observerProtocol];
```

## Instance methods

```
-[CAFCameraGeneral on];
-[CAFCameraGeneral removeObserver:];
-[CAFCameraGeneral addObserver:];
-[CAFCameraGeneral setOn:];
-[CAFCameraGeneral registerObserver:];
-[CAFCameraGeneral name];
-[CAFCameraGeneral unregisterObserver:];
-[CAFCameraGeneral userDismissible];
-[CAFCameraGeneral registeredForOn];
-[CAFCameraGeneral registeredForUserDismissible];
-[CAFCameraGeneral _characteristicDidUpdate:fromGroupUpdate:];
-[CAFCameraGeneral onCharacteristic];
-[CAFCameraGeneral userDismissibleCharacteristic];
```
