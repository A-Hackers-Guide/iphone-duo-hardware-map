# `SBKeyboardFocusSceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBKeyboardFocusResolutionStageSceneProviding`, `SBKeyboardFocusResolutionPipelineFactory`, `BSDescriptionStreaming`, `SBKeyboardFocusCoalitionMemberDelegate`, `SBFocusRedirectResolutionStageDelegate`, `SBSystemUISceneResolutionStageDelegate`, `SBSpringBoardFocusLockResolutionStageDelegate`, `SBKeyboardArbiterResolutionStageDelegate`, `SBKeyboardFocusAccessibilityResolutionDeelgate`, `SBSceneManagerObserver`, `SBTransientOverlayScenePresenterObserver`, `BSInvalidatable`
- 21 instance variables, 25 properties, 72 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _sbWindowScene;
@"SBKeyboardFocusTarget" _sbWindowSceneFocusTarget;
@"BKSHIDEventDeferringPredicate" _bufferingPredicate;
@"SBKeyboardFocusCoalitionMember" _coalitionMember;
@"<BSInvalidatable>" _stateCaptureAssertion;
B _updatingPreferences;
@"NSString" _debugName;
q _coalitionAffinity;
@"<SBKeyboardFocusSceneControllerDelegate>" _delegate;
@"SBKeyboardFocusCoalition" _coalition;
@"<_SBKeyboardFocusSceneControllerDependencyProviding>" _dependencies;
@"SBKeyboardFocusResolutionPipeline" _pipeline;
@"BSCompoundAssertion" _springBoardFocusRedirections;
@"BSCompoundAssertion" _springBoardFocusLockAssertions;
@"NSSet" _previousDependencyReasonsSpringShouldHaveFocus;
@"BSCompoundAssertion" _suppressKeyboardFocusEvaluationAssertion;
@"<SBKeyboardFocusPolicyEnforcer>" _policyEnforcer;
@"SBKeyboardFocusPolicy" _preferredPolicy;
@"SBKeyboardFocusPolicy" _enforcedPolicy;
@"SBKeyboardFocusTarget" _lastKeyboardArbiterSuggestedFocusTargetExcludingFocusLocks;
@"_SBRecentlyUsedSceneIdentityCache" _recentlyUsedScenes;
```

## Properties

```
@property (T@"<_SBKeyboardFocusSceneControllerDependencyProviding>",&,N,V_dependencies) dependencies;
@property (T@"NSString",C,N,V_debugName) debugName;
@property (Tq,N,V_coalitionAffinity) coalitionAffinity;
@property (T@"SBKeyboardFocusResolutionPipeline",&,N,V_pipeline) pipeline;
@property (T@"BSCompoundAssertion",&,N,V_springBoardFocusRedirections) springBoardFocusRedirections;
@property (T@"BSCompoundAssertion",&,N,V_springBoardFocusLockAssertions) springBoardFocusLockAssertions;
@property (T@"NSSet",C,N,V_previousDependencyReasonsSpringShouldHaveFocus) previousDependencyReasonsSpringShouldHaveFocus;
@property (T@"BSCompoundAssertion",&,N,V_suppressKeyboardFocusEvaluationAssertion) suppressKeyboardFocusEvaluationAssertion;
@property (T@"<SBKeyboardFocusPolicyEnforcer>",&,N,V_policyEnforcer) policyEnforcer;
@property (T@"SBKeyboardFocusPolicy",&,N,V_preferredPolicy) preferredPolicy;
@property (T@"SBKeyboardFocusPolicy",&,N,V_enforcedPolicy) enforcedPolicy;
@property (T@"SBKeyboardFocusTarget",&,N,V_lastKeyboardArbiterSuggestedFocusTargetExcludingFocusLocks) lastKeyboardArbiterSuggestedFocusTargetExcludingFocusLocks;
@property (T@"_SBRecentlyUsedSceneIdentityCache",&,N,V_recentlyUsedScenes) recentlyUsedScenes;
@property (T@"SBWindowScene",R,W,N) sbWindowScene;
@property (T@"SBKeyboardFocusTarget",R,N) sbWindowSceneFocusTarget;
@property (TB,R,N) supportsFlexibleWindowing;
@property (T@"<SBKeyboardFocusSceneControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"SBKeyboardFocusCoalition",&,N,V_coalition) coalition;
@property (T@"SBKeyboardFocusTarget",R,N) springBoardSceneFocusTarget;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"FBScene",R,N) systemUISceneRequestingFocus;
@property (T@"NSSet",R,N) springBoardFocusLockReasons;
```

## Instance methods

```
-[SBKeyboardFocusSceneController dependencies];
-[SBKeyboardFocusSceneController sceneManager:didAddExternalForegroundApplicationSceneHandle:];
-[SBKeyboardFocusSceneController setPipeline:];
-[SBKeyboardFocusSceneController transientOverlayScenePresenter:didDismissViewController:wasTopmostPresentation:];
-[SBKeyboardFocusSceneController debugDescription];
-[SBKeyboardFocusSceneController sceneManager:didRemoveExternalForegroundApplicationSceneHandle:];
-[SBKeyboardFocusSceneController setDebugName:];
-[SBKeyboardFocusSceneController setSuppressKeyboardFocusEvaluationAssertion:];
-[SBKeyboardFocusSceneController sceneManager:willRemoveExternalForegroundApplicationSceneHandle:withReason:];
-[SBKeyboardFocusSceneController recentlyUsedScenes];
-[SBKeyboardFocusSceneController invalidate];
-[SBKeyboardFocusSceneController setDelegate:];
-[SBKeyboardFocusSceneController setCoalition:];
-[SBKeyboardFocusSceneController removeKeyboardFocusFromScene:];
-[SBKeyboardFocusSceneController debugName];
-[SBKeyboardFocusSceneController shouldPreventFocusForSceneWithIdentityToken:];
-[SBKeyboardFocusSceneController delegate];
-[SBKeyboardFocusSceneController suppressKeyboardFocusEvaluationAssertion];
-[SBKeyboardFocusSceneController pipeline];
-[SBKeyboardFocusSceneController description];
-[SBKeyboardFocusSceneController appendDescriptionToStream:];
-[SBKeyboardFocusSceneController shouldAllowInteractionTrackingKeyboardFocusUpdateForWindow:];
-[SBKeyboardFocusSceneController setRecentlyUsedScenes:];
-[SBKeyboardFocusSceneController setDependencies:];
-[SBKeyboardFocusSceneController coalition];
-[SBKeyboardFocusSceneController enforcedPolicy];
-[SBKeyboardFocusSceneController systemUISceneRequestingFocus];
-[SBKeyboardFocusSceneController isCoverSheetHostingAnApp];
-[SBKeyboardFocusSceneController setEnforcedPolicy:];
-[SBKeyboardFocusSceneController preferredPolicy];
-[SBKeyboardFocusSceneController _topmostZOrderedSceneExcluding:];
-[SBKeyboardFocusSceneController _bootDidComplete:];
-[SBKeyboardFocusSceneController _focusLockSpringBoardWindow:forReason:];
-[SBKeyboardFocusSceneController _removeSceneFromRecentsAndUpdateKeyboardFocusTargetIfNeeded:reason:];
-[SBKeyboardFocusSceneController _requestPolicyReevaluationForReason:];
-[SBKeyboardFocusSceneController _updateKeyboardFocusTargetFromPreviouslyFocusedSceneIdentity:pid:];
-[SBKeyboardFocusSceneController _updatePolicyForReason:];
-[SBKeyboardFocusSceneController accessibilityKeyboardFocusOverrideTarget];
-[SBKeyboardFocusSceneController bufferEventsForReason:generation:];
-[SBKeyboardFocusSceneController coalitionAffinity];
-[SBKeyboardFocusSceneController coalitionMemberFocusDidChange:];
-[SBKeyboardFocusSceneController controlsScene:];
-[SBKeyboardFocusSceneController displayDidBecomeActive];
-[SBKeyboardFocusSceneController focusLockSpringBoardForReason:];
-[SBKeyboardFocusSceneController focusLockSpringBoardWindow:forReason:];
-[SBKeyboardFocusSceneController generateUpdatedPreferencesForCoalitionMember:reason:];
-[SBKeyboardFocusSceneController initWithWindowScene:dependencies:];
-[SBKeyboardFocusSceneController initWithWindowScene:policyEnforcer:pipelineFactory:dependencies:];
-[SBKeyboardFocusSceneController keyboardArbiterSuggestedFocusTarget:];
-[SBKeyboardFocusSceneController keyboardFocusRedirectionForTarget:];
-[SBKeyboardFocusSceneController lastKeyboardArbiterSuggestedFocusTargetExcludingFocusLocks];
-[SBKeyboardFocusSceneController mostRecentKeyboardArbiterSuggestedTarget];
-[SBKeyboardFocusSceneController newPipeline];
-[SBKeyboardFocusSceneController policyEnforcer];
-[SBKeyboardFocusSceneController previousDependencyReasonsSpringShouldHaveFocus];
-[SBKeyboardFocusSceneController redirectSpringBoardLockFocusForReason:toProcessidentifier:toSceneIdentityToken:];
-[SBKeyboardFocusSceneController requestPolicyReevaluationForReason:];
-[SBKeyboardFocusSceneController sbWindowScene];
-[SBKeyboardFocusSceneController sbWindowSceneFocusTarget];
-[SBKeyboardFocusSceneController sceneForFocusTarget:];
-[SBKeyboardFocusSceneController setCoalitionAffinity:];
-[SBKeyboardFocusSceneController setLastKeyboardArbiterSuggestedFocusTargetExcludingFocusLocks:];
-[SBKeyboardFocusSceneController setPolicyEnforcer:];
-[SBKeyboardFocusSceneController setPreferredPolicy:];
-[SBKeyboardFocusSceneController setPreviousDependencyReasonsSpringShouldHaveFocus:];
-[SBKeyboardFocusSceneController setSpringBoardFocusLockAssertions:];
-[SBKeyboardFocusSceneController setSpringBoardFocusRedirections:];
-[SBKeyboardFocusSceneController springBoardFocusLockAssertions];
-[SBKeyboardFocusSceneController springBoardFocusLockReasons];
-[SBKeyboardFocusSceneController springBoardFocusRedirections];
-[SBKeyboardFocusSceneController springBoardSceneFocusTarget];
-[SBKeyboardFocusSceneController supportsFlexibleWindowing];
```
