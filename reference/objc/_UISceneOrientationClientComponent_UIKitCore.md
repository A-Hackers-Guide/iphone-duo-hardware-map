# `_UISceneOrientationClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `FBSSceneObserver`, `_UISceneOrientationClientComponent`
- 2 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIWindowScene" _windowScene;
@"_UIWindowSceneTraitOverrideHandle" __traitHandle;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) interfaceOrientationLockState;
@property (TB,R,N,GisInterfaceOrientationLocked) interfaceOrientationLocked;
@property (Tq,N) interfaceOrientationLockPreference;
```

## Instance methods

```
-[_UISceneOrientationClientComponent isInterfaceOrientationLocked];
-[_UISceneOrientationClientComponent debugDescription];
-[_UISceneOrientationClientComponent scene:didUpdateSettings:];
-[_UISceneOrientationClientComponent setInterfaceOrientationLockPreference:];
-[_UISceneOrientationClientComponent evaluateInterfaceOrientationLockPreferenceIfNeeded];
-[_UISceneOrientationClientComponent interfaceOrientationLockPreference];
-[_UISceneOrientationClientComponent setScene:];
-[_UISceneOrientationClientComponent invalidate];
-[_UISceneOrientationClientComponent description];
-[_UISceneOrientationClientComponent appendDescriptionToStream:];
-[_UISceneOrientationClientComponent interfaceOrientationLockState];
```
