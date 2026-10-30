# `SBFluidSwitcherSpaceUnderlayAccessoryView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughClippingView`
- Protocols: `SBFluidSwitcherItemContainerHeaderViewDelegate`
- 22 instance variables, 19 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"SBFTouchPassThroughView" _contentView;
@"SBAppSwitcherSettings" _settings;
@"SBSystemPointerInteractionManager" _systemPointerInteractionManager;
@"SBFluidSwitcherItemContainerHeaderView" _headerView;
B _headerNeedsNonAnimatedLayout;
@"UIView" _backgroundView;
@"SBAppSwitcherPageShadowView" _shadowView;
B _trailingIconOpacityMatchesTextOpacity;
@"<SBFluidSwitcherSpaceUnderlayAccessoryViewDelegate>" _delegate;
d _cornerRadius;
Q _maskedCorners;
d _contentScale;
d _headerOpacity;
d _titleOpacity;
@"NSArray" _titleItems;
d _backgroundOpacity;
d _shadowAlpha;
d _shadowOffset;
q _shadowStyle;
@"UIBezierPath" _shadowPath;
d _contentViewScale;
{CGPoint="x"d"y"d} _contentViewOffset;
```

## Properties

```
@property (T@"<SBFluidSwitcherSpaceUnderlayAccessoryViewDelegate>",R,W,N,V_delegate) delegate;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (TQ,N,V_maskedCorners) maskedCorners;
@property (Td,N,V_contentScale) contentScale;
@property (Td,R,N,V_headerOpacity) headerOpacity;
@property (Td,N,V_titleOpacity) titleOpacity;
@property (TB,N,V_trailingIconOpacityMatchesTextOpacity) trailingIconOpacityMatchesTextOpacity;
@property (T@"NSArray",R,C,N,V_titleItems) titleItems;
@property (Td,N,V_backgroundOpacity) backgroundOpacity;
@property (Td,N,V_shadowAlpha) shadowAlpha;
@property (Td,N,V_shadowOffset) shadowOffset;
@property (Tq,N,V_shadowStyle) shadowStyle;
@property (T@"UIBezierPath",&,N,V_shadowPath) shadowPath;
@property (Td,N,V_contentViewScale) contentViewScale;
@property (T{CGPoint=dd},N,V_contentViewOffset) contentViewOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherSpaceUnderlayAccessoryView contentViewScale];
-[SBFluidSwitcherSpaceUnderlayAccessoryView shadowStyle];
-[SBFluidSwitcherSpaceUnderlayAccessoryView contentViewOffset];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setTitleOpacity:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setShadowStyle:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setShadowAlpha:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setShadowPath:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView shadowAlpha];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setContentViewScale:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setContentViewOffset:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setTitleItems:animated:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView titleOpacity];
-[SBFluidSwitcherSpaceUnderlayAccessoryView titleItems];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setBackgroundOpacity:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView _updateShadowVisibility];
-[SBFluidSwitcherSpaceUnderlayAccessoryView backgroundOpacity];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setShadowOffset:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView dealloc];
-[SBFluidSwitcherSpaceUnderlayAccessoryView _updateShadowView];
-[SBFluidSwitcherSpaceUnderlayAccessoryView _updateBackgroundView];
-[SBFluidSwitcherSpaceUnderlayAccessoryView layoutSubviews];
-[SBFluidSwitcherSpaceUnderlayAccessoryView hitTest:withEvent:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView maskedCorners];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setCornerRadius:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView shadowPath];
-[SBFluidSwitcherSpaceUnderlayAccessoryView trailingIconOpacityMatchesTextOpacity];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setMaskedCorners:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setHeaderOpacity:updateMode:settings:completion:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView prepareForReuse];
-[SBFluidSwitcherSpaceUnderlayAccessoryView cornerRadius];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setContentScale:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView contentScale];
-[SBFluidSwitcherSpaceUnderlayAccessoryView delegate];
-[SBFluidSwitcherSpaceUnderlayAccessoryView initWithDelegate:systemPointerInteractionManager:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView _updateContentView];
-[SBFluidSwitcherSpaceUnderlayAccessoryView headerOpacity];
-[SBFluidSwitcherSpaceUnderlayAccessoryView setTrailingIconOpacityMatchesTextOpacity:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView pointInside:withEvent:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView _configureDebugBorder];
-[SBFluidSwitcherSpaceUnderlayAccessoryView shadowOffset];
-[SBFluidSwitcherSpaceUnderlayAccessoryView _updateHeaderAnimated:];
-[SBFluidSwitcherSpaceUnderlayAccessoryView _updateBackgroundViewVisibility];
-[SBFluidSwitcherSpaceUnderlayAccessoryView itemContainerHeaderView:didSelectTitleItem:];
```
