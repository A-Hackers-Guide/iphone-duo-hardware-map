# `_UIStatusBarStringView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILabel`
- Protocols: `_UIStatusBarDisplayable`
- 6 instance variables, 15 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _showsAlternateText;
q _fontStyle;
@"NSString" _alternateText;
@"NSString" _originalText;
@"NSTimer" _alternateTextTimer;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _alignmentRectInsets;
```

## Properties

```
@property (TB,N,V_showsAlternateText) showsAlternateText;
@property (T@"NSString",C,N,V_originalText) originalText;
@property (T@"NSTimer",R,N,V_alternateTextTimer) alternateTextTimer;
@property (Tq,N,V_fontStyle) fontStyle;
@property (T{UIEdgeInsets=dddd},N,V_alignmentRectInsets) alignmentRectInsets;
@property (T@"NSString",C,N,V_alternateText) alternateText;
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
-[_UIStatusBarStringView setFontStyle:];
-[_UIStatusBarStringView prefersBaselineAlignment];
-[_UIStatusBarStringView accessibilityHUDRepresentation];
-[_UIStatusBarStringView fontStyle];
-[_UIStatusBarStringView didMoveToWindow];
-[_UIStatusBarStringView applyStyleAttributes:];
-[_UIStatusBarStringView alignmentRectInsets];
-[_UIStatusBarStringView showsAlternateText];
-[_UIStatusBarStringView setShowsAlternateText:];
-[_UIStatusBarStringView setAlternateText:];
-[_UIStatusBarStringView _updateAlternateTextTimer];
-[_UIStatusBarStringView alternateTextTimer];
-[_UIStatusBarStringView setAlignmentRectInsets:];
-[_UIStatusBarStringView setText:];
-[_UIStatusBarStringView wantsCrossfade];
-[_UIStatusBarStringView alternateText];
-[_UIStatusBarStringView initWithFrame:];
-[_UIStatusBarStringView originalText];
-[_UIStatusBarStringView setOriginalText:];
```
