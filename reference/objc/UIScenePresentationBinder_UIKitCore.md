# `UIScenePresentationBinder`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneLayerManagerObserver`, `FBSceneObserver`, `BSDescriptionProviding`, `BSInvalidatable`
- 9 instance variables, 6 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"UIView" _rootView;
@"NSMutableSet" _scenes;
q _priority;
Q _appearanceStyle;
@"<UIScenePresentationBinderDelegate>" _delegate;
B _invalidated;
@"NSMutableDictionary" _mapSceneIDToPresenter;
{?="delegateShouldPresentWithNoSceneLayers"b1"delegateDidStartPresentingScene"b1"delegateDidStopPresentingScene"b1} _delegateFlags;
```

## Properties

```
@property (T@"<UIScenePresentationBinderDelegate>",W,N,V_delegate) delegate;
@property (T@"NSSet",R,N,V_scenes) scenes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIScenePresentationBinder sceneDidInvalidate:withContext:];
-[UIScenePresentationBinder _delegateShouldPresentSceneOnlyWhenLayersExist];
-[UIScenePresentationBinder succinctDescriptionBuilder];
-[UIScenePresentationBinder scene:didUpdateSettings:];
-[UIScenePresentationBinder dealloc];
-[UIScenePresentationBinder descriptionWithMultilinePrefix:];
-[UIScenePresentationBinder _noteSceneMovedToBackground:];
-[UIScenePresentationBinder _rootView];
-[UIScenePresentationBinder succinctDescription];
-[UIScenePresentationBinder invalidate];
-[UIScenePresentationBinder setDelegate:];
-[UIScenePresentationBinder initWithIdentifier:priority:rootView:appearanceStyle:];
-[UIScenePresentationBinder addScene:];
-[UIScenePresentationBinder _activatePresenter:scene:reason:];
-[UIScenePresentationBinder _removeScene:forReason:];
-[UIScenePresentationBinder _noteSceneMovedToForeground:];
-[UIScenePresentationBinder sceneLayerManagerDidStartTrackingLayers:];
-[UIScenePresentationBinder delegate];
-[UIScenePresentationBinder _delegateDidStartPresentingScene:];
-[UIScenePresentationBinder setTransform:forScene:];
-[UIScenePresentationBinder _deactivatePresenter:scene:reason:];
-[UIScenePresentationBinder description];
-[UIScenePresentationBinder _evaluateSceneForHosting:forReason:];
-[UIScenePresentationBinder removeScene:];
-[UIScenePresentationBinder sceneLayerManagerDidStopTrackingLayers:];
-[UIScenePresentationBinder _delegateDidStopPresentingScene:];
-[UIScenePresentationBinder _noteDidStopPresentingScene:];
-[UIScenePresentationBinder _noteSceneChangedLevel:];
-[UIScenePresentationBinder _positionPresentationViewInRootViewOrderedCorrectly:];
-[UIScenePresentationBinder _noteWillStartPresentingScene:];
-[UIScenePresentationBinder scenes];
-[UIScenePresentationBinder descriptionBuilderWithMultilinePrefix:];
```
