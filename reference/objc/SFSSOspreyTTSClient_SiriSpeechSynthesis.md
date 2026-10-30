# `SFSSOspreyTTSClient`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OspreyChannel`
- 3 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _useBlazar;
@"NSString" _carryClusterId;
@"NSString" _deviceId;
```

## Properties

```
@property (T@"NSString",&,N,V_deviceId) deviceId;
@property (TB,N,V_useBlazar) useBlazar;
@property (T@"NSString",&,N,V_carryClusterId) carryClusterId;
```

## Class methods

```
+[SFSSOspreyTTSClient sharedInstance];
```

## Instance methods

```
-[SFSSOspreyTTSClient prewarm];
-[SFSSOspreyTTSClient deviceId];
-[SFSSOspreyTTSClient init];
-[SFSSOspreyTTSClient initWithURL:];
-[SFSSOspreyTTSClient setDeviceId:];
-[SFSSOspreyTTSClient carryClusterId];
-[SFSSOspreyTTSClient initWithURL:useBlazar:enableAuthentication:];
-[SFSSOspreyTTSClient performCustomBidirectionalStreamingRequest:handler:completion:];
-[SFSSOspreyTTSClient setCarryClusterId:];
-[SFSSOspreyTTSClient setUseBlazar:];
-[SFSSOspreyTTSClient streamBlazarTTS:headers:beginHandler:chunkHandler:endHandler:completion:];
-[SFSSOspreyTTSClient streamNativeTTS:headers:beginHandler:chunkHandler:endHandler:completion:];
-[SFSSOspreyTTSClient streamTTS:headers:beginHandler:chunkHandler:endHandler:completion:];
-[SFSSOspreyTTSClient useBlazar];
```
