# `_SBKeyboardServiceSceneResolver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBSceneResolving`
- 2 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"SBSystemUIScenesCoordinator" _systemUIScenesCoordinator;
@"<SBSceneStore>" _sceneStore;
```

## Properties

```
@property (T@"SBSystemUIScenesCoordinator",&,N,V_systemUIScenesCoordinator) systemUIScenesCoordinator;
@property (T@"<SBSceneStore>",&,N,V_sceneStore) sceneStore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBKeyboardServiceSceneResolver initWithSceneStore:];
-[_SBKeyboardServiceSceneResolver sceneForSceneIdentityToken:inProcess:];
-[_SBKeyboardServiceSceneResolver sceneStore];
-[_SBKeyboardServiceSceneResolver setSceneStore:];
-[_SBKeyboardServiceSceneResolver setSystemUIScenesCoordinator:];
-[_SBKeyboardServiceSceneResolver systemUIScenesCoordinator];
```
