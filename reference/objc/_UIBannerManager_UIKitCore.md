# `_UIBannerManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 3 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIWindowScene" _windowScene;
@"_UIBannerWindow" _window;
@"_UIBannerContainerView" _containerView;
```

## Properties

```
@property (T@"UIWindowScene",&,N,V_windowScene) windowScene;
@property (T@"_UIBannerWindow",&,N,V_window) window;
@property (T@"_UIBannerContainerView",&,N,V_containerView) containerView;
@property (T@"UIScene",W,N,G_scene,S_setScene:) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIBannerManager setContainerView:];
-[_UIBannerManager setWindowScene:];
-[_UIBannerManager _scene];
-[_UIBannerManager window];
-[_UIBannerManager initWithScene:];
-[_UIBannerManager containerView];
-[_UIBannerManager _createWindowIfNeeded];
-[_UIBannerManager bannerWithContent:];
-[_UIBannerManager _setScene:];
-[_UIBannerManager windowScene];
-[_UIBannerManager setWindow:];
```
