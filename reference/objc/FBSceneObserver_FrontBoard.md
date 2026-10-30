# `FBSceneObserver`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `FBSceneComponent_Internal`, `FBSceneObserver_Internal`, `FBSceneDelegate`, `FBSceneComponent`, `BSInvalidatable`
- 9 instance variables, 4 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"<FBSceneObserver>" _observer;
Q _observerAddress;
# _observerClass;
B _isDelegate;
{?="contentStateDidChange"B"didUpdateSettings"B"updatePreparedLEGACY"B"updateAppliedLEGACY"B"updateCompletedLEGACY"B"didUpdateClientSettings"B"clientSettingsUpdatedLEGACY"B"willActivate"B"didActivate"B"willDeactivateWithError"B"willDeactivateWithContext"B"didInvalidate"B"didInvalidateWithContext"B"clientDidConnect"B"handleActions"B"wantsInactiveUpdates"B} _observerFlags;
{?="willUpdateSettingsLEGACY"B"willUpdateSettings"B"didReceiveActions"B"didDeactivateWithError"B"didDeactivateWithContext"B} _delegateFlags;
{?="willUpdateSettingsLEGACY"B"willUpdateSettings"B"handlePrivateActions"B"willInvalidate"B"invalidate"B} _componentFlags;
@"<FBSceneComponent>" _component;
# _extension;
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
-[FBSceneObserver sceneWillDeactivate:withError:];
-[FBSceneObserver sceneDidDeactivate:withContext:];
-[FBSceneObserver sceneDidDeactivate:withError:];
-[FBSceneObserver sceneWillActivate:];
-[FBSceneObserver scene:willUpdateSettings:withTransitionContext:];
-[FBSceneObserver scene:clientDidConnect:];
-[FBSceneObserver scene:didReceiveActions:];
-[FBSceneObserver sceneWillDeactivate:withContext:];
-[FBSceneObserver sceneObserverWantsUpdatesFromInactiveScenes];
-[FBSceneObserver sceneDidInvalidate:withContext:];
-[FBSceneObserver scene:handlePrivateActions:];
-[FBSceneObserver scene:didPrepareUpdateWithContext:];
-[FBSceneObserver _initWithObserver:];
-[FBSceneObserver configureInitialSettings:];
-[FBSceneObserver scene:didApplyUpdateWithContext:];
-[FBSceneObserver succinctDescriptionBuilder];
-[FBSceneObserver scene:didUpdateSettings:];
-[FBSceneObserver scene:handleActions:];
-[FBSceneObserver sceneDidActivate:];
-[FBSceneObserver sceneContentStateDidChange:];
-[FBSceneObserver descriptionWithMultilinePrefix:];
-[FBSceneObserver initWithScene:];
-[FBSceneObserver sceneDidInvalidate:];
-[FBSceneObserver scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:];
-[FBSceneObserver scene:willUpdateSettings:];
-[FBSceneObserver succinctDescription];
-[FBSceneObserver invalidate];
-[FBSceneObserver componentWillInvalidate:];
-[FBSceneObserver hash];
-[FBSceneObserver description];
-[FBSceneObserver isEqual:];
-[FBSceneObserver scene:didCompleteUpdateWithContext:error:];
-[FBSceneObserver scene:didUpdateClientSettings:];
-[FBSceneObserver descriptionBuilderWithMultilinePrefix:];
```
