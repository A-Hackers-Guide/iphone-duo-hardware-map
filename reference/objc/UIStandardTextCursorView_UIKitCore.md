# `UIStandardTextCursorView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAAnimationDelegate`, `_UITextSelectionWidgetAnimating`, `_UIAssertionControllerSubject`, `UITextCursorView`
- 16 instance variables, 18 properties, 42 instance methods, 0 class methods

## Instance variables

```
@"UIView" _cursorShapeView;
@"_UITextCursorBlinkAnimation" _blinkAnimation;
@"_UITextCursorDictationAnimation" _dictationAnimation;
@"_UITextCursorIntelligenceAnimation" _intelligenceAnimation;
@"NSMutableSet" _cursorAnimations;
@"_UIAssertionController" _assertionController;
@"UIStandardTextCursorView" _trackedFloatingCursorView;
B _blinking;
B _hiddenForLoupeAnimation;
B _glowEffectEnabled;
B _floatingEffectEnabled;
B _ghostEffectEnabled;
B _intelligenceModeEnabled;
B _hasText;
d _shapeScale;
@"<_UIStandardTextCursorViewAudioLevelProvider>" _audioLevelProvider;
```

## Properties

```
@property (TB,N,GisGlowEffectEnabled,V_glowEffectEnabled) glowEffectEnabled;
@property (TB,N,GisFloatingEffectEnabled,V_floatingEffectEnabled) floatingEffectEnabled;
@property (TB,N,GisGhostEffectEnabled,V_ghostEffectEnabled) ghostEffectEnabled;
@property (TB,N,GisIntelligenceModeEnabled,V_intelligenceModeEnabled) intelligenceModeEnabled;
@property (TB,N,V_hasText) hasText;
@property (Td,N,S_setShapeScale:,V_shapeScale) _shapeScale;
@property (T@"<_UIStandardTextCursorViewAudioLevelProvider>",W,N,V_audioLevelProvider) audioLevelProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,N) originView;
@property (T{?={CGPoint=dd}{CGRect={CGPoint=dd}{CGSize=dd}}d@},R,N) originShape;
@property (T{?=@dd{CGSize=dd}},R,N) originShadow;
@property (TB,N,V_hiddenForLoupeAnimation) hiddenForLoupeAnimation;
@property (TB,R,N) crossfadeOnDismissal;
@property (TB,N,GisBlinking,V_blinking) blinking;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
```

## Instance methods

```
-[UIStandardTextCursorView hasText];
-[UIStandardTextCursorView assertionActivationStateForType:];
-[UIStandardTextCursorView originView];
-[UIStandardTextCursorView _trackingFloatingCursorView];
-[UIStandardTextCursorView isIntelligenceModeEnabled];
-[UIStandardTextCursorView setHidden:];
-[UIStandardTextCursorView originShape:];
-[UIStandardTextCursorView setBlinking:];
-[UIStandardTextCursorView _setShapeScale:];
-[UIStandardTextCursorView _setNeedsInitialDictationAnimation];
-[UIStandardTextCursorView originShape];
-[UIStandardTextCursorView layoutSubviews];
-[UIStandardTextCursorView setHasText:];
-[UIStandardTextCursorView hitTest:withEvent:];
-[UIStandardTextCursorView isGhostEffectEnabled];
-[UIStandardTextCursorView isFloatingEffectEnabled];
-[UIStandardTextCursorView _updateShadow];
-[UIStandardTextCursorView _performBulgeAnimation];
-[UIStandardTextCursorView isGlowEffectEnabled];
-[UIStandardTextCursorView setGlowEffectEnabled:];
-[UIStandardTextCursorView setAudioLevelProvider:];
-[UIStandardTextCursorView crossfadeOnDismissal];
-[UIStandardTextCursorView tintColorDidChange];
-[UIStandardTextCursorView setFloatingEffectEnabled:];
-[UIStandardTextCursorView audioLevelProvider];
-[UIStandardTextCursorView setIntelligenceModeEnabled:];
-[UIStandardTextCursorView setGhostEffectEnabled:];
-[UIStandardTextCursorView originShadow];
-[UIStandardTextCursorView assertionActivationStateChangedToState:forType:];
-[UIStandardTextCursorView resetBlinkAnimation];
-[UIStandardTextCursorView isBlinking];
-[UIStandardTextCursorView setHiddenForLoupeAnimation:];
-[UIStandardTextCursorView _intelligenceAnimation];
-[UIStandardTextCursorView obtainBlinkAnimationSuppressionAssertionForReason:];
-[UIStandardTextCursorView _createFloatingCursorView];
-[UIStandardTextCursorView hiddenForLoupeAnimation];
-[UIStandardTextCursorView initWithFrame:];
-[UIStandardTextCursorView _cursorShapeRectForBounds:];
-[UIStandardTextCursorView _shapeScale];
-[UIStandardTextCursorView _shadowSpecForEffects];
-[UIStandardTextCursorView _fillColorForEffects];
-[UIStandardTextCursorView _dictationAnimation];
```
