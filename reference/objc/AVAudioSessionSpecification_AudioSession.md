# `AVAudioSessionSpecification`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 11 instance variables, 11 properties, 24 instance methods, 1 class methods

## Instance variables

```
B autoReconnect;
B overrideUseLegacyImpl;
I sourceSessionID;
I useCaseIdentifier;
Q sessionType;
@"NSString" clientIdentifier;
@"NSString" clientProcessName;
@"NSString" clientProcessBundleID;
@"<AVAudioSecureSessionProtocol>" publishingSession;
@"NSNumber" useNewMacOSImpl;
{?="val"[8I]} _sourceAuditToken;
```

## Properties

```
@property (TQ,N,VsessionType) sessionType;
@property (T{?=[8I]},N,V_sourceAuditToken) sourceAuditToken;
@property (TI,N,VsourceSessionID) sourceSessionID;
@property (T@"NSString",C,N,VclientIdentifier) clientIdentifier;
@property (T@"NSString",C,N,VclientProcessName) clientProcessName;
@property (T@"NSString",C,N,VclientProcessBundleID) clientProcessBundleID;
@property (TI,N,VuseCaseIdentifier) useCaseIdentifier;
@property (T@"<AVAudioSecureSessionProtocol>",W,N,VpublishingSession) publishingSession;
@property (TB,N,VautoReconnect) autoReconnect;
@property (TB,N,VoverrideUseLegacyImpl) overrideUseLegacyImpl;
@property (T@"NSNumber",&,N,VuseNewMacOSImpl) useNewMacOSImpl;
```

## Class methods

```
+[AVAudioSessionSpecification supportsSecureCoding];
```

## Instance methods

```
-[AVAudioSessionSpecification useCaseIdentifier];
-[AVAudioSessionSpecification clientIdentifier];
-[AVAudioSessionSpecification setPublishingSession:];
-[AVAudioSessionSpecification setUseCaseIdentifier:];
-[AVAudioSessionSpecification setClientProcessName:];
-[AVAudioSessionSpecification overrideUseLegacyImpl];
-[AVAudioSessionSpecification sourceSessionID];
-[AVAudioSessionSpecification setUseNewMacOSImpl:];
-[AVAudioSessionSpecification setSourceAuditToken:];
-[AVAudioSessionSpecification setClientIdentifier:];
-[AVAudioSessionSpecification clientProcessName];
-[AVAudioSessionSpecification sessionType];
-[AVAudioSessionSpecification useNewMacOSImpl];
-[AVAudioSessionSpecification autoReconnect];
-[AVAudioSessionSpecification encodeWithCoder:];
-[AVAudioSessionSpecification setClientProcessBundleID:];
-[AVAudioSessionSpecification setSourceSessionID:];
-[AVAudioSessionSpecification publishingSession];
-[AVAudioSessionSpecification clientProcessBundleID];
-[AVAudioSessionSpecification initWithCoder:];
-[AVAudioSessionSpecification setOverrideUseLegacyImpl:];
-[AVAudioSessionSpecification setAutoReconnect:];
-[AVAudioSessionSpecification sourceAuditToken];
-[AVAudioSessionSpecification setSessionType:];
```
