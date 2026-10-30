# `AFRequestDispatcherServiceHelper` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/SiriRequestDispatcher`](../userland/System__Library__PrivateFrameworks__SiriRequestDispatcher.framework__SiriRequestDispatcher.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `AFServiceHelper`
- 0 instance variables, 0 properties, 39 instance methods, 0 class methods

## Instance methods

```
-[AFRequestDispatcherServiceHelper handleCommand:withExecutionContextMatchingInfo:completion:];
-[AFRequestDispatcherServiceHelper audioSessionID];
-[AFRequestDispatcherServiceHelper callState];
-[AFRequestDispatcherServiceHelper currentAuthorizationStyle:];
-[AFRequestDispatcherServiceHelper currentLocationWithAccuracy:timeout:completion:];
-[AFRequestDispatcherServiceHelper currentLocationWithFetchRequest:completion:];
-[AFRequestDispatcherServiceHelper fetchContextsForKeys:forRequestID:includesNearbyDevices:completion:];
-[AFRequestDispatcherServiceHelper headGestureConfiguration];
-[AFRequestDispatcherServiceHelper notifyAppLaunchWillBePresentedToUser];
-[AFRequestDispatcherServiceHelper registerInternalGestureTestingHandler:];
-[AFRequestDispatcherServiceHelper didRecognizeTokens:sessionUUID:];
-[AFRequestDispatcherServiceHelper meCard:];
-[AFRequestDispatcherServiceHelper didRecognizeVoiceCommandCandidatePackage:nluResult:sessionUUID:];
-[AFRequestDispatcherServiceHelper currentResponseMode];
-[AFRequestDispatcherServiceHelper deactivateAudioSessionIfNoActiveAssertions];
-[AFRequestDispatcherServiceHelper deactivateCurrentAnnouncementRequestForReason:];
-[AFRequestDispatcherServiceHelper deferAudioSessionDeactivationForAnnouncementRequest];
-[AFRequestDispatcherServiceHelper didCompleteRecognitionWithError:secureOfflineOnlyRecognition:sessionUUID:statistics:];
-[AFRequestDispatcherServiceHelper didRecognizeFinalResultCandidatePackage:sessionUUID:];
-[AFRequestDispatcherServiceHelper didRecognizePackage:nluResult:sessionUUID:];
-[AFRequestDispatcherServiceHelper didRecognizePackage:sessionUUID:];
-[AFRequestDispatcherServiceHelper didRecognizePartialPackage:nluResult:sessionUUID:];
-[AFRequestDispatcherServiceHelper didRecognizeTokens:nluResult:sessionUUID:];
-[AFRequestDispatcherServiceHelper dismissLocationServiceDialogIfNeeded];
-[AFRequestDispatcherServiceHelper drainLocationServiceRequestsForNewRequestAndClearLocationCache:dismissDialog:];
-[AFRequestDispatcherServiceHelper extendRequestTimeoutBy:forRequestID:];
-[AFRequestDispatcherServiceHelper fetchDeviceAndUserIdsForSharedUserId:withCallback:];
-[AFRequestDispatcherServiceHelper handleSpeechRecognized:completion:];
-[AFRequestDispatcherServiceHelper handleSpeechServerEndpointIdentified:completion:];
-[AFRequestDispatcherServiceHelper isBobbleAvailable];
-[AFRequestDispatcherServiceHelper logUUFRReadyEvent:];
-[AFRequestDispatcherServiceHelper notifySpeechDetectedIsUndirected];
-[AFRequestDispatcherServiceHelper requestClosed:forRequestID:];
-[AFRequestDispatcherServiceHelper selectResultWithResultCandidate:completion:];
-[AFRequestDispatcherServiceHelper startRequestWith:];
-[AFRequestDispatcherServiceHelper streamingServiceDelegateForRequestId:];
-[AFRequestDispatcherServiceHelper submitExternalActivationRequest:completion:];
-[AFRequestDispatcherServiceHelper topicChangedForRequestID:];
-[AFRequestDispatcherServiceHelper unredactedMeCard];
```
