# `SBTelephonyManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `STTelephonyStateObserver`
- 31 instance variables, 18 properties, 108 instance methods, 3 class methods

## Instance variables

```
^{__CTServerConnection=} _serverConnection;
B _containsCellularRadio;
B _hasCellularTelephony;
B _hasCellularData;
b1 _usingVPN;
@"NSObject<OS_dispatch_queue>" _wirelessModemDynamicStoreQueue;
^{__SCDynamicStore=} _queue_wirelessModemDynamicStore;
^{__CFString=} _queue_wirelessModemDynamicStoreSharingKey;
B _isNetworkTethering;
i _numberOfNetworkTetheredDevices;
b1 _hasShownWaitingAlert;
@"SBAlertItem" _activationAlertItem;
i _numActivationFailures;
i _inEmergencyCallbackMode;
i _supportsDynamicSIMConfiguration;
i _isSharingIdentitySupported;
b1 _loggingCallAudio;
^v _queue_fastDormancySuspendAssertion;
@"NWSystemPathMonitor" _systemPathMonitor;
@"TUCall" _incomingCall;
@"TUCall" _activeCall;
@"TUCall" _heldCall;
@"TUCall" _outgoingCall;
@"CoreTelephonyClient" _coreTelephonyClient;
@"STTelephonyStateProvider" _telephonyStateProvider;
@"STWifiStatusDomain" _wifiDomain;
@"SBBluetoothController" _bluetoothController;
@"NSString" _cachedSlot1CountryCode;
@"NSString" _cachedSlot2CountryCode;
@"NSString" _cachedSlot1SIMStatus;
@"NSString" _cachedSlot2SIMStatus;
```

## Properties

```
@property (T@"TUCall",&,N,V_incomingCall) incomingCall;
@property (T@"TUCall",&,N,V_activeCall) activeCall;
@property (T@"TUCall",&,N,V_heldCall) heldCall;
@property (T@"TUCall",&,N,V_outgoingCall) outgoingCall;
@property (T@"CoreTelephonyClient",&,N,V_coreTelephonyClient) coreTelephonyClient;
@property (T@"STTelephonyStateProvider",R,N,V_telephonyStateProvider) telephonyStateProvider;
@property (T@"STWifiStatusDomain",R,N,V_wifiDomain) wifiDomain;
@property (T@"SBBluetoothController",R,N,V_bluetoothController) bluetoothController;
@property (T@"NSString",C,N,V_cachedSlot1CountryCode) cachedSlot1CountryCode;
@property (T@"NSString",C,N,V_cachedSlot2CountryCode) cachedSlot2CountryCode;
@property (T@"NSString",C,N,V_cachedSlot1SIMStatus) cachedSlot1SIMStatus;
@property (T@"NSString",C,N,V_cachedSlot2SIMStatus) cachedSlot2SIMStatus;
@property (TQ,R,N) dataConnectionAvailabilityWithCurrentCalls;
@property (TB,N,GisCellDataSwitchingEnabled) cellDataSwitchingEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBTelephonyManager sharedTelephonyManagerCreatingIfNecessary:];
+[SBTelephonyManager defaultTelephonyCenter];
+[SBTelephonyManager sharedTelephonyManager];
```

## Instance methods

```
-[SBTelephonyManager isEndpointOnCurrentDevice];
-[SBTelephonyManager inBargeCall];
-[SBTelephonyManager numberOfNetworkTetheredDevices];
-[SBTelephonyManager _updateState];
-[SBTelephonyManager activateForEsimSetupInBuddy];
-[SBTelephonyManager disconnectAllCalls];
-[SBTelephonyManager activeCallExists];
-[SBTelephonyManager setCellDataSwitchingEnabled:];
-[SBTelephonyManager telephonyStateProvider];
-[SBTelephonyManager queue_setFastDormancySuspended:withConnection:];
-[SBTelephonyManager setCoreTelephonyClient:];
-[SBTelephonyManager observeValueForKeyPath:ofObject:change:context:];
-[SBTelephonyManager outgoingCallExists];
-[SBTelephonyManager coreTelephonyClient];
-[SBTelephonyManager _dataConnectedSubscriptionSlot];
-[SBTelephonyManager hasCellularData];
-[SBTelephonyManager bluetoothController];
-[SBTelephonyManager isUsingSlowDataConnection];
-[SBTelephonyManager cachedSlot2SIMStatus];
-[SBTelephonyManager isUsingVPNConnection];
-[SBTelephonyManager _secondarySubscriptionSlot];
-[SBTelephonyManager _otherSubscriptionSlot:];
-[SBTelephonyManager telephonyCallCount];
-[SBTelephonyManager setActiveCall:];
-[SBTelephonyManager _backgroundQueryQueue];
-[SBTelephonyManager inCallUsingSpeakerOrReceiver];
-[SBTelephonyManager outgoingCall];
-[SBTelephonyManager _secondaryMobileEquipmentInfo];
-[SBTelephonyManager supportsDynamicSIMConfiguration];
-[SBTelephonyManager setCachedSlot1CountryCode:];
-[SBTelephonyManager _primarySubscriptionSlot];
-[SBTelephonyManager swapCalls];
-[SBTelephonyManager setOutgoingCall:];
-[SBTelephonyManager _secondarySubscriptionInfoIfEnabled];
-[SBTelephonyManager _primarySubscriptionInfo];
-[SBTelephonyManager carrierBundleInfoDidChangeForStateProvider:slot:];
-[SBTelephonyManager _handleTelephonyDaemonRestart];
-[SBTelephonyManager _updateNetworkLocale];
-[SBTelephonyManager wifiDomain];
-[SBTelephonyManager isInEmergencyCallbackMode];
-[SBTelephonyManager disconnectIncomingCall];
-[SBTelephonyManager updateLocale];
-[SBTelephonyManager _mobileEquipmentInfoForSlot:];
-[SBTelephonyManager _callCountForService:];
-[SBTelephonyManager _avSystemControllerDidError:];
-[SBTelephonyManager inCallDuration];
-[SBTelephonyManager subscriptionInfoDidChangeForStateProvider:slot:];
-[SBTelephonyManager updateSpringBoard];
-[SBTelephonyManager _secondaryCarrierBundleInfo];
-[SBTelephonyManager _primaryCarrierBundleInfo];
-[SBTelephonyManager _setIsInEmergencyCallbackMode:];
-[SBTelephonyManager incomingCallExists];
-[SBTelephonyManager inCall];
-[SBTelephonyManager isSharingIdentitySupported];
-[SBTelephonyManager handleCallControlFailure:];
-[SBTelephonyManager setFastDormancySuspended:];
-[SBTelephonyManager isPhysicalSIMActive];
-[SBTelephonyManager callCount];
-[SBTelephonyManager _performQueryInBackground:withMainQueueResultHandler:];
-[SBTelephonyManager cachedSlot2CountryCode];
-[SBTelephonyManager _dataPreferredSubscriptionSlotIfSIMPresent];
-[SBTelephonyManager _serverConnection];
-[SBTelephonyManager telephonyAudioChangeHandler];
-[SBTelephonyManager _queue_noteWirelessModemDynamicStoreChanged];
-[SBTelephonyManager incomingCall];
-[SBTelephonyManager cachedSlot1CountryCode];
-[SBTelephonyManager isNetworkTethering];
-[SBTelephonyManager heldCall];
-[SBTelephonyManager isCellDataSwitchingEnabled];
-[SBTelephonyManager heldCallExists];
-[SBTelephonyManager dataConnectionAvailabilityWithCurrentCalls];
-[SBTelephonyManager callEventHandler:];
-[SBTelephonyManager preHeatDataLinkForDomains:];
-[SBTelephonyManager activeCall];
-[SBTelephonyManager _provisioningUpdateWithStatus:slot:];
-[SBTelephonyManager setCachedSlot1SIMStatus:];
-[SBTelephonyManager updateCalls];
-[SBTelephonyManager _subscriptionInfoForCall:];
-[SBTelephonyManager _setIsNetworkTethering:withNumberOfDevices:];
-[SBTelephonyManager _otherSubscriptionSlotIfSIMPresent:];
-[SBTelephonyManager _secondarySubscriptionInfo];
-[SBTelephonyManager displayedCall];
-[SBTelephonyManager containsCellularRadio];
-[SBTelephonyManager isEmergencyCallActive];
-[SBTelephonyManager _primaryMobileEquipmentInfo];
-[SBTelephonyManager isTTYEnabled];
-[SBTelephonyManager cachedSlot1SIMStatus];
-[SBTelephonyManager _setCurrentActivationAlertItem:];
-[SBTelephonyManager _anySubscriptionSlotWithSIMPresent];
-[SBTelephonyManager disconnectCallAndActivateHeld];
-[SBTelephonyManager emergencyCallSupported];
-[SBTelephonyManager setCachedSlot2CountryCode:];
-[SBTelephonyManager initWithStateProvider:bluetoothController:systemStatusServer:lockdownManager:];
-[SBTelephonyManager _subscriptionSlotIfSIMPresent:];
-[SBTelephonyManager toggleBargeCallState];
-[SBTelephonyManager _callsForService:];
-[SBTelephonyManager _serverConnectionDidError:];
-[SBTelephonyManager _secondarySubscriptionSlotIfEnabled];
-[SBTelephonyManager setNetworkRegistrationEnabled:];
-[SBTelephonyManager initWithStateProvider:wifiDomain:bluetoothController:lockdownManager:];
-[SBTelephonyManager _secondaryCarrierBundleInfoIfEnabled];
-[SBTelephonyManager setHeldCall:];
-[SBTelephonyManager setIncomingCall:];
-[SBTelephonyManager carrierDisabledApplicationIDs];
-[SBTelephonyManager setCachedSlot2SIMStatus:];
-[SBTelephonyManager faceTimeAudioCallCount];
-[SBTelephonyManager hasCellularTelephony];
-[SBTelephonyManager hasNonCellularNetworkConnection];
```
