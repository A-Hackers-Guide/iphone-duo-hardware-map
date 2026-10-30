# `SBKeyboardFocusCoalition`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BSInvalidatable`
- 8 instance variables, 15 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _invalidated;
@"<SBKeyboardFocusPolicyEnforcer>" _policyEnforcer;
@"NSString" _debugName;
@"<SBKeyboardFocusCoalitionDelegate>" _delegate;
@"SBKeyboardFocusPolicy" _enforcedPolicy;
@"<BSInvalidatable>" _stateCaptureHandle;
@"NSMutableArray" _internalMembers;
@"BSCompoundAssertion" _suppressKeyboardFocusEvaluationAssertion;
```

## Properties

```
@property (T@"NSString",C,N,V_debugName) debugName;
@property (T@"<BSInvalidatable>",&,N,V_stateCaptureHandle) stateCaptureHandle;
@property (T@"NSMutableArray",&,N,V_internalMembers) internalMembers;
@property (T@"BSCompoundAssertion",&,N,V_suppressKeyboardFocusEvaluationAssertion) suppressKeyboardFocusEvaluationAssertion;
@property (T@"NSArray",R,N) members;
@property (T@"SBKeyboardFocusPolicy",&,N,V_enforcedPolicy) enforcedPolicy;
@property (TB,R,N,GisInvalidated,V_invalidated) invalidated;
@property (T@"<SBKeyboardFocusPolicyEnforcer>",&,N,V_policyEnforcer) policyEnforcer;
@property (T@"<SBKeyboardFocusCoalitionDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisKeyboardFocusEvaluationSuppressed) keyboardFocusEvaluationSuppressed;
@property (T@"NSSet",R,N) keyboardFocusEvaluationSupressionReasons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBKeyboardFocusCoalition debugDescription];
-[SBKeyboardFocusCoalition init];
-[SBKeyboardFocusCoalition setStateCaptureHandle:];
-[SBKeyboardFocusCoalition setDebugName:];
-[SBKeyboardFocusCoalition dealloc];
-[SBKeyboardFocusCoalition setSuppressKeyboardFocusEvaluationAssertion:];
-[SBKeyboardFocusCoalition isInvalidated];
-[SBKeyboardFocusCoalition succinctDescription];
-[SBKeyboardFocusCoalition invalidate];
-[SBKeyboardFocusCoalition setDelegate:];
-[SBKeyboardFocusCoalition debugName];
-[SBKeyboardFocusCoalition delegate];
-[SBKeyboardFocusCoalition suppressKeyboardFocusEvaluationAssertion];
-[SBKeyboardFocusCoalition stateCaptureHandle];
-[SBKeyboardFocusCoalition description];
-[SBKeyboardFocusCoalition appendDescriptionToStream:];
-[SBKeyboardFocusCoalition suppressKeyboardFocusEvaluationForReason:];
-[SBKeyboardFocusCoalition members];
-[SBKeyboardFocusCoalition enforcedPolicy];
-[SBKeyboardFocusCoalition setEnforcedPolicy:];
-[SBKeyboardFocusCoalition internalMembers];
-[SBKeyboardFocusCoalition _initWithDebugName:];
-[SBKeyboardFocusCoalition _memberDidUpdatePreferences:];
-[SBKeyboardFocusCoalition _memberDidUpdateSettings:];
-[SBKeyboardFocusCoalition _registerMember:];
-[SBKeyboardFocusCoalition _unregisterMember:];
-[SBKeyboardFocusCoalition acquireMemberForWindowScene:delegate:];
-[SBKeyboardFocusCoalition addedMember:];
-[SBKeyboardFocusCoalition isKeyboardFocusEvaluationSuppressed];
-[SBKeyboardFocusCoalition keyboardFocusEvaluationSupressionReasons];
-[SBKeyboardFocusCoalition memberRequestsArbitration:forReason:];
-[SBKeyboardFocusCoalition policyEnforcer];
-[SBKeyboardFocusCoalition removedMember:];
-[SBKeyboardFocusCoalition setInternalMembers:];
-[SBKeyboardFocusCoalition setNeedsArbitrationForReason:];
-[SBKeyboardFocusCoalition setPolicyEnforcer:];
```
