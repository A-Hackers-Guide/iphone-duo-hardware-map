# `CAFOverlayView`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFService`
- 0 instance variables, 14 properties, 27 instance methods, 2 class methods

## Properties

```
@property (T@"CAFStringCharacteristic",R,N) displayPanelIdentifierCharacteristic;
@property (T@"CAFStringCharacteristic",R,N) identifierCharacteristic;
@property (T@"CAFBoolCharacteristic",R,N) onCharacteristic;
@property (T@"CAFFloatCharacteristic",R,N) originXCharacteristic;
@property (T@"CAFFloatCharacteristic",R,N) originYCharacteristic;
@property (T@"CAFFloatCharacteristic",R,N) widthCharacteristic;
@property (T@"CAFFloatCharacteristic",R,N) heightCharacteristic;
@property (T@"NSString",R,N) displayPanelIdentifier;
@property (T@"NSString",R,N) identifier;
@property (TB,R,N) on;
@property (Tf,R,N) originX;
@property (Tf,R,N) originY;
@property (Tf,R,N) width;
@property (Tf,R,N) height;
```

## Class methods

```
+[CAFOverlayView serviceIdentifier];
+[CAFOverlayView observerProtocol];
```

## Instance methods

```
-[CAFOverlayView on];
-[CAFOverlayView identifier];
-[CAFOverlayView removeObserver:];
-[CAFOverlayView addObserver:];
-[CAFOverlayView registerObserver:];
-[CAFOverlayView width];
-[CAFOverlayView name];
-[CAFOverlayView height];
-[CAFOverlayView unregisterObserver:];
-[CAFOverlayView originY];
-[CAFOverlayView originX];
-[CAFOverlayView registeredForOn];
-[CAFOverlayView displayPanelIdentifier];
-[CAFOverlayView registeredForDisplayPanelIdentifier];
-[CAFOverlayView registeredForHeight];
-[CAFOverlayView registeredForIdentifier];
-[CAFOverlayView registeredForOriginX];
-[CAFOverlayView registeredForOriginY];
-[CAFOverlayView registeredForWidth];
-[CAFOverlayView _characteristicDidUpdate:fromGroupUpdate:];
-[CAFOverlayView displayPanelIdentifierCharacteristic];
-[CAFOverlayView heightCharacteristic];
-[CAFOverlayView identifierCharacteristic];
-[CAFOverlayView onCharacteristic];
-[CAFOverlayView originXCharacteristic];
-[CAFOverlayView originYCharacteristic];
-[CAFOverlayView widthCharacteristic];
```
