# `SFSpeechSynthesisRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 15 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _isPrivate;
B _useCache;
B _returnFrontEndFeature;
q _type;
@"NSString" _text;
q _solutionType;
@"NSString" _locale;
@"NSString" _gender;
@"NSString" _voiceName;
@"NSString" _clientBundleIdentifier;
@"NSString" _requestIdentifer;
@"SFSpeechSynthesisVoice" _voice;
q _phoneSetType;
@"ProsodyTransferData" _prosodyTransferData;
@"NSString" _devServiceType;
```

## Properties

```
@property (T@"NSString",C,N,V_locale) locale;
@property (T@"NSString",C,N,V_gender) gender;
@property (T@"NSString",C,N,V_voiceName) voiceName;
@property (T@"NSString",C,N,V_clientBundleIdentifier) clientBundleIdentifier;
@property (T@"NSString",C,N,V_requestIdentifer) requestIdentifer;
@property (T@"SFSpeechSynthesisVoice",W,N,V_voice) voice;
@property (TB,N,V_useCache) useCache;
@property (TB,N,V_returnFrontEndFeature) returnFrontEndFeature;
@property (Tq,N,V_phoneSetType) phoneSetType;
@property (T@"ProsodyTransferData",&,N,V_prosodyTransferData) prosodyTransferData;
@property (T@"NSString",&,N,V_devServiceType) devServiceType;
@property (Tq,N,V_type) type;
@property (TB,N,V_isPrivate) isPrivate;
@property (T@"NSString",C,N,V_text) text;
@property (Tq,N,V_solutionType) solutionType;
```

## Instance methods

```
-[SFSpeechSynthesisRequest isPrivate];
-[SFSpeechSynthesisRequest text];
-[SFSpeechSynthesisRequest voice];
-[SFSpeechSynthesisRequest init];
-[SFSpeechSynthesisRequest setLocale:];
-[SFSpeechSynthesisRequest setClientBundleIdentifier:];
-[SFSpeechSynthesisRequest clientBundleIdentifier];
-[SFSpeechSynthesisRequest setUseCache:];
-[SFSpeechSynthesisRequest setType:];
-[SFSpeechSynthesisRequest locale];
-[SFSpeechSynthesisRequest type];
-[SFSpeechSynthesisRequest useCache];
-[SFSpeechSynthesisRequest setIsPrivate:];
-[SFSpeechSynthesisRequest setVoice:];
-[SFSpeechSynthesisRequest setGender:];
-[SFSpeechSynthesisRequest description];
-[SFSpeechSynthesisRequest setText:];
-[SFSpeechSynthesisRequest gender];
-[SFSpeechSynthesisRequest setVoiceName:];
-[SFSpeechSynthesisRequest voiceName];
-[SFSpeechSynthesisRequest setSolutionType:];
-[SFSpeechSynthesisRequest devServiceType];
-[SFSpeechSynthesisRequest phoneSetType];
-[SFSpeechSynthesisRequest prosodyTransferData];
-[SFSpeechSynthesisRequest requestIdentifer];
-[SFSpeechSynthesisRequest returnFrontEndFeature];
-[SFSpeechSynthesisRequest setDevServiceType:];
-[SFSpeechSynthesisRequest setPhoneSetType:];
-[SFSpeechSynthesisRequest setProsodyTransferData:];
-[SFSpeechSynthesisRequest setRequestIdentifer:];
-[SFSpeechSynthesisRequest setReturnFrontEndFeature:];
-[SFSpeechSynthesisRequest solutionType];
```
