# `LAUIPearlGlyphLabel`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 26 instance variables, 5 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"UIView" _container;
@"CABackdropLayer" _background;
@"UIView" _labelContainer;
@"UILabel" _label;
@"UIView" _glyphContainer;
@"LAUIPearlGlyphView" _glyph;
{map<CALayer *__unsafe_unretained, CALayer *, std::less<CALayer *__unsafe_unretained>, std::allocator<std::pair<CALayer *const __unsafe_unretained, CALayer *>>>="__tree_"{__tree<std::__value_type<CALayer *__unsafe_unretained, CALayer *>, std::__map_value_compare<CALayer *__unsafe_unretained, std::pair<CALayer *const __unsafe_unretained, CALayer *>, std::less<CALayer *__unsafe_unretained>>, std::allocator<std::pair<CALayer *const __unsafe_unretained, CALayer *>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _masks;
{vector<UIView *, std::allocator<UIView *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _labelSnapshots;
@"UIColor" _backgroundColor;
@"UIColor" _textColor;
@"UIFont" _baseFont;
{CGSize="width"d"height"d} _currentLabelSize;
{CGSize="width"d"height"d} _currentMaximumSize;
@"NSObject<OS_dispatch_source>" _visibilityTimer;
B _inWindow;
B _textNeedsUpdate;
B _textUpdateNeedsAnimation;
B _visible;
B _visibleNeedsUpdate;
B _allowDelayedVisibility;
B _animated;
B _reduceBlur;
B _shimmerEnabled;
q _style;
@"NSString" _text;
{CGSize="width"d"height"d} _maximumSize;
```

## Properties

```
@property (TB,D,N) inApplicationContext;
@property (Tq,R,N,V_style) style;
@property (TB,R,N,GisShimmerEnabled,V_shimmerEnabled) shimmerEnabled;
@property (T@"NSString",R,C,N,V_text) text;
@property (T{CGSize=dd},R,N,V_maximumSize) maximumSize;
```

## Instance methods

```
-[LAUIPearlGlyphLabel didMoveToWindow];
-[LAUIPearlGlyphLabel maximumSize];
-[LAUIPearlGlyphLabel text];
-[LAUIPearlGlyphLabel applicationDidBecomeActive:];
-[LAUIPearlGlyphLabel setStyle:animated:];
-[LAUIPearlGlyphLabel init];
-[LAUIPearlGlyphLabel dealloc];
-[LAUIPearlGlyphLabel layoutSubviews];
-[LAUIPearlGlyphLabel initWithStyle:];
-[LAUIPearlGlyphLabel style];
-[LAUIPearlGlyphLabel _updateText];
-[LAUIPearlGlyphLabel invalidate];
-[LAUIPearlGlyphLabel sizeThatFits:];
-[LAUIPearlGlyphLabel contentSizeCategoryDidChange:];
-[LAUIPearlGlyphLabel initWithFrame:];
-[LAUIPearlGlyphLabel _updateVisibilityAnimated:];
-[LAUIPearlGlyphLabel setInApplicationContext:];
-[LAUIPearlGlyphLabel _applyStyle];
-[LAUIPearlGlyphLabel layoutIfNeededAnimated:];
-[LAUIPearlGlyphLabel _applyVisibilityAnimated:];
-[LAUIPearlGlyphLabel _updateBoundsSizeAnimated:];
-[LAUIPearlGlyphLabel _updateFontAnimated:];
-[LAUIPearlGlyphLabel _updateGlyphPaused];
-[LAUIPearlGlyphLabel _updateReduceBlurState];
-[LAUIPearlGlyphLabel boldTextStatusDidChange:];
-[LAUIPearlGlyphLabel inApplicationContext];
-[LAUIPearlGlyphLabel isShimmerEnabled];
-[LAUIPearlGlyphLabel reduceMotionDidChange:];
-[LAUIPearlGlyphLabel reduceTransparencyDidChange:];
-[LAUIPearlGlyphLabel setMaximumSize:animated:];
-[LAUIPearlGlyphLabel setShimmerEnabled:animated:];
-[LAUIPearlGlyphLabel setText:animated:];
```
