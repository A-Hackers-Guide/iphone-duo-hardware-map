# `_UINavigationBarTitleView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UINavigationBarAugmentedTitleView`
- 20 instance variables, 48 properties, 80 instance methods, 0 class methods

## Instance variables

```
@"_UINavigationBarTitleViewOverlayRects" _overlayRects;
@"<_UINavigationBarTitleViewDataSource>" _dataSource;
B _underlayBarContent;
B _hideBackButton;
B _hideLeadingBarButtons;
B _hideStandardTitle;
B _hideCenterBarButtons;
B _hideTrailingBarButtons;
B _heightShouldBeIncreasedByTabBarHeight;
B _disallowNavigationBarMinimumTopPadding;
@"UINavigationItem" _navigationItem;
q _titleLocation;
d _height;
d _heightExtension;
d _backButtonMaximumWidth;
d _backButtonAlpha;
d _leadingBarAlpha;
d _trailingBarAlpha;
q _preferredContentAlignment;
q _displayLayer;
```

## Properties

```
@property (T@"UINavigationItem",R,W,N,V_navigationItem) navigationItem;
@property (Tq,R,N,V_titleLocation) titleLocation;
@property (TB,N,V_underlayBarContent) underlayBarContent;
@property (Td,N,V_height) height;
@property (Td,N,V_heightExtension) heightExtension;
@property (Td,N,V_backButtonMaximumWidth) backButtonMaximumWidth;
@property (TB,N,V_hideBackButton) hideBackButton;
@property (TB,N,V_hideLeadingBarButtons) hideLeadingBarButtons;
@property (TB,N,V_hideStandardTitle) hideStandardTitle;
@property (TB,N,V_hideCenterBarButtons) hideCenterBarButtons;
@property (TB,N,V_hideTrailingBarButtons) hideTrailingBarButtons;
@property (Td,N,V_backButtonAlpha) backButtonAlpha;
@property (Td,N,V_leadingBarAlpha) leadingBarAlpha;
@property (Td,N,V_trailingBarAlpha) trailingBarAlpha;
@property (T@"_UINavigationBarTitleViewOverlayRects",R,N) overlays;
@property (T@"NSArray",R,C,N) contentOverlayRects;
@property (Tq,R,N) leadingOverlayCount;
@property (Tq,R,N) trailingOverlayCount;
@property (Td,R,N) largeTitleHeight;
@property (Td,R,N) floatingTabBarHeight;
@property (TB,N,V_heightShouldBeIncreasedByTabBarHeight) heightShouldBeIncreasedByTabBarHeight;
@property (T{?=dd},R,N) largeTitleHeightRange;
@property (Td,R,N) contentBaselineOffsetFromTop;
@property (Td,R,N) contentBaseHeight;
@property (Tq,N,V_preferredContentAlignment) preferredContentAlignment;
@property (T@"UIMenu",R,C,N) backButtonMenu;
@property (Tq,N,V_displayLayer) displayLayer;
@property (TB,N,V_disallowNavigationBarMinimumTopPadding) disallowNavigationBarMinimumTopPadding;
@property (TB,R,N) _navigationBarHeightShouldBeIncreasedByTabBarHeight;
@property (T@"NSArray",R,C,N) _navigationBarContentOverlayRects;
@property (Td,R,N) _navigationBarContentHeight;
@property (Td,R,N) _navigationBarContentHeightExtension;
@property (Td,R,N) _navigationBarBackButtonMaximumWidth;
@property (TB,R,N) _hideNavigationBarBackButton;
@property (TB,R,N) _hideNavigationBarLeadingBarButtons;
@property (TB,R,N) _hideNavigationBarStandardTitle;
@property (TB,R,N) _hideNavigationBarCenterBarButtons;
@property (TB,R,N) _hideNavigationBarTrailingBarButtons;
@property (Td,R,N) _navigationBarBackButtonAlpha;
@property (Td,R,N) _navigationBarLeadingBarButtonsAlpha;
@property (Td,R,N) _navigationBarTrailingBarButtonsAlpha;
@property (Tq,R,N) _preferredAlignment;
@property (Tq,R,N) _displayLayer;
@property (TB,R,N) _disallowNavigationBarMinimumTopPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINavigationBarTitleView contentDidChange];
-[_UINavigationBarTitleView hitTest:withEvent:];
-[_UINavigationBarTitleView largeTitleHeight];
-[_UINavigationBarTitleView largeTitleHeightRange];
-[_UINavigationBarTitleView performTransition:willBeDisplayed:];
-[_UINavigationBarTitleView overlays];
-[_UINavigationBarTitleView setHeight:];
-[_UINavigationBarTitleView preferredContentSizeForSize:];
-[_UINavigationBarTitleView titleLocation];
-[_UINavigationBarTitleView description];
-[_UINavigationBarTitleView navigationItem];
-[_UINavigationBarTitleView initWithCoder:];
-[_UINavigationBarTitleView initWithFrame:];
-[_UINavigationBarTitleView height];
-[_UINavigationBarTitleView _displayLayer];
-[_UINavigationBarTitleView setBackButtonMaximumWidth:];
-[_UINavigationBarTitleView backButtonMaximumWidth];
-[_UINavigationBarTitleView _hideNavigationBarStandardTitle];
-[_UINavigationBarTitleView leadingBarAlpha];
-[_UINavigationBarTitleView backButtonAlpha];
-[_UINavigationBarTitleView heightExtension];
-[_UINavigationBarTitleView _contentDidChange];
-[_UINavigationBarTitleView _disallowNavigationBarMinimumTopPadding];
-[_UINavigationBarTitleView _hideNavigationBarBackButton];
-[_UINavigationBarTitleView _hideNavigationBarCenterBarButtons];
-[_UINavigationBarTitleView _hideNavigationBarLeadingBarButtons];
-[_UINavigationBarTitleView _hideNavigationBarTrailingBarButtons];
-[_UINavigationBarTitleView _navigationBarBackButtonAlpha];
-[_UINavigationBarTitleView _navigationBarBackButtonMaximumWidth];
-[_UINavigationBarTitleView _navigationBarContentHeight];
-[_UINavigationBarTitleView _navigationBarContentHeightExtension];
-[_UINavigationBarTitleView _navigationBarContentOverlayRects];
-[_UINavigationBarTitleView _navigationBarHeightShouldBeIncreasedByTabBarHeight];
-[_UINavigationBarTitleView _navigationBarLeadingBarButtonsAlpha];
-[_UINavigationBarTitleView _navigationBarTrailingBarButtonsAlpha];
-[_UINavigationBarTitleView _navigationBarTraitCollectionDidChangeTo:from:];
-[_UINavigationBarTitleView _navigationBarTransitionCompleted:willBeDisplayed:];
-[_UINavigationBarTitleView _navigationBarTransitionWillBegin:willBeDisplayed:];
-[_UINavigationBarTitleView _performNavigationBarTransition:willBeDisplayed:];
-[_UINavigationBarTitleView _preferredAlignment];
-[_UINavigationBarTitleView _preferredContentSizeForSize:];
-[_UINavigationBarTitleView _setDataSource:navigationItem:titleLocation:];
-[_UINavigationBarTitleView _traitCollectionOverridesForNavigationBarTraitCollection:];
-[_UINavigationBarTitleView _wantsTwoPartTransition];
-[_UINavigationBarTitleView backButtonMenu];
-[_UINavigationBarTitleView contentBaseHeight];
-[_UINavigationBarTitleView contentBaselineOffsetFromTop];
-[_UINavigationBarTitleView contentOverlayRects];
-[_UINavigationBarTitleView disallowNavigationBarMinimumTopPadding];
-[_UINavigationBarTitleView displayLayer];
-[_UINavigationBarTitleView floatingTabBarHeight];
-[_UINavigationBarTitleView heightShouldBeIncreasedByTabBarHeight];
-[_UINavigationBarTitleView hideBackButton];
-[_UINavigationBarTitleView hideCenterBarButtons];
-[_UINavigationBarTitleView hideLeadingBarButtons];
-[_UINavigationBarTitleView hideStandardTitle];
-[_UINavigationBarTitleView hideTrailingBarButtons];
-[_UINavigationBarTitleView leadingOverlayCount];
-[_UINavigationBarTitleView navigationBarTraitCollectionDidChangeTo:from:];
-[_UINavigationBarTitleView preferredContentAlignment];
-[_UINavigationBarTitleView preferredContentSizeDidChange];
-[_UINavigationBarTitleView setBackButtonAlpha:];
-[_UINavigationBarTitleView setDisallowNavigationBarMinimumTopPadding:];
-[_UINavigationBarTitleView setDisplayLayer:];
-[_UINavigationBarTitleView setHeightExtension:];
-[_UINavigationBarTitleView setHeightShouldBeIncreasedByTabBarHeight:];
-[_UINavigationBarTitleView setHideBackButton:];
-[_UINavigationBarTitleView setHideCenterBarButtons:];
-[_UINavigationBarTitleView setHideLeadingBarButtons:];
-[_UINavigationBarTitleView setHideStandardTitle:];
-[_UINavigationBarTitleView setHideTrailingBarButtons:];
-[_UINavigationBarTitleView setLeadingBarAlpha:];
-[_UINavigationBarTitleView setPreferredContentAlignment:];
-[_UINavigationBarTitleView setTrailingBarAlpha:];
-[_UINavigationBarTitleView setUnderlayBarContent:];
-[_UINavigationBarTitleView trailingBarAlpha];
-[_UINavigationBarTitleView trailingOverlayCount];
-[_UINavigationBarTitleView transitionCompleted:willBeDisplayed:];
-[_UINavigationBarTitleView transitionWillBegin:willBeDisplayed:];
-[_UINavigationBarTitleView underlayBarContent];
```
