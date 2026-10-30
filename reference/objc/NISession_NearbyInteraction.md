# `NISession`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UWBSessionDelegateProxyProtocol`, `ARInternalSessionObserver`
- 34 instance variables, 25 properties, 149 instance methods, 27 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSUUID" _internalID;
@"NIServerConnection" _connection;
@"NIExportedObjectForwarder" _exportedObjectForwarder;
@"NIConfiguration" _currentConfiguration;
@"NSObject<OS_dispatch_semaphore>" _discoveryTokenSemaphore;
{vector<UWBSessionInterruptionBookkeeping, std::allocator<UWBSessionInterruptionBookkeeping>>="__begin_"^{UWBSessionInterruptionBookkeeping}"__end_"^{UWBSessionInterruptionBookkeeping}""{?="__cap_"^{UWBSessionInterruptionBookkeeping}}} _interruptions;
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _readyForCallbacks;
@"NSObject<OS_os_log>" _log;
d _startTime;
d _duration;
B _updatedNearbyObjects;
q _motionState;
@"NIDiscoveryToken" _discoveryToken;
B _btcsConnectionLostPending;
@"NICarKeyEventNotifier" _carKeyEventNotifier;
Q _connectionOptions;
@"NIAcwgEventNotifier" _acwgEventNotifier;
@"NIDevicePresenceNotifier" _devicePresenceNotifier;
@"NIFindingNotifier" _findingNotifier;
@"NIBTCSRangingNotifier" _btcsRangingNotifier;
@"NISystemEventNotifier" _systemEventNotifier;
@"NISessionVisionContext" _visionContext;
@"NSDate" _lastObjectUpdateLogTime;
{NearbyObjectUpdateLogging="totalUpdates"i"totalObjects"i"objectsWithDistance"i"objectsWithHorizontalAngle"i"firstDistance"f"lastDistance"f"minDistance"f"maxDistance"f"firstHorizontalAngleRad"f"lastHorizontalAngleRad"f} _objectUpdateLogging;
B _itemLocalizerDidPrewarmRanging;
@"<NIBodyIdentifiable>" _originBody;
@"NIBodyToken" _bodyToken;
i _internalState;
@"<NISessionDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
@"NSError" _invalidationError;
@"NSDictionary" _activationResponse;
@"<NIInternalSessionDelegate>" _internalDelegate;
```

## Properties

```
@property (Tq,R) motionState;
@property (TB,R,GisPreciseRangingAllowed) preciseRangingAllowed;
@property (T@"NIRangingAuthUWBInfo",R,N) rangingAuthUWBInfo;
@property (TB,R,GisExtendedDistanceMeasurementAllowed) extendedDistanceMeasurementAllowed;
@property (TB,R,GisRangingLimitExceeded) rangingLimitExceeded;
@property (T@"NICarKeyEventNotifier",R) carKeyEventNotifier;
@property (T@"NIAcwgEventNotifier",R) acwgEventNotifier;
@property (TB,R,GisRangingLimitExceeded) rangingLimitExceeded;
@property (T@"NIDevicePresenceNotifier",R) devicePresenceNotifier;
@property (T@"NIFindingNotifier",R) findingNotifier;
@property (T@"NIBTCSRangingNotifier",R) btcsRangingNotifier;
@property (T@"NISystemEventNotifier",R,N) systemEventNotifier;
@property (Ti,V_internalState) internalState;
@property (T@"NSError",&,V_invalidationError) invalidationError;
@property (T@"NSDictionary",&,V_activationResponse) activationResponse;
@property (T@"<NIInternalSessionDelegate>",W,V_internalDelegate) internalDelegate;
@property (T@"<NISessionDelegate>",W,N,V_delegate) delegate;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_delegateQueue) delegateQueue;
@property (T@"NIDiscoveryToken",R,C,N) discoveryToken;
@property (T@"NIConfiguration",R,C,N) configuration;
@property (T@"<NIBodyIdentifiable>",&,N) originBody;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NISession deviceCapabilities];
+[NISession isSupported];
+[NISession observerSession];
+[NISession _localDeviceLogger];
+[NISession _queryAndCacheCapabilities];
+[NISession _supportedPlatform:];
+[NISession activelyInteractingDiscoveryTokens];
+[NISession cachedPlatformCapabilities];
+[NISession generateBluetoothDeviceTokenWithPublicAddress:IRK:];
+[NISession generateDiscoveryTokenFromBeaconIdentifier:];
+[NISession generateFindingDiscoveryToken];
+[NISession generateFindingDiscoveryTokenWithIdentityResolvingKey:];
+[NISession generateFindingDiscoveryTokenWithSharedSecret:];
+[NISession generateSOSBeaconSearcherDataMatchingSubjectData:completion:];
+[NISession generateSOSBeaconSubjectDataWithCompletion:];
+[NISession getAsyncActivelyInteractingDiscoveryTokens:];
+[NISession getAsyncInteractableDiscoveryTokens:];
+[NISession interactableDiscoveryTokens];
+[NISession internalDeviceCapabilities];
+[NISession localDevicePrintableState];
+[NISession requestTCCAccessForCurrentProcessWithCompletion:];
+[NISession requestTCCAccessForProcessWithAuditToken:completion:];
+[NISession setAsyncLocalDeviceInteractableDiscoveryTokens:completion:];
+[NISession setCachedPlatformCapabilities:];
+[NISession setLocalDeviceCanInteract:withDiscoveryTokens:];
+[NISession setLocalDeviceDebugParameters:];
+[NISession setLocalDeviceInteractableDiscoveryTokens:];
```

## Instance methods

```
-[NISession motionState];
-[NISession pause];
-[NISession runWithConfiguration:];
-[NISession _serverConnectionInvalidated];
-[NISession setConfigurationForTesting:];
-[NISession init];
-[NISession setInternalState:];
-[NISession internalDelegate];
-[NISession dealloc];
-[NISession setInternalDelegate:];
-[NISession invalidate];
-[NISession setDelegate:];
-[NISession _didUpdateBody:];
-[NISession configuration];
-[NISession setDelegateQueue:];
-[NISession invalidationError];
-[NISession delegate];
-[NISession hash];
-[NISession description];
-[NISession delegateQueue];
-[NISession isEqual:];
-[NISession internalState];
-[NISession _serverConnectionInterrupted];
-[NISession setInvalidationError:];
-[NISession isPreciseRangingAllowed];
-[NISession session:didChangeState:];
-[NISession session:didFailWithError:];
-[NISession session:didUpdateFrame:];
-[NISession sessionInterruptionEnded:];
-[NISession sessionWasInterrupted:];
-[NISession _addObject:];
-[NISession setARSession:];
-[NISession _remoteObject];
-[NISession session:didUpdateExternalAnchors:];
-[NISession session:willRunWithConfiguration:];
-[NISession sessionShouldAttemptRelocalization:completion:];
-[NISession activationResponse];
-[NISession setActivationResponse:];
-[NISession _removeObject:];
-[NISession _handleARSessionDidUpdateFrame:];
-[NISession _pauseInternalARSessionIfNeeded];
-[NISession _sendRemoteDevice:changedState:];
-[NISession didProcessAcwgRangingSessionResumeRequestMsgWithResponse:error:];
-[NISession _handleARSessionDidChangeState:];
-[NISession findingNotifier];
-[NISession _addRegionPredicate:];
-[NISession _configurationSupportsRetry];
-[NISession _configureAndRunInternalARSession];
-[NISession _debugInjectFakeUUID:degrees:];
-[NISession _didUpdateBodyInternal:];
-[NISession _getSessionFailureError];
-[NISession _handleARSession:willRunWithConfiguration:];
-[NISession _handleARSessionDidFailWithError:];
-[NISession _handleARSessionInterruptionEnded];
-[NISession _handleARSessionWasInterrupted];
-[NISession _handleActivationError:];
-[NISession _handleActivationSuccess:];
-[NISession _handlePauseSessionError:];
-[NISession _handlePauseSessionSuccess];
-[NISession _handleRunSessionError:];
-[NISession _handleRunSessionSuccess];
-[NISession _initAndConnectToServerWithOptions:];
-[NISession _internalRunWithConfiguration:];
-[NISession _interruptSessionWithInternalReason:cachedInterruption:nearbydReSuspension:];
-[NISession _invalidateInternal];
-[NISession _invalidateInternalARSessionIfNeeded];
-[NISession _invalidateSessionAndNotifyError:];
-[NISession _isInternalClient];
-[NISession _isValidARSession:andConfiguration:];
-[NISession _logDurationAndSubmit:];
-[NISession _logTime];
-[NISession _notifyDidInvalidateWithError:];
-[NISession _osLogNearbyObjectUpdate:];
-[NISession _performBlockOnDelegateQueue:ifRespondsToSelector:];
-[NISession _performBlockOnDelegateQueue:ifRespondsToSelector:evenIfNotRunning:];
-[NISession _processUpdatedLockState:];
-[NISession _provideTruthTag:];
-[NISession _reinterruptSessionWithCachedInterruption];
-[NISession _removeRegionPredicate:];
-[NISession _setARSessionInternal:];
-[NISession _setDebugURSK:transactionIdentifier:];
-[NISession _setURSKTTL:];
-[NISession _shouldReConnectToDaemonAfterCrash];
-[NISession _shouldReRunSessionAfterSessionInterruptionEnded];
-[NISession _submitErrorMetric:];
-[NISession _synchronousRemoteObject];
-[NISession _tryToRecoverFromFailure:];
-[NISession _verifyError:];
-[NISession acwgEventNotifier];
-[NISession btcsRangingNotifier];
-[NISession carKeyEventNotifier];
-[NISession deleteURSKs];
-[NISession devicePresenceNotifier];
-[NISession didDiscoverNearbyObject:];
-[NISession didGenerateShareableConfigurationData:forObject:];
-[NISession didPrefetchAcwgUrsk:error:];
-[NISession didProcessAcwgM1MsgWithResponse:error:];
-[NISession didProcessAcwgM3MsgWithResponse:error:];
-[NISession didReceiveAopSFZoneUpdate:];
-[NISession didReceiveRangingAuthRecommendation:forObject:];
-[NISession didRemoveNearbyObjects:withReason:];
-[NISession didStartAcwgRanging:];
-[NISession didSuspendAcwgRanging:];
-[NISession didUpdateAlgorithmState:forObject:];
-[NISession didUpdateDLTDOAMeasurements:];
-[NISession didUpdateDeviceAssociationStatus:];
-[NISession didUpdateHealthStatus:];
-[NISession didUpdateHomeDeviceUWBRangingAvailability:];
-[NISession didUpdateLocalDiscoveryToken:];
-[NISession didUpdateMotionState:];
-[NISession didUpdateNICoordinates:];
-[NISession didUpdateNearbyObjects:];
-[NISession didUpdateState:forItem:];
-[NISession discoveryToken];
-[NISession getInternalConnectionQueue];
-[NISession getInternalIdentifier];
-[NISession getInternalLogObject];
-[NISession isExtendedDistanceMeasurementAllowed];
-[NISession isRangingLimitExceeded];
-[NISession lightEstimateFromARLightEstimate:];
-[NISession niVisionInputTrackingStateFromARTRackingState:];
-[NISession object:didUpdateCVDistance:];
-[NISession object:didUpdateCVRegion:previousRegion:];
-[NISession object:didUpdateRegion:previousRegion:];
-[NISession originBody];
-[NISession prefetchAcwgUrsk:];
-[NISession processAcwgM1Msg:withSessionTriggerReason:];
-[NISession processAcwgM3Msg:];
-[NISession processAcwgRangingSessionResumeRequestMsg:withResumeTriggerReason:];
-[NISession processBluetoothEventWithType:btcClockTicks:];
-[NISession processBluetoothEventWithType:btcClockTicks:eventCounter:];
-[NISession processBluetoothHostTimeSyncWithType:btcClockTicks:eventCounter:];
-[NISession processDCKMessage:responseCallback:];
-[NISession processVisionInput:];
-[NISession rangingAuthUWBInfo];
-[NISession relayDCKMessage:];
-[NISession requestAcwgRangingSessionSuspend:withSuspendTriggerReason:];
-[NISession setOriginBody:];
-[NISession suspendAcwgRanging:withSuspendTriggerReason:];
-[NISession systemDidUpdateResourceUsageLimitExceeded:forSessionConfigurationTypeWithName:];
-[NISession systemDidUpdateState:];
-[NISession systemEventNotifier];
-[NISession updateMotionState:forObjectWithToken:];
-[NISession updateResponderDeviceIdentifier:completionHandler:];
-[NISession uwbSessionDidFailWithError:];
-[NISession uwbSessionDidInvalidateWithError:];
-[NISession uwbSessionInterruptedWithReason:timestamp:];
-[NISession uwbSessionInterruptionReasonEnded:timestamp:];
-[NISession worldTransformForObject:];
```
