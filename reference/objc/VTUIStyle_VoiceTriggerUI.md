# `VTUIStyle`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 9 properties, 189 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _deviceStringSuffixes;
@"NSString" _deviceClass;
B _isIpad;
B _isLargeIpad;
B _needMoreLineSpacing;
B _supportsSideButtonActivation;
@"UIFontMetrics" _bodyMetricsForScaling;
@"MGWrapper" _mgWrapper;
@"AFSettingsConnection" _settingsConnection;
@"NSObject<OS_dispatch_queue>" _settingsQueue;
B _isBuddyOrFollowUp;
B _isHeySiriAlwaysOn;
B _bluetoothDeviceSupportsHeySiri;
B _supportSideButtonActivation;
B _isFloatingWithReducedWidth;
B _shouldIncludeHomePodInCompactTriggerDisclosure;
q _enrollmentMode;
q _audioProductID;
@"NSString" _audioAccessoryName;
```

## Properties

```
@property (Tq,N,V_enrollmentMode) enrollmentMode;
@property (TB,N,V_isBuddyOrFollowUp) isBuddyOrFollowUp;
@property (TB,N,V_isHeySiriAlwaysOn) isHeySiriAlwaysOn;
@property (TB,N,V_bluetoothDeviceSupportsHeySiri) bluetoothDeviceSupportsHeySiri;
@property (TB,N,V_supportSideButtonActivation) supportSideButtonActivation;
@property (TB,N,V_isFloatingWithReducedWidth) isFloatingWithReducedWidth;
@property (TB,N,V_shouldIncludeHomePodInCompactTriggerDisclosure) shouldIncludeHomePodInCompactTriggerDisclosure;
@property (Tq,N,V_audioProductID) audioProductID;
@property (T@"NSString",&,N,V_audioAccessoryName) audioAccessoryName;
```

## Class methods

```
+[VTUIStyle sharedStyle];
```

## Instance methods

```
-[VTUIStyle enrollmentMode];
-[VTUIStyle horizontalPadding];
-[VTUIStyle init];
-[VTUIStyle dealloc];
-[VTUIStyle isIpad];
-[VTUIStyle buttonTextColor];
-[VTUIStyle subtitleFont];
-[VTUIStyle dynamicColorWithLightColor:darkColor:];
-[VTUIStyle VTUIDeviceSpecificString:];
-[VTUIStyle footerButtonFont];
-[VTUIStyle footerFont];
-[VTUIStyle isHeySiriAlwaysOn];
-[VTUIStyle setEnrollmentMode:];
-[VTUIStyle overrideBuddyImage];
-[VTUIStyle shouldOverrideBuddyBehavior];
-[VTUIStyle paneBackgroundColor];
-[VTUIStyle primaryButtonFont];
-[VTUIStyle PRXdismissButtonDefaultMargin];
-[VTUIStyle PRXdismissButtonMargin];
-[VTUIStyle PRXheaderFont];
-[VTUIStyle PRXtitleTopPadding];
-[VTUIStyle footerLabelFont];
-[VTUIStyle orbImageOffsetFromTopEnrollment];
-[VTUIStyle setSupportSideButtonActivation:];
-[VTUIStyle PRXcancelFont];
-[VTUIStyle PRXdismissButtonEdgeToEdgeMargin];
-[VTUIStyle PRXheaderColor];
-[VTUIStyle PRXpageFont];
-[VTUIStyle ProxCardKitTitleFontDescriptor];
-[VTUIStyle footerTextColor];
-[VTUIStyle instructionLabelFontWithWeight:];
-[VTUIStyle orbImagePadding];
-[VTUIStyle proxHeaderColor];
-[VTUIStyle VTUIDeviceSpecificAudioHintFileName:];
-[VTUIStyle _createStringSuffixesForDevice];
-[VTUIStyle _prefetchHomePodInfo];
-[VTUIStyle audioAccessoryName];
-[VTUIStyle audioProductID];
-[VTUIStyle bluetoothDeviceSupportsHeySiri];
-[VTUIStyle bottomOfContinueToNotNowFirstBaseline];
-[VTUIStyle continueButtonFromBottom];
-[VTUIStyle continueButtonFromBottomTwoButtons];
-[VTUIStyle continueButtonOffset];
-[VTUIStyle continueButtonPaddingTop];
-[VTUIStyle currentLocaleSupportsCompactVoiceTrigger];
-[VTUIStyle educationAssetNameForTraitCollection:];
-[VTUIStyle educationAssetSize];
-[VTUIStyle educationAssetTopPadding];
-[VTUIStyle educationViewDetailText];
-[VTUIStyle educationViewTitleText];
-[VTUIStyle finishEnrollmentFromBottom];
-[VTUIStyle footerButtonMaximumWidth];
-[VTUIStyle footerHorizontalPadding];
-[VTUIStyle footerSkipButtonBaselineFromBottom];
-[VTUIStyle footerTextBaselineFromTop];
-[VTUIStyle footerTextBottomPadding];
-[VTUIStyle headerTitleLinespacing];
-[VTUIStyle homeAppTintColor];
-[VTUIStyle horizontalPaddingLandscape];
-[VTUIStyle horizontalPaddingPortrait];
-[VTUIStyle horizontalTextPadding];
-[VTUIStyle iPadSolariumBottomOffset];
-[VTUIStyle imageViewTopOffsetLandscape];
-[VTUIStyle imageViewTopOffsetPortrait];
-[VTUIStyle instructionHorizontalPadding];
-[VTUIStyle instructionLabelFont];
-[VTUIStyle instructionOffsetFromTopTrainingForGM];
-[VTUIStyle instructionPreAndPostfixFont];
-[VTUIStyle instructionPreAndPostfixFontWithWeight:];
-[VTUIStyle isBuddyOrFollowUp];
-[VTUIStyle isEdgeToEdgePhone];
-[VTUIStyle isFloatingWithReducedWidth];
-[VTUIStyle isGreenTeaCapableDevice];
-[VTUIStyle isIPadWithVolumePowerSameSide];
-[VTUIStyle isIpadMini];
-[VTUIStyle isSmallestOnboardingDeviceInBuddy];
-[VTUIStyle laterButtonBaselinePadding];
-[VTUIStyle minimumImageViewHeight];
-[VTUIStyle orbImageLength];
-[VTUIStyle orbLength];
-[VTUIStyle orbOffsetFromTopEnrollment];
-[VTUIStyle orbOffsetFromTopTraining];
-[VTUIStyle paddingFromTop];
-[VTUIStyle primaryButtonHeight];
-[VTUIStyle primaryButtonHorizontalInset];
-[VTUIStyle proxAboutLinkFirstBaselineFromTop];
-[VTUIStyle proxAccessorySupportsCompactTrigger];
-[VTUIStyle proxBottomPaddingVoiceSelectionOptions];
-[VTUIStyle proxCancelFont];
-[VTUIStyle proxChooseForMeTopPaddingFromContinueButton];
-[VTUIStyle proxContainerCornerRadius];
-[VTUIStyle proxContainerHorizontalVerticalPadding];
-[VTUIStyle proxFooterFont];
-[VTUIStyle proxHSDescription:];
-[VTUIStyle proxHeaderFont];
-[VTUIStyle proxInstructionColor];
-[VTUIStyle proxInstructionFont];
-[VTUIStyle proxInstructionPreAndPostfixFont];
-[VTUIStyle proxIntroOrbFromTopLandscape];
-[VTUIStyle proxIntroOrbImageFromTopLandscape];
-[VTUIStyle proxIntroTitleFromTop];
-[VTUIStyle proxIntroTitleFromTopLandscape];
-[VTUIStyle proxLeading];
-[VTUIStyle proxLeadingLandscape];
-[VTUIStyle proxPaddingDataSharingSubtitle];
-[VTUIStyle proxPaddingFootnoteButton];
-[VTUIStyle proxPaddingFromBottom];
-[VTUIStyle proxPaddingFromTop];
-[VTUIStyle proxPaddingIntroSubtitle];
-[VTUIStyle proxPaddingIntroSubtitleLandscape];
-[VTUIStyle proxPaddingSkipButtonPageLabel];
-[VTUIStyle proxPaddingSuccessFromBottom];
-[VTUIStyle proxPaddingSuccessFromBottomLandscape];
-[VTUIStyle proxPaddingSuccessSubtitle];
-[VTUIStyle proxPaddingSuccessTitleLandscape];
-[VTUIStyle proxPaddingTrainingTitle];
-[VTUIStyle proxPaddingTrainingTitleLandscape];
-[VTUIStyle proxPaddingTryAgainTitleLandscape];
-[VTUIStyle proxPageFirstBaselineBottom];
-[VTUIStyle proxPageFont];
-[VTUIStyle proxPageLabelColor];
-[VTUIStyle proxPrimaryButtonColor];
-[VTUIStyle proxPrimaryButtonFont];
-[VTUIStyle proxPrimaryButtonHeight];
-[VTUIStyle proxSettingsLabelBottomMargin];
-[VTUIStyle proxSiriLogoHeightWidth];
-[VTUIStyle proxSiriLogoHeightWidthSmall];
-[VTUIStyle proxSkipButtonBaselineBottomMargin];
-[VTUIStyle proxStatusLabelMaxHeight];
-[VTUIStyle proxSubtitleColor];
-[VTUIStyle proxSubtitleFont];
-[VTUIStyle proxTitleFirstBaselineFromTop];
-[VTUIStyle proxTitleTrailingLandscape];
-[VTUIStyle proxTopPaddingVoiceSelectionOptions];
-[VTUIStyle proxTrailing];
-[VTUIStyle proxTrailingLandscape];
-[VTUIStyle proxTrainingDismissButtonHorizontalPadding];
-[VTUIStyle proxTrainingDismissButtonPhoneLandscapeHorizontalPadding];
-[VTUIStyle proxTrainingDismissButtonVerticalPaddingBottom];
-[VTUIStyle proxTrainingDismissButtonVerticalPaddingTop];
-[VTUIStyle proxTrainingDismissButtonWidthOrHeight];
-[VTUIStyle proxTrainingInstructionLabelHorizontalOffset];
-[VTUIStyle proxTrainingNotNowButtonVerticalPaddingTop];
-[VTUIStyle proxViewHeight];
-[VTUIStyle proxViewHeightPhoneLandscape];
-[VTUIStyle proxViewLanguageOptionsHeight];
-[VTUIStyle proxViewLanguageOptionsHeightPhoneLandscape];
-[VTUIStyle proxViewMaxWidth];
-[VTUIStyle proxViewMaxWidthPhoneLandscape];
-[VTUIStyle radarBtnHorizontalPadding];
-[VTUIStyle radarBtnVerticalPadding];
-[VTUIStyle secondaryButtonBaselinePadding];
-[VTUIStyle secondaryButtonFont];
-[VTUIStyle setAudioAccessoryName:];
-[VTUIStyle setAudioProductID:];
-[VTUIStyle setBluetoothDeviceSupportsHeySiri:];
-[VTUIStyle setIsBuddyOrFollowUp:];
-[VTUIStyle setIsFloatingWithReducedWidth:];
-[VTUIStyle setIsHeySiriAlwaysOn:];
-[VTUIStyle setShouldIncludeHomePodInCompactTriggerDisclosure:];
-[VTUIStyle shouldIncludeHomePodInCompactTriggerDisclosure];
-[VTUIStyle shouldPresentDisclosureForCompactVoiceTrigger];
-[VTUIStyle shouldPresentEducationView];
-[VTUIStyle shouldSetupForMultipleTriggerPhrases];
-[VTUIStyle shouldShowVoiceTriggerConfirmationInBuddy];
-[VTUIStyle shouldSkipGMEducationPages];
-[VTUIStyle siriIconImage];
-[VTUIStyle skipButtonBaselineBottomMarginLandscape];
-[VTUIStyle skipButtonBaselineBottomMarginPortrait];
-[VTUIStyle smallestDeviceOnboardingAsset];
-[VTUIStyle statusLabelMinHeight];
-[VTUIStyle statusLabelVerticalOffsetFromCenter];
-[VTUIStyle subtitle1BaselineOffset];
-[VTUIStyle subtitle2BaselineOffset];
-[VTUIStyle supportSideButtonActivation];
-[VTUIStyle supportsSideButtonActivation];
-[VTUIStyle supportsSiriConversationsAndBargeIn];
-[VTUIStyle textOverlayLabelWidth];
-[VTUIStyle textOverlayOffsetFromTop];
-[VTUIStyle titleBaselineOffsetFromTop];
-[VTUIStyle titleOffsetFromOrb];
-[VTUIStyle titleOffsetFromOrbImage];
-[VTUIStyle turnOnSiriContinueButtonFont];
-[VTUIStyle turnOnSiriContinueButtonHeight];
-[VTUIStyle turnOnSiriContinueButtonWidth];
-[VTUIStyle turnOnSiriFooterOffset];
-[VTUIStyle turnOnSiriImageOffsetFromTop];
-[VTUIStyle turnOnSiriSubtitle1BaselineOffset];
-[VTUIStyle turnOnSiriSubtitle2BaselineOffset];
```
