# `_UIInteractionEffect_deprecated`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDynamicReferenceSystem`
- 13 instance variables, 9 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UIDynamicAnimator" _animator;
@"_UIDynamicTransformer" _transformer;
@"_UISpringBehavior" _springBehavior;
@"UIPushBehavior" _forceBehavior;
@"UIDynamicItemBehavior" _itemProperties;
d _damping;
d _frequency;
d _density;
d _resistance;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _preferredContentTransform;
d _progress;
d _forceFactor;
@? _updateBlock;
```

## Properties

```
@property (Td,N,V_forceFactor) forceFactor;
@property (T@?,C,N,V_updateBlock) updateBlock;
@property (T{CGAffineTransform=dddddd},R,D,N) preferredContentTransform;
@property (Td,R,N) progress;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIInteractionEffect_deprecated setUpdateBlock:];
-[_UIInteractionEffect_deprecated init];
-[_UIInteractionEffect_deprecated updateBlock];
-[_UIInteractionEffect_deprecated progress];
-[_UIInteractionEffect_deprecated bounds];
-[_UIInteractionEffect_deprecated _stopAnimations];
-[_UIInteractionEffect_deprecated setForceFactor:];
-[_UIInteractionEffect_deprecated _prepareAnimatorIfNeeded];
-[_UIInteractionEffect_deprecated _updateAnimatorIfNeeded];
-[_UIInteractionEffect_deprecated _updateFromTransformer:];
-[_UIInteractionEffect_deprecated forceFactor];
-[_UIInteractionEffect_deprecated preferredContentTransform];
```
