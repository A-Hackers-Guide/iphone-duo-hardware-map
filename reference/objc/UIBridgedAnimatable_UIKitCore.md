# `UIBridgedAnimatable`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _isFinished;
@"CALayer" _layer;
@"NSString" _key;
@"<UIVectorOperatable>" _fromValue;
@"<UIVectorOperatable>" _toValue;
@"CAPresentationModifier" _presentationModifier;
@? _completion;
```

## Properties

```
@property (T@"CALayer",&,N,V_layer) layer;
@property (T@"NSString",&,N,V_key) key;
@property (T@"<UIVectorOperatable>",&,N,V_fromValue) fromValue;
@property (T@"<UIVectorOperatable>",&,N,V_toValue) toValue;
@property (T@"CAPresentationModifier",&,N,V_presentationModifier) presentationModifier;
@property (TB,N,V_isFinished) isFinished;
@property (T@?,C,N,V_completion) completion;
```

## Instance methods

```
-[UIBridgedAnimatable setCompletion:];
-[UIBridgedAnimatable updateWithProgress:];
-[UIBridgedAnimatable isFinished];
-[UIBridgedAnimatable completion];
-[UIBridgedAnimatable layer];
-[UIBridgedAnimatable dealloc];
-[UIBridgedAnimatable setKey:];
-[UIBridgedAnimatable key];
-[UIBridgedAnimatable toValue];
-[UIBridgedAnimatable fromValue];
-[UIBridgedAnimatable setFromValue:];
-[UIBridgedAnimatable setLayer:];
-[UIBridgedAnimatable setToValue:];
-[UIBridgedAnimatable animationDidFinish:];
-[UIBridgedAnimatable initWithLayer:key:fromValue:toValue:completion:];
-[UIBridgedAnimatable presentationModifier];
-[UIBridgedAnimatable setIsFinished:];
-[UIBridgedAnimatable setPresentationModifier:];
```
