# `UISceneActivationRequestOptions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`, `NSCopying`
- 4 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _preserveLayout;
B __requestFullscreen;
@"UIScene" _requestingScene;
q _collectionJoinBehavior;
```

## Properties

```
@property (TB,N,V_preserveLayout) preserveLayout;
@property (Tq,N) _collectionJoinBehavior;
@property (TB,N,S_setRequestFullscreen:,V__requestFullscreen) _requestFullscreen;
@property (T@"UIScene",&,N,V_requestingScene) requestingScene;
@property (Tq,N,V_collectionJoinBehavior) collectionJoinBehavior;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISceneActivationRequestOptions debugDescription];
-[UISceneActivationRequestOptions succinctDescriptionBuilder];
-[UISceneActivationRequestOptions preserveLayout];
-[UISceneActivationRequestOptions descriptionWithMultilinePrefix:];
-[UISceneActivationRequestOptions succinctDescription];
-[UISceneActivationRequestOptions debugDescriptionWithMultilinePrefix:];
-[UISceneActivationRequestOptions description];
-[UISceneActivationRequestOptions setPreserveLayout:];
-[UISceneActivationRequestOptions copyWithZone:];
-[UISceneActivationRequestOptions descriptionBuilderWithMultilinePrefix:];
-[UISceneActivationRequestOptions requestingScene];
-[UISceneActivationRequestOptions _collectionJoinBehavior];
-[UISceneActivationRequestOptions _requestFullscreen];
-[UISceneActivationRequestOptions _setRequestFullscreen:];
-[UISceneActivationRequestOptions collectionJoinBehavior];
-[UISceneActivationRequestOptions setCollectionJoinBehavior:];
-[UISceneActivationRequestOptions setRequestingScene:];
-[UISceneActivationRequestOptions set_collectionJoinBehavior:];
```
