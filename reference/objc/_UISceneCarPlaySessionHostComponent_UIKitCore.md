# `_UISceneCarPlaySessionHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneObserver`, `_UISceneCarPlaySessionHost`
- 1 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<_UISceneCarPlaySessionTouchpadFeedbackDelegate>" touchpadFeedbackDelegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N) availableInteractionModels;
@property (TQ,N) primaryInteractionModel;
@property (Tq,N) touchLevel;
@property (T@"NSArray",&,N) touchpads;
@property (T@"<_UISceneCarPlaySessionTouchpadFeedbackDelegate>",W,N,VtouchpadFeedbackDelegate) touchpadFeedbackDelegate;
```

## Instance methods

```
-[_UISceneCarPlaySessionHostComponent handlePrivateActions:];
-[_UISceneCarPlaySessionHostComponent availableInteractionModels];
-[_UISceneCarPlaySessionHostComponent primaryInteractionModel];
-[_UISceneCarPlaySessionHostComponent setAvailableInteractionModels:];
-[_UISceneCarPlaySessionHostComponent setPrimaryInteractionModel:];
-[_UISceneCarPlaySessionHostComponent setTouchLevel:];
-[_UISceneCarPlaySessionHostComponent setTouchpadFeedbackDelegate:];
-[_UISceneCarPlaySessionHostComponent setTouchpads:];
-[_UISceneCarPlaySessionHostComponent touchLevel];
-[_UISceneCarPlaySessionHostComponent touchpadFeedbackDelegate];
-[_UISceneCarPlaySessionHostComponent touchpads];
```
