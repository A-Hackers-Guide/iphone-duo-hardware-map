# `TUConversationManagerXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUConversationManagerXPCClient`, `TUConversationManagerDataSource`
- 19 instance variables, 27 properties, 152 instance methods, 7 class methods

## Instance variables

```
B _autoSharePlayEnabled;
B _hasRequestedInitialState;
B _hasInitialState;
B _shouldConnectToHost;
B _shouldPopulatePseudonymsOnSetup;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _accessorLock;
i _shouldConnectToken;
i _daemonLaunchToken;
@"<TUConversationManagerDataSourceDelegate>" _delegate;
@"<TUConversationMediaControllerDataSourceDelegate>" _mediaDelegate;
@"<TUConversationReactionsControllerDataSourceDelegate>" _reactionsDelegate;
@"NSXPCConnection" _xpcConnection;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSDictionary" _conversationsByGroupUUID;
@"NSDictionary" _pseudonymsByCallUUID;
@"NSDictionary" _advertisementsOnSystem;
@"NSDictionary" _activityAuthorizedBundleIdentifiers;
@"NSNumber" _sharePlayAvailable;
@"NSNumber" _screenSharingAvailable;
```

## Properties

```
@property (T{os_unfair_lock_s=I},R,N,V_accessorLock) accessorLock;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (TB,N,V_hasRequestedInitialState) hasRequestedInitialState;
@property (TB,N,V_hasInitialState) hasInitialState;
@property (Ti,N,V_shouldConnectToken) shouldConnectToken;
@property (TB,N,V_shouldConnectToHost) shouldConnectToHost;
@property (TB,N,V_shouldPopulatePseudonymsOnSetup) shouldPopulatePseudonymsOnSetup;
@property (Ti,N,V_daemonLaunchToken) daemonLaunchToken;
@property (T@"NSDictionary",C,N,V_conversationsByGroupUUID) conversationsByGroupUUID;
@property (T@"NSDictionary",C,N,V_pseudonymsByCallUUID) pseudonymsByCallUUID;
@property (T@"NSDictionary",C,N,V_advertisementsOnSystem) advertisementsOnSystem;
@property (T@"NSDictionary",C,N,V_activityAuthorizedBundleIdentifiers) activityAuthorizedBundleIdentifiers;
@property (T@"NSNumber",C,N,V_sharePlayAvailable) sharePlayAvailable;
@property (T@"NSNumber",C,N,V_screenSharingAvailable) screenSharingAvailable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,C,N) incomingPendingConversationsByGroupUUID;
@property (T@"NSSet",R,C,N) activatedConversationLinks;
@property (TB,N,V_autoSharePlayEnabled) autoSharePlayEnabled;
@property (TB,R,N) isSharePlayAvailable;
@property (TB,R,N) isScreenSharingAvailable;
@property (T@"<TUConversationManagerDataSourceDelegate>",W,N,V_delegate) delegate;
@property (T@"<TUConversationMediaControllerDataSourceDelegate>",W,N,V_mediaDelegate) mediaDelegate;
@property (T@"<TUConversationReactionsControllerDataSourceDelegate>",W,N,V_reactionsDelegate) reactionsDelegate;
```

## Class methods

```
+[TUConversationManagerXPCClient setAsynchronousServer:];
+[TUConversationManagerXPCClient asynchronousServer];
+[TUConversationManagerXPCClient setSynchronousServer:];
+[TUConversationManagerXPCClient synchronousServer];
+[TUConversationManagerXPCClient conversationManagerAllowedClasses];
+[TUConversationManagerXPCClient conversationManagerClientXPCInterface];
+[TUConversationManagerXPCClient conversationManagerServerXPCInterface];
```

## Instance methods

```
-[TUConversationManagerXPCClient leaveConversationWithUUID:];
-[TUConversationManagerXPCClient conversation:receivedActivitySessionEvent:];
-[TUConversationManagerXPCClient sharePlayAvailable];
-[TUConversationManagerXPCClient handleServerDisconnect];
-[TUConversationManagerXPCClient accessorLock];
-[TUConversationManagerXPCClient startAlignmentTimeOutForNearbySessionForConversation:];
-[TUConversationManagerXPCClient synchronousServerWithErrorHandler:];
-[TUConversationManagerXPCClient getInactiveLinkWithCompletionHandler:];
-[TUConversationManagerXPCClient addScreenSharingType:forConversation:];
-[TUConversationManagerXPCClient advertisementsOnSystem];
-[TUConversationManagerXPCClient setLinkName:forConversationLink:completionHandler:];
-[TUConversationManagerXPCClient conversation:collaborationStateChanged:highlightIdentifier:];
-[TUConversationManagerXPCClient setUsingAirplay:onActivitySession:onConversationWithUUID:];
-[TUConversationManagerXPCClient setPresentationAspectRatioStyle:conversation:];
-[TUConversationManagerXPCClient mediaPrioritiesChangedForConversation:];
-[TUConversationManagerXPCClient setLocalParticipantAudioVideoMode:forConversationUUID:];
-[TUConversationManagerXPCClient removeConversationNoticeWithUUID:];
-[TUConversationManagerXPCClient isSharePlayAvailable];
-[TUConversationManagerXPCClient hasInitialState];
-[TUConversationManagerXPCClient conversation:appLaunchState:forActivitySession:];
-[TUConversationManagerXPCClient markCollaborationWithIdentifierOpened:forConversationUUID:];
-[TUConversationManagerXPCClient launchAppForInterpreterRequestForConversationUUID:bundleID:requestID:completionHandler:];
-[TUConversationManagerXPCClient setLocalParticipantCluster:forConversation:];
-[TUConversationManagerXPCClient kickMember:conversation:];
-[TUConversationManagerXPCClient updateRemoteControlStatus:onConversation:];
-[TUConversationManagerXPCClient addedCollaborationDictionary:forConversation:];
-[TUConversationManagerXPCClient reportDualCaptureMetric:forConversationGroupUUID:];
-[TUConversationManagerXPCClient init];
-[TUConversationManagerXPCClient setXpcConnection:];
-[TUConversationManagerXPCClient activatedConversationLinks];
-[TUConversationManagerXPCClient getLatestRemoteScreenShareAttributesWithCompletionHandler:];
-[TUConversationManagerXPCClient conversation:participantDidStopReacting:];
-[TUConversationManagerXPCClient launchApplicationForActivitySessionUUID:authorizedExternally:forceBackground:completionHandler:];
-[TUConversationManagerXPCClient isScreenSharingAvailable];
-[TUConversationManagerXPCClient setHasInitialState:];
-[TUConversationManagerXPCClient updateExternalParticipants:];
-[TUConversationManagerXPCClient startInterpreterRequestWithBundleID:conversationUUID:requestID:completionHandler:];
-[TUConversationManagerXPCClient _requestInitialStateWithCompletionHandler:];
-[TUConversationManagerXPCClient shouldConnectToken];
-[TUConversationManagerXPCClient stopInterpreterRequestForConversationUUID:bundleID:requestID:completionHandler:];
-[TUConversationManagerXPCClient setDaemonLaunchToken:];
-[TUConversationManagerXPCClient dealloc];
-[TUConversationManagerXPCClient createActivitySession:onConversation:options:];
-[TUConversationManagerXPCClient screenSharingAvailableChanged:];
-[TUConversationManagerXPCClient setShouldPopulatePseudonymsOnSetup:];
-[TUConversationManagerXPCClient setScreenEnabled:withScreenShareAttributes:forConversationWithUUID:];
-[TUConversationManagerXPCClient registerWithCompletionHandler:];
-[TUConversationManagerXPCClient daemonLaunchToken];
-[TUConversationManagerXPCClient setShouldConnectToken:];
-[TUConversationManagerXPCClient setReactionsDelegate:];
-[TUConversationManagerXPCClient sharePlayAvailableChanged:];
-[TUConversationManagerXPCClient conversation:addedMembersLocally:];
-[TUConversationManagerXPCClient addCollaborationDictionary:forConversationWithUUID:fromMe:];
-[TUConversationManagerXPCClient setActivityAuthorization:forBundleIdentifier:];
-[TUConversationManagerXPCClient hasRequestedInitialState];
-[TUConversationManagerXPCClient queue];
-[TUConversationManagerXPCClient getMessagesGroupDetailsForMessagesGroupUUID:completionHandler:];
-[TUConversationManagerXPCClient linkSyncStateIncludeLinks:WithCompletion:];
-[TUConversationManagerXPCClient setDownlinkMuted:forParticipants:inConversation:completionHandler:];
-[TUConversationManagerXPCClient renewLink:expirationDate:reason:completionHandler:];
-[TUConversationManagerXPCClient xpcConnection];
-[TUConversationManagerXPCClient activateConversationNoticeWithActionURL:bundleIdentifier:];
-[TUConversationManagerXPCClient requestParticipantToShareScreen:forConversation:];
-[TUConversationManagerXPCClient remoteScreenShareEndedWithReason:];
-[TUConversationManagerXPCClient setActivityAuthorizedBundleIdentifiers:];
-[TUConversationManagerXPCClient activateLink:completionHandler:];
-[TUConversationManagerXPCClient conversation:participant:addedNotice:];
-[TUConversationManagerXPCClient checkLinkValidity:completionHandler:];
-[TUConversationManagerXPCClient invalidate];
-[TUConversationManagerXPCClient setIgnoreLetMeInRequests:forConversation:];
-[TUConversationManagerXPCClient buzzMember:destinationID:invitationContext:conversation:];
-[TUConversationManagerXPCClient setAdvertisementsOnSystem:];
-[TUConversationManagerXPCClient setDelegate:];
-[TUConversationManagerXPCClient receivedTrackedPendingMember:forConversationLink:];
-[TUConversationManagerXPCClient setScreenSharingAvailable:];
-[TUConversationManagerXPCClient didChangeConversationAdvertisement:];
-[TUConversationManagerXPCClient approvePendingMember:forConversation:];
-[TUConversationManagerXPCClient conversation:didChangeSceneAssociationForActivitySession:];
-[TUConversationManagerXPCClient _invokeCompletionHandler:];
-[TUConversationManagerXPCClient incomingPendingConversationsByGroupUUID];
-[TUConversationManagerXPCClient addCollaborationIdentifier:collaborationURL:cloudKitAppBundleIDs:forConversationUUID:];
-[TUConversationManagerXPCClient updateActivatedConversationLinks:];
-[TUConversationManagerXPCClient requestScreenSharingPickerForCallUUID:withContentStyle:];
-[TUConversationManagerXPCClient addRemoteMembers:otherInvitedHandles:invitationPreferences:toConversation:];
-[TUConversationManagerXPCClient addDisclosedCollaborationInitiator:toConversationUUID:];
-[TUConversationManagerXPCClient shouldPopulatePseudonymsOnSetup];
-[TUConversationManagerXPCClient updateActivityAuthorizedBundleIdentifierState:];
-[TUConversationManagerXPCClient conversation:buzzedMember:];
-[TUConversationManagerXPCClient joinConversationWithRequest:];
-[TUConversationManagerXPCClient setPseudonymsByCallUUID:];
-[TUConversationManagerXPCClient getActiveLinksWithCreatedOnly:completionHandler:];
-[TUConversationManagerXPCClient accessibilityLinkPseudonymsAmongPseudonyms:completionHandler:];
-[TUConversationManagerXPCClient setSharePlayAvailable:];
-[TUConversationManagerXPCClient startTrackingCollaborationWithIdentifier:collaborationURL:cloudKitAppBundleIDs:forConversationUUID:completionHandler:];
-[TUConversationManagerXPCClient interpreterRequestWithID:didUpdateToState:];
-[TUConversationManagerXPCClient delegate];
-[TUConversationManagerXPCClient setDownlinkMuted:forRemoteParticipantsInConversation:];
-[TUConversationManagerXPCClient updateIncomingPendingConversationsByGroupUUID:];
-[TUConversationManagerXPCClient setSupportsMessagesGroupProviding:];
-[TUConversationManagerXPCClient getMessagesGroupDetailsForConversationUUID:completionHandler:];
-[TUConversationManagerXPCClient setSharePlayHandedOff:onConversationWithUUID:];
-[TUConversationManagerXPCClient addTestActiveQRParticipant:identifier:tuConversation:];
-[TUConversationManagerXPCClient setMediaDelegate:];
-[TUConversationManagerXPCClient conversation:screenSharingChangedForParticipant:];
-[TUConversationManagerXPCClient autoSharePlayEnabled];
-[TUConversationManagerXPCClient requestScreenSharingPickerForConversationUUID:withContentStyle:];
-[TUConversationManagerXPCClient setAutoSharePlayEnabled:];
-[TUConversationManagerXPCClient prepareConversationWithUUID:withHandoffContext:];
-[TUConversationManagerXPCClient conversation:didChangeStateForActivitySession:];
-[TUConversationManagerXPCClient conversationUpdateMessagesGroupPhoto:];
-[TUConversationManagerXPCClient refreshActiveConversations];
-[TUConversationManagerXPCClient interpreterRequestWithID:debugSendLink:toHandle:];
-[TUConversationManagerXPCClient setLocalMemberNickname:forConversationUUID:reason:];
-[TUConversationManagerXPCClient generateLinkWithInvitedMemberHandles:linkLifetimeScope:completionHandler:];
-[TUConversationManagerXPCClient updateConversationsByGroupUUID:];
-[TUConversationManagerXPCClient conversation:participant:didUpdateNickname:reason:];
-[TUConversationManagerXPCClient setConversationsByGroupUUID:];
-[TUConversationManagerXPCClient registerMessagesGroupUUIDForConversationUUID:];
-[TUConversationManagerXPCClient updateLocalParticipantToAVLessWithPresentationMode:forConversationUUID:];
-[TUConversationManagerXPCClient screenSharingAvailable];
-[TUConversationManagerXPCClient cancelOrDenyScreenShareRequest:forConversation:];
-[TUConversationManagerXPCClient activityAuthorizedBundleIdentifiers];
-[TUConversationManagerXPCClient leaveActivitySession:onConversation:];
-[TUConversationManagerXPCClient setShouldConnectToHost:];
-[TUConversationManagerXPCClient conversationUpdatedMessagesGroupPhoto:];
-[TUConversationManagerXPCClient addInvitedMemberHandles:toConversationLink:completionHandler:];
-[TUConversationManagerXPCClient startAlignmentTimeOutForNearbyMembers:forConversation:];
-[TUConversationManagerXPCClient updatePseudonymsByCallUUID:];
-[TUConversationManagerXPCClient updateConversationWithUUID:participantPresentationContexts:];
-[TUConversationManagerXPCClient shouldConnectToHost];
-[TUConversationManagerXPCClient setHasRequestedInitialState:];
-[TUConversationManagerXPCClient invalidateLink:deleteReason:completionHandler:];
-[TUConversationManagerXPCClient getNeedsDisclosureOfCollaborationInitiator:forConversationUUID:completionHandler:];
-[TUConversationManagerXPCClient removeCollaborationIdentifier:forConversationUUID:];
-[TUConversationManagerXPCClient fetchUpcomingNoticeWithCompletionHandler:];
-[TUConversationManagerXPCClient setGridDisplayMode:conversation:];
-[TUConversationManagerXPCClient _requestInitialStateIfNecessary];
-[TUConversationManagerXPCClient activeParticipant:removedHighlightFromConversation:highlightIdentifier:];
-[TUConversationManagerXPCClient conversation:participant:didReact:];
-[TUConversationManagerXPCClient asynchronousServerWithErrorHandler:];
-[TUConversationManagerXPCClient conversationsByGroupUUID];
-[TUConversationManagerXPCClient mediaDelegate];
-[TUConversationManagerXPCClient presentDismissalAlertForActivitySession:onConversation:];
-[TUConversationManagerXPCClient reactionsDelegate];
-[TUConversationManagerXPCClient scheduleConversationLinkCheckInInitial:];
-[TUConversationManagerXPCClient activeParticipant:addedHighlightToConversation:highlightIdentifier:oldHighlightIdentifier:isFirstAdd:];
-[TUConversationManagerXPCClient updateMessagesGroupName:onConversation:];
-[TUConversationManagerXPCClient generateLinkForConversation:completionHandler:];
-[TUConversationManagerXPCClient pseudonymsByCallUUID];
-[TUConversationManagerXPCClient rejectPendingMember:forConversation:];
-[TUConversationManagerXPCClient remoteScreenShareAttributesChanged:isLocallySharing:];
-[TUConversationManagerXPCClient endActivitySession:onConversation:];
```
