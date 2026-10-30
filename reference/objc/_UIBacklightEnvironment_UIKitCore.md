# `_UIBacklightEnvironment`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIWindowSceneComponentProviding`, `BLSBacklightSceneEnvironmentDelegate`
- 4 instance variables, 7 properties, 19 instance methods, 5 class methods

## Instance variables

```
@"BLSBacklightSceneVisualState" _visualState;
@"NSHashTable" _observers;
B _shouldDeferWakeAnimationStart;
@"UIScene" _scene;
```

## Properties

```
@property (TB,N,V_shouldDeferWakeAnimationStart) shouldDeferWakeAnimationStart;
@property (T@"UITraitCollection",?,R,N) _traitOverrides;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIBacklightEnvironment _backlightEnvironmentSupported];
+[_UIBacklightEnvironment _performOnChildViewControllersForAlwaysOnTimelines:performBlock:withCompletion:];
+[_UIBacklightEnvironment _alwaysOnSupported];
+[_UIBacklightEnvironment _defaultAnimationDuration];
+[_UIBacklightEnvironment _postSynchronizeQueue];
```

## Instance methods

```
-[_UIBacklightEnvironment _windowScene];
-[_UIBacklightEnvironment updateSceneWithFrameSpecifier:layout:completion:];
-[_UIBacklightEnvironment transitionTraitsInUpdate:animations:completion:];
-[_UIBacklightEnvironment _scene];
-[_UIBacklightEnvironment removeObserver:];
-[_UIBacklightEnvironment _traitOverrides];
-[_UIBacklightEnvironment setShouldDeferWakeAnimationStart:];
-[_UIBacklightEnvironment environment:performBacklightSceneUpdate:];
-[_UIBacklightEnvironment _enumerateAllObserversWithBlock:];
-[_UIBacklightEnvironment initWithScene:];
-[_UIBacklightEnvironment addObserver:];
-[_UIBacklightEnvironment environment:timelinesForDateInterval:previousSpecifier:completion:];
-[_UIBacklightEnvironment _notifyObserversIfEnvironmentVisualStateDidChangeFromActiveOn:];
-[_UIBacklightEnvironment isObserver:];
-[_UIBacklightEnvironment _commit:andPerformPostSynchronizeBlock:];
-[_UIBacklightEnvironment _notifyObserversIfEnvironmentVisualStateDidChangeToActiveOn:];
-[_UIBacklightEnvironment _setScene:];
-[_UIBacklightEnvironment shouldDeferWakeAnimationStart];
-[_UIBacklightEnvironment _notifyObserversEnvironmentVisualStateWillChangeToState:];
```
