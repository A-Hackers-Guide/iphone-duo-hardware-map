# `TUCallContainer`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUBargeCallContainer`, `TUCallContainer`
- 1 instance variables, 40 properties, 68 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _calls;
```

## Properties

```
@property (T@"NSArray",R,C) bargeCalls;
@property (T@"TUCall",R,N) frontmostBargeCall;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",C,N,V_calls) calls;
@property (T@"NSArray",R,C,N) currentCalls;
@property (T@"NSArray",R,C,N) currentVideoCalls;
@property (T@"NSArray",R,C,N) currentAudioAndVideoCalls;
@property (T@"NSArray",R,C,N) incomingCalls;
@property (T@"NSArray",R,C,N) displayedCalls;
@property (T@"NSArray",R,C,N) displayedAudioAndVideoCalls;
@property (T@"NSArray",R,C,N) conferenceParticipantCalls;
@property (T@"NSArray",R,C,N) callsHostedElsewhere;
@property (T@"NSArray",R,C,N) callsWithAnEndpointElsewhere;
@property (T@"NSArray",R,C,N) callsHostedOrAnEndpointElsewhere;
@property (T@"NSArray",R,C,N) callsOnDefaultPairedDevice;
@property (T@"TUCall",R,N) incomingCall;
@property (T@"TUCall",R,N) incomingVideoCall;
@property (T@"TUCall",R,N) activeVideoCall;
@property (T@"TUCall",R,N) currentVideoCall;
@property (T@"TUCall",R,N) screeningCall;
@property (T@"TUCall",R,N) pendingUpgradeCall;
@property (TQ,R,N) currentCallCount;
@property (TQ,R,N) currentVideoCallCount;
@property (TQ,R,N) currentAudioAndVideoCallCount;
@property (TQ,R,N) callCountOnDefaultPairedDevice;
@property (TB,R,N) hasCurrentCalls;
@property (TB,R,N) hasCurrentAudioCalls;
@property (TB,R,N) hasCurrentVideoCalls;
@property (TB,R,N) anyCallIsHostedOnCurrentDevice;
@property (TB,R,N) anyCallIsEndpointOnCurrentDevice;
@property (T@"NSArray",R,C,N) currentCallGroups;
@property (T@"NSArray",R,C,N) currentAudioAndVideoCallGroups;
@property (T@"NSArray",R,C,N) callGroupsOnDefaultPairedDevice;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUCallContainer screeningCall];
-[TUCallContainer incomingVideoCall];
-[TUCallContainer frontmostCall];
-[TUCallContainer currentVideoCalls];
-[TUCallContainer frontmostAudioOrVideoCall];
-[TUCallContainer callsWithStatus:];
-[TUCallContainer calls];
-[TUCallContainer bargeCalls];
-[TUCallContainer displayedCalls];
-[TUCallContainer bargeCallsPassingTest:];
-[TUCallContainer displayedCallFromCalls:];
-[TUCallContainer callCountOnDefaultPairedDevice];
-[TUCallContainer hasCurrentVideoCalls];
-[TUCallContainer hasCurrentCalls];
-[TUCallContainer currentAudioAndVideoCallCount];
-[TUCallContainer countOfCallsPassingTest:];
-[TUCallContainer init];
-[TUCallContainer currentVideoCallCount];
-[TUCallContainer conferenceCall];
-[TUCallContainer enumerateCallsInvokingBlock:forCallsPassingTest:];
-[TUCallContainer _callGroupsFromCalls:];
-[TUCallContainer _allCallsWithStatus:];
-[TUCallContainer existingCallsHaveMultipleProviders];
-[TUCallContainer audioOrVideoCallWithStatus:];
-[TUCallContainer callPassingTest:];
-[TUCallContainer currentCallCount];
-[TUCallContainer _allCalls];
-[TUCallContainer frontmostBargeCall];
-[TUCallContainer hasCurrentAudioCalls];
-[TUCallContainer audioAndVideoCallsWithStatus:];
-[TUCallContainer initWithCalls:];
-[TUCallContainer displayedAudioAndVideoCalls];
-[TUCallContainer bargeCallWithUniqueProxyIdentifier:];
-[TUCallContainer anyCallPassesTest:];
-[TUCallContainer callWithUniqueProxyIdentifier:];
-[TUCallContainer activeVideoCall];
-[TUCallContainer callWithCallUUID:];
-[TUCallContainer enumerateCallsWithOptions:invokingBlock:forCallsPassingTest:];
-[TUCallContainer callsHostedOrAnEndpointElsewhere];
-[TUCallContainer conferenceParticipantCalls];
-[TUCallContainer incomingCall];
-[TUCallContainer currentCalls];
-[TUCallContainer allCallsAreOfService:];
-[TUCallContainer currentAudioAndVideoCalls];
-[TUCallContainer currentAudioAndVideoCallGroups];
-[TUCallContainer enumerateBargeCallsInvokingBlock:forCallsPassingTest:];
-[TUCallContainer anyCallIsHostedOnCurrentDevice];
-[TUCallContainer callWithStatus:];
-[TUCallContainer setCalls:];
-[TUCallContainer callsWithGroupUUID:];
-[TUCallContainer resolvedIncomingCall];
-[TUCallContainer currentCallGroups];
-[TUCallContainer videoCallWithStatus:];
-[TUCallContainer displayedCall];
-[TUCallContainer callsOnDefaultPairedDevice];
-[TUCallContainer callsWithAnEndpointElsewhere];
-[TUCallContainer callsPassingTest:];
-[TUCallContainer anyCallIsEndpointOnCurrentDevice];
-[TUCallContainer currentVideoCall];
-[TUCallContainer callsHostedElsewhere];
-[TUCallContainer bargeCallWithStatus:];
-[TUCallContainer callPassingTest:sortedUsingComparator:];
-[TUCallContainer allCallsPassTest:];
-[TUCallContainer incomingCalls];
-[TUCallContainer callGroupsOnDefaultPairedDevice];
-[TUCallContainer callPassingTest:withOptions:];
-[TUCallContainer pendingUpgradeCall];
-[TUCallContainer featureFlags];
```
