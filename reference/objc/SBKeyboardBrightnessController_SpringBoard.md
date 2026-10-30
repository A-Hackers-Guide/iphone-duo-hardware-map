# `SBKeyboardBrightnessController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHIDValueModifyingButtonSetArbiterDelegate`, `SBBrightnessRouteControlling`
- 3 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"<SBBrightnessRouteCoordinating>" _coordinator;
@"KeyboardBrightnessClient" _keyboardBrightnessClient;
@"SBHIDValueModifyingButtonSetArbiter" _buttonArbiter;
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
+[SBKeyboardBrightnessController handlesKeyCommands];
```

## Instance methods

```
-[SBKeyboardBrightnessController brightnessLevel];
-[SBKeyboardBrightnessController initWithCoordinator:];
-[SBKeyboardBrightnessController _setBrightnessLevel:animated:];
-[SBKeyboardBrightnessController handleBrightnessKeyPressEvent:];
-[SBKeyboardBrightnessController _currentBrightness];
-[SBKeyboardBrightnessController brightnessRouteType];
-[SBKeyboardBrightnessController buttonSetArbiter:performActionForButtonPage:usage:];
-[SBKeyboardBrightnessController buttonSetArbiterDidReset:];
-[SBKeyboardBrightnessController cancelBrightnessKeyPressEvent];
-[SBKeyboardBrightnessController noteValueUpdatesDidEnd];
-[SBKeyboardBrightnessController noteValueUpdatesWillBegin];
-[SBKeyboardBrightnessController setBrightnessLevel:animated:];
```
