# `SBWaitForSceneContentAvailableTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransaction`
- Protocols: `SBSceneHandleObserver`
- 4 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"SBSceneHandle" _sceneHandle;
B _isContentStateReady;
B _manualListener;
B _allowsInterruption;
```

## Properties

```
@property (T@"SBSceneHandle",C,N,V_sceneHandle) sceneHandle;
@property (TB,N,V_allowsInterruption) allowsInterruption;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWaitForSceneContentAvailableTransaction sceneHandle:didDestroyScene:];
-[SBWaitForSceneContentAvailableTransaction sceneHandle:didUpdateContentState:];
-[SBWaitForSceneContentAvailableTransaction _canBeInterrupted];
-[SBWaitForSceneContentAvailableTransaction _didComplete];
-[SBWaitForSceneContentAvailableTransaction _begin];
-[SBWaitForSceneContentAvailableTransaction sceneHandle];
-[SBWaitForSceneContentAvailableTransaction dealloc];
-[SBWaitForSceneContentAvailableTransaction setSceneHandle:];
-[SBWaitForSceneContentAvailableTransaction _noteSceneContentReadinessDidChange:];
-[SBWaitForSceneContentAvailableTransaction allowsInterruption];
-[SBWaitForSceneContentAvailableTransaction initWithSceneHandle:manualListener:];
-[SBWaitForSceneContentAvailableTransaction noteSceneContentIsReady:];
-[SBWaitForSceneContentAvailableTransaction setAllowsInterruption:];
```
