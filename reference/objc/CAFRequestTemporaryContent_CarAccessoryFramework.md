# `CAFRequestTemporaryContent`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 10 properties, 24 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) temporaryContentURLCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayZoneIdentifierCharacteristic;
@property (T@"CAFTemporaryContentChangedControl",R,N) temporaryContentChangedControl;
@property (TB,N) on;
@property (T@"NSString",C,N) temporaryContentURL;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
@property (TB,R,N) hasTemporaryContentChanged;
```

## Class methods

```
+[CAFRequestTemporaryContent serviceIdentifier];
+[CAFRequestTemporaryContent observerProtocol];
```

## Instance methods

```
-[CAFRequestTemporaryContent on];
-[CAFRequestTemporaryContent removeObserver:];
-[CAFRequestTemporaryContent addObserver:];
-[CAFRequestTemporaryContent setOn:];
-[CAFRequestTemporaryContent registerObserver:];
-[CAFRequestTemporaryContent name];
-[CAFRequestTemporaryContent unregisterObserver:];
-[CAFRequestTemporaryContent registeredForOn];
-[CAFRequestTemporaryContent displayPanelIdentifier];
-[CAFRequestTemporaryContent displayZoneIdentifier];
-[CAFRequestTemporaryContent registeredForDisplayPanelIdentifier];
-[CAFRequestTemporaryContent registeredForDisplayZoneIdentifier];
-[CAFRequestTemporaryContent registeredForTemporaryContentURL];
-[CAFRequestTemporaryContent setTemporaryContentURL:];
-[CAFRequestTemporaryContent temporaryContentURL];
-[CAFRequestTemporaryContent _characteristicDidUpdate:fromGroupUpdate:];
-[CAFRequestTemporaryContent displayPanelIdentifierCharacteristic];
-[CAFRequestTemporaryContent displayZoneIdentifierCharacteristic];
-[CAFRequestTemporaryContent hasTemporaryContentChanged];
-[CAFRequestTemporaryContent onCharacteristic];
-[CAFRequestTemporaryContent registeredForTemporaryContentChanged];
-[CAFRequestTemporaryContent temporaryContentChangedControl];
-[CAFRequestTemporaryContent temporaryContentChangedWithOn:temporaryContentURL:completion:];
-[CAFRequestTemporaryContent temporaryContentURLCharacteristic];
```
