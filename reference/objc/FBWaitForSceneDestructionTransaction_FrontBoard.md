# `FBWaitForSceneDestructionTransaction`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBTransaction`
- Protocols: `FBSceneObserver`
- 1 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"FBScene" _sceneToWaitForDeath;
```

## Properties

```
@property (T@"FBScene",R,N,V_sceneToWaitForDeath) scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBWaitForSceneDestructionTransaction _canBeInterrupted];
-[FBWaitForSceneDestructionTransaction _didComplete];
-[FBWaitForSceneDestructionTransaction _begin];
-[FBWaitForSceneDestructionTransaction _customizedDescriptionProperties];
-[FBWaitForSceneDestructionTransaction dealloc];
-[FBWaitForSceneDestructionTransaction initWithScene:];
-[FBWaitForSceneDestructionTransaction sceneDidInvalidate:];
-[FBWaitForSceneDestructionTransaction scene];
```
