# `LACUISceneRootViewController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `LACUISceneContentPresenter`, `LACUISceneButtonHandler`
- 2 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _isDismissing;
@"<LACUIScene>" _scene;
```

## Properties

```
@property (T@"<LACUIScene>",R,N,V_scene) scene;
@property (TB,R,N) didRequestDeactivation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACUISceneRootViewController dismiss];
-[LACUISceneRootViewController dealloc];
-[LACUISceneRootViewController _preferredStatusBarVisibility];
-[LACUISceneRootViewController initWithScene:];
-[LACUISceneRootViewController _canShowWhileLocked];
-[LACUISceneRootViewController scene];
-[LACUISceneRootViewController preferredStatusBarStyle];
-[LACUISceneRootViewController didRequestDeactivation];
-[LACUISceneRootViewController handleSceneButton:];
-[LACUISceneRootViewController present:animated:];
-[LACUISceneRootViewController present:animated:completion:];
```
