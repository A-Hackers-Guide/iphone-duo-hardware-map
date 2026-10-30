# `SBWindowSelfHostWrapper`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"UIWindow" _window;
@"<UIScenePresenter>" _presenter;
@"UIView<UIScenePresentation>" _hostView;
```

## Properties

```
@property (T@"NSString",R,C,N) requester;
@property (T@"UIWindow",R,N,V_window) window;
@property (T@"UIView<UIScenePresentation>",R,N,V_hostView) hostView;
@property (T@"<UIScenePresenter>",R,N,V_presenter) presenter;
@property (T@"UIScenePresentationContext",R,C,N) presentationContext;
```

## Class methods

```
+[SBWindowSelfHostWrapper wrapperForUseInWindow:hostRequester:sceneIdentifier:];
+[SBWindowSelfHostWrapper wrapperForWindow:orientation:hostRequester:sceneIdentifier:];
```

## Instance methods

```
-[SBWindowSelfHostWrapper hostView];
-[SBWindowSelfHostWrapper presenter];
-[SBWindowSelfHostWrapper presentationContext];
-[SBWindowSelfHostWrapper window];
-[SBWindowSelfHostWrapper requester];
-[SBWindowSelfHostWrapper modifyPresentationContext:];
-[SBWindowSelfHostWrapper stopHosting];
```
