# `SNSpeechPacket`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SNSessionObject`, `SNThunking`
- 1 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"SNSpeechPacketInternal" _underlyingSpeechPacket;
```

## Properties

```
@property (T@"SNSpeechPacketInternal",&,N,V_underlyingSpeechPacket) underlyingSpeechPacket;
@property (T@"NSArray",&,N) packets;
@property (Tq,N) packetNumber;
@property (T@"NSString",C,N) aceId;
@property (T@"NSString",C,N) refId;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SNSpeechPacket packets];
-[SNSpeechPacket setPackets:];
-[SNSpeechPacket init];
-[SNSpeechPacket isProvisional];
-[SNSpeechPacket description];
-[SNSpeechPacket aceId];
-[SNSpeechPacket refId];
-[SNSpeechPacket setAceId:];
-[SNSpeechPacket setRefId:];
-[SNSpeechPacket packetNumber];
-[SNSpeechPacket setPacketNumber:];
-[SNSpeechPacket logDiagnostics];
-[SNSpeechPacket isRestartable];
-[SNSpeechPacket supportedByRemoteLimitedSession];
-[SNSpeechPacket bufferingAllowedDuringActiveSession];
-[SNSpeechPacket isRetryable];
-[SNSpeechPacket serializedAceDataError:];
-[SNSpeechPacket sessionRequestId];
-[SNSpeechPacket setSessionRequestId:];
-[SNSpeechPacket setUnderlyingSpeechPacket:];
-[SNSpeechPacket siriNetwork_invokeThunk];
-[SNSpeechPacket supportedByLocalSession];
-[SNSpeechPacket underlyingSpeechPacket];
```
