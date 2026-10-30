# `SBLogoutProgressView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 16 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"CNContact" _userContact;
@"NSArray" _pendingApplications;
@"_UILegibilitySettings" _legibilitySettings;
@"UIImageView" _userAvatarView;
@"NSLayoutConstraint" _userAvatarVerticalConstraint;
@"UILabel" _goodbyeLabel;
@"NSLayoutConstraint" _goodbyeLabelConstraint;
@"UIView" _savingDocumentsActivityAndLabelContainerView;
@"UIActivityIndicatorView" _savingDocumentsActivityIndicator;
@"UILabel" _savingDocumentsLabel;
@"UILabel" _savingDocumentsMoreLabel;
@"NSLayoutConstraint" _savingDocumentsMoreLabelConstraint;
@"UIView" _blameContainerView;
@"UIImageView" _blameAppIconView;
@"UILabel" _blameAppNameLabel;
@"SBWindowSceneStatusBarSettingsAssertion" _statusBarSettingsAssertion;
```

## Properties

```
@property (T@"CNContact",&,N,V_userContact) userContact;
@property (T@"NSArray",C,N,V_pendingApplications) pendingApplications;
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
@property (TB,D,N,GisProgressVisible) progressVisible;
```

## Instance methods

```
-[SBLogoutProgressView _updateLegibility];
-[SBLogoutProgressView legibilitySettings];
-[SBLogoutProgressView updateConstraints];
-[SBLogoutProgressView setLegibilitySettings:];
-[SBLogoutProgressView initWithFrame:];
-[SBLogoutProgressView isProgressVisible];
-[SBLogoutProgressView userContact];
-[SBLogoutProgressView _updateViewData];
-[SBLogoutProgressView setUserContact:];
-[SBLogoutProgressView _goodbyeLabelBaselineOffset];
-[SBLogoutProgressView _moreDocumentsLabelBaselineOffset];
-[SBLogoutProgressView _updateBlame];
-[SBLogoutProgressView _updateGoodbye];
-[SBLogoutProgressView _updateUserAvatar];
-[SBLogoutProgressView _updateUserAvatarLegibility];
-[SBLogoutProgressView _userAvatarVerticalOffsetFromCenter];
-[SBLogoutProgressView pendingApplications];
-[SBLogoutProgressView setPendingApplications:];
-[SBLogoutProgressView setProgressVisible:];
```
