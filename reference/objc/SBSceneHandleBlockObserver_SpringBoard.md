# `SBSceneHandleBlockObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `SBSceneHandleObserver`
- 6 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _createBlocks;
@"NSMutableDictionary" _destroyBlocks;
@"NSMutableDictionary" _didUpdateContentStateBlocks;
@"NSMutableDictionary" _didUpdateSettingsBlocks;
@"NSMutableDictionary" _didUpdateClientSettingsBlocks;
B _invalidated;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSceneHandleBlockObserver sceneHandle:didDestroyScene:];
-[SBSceneHandleBlockObserver sceneHandle:didCreateScene:];
-[SBSceneHandleBlockObserver sceneHandle:didUpdateClientSettings:];
-[SBSceneHandleBlockObserver sceneHandle:didUpdateContentState:];
-[SBSceneHandleBlockObserver removeObserverForToken:];
-[SBSceneHandleBlockObserver observeDidUpdateClientSettings:];
-[SBSceneHandleBlockObserver sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBSceneHandleBlockObserver observeDidUpdateContentState:];
-[SBSceneHandleBlockObserver dealloc];
-[SBSceneHandleBlockObserver invalidate];
-[SBSceneHandleBlockObserver observeCreate:];
-[SBSceneHandleBlockObserver observeDestroy:];
-[SBSceneHandleBlockObserver observeDidUpdateSettings:];
```
