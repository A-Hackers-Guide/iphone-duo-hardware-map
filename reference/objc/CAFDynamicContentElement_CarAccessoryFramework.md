# `CAFDynamicContentElement`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 8 properties, 18 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) dynamicContentURLCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) userDismissibleCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) displayZoneIdentifierCharacteristic;
@property (T@"NSString",R,N) dynamicContentURL;
@property (TB,R,N) userDismissible;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) displayZoneIdentifier;
```

## Class methods

```
+[CAFDynamicContentElement serviceIdentifier];
+[CAFDynamicContentElement observerProtocol];
```

## Instance methods

```
-[CAFDynamicContentElement removeObserver:];
-[CAFDynamicContentElement addObserver:];
-[CAFDynamicContentElement registerObserver:];
-[CAFDynamicContentElement name];
-[CAFDynamicContentElement unregisterObserver:];
-[CAFDynamicContentElement userDismissible];
-[CAFDynamicContentElement displayPanelIdentifier];
-[CAFDynamicContentElement displayZoneIdentifier];
-[CAFDynamicContentElement dynamicContentURL];
-[CAFDynamicContentElement registeredForDisplayPanelIdentifier];
-[CAFDynamicContentElement registeredForDisplayZoneIdentifier];
-[CAFDynamicContentElement registeredForDynamicContentURL];
-[CAFDynamicContentElement registeredForUserDismissible];
-[CAFDynamicContentElement dynamicContentURLCharacteristic];
-[CAFDynamicContentElement _characteristicDidUpdate:fromGroupUpdate:];
-[CAFDynamicContentElement displayPanelIdentifierCharacteristic];
-[CAFDynamicContentElement displayZoneIdentifierCharacteristic];
-[CAFDynamicContentElement userDismissibleCharacteristic];
```
