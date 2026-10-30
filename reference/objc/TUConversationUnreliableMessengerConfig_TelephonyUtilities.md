# `TUConversationUnreliableMessengerConfig`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 17 instance methods, 2 class methods

## Instance variables

```
Q _establishChannelMaxAttempts;
Q _establishChannelRetryIntervalMillis;
Q _egressMessagePayloadMaxSizeBytes;
Q _channelStreamMaxQueueSize;
Q _channelStreamMaxTries;
Q _channelStreamRetryIntervalMillis;
Q _seqNumBufferSize;
@"NSData" _idsAliasingSalt;
```

## Properties

```
@property (TQ,R,N,V_establishChannelMaxAttempts) establishChannelMaxAttempts;
@property (TQ,R,N,V_establishChannelRetryIntervalMillis) establishChannelRetryIntervalMillis;
@property (TQ,R,N,V_egressMessagePayloadMaxSizeBytes) egressMessagePayloadMaxSizeBytes;
@property (TQ,R,N,V_channelStreamMaxQueueSize) channelStreamMaxQueueSize;
@property (TQ,R,N,V_channelStreamMaxTries) channelStreamMaxTries;
@property (TQ,R,N,V_channelStreamRetryIntervalMillis) channelStreamRetryIntervalMillis;
@property (TQ,R,N,V_seqNumBufferSize) seqNumBufferSize;
@property (T@"NSData",C,N,V_idsAliasingSalt) idsAliasingSalt;
```

## Class methods

```
+[TUConversationUnreliableMessengerConfig supportsSecureCoding];
+[TUConversationUnreliableMessengerConfig shared];
```

## Instance methods

```
-[TUConversationUnreliableMessengerConfig encodeWithCoder:];
-[TUConversationUnreliableMessengerConfig hash];
-[TUConversationUnreliableMessengerConfig description];
-[TUConversationUnreliableMessengerConfig initWithCoder:];
-[TUConversationUnreliableMessengerConfig copyWithZone:];
-[TUConversationUnreliableMessengerConfig isEqual:];
-[TUConversationUnreliableMessengerConfig idsAliasingSalt];
-[TUConversationUnreliableMessengerConfig channelStreamMaxQueueSize];
-[TUConversationUnreliableMessengerConfig channelStreamMaxTries];
-[TUConversationUnreliableMessengerConfig channelStreamRetryIntervalMillis];
-[TUConversationUnreliableMessengerConfig egressMessagePayloadMaxSizeBytes];
-[TUConversationUnreliableMessengerConfig establishChannelMaxAttempts];
-[TUConversationUnreliableMessengerConfig establishChannelRetryIntervalMillis];
-[TUConversationUnreliableMessengerConfig initWithEstablishChannelMaxAttempts:establishChannelRetryIntervalMillis:egressMessagePayloadMaxSizeBytes:channelStreamMaxQueueSize:channelStreamMaxTries:channelStreamRetryIntervalMillis:seqNumBufferSize:];
-[TUConversationUnreliableMessengerConfig isEqualToConversationUnreliableMessengerConfig:];
-[TUConversationUnreliableMessengerConfig seqNumBufferSize];
-[TUConversationUnreliableMessengerConfig setIdsAliasingSalt:];
```
