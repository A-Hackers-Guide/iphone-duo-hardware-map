# `SFSSTTSEngineFactory`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _keyToTTSEngineMap;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_keyToTTSEngineMap) keyToTTSEngineMap;
```

## Class methods

```
+[SFSSTTSEngineFactory sharedInstance];
+[SFSSTTSEngineFactory getKeyByVoiceAsset:resourceAsset:];
```

## Instance methods

```
-[SFSSTTSEngineFactory init];
-[SFSSTTSEngineFactory getEngineByVoiceAsset:resourceAsset:];
-[SFSSTTSEngineFactory keyToTTSEngineMap];
-[SFSSTTSEngineFactory removeAllEngines];
-[SFSSTTSEngineFactory removeEngineByVoiceAsset:resourceAsset:];
-[SFSSTTSEngineFactory setKeyToTTSEngineMap:];
```
