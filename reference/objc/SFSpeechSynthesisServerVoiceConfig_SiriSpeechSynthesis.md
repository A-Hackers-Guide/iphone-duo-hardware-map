# `SFSpeechSynthesisServerVoiceConfig`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 1 class methods

## Instance variables

```
B _useBlazar;
B _enableAuthentication;
@"NSString" _ospreyEndpointUrl;
```

## Properties

```
@property (T@"NSString",R,N,V_ospreyEndpointUrl) ospreyEndpointUrl;
@property (TB,R,N,V_useBlazar) useBlazar;
@property (TB,R,N,V_enableAuthentication) enableAuthentication;
```

## Class methods

```
+[SFSpeechSynthesisServerVoiceConfig getTtsServerEndpointByCluster:withServiceType:];
```

## Instance methods

```
-[SFSpeechSynthesisServerVoiceConfig enableAuthentication];
-[SFSpeechSynthesisServerVoiceConfig initWithUrl:useBlazar:enableAuthentication:];
-[SFSpeechSynthesisServerVoiceConfig ospreyEndpointUrl];
-[SFSpeechSynthesisServerVoiceConfig useBlazar];
```
