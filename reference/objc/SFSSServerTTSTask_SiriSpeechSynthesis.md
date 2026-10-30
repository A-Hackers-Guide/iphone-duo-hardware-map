# `SFSSServerTTSTask`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SFSpeechSynthesisTask`
- 1 instance variables, 1 properties, 5 instance methods, 9 class methods

## Instance variables

```
@"SFSSOspreyTTSClient" _ospreyTTSClient;
```

## Properties

```
@property (T@"SFSSOspreyTTSClient",W,N,V_ospreyTTSClient) ospreyTTSClient;
```

## Class methods

```
+[SFSSServerTTSTask createOspreyRequestFromReqeust:];
+[SFSSServerTTSTask audioStreamBasicDescription:];
+[SFSSServerTTSTask convertPhoneSetTypeToServerPhoneSetType:];
+[SFSSServerTTSTask convertVoiceTypeToServerType:];
+[SFSSServerTTSTask createGrpcHeadersFromRequest:];
+[SFSSServerTTSTask flatPhonemeSequence:];
+[SFSSServerTTSTask generateProsodyTransferConfig:];
+[SFSSServerTTSTask generateResourceAssetFromResourceMetaInfo:];
+[SFSSServerTTSTask generateVoiceAssetFromVoiceMetaInfo:];
```

## Instance methods

```
-[SFSSServerTTSTask initWithRequest:];
-[SFSSServerTTSTask startTask:];
-[SFSSServerTTSTask cancelTask];
-[SFSSServerTTSTask ospreyTTSClient];
-[SFSSServerTTSTask setOspreyTTSClient:];
```
