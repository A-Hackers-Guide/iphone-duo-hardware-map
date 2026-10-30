# `UIRootWindowScenePresentationBinder`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIScenePresentationBinder`
- 4 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"FBSDisplayConfiguration" _displayConfiguration;
@"UIRootSceneWindow" _rootSceneWindow;
B _shouldManageWindowLifecycle;
@"NSMutableSet" _presentedScenes;
```

## Properties

```
@property (T@"UIMutableTransformer",R,N) sceneTransformer;
```

## Instance methods

```
-[UIRootWindowScenePresentationBinder initWithPriority:displayConfiguration:];
-[UIRootWindowScenePresentationBinder _initWithIdentifier:priority:appearanceStyle:rootWindow:];
-[UIRootWindowScenePresentationBinder sceneTransformer];
-[UIRootWindowScenePresentationBinder _rootView];
-[UIRootWindowScenePresentationBinder invalidate];
-[UIRootWindowScenePresentationBinder initWithIdentifier:priority:appearanceStyle:rootWindow:];
-[UIRootWindowScenePresentationBinder _noteDidStopPresentingScene:];
-[UIRootWindowScenePresentationBinder _noteWillStartPresentingScene:];
-[UIRootWindowScenePresentationBinder descriptionBuilderWithMultilinePrefix:];
```
