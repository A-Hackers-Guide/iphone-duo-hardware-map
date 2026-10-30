# `TPPillView`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPControl`
- 12 instance variables, 14 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"<TPPillViewDelegate>" _delegate;
@"NSString" _badgeSymbolName;
Q _theme;
@"TPBadgeView" _badgeView;
@"UIImageView" _badgeImageView;
@"UIStackView" _stackView;
@"UILabel" _textLabel;
@"UITapGestureRecognizer" _gestureRecognizer;
@"NSLayoutConstraint" _stackViewBottomAnchorLayoutConstraint;
@"NSLayoutConstraint" _stackViewLeftAnchorLayoutConstraint;
@"NSLayoutConstraint" _stackViewRightAnchorLayoutConstraint;
@"NSLayoutConstraint" _stackViewTopAnchorLayoutConstraint;
```

## Properties

```
@property (T@"TPBadgeView",R,N,V_badgeView) badgeView;
@property (T@"UIImageView",R,N,V_badgeImageView) badgeImageView;
@property (T@"UIStackView",R,N,V_stackView) stackView;
@property (T@"UILabel",R,N,V_textLabel) textLabel;
@property (T@"UITapGestureRecognizer",R,N,V_gestureRecognizer) gestureRecognizer;
@property (T@"NSLayoutConstraint",&,N,V_stackViewBottomAnchorLayoutConstraint) stackViewBottomAnchorLayoutConstraint;
@property (T@"NSLayoutConstraint",&,N,V_stackViewLeftAnchorLayoutConstraint) stackViewLeftAnchorLayoutConstraint;
@property (T@"NSLayoutConstraint",&,N,V_stackViewRightAnchorLayoutConstraint) stackViewRightAnchorLayoutConstraint;
@property (T@"NSLayoutConstraint",&,N,V_stackViewTopAnchorLayoutConstraint) stackViewTopAnchorLayoutConstraint;
@property (T@"<TPPillViewDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",C,N,V_badgeSymbolName) badgeSymbolName;
@property (T@"NSString",C,N) badgeText;
@property (T@"NSString",C,N) title;
@property (TQ,N,V_theme) theme;
```

## Instance methods

```
-[TPPillView _controlEventsForActionTriggered];
-[TPPillView commonInit];
-[TPPillView theme];
-[TPPillView badgeText];
-[TPPillView updateTheme];
-[TPPillView contextMenuInteraction:configurationForMenuAtLocation:];
-[TPPillView gestureRecognizer];
-[TPPillView badgeView];
-[TPPillView textLabel];
-[TPPillView badgeImageView];
-[TPPillView setBadgeText:];
-[TPPillView handleTap:];
-[TPPillView setDelegate:];
-[TPPillView title];
-[TPPillView loadConstraints];
-[TPPillView delegate];
-[TPPillView updateFonts];
-[TPPillView stackView];
-[TPPillView setTitle:];
-[TPPillView setTheme:];
-[TPPillView unloadConstraints];
-[TPPillView badgeSymbolName];
-[TPPillView initWithTitle:frame:];
-[TPPillView initWithTitle:frame:theme:];
-[TPPillView setBadgeSymbolName:];
-[TPPillView setStackViewBottomAnchorLayoutConstraint:];
-[TPPillView setStackViewLeftAnchorLayoutConstraint:];
-[TPPillView setStackViewRightAnchorLayoutConstraint:];
-[TPPillView setStackViewTopAnchorLayoutConstraint:];
-[TPPillView stackViewBottomAnchorLayoutConstraint];
-[TPPillView stackViewLeftAnchorLayoutConstraint];
-[TPPillView stackViewRightAnchorLayoutConstraint];
-[TPPillView stackViewTopAnchorLayoutConstraint];
```
