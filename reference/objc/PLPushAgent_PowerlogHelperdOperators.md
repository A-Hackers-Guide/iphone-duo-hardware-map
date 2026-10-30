# `PLPushAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 17 instance variables, 17 properties, 47 instance methods, 24 class methods

## Instance variables

```
B _hadRealWakeSinceSBC;
@"PLXPCListenerOperatorComposition" _receivedPushListener;
@"PLXPCListenerOperatorComposition" _sentPushListener;
@"PLXPCListenerOperatorComposition" _suppressedPushesListener;
@"PLXPCListenerOperatorComposition" _sentKeepAliveListener;
@"PLXPCListenerOperatorComposition" _receivedKeepAliveListener;
@"PLTimer" _runTimeAggregatorTimer;
Q _numKeepAlives;
@"PLXPCListenerOperatorComposition" _apsdConnectedListener;
@"NSMutableDictionary" _pushUsageDict;
@"NSDate" _detectionStartTime;
@"PLXPCListenerOperatorComposition" _messageSentListener;
@"PLXPCListenerOperatorComposition" _messageReceivedListener;
@"PLXPCListenerOperatorComposition" _pushProxyIncomingListener;
@"PLXPCListenerOperatorComposition" _pushProxyOutgoingListener;
@"NSDate" _lastNetworkWakeEventDate;
@"PLEntryNotificationOperatorComposition" _sbcNotification;
```

## Properties

```
@property (T@"PLXPCListenerOperatorComposition",&,V_receivedPushListener) receivedPushListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_sentPushListener) sentPushListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_suppressedPushesListener) suppressedPushesListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_sentKeepAliveListener) sentKeepAliveListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_receivedKeepAliveListener) receivedKeepAliveListener;
@property (T@"PLTimer",&,V_runTimeAggregatorTimer) runTimeAggregatorTimer;
@property (TQ,V_numKeepAlives) numKeepAlives;
@property (T@"PLXPCListenerOperatorComposition",&,V_apsdConnectedListener) apsdConnectedListener;
@property (T@"NSMutableDictionary",&,V_pushUsageDict) pushUsageDict;
@property (T@"NSDate",&,V_detectionStartTime) detectionStartTime;
@property (T@"PLXPCListenerOperatorComposition",&,V_messageSentListener) messageSentListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_messageReceivedListener) messageReceivedListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_pushProxyIncomingListener) pushProxyIncomingListener;
@property (T@"PLXPCListenerOperatorComposition",&,V_pushProxyOutgoingListener) pushProxyOutgoingListener;
@property (T@"NSDate",&,V_lastNetworkWakeEventDate) lastNetworkWakeEventDate;
@property (TB,V_hadRealWakeSinceSBC) hadRealWakeSinceSBC;
@property (T@"PLEntryNotificationOperatorComposition",&,V_sbcNotification) sbcNotification;
```

## Class methods

```
+[PLPushAgent entryEventPointDefinitions];
+[PLPushAgent entryEventForwardDefinitions];
+[PLPushAgent entryEventBackwardDefinitions];
+[PLPushAgent entryEventNoneDefinitions];
+[PLPushAgent load];
+[PLPushAgent defaults];
+[PLPushAgent entryAggregateDefinitions];
+[PLPushAgent bundleIdFromTopic:];
+[PLPushAgent entryAggregateDefinitionAPSDConnected];
+[PLPushAgent entryAggregateDefinitionSentKeepAlive];
+[PLPushAgent entryAggregateDefinitionSentPushes];
+[PLPushAgent entryAggregateDefinitionSuppressedPushes];
+[PLPushAgent entryEventPointDefinitionIncomingPushProxyMessages];
+[PLPushAgent entryEventPointDefinitionMessage];
+[PLPushAgent entryEventPointDefinitionMessageReceived];
+[PLPushAgent entryEventPointDefinitionMessageSent];
+[PLPushAgent entryEventPointDefinitionOutgoingPushProxyMessages];
+[PLPushAgent entryEventPointDefinitionsAPSDConnectedEvent];
+[PLPushAgent entryEventPointDefinitionsReceivedKeepAlive];
+[PLPushAgent entryEventPointDefinitionsReceivedPush];
+[PLPushAgent entryEventPointDefinitionsSentKeepAlive];
+[PLPushAgent entryEventPointDefinitionsSentPush];
+[PLPushAgent isHighPriorityPushEntry:];
+[PLPushAgent replaceConnectionTypeWithEnum:];
```

## Instance methods

```
-[PLPushAgent init];
-[PLPushAgent initOperatorDependancies];
-[PLPushAgent setRunTimeAggregatorTimer:];
-[PLPushAgent log];
-[PLPushAgent runTimeAggregatorTimer];
-[PLPushAgent handleMessageEvent:isSentEvent:];
-[PLPushAgent logEventPointReceivedKeepAlive:];
-[PLPushAgent sbcNotification];
-[PLPushAgent accountReceivedPushWithEntry:];
-[PLPushAgent apsdConnectedListener];
-[PLPushAgent checkPushUsage:withPLEntry:];
-[PLPushAgent convertMessageProtocol:];
-[PLPushAgent detectionStartTime];
-[PLPushAgent hadRealWakeSinceSBC];
-[PLPushAgent handleSBCForNetworkWake];
-[PLPushAgent lastNetworkWakeEventDate];
-[PLPushAgent logAggregateSentKeepAlive:];
-[PLPushAgent logAggregateSuppressedPushes:];
-[PLPushAgent logPushProxyMessages:forMessageType:];
-[PLPushAgent messageReceivedListener];
-[PLPushAgent messageSentListener];
-[PLPushAgent numKeepAlives];
-[PLPushAgent pushProxyIncomingListener];
-[PLPushAgent pushProxyOutgoingListener];
-[PLPushAgent pushUsageDict];
-[PLPushAgent receivedKeepAliveListener];
-[PLPushAgent receivedPushListener];
-[PLPushAgent sendEnergyIssueSignatureNotification:withThreshold:];
-[PLPushAgent sentKeepAliveListener];
-[PLPushAgent sentPushListener];
-[PLPushAgent setApsdConnectedListener:];
-[PLPushAgent setDetectionStartTime:];
-[PLPushAgent setHadRealWakeSinceSBC:];
-[PLPushAgent setLastNetworkWakeEventDate:];
-[PLPushAgent setMessageReceivedListener:];
-[PLPushAgent setMessageSentListener:];
-[PLPushAgent setNumKeepAlives:];
-[PLPushAgent setPushProxyIncomingListener:];
-[PLPushAgent setPushProxyOutgoingListener:];
-[PLPushAgent setPushUsageDict:];
-[PLPushAgent setReceivedKeepAliveListener:];
-[PLPushAgent setReceivedPushListener:];
-[PLPushAgent setSbcNotification:];
-[PLPushAgent setSentKeepAliveListener:];
-[PLPushAgent setSentPushListener:];
-[PLPushAgent setSuppressedPushesListener:];
-[PLPushAgent suppressedPushesListener];
```
