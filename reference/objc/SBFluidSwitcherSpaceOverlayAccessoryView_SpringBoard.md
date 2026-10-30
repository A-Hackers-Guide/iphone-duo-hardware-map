# `SBFluidSwitcherSpaceOverlayAccessoryView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFTouchPassThroughClippingView`
- Protocols: `SBFluidSwitcherItemContainerFooterViewDelegate`, `SBSwitcherGenieEffectViewDelegate`, `SBFluidSwitcherHomeGrabberViewHosting`
- 27 instance variables, 26 properties, 60 instance methods, 0 class methods

## Instance variables

```
@"SBFTouchPassThroughView" _contentView;
@"SBAppSwitcherSettings" _settings;
@"SBFluidSwitcherItemContainerFooterView" _footerView;
B _drawsFocusIndicator;
@"CAShapeLayer" _focusIndicatorLayer;
@"SBFluidSwitcherIconOverlayView" _iconOverlayView;
@"SBSwitcherGenieEffectView" _genieEffectView;
B _drawsFooter;
B _uniqueIconsOnly;
B _wantsPointerInteractions;
@"SBHomeGrabberRotationView" _homeGrabberView;
@"<SBFluidSwitcherSpaceOverlayAccessoryViewDelegate>" _delegate;
d _cornerRadius;
Q _maskedCorners;
d _contentScale;
d _iconHitTestOutset;
Q _iconAlignment;
d _iconOpacity;
d _titleAndIconOpacity;
d _titleOpacity;
Q _footerStyle;
@"NSArray" _titleItems;
@"SBAppLayout" _appLayoutForIconOverlay;
@"SBSwitcherShelfViewController" _shelfViewController;
@"SBSwitcherStrongPairIndicatorView" _strongPairIndicatorView;
d _contentViewScale;
{CGPoint="x"d"y"d} _contentViewOffset;
```

## Properties

```
@property (T@"<SBFluidSwitcherSpaceOverlayAccessoryViewDelegate>",R,W,N,V_delegate) delegate;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (TQ,N,V_maskedCorners) maskedCorners;
@property (Td,N,V_contentScale) contentScale;
@property (TB,N,V_drawsFocusIndicator) drawsFocusIndicator;
@property (TB,N,V_drawsFooter) drawsFooter;
@property (TB,N,V_uniqueIconsOnly) uniqueIconsOnly;
@property (TB,N,V_wantsPointerInteractions) wantsPointerInteractions;
@property (Td,N,V_iconHitTestOutset) iconHitTestOutset;
@property (TQ,N,V_iconAlignment) iconAlignment;
@property (Td,N,V_iconOpacity) iconOpacity;
@property (Td,N,V_titleAndIconOpacity) titleAndIconOpacity;
@property (Td,N,V_titleOpacity) titleOpacity;
@property (TQ,N,V_footerStyle) footerStyle;
@property (T@"NSArray",C,N,V_titleItems) titleItems;
@property (T@"SBAppLayout",R,N,V_appLayoutForIconOverlay) appLayoutForIconOverlay;
@property (T@"SBSwitcherShelfViewController",&,N,V_shelfViewController) shelfViewController;
@property (T@"SBSwitcherGenieAttributes",R,N) genieAttributes;
@property (T@"SBSwitcherStrongPairIndicatorView",&,N,V_strongPairIndicatorView) strongPairIndicatorView;
@property (Td,N,V_contentViewScale) contentViewScale;
@property (T{CGPoint=dd},N,V_contentViewOffset) contentViewOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBHomeGrabberRotationView",&,N,V_homeGrabberView) homeGrabberView;
```

## Instance methods

```
-[SBFluidSwitcherSpaceOverlayAccessoryView contentViewScale];
-[SBFluidSwitcherSpaceOverlayAccessoryView contentViewOffset];
-[SBFluidSwitcherSpaceOverlayAccessoryView setGenieAttributes:mode:completion:];
-[SBFluidSwitcherSpaceOverlayAccessoryView genieEffectViewDidInvalidate:];
-[SBFluidSwitcherSpaceOverlayAccessoryView setTitleOpacity:];
-[SBFluidSwitcherSpaceOverlayAccessoryView iconHitTestOutset];
-[SBFluidSwitcherSpaceOverlayAccessoryView footerStyle];
-[SBFluidSwitcherSpaceOverlayAccessoryView wantsPointerInteractions];
-[SBFluidSwitcherSpaceOverlayAccessoryView drawsFocusIndicator];
-[SBFluidSwitcherSpaceOverlayAccessoryView setUniqueIconsOnly:];
-[SBFluidSwitcherSpaceOverlayAccessoryView setIconAlignment:];
-[SBFluidSwitcherSpaceOverlayAccessoryView _updateFooterVisibility];
-[SBFluidSwitcherSpaceOverlayAccessoryView setFooterStyle:];
-[SBFluidSwitcherSpaceOverlayAccessoryView setTitleItems:];
-[SBFluidSwitcherSpaceOverlayAccessoryView iconAlignment];
-[SBFluidSwitcherSpaceOverlayAccessoryView uniqueIconsOnly];
-[SBFluidSwitcherSpaceOverlayAccessoryView setContentViewScale:];
-[SBFluidSwitcherSpaceOverlayAccessoryView titleAndIconOpacity];
-[SBFluidSwitcherSpaceOverlayAccessoryView setContentViewOffset:];
-[SBFluidSwitcherSpaceOverlayAccessoryView setTitleItems:animated:];
-[SBFluidSwitcherSpaceOverlayAccessoryView setHomeGrabberView:];
-[SBFluidSwitcherSpaceOverlayAccessoryView homeGrabberView];
-[SBFluidSwitcherSpaceOverlayAccessoryView setIconHitTestOutset:];
-[SBFluidSwitcherSpaceOverlayAccessoryView setWantsPointerInteractions:];
-[SBFluidSwitcherSpaceOverlayAccessoryView drawsFooter];
-[SBFluidSwitcherSpaceOverlayAccessoryView genieEffectViewDidBegin:];
-[SBFluidSwitcherSpaceOverlayAccessoryView titleOpacity];
-[SBFluidSwitcherSpaceOverlayAccessoryView genieAttributes];
-[SBFluidSwitcherSpaceOverlayAccessoryView titleItems];
-[SBFluidSwitcherSpaceOverlayAccessoryView iconOpacity];
-[SBFluidSwitcherSpaceOverlayAccessoryView setDrawsFooter:];
-[SBFluidSwitcherSpaceOverlayAccessoryView setDrawsFocusIndicator:];
-[SBFluidSwitcherSpaceOverlayAccessoryView initWithDelegate:];
-[SBFluidSwitcherSpaceOverlayAccessoryView itemContainerFooterView:didSelectTitleItem:];
-[SBFluidSwitcherSpaceOverlayAccessoryView dealloc];
-[SBFluidSwitcherSpaceOverlayAccessoryView configureOverlayForAppLayout:iconZoomWithView:crossfadeViews:];
-[SBFluidSwitcherSpaceOverlayAccessoryView setIconOpacity:];
-[SBFluidSwitcherSpaceOverlayAccessoryView _inverseContentScale];
-[SBFluidSwitcherSpaceOverlayAccessoryView layoutSubviews];
-[SBFluidSwitcherSpaceOverlayAccessoryView hitTest:withEvent:];
-[SBFluidSwitcherSpaceOverlayAccessoryView maskedCorners];
-[SBFluidSwitcherSpaceOverlayAccessoryView _updateFocusIndicator];
-[SBFluidSwitcherSpaceOverlayAccessoryView setCornerRadius:];
-[SBFluidSwitcherSpaceOverlayAccessoryView setMaskedCorners:];
-[SBFluidSwitcherSpaceOverlayAccessoryView setShelfViewController:];
-[SBFluidSwitcherSpaceOverlayAccessoryView prepareForReuse];
-[SBFluidSwitcherSpaceOverlayAccessoryView cornerRadius];
-[SBFluidSwitcherSpaceOverlayAccessoryView setContentScale:];
-[SBFluidSwitcherSpaceOverlayAccessoryView contentScale];
-[SBFluidSwitcherSpaceOverlayAccessoryView delegate];
-[SBFluidSwitcherSpaceOverlayAccessoryView removeIconOverlay];
-[SBFluidSwitcherSpaceOverlayAccessoryView appLayoutForIconOverlay];
-[SBFluidSwitcherSpaceOverlayAccessoryView setStrongPairIndicatorView:];
-[SBFluidSwitcherSpaceOverlayAccessoryView _updateFooterAnimated:];
-[SBFluidSwitcherSpaceOverlayAccessoryView pointInside:withEvent:];
-[SBFluidSwitcherSpaceOverlayAccessoryView _updateContentViewLayout];
-[SBFluidSwitcherSpaceOverlayAccessoryView _configureDebugBorder];
-[SBFluidSwitcherSpaceOverlayAccessoryView strongPairIndicatorView];
-[SBFluidSwitcherSpaceOverlayAccessoryView setTitleAndIconOpacity:];
-[SBFluidSwitcherSpaceOverlayAccessoryView shelfViewController];
```
