# `BLSHOSDisplayInterfaceProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BLSDisplay`
- 0 instance variables, 11 properties, 22 instance methods, 0 class methods

## Properties

```
@property (T@"<BLSDisplayStateDelegate>",&,SsetDisplayStateDelegate:) displayStateDelegate;
@property (Tq,R,N) cbDisplayMode;
@property (TB,R,N) highLuminanceAODsupportedInCB;
@property (TB,R,N) supportsFlipbookState;
@property (Tq,R,N) cbFlipbookState;
@property (Tq,R,N) caDisplayState;
@property (Tq,R,N) caDisplayPowerState;
@property (TB,N,GisCloningDisabled) cloningDisabled;
@property (TB,R,N,GisSuppressionServiceActive) suppressionServiceActive;
@property (T@"BLSHSuppressionEvent",R,N) lastSuppressionEvent;
@property (Ti,R,N) surfaceType;
```

## Instance methods

```
-[BLSHOSDisplayInterfaceProviding cbDisplayMode];
-[BLSHOSDisplayInterfaceProviding createFlipbook];
-[BLSHOSDisplayInterfaceProviding surfaceType];
-[BLSHOSDisplayInterfaceProviding isCloningDisabled];
-[BLSHOSDisplayInterfaceProviding displayStateDelegate];
-[BLSHOSDisplayInterfaceProviding setCloningDisabled:];
-[BLSHOSDisplayInterfaceProviding cbFlipbookState];
-[BLSHOSDisplayInterfaceProviding isSuppressionServiceActive];
-[BLSHOSDisplayInterfaceProviding transitionToCADisplayState:];
-[BLSHOSDisplayInterfaceProviding transitionToDisplayMode:withDuration:didChangeAlwaysOnBrightnessCurve:];
-[BLSHOSDisplayInterfaceProviding highLuminanceAODsupportedInCB];
-[BLSHOSDisplayInterfaceProviding caDisplayState];
-[BLSHOSDisplayInterfaceProviding supportsFlipbookState];
-[BLSHOSDisplayInterfaceProviding switchToFlipbookState:];
-[BLSHOSDisplayInterfaceProviding caDisplayPowerState];
-[BLSHOSDisplayInterfaceProviding createDisplayPowerResourceHintWithState:];
-[BLSHOSDisplayInterfaceProviding lastSuppressionEvent];
-[BLSHOSDisplayInterfaceProviding acquireDisplayPowerAssertionForReason:];
-[BLSHOSDisplayInterfaceProviding setDisplayStateDelegate:];
-[BLSHOSDisplayInterfaceProviding endSuppressionService];
-[BLSHOSDisplayInterfaceProviding startSuppressionServiceWithHandler:];
-[BLSHOSDisplayInterfaceProviding didDetectSignificantUserInteraction];
```
