# `UIScenePresenter` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BSInvalidatable`
- 0 instance variables, 8 properties, 19 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) identifier;
@property (T@"UIScenePresentationManager",R,W,N) manager;
@property (T@"FBScene",R,W,N) scene;
@property (T@"UIScenePresentationContext",R,C,N) presentationContext;
@property (T@"UIView<UIScenePresentation>",R,N) presentationView;
@property (TB,R,N,GisActive) active;
@property (TB,R,N,GisInvalidated) invalidated;
@property (TB,R,N,GisHosting) hosting;
```

## Instance methods

```
-[UIScenePresenter deactivate];
-[UIScenePresenter captureSnapshotPresentationView];
-[UIScenePresenter identifier];
-[UIScenePresenter removeObserver:];
-[UIScenePresenter newSnapshotPresentationView];
-[UIScenePresenter presentationContext];
-[UIScenePresenter isHosting];
-[UIScenePresenter manager];
-[UIScenePresenter isInvalidated];
-[UIScenePresenter presentationView];
-[UIScenePresenter addObserver:];
-[UIScenePresenter invalidate];
-[UIScenePresenter scene];
-[UIScenePresenter newSnapshotContext];
-[UIScenePresenter activate];
-[UIScenePresenter prepareSnapshotPresentationViewWithConfigurator:];
-[UIScenePresenter newSnapshot];
-[UIScenePresenter modifyPresentationContext:];
-[UIScenePresenter isActive];
```
