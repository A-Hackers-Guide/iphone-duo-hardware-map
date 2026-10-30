# `_UISceneHostingSheetPresentationHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UISceneHostingSheetPresentationHostProviding`
- 2 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
I _sheetDisconnectionAssertionCount;
@"UIViewController" _targetViewController;
```

## Properties

```
@property (T@"UIViewController",W,N,S_setTargetViewController:,V_targetViewController) _targetViewController;
@property (T@"<_UIRemoteSheet_Internal>",?,R,N) _containedRemoteSheet;
@property (TB,?,R,N) _remoteSheetAllowsConnection;
@property (T@"_UISheetPresentationControllerConfiguration",&,N,S_setSheetConfiguration:) _sheetConfiguration;
@property (TB,N,S_setViewClipsToBounds:) _viewClipsToBounds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneHostingSheetPresentationHostComponent _setViewClipsToBounds:];
-[_UISceneHostingSheetPresentationHostComponent _setSheetConfiguration:];
-[_UISceneHostingSheetPresentationHostComponent _sheetConfiguration];
-[_UISceneHostingSheetPresentationHostComponent _targetViewController];
-[_UISceneHostingSheetPresentationHostComponent _remoteSheetAllowsConnection];
-[_UISceneHostingSheetPresentationHostComponent scene:handleActions:];
-[_UISceneHostingSheetPresentationHostComponent _sheetInteractionDraggingDidEnd];
-[_UISceneHostingSheetPresentationHostComponent _sheetInteractionDraggingDidBeginWithRubberBandCoefficient:];
-[_UISceneHostingSheetPresentationHostComponent _viewClipsToBounds];
-[_UISceneHostingSheetPresentationHostComponent currentPresentationController];
-[_UISceneHostingSheetPresentationHostComponent _setTargetViewController:];
-[_UISceneHostingSheetPresentationHostComponent sheetDisconnectionAssertionForReason:];
-[_UISceneHostingSheetPresentationHostComponent _sheetInteractionDraggingDidChangeWithTranslation:velocity:animateChange:];
-[_UISceneHostingSheetPresentationHostComponent evaluateSheetConnectionStateForNewAssertion:];
-[_UISceneHostingSheetPresentationHostComponent scene:didUpdateClientSettings:];
```
