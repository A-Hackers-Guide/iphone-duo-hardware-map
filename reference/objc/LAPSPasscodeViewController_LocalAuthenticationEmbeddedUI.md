# `LAPSPasscodeViewController`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LAPSPasscodeViewControllerBase`
- 10 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _isNextButtonEnabled;
@"UILabel" _headerLabel;
@"UILabel" _subHeaderLabel;
@"UILabel" _footerLabel;
@"UILabel" _errorCapsule;
@"UIView" _errorCapsuleContainer;
@"UIScrollView" _scrollView;
@"LACUIPasscodeField" _passcodeFieldVC;
@"UIButton" _optionsButton;
@"LACUIKeyboardLayoutGuide" _customKeyboardGuide;
```

## Instance methods

```
-[LAPSPasscodeViewController setup];
-[LAPSPasscodeViewController willMoveToParentViewController:];
-[LAPSPasscodeViewController viewDidLayoutSubviews];
-[LAPSPasscodeViewController viewDidAppear:];
-[LAPSPasscodeViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[LAPSPasscodeViewController setErrorMessage:];
-[LAPSPasscodeViewController setupNavigationItem];
-[LAPSPasscodeViewController _shouldUseStandardKeyboardGuide];
-[LAPSPasscodeViewController _bodyStackHorizontalPadding];
-[LAPSPasscodeViewController _bodyStackSpacing];
-[LAPSPasscodeViewController _handleCancel:];
-[LAPSPasscodeViewController _handleNext:];
-[LAPSPasscodeViewController _mainStackHorizontalPadding];
-[LAPSPasscodeViewController _mainStackInsets];
-[LAPSPasscodeViewController _mainStackSpacing];
-[LAPSPasscodeViewController _scrollTo:];
-[LAPSPasscodeViewController _scrollToPasscodeField];
-[LAPSPasscodeViewController _shouldShowNextButton];
-[LAPSPasscodeViewController _showPasscodeOptions:];
-[LAPSPasscodeViewController _widthMultiplier];
-[LAPSPasscodeViewController updateLayoutAfterPasscodeLengthChangeIfNeeded:];
```
