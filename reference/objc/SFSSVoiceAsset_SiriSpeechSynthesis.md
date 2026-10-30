# `SFSSVoiceAsset`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _assetPath;
@"NSString" _name;
@"NSString" _language;
q _gender;
q _footprint;
q _type;
q _contentVersion;
```

## Properties

```
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"NSString",R,C,N,V_language) language;
@property (Tq,R,N,V_gender) gender;
@property (Tq,R,N,V_footprint) footprint;
@property (Tq,R,N,V_type) type;
@property (Tq,R,N,V_contentVersion) contentVersion;
@property (T@"NSString",C,N,V_assetPath) assetPath;
```

## Class methods

```
+[SFSSVoiceAsset generateVoiceAssetFromVoiceKeyString:];
```

## Instance methods

```
-[SFSSVoiceAsset language];
-[SFSSVoiceAsset initWithPath:];
-[SFSSVoiceAsset contentVersion];
-[SFSSVoiceAsset footprint];
-[SFSSVoiceAsset type];
-[SFSSVoiceAsset name];
-[SFSSVoiceAsset gender];
-[SFSSVoiceAsset key];
-[SFSSVoiceAsset assetPath];
-[SFSSVoiceAsset setAssetPath:];
-[SFSSVoiceAsset init:gender:name:type:footprint:contentVersion:];
```
