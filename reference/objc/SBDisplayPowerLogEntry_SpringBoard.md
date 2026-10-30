# `SBDisplayPowerLogEntry`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSString" _displayName;
Q _windowingMode;
Q _zoomLevel;
{CGSize="width"d"height"d} _canvasSize;
{CGSize="width"d"height"d} _nativeSize;
```

## Properties

```
@property (T@"NSString",C,N,V_displayName) displayName;
@property (TQ,N,V_windowingMode) windowingMode;
@property (TQ,N,V_zoomLevel) zoomLevel;
@property (T{CGSize=dd},N,V_canvasSize) canvasSize;
@property (T{CGSize=dd},N,V_nativeSize) nativeSize;
```

## Class methods

```
+[SBDisplayPowerLogEntry forDisplay:mode:zoom:];
```

## Instance methods

```
-[SBDisplayPowerLogEntry canvasSize];
-[SBDisplayPowerLogEntry displayName];
-[SBDisplayPowerLogEntry nativeSize];
-[SBDisplayPowerLogEntry setDisplayName:];
-[SBDisplayPowerLogEntry setCanvasSize:];
-[SBDisplayPowerLogEntry hash];
-[SBDisplayPowerLogEntry setZoomLevel:];
-[SBDisplayPowerLogEntry description];
-[SBDisplayPowerLogEntry copyWithZone:];
-[SBDisplayPowerLogEntry zoomLevel];
-[SBDisplayPowerLogEntry isEqual:];
-[SBDisplayPowerLogEntry logPayload];
-[SBDisplayPowerLogEntry setNativeSize:];
-[SBDisplayPowerLogEntry setWindowingMode:];
-[SBDisplayPowerLogEntry windowingMode];
```
