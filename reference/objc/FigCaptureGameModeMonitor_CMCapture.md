# `FigCaptureGameModeMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 3 instance methods, 1 class methods

## Instance variables

```
i _gameModeNotifyToken;
@? _gameModeStateChangeHandler;
```

## Properties

```
@property (TB,R,GisGameModeEnabled) gameModeEnabled;
```

## Class methods

```
+[FigCaptureGameModeMonitor initialize];
```

## Instance methods

```
-[FigCaptureGameModeMonitor dealloc];
-[FigCaptureGameModeMonitor isGameModeEnabled];
-[FigCaptureGameModeMonitor initWithStateChangeHandler:];
```
