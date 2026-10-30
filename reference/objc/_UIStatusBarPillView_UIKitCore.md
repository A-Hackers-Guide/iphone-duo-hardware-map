# `_UIStatusBarPillView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarRoundedCornerView`
- Protocols: `_UIStatusBarDisplayable`, `_UIStatusBarPersistentAnimation`
- 7 instance variables, 16 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _pulsing;
@"UIVisualEffect" _visualEffect;
@"UIColor" _pillColor;
@"UIView" _subviewForBaselineAlignment;
@"CALayer" _pulseLayer;
@"UIVisualEffectView" _visualEffectView;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _alignmentRectInsets;
```

## Properties

```
@property (T@"CALayer",&,N,V_pulseLayer) pulseLayer;
@property (T@"UIVisualEffectView",&,N,V_visualEffectView) visualEffectView;
@property (T{UIEdgeInsets=dddd},N,V_alignmentRectInsets) alignmentRectInsets;
@property (TB,N,V_pulsing) pulsing;
@property (T@"UIVisualEffect",&,N,V_visualEffect) visualEffect;
@property (T@"UIColor",&,N,V_pillColor) pillColor;
@property (T@"UIView",W,N,V_subviewForBaselineAlignment) subviewForBaselineAlignment;
@property (TB,?,R,N) wantsCrossfade;
@property (TB,?,R,N) prefersBaselineAlignment;
@property (TB,?,R,N) prefersCenterVerticalAlignment;
@property (Tq,?,R,N) overriddenVerticalAlignment;
@property (T@"UIAccessibilityHUDItem",?,R,N) accessibilityHUDRepresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIStatusBarPillView pulsing];
-[_UIStatusBarPillView setPillColor:];
-[_UIStatusBarPillView resumePersistentAnimation];
-[_UIStatusBarPillView applyStyleAttributes:];
-[_UIStatusBarPillView visualEffectView];
-[_UIStatusBarPillView isUserInteractionEnabled];
-[_UIStatusBarPillView setSubviewForBaselineAlignment:];
-[_UIStatusBarPillView didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIStatusBarPillView alignmentRectInsets];
-[_UIStatusBarPillView subviewForBaselineAlignment];
-[_UIStatusBarPillView viewForLastBaselineLayout];
-[_UIStatusBarPillView layoutSubviews];
-[_UIStatusBarPillView setVisualEffectView:];
-[_UIStatusBarPillView visualEffect];
-[_UIStatusBarPillView pillColor];
-[_UIStatusBarPillView canBecomeFocused];
-[_UIStatusBarPillView setPulseLayer:];
-[_UIStatusBarPillView setAlignmentRectInsets:];
-[_UIStatusBarPillView pulseLayer];
-[_UIStatusBarPillView setPulsing:];
-[_UIStatusBarPillView _updateBackgroundColor];
-[_UIStatusBarPillView initWithFrame:];
-[_UIStatusBarPillView setVisualEffect:];
```
