# `_UITextCursorDictationAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITextCursorAnimation`
- 14 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _soundReactiveCursorEnabled;
B _needsInitialDictationAnimation;
@"CADisplayLink" _soundReactiveCursorDisplayLink;
@"UIView" _glowContainerView;
@"UIView" _glowShapeView;
@"UIDictationGlowEffect" _glowEffect;
@"_UIDictationAudioLevelSmoother" _levelSmoother;
d _animationStartTime;
B _enabled;
@"UIView" _cursorShapeView;
@"UIStandardTextCursorView" _cursorView;
@"UIColor" _tintColor;
@"<_UIStandardTextCursorViewAudioLevelProvider>" _audioLevelProvider;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _animatedCursorShapeBounds;
```

## Properties

```
@property (T@"UIStandardTextCursorView",W,N,V_cursorView) cursorView;
@property (T@"UIColor",&,N,V_tintColor) tintColor;
@property (T@"<_UIStandardTextCursorViewAudioLevelProvider>",W,N,V_audioLevelProvider) audioLevelProvider;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_animatedCursorShapeBounds) animatedCursorShapeBounds;
@property (T@"UIView",R,W,N,V_cursorShapeView) cursorShapeView;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextCursorDictationAnimation _displayLinkFired:];
-[_UITextCursorDictationAnimation dealloc];
-[_UITextCursorDictationAnimation cursorShapeDidChange];
-[_UITextCursorDictationAnimation setAudioLevelProvider:];
-[_UITextCursorDictationAnimation setCursorView:];
-[_UITextCursorDictationAnimation isEnabled];
-[_UITextCursorDictationAnimation setTintColor:];
-[_UITextCursorDictationAnimation audioLevelProvider];
-[_UITextCursorDictationAnimation setEnabled:];
-[_UITextCursorDictationAnimation initWithCursorShapeView:];
-[_UITextCursorDictationAnimation cursorShapeView];
-[_UITextCursorDictationAnimation tintColor];
-[_UITextCursorDictationAnimation cursorView];
-[_UITextCursorDictationAnimation _setSoundReactiveCursorEnabled:];
-[_UITextCursorDictationAnimation _setCursorGlowEffectEnabled:];
-[_UITextCursorDictationAnimation animatedCursorShapeBounds];
-[_UITextCursorDictationAnimation setAnimatedCursorShapeBounds:];
-[_UITextCursorDictationAnimation setNeedsInitialDictationAnimation];
```
