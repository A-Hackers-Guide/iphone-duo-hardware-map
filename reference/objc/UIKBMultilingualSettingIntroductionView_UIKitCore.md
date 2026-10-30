# `UIKBMultilingualSettingIntroductionView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBMultilingualIntroductionView`
- 7 instance variables, 7 properties, 20 instance methods, 4 class methods

## Instance variables

```
@"UIKeyboardInputMode" _inputMode;
@"_UIBackdropView" _backdropView;
@"UILabel" _titleLabel;
@"UILabel" _descriptionLabel;
@"UIButton" _settingButton;
@"UIButton" _continueButton;
@"UIView" _artworkView;
```

## Properties

```
@property (T@"UIKeyboardInputMode",&,N,V_inputMode) inputMode;
@property (T@"_UIBackdropView",&,N,V_backdropView) backdropView;
@property (T@"UILabel",&,N,V_titleLabel) titleLabel;
@property (T@"UILabel",&,N,V_descriptionLabel) descriptionLabel;
@property (T@"UIButton",&,N,V_settingButton) settingButton;
@property (T@"UIButton",&,N,V_continueButton) continueButton;
@property (T@"UIView",&,N,V_artworkView) artworkView;
```

## Class methods

```
+[UIKBMultilingualSettingIntroductionView displayArtwork:];
+[UIKBMultilingualSettingIntroductionView displayDescription:];
+[UIKBMultilingualSettingIntroductionView displayTitle:];
+[UIKBMultilingualSettingIntroductionView shouldShowIntroductionForInputMode:];
```

## Instance methods

```
-[UIKBMultilingualSettingIntroductionView setDescriptionLabel:];
-[UIKBMultilingualSettingIntroductionView setBackdropView:];
-[UIKBMultilingualSettingIntroductionView artworkView];
-[UIKBMultilingualSettingIntroductionView descriptionLabel];
-[UIKBMultilingualSettingIntroductionView setInputMode:];
-[UIKBMultilingualSettingIntroductionView backdropView];
-[UIKBMultilingualSettingIntroductionView inputMode];
-[UIKBMultilingualSettingIntroductionView setTitleLabel:];
-[UIKBMultilingualSettingIntroductionView titleLabel];
-[UIKBMultilingualSettingIntroductionView layoutSubviews];
-[UIKBMultilingualSettingIntroductionView setArtworkView:];
-[UIKBMultilingualSettingIntroductionView _updateContainer];
-[UIKBMultilingualSettingIntroductionView backdropStyleForRenderConfig:];
-[UIKBMultilingualSettingIntroductionView continueButton];
-[UIKBMultilingualSettingIntroductionView continueButtonTapped];
-[UIKBMultilingualSettingIntroductionView initWithInputMode:frame:];
-[UIKBMultilingualSettingIntroductionView setContinueButton:];
-[UIKBMultilingualSettingIntroductionView setSettingButton:];
-[UIKBMultilingualSettingIntroductionView settingButton];
-[UIKBMultilingualSettingIntroductionView settingButtonTapped];
```
