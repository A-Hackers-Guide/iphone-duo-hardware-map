# `SBSystemActionPreviewCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemActionPreviewCoordinating`
- 8 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _previewProviders;
@"NSHashTable" _observers;
@"NSHashTable" _activeSceneElementProviders;
@"NSMapTable" _activeSimplePreviewElementsToAssertions;
@"NSMapTable" _activeSimplePreviewPresentableViewControllersToAssertions;
@"SBSystemActionPreviewBannerAuthority" _systemActionPreviewBannerAuthority;
@"SBActivityManager" _activityManager;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemActionPreviewCoordinator windowScene];
-[SBSystemActionPreviewCoordinator customSoundForPerformingAction:];
-[SBSystemActionPreviewCoordinator previewContextForAction:];
-[SBSystemActionPreviewCoordinator provideDiscreteNoActionInteractionFeedback];
-[SBSystemActionPreviewCoordinator showPreviewForAction:withContext:];
```
