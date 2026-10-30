# `_SBActiveRemoteTransientOverlayViewProviderRegistry`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSMapTable" _viewProviderAdapterForSceneIdentifier;
@"NSMutableDictionary" _sceneIdentifierToStashedViewProviderBySceneBackedPreference;
```

## Class methods

```
+[_SBActiveRemoteTransientOverlayViewProviderRegistry sharedInstance];
```

## Instance methods

```
-[_SBActiveRemoteTransientOverlayViewProviderRegistry init];
-[_SBActiveRemoteTransientOverlayViewProviderRegistry _extractStashedViewProviderMatchingViewProvider:];
-[_SBActiveRemoteTransientOverlayViewProviderRegistry registerViewProvider:];
-[_SBActiveRemoteTransientOverlayViewProviderRegistry removeStashedViewProviderIfNecessary:];
-[_SBActiveRemoteTransientOverlayViewProviderRegistry restoreStashedPresentationStateIntoViewProvider:];
-[_SBActiveRemoteTransientOverlayViewProviderRegistry stashPresentationStateForWindowSceneMoveForViewProvider:];
-[_SBActiveRemoteTransientOverlayViewProviderRegistry unregisterViewProvider:];
```
