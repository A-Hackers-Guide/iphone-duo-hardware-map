# `_UIViewControllerSceneCompanionBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `_UIViewControllerBehavior`
- 4 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UISceneAccessoryRegistration" _registration;
@"UIViewController" _viewController;
@"<UITraitChangeRegistration>" _collectorChangeRegistration;
@"<_UIInvalidatable>" _collectorContribution;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIViewController",R,W,N,V_viewController) viewController;
```

## Instance methods

```
-[_UIViewControllerSceneCompanionBehavior debugDescription];
-[_UIViewControllerSceneCompanionBehavior viewIsAppearing:];
-[_UIViewControllerSceneCompanionBehavior viewWillDisappear:];
-[_UIViewControllerSceneCompanionBehavior viewController];
-[_UIViewControllerSceneCompanionBehavior succinctDescription];
-[_UIViewControllerSceneCompanionBehavior viewWillAppear:];
-[_UIViewControllerSceneCompanionBehavior viewDidAppear:];
-[_UIViewControllerSceneCompanionBehavior description];
-[_UIViewControllerSceneCompanionBehavior viewDidDisappear:];
-[_UIViewControllerSceneCompanionBehavior appendDescriptionToStream:];
-[_UIViewControllerSceneCompanionBehavior _viewControllerSceneHandleCollectorDidChange];
-[_UIViewControllerSceneCompanionBehavior didMoveToViewController:];
-[_UIViewControllerSceneCompanionBehavior willMoveToViewController:];
```
