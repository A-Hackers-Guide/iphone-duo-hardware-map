# `_UIScenePresenter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `UIScenePresenter`
- 13 instance variables, 15 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"UIScenePresentationManager" _weakManager;
@"UIScenePresentationManager" _strongManager;
@"FBScene" _strongScene;
@"_UIScenePresenterOwner" _owner;
@"UIScenePresentationContext" _presentationContext;
d _initializeTime;
@"<NSCopying><_UIComparable>" _sortContext;
@"NSString" _identifier;
B _invalidated;
B _visibilityPropagationEnabled;
@"_UIScenePresentationView" _view;
@"NSHashTable" _observers;
B _hosting;
```

## Properties

```
@property (Td,N,V_initializeTime) _initializeTime;
@property (TB,N,GisVisibilityPropagationEnabled,V_visibilityPropagationEnabled) visibilityPropagationEnabled;
@property (T@"<NSCopying>",R,C,N,V_sortContext) sortContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) identifier;
@property (T@"UIScenePresentationManager",R,W,N) manager;
@property (T@"FBScene",R,W,N) scene;
@property (T@"UIScenePresentationContext",R,C,N,V_presentationContext) presentationContext;
@property (T@"UIView<UIScenePresentation>",R,N) presentationView;
@property (TB,R,N,GisActive) active;
@property (TB,R,N,GisInvalidated) invalidated;
@property (TB,R,N,GisHosting,V_hosting) hosting;
```

## Instance methods

```
-[_UIScenePresenter initWithManager:scene:owner:identifier:sortContext:];
-[_UIScenePresenter deactivate];
-[_UIScenePresenter captureSnapshotPresentationView];
-[_UIScenePresenter identifier];
-[_UIScenePresenter succinctDescriptionBuilder];
-[_UIScenePresenter removeObserver:];
-[_UIScenePresenter compare:];
-[_UIScenePresenter newSnapshotPresentationView];
-[_UIScenePresenter init];
-[_UIScenePresenter presentationContext];
-[_UIScenePresenter notifyObserversHostingDidChange:];
-[_UIScenePresenter dealloc];
-[_UIScenePresenter isHosting];
-[_UIScenePresenter set_initializeTime:];
-[_UIScenePresenter manager];
-[_UIScenePresenter descriptionWithMultilinePrefix:];
-[_UIScenePresenter isInvalidated];
-[_UIScenePresenter presentationView];
-[_UIScenePresenter succinctDescription];
-[_UIScenePresenter addObserver:];
-[_UIScenePresenter invalidate];
-[_UIScenePresenter scene];
-[_UIScenePresenter newSnapshotContext];
-[_UIScenePresenter activate];
-[_UIScenePresenter prepareSnapshotPresentationViewWithConfigurator:];
-[_UIScenePresenter _initializeTime];
-[_UIScenePresenter description];
-[_UIScenePresenter _isHosting];
-[_UIScenePresenter newSnapshot];
-[_UIScenePresenter notifyObserversDidUpdateContext:];
-[_UIScenePresenter sortContext];
-[_UIScenePresenter modifyPresentationContext:];
-[_UIScenePresenter isActive];
-[_UIScenePresenter notifyObserversHostingWillChange:];
-[_UIScenePresenter isVisibilityPropagationEnabled];
-[_UIScenePresenter updateHostingStateIfNecessary];
-[_UIScenePresenter setVisibilityPropagationEnabled:];
-[_UIScenePresenter descriptionBuilderWithMultilinePrefix:];
```
