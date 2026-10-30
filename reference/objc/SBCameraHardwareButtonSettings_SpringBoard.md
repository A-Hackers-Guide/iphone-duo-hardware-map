# `SBCameraHardwareButtonSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
B _shutterButtonShouldUsePocketDetection;
d _shutterButtonLongPressTimeout;
d _shutterButtonLongPressCancellationTimeout;
```

## Properties

```
@property (Td,N,V_shutterButtonLongPressTimeout) shutterButtonLongPressTimeout;
@property (Td,N,V_shutterButtonLongPressCancellationTimeout) shutterButtonLongPressCancellationTimeout;
@property (TB,N,V_shutterButtonShouldUsePocketDetection) shutterButtonShouldUsePocketDetection;
```

## Class methods

```
+[SBCameraHardwareButtonSettings settingsControllerModule];
```

## Instance methods

```
-[SBCameraHardwareButtonSettings setDefaultValues];
-[SBCameraHardwareButtonSettings setShutterButtonLongPressCancellationTimeout:];
-[SBCameraHardwareButtonSettings setShutterButtonLongPressTimeout:];
-[SBCameraHardwareButtonSettings setShutterButtonShouldUsePocketDetection:];
-[SBCameraHardwareButtonSettings shutterButtonLongPressCancellationTimeout];
-[SBCameraHardwareButtonSettings shutterButtonLongPressTimeout];
-[SBCameraHardwareButtonSettings shutterButtonShouldUsePocketDetection];
```
