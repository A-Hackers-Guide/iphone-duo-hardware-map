# `_UITextCursorTrailingGlowView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAAnimationDelegate`
- 8 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"_UIShapeView" _shapeView;
@"UIDictationGlowEffect" _dictationGlowEffect;
@"CABasicAnimation" _animation;
d _animationStartTime;
B _needsToUpdateAnimation;
B _trailingAnimationEnabled;
@? _transitionBlock;
@? _willBeginAnimationBlock;
```

## Properties

```
@property (T@?,C,N,V_transitionBlock) transitionBlock;
@property (T@?,C,N,V_willBeginAnimationBlock) willBeginAnimationBlock;
@property (TB,N,GisTrailingAnimationEnabled,V_trailingAnimationEnabled) trailingAnimationEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextCursorTrailingGlowView animationDidStart:];
-[_UITextCursorTrailingGlowView setTransitionBlock:];
-[_UITextCursorTrailingGlowView animationDidStop:finished:];
-[_UITextCursorTrailingGlowView willBeginAnimationBlock];
-[_UITextCursorTrailingGlowView pathForRect:];
-[_UITextCursorTrailingGlowView estimatedCurrentFrame];
-[_UITextCursorTrailingGlowView setTintColor:];
-[_UITextCursorTrailingGlowView _updateShapeAndAnimate];
-[_UITextCursorTrailingGlowView transitionBlock];
-[_UITextCursorTrailingGlowView isTrailingAnimationEnabled];
-[_UITextCursorTrailingGlowView setTrailingAnimationEnabled:];
-[_UITextCursorTrailingGlowView cursorDidMoveToFrame:fromPreviousFrame:isNewLine:];
-[_UITextCursorTrailingGlowView setWillBeginAnimationBlock:];
-[_UITextCursorTrailingGlowView initWithFrame:];
-[_UITextCursorTrailingGlowView _animate];
```
