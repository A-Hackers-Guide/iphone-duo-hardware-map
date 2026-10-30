# `_UIConcreteAnimatedTextSpacerAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIAnimatedTextSpacerAnimation`
- 5 instance variables, 8 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _isFinalized;
f _progress;
@"_UIAnimatedTextSpacerAnimationInfo" _animationInfo;
@? _updateBlock;
@? _finalizeBlock;
```

## Properties

```
@property (T@"_UIAnimatedTextSpacerAnimationInfo",R,N,V_animationInfo) animationInfo;
@property (T@?,R,C,N,V_updateBlock) updateBlock;
@property (T@?,R,C,N,V_finalizeBlock) finalizeBlock;
@property (Tf,N,V_progress) progress;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIConcreteAnimatedTextSpacerAnimation finalize];
-[_UIConcreteAnimatedTextSpacerAnimation setProgress:];
-[_UIConcreteAnimatedTextSpacerAnimation updateBlock];
-[_UIConcreteAnimatedTextSpacerAnimation animationInfo];
-[_UIConcreteAnimatedTextSpacerAnimation progress];
-[_UIConcreteAnimatedTextSpacerAnimation finalizeBlock];
-[_UIConcreteAnimatedTextSpacerAnimation initWithAnimationInfo:updateBlock:finalizeBlock:];
```
