# `TUCallContainer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 29 properties, 44 instance methods, 0 class methods

## Properties

```
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
```

## Instance methods

```
-[TUCallContainer screeningCall];
-[TUCallContainer incomingVideoCall];
-[TUCallContainer currentVideoCalls];
-[TUCallContainer callsWithStatus:];
-[TUCallContainer displayedCalls];
-[TUCallContainer displayedCallFromCalls:];
-[TUCallContainer callCountOnDefaultPairedDevice];
-[TUCallContainer hasCurrentVideoCalls];
-[TUCallContainer hasCurrentCalls];
-[TUCallContainer currentAudioAndVideoCallCount];
-[TUCallContainer countOfCallsPassingTest:];
-[TUCallContainer currentVideoCallCount];
-[TUCallContainer audioOrVideoCallWithStatus:];
-[TUCallContainer callPassingTest:];
-[TUCallContainer currentCallCount];
-[TUCallContainer hasCurrentAudioCalls];
-[TUCallContainer audioAndVideoCallsWithStatus:];
-[TUCallContainer displayedAudioAndVideoCalls];
-[TUCallContainer anyCallPassesTest:];
-[TUCallContainer callWithUniqueProxyIdentifier:];
-[TUCallContainer activeVideoCall];
-[TUCallContainer callWithCallUUID:];
-[TUCallContainer callsHostedOrAnEndpointElsewhere];
-[TUCallContainer conferenceParticipantCalls];
-[TUCallContainer incomingCall];
-[TUCallContainer currentCalls];
-[TUCallContainer allCallsAreOfService:];
-[TUCallContainer currentAudioAndVideoCalls];
-[TUCallContainer currentAudioAndVideoCallGroups];
-[TUCallContainer anyCallIsHostedOnCurrentDevice];
-[TUCallContainer callWithStatus:];
-[TUCallContainer callsWithGroupUUID:];
-[TUCallContainer currentCallGroups];
-[TUCallContainer videoCallWithStatus:];
-[TUCallContainer callsOnDefaultPairedDevice];
-[TUCallContainer callsWithAnEndpointElsewhere];
-[TUCallContainer callsPassingTest:];
-[TUCallContainer anyCallIsEndpointOnCurrentDevice];
-[TUCallContainer currentVideoCall];
-[TUCallContainer callsHostedElsewhere];
-[TUCallContainer allCallsPassTest:];
-[TUCallContainer incomingCalls];
-[TUCallContainer callGroupsOnDefaultPairedDevice];
-[TUCallContainer pendingUpgradeCall];
```
