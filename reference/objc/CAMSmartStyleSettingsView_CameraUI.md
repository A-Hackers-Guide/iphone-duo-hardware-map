# `CAMSmartStyleSettingsView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAMSemanticStylePickerDelegate`, `CAMScrollViewLayoutDelegate`
- 33 instance variables, 42 properties, 115 instance methods, 5 class methods

## Instance variables

```
B __settingDpadValue;
@"<CAMSmartStyleSettingsViewDelegate>" _delegate;
@"CAMScrollViewWithLayoutDelegate" __scrollView;
@"UIButton" __selectAssetsButton;
@"UIButton" __showGridButton;
@"NSArray" __styleClippingContainerViews;
@"CAMSemanticStylePicker" __stylePicker;
@"NSMutableDictionary" __previewViewControllersByStyleIndex;
@"UIPageControl" __previewPageDots;
@"NSMutableArray" __styleNameBadges;
@"PEPhotoStyleDPad" __dpadControl;
@"PEPhotoStyleValuesPlatterView" __styleValuesPlatterView;
@"NSMutableArray" __intensitySliders;
@"NSMutableArray" __styleDescriptionLabels;
@"UILabel" __chooseInstructionLabel;
@"UIImageView" __chooseInstructionArrow;
@"UILabel" __tuneInstructionLabel;
@"UIButton" __confirmButton;
@"UIButton" __customizeButton;
Q __stage;
@"NSArray" __styleTypes;
q _visiblePreviewIndex;
@"NSArray" __styleNames;
@"UIImage" __thumbnailPreviewImage;
@"NSMutableSet" __stageButtonSuppressionReasons;
@"CEKAnimationSequence" __animationSequence;
@"NSLayoutConstraint" __pickerTopConstraintChooseStages;
@"NSLayoutConstraint" __pickerTopConstraintTuneStages;
@"NSMutableArray" __styleBadgeCenterXConstraints;
@"NSMutableArray" __descriptionBottomConstraints;
@"NSLayoutConstraint" __chooseInstructionArrowXConstraint;
@"NSLayoutConstraint" __tuneInstructionLabelBottomConstraint;
@"CAMFeedbackController" __feedbackController;
```

## Properties

```
@property (T@"CAMScrollViewWithLayoutDelegate",R,N,V__scrollView) _scrollView;
@property (T@"UIButton",R,N,V__selectAssetsButton) _selectAssetsButton;
@property (T@"UIButton",R,N,V__showGridButton) _showGridButton;
@property (T@"NSArray",R,N,V__styleClippingContainerViews) _styleClippingContainerViews;
@property (T@"CAMSemanticStylePicker",R,N,V__stylePicker) _stylePicker;
@property (T@"NSMutableDictionary",R,N,V__previewViewControllersByStyleIndex) _previewViewControllersByStyleIndex;
@property (T@"UIPageControl",R,N,V__previewPageDots) _previewPageDots;
@property (T@"NSMutableArray",R,N,V__styleNameBadges) _styleNameBadges;
@property (T@"PEPhotoStyleDPad",R,N,V__dpadControl) _dpadControl;
@property (T@"PEPhotoStyleValuesPlatterView",R,N,V__styleValuesPlatterView) _styleValuesPlatterView;
@property (T@"NSMutableArray",R,N,V__intensitySliders) _intensitySliders;
@property (T@"NSMutableArray",R,N,V__styleDescriptionLabels) _styleDescriptionLabels;
@property (T@"UILabel",R,N,V__chooseInstructionLabel) _chooseInstructionLabel;
@property (T@"UIImageView",R,N,V__chooseInstructionArrow) _chooseInstructionArrow;
@property (T@"UILabel",R,N,V__tuneInstructionLabel) _tuneInstructionLabel;
@property (T@"UIButton",R,N,V__confirmButton) _confirmButton;
@property (T@"UIButton",R,N,V__customizeButton) _customizeButton;
@property (TQ,N,S_setStage:,V__stage) _stage;
@property (TB,N,S_setDidCompleteChooseInstructions:) _didCompleteChooseInstructions;
@property (TB,N,S_setDidCompleteTuneInstructions:) _didCompleteTuneInstructions;
@property (T@"NSArray",R,N,V__styleTypes) _styleTypes;
@property (Tq,R,N) _selectedStylePreset;
@property (T@"CEKSmartStyle",R,N) _selectedStyle;
@property (Tq,R,N,V_visiblePreviewIndex) visiblePreviewIndex;
@property (T@"NSArray",R,N,V__styleNames) _styleNames;
@property (T@"UIImage",R,N,V__thumbnailPreviewImage) _thumbnailPreviewImage;
@property (T@"NSMutableSet",R,N,V__stageButtonSuppressionReasons) _stageButtonSuppressionReasons;
@property (T@"CEKAnimationSequence",&,N,S_setAnimationSequence:,V__animationSequence) _animationSequence;
@property (T@"NSLayoutConstraint",R,N,V__pickerTopConstraintChooseStages) _pickerTopConstraintChooseStages;
@property (T@"NSLayoutConstraint",R,N,V__pickerTopConstraintTuneStages) _pickerTopConstraintTuneStages;
@property (T@"NSMutableArray",R,N,V__styleBadgeCenterXConstraints) _styleBadgeCenterXConstraints;
@property (T@"NSMutableArray",R,N,V__descriptionBottomConstraints) _descriptionBottomConstraints;
@property (T@"NSLayoutConstraint",R,N,V__chooseInstructionArrowXConstraint) _chooseInstructionArrowXConstraint;
@property (T@"NSLayoutConstraint",R,N,V__tuneInstructionLabelBottomConstraint) _tuneInstructionLabelBottomConstraint;
@property (T@"CAMFeedbackController",R,N,V__feedbackController) _feedbackController;
@property (TB,N,G_isSettingDpadValue,S_settingDpadValue:,V__settingDpadValue) _settingDpadValue;
@property (T@"<CAMSmartStyleSettingsViewDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N) scrollEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMSmartStyleSettingsView _descriptionForStylePreset:];
+[CAMSmartStyleSettingsView _updateButtonConfiguration:];
+[CAMSmartStyleSettingsView confirmButtonConfiguration];
+[CAMSmartStyleSettingsView dpadWidthRatio];
+[CAMSmartStyleSettingsView showAssetsButtonConfiguration];
```

## Instance methods

```
-[CAMSmartStyleSettingsView _feedbackController];
-[CAMSmartStyleSettingsView speedUpFadeInAnimations];
-[CAMSmartStyleSettingsView _scrollView];
-[CAMSmartStyleSettingsView didMoveToWindow];
-[CAMSmartStyleSettingsView layoutSubviews];
-[CAMSmartStyleSettingsView setScrollEnabled:];
-[CAMSmartStyleSettingsView _addConstraints];
-[CAMSmartStyleSettingsView delegate];
-[CAMSmartStyleSettingsView semanticStylePickerDidChangeSelectedStyle:];
-[CAMSmartStyleSettingsView semanticStylePickerDidScroll:];
-[CAMSmartStyleSettingsView scrollEnabled];
-[CAMSmartStyleSettingsView _stage];
-[CAMSmartStyleSettingsView flashScrollIndicators];
-[CAMSmartStyleSettingsView _setStage:];
-[CAMSmartStyleSettingsView _handlePageControlValueChanged:];
-[CAMSmartStyleSettingsView _performHaptics];
-[CAMSmartStyleSettingsView _showGridButton];
-[CAMSmartStyleSettingsView _prepareHaptics];
-[CAMSmartStyleSettingsView _advanceToTuneStageIfPossible];
-[CAMSmartStyleSettingsView _animationSequence];
-[CAMSmartStyleSettingsView _assetButtonConfiguration];
-[CAMSmartStyleSettingsView _beginAssetSelection:];
-[CAMSmartStyleSettingsView _centerSquareOfImage:appliesScale:];
-[CAMSmartStyleSettingsView _chooseInstructionArrow];
-[CAMSmartStyleSettingsView _chooseInstructionArrowXConstraint];
-[CAMSmartStyleSettingsView _chooseInstructionLabel];
-[CAMSmartStyleSettingsView _chooseInstructionText];
-[CAMSmartStyleSettingsView _confirmButton];
-[CAMSmartStyleSettingsView _confirmButtonTitle];
-[CAMSmartStyleSettingsView _createNeededStylePages];
-[CAMSmartStyleSettingsView _customizeButton];
-[CAMSmartStyleSettingsView _debugStringForStage:];
-[CAMSmartStyleSettingsView _descriptionBottomConstraints];
-[CAMSmartStyleSettingsView _desiredCarouselRatio];
-[CAMSmartStyleSettingsView _didCompleteChooseInstructions];
-[CAMSmartStyleSettingsView _didCompleteTuneInstructions];
-[CAMSmartStyleSettingsView _dpadControl];
-[CAMSmartStyleSettingsView _dpadControlUpdated:];
-[CAMSmartStyleSettingsView _firstNeededTuneStage];
-[CAMSmartStyleSettingsView _fontWithTextStyle:];
-[CAMSmartStyleSettingsView _fontWithTextStyle:traits:];
-[CAMSmartStyleSettingsView _handleConfirmButton:];
-[CAMSmartStyleSettingsView _handleCustomizeButton:];
-[CAMSmartStyleSettingsView _handlePageControlTouchDown:];
-[CAMSmartStyleSettingsView _handleShowGridButton:];
-[CAMSmartStyleSettingsView _handleStylePickerTap:];
-[CAMSmartStyleSettingsView _intensitySliders];
-[CAMSmartStyleSettingsView _isBlockingStageButtons];
-[CAMSmartStyleSettingsView _isSettingDpadValue];
-[CAMSmartStyleSettingsView _layoutMaskedViews];
-[CAMSmartStyleSettingsView _moveToNextStageIfAllowedAnimated:];
-[CAMSmartStyleSettingsView _newInstructionLabel];
-[CAMSmartStyleSettingsView _newSecondaryButton];
-[CAMSmartStyleSettingsView _pickerTopConstraintChooseStages];
-[CAMSmartStyleSettingsView _pickerTopConstraintTuneStages];
-[CAMSmartStyleSettingsView _playArrowAnimation];
-[CAMSmartStyleSettingsView _playChooseInstructionAnimations];
-[CAMSmartStyleSettingsView _playTuneInstructionAnimations];
-[CAMSmartStyleSettingsView _previewIndexFromPageDots];
-[CAMSmartStyleSettingsView _previewPageDots];
-[CAMSmartStyleSettingsView _previewViewControllersByStyleIndex];
-[CAMSmartStyleSettingsView _readBooleanPreferenceForKey:];
-[CAMSmartStyleSettingsView _resetCurrentSmartStyleToDefaults];
-[CAMSmartStyleSettingsView _resetCurrentStyleToDefaults];
-[CAMSmartStyleSettingsView _secondaryButtonConfiguration];
-[CAMSmartStyleSettingsView _selectAssetsButton];
-[CAMSmartStyleSettingsView _selectedSmartStyleDisplayName];
-[CAMSmartStyleSettingsView _selectedStyle];
-[CAMSmartStyleSettingsView _selectedStyleDescription];
-[CAMSmartStyleSettingsView _selectedStyleDisplayName];
-[CAMSmartStyleSettingsView _selectedStylePreset];
-[CAMSmartStyleSettingsView _setAnimationSequence:];
-[CAMSmartStyleSettingsView _setBooleanPreference:forKey:];
-[CAMSmartStyleSettingsView _setDidCompleteChooseInstructions:];
-[CAMSmartStyleSettingsView _setDidCompleteTuneInstructions:];
-[CAMSmartStyleSettingsView _setPreviewViewControllersExpandedItemIndex:animated:];
-[CAMSmartStyleSettingsView _setStage:animated:];
-[CAMSmartStyleSettingsView _setStageButtonsEnabled:forReason:];
-[CAMSmartStyleSettingsView _setVisiblePreviewIndex:updatePageControl:updateStylePicker:animated:notifyDelegate:];
-[CAMSmartStyleSettingsView _settingDpadValue:];
-[CAMSmartStyleSettingsView _shouldShowStylePlatterViewForCurrentStyle];
-[CAMSmartStyleSettingsView _showGridButtonConfiguration];
-[CAMSmartStyleSettingsView _smartStyleIntensitySliderUpdated];
-[CAMSmartStyleSettingsView _stageButtonSuppressionReasons];
-[CAMSmartStyleSettingsView _stageUpdates];
-[CAMSmartStyleSettingsView _styleBadgeCenterXConstraints];
-[CAMSmartStyleSettingsView _styleClippingContainerViews];
-[CAMSmartStyleSettingsView _styleDescriptionLabels];
-[CAMSmartStyleSettingsView _styleNameBadges];
-[CAMSmartStyleSettingsView _styleNames];
-[CAMSmartStyleSettingsView _stylePicker];
-[CAMSmartStyleSettingsView _styleTypes];
-[CAMSmartStyleSettingsView _styleValuesPlatterView];
-[CAMSmartStyleSettingsView _thumbnailPreviewImage];
-[CAMSmartStyleSettingsView _titleCheckmarkView];
-[CAMSmartStyleSettingsView _titleLabelWithText:];
-[CAMSmartStyleSettingsView _tuneInstructionLabel];
-[CAMSmartStyleSettingsView _tuneInstructionLabelBottomConstraint];
-[CAMSmartStyleSettingsView _tuneInstructionText];
-[CAMSmartStyleSettingsView _updateAlphaForStylePlatterAnimated:];
-[CAMSmartStyleSettingsView _updateConfirmButtonTitle];
-[CAMSmartStyleSettingsView _updateDpadForPresetType:animated:];
-[CAMSmartStyleSettingsView _updateForStageAnimated:scrollToTop:];
-[CAMSmartStyleSettingsView _updatePreviewAdjustmentsUseCurrentUIValues:updateModelValues:];
-[CAMSmartStyleSettingsView _updatePreviewPageDots];
-[CAMSmartStyleSettingsView _updateScrollViewEnablement];
-[CAMSmartStyleSettingsView _updateShowGridButtonAnimated:];
-[CAMSmartStyleSettingsView _updateValuesPlatterWithSmartStyle:];
-[CAMSmartStyleSettingsView _userFacingContentPageNumberForStage:];
-[CAMSmartStyleSettingsView initWithDelegate:stylePresets:selectedIndex:];
-[CAMSmartStyleSettingsView scrollViewDidLayoutSubviews:];
-[CAMSmartStyleSettingsView stopAllAnimations];
-[CAMSmartStyleSettingsView updateImageViews];
-[CAMSmartStyleSettingsView visiblePreviewIndex];
-[CAMSmartStyleSettingsView zoomOutToGridAnimated:];
```
