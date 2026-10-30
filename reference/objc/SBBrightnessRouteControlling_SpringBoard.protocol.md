# `SBBrightnessRouteControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 7 instance methods, 1 class methods

## Properties

```
@property (Tf,R,N) brightnessLevel;
@property (class, TB,R,N) handlesKeyCommands;
```

## Class methods

```
+[SBBrightnessRouteControlling handlesKeyCommands];
```

## Instance methods

```
-[SBBrightnessRouteControlling brightnessLevel];
-[SBBrightnessRouteControlling handleBrightnessKeyPressEvent:];
-[SBBrightnessRouteControlling brightnessRouteType];
-[SBBrightnessRouteControlling cancelBrightnessKeyPressEvent];
-[SBBrightnessRouteControlling noteValueUpdatesDidEnd];
-[SBBrightnessRouteControlling noteValueUpdatesWillBegin];
-[SBBrightnessRouteControlling setBrightnessLevel:animated:];
```
