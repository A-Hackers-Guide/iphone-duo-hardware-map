# `BWOverlaidRectangle`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
i _displayStyle;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
B _disappeared;
i _animationState;
@"BWRamp" _rampAnimation;
i _numFramesFullyVisible;
```

## Properties

```
@property (Ti,R,N,V_displayStyle) displayStyle;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_bounds) bounds;
@property (TB,N,V_disappeared) disappeared;
@property (Ti,N,V_animationState) animationState;
@property (T@"BWRamp",&,N,V_rampAnimation) rampAnimation;
@property (Ti,N,V_numFramesFullyVisible) numFramesFullyVisible;
```

## Instance methods

```
-[BWOverlaidRectangle animationState];
-[BWOverlaidRectangle displayStyle];
-[BWOverlaidRectangle dealloc];
-[BWOverlaidRectangle setBounds:];
-[BWOverlaidRectangle bounds];
-[BWOverlaidRectangle setAnimationState:];
-[BWOverlaidRectangle disappeared];
-[BWOverlaidRectangle setDisappeared:];
-[BWOverlaidRectangle initWithDisplayStyle:];
-[BWOverlaidRectangle numFramesFullyVisible];
-[BWOverlaidRectangle rampAnimation];
-[BWOverlaidRectangle setNumFramesFullyVisible:];
-[BWOverlaidRectangle setRampAnimation:];
```
