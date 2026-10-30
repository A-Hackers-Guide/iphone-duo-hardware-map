# `_UIDynamicCaretInput`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 6 properties, 28 instance methods, 0 class methods

## Instance variables

```
^{CGContext=} _bitmapContext;
q _fadeCount;
{CGPoint="x"d"y"d} _lastViewLoc;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inkedAreaOfBitmapContext;
@"NSTimer" _fadeTimer;
@"TIHandwritingStrokes" _accumulatedStrokes;
@"UIDelayedAction" _committedAction;
@"_UIDynamicCaretDot" _dotView;
```

## Properties

```
@property (T@"NSTimer",&,N,V_fadeTimer) fadeTimer;
@property (T@"TIHandwritingStrokes",&,N,V_accumulatedStrokes) accumulatedStrokes;
@property (T@"UIDelayedAction",&,N,V_committedAction) committedAction;
@property (T@"_UIDynamicCaretDot",&,N,V_dotView) dotView;
@property (TB,R,N) hasInk;
@property (TB,R,N) isInking;
```

## Instance methods

```
-[_UIDynamicCaretInput send];
-[_UIDynamicCaretInput dealloc];
-[_UIDynamicCaretInput drawRect:];
-[_UIDynamicCaretInput setFrame:];
-[_UIDynamicCaretInput setNeedsDisplayInRect:];
-[_UIDynamicCaretInput log];
-[_UIDynamicCaretInput initWithFrame:];
-[_UIDynamicCaretInput clearAndNotify:];
-[_UIDynamicCaretInput committedAction];
-[_UIDynamicCaretInput dotView];
-[_UIDynamicCaretInput _fadeInk];
-[_UIDynamicCaretInput accumulatedStrokes];
-[_UIDynamicCaretInput addInkPoint:fromLastPoint:];
-[_UIDynamicCaretInput addTouchAtPoint:];
-[_UIDynamicCaretInput cancelTouchAtPoint:];
-[_UIDynamicCaretInput clearFadeTimer];
-[_UIDynamicCaretInput committedStrokes];
-[_UIDynamicCaretInput drawPoint:];
-[_UIDynamicCaretInput endTouchAtPoint:];
-[_UIDynamicCaretInput fadeTimer];
-[_UIDynamicCaretInput hasInk];
-[_UIDynamicCaretInput inkWidth];
-[_UIDynamicCaretInput isInking];
-[_UIDynamicCaretInput setAccumulatedStrokes:];
-[_UIDynamicCaretInput setCommittedAction:];
-[_UIDynamicCaretInput setDotView:];
-[_UIDynamicCaretInput setFadeTimer:];
-[_UIDynamicCaretInput startTouchAtPoint:];
```
