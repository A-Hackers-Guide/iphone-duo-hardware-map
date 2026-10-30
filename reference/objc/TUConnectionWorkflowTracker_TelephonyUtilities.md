# `TUConnectionWorkflowTracker`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 12 properties, 34 instance methods, 3 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _instanceLock;
B _avcAddParticipantEnded;
B _audioSetupStarted;
B _audioSetupEnded;
B _connectingUIStarted;
B _connectingUIEnded;
B _calleeFullConnectionFlowEnded;
B _faceTimeCallerConnectionMetricsWorkflowBegan;
B _faceTimeInitiationDelayEnded;
B _remoteParticipantVideoDelayStarted;
B _remoteParticipantVideoDelayEnded;
@"NSUUID" _uuid;
Q _signpostID;
```

## Properties

```
@property (T@"NSUUID",&,N,V_uuid) uuid;
@property (TQ,N,V_signpostID) signpostID;
@property (TB,N,V_avcAddParticipantEnded) avcAddParticipantEnded;
@property (TB,N,V_audioSetupStarted) audioSetupStarted;
@property (TB,N,V_audioSetupEnded) audioSetupEnded;
@property (TB,N,V_connectingUIStarted) connectingUIStarted;
@property (TB,N,V_connectingUIEnded) connectingUIEnded;
@property (TB,N,V_calleeFullConnectionFlowEnded) calleeFullConnectionFlowEnded;
@property (TB,N,V_faceTimeCallerConnectionMetricsWorkflowBegan) faceTimeCallerConnectionMetricsWorkflowBegan;
@property (TB,N,V_faceTimeInitiationDelayEnded) faceTimeInitiationDelayEnded;
@property (TB,N,V_remoteParticipantVideoDelayStarted) remoteParticipantVideoDelayStarted;
@property (TB,N,V_remoteParticipantVideoDelayEnded) remoteParticipantVideoDelayEnded;
```

## Class methods

```
+[TUConnectionWorkflowTracker rekeySignpostControllerFromUUID:toConversationUUID:];
+[TUConnectionWorkflowTracker removeSignpostControllerForConversationUUID:];
+[TUConnectionWorkflowTracker signpostControllerForConversationUUID:];
```

## Instance methods

```
-[TUConnectionWorkflowTracker uuid];
-[TUConnectionWorkflowTracker initWithUUID:];
-[TUConnectionWorkflowTracker setUuid:];
-[TUConnectionWorkflowTracker setSignpostID:];
-[TUConnectionWorkflowTracker signpostID];
-[TUConnectionWorkflowTracker audioSetupEnded];
-[TUConnectionWorkflowTracker audioSetupSignpost:];
-[TUConnectionWorkflowTracker audioSetupStarted];
-[TUConnectionWorkflowTracker avcAddParticipantEnded];
-[TUConnectionWorkflowTracker avcAddParticipantSignpost:];
-[TUConnectionWorkflowTracker avcSessionCreationBlockSignpost:];
-[TUConnectionWorkflowTracker avcSessionStartSignpost:];
-[TUConnectionWorkflowTracker calleeFullConnectionFlowEnded];
-[TUConnectionWorkflowTracker calleeFullConnectionFlowSignpost:];
-[TUConnectionWorkflowTracker connectingUIEnded];
-[TUConnectionWorkflowTracker connectingUISignpost:];
-[TUConnectionWorkflowTracker connectingUIStarted];
-[TUConnectionWorkflowTracker faceTimeCallerConnectionMetricsWorkflowBegan];
-[TUConnectionWorkflowTracker faceTimeInitiationDelayEnded];
-[TUConnectionWorkflowTracker faceTimeInitiationDelaySignpost:];
-[TUConnectionWorkflowTracker idsSessionJoinSignpost:];
-[TUConnectionWorkflowTracker remoteParticipantVideoDelayEnded];
-[TUConnectionWorkflowTracker remoteParticipantVideoDelaySignpost:];
-[TUConnectionWorkflowTracker remoteParticipantVideoDelayStarted];
-[TUConnectionWorkflowTracker setAudioSetupEnded:];
-[TUConnectionWorkflowTracker setAudioSetupStarted:];
-[TUConnectionWorkflowTracker setAvcAddParticipantEnded:];
-[TUConnectionWorkflowTracker setCalleeFullConnectionFlowEnded:];
-[TUConnectionWorkflowTracker setConnectingUIEnded:];
-[TUConnectionWorkflowTracker setConnectingUIStarted:];
-[TUConnectionWorkflowTracker setFaceTimeCallerConnectionMetricsWorkflowBegan:];
-[TUConnectionWorkflowTracker setFaceTimeInitiationDelayEnded:];
-[TUConnectionWorkflowTracker setRemoteParticipantVideoDelayEnded:];
-[TUConnectionWorkflowTracker setRemoteParticipantVideoDelayStarted:];
```
