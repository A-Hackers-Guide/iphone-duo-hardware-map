# `TUConversationManagerXPCClient` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `TUConversationMediaControllerXPCClient`, `TUConversationMessagesGroupProviderXPCClient`, `TUConversationReactionsControllerXPCClient`
- 0 instance variables, 0 properties, 27 instance methods, 0 class methods

## Instance methods

```
-[TUConversationManagerXPCClient conversation:receivedActivitySessionEvent:];
-[TUConversationManagerXPCClient conversation:collaborationStateChanged:highlightIdentifier:];
-[TUConversationManagerXPCClient conversation:appLaunchState:forActivitySession:];
-[TUConversationManagerXPCClient addedCollaborationDictionary:forConversation:];
-[TUConversationManagerXPCClient screenSharingAvailableChanged:];
-[TUConversationManagerXPCClient sharePlayAvailableChanged:];
-[TUConversationManagerXPCClient conversation:addedMembersLocally:];
-[TUConversationManagerXPCClient remoteScreenShareEndedWithReason:];
-[TUConversationManagerXPCClient conversation:participant:addedNotice:];
-[TUConversationManagerXPCClient receivedTrackedPendingMember:forConversationLink:];
-[TUConversationManagerXPCClient didChangeConversationAdvertisement:];
-[TUConversationManagerXPCClient conversation:didChangeSceneAssociationForActivitySession:];
-[TUConversationManagerXPCClient updateActivatedConversationLinks:];
-[TUConversationManagerXPCClient updateActivityAuthorizedBundleIdentifierState:];
-[TUConversationManagerXPCClient conversation:buzzedMember:];
-[TUConversationManagerXPCClient interpreterRequestWithID:didUpdateToState:];
-[TUConversationManagerXPCClient updateIncomingPendingConversationsByGroupUUID:];
-[TUConversationManagerXPCClient conversation:screenSharingChangedForParticipant:];
-[TUConversationManagerXPCClient conversation:didChangeStateForActivitySession:];
-[TUConversationManagerXPCClient interpreterRequestWithID:debugSendLink:toHandle:];
-[TUConversationManagerXPCClient updateConversationsByGroupUUID:];
-[TUConversationManagerXPCClient conversation:participant:didUpdateNickname:reason:];
-[TUConversationManagerXPCClient conversationUpdatedMessagesGroupPhoto:];
-[TUConversationManagerXPCClient updatePseudonymsByCallUUID:];
-[TUConversationManagerXPCClient activeParticipant:removedHighlightFromConversation:highlightIdentifier:];
-[TUConversationManagerXPCClient activeParticipant:addedHighlightToConversation:highlightIdentifier:oldHighlightIdentifier:isFirstAdd:];
-[TUConversationManagerXPCClient remoteScreenShareAttributesChanged:isLocallySharing:];
```
