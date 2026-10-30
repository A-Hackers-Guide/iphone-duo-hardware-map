# `UIKBMultilingualKeyboardIntroductionView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBMultilingualIntroductionView`
- 15 instance variables, 15 properties, 39 instance methods, 4 class methods

## Instance variables

```
B _laidOutForPortrait;
@"UIKeyboardInputMode" _inputMode;
@"_UIBackdropView" _backdropView;
@"UILabel" _titleLabel;
@"UILabel" _descriptionLabel;
@"UIButton" _continueButton;
@"NSArray" _contentConstraints;
@"NSArray" _containerConstraints;
@"NSLayoutAnchor" _containerTopReference;
@"UIView" _containerReferenceView;
@"UIKBMultilingualIntroductionArrowView" _arrowView;
@"UIView" _highlight;
@"UIMultiscriptCandidateView" _multiscriptCandidateView;
@"UIView" _artworkView;
@"TUIPredictionView" _predictionView;
```

## Properties

```
@property (T@"UIKeyboardInputMode",&,N,V_inputMode) inputMode;
@property (T@"_UIBackdropView",&,N,V_backdropView) backdropView;
@property (T@"UILabel",&,N,V_titleLabel) titleLabel;
@property (T@"UILabel",&,N,V_descriptionLabel) descriptionLabel;
@property (T@"UIButton",&,N,V_continueButton) continueButton;
@property (T@"NSArray",&,N,V_contentConstraints) contentConstraints;
@property (T@"NSArray",&,N,V_containerConstraints) containerConstraints;
@property (T@"NSLayoutAnchor",W,N,V_containerTopReference) containerTopReference;
@property (T@"UIView",W,N,V_containerReferenceView) containerReferenceView;
@property (TB,N,V_laidOutForPortrait) laidOutForPortrait;
@property (T@"UIKBMultilingualIntroductionArrowView",&,N,V_arrowView) arrowView;
@property (T@"UIView",&,N,V_highlight) highlight;
@property (T@"UIMultiscriptCandidateView",&,N,V_multiscriptCandidateView) multiscriptCandidateView;
@property (T@"UIView",&,N,V_artworkView) artworkView;
@property (T@"TUIPredictionView",&,N,V_predictionView) predictionView;
```

## Class methods

```
+[UIKBMultilingualKeyboardIntroductionView displayArtwork:];
+[UIKBMultilingualKeyboardIntroductionView displayDescription:];
+[UIKBMultilingualKeyboardIntroductionView displayTitle:];
+[UIKBMultilingualKeyboardIntroductionView shouldShowIntroductionForInputMode:];
```

## Instance methods

```
-[UIKBMultilingualKeyboardIntroductionView setDescriptionLabel:];
-[UIKBMultilingualKeyboardIntroductionView setBackdropView:];
-[UIKBMultilingualKeyboardIntroductionView artworkView];
-[UIKBMultilingualKeyboardIntroductionView descriptionLabel];
-[UIKBMultilingualKeyboardIntroductionView setInputMode:];
-[UIKBMultilingualKeyboardIntroductionView backdropView];
-[UIKBMultilingualKeyboardIntroductionView inputMode];
-[UIKBMultilingualKeyboardIntroductionView setTitleLabel:];
-[UIKBMultilingualKeyboardIntroductionView titleLabel];
-[UIKBMultilingualKeyboardIntroductionView layoutSubviews];
-[UIKBMultilingualKeyboardIntroductionView predictionView];
-[UIKBMultilingualKeyboardIntroductionView setHighlight:];
-[UIKBMultilingualKeyboardIntroductionView updateConstraints];
-[UIKBMultilingualKeyboardIntroductionView highlight];
-[UIKBMultilingualKeyboardIntroductionView setArtworkView:];
-[UIKBMultilingualKeyboardIntroductionView _rebuildContentConstraints];
-[UIKBMultilingualKeyboardIntroductionView _updateContainer];
-[UIKBMultilingualKeyboardIntroductionView _updatePath];
-[UIKBMultilingualKeyboardIntroductionView arrowView];
-[UIKBMultilingualKeyboardIntroductionView backdropStyleForRenderConfig:];
-[UIKBMultilingualKeyboardIntroductionView containerConstraints];
-[UIKBMultilingualKeyboardIntroductionView containerReferenceView];
-[UIKBMultilingualKeyboardIntroductionView containerTopReference];
-[UIKBMultilingualKeyboardIntroductionView contentConstraints];
-[UIKBMultilingualKeyboardIntroductionView continueButton];
-[UIKBMultilingualKeyboardIntroductionView continueButtonTapped];
-[UIKBMultilingualKeyboardIntroductionView initWithInputMode:frame:];
-[UIKBMultilingualKeyboardIntroductionView laidOutForPortrait];
-[UIKBMultilingualKeyboardIntroductionView multiscriptCandidateView];
-[UIKBMultilingualKeyboardIntroductionView setArrowView:];
-[UIKBMultilingualKeyboardIntroductionView setContainerConstraints:];
-[UIKBMultilingualKeyboardIntroductionView setContainerReferenceView:];
-[UIKBMultilingualKeyboardIntroductionView setContainerTopReference:];
-[UIKBMultilingualKeyboardIntroductionView setContentConstraints:];
-[UIKBMultilingualKeyboardIntroductionView setContinueButton:];
-[UIKBMultilingualKeyboardIntroductionView setLaidOutForPortrait:];
-[UIKBMultilingualKeyboardIntroductionView setMultiscriptCandidateView:];
-[UIKBMultilingualKeyboardIntroductionView setPredictionView:];
-[UIKBMultilingualKeyboardIntroductionView textBodyFont];
```
