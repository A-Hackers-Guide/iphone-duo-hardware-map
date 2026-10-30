# `_UICompanionSceneInterestHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `_UICompanionSceneInterestHost`, `FBSceneObserver`
- 1 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",R,C,N) interestedAttributes;
```

## Instance methods

```
-[_UICompanionSceneInterestHostComponent debugDescription];
-[_UICompanionSceneInterestHostComponent removeObserver:];
-[_UICompanionSceneInterestHostComponent succinctDescription];
-[_UICompanionSceneInterestHostComponent addObserver:];
-[_UICompanionSceneInterestHostComponent interestedAttributes];
-[_UICompanionSceneInterestHostComponent description];
-[_UICompanionSceneInterestHostComponent appendDescriptionToStream:];
-[_UICompanionSceneInterestHostComponent scene:didUpdateClientSettings:];
```
