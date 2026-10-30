# `SBActionHardwareButtonSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 2 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
d _longPressTime;
d _longPressTimeWhenSuppressed;
```

## Properties

```
@property (Td,N,V_longPressTime) longPressTime;
@property (Td,N,V_longPressTimeWhenSuppressed) longPressTimeWhenSuppressed;
@property (T@"SBActionButtonParameters",C,N) actionButtonParameters;
```

## Class methods

```
+[SBActionHardwareButtonSettings settingsControllerModule];
```

## Instance methods

```
-[SBActionHardwareButtonSettings setDefaultValues];
-[SBActionHardwareButtonSettings setLongPressTimeWhenSuppressed:];
-[SBActionHardwareButtonSettings actionButtonParameters];
-[SBActionHardwareButtonSettings longPressTime];
-[SBActionHardwareButtonSettings longPressTimeWhenSuppressed];
-[SBActionHardwareButtonSettings setActionButtonParameters:];
-[SBActionHardwareButtonSettings setLongPressTime:];
```
