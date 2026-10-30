# `FBSceneObserver` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance methods

```
-[FBSceneObserver sceneWillDeactivate:withError:];
-[FBSceneObserver sceneWillActivate:];
-[FBSceneObserver scene:clientDidConnect:];
-[FBSceneObserver sceneWillDeactivate:withContext:];
-[FBSceneObserver sceneDidInvalidate:withContext:];
-[FBSceneObserver scene:didPrepareUpdateWithContext:];
-[FBSceneObserver scene:didApplyUpdateWithContext:];
-[FBSceneObserver scene:didUpdateSettings:];
-[FBSceneObserver scene:handleActions:];
-[FBSceneObserver sceneDidActivate:];
-[FBSceneObserver sceneContentStateDidChange:];
-[FBSceneObserver sceneDidInvalidate:];
-[FBSceneObserver scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:];
-[FBSceneObserver scene:didCompleteUpdateWithContext:error:];
-[FBSceneObserver scene:didUpdateClientSettings:];
```
