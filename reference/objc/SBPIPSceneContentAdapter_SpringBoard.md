# `SBPIPSceneContentAdapter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLayoutStateTransitionObserver`, `SBPIPControllerAdapter`
- 7 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBPIPController<SBPIPControllerAdapterContextProviding>" _pipController;
q _pipContentType;
@"NSMutableSet" _trackedPIPBundleIdentifiers;
q _effectiveEnvironmentMode;
@"SBFloatingDockWindowLevelAssertion" _dockWindowLevelAssertion;
@"NSMutableSet" _interruptingBundleIdentifiersSinceLastTransition;
@"SBWindowScene" _sbWindowScene;
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
-[SBPIPSceneContentAdapter setPIPController:];
-[SBPIPSceneContentAdapter contentTypeForPIPController:];
-[SBPIPSceneContentAdapter pipController:willBeginPIPInterruptionForAssertion:];
-[SBPIPSceneContentAdapter isStartingStoppingOrCancellingPictureInPictureForPIPController:];
-[SBPIPSceneContentAdapter layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBPIPSceneContentAdapter restorePictureInPictureForPIPController:applicationBundleIdentifier:forDisplayContentModeSwap:];
-[SBPIPSceneContentAdapter isStoppingOrCancellingPictureForPIPController:applicationWithBundleIdentifier:scenePersistenceIdentifier:];
-[SBPIPSceneContentAdapter shouldStartPictureInPictureForPIPController:applicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:];
-[SBPIPSceneContentAdapter isPresentingPictureInPictureForPIPController:applicationBundleIdentifier:];
-[SBPIPSceneContentAdapter tetheringModeForScenePersistenceIdentifier:];
-[SBPIPSceneContentAdapter _recalculateLevelAssertions];
-[SBPIPSceneContentAdapter initWithPIPContentType:windowScene:];
-[SBPIPSceneContentAdapter pipController:didAddContainerViewController:];
-[SBPIPSceneContentAdapter pipController:didUpdateEnhancedWindowingModeEnabled:windowScene:];
-[SBPIPSceneContentAdapter pipController:willRemoveContainerViewController:];
-[SBPIPSceneContentAdapter windowLevelDidChangeForPIPController:];
-[SBPIPSceneContentAdapter windowVisibilityDidChangeForPIPController:];
```
