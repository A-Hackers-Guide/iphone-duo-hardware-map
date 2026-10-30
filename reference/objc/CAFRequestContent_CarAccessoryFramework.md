# `CAFRequestContent`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 10 properties, 22 instance methods, 2 class methods

## Properties

```
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) contentURLCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) userDismissibleCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayZoneIdentifierCharacteristic;
@property (TB,N) on;
@property (T@"NSString",R,N) contentURL;
@property (TB,R,N) userDismissible;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
```

## Class methods

```
+[CAFRequestContent serviceIdentifier];
+[CAFRequestContent observerProtocol];
```

## Instance methods

```
-[CAFRequestContent contentURL];
-[CAFRequestContent on];
-[CAFRequestContent removeObserver:];
-[CAFRequestContent addObserver:];
-[CAFRequestContent setOn:];
-[CAFRequestContent registerObserver:];
-[CAFRequestContent name];
-[CAFRequestContent unregisterObserver:];
-[CAFRequestContent userDismissible];
-[CAFRequestContent registeredForOn];
-[CAFRequestContent displayPanelIdentifier];
-[CAFRequestContent displayZoneIdentifier];
-[CAFRequestContent registeredForContentURL];
-[CAFRequestContent registeredForDisplayPanelIdentifier];
-[CAFRequestContent registeredForDisplayZoneIdentifier];
-[CAFRequestContent registeredForUserDismissible];
-[CAFRequestContent _characteristicDidUpdate:fromGroupUpdate:];
-[CAFRequestContent contentURLCharacteristic];
-[CAFRequestContent displayPanelIdentifierCharacteristic];
-[CAFRequestContent displayZoneIdentifierCharacteristic];
-[CAFRequestContent onCharacteristic];
-[CAFRequestContent userDismissibleCharacteristic];
```
