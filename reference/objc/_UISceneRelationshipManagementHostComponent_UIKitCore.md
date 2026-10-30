# `_UISceneRelationshipManagementHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UIScenePresentationViewObserver`, `_UIScenePresentationManagerPrioritizedPresenterObserver`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"_UIScenePresenter" _prioritizedPresenter;
@"NSHashTable" _observers;
@"<_UIRemoteContentParent>" _parent;
@"_UIChildRemoteContentRegistry" _associatedRemoteContentRegistry;
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
-[_UISceneRelationshipManagementHostComponent sceneDidInvalidate:withContext:];
-[_UISceneRelationshipManagementHostComponent presentationView:didMoveToWindow:];
-[_UISceneRelationshipManagementHostComponent windowDidMoveToScene:];
-[_UISceneRelationshipManagementHostComponent removeObserver:];
-[_UISceneRelationshipManagementHostComponent setScene:];
-[_UISceneRelationshipManagementHostComponent _willMoveToWindowWithDelayedPresentation:];
-[_UISceneRelationshipManagementHostComponent windowWillMoveToNilScene:];
-[_UISceneRelationshipManagementHostComponent addObserver:];
-[_UISceneRelationshipManagementHostComponent invalidate];
-[_UISceneRelationshipManagementHostComponent _scenePresenterIsMovingToWindow:];
-[_UISceneRelationshipManagementHostComponent _presentationManager:willPrioritizePresenter:];
-[_UISceneRelationshipManagementHostComponent notifyObserversOfParentChange:];
-[_UISceneRelationshipManagementHostComponent windowContainsPrioritizedPresenter:];
```
