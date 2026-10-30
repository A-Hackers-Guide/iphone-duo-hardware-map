# `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 6,927,328 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 209 (Size: 12960)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (32)

- `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore (compatibility version 1.0.0, current version 2319.52.2)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libbsm.0.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/LocalAuthenticationCredentialServices.framework/LocalAuthenticationCredentialServices (compatibility version 1.0.0, current version 2319.52.2)`
- `/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices (compatibility version 1.0.0, current version 1226.0.0)`
- `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices (compatibility version 0.0.0, current version 1153.2.2, weak)`
- `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices (compatibility version 1.0.0, current version 1084.40.7, weak)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices (compatibility version 1.0.0, current version 4637.1.14, weak)`
- `/usr/lib/libAccessibility.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/AppleMobileFileIntegrity.framework/AppleMobileFileIntegrity (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/TCC.framework/TCC (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/Combine.framework/Combine (compatibility version 1.0.0, current version 3023.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftSynchronization.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_Concurrency.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (390 classes, 218 protocols)

Classes: `LACACMHelper`, `LACACMParameter`, `LACACMParameterCollection`, `LACACMPoolInfo`, `LACACMPoolsInfo`, `LACACMRequirementTransformerFactory`, `LACACMTransformScopeMutable`, `LACADMUser`, `LACADMUserProvider`, `LACAKSHelper`, `LACAccessControl`, `LACAccessControlOperation`, `LACAgentProxyWithErrorHandler`, `LACAgentProxyXPCWrapper`, `LACAnalyticsContextManagementReporterProvider`, `LACAnalyticsData`, `LACAnalyticsProcessor`, `LACAnalyticsReporter`, `LACAnalyticsServiceXPCHost`, `LACAnalyticsSession`, `LACAnalyticsSessionClient`, `LACAnalyticsSessionXPCHost`, `LACAnalyticsTCCReporterProvider`, `LACAnalyticsUtils`, `LACAngelConnectionProvider`, `LACAngelHostedSceneConfiguration`, `LACAppProtectionAdapter`, `LACApplePayBiometryToggleProcessor`, `LACAuditToken`, `LACAuthenticationUIManagerComposite`, `LACAuthenticationUIManagerCustom`, `LACAuthenticationUIManagerDefault`, `LACAuthenticationUIManagerFactory`, `LACAuthenticationUINotificationCenter`, `LACAuthenticatorHelper`, `LACAutoLockServiceFactory`, `LACAutoLockStrictModeAdapter`, `LACBATS`, `LACBackgroundTask`, `LACBackgroundTaskErrorBuilder`, `LACBackgroundTaskQueued`, `LACBackgroundTaskResult`, `LACBiomeDialogDonationHelper`, `LACBiomeDialogEvent`, `LACBiomeEvaluationDonationHelper`, `LACBiomeEvaluationEvent`, `LACBiomeEvaluationMechanismState`, `LACBiometryHelper`, `LACBootArgParser`, `LACCache`, `LACCacheAsync`, `LACCacheSync`, `LACClientInfo`, `LACClientInfoProvider`, `LACCompanionAuthenticationController`, `LACCompanionAuthenticationCoordinator`, `LACCompanionAuthenticationEnvironment`, `LACCompanionAuthenticationProviderSharing`, `LACCompanionAuthenticationRequest`, `LACCompanionAuthenticationSessionMonitor`, `LACCompanionAuthenticationSignpostEvent`, `LACConcurrencyUtilities`, `LACConcurrentEvaluationConfiguration`, `LACConcurrentEvaluationController`, `LACConcurrentEvaluationHelper`, `LACConcurrentEvaluationManager`, `LACConcurrentIdleUIListenerProvider`, `LACContextCredentialCoder`, `LACCoreMotionAdapter`, `LACCoreRoutineAdapter`, `LACCredentialExtractablePasswordAuthorizerProvider`, `LACCryptoHelper`, `LACDTOAnalyticsEvent`, `LACDTOAnalyticsEventFactory`, `LACDTOAnalyticsProcessor`, `LACDTOAnalyticsService`, `LACDTOAppleAccountInfoProvider`, `LACDTOBiometryWatchdog`, `LACDTOBiometryWatchdogPack`, `LACDTOCoreProcessor`, `LACDTODarwinNotificationsController`, `LACDTOEnvironmentProviderFactory`, `LACDTOError`, `LACDTOEvent`, `LACDTOEventBus`, `LACDTOExtendedPolicyProtectionProcessor`, `LACDTOFailureProcessor`, `LACDTOFeatureController`, `LACDTOFeatureEnablementMode`, `LACDTOFeatureEnablementModeCoder`, `LACDTOFeatureEnablementOptions`, `LACDTOFeatureRequirement`, `LACDTOFeatureRequirementQuery`, `LACDTOFeatureRequirementsDataSource`, `LACDTOGracePeriodState`, `LACDTOKVStoreMigrationController`, `LACDTOKVStoreValue`, `LACDTOLocationController`, `LACDTOLocationControllerFactory`, `LACDTOLocationMonitor`, `LACDTOLocationPrewarmController`, `LACDTOLocationPrewarmStrategy`, `LACDTOLocationProviderCRAdapter`, `LACDTOLocationProviderKVSAdapter`, `LACDTOLocationProviderModeDecorator`, `LACDTOLocationProviderTaskDecorator`, `LACDTOLocationServicesInfoProvider`, `LACDTOLocationState`, `LACDTOLostModeController`, `LACDTOLostModeProviderAKAdapter`, `LACDTOLostModeProviderKVSAdapter`, `LACDTOLostModeState`, `LACDTOMutableEnvironment`, `LACDTOMutableFeatureRequirements`, `LACDTOMutableFeatureState`, `LACDTOMutableKVStoreReadRequest`, `LACDTOMutableKVStoreWriteRequest`, `LACDTOMutableLostModeFetchRequest`, `LACDTOMutableNotificationAction`, `LACDTOMutableNotificationCategory`, `LACDTOMutablePolicyEvaluationRequest`, `LACDTOMutablePolicyEvaluationResult`, `LACDTOMutableSensorRepairState`, `LACDTOMutableSensorTrustState`, `LACDTOMutableTimerConfiguration`, `LACDTONotificationFactory`, `LACDTONotificationManager`, `LACDTOPendingPolicyEvaluationController`, `LACDTOPendingPolicyEvaluationFactory`, `LACDTOPendingPolicyEvaluationStore`, `LACDTOPolicyEvaluationController`, `LACDTOPolicyProcessorEmptyPasscode`, `LACDTORatchetEndpointProvider`, `LACDTORatchetHandler`, `LACDTORatchetManager`, `LACDTORatchetSEPInterface`, `LACDTORatchetSEPStateParser`, `LACDTORatchetState`, `LACDTORatchetStateComposite`, `LACDTORatchetStateMonitor`, `LACDTOSensorRepairStateProviderCRAdapter`, `LACDTOSensorRepairStateProviderDefaultsDecorator`, `LACDTOSensorRepairStateProviderFactory`, `LACDTOSensorRepairStateProviderNullAdapter`, `LACDTOSensorRepairStateProviderTaskDecorator`, `LACDTOSensorTrustController`, `LACDTOSensorTrustService`, `LACDTOSensorTrustStateProvider`, `LACDTOSensorTrustStoreKVSAdapter`, `LACDTOSensorTrustVerifier`, `LACDTOSensorTrustVerifyService`, `LACDTOServiceProcessor`, `LACDTOServiceXPCClient`, `LACDTOServiceXPCHost`, `LACDTOTelemetryReporter`, `LACDTOTimerConfigurationProvider`, `LACDarwinNotificationCenter`, `LACDefaultServiceSession`, `LACDevice`, `LACDeviceLifecycleManager`, `LACDeviceTreeReader`, `LACDomainStateDecorator`, `LACDomainStateProvider`, `LACDomainStateProviderBiometry`, `LACEligibilityHelper`, `LACEntitlementsChecker`, `LACEnvironmentDependencies`, `LACEnvironmentMechanism`, `LACEnvironmentMechanismBiometry`, `LACEnvironmentMechanismCompanion`, `LACEnvironmentMechanismUserPassword`, `LACEnvironmentServiceXPCHost`, `LACEnvironmentState`, `LACError`, `LACEvaluationEvent`, `LACEvaluationRequestDefault`, `LACEvaluationRequestPreflightProcessor`, `LACEvaluationRequestProcessorEmpty`, `LACEvaluationRequestProcessorFactory`, `LACEvaluationResult`, `LACExternalizedContextProvider`, `LACFlags`, `LACGlobalDomain`, `LACInstalledAppsCache`, `LACInstanceIDGenerator`, `LACInternalInfoParser`, `LACKeyBagMKBAdapter`, `LACKeyBagObserverCollection`, `LACKeyBagProvider`, `LACKeyBagStateProviderMKBAdapter`, `LACLocalBackoffCounter`, `LACLocalization`, `LACLocalizationUtils`, `LACManagedConfiguration`, `LACMaxBiometryFailureProcessor`, `LACMechanismTree`, `LACMobileGestalt`, `LACMutableCredentialRequest`, `LACMutableEvaluationEventValueActivity`, `LACMutableEvaluationEventValueBiometricStatus`, `LACMutableEvaluationEventValueBootstrap`, `LACMutableEvaluationEventValueCoachingFeedback`, `LACMutableEvaluationEventValueCompanionStatus`, `LACMutableEvaluationEventValueFailure`, `LACMutableEvaluationEventValuePasscodeStatus`, `LACMutableEvaluationEventValuePushButtonStatus`, `LACMutableEvaluationEventValueRatchetStatus`, `LACMutablePasscodeVerificationRequest`, `LACMutableSharedModeDataSourceRequestOptions`, `LACMutableXPCClient`, `LACNRDeviceMonitorAdapter`, `LACNWPathMonitorAdapter`, `LACOnenessController`, `LACOnenessEnvironmentProvider`, `LACOwnerInfo`, `LACOwnerInfos`, `LACPSAuthorizerComposite`, `LACPSAuthorizerDispatchDecorator`, `LACPSAuthorizerEntitlementsAdapter`, `LACPWDHelper`, `LACParamChecker`, `LACPasscode`, `LACPasscodeCollection`, `LACPasscodeFormatter`, `LACPasscodeHelper`, `LACPasscodeHelperPasscodeStateManagedSettings`, `LACPasscodeHelperPasscodeStateRepository`, `LACPasscodeHelperPasscodeStateSimulator`, `LACPasscodeMKBHelper`, `LACPasscodeUserHelper`, `LACPersistentStoreFactory`, `LACPhoneIntegrationController`, `LACPhoneIntegrationEnvironmentProvider`, `LACPhoneIntegrationSessionProcessor`, `LACPolicyUtilities`, `LACPreboardAMFIHelper`, `LACPreboardErrorBuilder`, `LACPreboardLauncher`, `LACPreboardUPPProfile`, `LACProcessingConfiguration`, `LACRemoteUIParams`, `LACSDKHelper`, `LACSecureData`, `LACSecureStorage`, `LACSecureStorageConfiguration`, `LACServiceAdapter`, `LACServiceBase`, `LACServiceLocator`, `LACServiceManagerBase`, `LACServiceXPCClient`, `LACServiceXPCEndpointProvider`, `LACSetUpStateProvider`, `LACSharedMode`, `LACSharedModeDataSourceDefaultsDecorator`, `LACSharedModeDataSourceFTRCAdapter`, `LACSharedModeDataSourceMSAdapter`, `LACSharedModeDataSourceNullAdapter`, `LACSharedModeDataSourceTaskDecorator`, `LACSharedModeDataSourceTaskDecoratorRuntime`, `LACSharedModePolicyCoordinatorACMAdapter`, `LACSharedModePolicyCoordinatorACMStorage`, `LACSharedModePolicyCoordinatorACMStorageRequest`, `LACSharedModePolicyCoordinatorACMStorageRequestFactory`, `LACSharedModePolicyTraitsManager`, `LACSharedModeProcessor`, `LACSharedModeService`, `LACSharingManager`, `LACSignpostEvent`, `LACStashedCredentialsProcessor`, `LACStopwatch`, `LACStorageError`, `LACStorageValueTransformer`, `LACStringHelper`, `LACSysUtility`, `LACTCCManager`, `LACThreadSafeCollection`, `LACThreadSafeDictionary`, `LACThreadSafeObject`, `LACThreadSafeQueue`, `LACTimer`, `LACUNManager`, `LACUNManagerProvider`, `LACUNManagerQueueDecorator`, `LACUNManagerSetUpDecorator`, `LACUNMutableNotification`, `LACURLOpener`, `LACUserInterfaceController`, `LACUserInterfaceNullAdapter`, `LACUserInterfacePresenter`, `LACUserInterfaceRemoteUIAdapter`, `LACUserInterfaceRequest`, `LACUserInterfaceRequestCoder`, `LACUserMembershipHelper`, `LACWeakBox`, `LACXPCClient`, `LACXPCConnectionBSAdapter`, `LACXPCConnectionConfigurationDefaultAdapter`, `LACXPCConnectionDefaultAdapter`, `LACXPCConnectionEndpointBSAdapter`, `LACXPCConnectionListenerBSAdapter`, `LACXPCInterface`, `_TtC23LocalAuthenticationCore10SerialTask`, `_TtC23LocalAuthenticationCore15LACDateProvider`, `_TtC23LocalAuthenticationCore16LACAutoLockStore`, `_TtC23LocalAuthenticationCore18LACAutoLockService`, `_TtC23LocalAuthenticationCore18LACAutoLockTrigger`, `_TtC23LocalAuthenticationCore18LACPasscodeMonitor`, `_TtC23LocalAuthenticationCore18LACPreboardStorage`, `_TtC23LocalAuthenticationCore19LACPasscodeVerifier`, `_TtC23LocalAuthenticationCore20LACTapToRadarService`, `_TtC23LocalAuthenticationCore21LACACMContextProvider`, `_TtC23LocalAuthenticationCore21LACAppCategoryAdapter`, `_TtC23LocalAuthenticationCore21LACPasscodeSuccessAge`, `_TtC23LocalAuthenticationCore21LACPreboardController`, `_TtC23LocalAuthenticationCore21LACPreboardUPPManager`, `_TtC23LocalAuthenticationCore22LACAutoLockWatchSignal`, `_TtC23LocalAuthenticationCore23LACAnalyticsTCCReporter`, `_TtC23LocalAuthenticationCore23LACAutoLockDeviceLocker`, `_TtC23LocalAuthenticationCore23LACAutoLockKeybagSignal`, `_TtC23LocalAuthenticationCore23LACAutoLockSnatchSignal`, `_TtC23LocalAuthenticationCore23LACAutoLockWatchMonitor`, `_TtC23LocalAuthenticationCore23LACBackgroundTaskEngine`, `_TtC23LocalAuthenticationCore23LACBiometryTypeProvider`, `_TtC23LocalAuthenticationCore24LACAutoLockAirPodsSignal`, `_TtC23LocalAuthenticationCore24LACAutoLockKeybagMonitor`, `_TtC23LocalAuthenticationCore24LACAutoLockNetworkSignal`, `_TtC23LocalAuthenticationCore24LACAutoLockPeriodTracker`, `_TtC23LocalAuthenticationCore24LACAutoLockSnatchMonitor`, `_TtC23LocalAuthenticationCore25LACAutoLockAirPodsMonitor`, `_TtC23LocalAuthenticationCore25LACAutoLockBackoffMonitor`, `_TtC23LocalAuthenticationCore25LACAutoLockBackoffTracker`, `_TtC23LocalAuthenticationCore25LACAutoLockBiometrySignal`, `_TtC23LocalAuthenticationCore25LACAutoLockNetworkMonitor`, `_TtC23LocalAuthenticationCore25LACDTOEnvironmentProvider`, `_TtC23LocalAuthenticationCore25LACOnenessSessionProvider`, `_TtC23LocalAuthenticationCore25LACPreboardStorageRequest`, `_TtC23LocalAuthenticationCore26LACAutoLockContextProvider`, `_TtC23LocalAuthenticationCore26LACAutoLockEvaluationCache`, `_TtC23LocalAuthenticationCore26LACAutoLockRecoveryTracker`, `_TtC23LocalAuthenticationCore26LACPreboardUseCaseProvider`, `_TtC23LocalAuthenticationCore26LACSeparationAlertsAdapter`, `_TtC23LocalAuthenticationCore27LACAutoLockAppContextSignal`, `_TtC23LocalAuthenticationCore27LACAutoLockBiometryVerifier`, `_TtC23LocalAuthenticationCore27LACAutoLockMigrationChecker`, `_TtC23LocalAuthenticationCore27LACAutoLockSilentUIDelegate`, `_TtC23LocalAuthenticationCore27LACPreboardPasscodeVerifier`, `_TtC23LocalAuthenticationCore28LACAutoLockAppContextMonitor`, `_TtC23LocalAuthenticationCore28LACAutoLockEvaluationRequest`, `_TtC23LocalAuthenticationCore28LACAutoLockTriggerController`, `_TtC23LocalAuthenticationCore29LACAutoLockNotificationAction`, `_TtC23LocalAuthenticationCore29LACAutoLockTapToRadarProvider`, `_TtC23LocalAuthenticationCore30LACAutoLockNotificationService`, `_TtC23LocalAuthenticationCore30LACCredentialAnalyticsReporter`, `_TtC23LocalAuthenticationCore30LACPreboardUseCaseProviderAMFI`, `_TtC23LocalAuthenticationCore30LACRunningBoardServicesAdapter`, `_TtC23LocalAuthenticationCore30LACUserDefaultsPersistentStore`, `_TtC23LocalAuthenticationCore31LACAutoLockCoreAnalyticsService`, `_TtC23LocalAuthenticationCore31LACAutoLockDisconnectionTracker`, `_TtC23LocalAuthenticationCore31LACAutoLockFeatureFlagsProvider`, `_TtC23LocalAuthenticationCore31LACAutoLockNotificationCategory`, `_TtC23LocalAuthenticationCore31LACDTOAnalyticsReporterLostMode`, `_TtC23LocalAuthenticationCore32LACConcurrentEvaluationAllowList`, `_TtC23LocalAuthenticationCore33LACAutoLockFamiliarLocationSignal`, `_TtC23LocalAuthenticationCore33LACEvaluationRequestRootProcessor`, `_TtC23LocalAuthenticationCore34LACAutoLockFamiliarLocationMonitor`, `_TtC23LocalAuthenticationCore34LACAutoLockOneTimeSignalAggregator`, `_TtC23LocalAuthenticationCore34LACPhoneIntegrationSessionProvider`, `_TtC23LocalAuthenticationCore35LACAutoLockPeriodicSignalAggregator`, `_TtC23LocalAuthenticationCore36LACAutoLockDailyAggregationScheduler`, `_TtC23LocalAuthenticationCore36LACDTOAnalyticsReporterLocationState`, `_TtC23LocalAuthenticationCore36LACDTOMutablePendingPolicyEvaluation`, `_TtC23LocalAuthenticationCore36LACPreboardACMContextProviderFactory`, `_TtC23LocalAuthenticationCore37LACACMRequirementTransformerComposite`, `_TtC23LocalAuthenticationCore37LACAnalyticsContextManagementReporter`, `_TtC23LocalAuthenticationCore37LACDTOAnalyticsReporterAutoEnablement`, `_TtC23LocalAuthenticationCore37LACEvaluationRequestCompoundProcessor`, `_TtC23LocalAuthenticationCore39LACCompanionAuthenticationProviderDummy`, `_TtC23LocalAuthenticationCore40LACDTOAnalyticsReporterFeatureEnablement`, `_TtC23LocalAuthenticationCore40LACDTOAnalyticsReporterRatchetEvaluation`, `_TtC23LocalAuthenticationCore40LACPasscodeRateLimitingEmbeddedPlatforms`, `_TtC23LocalAuthenticationCore41LACDTOAnalyticsReporterCollapseEvaluation`, `_TtC23LocalAuthenticationCore42LACCredentialExtractablePasswordAuthorizer`, `_TtC23LocalAuthenticationCore44LACPasscodeVerifierStrategyEmbeddedPlatforms`, `_TtC23LocalAuthenticationCore46LACCompanionAuthenticationSessionProviderDummy`, `_TtC23LocalAuthenticationCore50LACCompanionAuthenticationControllerPendingRequest`, `_TtC23LocalAuthenticationCoreP33_53C4CF2605483CE5CE76F1EC3A4D036F37LACConcurrentEvaluationManagedRequest`, `_TtC23LocalAuthenticationCoreP33_7C23A2E67F893FA563A4E1A97AE88CD340LACCompanionAuthenticationPendingRequest`, `_TtC23LocalAuthenticationCoreP33_90B816A50749E299DCEB0219728B5FAE18LACDTOEventBusTask`, `_TtC23LocalAuthenticationCoreP33_90B816A50749E299DCEB0219728B5FAE24LACDTOEventBusDispatcher`, `_TtCE23LocalAuthenticationCoreCSo8NSBundleP33_06C5009961CF12380B02F6187ECF79568Sentinel`

Protocols: `BKSAlternateSystemAppDelegate`, `BSServiceConnectionListenerDelegate`, `LACACMHelper`, `LACACMRequirementTransformer`, `LACACMTransformScope`, `LACADMUserProtocol`, `LACADMUserProviding`, `LACAccelerometerProviding`, `LACAgentProxyXPC`, `LACAnalyticsCollecting`, `LACAnalyticsContextManagementReporting`, `LACAnalyticsReporting`, `LACAnalyticsServiceXPC`, `LACAnalyticsSessionXPC`, `LACAnalyticsTCCReporting`, `LACAppProtectionProviding`, `LACAuthenticationUIEventHandling`, `LACAuthenticationUIManaging`, `LACAuthenticationUINotifying`, `LACAuthenticationUIProxy`, `LACAutoLockService`, `LACAutoLockStrictModeProviding`, `LACBackoffCounter`, `LACBootArgParsing`, `LACClientInfoProviding`, `LACClientRequest`, `LACCompanionAuthenticationControlling`, `LACCompanionAuthenticationCoordinating`, `LACCompanionAuthenticationEnvironmentProviding`, `LACCompanionAuthenticationProviderDelegate`, `LACCompanionAuthenticationProviding`, `LACCompanionAuthenticationRequestType`, `LACCompanionAuthenticationSessionMonitorObserver`, `LACCompanionAuthenticationSessionMonitoring`, `LACConcurrentEvaluationConfiguring`, `LACConcurrentEvaluationControlling`, `LACConcurrentEvaluationManagerObserver`, `LACConcurrentEvaluationManaging`, `LACConcurrentIdleUIHandling`, `LACConcurrentIdleUIListenerProviding`, `LACConcurrentIdleUIPresenting`, `LACConcurrentIdleUIXPCHandling`, `LACContextUIDelegate`, `LACCoreRoutineProviding`, `LACCredentialExtractablePasswordAuthorizing`, `LACCredentialRequest`, `LACCryptoHelping`, `LACDTOAnalyticsReporting`, `LACDTOAppleAccountInfoProviding`, `LACDTOEnvironment`, `LACDTOEnvironmentProviding`, `LACDTOEventBus`, `LACDTOEventHandler`, `LACDTOEventProducer`, `LACDTOFeatureControlling`, `LACDTOFeatureEnablementMode`, `LACDTOFeatureRequirements`, `LACDTOFeatureRequirementsDataSource`, `LACDTOFeatureState`, `LACDTOFeatureStateProviding`, `LACDTOKVStoreMigrationController`, `LACDTOKVStoreReadRequest`, `LACDTOKVStoreReader`, `LACDTOKVStoreWriteRequest`, `LACDTOLocationController`, `LACDTOLocationMonitor`, `LACDTOLocationMonitorDelegate`, `LACDTOLocationPrewarmController`, `LACDTOLocationPrewarmStrategy`, `LACDTOLocationProvider`, `LACDTOLocationServicesInfoProviding`, `LACDTOLostModeFetchRequest`, `LACDTOLostModeFetchService`, `LACDTOLostModeProvider`, `LACDTONotificationFactory`, `LACDTONotificationManagerDelegate`, `LACDTOPendingPolicyEvaluation`, `LACDTOPendingPolicyEvaluationController`, `LACDTOPendingPolicyEvaluationControllerObserver`, `LACDTOPendingPolicyEvaluationMutable`, `LACDTOPendingPolicyEvaluationStore`, `LACDTOPolicyEvaluation`, `LACDTOPolicyEvaluationController`, `LACDTOPolicyEvaluationControllerObserver`, `LACDTOPolicyEvaluationRequest`, `LACDTOPolicyEvaluationResult`, `LACDTORatchetHandler`, `LACDTORatchetSEPInterface`, `LACDTORatchetStateProvider`, `LACDTOSensorRepairState`, `LACDTOSensorRepairStateProvider`, `LACDTOSensorTrustService`, `LACDTOSensorTrustState`, `LACDTOSensorTrustStateProvider`, `LACDTOSensorTrustStore`, `LACDTOSensorTrustVerifier`, `LACDTOSensorTrustVerifyService`, `LACDTOServiceXPC`, `LACDTOServiceXPCClient`, `LACDTOServiceXPCEndpointProvider`, `LACDTOTelemetryReporting`, `LACDTOTimerConfiguration`, `LACDTOTimerConfigurationProvider`, `LACDarwinNotificationCenter`, `LACDarwinNotificationCenterObserver`, `LACDeviceLifecycleManaging`, `LACDomainFlagsProviderAutoLock`, `LACDomainFlagsProviderDTO`, `LACDomainStateProviding`, `LACEligibilityHelping`, `LACEnvironmentServiceXPC`, `LACEvaluationEventHandling`, `LACEvaluationEventValue`, `LACEvaluationEventValueActivity`, `LACEvaluationEventValueBiometricStatus`, `LACEvaluationEventValueBootstrap`, `LACEvaluationEventValueCoachingFeedback`, `LACEvaluationEventValueCompanionStatus`, `LACEvaluationEventValueFailure`, `LACEvaluationEventValuePasscodeStatus`, `LACEvaluationEventValuePushButtonStatus`, `LACEvaluationEventValueRatchetStatus`, `LACEvaluationRequest`, `LACEvaluationRequestProcessor`, `LACEvaluationRequestRootProcessing`, `LACFeatureFlagsCredentials`, `LACFeatureFlagsProviderAutoLock`, `LACFeatureFlagsProviderDTO`, `LACFlagsCredentials`, `LACFlagsProvider`, `LACFlagsProviderAutoLock`, `LACFlagsProviderDTO`, `LACGlobalDomain`, `LACGlobalDomainAutoLock`, `LACGlobalDomainDTO`, `LACGlobalDomainPreboard`, `LACKeyBag`, `LACKeyBagObserver`, `LACKeyBagProvider`, `LACManagedConfiguration`, `LACNRDeviceMonitorAdapter`, `LACPSAuthorizer`, `LACPasscodeHelperPasscodeState`, `LACPasscodeObserver`, `LACPasscodeRateLimiting`, `LACPasscodeVerificationRequest`, `LACPasscodeVerifying`, `LACPersistentStore`, `LACPreboardControlling`, `LACReachabilityProviding`, `LACRemoteContext`, `LACRemoteContextProviding`, `LACRemoteUI`, `LACRemoteUIClientProtocol`, `LACRemoteUIHost`, `LACRemoteUIServerProtocol`, `LACRequest`, `LACSecureStorageDelegate`, `LACSecureStorageType`, `LACService`, `LACServiceLocator`, `LACServiceManager`, `LACServiceSession`, `LACServiceXPCEndpointProvider`, `LACSetUpStateProvider`, `LACSharedModeDataSource`, `LACSharedModeDataSourceRequestOptions`, `LACSharedModePolicyCoordinator`, `LACSharedModePolicyCoordinatorACMStorage`, `LACSharedModePolicyTraitsManager`, `LACSharedModeService`, `LACSharingManagerDelegate`, `LACSharingManaging`, `LACStorageRequest`, `LACSysUtilityType`, `LACTCCManaging`, `LACTimer`, `LACUIMechanism`, `LACUNManager`, `LACUNManagerDelegate`, `LACUNNotification`, `LACUNNotificationAction`, `LACUNNotificationCategory`, `LACURLOpener`, `LACUserInterface`, `LACUserInterfaceConnectionProviding`, `LACUserInterfaceController`, `LACUserInterfacePresenting`, `LACUserServiceXPC`, `LACXPCClient`, `LACXPCConnection`, `LACXPCConnectionConfiguration`, `LACXPCConnectionDelegate`, `LACXPCConnectionEndpoint`, `LACXPCConnectionListener`, `MCProfileConnectionObserver`, `NRDeviceMonitorDelegate`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`, `RBSProcessMonitorConfiguring`, `SFAuthenticationManagerDelegate`, `UNUserNotificationCenterDelegate`, `_TtP23LocalAuthenticationCore25LACAutoLockKeybagObserver_`, `_TtP23LocalAuthenticationCore26LACAutoLockWatchMonitoring_`, `_TtP23LocalAuthenticationCore27LACAutoLockKeybagMonitoring_`, `_TtP23LocalAuthenticationCore27LACAutoLockSnatchMonitoring_`, `_TtP23LocalAuthenticationCore28LACAutoLockAirPodsMonitoring_`, `_TtP23LocalAuthenticationCore28LACAutoLockNetworkMonitoring_`, `_TtP23LocalAuthenticationCore31LACAutoLockWatchMonitorObserver_`, `_TtP23LocalAuthenticationCore32LACAutoLockSnatchMonitorObserver_`, `_TtP23LocalAuthenticationCore33LACAutoLockAirPodsMonitorObserver_`, `_TtP23LocalAuthenticationCore33LACAutoLockNetworkMonitorObserver_`, `_TtP23LocalAuthenticationCore36LACAutoLockAppContextMonitorObserver_`, `_TtP23LocalAuthenticationCore37LACAutoLockFamiliarLocationMonitoring_`, `_TtP23LocalAuthenticationCore42LACAutoLockFamiliarLocationMonitorObserver_`

## Strings (7,838)

First 2,500 of 7,838.
```
Fetching Mac companion assertion
Stashed credentials processor skipping rid: %{public}u — preflight did not return notInteractive
Initiating canAuthenticate call for companion:%{public}@
Scheduled notification for evaluation: %{public}@ after: %.2f secs
Disabled %s signal
Failed to persist backoff state: %s
%{public}@ Not handling request rid: %{public}u - feature not supported
Loaded persisted auto-lock timestamp: device has been locked for %fs
Created %{public}@
ACMContextCreateWithFlags rc=0 (after retrying on rc=%d).
Skipping biome donation because D&U flag is disabled
%{public}@ Biometry is not replaceable by companion for request: %{public}u error: %@
Companion authentication finished for session: %{public}s but there is no pending authentication for it
Starting Watch connectivity monitoring
isFeatureStrictModeEnabled: %s
Auto-lock trigger attempt but blocked by backoff
Separation alerts not available - cannot start monitoring
Authentication for bundleID: %{public}@ app name: %{public}@ companion:%{public}@ returned: %{public}@
Ignoring notification response for unknown action: %s
Auto-lock trigger dismissed: device already locked
Environment variable set failed with error: %@
Keybag signal not enabled, voting NO
Pruning invalidated evaluations
DTOEnvironmentUpdate
%{public}@[%u] %s visible
Started Watch signal monitoring
Auto-lock network monitor initialized
Stopped app-context signal
ACMContextCreateWithExternalForm returned NULL.
Ignoring notification response for unknown category: %s
Device identifier creation failed: %{public}@
Identities updated from %{public}@ to %{public}@
Update keybag state. Current one: %@
Failed to query process states
The pending evaluation for %@ is using the existing cool off timestamp: %@
%s - feature is not supported
Unexpected processing result during post-processing: %@
Connected to %{public}@ for contextUUID: %{public}@
%@ replied with %s to event: %@
%{public}@ Tree: %@ %s satisfiable by %ld
Familiar location signal not enabled - LOCK
%{public}@ Cancelling request: %{public}s during preprocessing
Unable to find bundle record for audit token error: %@
Skipping sensor trust alert on client's request
Network status changed from %@ to %@
AMFIProfileCommitProfile returned: %d
Checking ACM credential %d on ACMContext %u
Filing radar for auto-lock false positive report
Cancelling requests: %{public}s
UPP install succeeded
Unknown path status: %d
isFeatureStrictModeEnabled: NO (%{public}@)
Auto Enablement: NO (%{public}@)
Using mocked use case: %ld
Failed to create extractable password for rid: %{public}u
%s: %s: CS[%u] deleted (contextDestroyed=%s).\n
Keybag state %@ is equal to new state %@. Ignoring...
Could not fetch feature strict mode status (%{public}@)
Updated pending evaluations after significant time change: %@
%{public}@ Did start companion session with id: %{public}s for request %{public}u
Sysctl security.codesigning.config failed with error code: %d global error: %d
Keybag state updated. New one: %@
%@ mapping error %@ to success
%@ UI dismissed with error: %{public}@
isFeatureAvailable = isFeatureEnabled = YES
extended policy update failed: %{public}@
AppProtection available - locked apps: %@
Can't query Face ID landscape.
Failed to decode backoff state: %s
Start date (%s) must not be after end date (%s)
ACM requirement for policy %{public}s (satisfied: %d): %{public}@
Unable to clean storage with error: %@
%{public}@ finished
%{public}@ - user responded to new security delay required notification %{public}@ with action %{public}@
AirPods became SEPARATED
%{public}@ Processed result for rid: %{public}u original: %@, processed: %@
Handling new keybag state: %s
Preboard did not launch with error: %{public}@
Posted notification with content: (%@) identifier: %@)
Cancelling all notifications
bioLockoutState failed: %{public}@
Ratchet state changed from: %{public}@ to %{public}@
deviceHasPearl returned %d
Signal triggered: %s. New evaluation run: %s
%{public}@ Not preflying request: %{public}s - not interactive evaluation
ACMParameter length overflow
Stopped analytics service and daily aggregation scheduler
Updated: %{public}@
%{public}@ Companion authentication failed for session: %{public}s with error: %@
Determined path for PID %d: %{public}@
MKB device unlock for keybag %d returned %d
Failed to persist current %s period start: %s
Persisted pending evaluations %s
%@ not processing dismiss message for rid: %u - id does not match %u
%{public}@: no session for authentication action
Will simulate companion authentication success
%{public}@ Not handling request rid: %{public}u - session not active
User present: %{public}@
%{public}@ %@ replaced error: %@ with concurrentBiometryAndCompanion option
No genre available for %s (1P or sideloaded)
Recovery event sent: lockedTime=%ld, unlockMechanism=%ld
Device became UNLOCKED
Loaded pending evaluations %s
Will present UI for %@
Auto enablement is not allowed (%{public}@)
Stashing a LACredentialTypeExtractablePassword requires the '%s' entitlement
%{public}s retrying stashed request rid: %u
%@ created for rid: %u
%{public}@ Request: %{public}s not cancelled because it is already evaluating
%@ Custom UI replied for rid: %u to event (%s) with params: %{public}s
Enabling protected option for usecase: %ld
AppProtection not available - no locked apps
Data exchange for key: %ld failed: %@
Failed to get process handle for %{public}@[%u]: %{public}@
Donating %@ to %@
Allocated: %@, receiver: %@
Legit user confirmed - DON'T LOCK
Did exchange data: %s for key: %ld
AMFIProfileSetTrustWithOptions returned: %d
Accelerometer not available on this device
%{public}@ %@ failing immediately because user explicitly cancelled authentication on companion
Adding DTO option for policy
%@ refreshing availability
Auto-lock trigger attempt but blocked during migration
Started network reachability monitoring
deviceSupportsSecureDoubleClick returned %d
camera rotation: %d
connectSessionForContext:%{public}@ on %{public}@: %{public}@
%@ did refresh availability to %{bool}d
Device connected (WiFi fallback) changed: %{public}@
%{public}@ starting monitor with an interval of %.2f secs with reason: %{public}@
%{public}@: no session for updated context
Connection failed with error %{public}@
Returning cached value: %s
Uninterruptible app %s - deferring auto-lock
Preboard exited with code: %d
Snatch cooldown period ended, monitoring resumed
Vision fetching companion session state skipped - companion not available
Could not get Bluetooth identifier from paired Watch
%{public}@ Policy update for shared mode finished err=%{public}@
isExtendedPolicyProtectionEnabled: %s
Auto-lock notification service initialized
Starting familiar location monitoring
Rebooting device with reason: %@
supportsFaceIDLandscapeMatching returned %d
Skipping cancellation of pending evaluation with reason: %@, identifier: %@
UserID: %@ does not meet requirements of authenticator: %ld - %s
Active requests count: %ld
Failed to get audit token for PID %u
%{public}@ will use strict mode value %@
Cancelling existing auto-lock notifications
LACEvaluationRequestRootProcessor was deinitialized
LACBackgroundTaskEngine(%{public}s) handler queued with timeout %fsecs
No frontmost user app found
OneTimeSignal event sent: type=%ld, occurrences=%ld
%{public}@ started
Unable to get audit token from data
Will remove pending evaluation with identifier: %@
finishSession for %{public}@: %{public}@
isExtendedPolicyProtectionEnabled: NO (%{public}@)
RBSProcessEverythingPredicate not available
Environment query will start
%s (%s)
Can authenticate check started with sessionID:%{public}@
Policy evaluation did finish: %@
Did register observer %@
AirPods reconnected
AirPods monitoring unavailable / not yet determined
MKBUserTypeDeviceMode returned NULL: %{public}@
Setting ACM envrionment variable: %d
Policy verification failed: %d
%@ Did refresh availability isAvailable: %{bool}d
RBSProcessEverythingPredicate not available for synchronous query
%{public}@ No pending request for rid: %{public}u
%@ No parameters to be sent to custom UI for event %ld (%s)
%{public}s canceling stashed request: %u
Interruption invoked in service: %@
Committing UPP profile value: nil with result: %u
Strict mode enabled, all locations untrusted - LOCK
Unable to unarchive application identity error: %@
Cannot interact with UserNotifications at the moment.
isFeatureAvailable: YES
Preprocessing value completed (%{private}@)
Daily aggregation scheduler already running
Keybag state changed: %s
Unable to launch preboard as the feature is not supported
Skipping redundant repair checks
Sensor trust verification finished with code: %{public}@
Returning cached value: %{bool}d
%{public}@ Obtained TUCallCenter endpoint %@
Performing daily aggregation report
Starting AirPods separation monitoring
Starting keybag monitoring
%{public}@: no context for session update
exchangeData rid:%u returned %{private}@
DTORepairStateQuery
Auto-lock trigger attempt but disabled for %s
Failed to persist %s periods: %s
Failed to load backoff state: %s
Companion authentication failed for session: %{public}s with error: %@ but there is no pending authentication for it
%{public}@ No requests to cancel for contextID: %{public}s
Deferred lock resolved - triggering re-evaluation
Could not bootstrap service with type: %{public}@ (%{public}@)
%{public}@ Did stop listener for AKS events
Connect idle UI for rid: %u
Can't query OpticID.
Will add new pending evaluation with identifier: %@
%{public}@ performing scheduled query
Mac Companion session subscriber does not exist
Disabled keybag signal monitoring
Starting deferred monitoring for %s
%@ XPC target UID: %u (UI)
Signal monitoring blocked: device is in setup/migration state
AirPods signal not enabled, voting NO
ACMParameter: %@ data length exceeds UINT32_MAX
Determined localized name for bundle %{public}@: `%{public}@`
CompanionAuthenticationRequest
Destroying idle UI for %s because the request does not allow idling UI
DTOLostModeStateResult
Does not need pending evaluation record for '%@' after success
Connection accepted for non-tracked listener: %@ in service: %@
Migration of key: %{public}@ did finish successfully
%{public}@ will start query with '%@' strategy
Force disabling usage of LACPolicyOptionFallbackToNoAuthentication for this policy
Watch became UNREACHABLE
Skipping UI for %@ rid: %{public}@, not interactive evaluation
CMMotionManager not available
%{public}@ has merged %{public}@
Protected app foreground: %s - LOCK
Network became REACHABLE
%{public}@ - sending Expired on prune
TXM boot mode %ld
No active request for %{public}s rid: %u to remove
Watch became REACHABLE
%{public}@ Continuity unlock not available for request: %{public}u error: %@
Did register observer %@ of notification %@
%@ did remove observer %@
updateContext:%{public}@: %{public}@
Snatch signal not enabled, voting NO
Returning cached eligibility result: %{bool}d for domain: %s
%{public}@ Post-processing request: %{public}s with result: %s
%@ -> %s
Added client to service: %@ clientID: %@
%s returned %s, error: %{public}@
%s options:%@
%{public}@ did finish query with error: %{public}@
Failed to create NWPathMonitor
Evaluation request %s deallocated
Started keybag monitoring
Prewarm skipped because feature is disabled
Restarting security delay for invalidated evaluations
%{public}@ Did not start listener - provider not available
No requests to cancel for contextID: %{public}s
%s: %s: log level set to %d.\n
hasCompletedSetup: %@
%{public}@: no session for failed authentication attempt
Adding observer %{public}s for request rid: %{public}s
%{public}@ Skipping presentation of failure UI for rid: %{public}u. No failure UI option.
%{public}@ feature not supported in this platform %{public}@
Replacing ACM passphrase credential with purpose %d on ACMContext %u
authenticationAction:%{public}@ failing:%d for %{public}@: %{public}@
%{public}@ Companion not available for request: %{public}u error: %@
Watch signal not enabled, voting NO
Cancelling stashed request %{public}s because a new request for session %s is registered
Unable to get externalized context
%s returned %d
%@ No UI delegate to send custom UI event %ld (%s)
isFeatureEnabled: NO (error: %{public}@)
%@ DSLMode changed from: %@ to %@
Will notify %d observers about new state: %{public}@
Device created successfully with type: %@
%{public}@ did set traits = [%{public}@] err=%{public}@
Not adding new pending evaluation with identifier: %@, the evaluation is invalidated
Reused session service: %@ clientID: %@
setObject rid:%u returned %{public}@
Ignoring redundant finish request (%{public}@)
Does not need pending evaluation record for '%@' after user cancel
Cooldown expired
Daily aggregation report complete
Biometric check only for Face ID (current: %ld)
TXM boot mode returned value: %d error: %d global error: %d
Can't query SecureDoubleClick.
AirPods are CONNECTED
LACBackgroundTaskEngine(%{public}s) started worker
Device monitor created
AppProtection query failed: %{public}@
Persisted backoff state (strikes=%ld)
Fetching paired devices for companion:%{public}@
%{public}@ falling back to %{public}@ because the TUCallCenter endpoint was nil
Did create notification manager
Backoff tracker: loaded persisted state (strikes=%ld - cooldown expiration=%s)
Releasing device monitor
isFeatureEnabled: YES
Auto-lock AirPods monitor initialized
Received unexpected modification timestamp data %@ length: %d
exchangeData forKey:%d rid:%u
%{public}@ Companion session updated isActive: %{bool}d. Informing observer %s
Prewarm skipped because sensor is trusted
ACM requirement transformed for ACL operation %{public}@: %{public}@
Not restarting security delay - no invalidated evaluations
%{public}@ found %{public}@ %{public}s
DTOLostModeQuery
 enableTelemetry=YES  rc=%{public,signpost.telemetry:number1,name=rc}d  ts=%{public,signpost.telemetry:number2,name=ts}d 
Received unexpected time since boot data %@ length: %d
Failed to load trigger timestamp: %s
Ignoring stale completion (generation %lu != %lu)
Initiating companion authentication for bundleID: %{public}@ app name: %{public}@ companion:%{public}@
Did not schedule notification for evaluation: %{public}@ due to error: %{public}@
Aggregated %ld %ld periods: min=%fs (%ld), avg=%fs (%ld), max=%fs (%ld)
Failed to clear trigger timestamp: %s
Failed to create context: %s
%{public}@ Unable to determine shared mode status due to missing dependencies
Querying familiar location status
Stopped Watch signal monitoring
Failed to persist pending evaluations with error %{public}@
Keybag state changed from %@ to %@
Persisted current %s period start: %s
%{public}@ Using mocked session provider
Stashed credentials verification for rid: %{public}u result: %ld
Loading pending evaluations
Deallocated service: %@ clients: %ld vended listeners: %ld
MKB stash creation finished with rc=%d (mode=%d, manifest=%d)
enableFeatureWithOptions: strict mode enable failed (non-fatal): %{public}@
<<< Not triggering auto-lock for %s, ABSTAINED by %s (signal not relevant)
%{public}s no stashed record for request rid: %u
%s context:%{public}@ options:%{public}@
Committing developer mode value: %u with result: %u
%@ failed to persist location state: %@
No active request for %{public}s rid: %u to stash
Will schedule notification %{public}@ for %{public}@
Mac Companion assertion is active: %{bool}d
Vision companion session is active: %{bool}d
%s: %s: returning, err = %ld, code=%u.\n
Should trigger auto-lock? %{bool}d
Unregistering request %{public}s
Vended service endpoint: %@ for service: %@
Skipping notification for security delay restart migration: %d, unlock: %d
App-context signal not enabled - LOCK
%{public}@ did finish query with error %{public}@
Biometric liveness verified via enrollment date (threshold: %.0f)
>>> Evaluating %s for triggering signal: %s
%s: %s: returning.\n
Registered session service: %@ client: %@
%{public}@ created: %{public}@
Starting reachability monitoring
Did receive notification %{public}@
%{public}@ Preflight for request: %{public}s finished with error: %@
%@ vending a new listener %@
Enabled biometry signal
Passcode verification request %{public}s will start
Did not post notification for security delay restart error: %{public}@
Could not parse tree: %s
%{public}@ Unable to create authentication request
Failed to create secure copy of passcode: %{public}@
Preboard terminated with signal: %d
%{public}@ Cannot process request: %{public}s, no such pending request
%{public}@ will perform query with %.2f sec timeout
Did show UI with error: %@
%{public}@[%u] is not running scheduled, task state: %u
Failed to encode %@: %@
Unable to load pending evaluations with error: %{public}@
Snatch detected! Applied G-force: %fG over threshold: %fG
Eligibility call for domain: %s returned result: %llu
Authentication with Vision Pro is available only for Face ID devices
%{public}@ Tree: %@ and value %ld %s replaceable by %ld
Did dismiss UI for %@ with error: %@
No pending request for rid: %i
%@ did receive passcode changed notification
%@ no queued event
%{public}@ Continuity unlock not satisfiable for request: %{public}u error: %@
Listener timed out without connection: %@ for service: %@
Visit event received
UPP install failed with error: %@
%{public}@ failed with background task error %{public}@. Resolving to unknown repair state.
Scheduling next daily report in %fs at hour %ld
State didn't change, keybag is still %s
Failed to find LSBundleRecord: %@
Stopping familiar location monitoring
Evaluating FaceID policy
Deallocated session service: %@ clientID: %@
Will start location prewarm
Environment variable set succeeded
Successfully cleaned storage
Could not create device identifier
Determined localized name for path %{public}@: `%{public}@`
backoff: %{public}@
Can't merge %{public}@ into %{public}@, data is not tracked by this session.
Disabled biometry signal
%{public}@ Removing %d option because user %d has passcode
%{public}@ failed err=%{public}@
Auto-lock trigger attempt but disabled by master flag
Extracting a LACredentialTypeExtractablePassword after %ld secs requires the '%s' entitlement
%@ received a new connection %@ for listener %@
batchOptions semaphore timed out.
Can authenticate failure for sessionID:%{public}@ error:%{public}@
%{public}@ stopping monitor with reason: %{public}@
ACM requirement transformed for policy %{public}s: %{public}@
Setting secret to passcode stash on ACMContext %u
Passcode verification failed
Threshold elapsed — Watch still unreachable, triggering signal change
%{public}s setting disableConcurrentEvaluation to %{bool}d
Migration of key: %{public}@ did fail (error=%{public}@)
Failed to get protected configuration for user %{public}@: %{public}@
Not monitoring - ignoring stop request
NanoRegistry or NetworkRelay framework not available
Could not post notification %{public}@ (error:=%{public}@)
setObject rid:%u returned %{private}@
%{public}@ deallocated
Allocated session service: %@ clientID: %@
Auto-lock attempt failed
No authentication to cancel
Created context for FaceID evaluation
Watch reconnected
%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n
Did receive notification: %@
Did post notification %{public}@
Stopped snatch monitoring
Hosted scene requested by: %@
Vision companion session listener subscribed
Unable to enable protected option as the feature is not supported
Rebooting because PreBoard failed to complete current boot mode
deviceHasTouchID returned %d
No stashed request
Stashed credentials processor skipping rid: %{public}u — no mechanism tree in preflight error
Passcode verification failed with code: %d
Deferred app lost foreground - resolving deferred lock
Subclasses of %@ must provide an `exportedInterface`
CanAuthenticate for companion:%{public}@ returned: %{public}@
Paused network monitoring
%{public}@: no session for successful authentication
%@ Sending custom UI for rid: %u event (%s) with params: %{public}s
Sensor trust verification will start
Started %{public}@ for contextUUID: %{public}@
isFeatureSupported: NO (%{public}@)
Failed to persist %s disconnection count: %s
%{public}@ Will preflight request: %{public}s
%{public}@ Unable to determine shared mode status due to missing dependencies %{public}@
%{public}@ Will finish processing of request: %{public}s
%{public}@ %{public}@
%@ will start query
Missing identifiers to register request rid: %u
Passcode verification request did finish: %{public}ld
%{public}@ Companion authentication controller already deallocated
Disabled network signal monitoring
Re-fetching state
Could not fetch feature available status (%{public}@)
%{public}@ did finish self-repair query with result %@
Could not fetch user disablement status (%{public}@)
%{public}@ Cannot preflight request: %{public}s, no such pending request
No client available for rid: %{public}u
Could not fetch LocationServices status %{public}@
Finishing %{public}@
isExtendedPolicyProtectionAvailable: %s
%@ isActive: %{bool}d
%{public}@ - not handling notification %{public}@
Does not need pending evaluation record for '%@' for current ratchet state: %@
authenticationStartedForEvent:%{public}@ for %{public}@: %{public}@
Missing ACM context
%{public}@ Companion session is not active, evaluating right away
%s: %s: returning, -> ctx = %p.\n
%s: %s: returning, err = %ld, var=%u.\n
Resumed network monitoring
Requested termination of service: %@
%{public}@
Failed to create LSApplicationIdentity from %@
%s finished with error: %{public}@
%{public}@ did finish query with value: %@
Skipping trust state update because trust can only be regained in SEP
Mac Companion session listener unsubscribed
%@ handles event: %@
Vision companion session subscriber does not exist
No frontmost app
companionForUser:%u type:%d -> %{public}@
%@ dumping event queue
%@ will dealloc
Posting auto-lock notification
Removing observer %{public}s for request rid: %{public}s
Uninterruptible app foreground: %s - DEFER
Performing ratchet state query
%@ Invalidated
%{private}s
Persisted %ld %s periods
Repeating timers with zero length are not supported
%s identifier:%{public}@, reason:%{public}@
Biometric attempt notification finished with status (%d)
ACMContextCreateWithFlags rc=%d.
%{public}@ Will cancel companion authentication for session: %{public}s
%{public}@ Cannot stop monitoring, no AKS listener registered
Prewarm skipped because device has not finished setup
Completing boot mode: %u with result: %u
%{public}@ will skip query because current ratchet state allows it
Temporarily waiving access requirements
%s
%{public}@ - sending Completed for %{public}@
Prewarm skipped because keybag is not unlocked
Failed to persist trigger timestamp: %s
AirPods not being monitored (no paired AirPods) - voting `no`
Started AirPods separation monitoring
Watch not being monitored (no paired Watch) - voting `no`
User %{public}@ is locked out: %{public}@, purpose:%d
%@ Activated
startSessionForContext:%{public}@ dialogID:%{public}@ bundleID:%{private}@ on %{public}@: %{public}@
%{public}@ query finished with error %{public}@
New state (%@) informed to observer: %@
Failed to determine task name for PID %u
Is unlocked? %{bool}d - Is %fs threshold met after %fs? %{bool}d = Result %{bool}d
AKS get device state returned non-zero result: %d
The pending evaluation for %@ has no cool off timestamp yet
checkCanEnableFeature: YES
%{public}@ did finish query %@
Can't query Touch ID.
%@ ignoring update to %@, state unchanged
Started analytics service with daily aggregation scheduler
Failed service bootstrap serviceType: %@ clientID: %@ error: %@
Setup checks are not available due to missing dependencies
Snatch detected (%fG) - triggering signal change
Auto-lock trigger controller initialized
Recorded auto-lock trigger at %s
Could not fetch HSA2Account (%{public}@)
Biometry verifier initialized
Stashed credentials missing for rid: %{public}u
Can authenticate success for sessionID:%{public}@
%{public}@ is now tracking %{public}@
Could not fetch biometric liveness (%{public}@)
Missing identifiers to stash request rid: %u
Actively served requests count: %ld
%@ configured with unsupported configuration object %@
Failed to start network monitoring: Work queue cannot be NULL
%{public}@ Missing client info
No requests to retry for contextID: %{public}s
objectForKey rid:%u returned %{private}@
Successfully posted auto-lock notification
There is another stashed request for sessionID: %{public}s
Injected LACPolicyOptionCheckApplePayEnabled rid: %u
Informing %{public}s about unstashing of request %{public}s
Invalid string (%@)
Started familiar location signal
Stashed credentials processor skipping rid: %{public}u — passcode not required or satisfiable in mechanism tree: %@
Prewarm skipped because strict mode is enabled
Unable to load pending evaluations, ratchet state failure: %{public}@
Missing BiomeLibrary dependencies
Failure alert did disappear (err: %@)
Eligibility call for domain: %s failed with status code: %d
Failed to convert payload to NSObject dictionary for event: %s
%@ Failed to externalize context with error: : %@
Unable to complete boot mode with error: %@
TCC access request for %@ returned %@
The pending evaluation for %@ will use the current time for cool off timestamp: %@
Restarting remote UI
Stopped daily aggregation scheduler
Started app-context signal
There are more than one requests for contextID: %{public}s
dropAllUnlockTokens failed: %{public}@
%{public}@ will start self-repair query
Did remove observer %@
%{public}@ Cancelling requests: %{public}s for contextID: %{public}s
%{public}@ Cannot authenticate request: %{public}s, no such pending request
Idle UI for rid: %u got focus
Failed to get pool info from ACM: %d
LACBackgroundTaskEngine(%{public}s) worker will deliver result to %ld handlers
BKSAlternateSystemApp not available
%{public}@ - will handle notification action %{public}@
Does need pending evaluation record for '%@' for current ratchet state: %@
Migration of key: '%{public}@' will start
Listing eligible devices returned: %@
%{public}@ will use cached value %@
Failed to register agent proxy: %{public}@
Adding ACM credential %d for scope %d on ACMContext %u
Accelerometer error: %{public}@
No periods to aggregate for %ld
Stopping AirPods separation monitoring
TCC access request for %@ returned error: %@
processError rid:%u returned %{private}@
<<< Triggering auto-lock for %s, TRIGGERED by %s
Failed to encode %s periods
Verifying ACM requirement %d using policy %s %{public}@ on ACMContext %u
New keybag state: %s
LACBackgroundTaskEngine(%{public}s) timeout handler ignored: %{public}s
LACEValuationRequestCompoundProcessor was unexpectedly released during post-processing
%{public}@ will start query
Cancelling notifications with identifiers: (%@)
Auto-lock trigger successfully executed
Could not fetch current configuration (%@). Falling back to default
XPC connection to LACDTOServiceXPC endpoint closed
Did finish location prewarm with result: %{public}@
%{public}@ Not handling request rid: %{public}u - authenticator not available
No paired Watch found - cannot start monitoring
Watch reachable status update: %{bool}d
Unable to fetch UPP profile
Request %{public}s already stashed
%s: %s: called.\n
removeObjectForKey rid:%u returned %{private}@
Registering request %{public}s with sessionID: %{public}s
%s: %s: CS[%u] created (flags=0x%x).\n
Successfully acquired audit token for PID %u
Finishing Preboard with reason: %s success: %{bool}d
%{public}@ did finish
Failed to read identities: %@
Mac Companion session listener subscribed
%@ skipping persist, rawValue unchanged: %@
Can't query Face ID.
%@ did finish query %@
Failed to create secure password: %@
%{public}@ Failing request: %{public}s with error: %@ - Authentication not supported
Preboard activated
Sysctl security.codesigning.monitor failed with error code: %d global error: %d
Canceling authentication for sessionID: %{public}@
Requested hard reboot with result: %d
%{public}@ will set traits = [%{public}@]
Schedule ratchet state check in %.2f
Canceling requests with UUID %{public}s
%@ ZDR is disabled. Falling back to previous location value
Started familiar location monitoring
Started Watch connectivity monitoring
App context: %s - allowing auto-lock
Resetting ratchet with reason: %{public}@
Failed to create context for security delay restart: %{public}@
Sensor trust verification did finish with result: %@
Failed to look up app record for %s: %@
Auto-lock trigger blocked: signal %s flag is OFF
Mapping unapproved sensor error %{public}@ to success on client's request
Informing %{public}s about canceling of request %{public}s
Removed client from service: %@ clientID: %@
%{public}@ failed %{public}@
%{public}@ - user tapped security delay ended notification %{public}@
%{public}@ Starting listener for session monitoring
Removing ACM credential %d on ACMContext %u
Pruning pending evaluations with uuid: %{public}@
Not eligible for authentication with Vision Pro
Unable to retrieve LACRemoteContext - LOCK
Network became UNREACHABLE
Could not fetch extended policy protection status (%{public}@)
%{public}@ Preflight for request: %{public}s finished with success
Cleared pending auto-lock timestamp
Stopping Watch connectivity monitoring
enableFeatureWithOptions: caller is missing entitlement '%{public}@', enabling with grace period instead
MKB password verification for keybag %d returned %d
Invalid requirement flags: %p[%zu]
authenticationAttemptFailedForEvent:%{public}@ for %{public}@: %{public}@
Failed to post notification: %@
Resolved genre for %s: %s
%{public}@ Did start companion authentication for request %{public}u
Enabled network signal monitoring
Did receive response for notification %{public}@
Auto-lock notification blocked: Wrong signal
Cleared current %s period start
Reseting Ratchet as there are no pending evaluations
objectForKey:%d rid:%u
User didn't pass biometry: %s
%{public}@ did finish query with error: (%{public}@)
Environment query did finish env=%s, err=%s
%{public}@ Companion authentication successfully finished for session: %{public}s
Allocated service: %@
Skipping notification for '%@' — evaluation is currently active (after: %.2f, validity: %.2f)
%{public}@ Cannot finish processing of request: %{public}s, no such pending request
LACBackgroundTaskEngine(%{public}s) handler timed out: %{public}s
%s: %s: cmd(%u) on CS[%u] -> ok.\n
_identitiesForUser() - UID: %{public}@ adminOnly: %{public}d
Unable to find application record for identity: %@ error: %@
Enabled keybag signal monitoring
Threshold met (%ld strikes), cooldown activated (%fs)
%{public}@ Companion session changed to isActive: %{bool}d
%s: %s: CS[%u] acquired.\n
Accelerometer availability: %{BOOL}d
%{public}@ will dealloc
Deallocated: %@, receiver: %@
%@ retrying request %s for error: %@
Persisted trigger timestamp: %s
TriggerSignal event sent: strategy=%s, signal=%s, networkReachable=%{bool}d, keybagLocked=%{bool}d
Backoff event sent: action=%ld
Paired devices for companion:%{public}@ returned: %@
Ignoring redundant prewarm request
Failed to load current %s period start: %s
%s returned %s
%{public}@ is no longer tracking %{public}@
%@ did register observer %@
%{public}@ Will authenticate request: %{public}s
%{public}@: no session for starting authentication
Failure alert will appear.
SuppressionSignal event sent: trigger=%s, strategy=%s, suppressor=%s
Failed to determine catacomb UUID: %{public}@
Sensor trust alert did disappear (err: %@)
Stopping reachability monitoring
Environment state for PID %u: %@
BK notification received: %{public}@
Extracting a LACredentialTypeExtractablePassword requires the '%s' entitlement
Stashed credentials processor will handle request rid: %{public}u
NRPairedDeviceRegistry not available
fetchEnablementMode: %{public}@ (flags: %@)
Mac Companion session asked to refresh
Started targeted RBSProcessMonitor for %s
<<< Not triggering auto-lock for %s, VETOED by %s, TRIGGERED by %s
Will dispatch %@
isLockedOutForUser() - UID: %{public}@, request: %{public}@.
ACM requirement for ACL operation %{public}@ (satisfied: %d): %{public}@
No stashed request to refocus with rid: %u
Interruptible app foreground: %s - LOCK
Did not update pending evaluations after significant time change because we are not in the state of interest
%@ is handling %@ with %s
Enabled %s signal
Already is/Has arrived at familiar location
Away from/Has left familiar location
Auto-lock trigger blocked: backoff cooldown is active
Failed to determine path for pid: %d
DTOLocationStatusPolicyResult
%@ finishing with error: %{public}@
processError key:%d rid:%u
Could not stash context data
SuppressionSignal event skipped: %s is not a suppression signal
Stopping keybag monitoring
Auto-lock trigger blocked: device is in setup/migration state
Could not schedule notification %{public}@ for %{public}@ (error:=%{public}@)
Controller deallocated
%s use case: %ld
%s reason:%{public}@
Configuring targeted RBSProcessMonitor for %s
isFeatureSupported: YES
Policy evaluation will start: %@
Biometric liveness verified via SEP flag
Could not fetch feature supported status (%{public}@)
Updated pending evaluations after switch to cool off state: %@
%{public}@ Cancelling companion authentication of request: %{public}s
Failed to trigger device lock
Reusing running timers is not supported
%{public}@ did finish query %{public}@
Mapping %{public}@ into %{public}@
%{public}@ Missing required RTRoutineManager dependency
Started snatch monitoring (threshold: %fG, cooldown: %fs)
%s finished with result: %{public}@, error: %{public}@
Network monitoring already started
Vision fetching companion session state
Recovery after %fs (bucket: %ld), mechanism: %ld
Accessing the credential encoding seed requires the '%s' or '%s' entitlement
 enableTelemetry=YES  LocationState=%{public,signpost.telemetry:number1,name=LocationState}d  Policy=%{public,signpost.telemetry:number2,name=Policy}d 
Could not fetch ratchet state (%{public}@)
authenticationSuccessfulForEvent:%{public}@ for %{public}@: %{public}@
Stopped familiar location signal
Retrying requests with UUID %{public}s
Returning new state: %@
Requested soft reboot
Ignoring event %ld, because UI is transitioning.
AirPods separated - triggering signal change
Successfully triggered device lock
%s returned %{public}@
Did skip notification with identifier: %{public}@
CompanionEligibleDevicesRequest
Keeping service alive because there are still %d clients and %d vended listeners
Stopping deferred monitoring
%s: %s: returning, err = %ld.\n
No service registered for identifier: %{public}@
Snatch state reset
Already monitoring - ignoring duplicate start request
Updated max biometry failures for rid: %u to: %ld
Is offline? %{bool}d - Is threshold met? %{bool}d = Result %{bool}d
Could not get synchronous remote object proxy (%{public}@)
Sensor trust verification result could not be stored %{public}@
Disabled all signal monitoring
No ACM context available for rid: %{public}u
Mac Companion session subscriber already exists
Already monitoring Watch connectivity
Accelerometer update: No data
Could not fetch sensor trust status (%{public}@)
%{public}@ Unable to start companion authentication for request: %{public}u
Did launch preboard
XPC connection to service endpoint with identifier '%@' was closed
Could not fetch extended policy protection availability (%{public}@)
Reseting ACM Ratchet
Authentication with Vision Pro is not enabled
TriggerSignal: signal=%s, strategy=%s
Stashed credentials processor did preflight rid: %{public}u result: %@
%s finished with state: %{public}@
Did finish security delay restart with result: %{public}@
Auto-lock familiar location monitor initialized
Auto-lock trigger blocked: master DimpleKeySentinelAlpha flag is OFF
ACMContext for request: %{public}u is nil
LACBackgroundTaskEngine(%{public}s) worker finished
Could not fetch feature enabled status (%{public}@)
%{public}@ not needed for this request type
%@ cannot present UI for identifier: %@
Missing BiomeLibrary
Failed to encode backoff state
Unexpected biometry type: %d
PeriodicSignal event sent: type=%ld, min=%ld, avg=%ld, max=%ld
Failed to fetch biometric liveness flag from KV store: %{public}@, falling back to enrollment date check
Successfully filed radar
Failed to load %s periods: %s
Cleared trigger timestamp
Auto-lock trigger initialized
Stashing request %{public}s with sessionID: %{public}s acceptsIdleUI: %{bool}d
DTOLocationStateQuery
%@, forwarding to: %@
TriggerSignal event skipped: %s is not a trigger signal
checkCanEnableFeature: NO (%{public}@)
Device nearby (Bluetooth) changed: %{public}@
Unregistered session service: %@ client: %@
Failed to get externalized context: %{public}@
Auto-lock notification blocked: DimpleKeySentinelPsi flag is OFF
Unsupported platform
%{public}@ Did start listener for session events
Cached %s for request %s
%{public}@ %@ replaced authentication error: %@ with next
Started AirPods signal monitoring
%{public}@ Unable to determine current shared mode status %{public}@. Falling back to : %{public}@
Delaying donation of %{public}@ until %{public}@ is finished.
Vision Companion session asked to refresh
Started network monitoring
Stopped RBSProcessMonitor visibility tracking
Did schedule notification %{public}@ for %{public}@
setObject forKey:%d rid:%u
Stopped snatch signal monitoring
SuppressionSignal event skipped: %s is not a trigger signal
Missing identifiers to unregister request %u
LACEValuationRequestCompoundProcessor was unexpectedly released during processing
NRPairedDeviceRegistry class not available
lockoutErrorForExtendedState:%d returned %{public}@
Posted notification for security delay restart
Monitoring was stopped during async operation - ignoring completion
Did post notification with identifier: %{public}@
Performing FaceID check
Could not stash context data %@
AirPods separation state: %ld -> %ld
LACBackgroundTaskEngine(%{public}s) rejected: %{public}@
Data exchange returned error: %@ for key: %ld but we return nil for compatibility reasons
isFeatureEnabled: NO (%{public}@)
Failed to file radar: %@
Vision companion session listener unsubscribed
Skipping processing of request rid: %{public}u by %s
 enableTelemetry=YES 
XPC connection to service endpoint with identifier '%@' was activated
Ratchet config-and-status payload anomaly (reason=%ld, secondsSinceBoot=%ld)
Signal evaluation completed. Duration: %s
Network signal not enabled, voting NO
NRDeviceIdentifier class not available
Effective reachable state changed: %{public}@ (nearby=%{public}@, connected=%{public}@)
Failed to load %s disconnection count: %s
Will post %{public}@
Stopped AirPods signal monitoring
Rightful user passed biometry
Preboard terminated
%{public}@: no session to finish
Cleared all completed periods from trackers
%{public}@ session listener already registered
Error on connection to system daemon: %{public}@
fetchEnablementMode: NO (%{public}@)
Unable to verify user - LOCK
Failed to create endpoint for session service: %@ clientID: %@ error: %@
Will post notification %{public}@
Device became LOCKED
Watch disconnected — starting %fs threshold timer
Auto-lock app context monitor initialized with %ld 1P bundle IDs and %ld categories
NRDeviceMonitor class not available
Available devices: %@
Device location: %ld
Could not extract triggering signal from notification identifier: %s
Persisted %s disconnection count: %ld
%{public}@ Required feature flags are not enabled %{public}@
isFeatureAvailable: NO (%{public}@)
%{public}@ Face ID not requested but request can be authenticated by companion
Biometry signal not enabled - LOCK
Could not fetch HSA2 account %{public}@
Setting data of type %d on ACMContext %u
Network monitoring not active
removeObjectForKey:%d rid:%u
Failed to cancel existing notifications: %@
%{public}@ Tree: %@ value: %ld %s required
biometryDatabaseHashForUser returned error: %@
%@ did unregister from passcode observation
%{public}@ did finish query
%{public}@ ignoring redundant request to start
Monitored app %s lost foreground visibility
Connection invalidated for request rid: %u
Unexpected notification parameters
%@ Interrupted
Backoff: recorded lock strike (%ld/%ld)
There are other active requests for sessionID: %{public}s
Vision companion session subscriber already exists
%{public}@ Registered pending request: %{public}s for evaluation request rid: %u
Preboard completed
AMFIProfileGetScheduledProfile returned error code: %d
%@ error: %@
Canceling pending evaluation with reason: %@, identifier: %@, did find instance: %@
Familiar location not yet determined - LOCK
Sensor trust verification failed %{public}@
Request %{public}s already registered
Deferred monitoring already active - ignoring
Authorization failed: %{public}@
Familiar location state changed: %s -> %{bool}d
%{public}@ Will process request: %{public}s
Connection accepted for vended listener: %@ in service: %@
Could not fetch LocationServices status (%{public}@)
No known ACM policy for LA policy %d
Failed to clear current %s period start: %s
Auto-lock Watch monitor initialized
Unable to terminate preboard as the feature is not supported
Could not determine the current SDK version
Started snatch signal monitoring
Unable to instantiate ACM helper
deviceHasSecureDoublePressHW returned %d
Sensor trust alert with id: %@ will appear.
%{public}@ Face ID not available for request: %{public}u error: %@
%s invalidated, %@ listener
Keybag monitor initialized
No active paired Watch device
%@ did register for passcode observation
%{public}@ falling back to %{public}@ because the TUCallCenter has no active calls
%{public}@ will start
Failed to get everythingPredicate
Skipping resolution of bundle ID for pid %d - migration in progress
%@ terminating with reason: %{public}@
Verified using ACM policy %s that requirement %d is %s on ACMContext %u, flags: %{public}@
Preboard launched
Unexpected AMFI error when setting boot mode, amfiErr: %u
Missing client info
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/platform/platform_lib.c
-[LACDTORatchetManager resetRatchetWithReason:completion:]
en
TrustedBiometricSensorUUID
UseKeyKeyExchange
enableBatch(for:)
LibCall_ACMContextUnloadToImage
LACMechanismUserInfoKeyMaxFailuresExceeded
PushButton
@\"LACDTORatchetStateComposite\"8@?0
ACM failed to set ACMContextData. acmErr: %d
Not Applicable
com.apple.LocalAuthentication.notbackedup
ACMCredential - ACMCredentialDataBiometryMatched
LibCall_ACMSecContextCopyCredentialsArrayEx
com.apple.BiometricKit.generalLockoutStateChanged
ccgcm_init
/Library/MediaStream
%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n
LADTOEventRawValueFeatureEnabledStatusDidChange
Unknown lockout state
Sync request timed out after %.3f secs
kv
ACMContextVerifyPolicy
ed
GroupSeedGeneration
Failed to create endpoint for new session
Failed to create ACMContextRef from externalized form - missing delegate
OnenessAutomaticMode
1
Invalid LACEventSimpleStatusFaceID: %d
v16@?0@\"NSError\"8
com.apple.private.LocalAuthentication.Storage.SetDSLMode
DimpleKeySentinelDelta
DTO policies are not available before first unlock
Device needs to reboot to Preboard to set protected variables
ACMRequirement - ACMRequirementDataSecureIntent
/Library/Logs
is not
recording failed authentication attempt
DTO_Environment
, 
<%@ %p; %@>
Click
CFBundleName
AutoLock_Evaluation
i8@?0
ApplePay
LACPolicyDeviceOwnerAuthenticationWithPassword
LACPolicyPrague
LACEvaluationResult rawValue is next but there is no request
No session exists for this context
Passcode not set
aks_absinthe_collection
com.apple.LocalAuthentication.DTO.RatchetEvaluation
@\"LACUserInterfaceRequest\"8@?0
isConfirmed
MechanismUI
Internal
com.apple.LocalAuthenticationUIService
LACPolicySoftwareUpdate
Required Core Repair dependency was not found
withdrawInterval
v16@?0@\"NSObject<OS_nw_path>\"8
Auto enablement denied for unknown reason
ACMContextCredentialGetPropertyEx
UNUserNotificationCenter
LACMechanismUserInfoKeyAuthType
NumericSixDigits
LACPolicyDeviceOwnerAuthenticationWithCompanion
Unknown internalOperation: %@
LocalAuthenticationCore.LACDTOAnalyticsReporterAutoEnablement
cup
oe
-[LACDTORatchetManager isFeatureSupported]
B16@?0@\"TUCall\"8
BKLockoutStateInBioLockout
Invalid LACCoachingFeedbackOpticID: %d
Auto enablement is disabled due to no biometric enrollments
aks_remote_session
LA.autoLock.uninterruptibleFirstPartyBundleIDs
-[LACDTORatchetManager isSensorTrusted]_block_invoke
Unrecognized enablement flag: %@
LACAngelHostedSceneSpecificationKeyWaitForEndpoint
%@ unable to establish connection to UI
Expected BOOL in NSNumber.
%s: %s: called.\n
ACMRequirement - ACMRequirementDataBiometryMatchAttempted
@\"LACDTOMutablePolicyEvaluationResult\"8@?0
B24@?0^{__ACMHandle=}8^@16
com.apple.private.LocalAuthentication.ContextData.ExtendedMaxAge
LocalAuthenticationCore.LACEvaluationRequestRootProcessor
com.apple.installer.osisstashhelper
ACMContextContainsCredentialTypeEx
LACPolicyMarzipanWithPIN
WatchApproved
ready: %@
com.apple.LocalAuthentication.ContextManagement.Anomaly
com.apple.LocalAuthentication.AutoLock.PeriodicSignal
%s:%spid:%d,%s:%s%s%s%s%s%u:%s overflow%s\n
DTO_Location
nw_path_monitor_set_update_handler
LibSer_ACMDeserializeEnvironmentVariableType
LibCall_ACMGlobalContextCredentialGetProperty_Block
-[LACDTORatchetManager isFeatureStrictModeEnabled]_block_invoke
, securityDelayEndedDueToFamiliarLocation: 
com.apple.iWork.Keynote
lockoutState
waitingForSecondAuth: %@
DimpleKeySentinelPsi
@\"NSMutableDictionary\"8@?0
com.apple.LocalAuthentication.ContextManagement.Registration
BIOMETRY_NOT_AVAILABLE
aks_get_cx_window
DimpleKeySentinelBeta
LACErrorCodeNotInteractive
-[LACDTORatchetManager resetRatchetWithReason:completion:]_block_invoke
installedSensorID: %@
mbr_uid_to_uuid failed to convert UID %u to UUID
LocalAuthenticationCore.LACMechanismTree
PreRequisite
,
v16@?0@\"<LACDTOFeatureState>\"8
com.apple.intents-service
isAvailable || error != nil
LACEvaluationEventValueCompanionStatus(authenticationResult: 
LACErrorCodeBiometryDeniedForApp
processAclInternal
Biometry is not available in passcode lockout.
BKLockoutStatePearlInterlocked
LACPolicyDeviceOwner
No active analytics session for %@
ckon
e-apfs
aks_drain_backup_keys
NotRepaired
com.apple.iWork.Pages
ACMRequirement - ACMRequirementDataAnd
akstest_rewrap_ek
PreboardUPP
CompanionAuthentication-%@-%@
isGracePeriodActive: %@
Face ID not available
com.apple.LocalAuthentication.AutoLock.backoffState
Rarely
/Library/adi
systemIconName
AutoLock_Watch
UIManager
BiometrySensorActive
LibCall_ACMKernelControl
f
aks_auth_token_create
<LACAnalyticsData %p; %@>
v24@?0@\"LACDTORatchetState\"8@\"NSError\"16
@\"LACDTOSensorRepairStateProviderCRAdapter\"8@?0
Auto enablement is not supported on this device
com.apple.private.LocalAuthentication.Storage.BiometricSuccessAge
shared allow list:
liveness
LocalAuthenticationCore.LACAutoLockNotificationService
LocalAuthenticationCore.LACDTOFeatureRequirement
Busy
oacl
Failed to decrypt data %d
Requirement %d not satisfied.
AUTO_LOCK_TRIGGERED_SUBTITLE
AUTHENTICATION_CANCELED
aks_get_lock_state
aks_enable_cache_flow
SwiftUI_PasscodeServices
biometryWatchdogPack: %@
BiometrySensorInactive
Failed to set ACM credential's passphrase-purpose property: %d
LibCall_ACMContexRemoveCredentialsByTypeAndScope
isDTOEnabled: %@
LACPolicyBiometricUserIdentification
Failed to obtain encryption size %d
LibCall_ACMContextUnloadToImage_Block
Util_DeallocRequirement
/Library/AddressBook
PasscodeGeneration
DimpleKey_ExtendedPolicyProtection
com.apple.coreauthd.notifications.action.securityDelay.start
User has denied the use of biometry for this app.
FingerOff
LocalAuthenticationCore.LACInternalInfoParser
I Didn't Try
%s: %s (len=%u): operation:
wheel
LA.dto.biometricLivenessEnrollmentAgeThreshold
BiometricSuccessAge
TCCServerPrompt
LACMechanismUserInfoKeyWillTryToRecover
hasExpiredBiometry: %@
ACM
UserIdentificationWithBiometrics
Pending evaluations detected
LACDTORatchetStateRawValueCollapsed
ACMGlobalContextCredentialGetProperty
connection: %@
SFAuthenticationErrorCodeDomain
Biometry lost.
isTimeSensitive
approvalState: %@
LocalAuthentication
ACMGlobalContextVerifyPolicy
v24@?0@\"LACDTORatchetStateComposite\"8@\"NSError\"16
LACPolicyDeviceOwnerAuthenticationWithWristDetection
AutoLock
AutoLock_AppContext
com.apple.private.LocalAuthentication.Storage.SetThumbAndPayEnabled
LACBackgroundTask-
everythingPredicate
aks_lock_device
BKLockoutStateInPasscodeLockout
DTO_Sensor
root
error: validating (sign) v0 local signing key failed: %d
Failed to query ACM credential: %d
/Library/CoreFollowUp
allowsGracePeriodUI: %@
LACEvaluationResult rawValue is success but there is no value
Companion session is active but authentication on companion device is not supported
/Library/DeviceRegistry.dontBackUp
/Library/NanoTimeKit
GroupSeedKCV
LA.simulator.passcodeType
BKLockoutStateBeforeFirstUnlock
/MobileSoftwareUpdate
/protected/trustd
LA.autoLock.maxOfflineSeconds
serializeParameters
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n
%@ is not supported on %@.
pid: %@
LACEvaluationEvent(
ACMRequirementGetProperty
LibCall_ACMRequirementDelete
-[LACDTORatchetManager disableFeatureWithContext:completion:]_block_invoke
LACPolicyDeveloperModeControl
Storage policy not satisfied.
Missing remote UI instance
aks_backup_rewrap_ek
TKTokenAuthOperation
init(authenticator:environmentProvider:sessionMonitor:reply:)
/Library/WebClips
Task
com.apple.LocalAuthentication.AutoLock.
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n
FaceOut
Runtime minValue must be less than or equal to maxValue
isExtendedPolicyModeEnabled: 
/Library/Backup
NotFound
Connection to UI was invalidated
AppleCredentialManager
LAUI.UseAlwaysOnPasswordField
@\"LACDTOLocationProviderModeDecorator\"8@?0
_aks_unlock_bag
bid
daemon
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/shared_crypto.c
contextUUID: %@
No UI event delegate set, cannot connect UI mechanism
com.apple.settings.passcode.remove
pkofn
%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n
v24@?0@\"RTVisit\"8@\"NSError\"16
com.apple.private.CoreAuthentication.SPI
Util_hexDumpToStrHelper
com.apple.LocalAuthentication.ui.dismissed
array of ACMParameter
LibCall_ACMContextContainsCredentialTypeEx
aks-client-queue
-[LACKeyBagObserverCollection publishKeybagStateUpdate:state:]_block_invoke
Companion session is active but companion device is not available
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c
IOService:/IOResources/AppleKeyStore
AKDeviceListRequestContext
Could not initialize trivial ACL (%@)
com.apple.LocalAuthentication.Credentials.ReadAttemptInternal
My device was auto-locked because it was unlocked for an extended period
LACBackgroundTaskErrorDomain
LA.Preboard.Mode
BiometricLivenessFlag
NumericCustomDigits
SecurityDelayBegan
com.apple.private.LocalAuthentication.SaveExtractableCredential
Request does not accept idling UI
akstest_new_key
confirmed
UserUUID
#
SFAuthenticationManager
AUTO_LOCK_TRIGGERED_BODY
%s: %s (len=%u): acl:
ag
aks_pki_token_op_register
decode_pfk_bulk_data
Request '%@' timed out after %.3f secs
UNNotificationAction
LACAngelHostedSceneSpecificationKeyRequestIdentifier
Unlocked
LocalAuthenticationCore.LACEvaluationEvent
aks_absinthe_generate
FrontBoardServices is not available
kLACDTOPolicyEvaluationRequestPayloadKeyAssociatedIdentifiers
Service not available in Setup
%@ error %d
RatchetState
bc
Missing CoreLocation dependency
-[LACDTORatchetManager disableFeatureWithContext:completion:]
MirroringToDefaultUI
^.+$
Failed to replace ACM passphrase credential: %d
v16@?0q8
isRunningInRecovery: %@
LocalAuthenticationCore.LACCompanionAuthenticationController
<%@; disposable: %@, non-disposable: %@>
Invalid LACAnalyticsAction value: %d
com.apple.private.LocalAuthentication.Storage.MacBuddyPassword
Books,Entertainment,Games,Healthcare & Fitness,Music,Navigation,Sports,Travel
@\"UNUserNotificationCenter\"8@?0
FaceIdLowTemperature
ACMRequirement - ACMRequirementDataBiometryMatched
-[LACDTORatchetManager isExtendedPolicyProtectionEnabled]
/Library/MobileInstallation
-[LACDTORatchetManager performArmRequestWithContext:options:completion:]
BKOperationStateOnHold
Unhandled LACEvaluationResult rawValue
%s: %s: CoreCrypto - %s() failed, ccErr: %d.\n
LibCall_ACMContextVerifyPolicyAndCopyRequirementEx
v32@?0@\"NSNumber\"8@\"NSArray\"16^B24
clientInfo: %@
AppProtectionLockedApps
Service
Biometry is not available on this device.
LACMechanismUserInfoKeyUnderlyingError
v16@?0@\"<LACAnalyticsServiceXPC>\"8
%s: %s: requirePasscode = %p.\n
/Library/SoftwareUpdate
Timeout
Biometry is locked out.
touchid
AppleKeyStore
v24@?0@\"CMAccelerometerData\"8@\"NSError\"16
com.apple.private.LocalAuthentication.Storage.PasscodeSuccessAge
com.apple.private.LocalAuthentication.User.Domain.Select
Disabled via feature flag
Error
BKDeviceManager
categoryIdentifier
@\"LACDTOFeatureRequirementQuery\"8@?0
ccgcm_set_iv
ConfigFlags
UPP install failed with error: 
/Library/Cookies
com.apple.LocalAuthentication.DTO.SecurityDelay
^\\d{4}$
OverContent
PasscodeRejected
/Library/SyncedPreferences
UNNotificationRequest
ratchetStateAfter
<LACAnalyticsSession %p; dialogID: %@, evaluationAnalytics: %u>
UI/Usability
getLengthOfParameters
aks_fs_supports_enhanced_apfs
com.apple.private.LocalAuthentication.Storage.SetLockdownMode
bioLockoutRecovery: 
Power
com.apple.settings.sdp.disable
com.apple.LocalAuthentication.environment.StateDidChange
Mocked authentication cancel
ACMRequirement
not set
LibCall_ACMSecContextVerifyPolicyAndCopyRequirementEx
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n
LA.dto.sr.mock.repairTypeQueryLatency
com.apple.LocalAuthenticationUIService.authentication-service
ACMCredential - ACMCredentialDataSecureIntent
-init is not a valid initializer for the class LACSecureData
LACPolicyAccessoryAuthorization
com.apple.notifyd.matching
credential
, accessoryAuthorizationResult: 
SwiftUI_PasscodeLandscape
ENTER_PASSCODE
LocalAuthenticationCore.LACPreboardStorage
ACMRequirementGetProperties
%d (%@))
@\"LACSecureData\"24@?0^{__ACMHandle=}8^@16
aks_bak_get_swizzler_internal
@\"LACDTOSensorRepairStateProviderDefaultsDecorator\"8@?0
Could not query entitlements %@
Listener released
LocalAuthenticationCore.LACCompanionAuthenticationEnvironment
ACMGetAclAuthMethod
oke
error parsing signing key: %d
TouchIDLockoutError
com.apple.private.LocalAuthentication.Storage.PSSO
com.apple.coreauthd.notifications.autoLock.triggered
companions: %@
AKAppleIDAuthenticationController
RetryButtonPressed
allowsUI: %@
@\"LACDTOMutableFeatureState\"8@?0
Control for key: %d not available in ACM
ACMContextGetExternalForm
LA.dto.sr.mock.repairType
FaceDetectTimeoutSet
isSubtitleLocalized
Session already exists for this context
ccgcm_finalize
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n
UI
com.apple.LocalAuthentication.ui.presented
Companion authentication not available
wk
aks_internal_state
shouldDisplayActionsInline
/Library/DataAccess
user allow list:
Token for device unlock has expired.
%s: %s: constraintState = %p.\n
oa
maxAge: %.2f
TouchIDWatch
LACPolicyTrustComputer
verifyAclConstraintInternal
/Library/UserConfigurationProfiles
B16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8
Passphrase
ACMRequirement - ACMRequirementDataRatchet
%lld,%d\n
aks_kc_backup_get_handle
NRDeviceIdentifier
DimpleKeySentinelEta
Unable to load BKSAlternateSystemApp
Failed to enumerate biometric devices
nw_path_get_status
com.apple.private.LocalAuthentication.NonDisposableContextPool
ACMGlobalContextRemoveCredentialsByType
com.apple.LocalAuthentication
ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes
aks_se_recover
Platform not supported
confirmed: %@
/tmp
error: %@
Failed to fetch feature requirements
com.apple.LocalAuthentication.lac-cache-queue
com.apple.private.LocalAuthentication.DTO.AllowUnapprovedSensor
Unexpected failure to enumerate device of type %d
gracePeriodEnabled
Failed to add ACM credential: %d
Oslo
Auto-Lock | Device locked unexpectedly due to prolonged network disconnection
appContext
FaceIdSilentFallback
DeviceOwnerAuthenticationWithWatch
ACMRequirement: NULL
ACMRequirement - ACMRequirementDataPushButton
-[LACDTORatchetManager ratchetState]_block_invoke
enablementMode: %@
AutoLock_Persistence
/MobileDevice/ProvisioningProfiles
%s%s\n
aks_backup_rewrap_key
requirement
/Library/CrashReporter
v24@?0@\"<LACService>\"8@\"NSError\"16
ACMContextContainsCredentialType
error: validating v1 local signing key failed: %d
aks_pki_token_request_challenge
Biometry is disabled for unlock.
catacombUUID
BATS
AirDB
opticIDAuthenticationDisabled
AutoLock_Analytics
Network
YES (1)
LocalAuthenticationCore.LACDTOFeatureEnablementOptions
triggeringSignal
Duplicate values for key: '
CLASS D
Enter Passcode
PasscodeService
DidAppear
kLACEvaluationRequestPayloadKeySecureIntentRequested
Control exchange data failed with error code: %d
@\"<LACDTOPendingPolicyEvaluationMutable>\"8@?0
oc
com.apple.siri
, is not supported
ock
durationMs
Biometry is not replaceable by companion
DeallocCredentialList
ACMContextReplacePassphraseCredentialsWithScope
aks_stash_persist
aks_pki_token_op_set_password
0`
coolOffStarted: 
cob
-[LACDTORatchetManager isExtendedPolicyProtectionEnabled]_block_invoke
com.apple.LocalAuthentication.Credentials.EncodingSeedAttempt
ACMCredential - ACMCredentialDataPasscodeValidated
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/aeskeywrap.c
akstest_new_ek
IODeviceTree:/filesystems
DimpleKey_GP_UI
DTO_State
Allow
The error instance does not require reboot
p
aks_lock_bag
LACAngelHostedSceneIdentifierPasscodeEmbedded
LACPolicyStockholm
rkm
-[LACDTORatchetManager stateCompositeInContext:completion:]_block_invoke
Could not determine device SN
Auto enablement is disabled via feature-flag
LocalAuthenticationCore.LACConcurrentEvaluationManager
aks_kext_get_options
com.apple.LocalAuthenticationUIService.authentications
aks_assert_consume
aks_pki_token_op_verify
LibCall_ACMContextSetData
/Media
aks_keybag_persona_create
aks_memento_efface_blob
kLAEvaluationRequestPayloadKeyDTOEnvironment
/root/Library/MobileContainerManager
ACMLib
_aks_set_system_with_passcode
LibCall_ACMGlobalContextCredentialGetProperty
aks_fv_new_kek
@\"<LACSharedModeDataSource>\"8@?0
v24@?0@\"<LACDTOPolicyEvaluationRequest>\"8@\"LACEvaluationResult\"16
LACEvaluationEventValueActivity(isActive: 
aks_copy_volume_cookie_persona
tap-to-radar://new
v24@?0@\"<LACDTOSensorRepairState>\"8@\"NSError\"16
d
aks_set_keybag_for_volume_with_cookie_persona
aks_fairplay_wrap
!
security.codesigning.security_boot_mode_complete
, isCredentialPresent: 
LibCall_ACMGetEnvironmentVariable_Block
ACMRequirement - ACMRequirementDataSecureStateWithAttributes
BindKEKToKB
Authorization
AutoLock_Network
Unable to set up dependencies
DeserializeCredentialList
ACMContextRemoveCredentialsByTypeAndScope
acl
aks
Invalid cipher text length
LACPolicyDoublePressAndBiometrics
marketing-name
%@(%d)
InfoPlist
<private>
aks_stash_commit
aks_get_dsme_key
TouchIDSimpleStatus
LACPolicyTokenAuthentication
AUTHENTICATE_TO_RETRY_TOUCH_ID
LA.autoLock.snatchCooldownSeconds
RetryTime
DTO
Auto enablement is disabled via boot-arg
notificationScheduledAt
crypto_generateKeyFromSharedInfo
/.overprovisioning_file
com.apple.coreauthd.notifications.newSecurityDelayRequired
BiometryType
v24@?0@\"<LACAgentProxyXPC>\"8@\"NSError\"16
%@, but I believe this was a false positive.\n\nPlease describe the Apple Watch state and conditions when the auto-lock occurred:\n\n- Was your Apple Watch on your wrist and unlocked?\n- What was the approximate distance between iPhone and 
/.exclave
aks_drop_auxiliary_auth_by_uid
security.codesigning.monitor
com.apple.LocalAuthentication.Storage
duration: %@
AppleKeyStoreTest
aks_change_secret_with_kek
BKDeviceTypePearl
duration: %.2f
visionpro
Expected 1 byte for LBDOA flag
nw_path_monitor_create
com.apple.private.LocalAuthentication.DTO
FingerDetectTimeoutExpired
/Library/Mail
Missing ACM context.
/logs/BurnIn
/preferences
aks_backup_copy_current_bag_uuid
MementoPasscodeGeneration
LACUserInterfaceSceneIdentifierSceneHosting
<UNKNOWN>
com.apple.coreauthd.notifications.category.securityDelay.required
ConfirmedPassword
LocalAuthenticationCore.LACAuthenticationUIManagerComposite
LocalAuthenticationCore.LACPasscodeVerifier
DTO_ERROR_DEVICE_TYPE_NOT_SUPPORTED
/Library/DeviceRegistry
url
ACL
isActive
ConcurrentEvaluations
RatchetStateComposite
No storage key for use case: 
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n
aks_register_for_notifications
PushButtonDoubleClicked
Invalid LACCoachingFeedback: %d
Boot mode not completed
ratchetStateBefore
{?=[8I]}
Could not generate random data
commandCursor == commandBuffer + sizeof(commandBuffer)
EnabledBiometryUsers
No identities are enrolled.
BKOperationStateRunning
aks_save_bag
aks_se_get_reset_sig
v24@?0@\"AKDeviceListResponse\"8@\"NSError\"16
B16@?0@\"<LACDTOPendingPolicyEvaluationControllerObserver>\"8
<data>
/Library/ConfigurationProfiles
/Documents/Pearl
/Library/CoreBrightness
BKOperationEndReasonCanceled
TouchIDSpinner
FaceMatchingBegin
isPreflight
Explicitly disabled by user
AuthorizedLocation
AUTHENTICATE_TO_RETRY_FACE_ID
not enrolled
LiftFinger
/Library/IdentityServices
LA.companion.mac.sessionActive
FaceDetectTimeoutExpired
-[LACDTORatchetManager isExtendedPolicyProtectionAvailable]
locationState: %@
q
com.apple.private.LocalAuthentication.LaunchAngel
, postRequisite: 
ACMContextRemovePassphraseCredentialsByPurposeAndScope
aks_kc_backup_get_uuid
Invalid LACEvent value: %d
DoublePressAndBio
ACMCredential - ACMCredentialDataAP
SwiftUI_Passcode
LocalAuthenticationCore.LACAutoLockEvaluationRequest
LibCall_ACMContextCopyData
OsloPIN
LACErrorCodeCompanionNotAvailable
ccrng
TouchID
BiometryMatch
LACEvaluationEventValueRatchetStatus(isSecurityDelayRunning: 
Feature not supported
/root/Library
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n
aks_make_public_backup_bag
Failed to set ACM credential data: %d
Failed to get SEPTimeSinceBootInMs: %d
@\"LACDTOFeatureEnablementMode\"8@?0
ACMGlobalContextAddCredential
Essonite
stateHash: %@
isGracePeriodEnabled: 
exchangeUPPSignature(for:useCase:)
aks_keybag_persona_delete
SensorActive
Manifest
biometryType: %d
Lowest
v24@?0@8@\"NSError\"16
/Library/DeviceRegistry.state
/Library/Caches/com.apple.xbs/30005FB9-ACD3-4289-B86F-C646C0E23C4D/TemporaryDirectory.bs7wo8/Sources/AppleKeyStore_libs/backup_serialize.c
opticid
LibCall_ACMContextVerifyPolicyWithPreflight_Block
ACMCredential - ACMCredentialDataKextDenyList
ACMCredential - ACMCredentialDataBiometryMatchAttempted
/iomfb_bics_daemon
/Library/UserNotifications
SharedMode
flags
aks_get_icsc_srp
-[LACDTORatchetManager enableFeatureWithOptions:reply:]
@\"LACSignpostEvent\"8@?0
@\"<LACDTOServiceXPCClient>\"8@?0
unknown
<LACBiomeEvaluationMechanismState available: %d, started: %d, success: %d, lockout: %d>
Enhancement
aks_keybag_persona_list
-[LACDTORatchetManager addObserver:]
Stolen Device Protection
DTO_Timers
Failed to get ACM context data ModificationTimestamp: %d
ProcessId
crypto_generateKey
Util_AllocRequirement
v16@?0@\"LACBackgroundTaskResult\"8
<%@; size: %d, used: %d, free: %d, freeForLA: %d, reservedForLA: %d>
UNTimeIntervalNotificationTrigger
ACMContextAddCredentialWithScope
ACMGetEnvironmentVariableData
rk
%s:\n\tNum files:\t%u,\n\tNum hardlinks:\t%u,\n\tNum compressed:\t%u,\n\tTotal Size:\t%lld,\n\tMin File Size:\t%lld,\n\tMax File Size:\t%lld,\n
aks_unlock_device_with_acm
LACEnvironmentServiceXPCHost.m
TCCService
com.apple.LocalAuthentication.AutoLock.SuppressionSignal
Passcode not set.
DisconnectionEventCount
No result returned
network
crypto_deriveKeyAndDecryptData
LibCall_ACMContextCreate
Stockholm
ACMCredentialGetProperty
PreboardDeveloperMode
RepairedByFirstParty
, feedbackValue: 
Protected option successfully enabled
LACErrorCodeBiometryDisconnected
crypto_encryptText_version2
LibCall_ACMContextVerifyPolicyEx_Block
%s: mode=%o, u/g=%i:%i class=%i%s\n
LA.companion.vision.sessionActive
v24@?0@\"NSSet\"8@\"NSError\"16
BKLockoutStateInIdentificationLockout
/Library/SpringBoard
-[LACDTORatchetManager disableFeatureStrictModeWithContext:completion:]
<LACBackgroundTaskQueued; identifier: 
com.apple.settings.biometry.touchid.remove
FaceDetectBegin
ow
aks_fv_prot_cmd_stash_commit = %d
com.apple.private.LocalAuthentication.DTO.EnableWithoutGracePeriod
com.apple.installer.osinstallersetupd
src || !srcLen
Util_DeallocCredential
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n
LACDTOFeatureController.m
, evaluationError: 
pd
tag
/Library
-[LACBiometryHelper resetBiometry]
LACDTORatchetStateRawValueNotStarted
Disabled
%u-%u-%li
Tests
snatch
LibCall_ACMContextCredentialGetProperty
okd
DimpleKeySentinelEpsilon
Face ID interlocked
com.apple.private.LocalAuthentication.Storage.BiometricLivenessFlag
LocalAuthenticationCore.LACMutablePasscodeVerificationRequest
LibCall_ACMPing
/Library/Trial
BiometryNoMatch
com.apple.LocalAuthentication.AutoLock.OneTimeSignal
AutoLock_Keybag
0123456789abcdef
/Library/BulletinBoard
aks_pki_token_op_unlock
AccessoryAuthorizationBegin
platform_rng
failed to open userclient via %s: %d\n
v24@?0@\"NSNumber\"8@\"NSError\"16
lostMode: %@
isAuditTokenApplicationIdentity: %@
Passcode
od
SharedModeStateQuery
-[LACDTORatchetManager isFeatureEnabled]
-[LACDTORatchetManager enableExtendedPolicyProtectionWithCompletion:]
LocalAuthenticationCore.LACDTOAnalyticsReporterCollapseEvaluation
LocalAuthenticationCore.LACDTOAnalyticsProcessor
BKLockoutStateNone
LACEvaluationEventValueCoachingFeedback(feedbackType: 
secondsSinceBoot
success
UseKeyDecrypt
Availability
LocalAuthenticationCore.LACDTOAnalyticsReporterLocationState
ACMCredential - ACMCredentialDataUserOutputDisplayed
ACMContextCreateWithExternalForm
InactivityRebootEnabled
FaceMatchingEnd
Failed to create endpoint for existing session
com.apple.springboard.lockstate
credential type
%@-%@
dtoFallback: %@
: companionType: 
biometryDbHash
BiometryPresenceDetectionOut
pbioa
LocalAuthenticationCore.LACDTOAnalyticsReporterFeatureEnablement
AUTHENTICATION_FAILURE
aks_unwrap_key
UnboundMatch
com.apple.LocalAuthentication.TCC.FaceID
request: %@
kLACServiceTypeAnalytics
com.apple.private.LocalAuthentication.SoftwareUpdate
userID
@\"NSObject\"24@?0@\"NSObject\"8^@16
LACPolicyUserAuthenticationWithPasscodeRecovery
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n
WatchDeviceIdentifier
Vision authentication disabled
PasscodeServices_UseKeyboardGuide
Biome
s, watchThreshold=
SensorInactive
DTO_SECURITY_DELAY_ENDED_TEXT
com.apple.DigitalSeparation.touchID
cchkdf
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c
prp
aks_se_get_passcode_derivation
UserAuthDaemon
outcome
ACMRequirement - ACMRequirementDataAccessGroups
aks_get_convenience_bio_state
threshold: %.2f
com.apple.private.LocalAuthentication.PasscodeServices
isForSoftwareUpdate: %@
com.apple.Fitness,com.apple.Maps,com.apple.facetime,com.apple.iBooks,com.apple.mobiletimer,com.apple.music,com.apple.podcasts,com.apple.tv
ACMContextCopyData
__aks_se_set_secret
LA.autoLock.snatchGForceThreshold
-[LACDTORatchetManager enableFeatureStrictModeWithCompletion:]
Failed to acquire device manager class
com.apple.settings.biometry.faceid.glasses.add
PhoneIntegration
v24@?0@\"LACDTOKVStoreValue\"8@\"NSError\"16
-[LACDTORatchetManager isFeatureStrictModeEnabled]
<LACBiomeDialogEvent dialogID: %@, bundleID: %@, timeSinceUpdate: %.0f, mechanisms: %@, successfulMechanism: %d, failedMechanisms: %@, actions: %@, failingAction: %d>
LACEvaluationRequestPayloadKeyConcurrentEvaluationConfig
Service bootstrapping service not implemented
AES encryption failure (%@)
DoublePressBypass
LocalAuthenticationCore/LACPreboardController.swift
Failed to set ACM credential property: %d
time: %@
com.apple.LocalAuthentication.ContextManagement.ContextExhaustion
LACConcurrentEvaluationManagedRequest rid: 
BKDeviceTypeTouchID
faceid
com.apple.private.LocalAuthentication.ExtractCredential
v24@?0r^v8Q16
com.apple.ahp
Unsupported platform
updateLogLevelFromKext
CLASS NONE
UNNotificationCategory
BKDevice
FrontCameraRotationForISP
BYSetupAssistantNeedsToRun
FaceIdAtPasscode
oect
BKMatchFailReasonPearlInterlocked
PraguePIN
Pending evaluations finished
com.apple.InstallAssistant.
Terminating LAPreboard
isGracePeriodEnabled: %@
DimpleKey_ZDR
com.apple.LocalAuthentication.Storage.error.key.RequiredBootMode
isBodyLocalized
Companion session is active but authentication is not satisfiable by the companion device
odel
crypto_decryptText_version2
aks_se_delete_reset_token
eP/CPXY0Q1CoIqAWn/J97g
ACMContextGetDataEx
/Library/Voicemail
%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n
Unable to set profile trust
Passcode backoff
biometryWatchdogDTO: %@
Call must be made on a subclass
LocalAuthenticationCore.LACDTOMutablePendingPolicyEvaluation
BIOMETRY_NOT_ENROLLED
%s: %s: command = %u.\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n
Subcode
Failed to get ACM context data: %d
com.apple.LocalAuthentication.storage.ProtectedVariableSetFailure
Insufficient biometric liveness
/Library/Fonts
aks_fv_get_size
com.apple.LocalAuthentication.AutoLock.Recovery
ouw
Unknown %@: '%@'
v32@?0@8@16^B24
pid: %x
ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes
<var>
aks_get_bag_uuid
AKAccountManager
Deny
Unknown storage
kLACDomainStateResultKeyAvailableCompanionTypes
Failed to fetch ratchet state and config (stat: %d)
Current user is not admin
LocalAuthenticationCore.LACPasscodeHelper
aks_run_internal_test
DimpleKey_GP
/Library/Keyboard
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n
LACEligibilityDomainPhoneIntegration
Could not determine if audit token belongs to platform binary
/Library/AggregateDictionary
SECURITY_DELAY_ENDED
LACEvaluationEventValueFailure(authType: 
LibCall_ACMSecContextGetUnlockSecret
circular_queue_init
CRIsSelfRepairedComponent
com.apple.mobile.keybagd.lock_status
AKS
LACPolicyPraguePrerequisite
DTO_Feature
LocalAuthenticationCore.LACPreboardController
/Applications
A
XPC connection to service endpoint with identifier '%@' could not be created
BiometryPresenceDetectionIn
v16@?0@\"<BSNSXPCConnectionConfiguring>\"8
currentConnection
com.apple.iWork.Numbers
MementoBlobExists
-[LACDTORatchetManager checkCanEnableFeatureWithCompletion:]_block_invoke
Keyboard
FingerOn
No biometric enrollments
Unable to parse mechanism tree
false
aks_bak_get_beacon_internal
LA.evaluation.releaseUIDelegate
LACUserInterfaceSceneIdentifierRemoteAlertLegacy
DoNotStartDTOTimers
LACDTORatchetStateRawValueWaitingForSecondAuthentication
coolOff: %@
Auto enablement denied due to insufficient biometric liveness
LibCall_ACMTRMLoadState
%s: %s: parameters = %p, parameterCount = %u.\n
user %@
nil
com.apple.coreauthd.notifications.category.securityDelay.ended
minValue
Fallback
Invalid LACEventSimpleStatusTouchID: %d
G, snatchCooldown=
LocalAuthenticationCore.LACCredentialExtractablePasswordAuthorizer
AKBiometricRatchetIdentifierKey
/Library/SMS
could not create file: %s (%s)\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n
FBSOpenApplicationOptionKeyPromptUnlockDevice
FacePartiallyOutOfView
LACPolicyOslo
ABM
LibCall_ACMContextRemoveCredentialsByValueAndScope
/Library/ControlCenter
aks_stash_create_for_bag_and_kek
-[LACDTORatchetManager stateInContext:completion:]_block_invoke
LACPolicyDoublePressBypass
_aks_remote_peer_get_state
HardwareFailure
not present
com.apple.LocalAuthentication.intent.waiting
ACMCredential - ACMCredentialDataPassphraseEntered
ACMCredential - ACMCredentialDataContinuityUnlock
stat failed: %s\n
LACPolicyHumanPresence
ratchetOperationAbandoned
LACPolicyLocationBasedDeviceOwnerAuthenticationWithBiometricRatchet
FBSOpenApplicationOptionKeyUnlockDevice
LibCall_ACMSEPControl_Block
ACMCredential - ACMCredentialDataPasscodeValidated2
os
aks_kc_backup_wrap_key
RecoveryFlags
LA.dto.strictModeEnabled
security.codesigning.config
Skip
crypto_generateKeyFromSharedInfo_version2
FeatureEnabledFlag
UseItem
DTO_Processor
nw_path_monitor_set_queue
Requirements check failed
LocalAuthenticationCore.LACCompanionAuthenticationProviderDummy
My device was auto-locked because it lost connection with my paired Apple Watch
Always
isExtendedPolicyProtectionEnabled: %@
com.apple.installer.osishelperd
LA.test.useTestAppleKeyStoreDaemon
WatchResult
Authenticator
Could not determine the age of the kACMContextDataTypePassphrase credential
DismissButtonPressed
Companion session is active
ACMSEPControl failed: %d
LACErrorCodeNotFound
AutoLock_Snatch
DTO_LostMode
LA.autoLock.uninterruptibleCategories
macbook
PushButtonSecondary
/Library/Caches
/Library/NanoBackup
Request '%@' is already running
-[LACDTORatchetManager stateInContext:completion:]
rc
com.apple.LocalAuthentication.default
triggerInterval
category
unanimous
LocalAuthenticationCore.LACConcurrentEvaluationAllowList
orwk
SecurityDelayEnded
could not open file: %s (%s)\n
BKOperationStateIdle
init
LACPolicyBoot
isStrictModeEnabled: %@
v16@?0@\"LACEvaluationResult\"8
Password
LocalAuthenticationCore.LACDTOCoreProcessor
LACEvaluationResult rawValue is failure but there is no error
LocalAuthenticationCore.LACPreboardStorageRequest
ACMCredential
/vm
v24@?0@\"NSArray\"8@\"NSError\"16
kLACDomainStateResultKeyCompanionStateHashes
%@ is busy
Unknown unsatisfied availability requirement
aks_stash_destroy
aks_wrap_key
-[LACDTORatchetManager disableExtendedPolicyProtectionWithContext:completion:]
LACMechanismUserInfoKeyHardwareIssue
+[LACMobileGestalt deviceHasOpticID]
Auto enablement is not allowed because no passcode is set
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n
bypassEntitlements: %@
gracePeriodState: %@
-[LACDTORatchetManager isFeatureEnabled]_block_invoke
com.apple.LocalAuthentication.DTO.AutoEnablementCheck
com.apple.LocalAuthentication.GlobalDomainDidChange
<LACBackgroundTask; identifier: 
/Library/Calendar
-[LACDTORatchetManager checkCanEnableFeatureWithCompletion:]
UnsatisfiableWithCompanion
com.apple.DigitalSeparation.faceID
GroupSeedWrappingType
Connection to UI was interrupted
usable
Serious Bug
DTO_ERROR_BIOMETRY_NOT_ENROLLED
watch
aks_se_set_nonce
PostRequisite
Externalization proxy unavailable
companionType: %d
createdAt: %@
/log/com.apple.xpc.launchd
GroupUserCount
OysterSimpleStatus
LACPolicyIDV
HomeGestureInJindoForStockholm
PoseOutOfRange
CLASS C
Free Blocks:%lld blocks of size:%d\n
FaceIn
LADTOEventRawValueRatchetStateDidChange
Failed to validate secret for ACM passcode stash, acmErr: %d
com.apple.frontboard.visibility
AUTO_LOCK_ACTION_FILE_RADAR
/.fseventsd
/Library/VoiceServices
/Library/CallHistoryDB
file: %s %i\n
LibSer_ACMDeserializeSEPControlCode
LibCall_ACMKernelControl_Block
DTO_Event
v20@?0B8@\"NSError\"12
-[LACDTORatchetManager cancelArmRequestWithIdentifier:reason:completion:]_block_invoke
angelIdentifier
LACMechanismUserInfoKeySecurityDelayEndedDueToFamiliarLocation
PasscodeUI
LibCall_ACMGlobalContextVerifyPolicy_Block
LibCall_ACMContextCreateWithExternalForm
-[LACDTORatchetManager disableFeatureStrictModeWithContext:completion:]_block_invoke
DTO_Evaluation
isRunningInSystemContext: %@
aks_remote_reset_all_peers
DTO_Storage
NULL
Unknown unsatisfied support requirement
ResetAllSettings
/run
/Library/ApplePushService
Could not determine safety state. Device not found.
B8@?0
SFAuthenticationDevice
HardwareSupportsSecureDoubleClick
BMLocalAuthenticationEvaluationsMechanism
%@, but I believe this was a false positive.\n\nPlease describe the network conditions and device state when the auto-lock occurred:\n\n- Was the device connected to Wi-Fi? If so, what type of network (home, work, public)?\n- Was cellular d
ComponentVersion
ACMRequirement - ACMRequirementDataPassphraseEntered
_securityd
LACPolicyDeviceOwnerAuthenticationWithBiometricsOrCompanion
com.apple.LocalAuthentication.AutoLock.Backoff
/log
mobile
/Library/MobileContainerManager
aks_unload_bag
ExtendedPolicyProtectionEnabledFlag
userPassword: %@
v12@?0B8
 attempted to connect
ACMContextSetData
LACAngelHostedSceneUserActivityType
@\"LACXPCConnectionDefaultAdapter\"8@?0
No user with the given ID
BIOMETRY_LOCKED_OUT
Biometry is disabled for ApplePay
watchdogTimeBucket
RecoveryIterations
repairFlag: %@
ratchetOperation
com.apple.LocalAuthentication.DTO.RatchetConfigAnomaly
Sessions
LocalAuthenticationCore.LACPasscodeRateLimitingEmbeddedPlatforms
LACErrorCodeInvalidDimensions
%s: %s: acl = %p, aclLength = %zu.\n
/logs
akstest_new_ekwk
%p
DFRConfirmation
LACEvaluationEventResponseKeyIsShowingUIBeforeFailure
isStrictModeEnabled: 
locationStatus
ACM failed to %s the value: %d
LocalAuthenticationCore.LACConcurrentEvaluationController
/installd
BiometryDatabaseHash
periocular
strictModeEnabled
v16@?0@\"LACDTOLostModeState\"8
LACAuthenticationUIManagerDefault
LocalAuthenticationCore.LACUserDefaultsPersistentStore
isAutoEnablement: 
PairedDeviceStateQuery-%@
v16@?0@\"<LACDTOPolicyEvaluationControllerObserver>\"8
DeserializeProcessAcl
LACPolicyDeviceOwnerAuthenticationWithBiometrics
v16@?0@\"NSMapTable\"8
/keybags
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n
v24@?0@\"<LACDTOSensorTrustState>\"8@\"NSError\"16
FaceID
PoseOutOfNegativePitchRange
com.apple.LocalAuthentication.AutoLock.triggerTimestamp
BKLockoutStateTokenExpired
<'%@' %@ (%@)>
-apfs_shared_datavolume
ParentK
NEW_SECURITY_DELAY_REQUIRED_TITLE
isAutoEnablement
com.apple.LocalAuthentication.Analytics
Security
deserializeParameters
CLASS A
akstest_unwrap_key
LA.sharedMode.latency
BKMatchFailReasonCanceled
Vision Pro
LACAngelHostedSceneSpecificationKeySceneIdentifier
FaceTooFar
keybag
aks_lkgp_recover
Could not determine safety state. Missing value
kLACEvaluationRequestPayloadKeyInternalInfo
com.apple.LocalAuthentication.Credentials.ReadAttempt
Could note deserialize ACL (%@)
generateRandom
SwiftUI_Dialog_macOS
Failed to convert NSDictionary to ACM batch enablement data
com.apple.devicemanagementclient.DMCRatchet
LibCall_ACMPublishTrustedAccessories
IOService:/IOResources/AppleKeyStoreTest
Failed to set ACM credential's passphrase property: %d
Invalid event: '%@'
Unknown storage for ACMContextData
ACMRequirement - ACMRequirementDataUserOutputDisplayed
-[LACDTORatchetManager isFeatureAvailable]_block_invoke
Cancel
LACAngelHostedSceneIdentifierPassword
Analytics
v20@?0B8@\"LACDTORatchetState\"12
BiometryRequired
evaluationRequestIdentifier
APApplication
aks_unlock_device
Unsupported operation 
LibCall_ACMGlobalContextVerifyPolicyEx
aks_fv_rewrap_kek
LA.companion.device-mock
policy: %d
Credentials
-[LACDTORatchetManager stateCompositeInContext:completion:]
CFBundleDisplayName
^\\d{6}$
FaceIDUI
invalid
maxThreshold: %@
-[LACDTORatchetManager stateWithCompletion:]_block_invoke
-[LACDTORatchetManager enableExtendedPolicyProtectionWithCompletion:]_block_invoke
UseKeySign
No result for request rid: 
Unable
aclRequiresPasscodeInternal
failed to write restore bag to disk %s\n
akstest_check_class
ratchetState: %@
ACMRequirement: %@
LocalAuthenticationCore.LACDTOExtendedPolicyProtectionProcessor
aks_assert_promote
aks_pki_token_register_internal
Failed to create ACMContextRef from externalized form
cbio
Caller is missing the required '%@' entitlement.
com.apple.settings.biometry.faceid.remove
com.apple.settings.biometry.payments.disable
ACMRequirement - ACMRequirementDataAP
acmh
_aks_se_get_reset_token_for_memento_secret
LocationServicesQuery
@\"NSString\"8@?0
v16@?0@\"NSObject<OS_xpc_object>\"8
/root/Library/Preferences
/Library/Accounts
_aks_stash_load
LostModeEnabledFlag
%d
createdAtTimestamp: %.2f
AppleLanguagePreferencesChangedNotification
LACErrorCodeOperationNotAllowed
/Library/Caches/com.apple.xbs/C54CD331-5FA7-4554-B7FE-F4448552AFB8/TemporaryDirectory.zKtgW9/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c
ACMContextGetDataProperty
com.apple.LocalAuthentication.DTO.SecurityDelayUI
GotFocus
TouchIdEnrollment
BMLocalAuthenticationEvaluations
Identification lockout
Auto enablement denied because user has explicitly disabled the feature
Expected min %u bytes.
ACM failed to query the value: %d
acm_transport
oskc
/Library/BackBoard
/Library/MedicalID
ExtractableCredentialProtection
CLLocationManager
BKMatchFailReasonThermalIssueTooCold
RTRoutineManager
com.apple.private.LocalAuthentication.Storage.SetDSLExtendedPolicyProtectionEnabled
%s: %s: context = %p.\n
_get_device_state
generate_wrapping_key_curve25519
None
TouchIDIdentity
kLACDomainStateResultKeyAvailableBiometryTypes
policy: %@
Storage requires reboot
com.apple.LocalAuthentication.Credentials.WriteAttempt
com.apple.findmydevice.ratchet.turnOff
com.apple.settings.biometry.faceid.add
ACMRequirement - ACMRequirementDataKeyRef
DimpleKeySentinelIota
watchdogs: %@
, value: %@
LocalAuthenticationCore.LACDTOLocationController
%s:%spid:%d,%s:%s%s%s%s%s%u:%s cccurve25519 failed: small-order point used%s\n
PearlLockoutError
-[LACEnvironmentServiceXPCHost environmentStateForUser:completion:]
__LAC_LOCALIZATION_DEVICE_VARIANT__
<LACRemoteUIParams ID:%@, SU: %d, Siri: %d, uid: %@, pid: %u, lsai: %d>
%s: %s: maxGlobalCredentialAge = %u.\n
Missing AuthKit dependencies
LACPolicyMarzipan
sensor inaccessible
HumanPresence
5
LocalAuthenticationCore.LACDTOAnalyticsReporterRatchetEvaluation
/.ssh
LocationStateQuery
LACAngelHostedSceneIdentifierPasscode
%@ is not supported in this platform
LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement
/root/Library/Lockdown
identifier
Keybag
TouchIDUI
lostModeState: %@
aks_kext_set_options
aks_assert_drop
LACPolicyLocationBasedDeviceOwnerAuthentication
BiometricRatchetAuthentication
LocalAuthenticationCore.LACDTOPendingPolicyEvaluationStore
%d (%@)
v16@?0@\"LACSharedMode\"8
B24@?0@\"LACOwnerInfo\"8@\"NSDictionary\"16
Alphanumeric
environment != nil
OpticIDUI
DeserializeVerifyAclConstraint
aks_fv_set_protection
akstest_unwrap_ek
-[LACDTORatchetManager disableExtendedPolicyProtectionWithContext:completion:]_block_invoke
expected actual 
LocalAuthenticationCore.LACAutoLockNotificationCategory
^$
, preRequisite: 
pendingEvaluations
Unexpected ACM var when reboot is requested
ACMRequirement - ACMRequirementDataPasscodeValidated
v16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8
aks_fv_get_blob_state
-[LACDTORatchetManager isAutoEnablementAllowed:]
identifier: %@
Unable to create context
v16@?0@\"NSHashTable\"8
is
Granted
defaultActionURL
`
value: %@
v24@?0@\"LACDTOLostModeState\"8@\"NSError\"16
SerialNumber
DeviceOwnerAuthentication
MCProfileConnection
Invalid %@: '%@'
LACErrorCodePasscodeNotSet
_networkd
isValid: %@
com.apple.LocalAuthentication.intent.not-waiting
UpdatedUserName
Request mismatch: 
com.apple.LocalAuthentication.Credentials.WriteAttemptInternal
%s: %s: returning.\n
/Library/Logs/AppleSupport
decode_pfk_bulk_entry
LA.autoLock.maxUnlockedSeconds
Failed to create device with %@: %@
processing option
com.apple.coreauthd.notifications.action.autoLock.fileRadar
ACMRequirement - ACMRequirementDataOr
EscrowPasscodePeriod
aks_keybag_persona_create_with_flags
malloc failed
SecureIntentSupport
FaceIdHighTemperature
clientAuditTokenData: %@
init()
LACErrorCodeTimeout
_aks_unlock_with_sync_bag
isDisapproved: %@
%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unwrapped DER backup bag%s\n
PasscodeServicesProtection
dtoShortFallback: %@
B32@?0@\"NSNumber\"8Q16^B24
store
bh
aks_load_bag
aks_se_recover_with_acm
identities
LACErrorCodeBiometryNotPaired
aks_get_internal_info_for_key
Invalid LACNetworkStatus: %ld
_NRDevicePropertyBluetoothIdentifier
-[LACDTORatchetManager isFeatureSupported]_block_invoke
B16@?0@\"<LACDTOPendingPolicyEvaluationMutable>\"8
/backup
aks_kc_backup_unwrap_key
REQUIRE_func
LocalAuthenticationCore.LACAutoLockKeybagMonitor
LACDTORatchetStateRawValueWaitingForCoolOff
not satisfied
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n
BestEffort
iOS
ContinueButtonPressed
kofn
LostModeStateQuery
My device was auto-locked because it lost connection with my paired AirPods
LibCall_ACMContextGetData
/mobile
aks_get_internal_state
No pending evaluations
com.apple.private.LocalAuthentication.Storage.SetDSLModeEnabled
ACMContextVerifyPolicyEx
subrequirements
uid: %x
Variable: %d not available in ACM
cag
aks_delete_xart_leak
kLACServiceTypeRatchet
[observer conformsToProtocol:@protocol(LACKeyBagObserver)]
%@, but I believe this was a false positive.\n\nPlease describe the conditions when the auto-lock occurred:\n\n- What app were you using before the lock?\n- Did you switch apps or go to the home screen before the lock?\n- Were you actively 
ACMHandleWithPayload
-[LACDTORatchetManager performArmRequestWithContext:options:completion:]_block_invoke
TargetSubType
com.apple.private.LocalAuthentication.Storage.SetOwnerPresence
LocalAuthenticationCore.LACCredentialAnalyticsReporter
allowLandscapeTouchID
result: %@
CreateItem
LibCall_ACMKernDoubleClickNotify
_get_prederived_configuration
-[LACDTORatchetManager cancelArmRequestWithIdentifier:reason:completion:]
notificationScheduledAt: 
LibCall_ACMGetEnvironmentVariable
LocalAuthenticationCore/LACEvaluationRequestCompoundProcessor.swift
CFBundleVisibleComponentName
com.apple.LocalAuthentication.ratchet.StateDidChange
Auto-Lock | Device locked unexpectedly due to AirPods disconnection
array of ACMCredentialRef
osgn
%i
LACMechanismUserInfoKeyUnboundMatch
com.apple.private.LocalAuthentication.Storage
LibCall_ACMTRMSaveState
_fairplay_generate_csk_internal
B32@?0@\"AKRemoteDevice\"8Q16^B24
Unsupported use case: 
uninterruptible(
aks_oneness_heartbeat
remote_session_operate
AHP
crypto_decryptText
LibCall.c
aks_backup_disable_volume
uuid: %@
finishing
environment: %@
XPC connection to LACDTOServiceXPC could not be created
%@, but I believe this was a false positive.\n\nPlease describe how you were using the device when the auto-lock occurred:\n\n- Approximately how long had the device been unlocked?\n- Were you actively using the device or was it idle?\n- Wh
LACEvaluationEventValuePushButtonStatus(authorizingAccessoryId: 
com.apple.Safari.web-extension
SignificantTimeChangeNotification
v20@?0I8@\"NSError\"12
aks_se_get_reset_pubkey
v24@?0@\"NSUUID\"8@\"NSError\"16
v24@?0@\"<LACDTOFeatureRequirements>\"8@\"NSError\"16
User interaction is required
-[LACDTORatchetManager isSensorTrusted]
-[LACDTORatchetManager stateCompositeWithCompletion:]
NOT_NOW_ACTION
Unexpected AMFI error when setting standard boot mode, amfiErr: %u
Auto-Lock | Device locked unexpectedly
/root/Library/Caches
SensorNotTrustedStrictMode
User is not admin
/usr/local/bin/latool
CoreRoutine
Watch
title
ACMContextRemoveCredentialsByValueAndScope
aks_se_stage_stash
interrupted
LibSerialization.c
set
lost
AES decryption failure (%@)
DeviceClassNumber
MarketingDeviceFamilyName
Disk
<LACBiomeEvaluationEvent caller: %@, policy: %d, errorCode: %d, dtoState: %d, ratchetState: %d, biometry: %@, passcode: %@>
cooldownExpiration
isEnabled: %@
allowsAuthenticationFallbacks: %@
pcma
akstest_last_user
_aks_recover_with_escrow_bag
%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n
isRunning: %@
Biometry not supported in Shared iPad mode
IsVirtualDevice
AccessoryAuthorizationEnd
PearlIDCapability
com.apple.private.LocalAuthentication.Storage.SetDSLStrictModeEnabled
com.apple.LocalAuthentication.DTOErrorDomain
ACMCredential - ACMCredentialDataPassphraseExtractable
%s: %s: operation = %p, operationLength = %zu.\n
biometry: %@
Missing AuthKit dependency
Storage
com.apple.coreauthd.notifications.action.securityDelay.dismiss
Auto-Lock | Device locked unexpectedly due to Apple Watch disconnection
aks_se_secret_drop
TUCallCenter
FamiliarLocationFlag
v24@?0@\"NSData\"8@\"NSError\"16
OpticID
LACEvaluationEventValueBootstrap(initialPosition: 
 dir: %s %i\n
Failed to get data protection class for given path %s with errno %s (%d)\n
-[LACDTORatchetManager ratchetState]
LostFocus
maxValue
time: %.2f
gracePeriod: %@
AuditToken
com.apple.LocalAuthentication.Credentials.ExemptionInternal
AvailableMechanisms
@\"LACDTOMutableSensorRepairState\"8@?0
evaluationRequestIdentifier: %@
com.apple.LocalAuthentication.AutoLock.current
bypassEntitlements: 
aks_sign_signing_key
Online
s, snatchGForce=
Crash/Hang/Data Loss
default
PraguePrerequisite
, matchingStatus: 
Auto-Lock | Device locked unexpectedly due to snatch detection
Unable to externalize ACM context
/Library/CountryBundles
aks_invalidate_bag
<%@ : %@>
LACPolicyDeviceAdminAuthentication
START_SECURITY_DELAY_ACTION
ACMContextRemoveCredentialsByValue
%s/mobile
UID:%u
q8@?0
biometryWatchdogGlobal: %@
LocationBasedTrustComputer
LocalAuthenticationCore.LACBackgroundTaskQueued
Auto-Lock | Device locked unexpectedly after extended unlocked period
LA.RunningInBATS
^\\d+$
-[LACDTORatchetManager isAutoEnablementAllowed:]_block_invoke
BKMatchFailReasonPowerIssue
YES (2)
/networkd
aks_se_support_in_rm
Bootstrap
LocalAuthenticationCore.LACDTOAnalyticsService
ACMContextVerifyPolicyWithPreflight
oecd
aks_lower_iteration_count
_aks_remote_peer_drop
PreboardSyncQueue
aks_fv_unwrap_vek_with_acm
NO
Companion
getRequirementDataSizeForVersion
ACMContextCreateWithFlags
LA.ui.disableSensitiveUIRedaction
NoMatch
sceneIdentifier
LADTOEventRawValueLocationStatusDidChange
LACAngelHostedSceneIdentifierAuthorization
```
