# `SBAccessibilityUIServerUISceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemUISceneController`
- 2 instance variables, 0 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"SBSUIFeaturePolicyHostComponent" _reachabilityDisablingFeaturePolicyComponent;
@"NSMutableDictionary" _presentersByPresentationStyle;
```

## Class methods

```
+[SBAccessibilityUIServerUISceneController _setupInfo];
+[SBAccessibilityUIServerUISceneController _setupInfoForSceneSpecification:];
```

## Instance methods

```
-[SBAccessibilityUIServerUISceneController _evaluateAvailablePresenters:forSceneControllers:];
-[SBAccessibilityUIServerUISceneController scenePresenter:willDismissScene:];
-[SBAccessibilityUIServerUISceneController scenePresenter:didPresentScene:];
-[SBAccessibilityUIServerUISceneController _requiresKeyboard];
-[SBAccessibilityUIServerUISceneController _isDefaultPresenterDelegate];
-[SBAccessibilityUIServerUISceneController _newSceneControllerForWindowScene:sceneRequestOptions:traitsRole:level:];
```
