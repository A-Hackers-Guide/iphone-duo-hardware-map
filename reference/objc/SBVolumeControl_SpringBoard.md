# `SBVolumeControl`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBControlCenterObserver`, `SBElasticHUDViewControllerDelegate`, `SBElasticVolumeDataSource`, `SBFZStackParticipantObserver`, `PTSettingsKeyObserver`, `SBWindowSceneAttachmentObserving`
- 18 instance variables, 6 properties, 57 instance methods, 2 class methods

## Instance variables

```
@"<SBHUDControlling>" _hudController;
@"SBElasticHUDSettings" _elasticHUDSettings;
@"SBRingerControl" _ringerControl;
@"SBTelephonyManager" _telephonyManager;
@"SBConferenceManager" _conferenceManager;
B _debounce;
Q _mode;
@"NSSet" _audioCategoriesDisablingVolumeHUD;
@"NSMutableSet" _alwaysHiddenCategories;
@"NSString" _lastEventCategory;
B _volumeDownButtonIsDown;
B _volumeUpButtonIsDown;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _effectiveVolumeLock;
f _effectiveVolume;
@"NSObject<OS_dispatch_queue>" _avscOperationsQueue;
@"SBAVSystemControllerCache" _avCache;
@"NSString" _lastDisplayedCategory;
@"SBControlCenterCoordinator" _controlCenterCoordinator;
```

## Properties

```
@property (T@"SBControlCenterCoordinator",R,W,N,V_controlCenterCoordinator) controlCenterCoordinator;
@property (T@"NSString",R,N,V_lastDisplayedCategory) lastDisplayedCategory;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBVolumeControl _isVolumeChangeAllowedForState:error:];
+[SBVolumeControl _isVolumeManagedForCategory:];
```

## Instance methods

```
-[SBVolumeControl _effectiveVolume];
-[SBVolumeControl zStackParticipantWithIdentifier:settingsDidChange:];
-[SBVolumeControl _processZStackParticipantSettings:];
-[SBVolumeControl zStackParticipantWithIdentifier:wasAcquiredWithSettings:];
-[SBVolumeControl windowSceneDidDisconnect:];
-[SBVolumeControl dealloc];
-[SBVolumeControl setActiveCategoryVolume:];
-[SBVolumeControl settings:changedValueForKey:];
-[SBVolumeControl windowSceneDidConnect:];
-[SBVolumeControl controlCenterCoordinator];
-[SBVolumeControl cancelVolumeEvent];
-[SBVolumeControl decreaseVolume];
-[SBVolumeControl handleVolumeButtonWithType:down:];
-[SBVolumeControl increaseVolume];
-[SBVolumeControl existingVolumeHUDViewController];
-[SBVolumeControl _avscOperationsQueue];
-[SBVolumeControl _buttonRepeatDelay];
-[SBVolumeControl _configureVolumeStepDeltaForVolumeHUDViewController:];
-[SBVolumeControl _dispatchAVSystemControllerAsync:];
-[SBVolumeControl _dispatchAVSystemControllerSync:];
-[SBVolumeControl _displaysVolumeForCategory:];
-[SBVolumeControl _effectiveVolumeChanged:];
-[SBVolumeControl _getMediaVolumeForIAP];
-[SBVolumeControl _isCategoryAlwaysHidden:];
-[SBVolumeControl _isHUDDisplayableForCategory:outReason:];
-[SBVolumeControl _isHUDDisplayableForLastEventCategoryWithReason:];
-[SBVolumeControl _isHUDDisplayableWithReason:];
-[SBVolumeControl _isVolumeHUDVisible];
-[SBVolumeControl _isVolumeHUDVisibleOnHUDController:];
-[SBVolumeControl _isVolumeHUDVisibleOnWindowScene:];
-[SBVolumeControl _presentVolumeHUDWithVolume:];
-[SBVolumeControl _resetMediaServerConnection];
-[SBVolumeControl _serverConnectionDied:];
-[SBVolumeControl _setMediaVolumeForIAP:];
-[SBVolumeControl _targetWindowScene];
-[SBVolumeControl _updateEffectiveVolume:];
-[SBVolumeControl acquireVolumeHUDHiddenAssertionForReason:];
-[SBVolumeControl addAlwaysHiddenCategory:];
-[SBVolumeControl canChangeVolumeForActiveCategory:isAudioSessionPlaying:];
-[SBVolumeControl changeVolumeByDelta:];
-[SBVolumeControl clearAlwaysHiddenCategories];
-[SBVolumeControl controlCenter:didDismissOnWindowScene:];
-[SBVolumeControl controlCenter:willPresentOnWindowScene:];
-[SBVolumeControl elasticHUDViewControllerCanBePresented:withReason:];
-[SBVolumeControl elasticHUDViewControllerRequestsDismissal:];
-[SBVolumeControl elasticValueViewController:updateCurrentValue:];
-[SBVolumeControl elasticValueViewControllerCurrentValue:];
-[SBVolumeControl elasticVolumeViewControllerActiveAudioCategory:];
-[SBVolumeControl hideVolumeHUDIfVisible];
-[SBVolumeControl initWithHUDController:ringerControl:telephonyManager:conferenceManager:avSystemControllerCache:controlCenterCoordinator:];
-[SBVolumeControl lastDisplayedCategory];
-[SBVolumeControl presentedVolumeHUDViewController];
-[SBVolumeControl removeAlwaysHiddenCategory:];
-[SBVolumeControl setVolume:forCategory:];
-[SBVolumeControl toggleMute];
-[SBVolumeControl volumeStepDown];
-[SBVolumeControl volumeStepUp];
```
