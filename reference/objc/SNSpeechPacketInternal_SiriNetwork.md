# `SNSpeechPacketInternal`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SNThunking`
- 4 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
? internalAceId;
? internalRefId;
? packets;
q packetNumber;
```

## Properties

```
@property (T@"NSString",N,C) internalAceId;
@property (T@"NSString",N,C) internalRefId;
@property (T@"NSArray",N,C) packets;
@property (Tq,N,VpacketNumber) packetNumber;
```

## Instance methods

```
-[SNSpeechPacketInternal packets];
-[SNSpeechPacketInternal setPackets:];
-[SNSpeechPacketInternal init];
-[SNSpeechPacketInternal isProvisional];
-[SNSpeechPacketInternal packetNumber];
-[SNSpeechPacketInternal setPacketNumber:];
-[SNSpeechPacketInternal logDiagnostics];
-[SNSpeechPacketInternal isRestartable];
-[SNSpeechPacketInternal supportedByRemoteLimitedSession];
-[SNSpeechPacketInternal bufferingAllowedDuringActiveSession];
-[SNSpeechPacketInternal internalAceId];
-[SNSpeechPacketInternal internalRefId];
-[SNSpeechPacketInternal isRetryable];
-[SNSpeechPacketInternal serializedAceDataAndReturnError:];
-[SNSpeechPacketInternal sessionRequestId];
-[SNSpeechPacketInternal setInternalAceId:];
-[SNSpeechPacketInternal setInternalRefId:];
-[SNSpeechPacketInternal setSessionRequestId:];
-[SNSpeechPacketInternal siriNetwork_invokeThunk];
-[SNSpeechPacketInternal supportedByLocalSession];
```
