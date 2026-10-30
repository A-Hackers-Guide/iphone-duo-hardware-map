# `CAFActivityIndicator`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 9 properties, 18 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) cameraActiveCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) microphoneActiveCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) locationActiveCharacteristic;
@property (TB,R,N) cameraActive;
@property (TB,R,N) hasCameraActive;
@property (TB,R,N) microphoneActive;
@property (TB,R,N) hasMicrophoneActive;
@property (TB,R,N) locationActive;
@property (TB,R,N) hasLocationActive;
```

## Class methods

```
+[CAFActivityIndicator serviceIdentifier];
+[CAFActivityIndicator observerProtocol];
```

## Instance methods

```
-[CAFActivityIndicator removeObserver:];
-[CAFActivityIndicator addObserver:];
-[CAFActivityIndicator registerObserver:];
-[CAFActivityIndicator name];
-[CAFActivityIndicator unregisterObserver:];
-[CAFActivityIndicator hasCameraActive];
-[CAFActivityIndicator cameraActive];
-[CAFActivityIndicator hasLocationActive];
-[CAFActivityIndicator hasMicrophoneActive];
-[CAFActivityIndicator locationActive];
-[CAFActivityIndicator microphoneActive];
-[CAFActivityIndicator registeredForCameraActive];
-[CAFActivityIndicator registeredForLocationActive];
-[CAFActivityIndicator registeredForMicrophoneActive];
-[CAFActivityIndicator _characteristicDidUpdate:fromGroupUpdate:];
-[CAFActivityIndicator cameraActiveCharacteristic];
-[CAFActivityIndicator locationActiveCharacteristic];
-[CAFActivityIndicator microphoneActiveCharacteristic];
```
