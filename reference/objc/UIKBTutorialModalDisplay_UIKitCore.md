# `UIKBTutorialModalDisplay`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 22 properties, 49 instance methods, 0 class methods

## Instance variables

```
B _didConfigureBackgroundBlur;
q _appearance;
@"UIView" _containerView;
@"UIView" _mediaView;
@"UIButton" _button;
@"UIKBTutorialModalDisplayStyling" _styling;
@"UIVisualEffectView" _backgroundBlurView;
@"NSArray" _compactConstraints;
@"NSArray" _wideConstraints;
@"NSArray" _sharedConstraints;
```

## Properties

```
@property (T@"UIKBTutorialModalDisplayStyling",&,N,V_styling) styling;
@property (T@"UIVisualEffectView",&,N,V_backgroundBlurView) backgroundBlurView;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"UIView",&,N,V_mediaView) mediaView;
@property (T@"UIButton",&,N,V_button) button;
@property (T@"NSArray",&,N,V_compactConstraints) compactConstraints;
@property (T@"NSArray",&,N,V_wideConstraints) wideConstraints;
@property (T@"NSArray",&,N,V_sharedConstraints) sharedConstraints;
@property (TB,N,V_didConfigureBackgroundBlur) didConfigureBackgroundBlur;
@property (Tq,N,V_appearance) appearance;
@property (T@"NSString",R,N) buttonTitle;
@property (T@"NSArray",R,N) textTitleDescriptions;
@property (T@"UIFont",R,N) textTitleFont;
@property (T@"NSArray",R,N) textBodyDescriptions;
@property (T@"UIFont",R,N) textBodyFont;
@property (T@"NSString",R,N) largeTitle;
@property (T@"UIFont",R,N) largeTitleFont;
@property (T@"NSArray",R,N) mediaContents;
@property (Td,R,N) pagingInterval;
@property (Td,R,N) mediaLayoutWidthAdjustment;
@property (Tq,R,N) textBodyMaxLines;
@property (TB,R,N) presentsFullScreen;
```

## Instance methods

```
-[UIKBTutorialModalDisplay isPortrait];
-[UIKBTutorialModalDisplay backgroundBlurView];
-[UIKBTutorialModalDisplay setContainerView:];
-[UIKBTutorialModalDisplay safeAreaInsets];
-[UIKBTutorialModalDisplay setAppearance:];
-[UIKBTutorialModalDisplay setButton:];
-[UIKBTutorialModalDisplay button];
-[UIKBTutorialModalDisplay layoutSubviews];
-[UIKBTutorialModalDisplay containerView];
-[UIKBTutorialModalDisplay mediaView];
-[UIKBTutorialModalDisplay setBackgroundBlurView:];
-[UIKBTutorialModalDisplay appearance];
-[UIKBTutorialModalDisplay styling];
-[UIKBTutorialModalDisplay setStyling:];
-[UIKBTutorialModalDisplay updateMediaViewTextAndPlacement];
-[UIKBTutorialModalDisplay wideConstraints];
-[UIKBTutorialModalDisplay buttonTitle];
-[UIKBTutorialModalDisplay compactConstraints];
-[UIKBTutorialModalDisplay configBackgroundBlur];
-[UIKBTutorialModalDisplay configContainerView];
-[UIKBTutorialModalDisplay constructMediaView];
-[UIKBTutorialModalDisplay containerBottomPadding];
-[UIKBTutorialModalDisplay containerForAlertPresentation];
-[UIKBTutorialModalDisplay containerForFullScreenView];
-[UIKBTutorialModalDisplay containerForKeyboardView];
-[UIKBTutorialModalDisplay containerTopPadding];
-[UIKBTutorialModalDisplay didConfigureBackgroundBlur];
-[UIKBTutorialModalDisplay extraButtonTapAction];
-[UIKBTutorialModalDisplay initWithKeyboardAppearance:];
-[UIKBTutorialModalDisplay largeTitle];
-[UIKBTutorialModalDisplay largeTitleFont];
-[UIKBTutorialModalDisplay mediaContents];
-[UIKBTutorialModalDisplay mediaLayoutWidthAdjustment];
-[UIKBTutorialModalDisplay pagingInterval];
-[UIKBTutorialModalDisplay presentsFullScreen];
-[UIKBTutorialModalDisplay restartPagingAnimation];
-[UIKBTutorialModalDisplay setCompactConstraints:];
-[UIKBTutorialModalDisplay setDidConfigureBackgroundBlur:];
-[UIKBTutorialModalDisplay setMediaView:];
-[UIKBTutorialModalDisplay setSharedConstraints:];
-[UIKBTutorialModalDisplay setWideConstraints:];
-[UIKBTutorialModalDisplay sharedConstraints];
-[UIKBTutorialModalDisplay sizeForTutorialPageView];
-[UIKBTutorialModalDisplay tapInsideButton:];
-[UIKBTutorialModalDisplay textBodyDescriptions];
-[UIKBTutorialModalDisplay textBodyFont];
-[UIKBTutorialModalDisplay textBodyMaxLines];
-[UIKBTutorialModalDisplay textTitleDescriptions];
-[UIKBTutorialModalDisplay textTitleFont];
```
