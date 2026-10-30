# `SBAssistantSceneControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `BSInvalidatable`
- 0 instance variables, 11 properties, 18 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisSystemAssistantExperienceAvailable) systemAssistantExperienceAvailable;
@property (TB,R,N,GisSystemAssistantExperienceEnabled) systemAssistantExperienceEnabled;
@property (TB,R,N,GisSystemAssistantExperiencePersistentSiriEnabled) systemAssistantExperiencePersistentSiriEnabled;
@property (TB,R,N,GisLinwoodDismissalEnabled) linwoodDismissalEnabled;
@property (TB,R,N,GisHomeAffordanceDoubleTapGestureEnabled) homeAffordanceDoubleTapGestureEnabled;
@property (TB,R,N,GisVisualSearchEnabled) visualSearchEnabled;
@property (TB,R,N,GisVisible) visible;
@property (TB,R,N,GisOccludingSystemContent) occludingSystemContent;
@property (T@"SBAssistantSessionPresentationContext",R,N) presentationContext;
@property (T@"SBWindow",R,N) window;
@property (T@"SBAssistantRootViewController",R,N) assistantRootViewController;
```

## Instance methods

```
-[SBAssistantSceneControlling assistantRootViewController];
-[SBAssistantSceneControlling isLinwoodDismissalEnabled];
-[SBAssistantSceneControlling removeObserver:];
-[SBAssistantSceneControlling isSystemAssistantExperiencePersistentSiriEnabled];
-[SBAssistantSceneControlling presentationContext];
-[SBAssistantSceneControlling isSystemAssistantExperienceEnabled];
-[SBAssistantSceneControlling isVisible];
-[SBAssistantSceneControlling window];
-[SBAssistantSceneControlling dismissAssistantViewIfNecessaryWithAnimation:completion:];
-[SBAssistantSceneControlling addObserver:];
-[SBAssistantSceneControlling dismissAssistantViewIfNecessary];
-[SBAssistantSceneControlling dismissAssistantViewIfNecessaryForGestureTranslation:velocity:];
-[SBAssistantSceneControlling isHomeAffordanceDoubleTapGestureEnabled];
-[SBAssistantSceneControlling isSystemAssistantExperienceAvailable];
-[SBAssistantSceneControlling commandeerCaptureDropletPreludeForVisionInvocation:];
-[SBAssistantSceneControlling dismissAssistantViewIfNecessaryWithAnimation:];
-[SBAssistantSceneControlling isVisualSearchEnabled];
-[SBAssistantSceneControlling isOccludingSystemContent];
```
