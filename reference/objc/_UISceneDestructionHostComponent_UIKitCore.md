# `_UISceneDestructionHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneComponent`, `FBSceneObserver`
- 1 instance variables, 6 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
```

## Properties

```
@property (T@"NSSet",R,C,N) destructionConditions;
@property (T@"UISceneClosureConfirmation",R,C,N) closureConfirmation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneDestructionHostComponent removeObserver:];
-[_UISceneDestructionHostComponent closureConfirmation];
-[_UISceneDestructionHostComponent addObserver:];
-[_UISceneDestructionHostComponent destructionConditions];
-[_UISceneDestructionHostComponent scene:didUpdateClientSettings:];
```
