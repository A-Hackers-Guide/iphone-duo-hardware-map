# `TUConversationManagerDataSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 12 properties, 89 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",R,C,N) advertisementsOnSystem;
@property (T@"NSDictionary",R,C,N) conversationsByGroupUUID;
@property (T@"NSDictionary",R,C,N) incomingPendingConversationsByGroupUUID;
@property (T@"NSDictionary",R,C,N) pseudonymsByCallUUID;
@property (T@"NSSet",R,C,N) activatedConversationLinks;
@property (T@"NSDictionary",R,C,N) activityAuthorizedBundleIdentifiers;
@property (TB,N) autoSharePlayEnabled;
@property (TB,R,N) isSharePlayAvailable;
@property (TB,R,N) isScreenSharingAvailable;
@property (T@"<TUConversationManagerDataSourceDelegate>",W,N) delegate;
@property (T@"<TUConversationMediaControllerDataSourceDelegate>",W,N) mediaDelegate;
@property (T@"<TUConversationReactionsControllerDataSourceDelegate>",W,N) reactionsDelegate;
```

## Instance methods

```
-[TUConversationManagerDataSource leaveConversationWithUUID:];
-[TUConversationManagerDataSource startAlignmentTimeOutForNearbySessionForConversation:];
-[TUConversationManagerDataSource getInactiveLinkWithCompletionHandler:];
-[TUConversationManagerDataSource addScreenSharingType:forConversation:];
-[TUConversationManagerDataSource advertisementsOnSystem];
-[TUConversationManagerDataSource setLinkName:forConversationLink:completionHandler:];
-[TUConversationManagerDataSource setUsingAirplay:onActivitySession:onConversationWithUUID:];
-[TUConversationManagerDataSource setPresentationAspectRatioStyle:conversation:];
-[TUConversationManagerDataSource setLocalParticipantAudioVideoMode:forConversationUUID:];
-[TUConversationManagerDataSource removeConversationNoticeWithUUID:];
-[TUConversationManagerDataSource isSharePlayAvailable];
-[TUConversationManagerDataSource markCollaborationWithIdentifierOpened:forConversationUUID:];
-[TUConversationManagerDataSource launchAppForInterpreterRequestForConversationUUID:bundleID:requestID:completionHandler:];
-[TUConversationManagerDataSource setLocalParticipantCluster:forConversation:];
-[TUConversationManagerDataSource kickMember:conversation:];
-[TUConversationManagerDataSource updateRemoteControlStatus:onConversation:];
-[TUConversationManagerDataSource reportDualCaptureMetric:forConversationGroupUUID:];
-[TUConversationManagerDataSource activatedConversationLinks];
-[TUConversationManagerDataSource getLatestRemoteScreenShareAttributesWithCompletionHandler:];
-[TUConversationManagerDataSource launchApplicationForActivitySessionUUID:authorizedExternally:forceBackground:completionHandler:];
-[TUConversationManagerDataSource isScreenSharingAvailable];
-[TUConversationManagerDataSource updateExternalParticipants:];
-[TUConversationManagerDataSource startInterpreterRequestWithBundleID:conversationUUID:requestID:completionHandler:];
-[TUConversationManagerDataSource stopInterpreterRequestForConversationUUID:bundleID:requestID:completionHandler:];
-[TUConversationManagerDataSource createActivitySession:onConversation:options:];
-[TUConversationManagerDataSource setScreenEnabled:withScreenShareAttributes:forConversationWithUUID:];
-[TUConversationManagerDataSource registerWithCompletionHandler:];
-[TUConversationManagerDataSource setReactionsDelegate:];
-[TUConversationManagerDataSource addCollaborationDictionary:forConversationWithUUID:fromMe:];
-[TUConversationManagerDataSource setActivityAuthorization:forBundleIdentifier:];
-[TUConversationManagerDataSource linkSyncStateIncludeLinks:WithCompletion:];
-[TUConversationManagerDataSource setDownlinkMuted:forParticipants:inConversation:completionHandler:];
-[TUConversationManagerDataSource renewLink:expirationDate:reason:completionHandler:];
-[TUConversationManagerDataSource activateConversationNoticeWithActionURL:bundleIdentifier:];
-[TUConversationManagerDataSource requestParticipantToShareScreen:forConversation:];
-[TUConversationManagerDataSource activateLink:completionHandler:];
-[TUConversationManagerDataSource checkLinkValidity:completionHandler:];
-[TUConversationManagerDataSource invalidate];
-[TUConversationManagerDataSource setIgnoreLetMeInRequests:forConversation:];
-[TUConversationManagerDataSource buzzMember:destinationID:invitationContext:conversation:];
-[TUConversationManagerDataSource setDelegate:];
-[TUConversationManagerDataSource approvePendingMember:forConversation:];
-[TUConversationManagerDataSource incomingPendingConversationsByGroupUUID];
-[TUConversationManagerDataSource addCollaborationIdentifier:collaborationURL:cloudKitAppBundleIDs:forConversationUUID:];
-[TUConversationManagerDataSource requestScreenSharingPickerForCallUUID:withContentStyle:];
-[TUConversationManagerDataSource addRemoteMembers:otherInvitedHandles:invitationPreferences:toConversation:];
-[TUConversationManagerDataSource addDisclosedCollaborationInitiator:toConversationUUID:];
-[TUConversationManagerDataSource joinConversationWithRequest:];
-[TUConversationManagerDataSource getActiveLinksWithCreatedOnly:completionHandler:];
-[TUConversationManagerDataSource startTrackingCollaborationWithIdentifier:collaborationURL:cloudKitAppBundleIDs:forConversationUUID:completionHandler:];
-[TUConversationManagerDataSource delegate];
-[TUConversationManagerDataSource setDownlinkMuted:forRemoteParticipantsInConversation:];
-[TUConversationManagerDataSource setSupportsMessagesGroupProviding:];
-[TUConversationManagerDataSource getMessagesGroupDetailsForConversationUUID:completionHandler:];
-[TUConversationManagerDataSource setSharePlayHandedOff:onConversationWithUUID:];
-[TUConversationManagerDataSource setMediaDelegate:];
-[TUConversationManagerDataSource autoSharePlayEnabled];
-[TUConversationManagerDataSource requestScreenSharingPickerForConversationUUID:withContentStyle:];
-[TUConversationManagerDataSource setAutoSharePlayEnabled:];
-[TUConversationManagerDataSource prepareConversationWithUUID:withHandoffContext:];
-[TUConversationManagerDataSource conversationUpdateMessagesGroupPhoto:];
-[TUConversationManagerDataSource refreshActiveConversations];
-[TUConversationManagerDataSource setLocalMemberNickname:forConversationUUID:reason:];
-[TUConversationManagerDataSource generateLinkWithInvitedMemberHandles:linkLifetimeScope:completionHandler:];
-[TUConversationManagerDataSource registerMessagesGroupUUIDForConversationUUID:];
-[TUConversationManagerDataSource updateLocalParticipantToAVLessWithPresentationMode:forConversationUUID:];
-[TUConversationManagerDataSource cancelOrDenyScreenShareRequest:forConversation:];
-[TUConversationManagerDataSource activityAuthorizedBundleIdentifiers];
-[TUConversationManagerDataSource leaveActivitySession:onConversation:];
-[TUConversationManagerDataSource addInvitedMemberHandles:toConversationLink:completionHandler:];
-[TUConversationManagerDataSource startAlignmentTimeOutForNearbyMembers:forConversation:];
-[TUConversationManagerDataSource updateConversationWithUUID:participantPresentationContexts:];
-[TUConversationManagerDataSource invalidateLink:deleteReason:completionHandler:];
-[TUConversationManagerDataSource getNeedsDisclosureOfCollaborationInitiator:forConversationUUID:completionHandler:];
-[TUConversationManagerDataSource removeCollaborationIdentifier:forConversationUUID:];
-[TUConversationManagerDataSource fetchUpcomingNoticeWithCompletionHandler:];
-[TUConversationManagerDataSource setGridDisplayMode:conversation:];
-[TUConversationManagerDataSource conversationsByGroupUUID];
-[TUConversationManagerDataSource mediaDelegate];
-[TUConversationManagerDataSource presentDismissalAlertForActivitySession:onConversation:];
-[TUConversationManagerDataSource reactionsDelegate];
-[TUConversationManagerDataSource scheduleConversationLinkCheckInInitial:];
-[TUConversationManagerDataSource updateMessagesGroupName:onConversation:];
-[TUConversationManagerDataSource generateLinkForConversation:completionHandler:];
-[TUConversationManagerDataSource pseudonymsByCallUUID];
-[TUConversationManagerDataSource rejectPendingMember:forConversation:];
-[TUConversationManagerDataSource endActivitySession:onConversation:];
-[TUConversationManagerDataSource accessibilityLinkPseudonymsAmongPseudonyms:completionHandler:];
-[TUConversationManagerDataSource addTestActiveQRParticipant:identifier:tuConversation:];
```
