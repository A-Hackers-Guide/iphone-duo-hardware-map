# `_UIWTCProofreadingInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIInteraction`
- 3 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UITapGestureRecognizer" _proofreadingTap;
@"UIView" _view;
@"<_UIWTCProofreadingInteractionDelegate>" _delegate;
```

## Properties

```
@property (T@"<_UIWTCProofreadingInteractionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[_UIWTCProofreadingInteraction initWithDelegate:];
-[_UIWTCProofreadingInteraction tapInteraction:];
-[_UIWTCProofreadingInteraction view];
-[_UIWTCProofreadingInteraction setDelegate:];
-[_UIWTCProofreadingInteraction gestureRecognizerShouldBegin:];
-[_UIWTCProofreadingInteraction willMoveToView:];
-[_UIWTCProofreadingInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIWTCProofreadingInteraction delegate];
-[_UIWTCProofreadingInteraction didMoveToView:];
-[_UIWTCProofreadingInteraction proofreadingTapCreateIfNecessary];
```
