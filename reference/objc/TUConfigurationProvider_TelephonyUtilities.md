# `TUConfigurationProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 67 properties, 108 instance methods, 0 class methods

## Instance variables

```
i _token;
@"<TUConfigurationProviderDelegate>" _delegate;
@"TUUserConfiguration" _userConfiguration;
@"<TUConfigurationProviderNotifier>" _configurationProviderNotifier;
@"CoreTelephonyClient" _coreTelephonyClient;
@"TULiveLookupManagerProxy" _liveLookupExtensionManager;
@"<TUCarrierBundleControllerProtocol>" _carrierBundleController;
@"TUFeatureFlags" _featureFlags;
```

## Properties

```
@property (T@"TUUserConfiguration",R,N,V_userConfiguration) userConfiguration;
@property (T@"<TUConfigurationProviderNotifier>",R,N,V_configurationProviderNotifier) configurationProviderNotifier;
@property (T@"CoreTelephonyClient",R,N,V_coreTelephonyClient) coreTelephonyClient;
@property (T@"TULiveLookupManagerProxy",R,N,V_liveLookupExtensionManager) liveLookupExtensionManager;
@property (Ti,R,N,V_token) token;
@property (T@"<TUCarrierBundleControllerProtocol>",R,N,V_carrierBundleController) carrierBundleController;
@property (T@"TUFeatureFlags",R,N,V_featureFlags) featureFlags;
@property (T@"<TUConfigurationProviderDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisSIMAvailable) simAvailable;
@property (TB,R,N,GisIncomingCallsAvailableForPhone) incomingCallsAvailableForPhone;
@property (TB,R,N,GisCallAnnouncementAvailableForPhone) callAnnouncementAvailableForPhone;
@property (TB,R,N,GisMyNumberAvailable) myNumberAvailable;
@property (TB,R,N,GisCallReportingAvailable) callReportingAvailable;
@property (TB,R,N,GisShareNameAndPhotosAvailable) shareNameAndPhotosAvailable;
@property (TB,R,N,GisWiFiCallingAvailable) wiFiCallingAvailable;
@property (TB,R,N,GisRelayPrimaryAvailable) relayPrimaryAvailable;
@property (TB,R,N,GisRelaySecondaryAvailable) relaySecondaryAvailable;
@property (TB,R,N,GisRespondwithTextAvailable) respondwithTextAvailable;
@property (TB,R,N,GisCallForwardingAvailable) callForwardingAvailable;
@property (TB,R,N,GisCallWaitingAvailable) callWaitingAvailable;
@property (TB,R,N,GisShowMyCallerIDAvailable) showMyCallerIDAvailable;
@property (TB,R,N,GisCallScreeningAvailable) callScreeningAvailable;
@property (TB,R,N,GisReceptionistAvailable) receptionistAvailable;
@property (TB,R,N,GisBrandedCallingAvailable) brandedCallingAvailable;
@property (TB,R,N,GisBusinessConnectCallingAvailable) businessConnectCallingAvailable;
@property (TB,R,N,GisLiveLookupAvailable) liveLookupAvailable;
@property (TB,R,N,GisCallBlockingAndIdentificationAvailable) callBlockingAndIdentificationAvailable;
@property (TB,R,N,GisBlockedContactsAvailable) blockedContactsAvailable;
@property (TB,R,N,GisILClassificationAvailable) iLClassificationAvailable;
@property (TB,R,N,GisDialAssistAvailable) dialAssistAvailable;
@property (TB,R,N,GisCallIdentificationAppsAvailable) callIdentificationAppsAvailable;
@property (TB,R,N,GisSilenceJunkCallingAvailable) silenceJunkCallingAvailable;
@property (TB,R,N,GisJunkFilteringAvailable) junkFilteringAvailable;
@property (TB,R,N,GisCallRecordingAvailable) callRecordingAvailable;
@property (TB,N,GisCallRecordingEnabled,SsetCallRecordingEnabled:) callRecordingEnabled;
@property (TB,R,N,GisUplevelFTAAvailable) uplevelFTAAvailable;
@property (TB,N,GisCallScreeningEnabled,SsetCallScreeningEnabled:) callScreeningEnabled;
@property (TB,N,GisReceptionistEnabled,SsetReceptionistEnabled:) receptionistEnabled;
@property (TB,N,GisEligibleForReceptionistOnboardingNotification,SsetEligibleForReceptionistOnboardingNotification:) eligibleForReceptionistOnboardingNotification;
@property (TB,N,GisSilenceUnknownCallersEnabledForPhone,SsetSilenceUnknownCallersEnabledForPhone:) silenceUnknownCallersEnabledForPhone;
@property (TB,N,GisSilenceUnknownCallersEnabledForFaceTime,SsetSilenceUnknownCallersEnabledForFaceTime:) silenceUnknownCallersEnabledForFaceTime;
@property (TB,N,GisFilterAsNewCallersEnabledForPhone,SsetFilterAsNewCallersEnabledForPhone:) filterAsNewCallersEnabledForPhone;
@property (TB,N,GisFilterAsNewCallersEnabledForFaceTime,SsetFilterAsNewCallersEnabledForFaceTime:) filterAsNewCallersEnabledForFaceTime;
@property (TB,N,GisSilenceJunkCallingEnabled,SsetSilenceJunkCallingEnabled:) silenceJunkCallingEnabled;
@property (TB,N,GisSilenceJunkCallingUserPreferenceEnabled,SsetSilenceJunkCallingUserPreferenceEnabled:) silenceJunkCallingUserPreferenceEnabled;
@property (TB,N,GisBusinessConnectCallingEnabled,SsetBusinessConnectCallingEnabled:) businessConnectCallingEnabled;
@property (TB,N,GisUplevelFTAEnabled,SsetUplevelFTAEnabled:) uplevelFTAEnabled;
@property (TB,N,GisHoldAssistDetectionEnabled,SsetHoldAssistDetectionEnabled:) holdAssistDetectionEnabled;
@property (TB,R,N,GisCallHapticsAvailable) callHapticsAvailable;
@property (TB,N,GisCallHapticsEnabled,SsetCallHapticsEnabled:) callHapticsEnabled;
@property (TB,R,N,GisFaceTimeEnabledInSettings) faceTimeEnabledInSettings;
@property (TB,R,N,GisIncomingCallsAvailableForFaceTime) incomingCallsAvailableForFaceTime;
@property (TB,R,N,GisCallAnnouncementAvailableForFaceTime) callAnnouncementAvailableForFaceTime;
@property (TB,R,N,GisSharePlayAvailable) sharePlayAvailable;
@property (TB,R,N,GisAutomaticProminenceAvailable) automaticProminenceAvailable;
@property (TB,R,N,GisLivePhotosAvailable) livePhotosAvailable;
@property (TB,N,GisSpamFilterEnabledForFaceTime,SsetSpamFilterEnabledForFaceTime:) spamFilterEnabledForFaceTime;
@property (TB,R,N,GisSIMPINAvailable) simPINAvailable;
@property (TB,R,N,GisNetworkSelectionAvailable) networkSelectionAvailable;
@property (Tq,N,GgetSelectedIntelligentCallScreeningMenuOptionForFaceTime,SsetSelectedIntelligentCallScreeningMenuOptionForFaceTime:) intelligentCallScreeningMenuOptionForFaceTime;
@property (Tq,N,GgetSelectedIntelligentCallScreeningMenuOptionForPhone,SsetSelectedIntelligentCallScreeningMenuOptionForPhone:) intelligentCallScreeningMenuOptionForPhone;
@property (TB,R,N,GisGranularCallFilteringAvailableForFaceTime) granularCallFilteringAvailableForFaceTime;
@property (TQ,N,SsetFaceTimeNewCallersFilterMode:) faceTimeNewCallersFilterMode;
@property (TB,R,N,GisFaceTimeHideNotificationsAvailable) faceTimeHideNotificationsAvailable;
@property (TB,N,SsetFaceTimeHideNotifications:) faceTimeHideNotifications;
@property (TB,R,N,GisSmartVoicemailActionsAvailable) smartVoicemailActionsAvailable;
@property (TB,N,GisSmartVoicemailActionsEnabled,SsetSmartVoicemailActionsEnabled:) smartVoicemailActionsEnabled;
```

## Instance methods

```
-[TUConfigurationProvider setReceptionistEnabled:];
-[TUConfigurationProvider setBusinessConnectCallingEnabled:];
-[TUConfigurationProvider isCallScreeningEnabled];
-[TUConfigurationProvider isSharePlayAvailable];
-[TUConfigurationProvider coreTelephonyClient];
-[TUConfigurationProvider isSilenceJunkCallingEnabled];
-[TUConfigurationProvider isCallRecordingEnabled];
-[TUConfigurationProvider setFilterAsNewCallersEnabledForFaceTime:];
-[TUConfigurationProvider setSpamFilterEnabledForFaceTime:];
-[TUConfigurationProvider init];
-[TUConfigurationProvider setFilterAsNewCallersEnabledForPhone:];
-[TUConfigurationProvider isSpamFilterEnabledForFaceTime];
-[TUConfigurationProvider isSmartVoicemailActionsEnabled];
-[TUConfigurationProvider isBusinessConnectCallingEnabled];
-[TUConfigurationProvider dealloc];
-[TUConfigurationProvider setCallRecordingEnabled:];
-[TUConfigurationProvider isFilterAsNewCallersEnabledForFaceTime];
-[TUConfigurationProvider setHoldAssistDetectionEnabled:];
-[TUConfigurationProvider faceTimeNewCallersFilterMode];
-[TUConfigurationProvider setFaceTimeHideNotifications:];
-[TUConfigurationProvider isEligibleForReceptionistOnboardingNotification];
-[TUConfigurationProvider setFaceTimeNewCallersFilterMode:];
-[TUConfigurationProvider setUplevelFTAEnabled:];
-[TUConfigurationProvider setSilenceJunkCallingEnabled:];
-[TUConfigurationProvider setSilenceUnknownCallersEnabledForFaceTime:];
-[TUConfigurationProvider setDelegate:];
-[TUConfigurationProvider setSilenceUnknownCallersEnabledForPhone:];
-[TUConfigurationProvider setCallScreeningEnabled:];
-[TUConfigurationProvider faceTimeHideNotifications];
-[TUConfigurationProvider delegate];
-[TUConfigurationProvider objectForKeyHierarchy:subscriptionContext:error:];
-[TUConfigurationProvider isBrandedCallingEnabled:];
-[TUConfigurationProvider setEligibleForReceptionistOnboardingNotification:];
-[TUConfigurationProvider isCallHapticsEnabled];
-[TUConfigurationProvider isUplevelFTAEnabled];
-[TUConfigurationProvider isHoldAssistDetectionEnabled];
-[TUConfigurationProvider token];
-[TUConfigurationProvider setCallHapticsEnabled:];
-[TUConfigurationProvider isFilterAsNewCallersEnabledForPhone];
-[TUConfigurationProvider isSilenceUnknownCallersEnabledForPhone];
-[TUConfigurationProvider isSilenceUnknownCallersEnabledForFaceTime];
-[TUConfigurationProvider setSmartVoicemailActionsEnabled:];
-[TUConfigurationProvider isReceptionistEnabled];
-[TUConfigurationProvider featureFlags];
-[TUConfigurationProvider _isSharedNameAndPhotoPermitted];
-[TUConfigurationProvider carrierBundleController];
-[TUConfigurationProvider configurationProviderNotifier];
-[TUConfigurationProvider getSelectedIntelligentCallScreeningMenuOptionForFaceTime];
-[TUConfigurationProvider getSelectedIntelligentCallScreeningMenuOptionForPhone];
-[TUConfigurationProvider initWithNotifier:];
-[TUConfigurationProvider isAutomaticProminenceAvailable];
-[TUConfigurationProvider isBlockedContactsAvailable];
-[TUConfigurationProvider isBrandedCallingAvailable];
-[TUConfigurationProvider isBusinessConnectCallingAvailable];
-[TUConfigurationProvider isCallAnnouncementAvailableForFaceTime];
-[TUConfigurationProvider isCallAnnouncementAvailableForPhone];
-[TUConfigurationProvider isCallBlockingAndIdentificationAvailable];
-[TUConfigurationProvider isCallForwardingAvailable];
-[TUConfigurationProvider isCallHapticsAvailable];
-[TUConfigurationProvider isCallIdentificationAppsAvailable];
-[TUConfigurationProvider isCallRecordingAvailable];
-[TUConfigurationProvider isCallReportingAvailable];
-[TUConfigurationProvider isCallScreeningAvailable];
-[TUConfigurationProvider isCallWaitingAvailable];
-[TUConfigurationProvider isDialAssistAvailable];
-[TUConfigurationProvider isFaceTimeEnabledInSettings];
-[TUConfigurationProvider isFaceTimeHideNotificationsAvailable];
-[TUConfigurationProvider isGranularCallFilteringAvailableForFaceTime];
-[TUConfigurationProvider isHoldAssistAvailable];
-[TUConfigurationProvider isILClassificationAvailable];
-[TUConfigurationProvider isIncomingCallsAvailableForFaceTime];
-[TUConfigurationProvider isIncomingCallsAvailableForPhone];
-[TUConfigurationProvider isJunkFilteringAvailable];
-[TUConfigurationProvider isLiveLookupAvailable];
-[TUConfigurationProvider isLivePhotosAvailable];
-[TUConfigurationProvider isMyNumberAvailable];
-[TUConfigurationProvider isNetworkSelectionAvailable];
-[TUConfigurationProvider isReceptionistAvailable];
-[TUConfigurationProvider isRelayPrimaryAvailable];
-[TUConfigurationProvider isRelaySecondaryAvailable];
-[TUConfigurationProvider isRespondwithTextAvailable];
-[TUConfigurationProvider isSIMAvailable];
-[TUConfigurationProvider isSIMPINAvailable];
-[TUConfigurationProvider isShareNameAndPhotosAvailable];
-[TUConfigurationProvider isShowMyCallerIDAvailable];
-[TUConfigurationProvider isSilenceJunkCallingAvailable];
-[TUConfigurationProvider isSilenceJunkCallingUserPreferenceEnabled];
-[TUConfigurationProvider isSmartVoicemailActionsAvailable];
-[TUConfigurationProvider isSystemCapabilityAvailableForName:];
-[TUConfigurationProvider isUplevelFTAAvailable];
-[TUConfigurationProvider isWiFiCallingAvailable];
-[TUConfigurationProvider liveLookupExtensionManager];
-[TUConfigurationProvider numberForKeyHierarchy:subscriptionContext:error:];
-[TUConfigurationProvider postConfigurationChangedNotification];
-[TUConfigurationProvider setBrandedCallingEnabled:primary:];
-[TUConfigurationProvider setSelectedIntelligentCallScreeningMenuOptionForFaceTime:];
-[TUConfigurationProvider setSelectedIntelligentCallScreeningMenuOptionForPhone:];
-[TUConfigurationProvider setSilenceJunkCallingUserPreferenceEnabled:];
-[TUConfigurationProvider shouldShowCarrierAttributionForSimUUID:];
-[TUConfigurationProvider shouldShowCarrierAttributionForSubscriptionContext:];
-[TUConfigurationProvider stringForKeyHierarchy:subscriptionContext:error:];
-[TUConfigurationProvider supportsBrandedCallingForSubscriptionContext:];
-[TUConfigurationProvider supportsBusinessConnectCallingForSubscriptionContext:];
-[TUConfigurationProvider supportsCallBlockingForSubscriptionContext:];
-[TUConfigurationProvider supportsDialAssistForSubscriptionContext:];
-[TUConfigurationProvider supportsSystemCapabilityWithName:subscriptionContext:];
-[TUConfigurationProvider systemCapabilitiesForSubscriptionContext:];
-[TUConfigurationProvider userConfiguration];
```
