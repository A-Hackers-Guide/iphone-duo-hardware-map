# `_UIExpandingGlyphsView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIStatusBarDisplayable`, `CAAnimationDelegate`
- 8 instance variables, 21 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _expandsFromLeftToRight;
B _fadesOut;
i _remainingAnimationCount;
@"NSAttributedString" _attributedString;
d _baselineOffset;
@"NSArray" _imageViews;
@? _completionBlock;
{CGSize="width"d"height"d} _intrinsicSize;
```

## Properties

```
@property (TB,?,R,N) wantsCrossfade;
@property (TB,?,R,N) prefersBaselineAlignment;
@property (TB,?,R,N) prefersCenterVerticalAlignment;
@property (Tq,?,R,N) overriddenVerticalAlignment;
@property (T@"UIAccessibilityHUDItem",?,R,N) accessibilityHUDRepresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",&,N,V_imageViews) imageViews;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (Ti,N,V_remainingAnimationCount) remainingAnimationCount;
@property (T{CGSize=dd},N,V_intrinsicSize) intrinsicSize;
@property (T@"NSAttributedString",&,N,V_attributedString) attributedString;
@property (Td,R,N,V_baselineOffset) baselineOffset;
@property (TB,N,V_expandsFromLeftToRight) expandsFromLeftToRight;
@property (TB,N,V_fadesOut) fadesOut;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIExpandingGlyphsView baselineOffset];
-[_UIExpandingGlyphsView prefersBaselineAlignment];
-[_UIExpandingGlyphsView intrinsicContentSize];
-[_UIExpandingGlyphsView setCompletionBlock:];
-[_UIExpandingGlyphsView completionBlock];
-[_UIExpandingGlyphsView animationDidStop:finished:];
-[_UIExpandingGlyphsView setAttributedString:];
-[_UIExpandingGlyphsView attributedString];
-[_UIExpandingGlyphsView sizeThatFits:];
-[_UIExpandingGlyphsView initWithFrame:];
-[_UIExpandingGlyphsView animateCompletionBlock:];
-[_UIExpandingGlyphsView expandsFromLeftToRight];
-[_UIExpandingGlyphsView fadesOut];
-[_UIExpandingGlyphsView imageViews];
-[_UIExpandingGlyphsView intrinsicSize];
-[_UIExpandingGlyphsView remainingAnimationCount];
-[_UIExpandingGlyphsView setExpandsFromLeftToRight:];
-[_UIExpandingGlyphsView setFadesOut:];
-[_UIExpandingGlyphsView setImageViews:];
-[_UIExpandingGlyphsView setIntrinsicSize:];
-[_UIExpandingGlyphsView setRemainingAnimationCount:];
```
