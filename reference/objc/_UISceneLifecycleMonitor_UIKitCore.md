# `_UISceneLifecycleMonitor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"UIScene" __scene;
```

## Properties

```
@property (T@"UIScene",W,N,V__scene) _scene;
@property (Tq,R,N) currentActivationState;
```

## Instance methods

```
-[_UISceneLifecycleMonitor willConnect];
-[_UISceneLifecycleMonitor willEnterForeground];
-[_UISceneLifecycleMonitor didEnterBackground];
-[_UISceneLifecycleMonitor didConnect];
-[_UISceneLifecycleMonitor _scene];
-[_UISceneLifecycleMonitor didBecomeActive];
-[_UISceneLifecycleMonitor willBecomeActive];
-[_UISceneLifecycleMonitor willResignActive];
-[_UISceneLifecycleMonitor willEnterBackground];
-[_UISceneLifecycleMonitor didEnterForeground];
-[_UISceneLifecycleMonitor didResignActive];
-[_UISceneLifecycleMonitor initWithScene:];
-[_UISceneLifecycleMonitor currentActivationState];
-[_UISceneLifecycleMonitor set_scene:];
-[_UISceneLifecycleMonitor didDisonnect];
-[_UISceneLifecycleMonitor willDisonnect];
-[_UISceneLifecycleMonitor transitionToTargetState:fromState:withTransitionContext:preparations:];
```
