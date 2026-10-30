# `SBPIPControllerAdapter` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance methods

```
-[SBPIPControllerAdapter setPIPController:];
-[SBPIPControllerAdapter contentTypeForPIPController:];
-[SBPIPControllerAdapter isStartingStoppingOrCancellingPictureInPictureForPIPController:];
-[SBPIPControllerAdapter restorePictureInPictureForPIPController:applicationBundleIdentifier:forDisplayContentModeSwap:];
-[SBPIPControllerAdapter isStoppingOrCancellingPictureForPIPController:applicationWithBundleIdentifier:scenePersistenceIdentifier:];
-[SBPIPControllerAdapter shouldStartPictureInPictureForPIPController:applicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:];
-[SBPIPControllerAdapter isPresentingPictureInPictureForPIPController:applicationBundleIdentifier:];
-[SBPIPControllerAdapter tetheringModeForScenePersistenceIdentifier:];
-[SBPIPControllerAdapter pipController:morphAnimatorDataSourceForMorphAnimatorController:];
-[SBPIPControllerAdapter preventStashAssertionsForPIPController:];
-[SBPIPControllerAdapter pipController:willBeginPIPInterruptionForAssertion:];
-[SBPIPControllerAdapter pipController:didStartPictureInPictureForApplicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:animated:completionHandler:];
-[SBPIPControllerAdapter pipController:willRestorePictureInPictureForTestForApplicationWithBundleIdentifier:];
-[SBPIPControllerAdapter pipController:didCancelPictureInPictureForApplicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:];
-[SBPIPControllerAdapter pipController:willEndPIPInterruptionForAssertion:];
-[SBPIPControllerAdapter pipController:willStartPictureInPictureTestActionForApplicationWithBundleIdentifier:];
-[SBPIPControllerAdapter pipController:didAddContainerViewController:];
-[SBPIPControllerAdapter pipController:didUpdateEnhancedWindowingModeEnabled:windowScene:];
-[SBPIPControllerAdapter pipController:willRemoveContainerViewController:];
-[SBPIPControllerAdapter windowLevelDidChangeForPIPController:];
-[SBPIPControllerAdapter windowVisibilityDidChangeForPIPController:];
```
