# `PLGameModeService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _previousGameModeState;
@"PLCFNotificationOperatorComposition" _consoleModeListener;
```

## Properties

```
@property (T@"PLCFNotificationOperatorComposition",&,V_consoleModeListener) consoleModeListener;
@property (TB,V_previousGameModeState) previousGameModeState;
```

## Class methods

```
+[PLGameModeService load];
```

## Instance methods

```
-[PLGameModeService setConsoleModeListener:];
-[PLGameModeService init];
-[PLGameModeService initOperatorDependancies];
-[PLGameModeService consoleModeListener];
-[PLGameModeService postGameModeStatusChangeNotification:];
-[PLGameModeService previousGameModeState];
-[PLGameModeService setPreviousGameModeState:];
-[PLGameModeService updateGameMode];
```
