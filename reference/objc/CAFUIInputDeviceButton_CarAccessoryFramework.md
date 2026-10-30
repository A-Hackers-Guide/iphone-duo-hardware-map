# `CAFUIInputDeviceButton`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFUIInputDevice`
- 0 instance variables, 2 properties, 9 instance methods, 2 class methods

## Properties

```
@property (T@"CAFUIInputDeviceButtonEventCharacteristic",R,N) uiInputDeviceButtonEventCharacteristic;
@property (TC,R,N) uiInputDeviceButtonEvent;
```

## Class methods

```
+[CAFUIInputDeviceButton serviceIdentifier];
+[CAFUIInputDeviceButton observerProtocol];
```

## Instance methods

```
-[CAFUIInputDeviceButton removeObserver:];
-[CAFUIInputDeviceButton addObserver:];
-[CAFUIInputDeviceButton registerObserver:];
-[CAFUIInputDeviceButton name];
-[CAFUIInputDeviceButton unregisterObserver:];
-[CAFUIInputDeviceButton registeredForUIInputDeviceButtonEvent];
-[CAFUIInputDeviceButton uiInputDeviceButtonEvent];
-[CAFUIInputDeviceButton _characteristicDidUpdate:fromGroupUpdate:];
-[CAFUIInputDeviceButton uiInputDeviceButtonEventCharacteristic];
```
