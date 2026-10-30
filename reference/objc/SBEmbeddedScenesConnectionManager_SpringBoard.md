# `SBEmbeddedScenesConnectionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _mainSBWindowScenes;
@"NSHashTable" _systemApertureScenes;
@"NSHashTable" _systemApertureCurtainScenes;
@"SBWindowScene" _mainSBWindowScene;
@"UIWindowScene" _systemApertureScene;
@"UIWindowScene" _systemApertureCurtainScene;
```

## Instance methods

```
-[SBEmbeddedScenesConnectionManager _reevaluateSceneConnection];
-[SBEmbeddedScenesConnectionManager noteMainSceneConnected:];
-[SBEmbeddedScenesConnectionManager noteSystemApertureCurtainSceneConnected:];
-[SBEmbeddedScenesConnectionManager noteSystemApertureSceneConnected:];
```
