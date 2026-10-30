# `SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIAnimationControllerTransitionContextProvider`
- 4 instance variables, 10 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"SBApplicationSceneEntity" _toAppSceneEntity;
@"SBApplicationSceneEntity" _fromAppSceneEntity;
@"SBApplicationSceneEntity" _toApplicationSceneEntity;
@"SBApplicationSceneEntity" _fromApplicationSceneEntity;
```

## Properties

```
@property (T@"SBApplicationSceneEntity",&,N,V_toAppSceneEntity) activatingAppSceneEntity;
@property (T@"SBApplicationSceneEntity",&,N,V_fromAppSceneEntity) deactivatingAppSceneEntity;
@property (T@"NSSet",R,C,N) toApplicationSceneEntities;
@property (T@"SBApplicationSceneEntity",R,N,V_toApplicationSceneEntity) toApplicationSceneEntity;
@property (T@"NSSet",R,C,N) fromApplicationSceneEntities;
@property (T@"SBApplicationSceneEntity",R,N,V_fromApplicationSceneEntity) fromApplicationSceneEntity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider transitionContextProviderWithToApplicationSceneEntity:fromApplicationSceneEntity:];
```

## Instance methods

```
-[SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider fromApplicationSceneEntities];
-[SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider toApplicationSceneEntities];
-[SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider activatingAppSceneEntity];
-[SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider deactivatingAppSceneEntity];
-[SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider fromApplicationSceneEntity];
-[SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider initWithToApplicationSceneEntity:fromApplicationSceneEntity:];
-[SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider setActivatingAppSceneEntity:];
-[SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider setDeactivatingAppSceneEntity:];
-[SBUIAnimationControllerActivatingAndDeactivatingAppTransitionContextProvider toApplicationSceneEntity];
```
