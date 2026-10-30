# `SBSwitcherTraitsAssistant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBTraitsParticipantDelegate`
- 11 instance variables, 7 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"SBTraitsSwitcherPolicySpecifier" _switcherPolicySpecifier;
@"SBTraitsSwitcherLiveOverlayPolicySpecifier" _liveOverlaysPolicySpecifier;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
@"TRAParticipant" _guidingPortraitOnlyParticipant;
@"TRAParticipant" _guidingLandscapeOnlyParticipant;
@"NSMutableDictionary" _guidingSceneOrientationRequestParticipantsMap;
@"NSMutableDictionary" _participantUniqueIDToAssociatedParticipantMap;
@"SBTraitsPipelineBlockBasedPolicySpecifier" _blockBasedPolicySpecifier;
@"TRAArbiter" _traitsArbiter;
@"TRAParticipant" _switcherParticipant;
@"<SBSwitcherTraitsAssistantDelegate>" _delegate;
```

## Properties

```
@property (T@"TRAArbiter",R,W,N,V_traitsArbiter) traitsArbiter;
@property (T@"TRAParticipant",R,W,N,V_switcherParticipant) switcherParticipant;
@property (T@"<SBSwitcherTraitsAssistantDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSwitcherTraitsAssistant _stateCaptureDescription];
-[SBSwitcherTraitsAssistant dealloc];
-[SBSwitcherTraitsAssistant didChangeSettingsForParticipant:context:];
-[SBSwitcherTraitsAssistant updatePreferencesForParticipant:updater:];
-[SBSwitcherTraitsAssistant delegate];
-[SBSwitcherTraitsAssistant _setupStateCapture];
-[SBSwitcherTraitsAssistant traitsArbiter];
-[SBSwitcherTraitsAssistant _guidingPortraitOnlyLiveOverlay];
-[SBSwitcherTraitsAssistant _addGuidingParticipantsIdentifiersToArray:];
-[SBSwitcherTraitsAssistant _addGuidingSpecifierIfNeeded];
-[SBSwitcherTraitsAssistant _evaluateIfGuidingSpecifierIsSillNeeded];
-[SBSwitcherTraitsAssistant _guidingLandscapeOnlyLiveOverlay];
-[SBSwitcherTraitsAssistant _guidingSceneOrientationRequestParticipantWithMask:];
-[SBSwitcherTraitsAssistant _handleOrientationLockRequest:];
-[SBSwitcherTraitsAssistant _handleUpdateRequest:];
-[SBSwitcherTraitsAssistant _isContentContainerAspectRatioPortrait];
-[SBSwitcherTraitsAssistant _setupGuidingRelationshipIfNeededForParticipant:withSceneHandle:];
-[SBSwitcherTraitsAssistant _setupPolicySpecifierIfNeeded];
-[SBSwitcherTraitsAssistant _updateAcquiredParticipantsPolicies:];
-[SBSwitcherTraitsAssistant _updateArbitrationForElementsParticipants:sceneHandleProviderBlock:forceResolution:reason:orientationActuationContext:];
-[SBSwitcherTraitsAssistant _updateGuidingSpecifiersIfNeededForParticipants:sceneHandleProviderBlock:];
-[SBSwitcherTraitsAssistant createTraitsParticipantsForLayoutElements:outParticipantsByElementIdentifier:outDelegatesByParticipant:outPrimaryDelegate:];
-[SBSwitcherTraitsAssistant initWithTraitsArbiter:switcherParticipant:delegate:];
-[SBSwitcherTraitsAssistant switcherParticipant];
-[SBSwitcherTraitsAssistant updateAllParticipants:withPrimaryDelegate:nonPrimaryPolicy:primaryPolicy:ownPolicy:orientationActuationContext:];
```
