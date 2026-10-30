# `VTPhraseDetectorConfig`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _useRecognizerCombination;
B _useKeywordSpotting;
@"NSString" _resourcePath;
@"NSString" _configPathNDAPI;
@"NSString" _configPathRecognizer;
@"NSArray" _phraseConfigs;
```

## Properties

```
@property (T@"NSString",R,N,V_resourcePath) resourcePath;
@property (T@"NSString",R,N,V_configPathNDAPI) configPathNDAPI;
@property (TB,R,N,V_useRecognizerCombination) useRecognizerCombination;
@property (T@"NSString",R,N,V_configPathRecognizer) configPathRecognizer;
@property (TB,R,N,V_useKeywordSpotting) useKeywordSpotting;
@property (T@"NSArray",R,N,V_phraseConfigs) phraseConfigs;
```

## Instance methods

```
-[VTPhraseDetectorConfig resourcePath];
-[VTPhraseDetectorConfig configPathNDAPI];
-[VTPhraseDetectorConfig configPathRecognizer];
-[VTPhraseDetectorConfig phraseConfigs];
-[VTPhraseDetectorConfig useKeywordSpotting];
-[VTPhraseDetectorConfig useRecognizerCombination];
-[VTPhraseDetectorConfig initWithResourcePath:configPathNDAPI:useRecognizerCombination:configPathRecognizer:useKeywordSpotting:phraseConfigs:];
```
