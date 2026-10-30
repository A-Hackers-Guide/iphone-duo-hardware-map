# `SBDisplayBrightnessController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHIDValueModifyingButtonSetArbiterDelegate`, `SBBrightnessRouteControlling`
- 6 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
^{BKSDisplayBrightnessTransaction=} _brightnessTransaction;
@"<SBBrightnessRouteCoordinating>" _coordinator;
@"SBHIDValueModifyingButtonSetArbiter" _buttonArbiter;
@"SBUIViewFloatSpringProperty" _brightnessProperty;
@"BrightnessSystemClient" _brightnessSystemClient;
B _brightnessControlAvailable;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tf,R,N) brightnessLevel;
```

## Class methods

```
+[SBDisplayBrightnessController handlesKeyCommands];
```

## Instance methods

```
-[SBDisplayBrightnessController dealloc];
-[SBDisplayBrightnessController brightnessLevel];
-[SBDisplayBrightnessController initWithCoordinator:];
-[SBDisplayBrightnessController _setBrightnessLevel:animated:];
-[SBDisplayBrightnessController handleBrightnessKeyPressEvent:];
-[SBDisplayBrightnessController _beginBrightnessTransaction];
-[SBDisplayBrightnessController _brightnessControlAvailabilityDidChange];
-[SBDisplayBrightnessController _completeBrightnessTransaction];
-[SBDisplayBrightnessController _effectiveCurrentTargetBrightness];
-[SBDisplayBrightnessController _isBrightnessPropertyRunning];
-[SBDisplayBrightnessController brightnessRouteType];
-[SBDisplayBrightnessController buttonSetArbiter:performActionForButtonPage:usage:];
-[SBDisplayBrightnessController buttonSetArbiterDidReset:];
-[SBDisplayBrightnessController cancelBrightnessKeyPressEvent];
-[SBDisplayBrightnessController noteValueUpdatesDidEnd];
-[SBDisplayBrightnessController noteValueUpdatesWillBegin];
-[SBDisplayBrightnessController setBrightnessLevel:animated:];
```
