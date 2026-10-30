# `SBDisplayCloneTransitionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `SBFDisplayContentModeTransitionParticipant`
- 10 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBWindowSceneManager" _windowSceneManager;
@"<SBDisplayFramebufferCloneProviding>" _cloneProvider;
@"<SBDisplayCloneTransitionOutputHosting>" _outputHosting;
@"NSMutableArray" _activeClones;
@"NSMutableArray" _activeOutputViews;
@"NSMutableArray" _activeHostingHandles;
@"NSMutableArray" _activeFadeViews;
@"NSMutableArray" _activeCoverViews;
@"NSMutableArray" _activeCoverHostingHandles;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",?,R,N) displayContentModeTransitionSignpostName;
```

## Class methods

```
+[SBDisplayCloneTransitionCoordinator fadeAlphaForProgressToSwap:progressFromSwap:];
```

## Instance methods

```
-[SBDisplayCloneTransitionCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBDisplayCloneTransitionCoordinator dealloc];
-[SBDisplayCloneTransitionCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBDisplayCloneTransitionCoordinator displayContentModeTransitionSignpostName];
-[SBDisplayCloneTransitionCoordinator _acquireMechanismForAction:sourceScene:targetScene:];
-[SBDisplayCloneTransitionCoordinator _acquireMechanismsWithContext:];
-[SBDisplayCloneTransitionCoordinator _cleanupOpacityModifications:];
-[SBDisplayCloneTransitionCoordinator _driveMechanismsWithContext:];
-[SBDisplayCloneTransitionCoordinator _hostIndividualOutputView:aboveSourceView:onWindowScene:];
-[SBDisplayCloneTransitionCoordinator _modifyView:opacity:];
-[SBDisplayCloneTransitionCoordinator _partnerSceneForScene:amongScenes:];
-[SBDisplayCloneTransitionCoordinator _prepareViewForOpacityModification:];
-[SBDisplayCloneTransitionCoordinator _releaseMechanismsWithContext:];
-[SBDisplayCloneTransitionCoordinator initWithDisplayContentModeCoordinator:windowSceneManager:cloneProvider:outputHosting:];
-[SBDisplayCloneTransitionCoordinator installSwapCoversWithContext:];
-[SBDisplayCloneTransitionCoordinator removeSwapCovers];
-[SBDisplayCloneTransitionCoordinator transitionActionsForResolver:];
```
