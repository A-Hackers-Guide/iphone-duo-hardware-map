# `TUCollaborationManager`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUCollaborationProviderDelegate`, `TUConversationManagerDelegate`
- 12 instance variables, 16 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _isIpad;
@"<TUCollaborationProvider>" _collaborationProvider;
@"<TUCollaborationManagerDelegate>" _delegate;
@"NSMutableSet" _pendingHighlightIdentifiers;
@"NSMutableDictionary" _originatingParticipantByHighlightIdentifier;
@"NSMutableDictionary" _highlightsByIdentifier;
@"NSMutableDictionary" _conversationsByHighlightIdentifier;
@"<TUFeatureFlags>" _featureFlags;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _collaborationStateByIdentifier;
@"NSString" _pendingCollaborationToAdd;
@"TUConversation" _pendingConversationToAdd;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"NSMutableDictionary",R,N,V_collaborationStateByIdentifier) collaborationStateByIdentifier;
@property (T@"NSString",&,N,V_pendingCollaborationToAdd) pendingCollaborationToAdd;
@property (T@"TUConversation",&,N,V_pendingConversationToAdd) pendingConversationToAdd;
@property (T@"<TUCollaborationProvider>",R,N,V_collaborationProvider) collaborationProvider;
@property (T@"<TUCollaborationManagerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSMutableSet",&,N,V_pendingHighlightIdentifiers) pendingHighlightIdentifiers;
@property (T@"NSMutableDictionary",&,N,V_originatingParticipantByHighlightIdentifier) originatingParticipantByHighlightIdentifier;
@property (T@"NSMutableDictionary",&,N,V_highlightsByIdentifier) highlightsByIdentifier;
@property (T@"NSMutableDictionary",&,N,V_conversationsByHighlightIdentifier) conversationsByHighlightIdentifier;
@property (T@"<TUFeatureFlags>",R,N,V_featureFlags) featureFlags;
@property (TB,R,N,V_isIpad) isIpad;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUCollaborationManager participant:removedHighlightFromConversation:highlightIdentifier:];
-[TUCollaborationManager initWithCollaborationProvider:featureFlags:deviceSupport:];
-[TUCollaborationManager collaborationForConversation:];
-[TUCollaborationManager collaborationStateByIdentifier];
-[TUCollaborationManager participant:reAddedHighlightToConversation:highlightIdentifier:];
-[TUCollaborationManager setConversationsByHighlightIdentifier:];
-[TUCollaborationManager setPendingConversationToAdd:];
-[TUCollaborationManager associateCollaborationWithNewConversation:];
-[TUCollaborationManager notifyDelegateOfHighlightChanged:onConversation:];
-[TUCollaborationManager vendNoticeForCollaboration:participant:forConversation:type:];
-[TUCollaborationManager setHighlightsByIdentifier:];
-[TUCollaborationManager pendingCollaborationToAdd];
-[TUCollaborationManager conversationManager:stateChangedForConversation:];
-[TUCollaborationManager queue];
-[TUCollaborationManager pendingHighlightIdentifiers];
-[TUCollaborationManager setPendingCollaborationToAdd:];
-[TUCollaborationManager collaborationsDidChange:];
-[TUCollaborationManager isCollaborationLocallyInitiatedForConversation:];
-[TUCollaborationManager participant:addedHighlightToConversation:highlightIdentifier:oldHighlightIdentifier:isFirstAdd:];
-[TUCollaborationManager conversationsByHighlightIdentifier];
-[TUCollaborationManager setDelegate:];
-[TUCollaborationManager queueCollaborationIdentifierForCollaboration:toConversation:];
-[TUCollaborationManager isIpad];
-[TUCollaborationManager originatingParticipantByHighlightIdentifier];
-[TUCollaborationManager startTrackingCollaborationIfNecessaryAndNotifyDelegate:forConversation:];
-[TUCollaborationManager highlightsByIdentifier];
-[TUCollaborationManager setCollaborationState:forCollaborationIdentifier:];
-[TUCollaborationManager stopTrackingHighlightForConversation:];
-[TUCollaborationManager delegate];
-[TUCollaborationManager collaborationStateForConversation:];
-[TUCollaborationManager initWithCollaborationProvider:];
-[TUCollaborationManager setPendingHighlightIdentifiers:];
-[TUCollaborationManager collaborationProvider];
-[TUCollaborationManager setOriginatingParticipantByHighlightIdentifier:];
-[TUCollaborationManager pendingConversationToAdd];
-[TUCollaborationManager featureFlags];
```
