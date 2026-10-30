# `SBFluidSwitcherItemContainerFooterView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughView`
- Protocols: `PTSettingsKeyObserver`, `UIPointerInteractionDelegate`
- 16 instance variables, 13 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _iconViews;
@"NSMutableArray" _titleLabels;
@"BSUIEmojiLabelView" _subtitleLabel;
q _subtitleStylingUserInterfaceStyle;
@"NSArray" _titleItems;
@"NSArray" _visibleTitleItems;
@"SBMedusaSettings" _settings;
B _uniqueIconsOnly;
B _wantsIconPointerInteractions;
@"<SBFluidSwitcherItemContainerFooterViewDelegate>" _delegate;
Q _footerStyle;
d _iconAlpha;
d _textAlpha;
Q _iconAlignment;
d _iconHitTestOutset;
@"UITapGestureRecognizer" _tapGestureRecognizer;
```

## Properties

```
@property (T@"<SBFluidSwitcherItemContainerFooterViewDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,N,V_footerStyle) footerStyle;
@property (Td,N,V_iconAlpha) iconAlpha;
@property (Td,N,V_textAlpha) textAlpha;
@property (TQ,N,V_iconAlignment) iconAlignment;
@property (TB,N,V_uniqueIconsOnly) uniqueIconsOnly;
@property (TB,N,V_wantsIconPointerInteractions) wantsIconPointerInteractions;
@property (Td,N,V_iconHitTestOutset) iconHitTestOutset;
@property (T@"UITapGestureRecognizer",R,N,V_tapGestureRecognizer) tapGestureRecognizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherItemContainerFooterView iconHitTestOutset];
-[SBFluidSwitcherItemContainerFooterView footerStyle];
-[SBFluidSwitcherItemContainerFooterView tapGestureRecognizer];
-[SBFluidSwitcherItemContainerFooterView setUniqueIconsOnly:];
-[SBFluidSwitcherItemContainerFooterView setIconAlignment:];
-[SBFluidSwitcherItemContainerFooterView setFooterStyle:];
-[SBFluidSwitcherItemContainerFooterView iconAlignment];
-[SBFluidSwitcherItemContainerFooterView uniqueIconsOnly];
-[SBFluidSwitcherItemContainerFooterView setTitleItems:animated:];
-[SBFluidSwitcherItemContainerFooterView setIconHitTestOutset:];
-[SBFluidSwitcherItemContainerFooterView intrinsicContentSize];
-[SBFluidSwitcherItemContainerFooterView pointerInteraction:styleForRegion:];
-[SBFluidSwitcherItemContainerFooterView dealloc];
-[SBFluidSwitcherItemContainerFooterView layoutSubviews];
-[SBFluidSwitcherItemContainerFooterView settings:changedValueForKey:];
-[SBFluidSwitcherItemContainerFooterView _handleTapGestureRecognizer:];
-[SBFluidSwitcherItemContainerFooterView _updateLabels];
-[SBFluidSwitcherItemContainerFooterView pointerInteraction:regionForRequest:defaultRegion:];
-[SBFluidSwitcherItemContainerFooterView delegate];
-[SBFluidSwitcherItemContainerFooterView _contentSizeCategoryDidChange:];
-[SBFluidSwitcherItemContainerFooterView setTextAlpha:];
-[SBFluidSwitcherItemContainerFooterView pointInside:withEvent:];
-[SBFluidSwitcherItemContainerFooterView initWithFrame:delegate:];
-[SBFluidSwitcherItemContainerFooterView textAlpha];
-[SBFluidSwitcherItemContainerFooterView iconAlpha];
-[SBFluidSwitcherItemContainerFooterView setIconAlpha:];
-[SBFluidSwitcherItemContainerFooterView _updateSubtitleLabel];
-[SBFluidSwitcherItemContainerFooterView _hasTitleShadow];
-[SBFluidSwitcherItemContainerFooterView _attributedTextFromText:];
-[SBFluidSwitcherItemContainerFooterView _isTextEffectivelyEmpty:];
-[SBFluidSwitcherItemContainerFooterView _makeIconView];
-[SBFluidSwitcherItemContainerFooterView _makeLabel];
-[SBFluidSwitcherItemContainerFooterView _makeSubtitleLabel];
-[SBFluidSwitcherItemContainerFooterView _maximumTitleLabelHeight];
-[SBFluidSwitcherItemContainerFooterView _reloadVisibleTitleItems];
-[SBFluidSwitcherItemContainerFooterView _updateIconPointerInteractions];
-[SBFluidSwitcherItemContainerFooterView _updateIconViewShadow:];
-[SBFluidSwitcherItemContainerFooterView _updateIconViewsAndLabels];
-[SBFluidSwitcherItemContainerFooterView setWantsIconPointerInteractions:];
-[SBFluidSwitcherItemContainerFooterView wantsIconPointerInteractions];
```
