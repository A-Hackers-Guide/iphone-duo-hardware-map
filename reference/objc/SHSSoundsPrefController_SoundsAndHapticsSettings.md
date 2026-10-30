# `SHSSoundsPrefController`

- Image: [`/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`](../userland/System__Library__PrivateFrameworks__Settings__SoundsAndHapticsSettings.framework__SoundsAndHapticsSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- Protocols: `SHSRingerControlDelegate`, `SHSAlarmControlDelegate`, `SHSSystemSoundsControlDelegate`, `CoreTelephonyClientCarrierBundleDelegate`, `_TtP24SoundsAndHapticsSettings29SHSHapticsOptionsViewDelegate_`, `PSListControllerTestableSpecifiers`
- 21 instance variables, 23 properties, 124 instance methods, 1 class methods

## Instance variables

```
B _hasTelephony;
B _volumeHUDsuppressed;
q _currentPreviewAlertType;
B _viewIsDisappearing;
B __volumeSliderVisible;
@"ADASManager" _audioSettingsManager;
@"NSNumberFormatter" _numberFormatter;
@"SHSAudioPlayback" __audioPlayback;
@"SHSRingerControl" __ringerControl;
@"SHSAlarmControl" __alarmControl;
@"SHSSystemSoundsControl" __systemSoundsControl;
@"CoreTelephonyClient" __client;
@"PSSpecifier" __voiceMailSpecifier;
@"PSSpecifier" __alarmVolumeSliderSpecifier;
@"PSSpecifier" __alertVolumeSliderSpecifier;
@"PSSpecifier" __audioGroupSpecifier;
@"PSSpecifier" __headphoneLevelLimitingSpecifier;
q __voiceMailSpecifierIndex;
@"NSNumber" __cachedShouldHideValue;
@"UISlider" __alertVolumeSlider;
@"UISlider" __alarmVolumeSlider;
```

## Properties

```
@property (T@"ADASManager",&,N,V_audioSettingsManager) audioSettingsManager;
@property (T@"NSNumberFormatter",&,N,V_numberFormatter) numberFormatter;
@property (T@"SHSAudioPlayback",&,N,V__audioPlayback) _audioPlayback;
@property (TB,N,G_isVolumeSliderVisible,V__volumeSliderVisible) _volumeSliderVisible;
@property (T@"SHSRingerControl",&,N,V__ringerControl) _ringerControl;
@property (T@"SHSAlarmControl",&,N,V__alarmControl) _alarmControl;
@property (T@"SHSSystemSoundsControl",&,N,V__systemSoundsControl) _systemSoundsControl;
@property (T@"CoreTelephonyClient",&,N,V__client) _client;
@property (T@"PSSpecifier",&,N,V__voiceMailSpecifier) _voiceMailSpecifier;
@property (T@"PSSpecifier",&,N,V__alarmVolumeSliderSpecifier) _alarmVolumeSliderSpecifier;
@property (T@"PSSpecifier",&,N,V__alertVolumeSliderSpecifier) _alertVolumeSliderSpecifier;
@property (T@"PSSpecifier",&,N,V__audioGroupSpecifier) _audioGroupSpecifier;
@property (T@"PSSpecifier",&,N,V__headphoneLevelLimitingSpecifier) _headphoneLevelLimitingSpecifier;
@property (Tq,N,V__voiceMailSpecifierIndex) _voiceMailSpecifierIndex;
@property (T@"NSNumber",&,N,V__cachedShouldHideValue) _cachedShouldHideValue;
@property (T@"UISlider",W,N,V__alertVolumeSlider) _alertVolumeSlider;
@property (T@"UISlider",W,N,V__alarmVolumeSlider) _alarmVolumeSlider;
@property (TB,R,N) _isKeyHapticsSupported;
@property (TB,R,N) _isV68;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SHSSoundsPrefController booleanCapabilitiesToTest];
```

## Instance methods

```
-[SHSSoundsPrefController numberFormatter];
-[SHSSoundsPrefController carrierBundleChange:];
-[SHSSoundsPrefController tableView:cellForRowAtIndexPath:];
-[SHSSoundsPrefController willBecomeActive];
-[SHSSoundsPrefController willResignActive];
-[SHSSoundsPrefController init];
-[SHSSoundsPrefController viewWillDisappear:];
-[SHSSoundsPrefController tableView:didEndDisplayingCell:forRowAtIndexPath:];
-[SHSSoundsPrefController dealloc];
-[SHSSoundsPrefController _deviceType];
-[SHSSoundsPrefController viewDidLoad];
-[SHSSoundsPrefController viewWillAppear:];
-[SHSSoundsPrefController viewDidAppear:];
-[SHSSoundsPrefController set_client:];
-[SHSSoundsPrefController _client];
-[SHSSoundsPrefController setNumberFormatter:];
-[SHSSoundsPrefController didLock];
-[SHSSoundsPrefController showController:animate:];
-[SHSSoundsPrefController specifiers];
-[SHSSoundsPrefController endInterruption];
-[SHSSoundsPrefController updateVolume];
-[SHSSoundsPrefController _isV68];
-[SHSSoundsPrefController refreshShouldHideAllVoicemailUI];
-[SHSSoundsPrefController setPlayKeyboardSound:specifier:];
-[SHSSoundsPrefController set_alarmVolumeSliderSpecifier:];
-[SHSSoundsPrefController detailTextForToneWithSpecifier:];
-[SHSSoundsPrefController ringtoneVolume:];
-[SHSSoundsPrefController setSilentModeEnabled:specifier:];
-[SHSSoundsPrefController set_alertVolumeSliderSpecifier:];
-[SHSSoundsPrefController startVolumePreviewForAlertType:];
-[SHSSoundsPrefController volume:];
-[SHSSoundsPrefController _alarmControl];
-[SHSSoundsPrefController _alarmVolumeSlider];
-[SHSSoundsPrefController _alarmVolumeSliderSpecifier];
-[SHSSoundsPrefController _alertVolumeSlider];
-[SHSSoundsPrefController _alertVolumeSliderSpecifier];
-[SHSSoundsPrefController _attachAlarmSliderTouchHandlers:];
-[SHSSoundsPrefController _attachAlertSliderTouchHandlers:];
-[SHSSoundsPrefController _audioGroupSpecifier];
-[SHSSoundsPrefController _audioPlayback];
-[SHSSoundsPrefController _cachedShouldHideValue];
-[SHSSoundsPrefController _headphoneLevelLimitingSpecifier];
-[SHSSoundsPrefController _isKeyHapticsSupported];
-[SHSSoundsPrefController _isVolumeSliderVisible];
-[SHSSoundsPrefController _keyboardClicksTitle:];
-[SHSSoundsPrefController _keyboardFeedbackSpecifier];
-[SHSSoundsPrefController _queryRingtoneMinimumVolume];
-[SHSSoundsPrefController _reattachTouchHandlersForVisibleVolumeSliders];
-[SHSSoundsPrefController _ringerControl];
-[SHSSoundsPrefController _systemSoundsControl];
-[SHSSoundsPrefController _updateRingtoneSliderMinimum];
-[SHSSoundsPrefController _voiceMailSpecifier];
-[SHSSoundsPrefController _voiceMailSpecifierIndex];
-[SHSSoundsPrefController _volumeSliderCell];
-[SHSSoundsPrefController ageOfToggleForSilentModeOn:];
-[SHSSoundsPrefController alarmControl:volumeValueDidChange:];
-[SHSSoundsPrefController alarmControlDidObserveEffectiveSystemVolumeChange:];
-[SHSSoundsPrefController alarmSliderTouchBegan:];
-[SHSSoundsPrefController alarmSliderTouchEnded:];
-[SHSSoundsPrefController alarmVolume:];
-[SHSSoundsPrefController alertSliderTouchBegan:];
-[SHSSoundsPrefController alertSliderTouchEnded:];
-[SHSSoundsPrefController alertVolume:];
-[SHSSoundsPrefController audioSettingsManager];
-[SHSSoundsPrefController canChangeRingtoneWithButtons:];
-[SHSSoundsPrefController didBackground];
-[SHSSoundsPrefController getFixedVolumeControlsFooterWithSwitch:];
-[SHSSoundsPrefController getHeadphoneLevelLimitSetting];
-[SHSSoundsPrefController getMicrophoneLabel:];
-[SHSSoundsPrefController getSelectedHapticsOption];
-[SHSSoundsPrefController getSelectedHapticsOptionTitleWithSpecifier:];
-[SHSSoundsPrefController getSilentModeFooterWithSwitch:];
-[SHSSoundsPrefController handleInputNotification:];
-[SHSSoundsPrefController handleSilentModeNotification:];
-[SHSSoundsPrefController hapticsOptionsDidChange:];
-[SHSSoundsPrefController matchAlarmRingtoneVolume:];
-[SHSSoundsPrefController matchRingtoneVolume:];
-[SHSSoundsPrefController presentHapticsController:];
-[SHSSoundsPrefController ringerControl:volumeValueDidChange:];
-[SHSSoundsPrefController ringerControlDidObserveEffectiveSystemVolumeChange:];
-[SHSSoundsPrefController serverDiedNotificationHandler:];
-[SHSSoundsPrefController setAlarmVolume:specifier:];
-[SHSSoundsPrefController setAlertVolume:specifier:];
-[SHSSoundsPrefController setAudioSettingsManager:];
-[SHSSoundsPrefController setCanChangeRingtoneWithButtons:specifier:];
-[SHSSoundsPrefController setFixedVolumeControls:specifier:];
-[SHSSoundsPrefController setLateNightMode:specifier:];
-[SHSSoundsPrefController setMatchAlarmRingtoneVolume:specifier:];
-[SHSSoundsPrefController setMatchRingtoneVolume:specifier:];
-[SHSSoundsPrefController setPlayLockSound:specifier:];
-[SHSSoundsPrefController setRingtoneVolume:specifier:];
-[SHSSoundsPrefController setShowInStatusBarEnabled:specifier:];
-[SHSSoundsPrefController setSilentModeOff:];
-[SHSSoundsPrefController setSilentModeOn:];
-[SHSSoundsPrefController setSoundEffects:specifier:];
-[SHSSoundsPrefController setSystemHapticsEnabled:specifier:];
-[SHSSoundsPrefController setUpSilentModeNotifications];
-[SHSSoundsPrefController setVolume:specifier:];
-[SHSSoundsPrefController setVolumeHUDsuppression:];
-[SHSSoundsPrefController set_alarmControl:];
-[SHSSoundsPrefController set_alarmVolumeSlider:];
-[SHSSoundsPrefController set_alertVolumeSlider:];
-[SHSSoundsPrefController set_audioGroupSpecifier:];
-[SHSSoundsPrefController set_audioPlayback:];
-[SHSSoundsPrefController set_cachedShouldHideValue:];
-[SHSSoundsPrefController set_headphoneLevelLimitingSpecifier:];
-[SHSSoundsPrefController set_ringerControl:];
-[SHSSoundsPrefController set_systemSoundsControl:];
-[SHSSoundsPrefController set_voiceMailSpecifier:];
-[SHSSoundsPrefController set_voiceMailSpecifierIndex:];
-[SHSSoundsPrefController set_volumeSliderVisible:];
-[SHSSoundsPrefController showInStatusBarEnabled:];
-[SHSSoundsPrefController silentModeEnabled:];
-[SHSSoundsPrefController soundEffects:];
-[SHSSoundsPrefController startSystemSoundVolumePreview];
-[SHSSoundsPrefController systemHapticsEnabled:];
-[SHSSoundsPrefController systemSoundsControl:volumeValueDidChange:];
-[SHSSoundsPrefController systemSoundsControlDidObserveEffectiveSystemVolumeChange:];
-[SHSSoundsPrefController unregisterSilentModeNotifications];
-[SHSSoundsPrefController updateSilentModeGroupFooterWithNewValue:];
-[SHSSoundsPrefController updateVoiceMailVisibility];
-[SHSSoundsPrefController willForeground];
-[SHSSoundsPrefController willHideSlider];
-[SHSSoundsPrefController willShowSlider];
```
