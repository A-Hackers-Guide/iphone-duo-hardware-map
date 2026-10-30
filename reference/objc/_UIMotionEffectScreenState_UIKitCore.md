# `_UIMotionEffectScreenState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _screenDimmed;
@"NSMutableDictionary" _bodyGroups;
@"UIScreen" _screen;
@"CADisplayLink" _displayLink;
@"_UIMotionEffectEvent" _lastProcessedEvent;
@"_UIMotionEffectEvent" _lastEvent;
@"<BLSBacklightStateObservable>" _backlight;
```

## Properties

```
@property (T@"UIScreen",W,N,V_screen) screen;
@property (T@"CADisplayLink",&,N,V_displayLink) displayLink;
@property (T@"NSMutableDictionary",&,N,V_bodyGroups) bodyGroups;
@property (T@"_UIMotionEffectEvent",&,N,V_lastProcessedEvent) lastProcessedEvent;
@property (T@"_UIMotionEffectEvent",&,N,V_lastEvent) lastEvent;
@property (TB,N,V_screenDimmed) screenDimmed;
@property (T@"<BLSBacklightStateObservable>",&,N,V_backlight) backlight;
```

## Instance methods

```
-[_UIMotionEffectScreenState displayLink];
-[_UIMotionEffectScreenState screen];
-[_UIMotionEffectScreenState bodyGroups];
-[_UIMotionEffectScreenState setBacklight:];
-[_UIMotionEffectScreenState lastProcessedEvent];
-[_UIMotionEffectScreenState setScreen:];
-[_UIMotionEffectScreenState setDisplayLink:];
-[_UIMotionEffectScreenState setScreenDimmed:];
-[_UIMotionEffectScreenState setLastEvent:];
-[_UIMotionEffectScreenState lastEvent];
-[_UIMotionEffectScreenState setLastProcessedEvent:];
-[_UIMotionEffectScreenState screenDimmed];
-[_UIMotionEffectScreenState setBodyGroups:];
-[_UIMotionEffectScreenState backlight];
```
