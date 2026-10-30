# `SSRVoiceProfileModelContext`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _configFilePath;
@"NSURL" _voiceProfileModelFilePath;
@"NSURL" _secureProfileModelFilePath;
@"NSDictionary" _compareModelFilePaths;
```

## Properties

```
@property (T@"NSURL",R,N,V_configFilePath) configFilePath;
@property (T@"NSURL",R,N,V_voiceProfileModelFilePath) voiceProfileModelFilePath;
@property (T@"NSURL",R,N,V_secureProfileModelFilePath) secureProfileModelFilePath;
@property (T@"NSDictionary",R,N,V_compareModelFilePaths) compareModelFilePaths;
```

## Instance methods

```
-[SSRVoiceProfileModelContext initWithConfigFilePath:withModelPath:withCompareModelFilePaths:];
-[SSRVoiceProfileModelContext compareModelFilePaths];
-[SSRVoiceProfileModelContext configFilePath];
-[SSRVoiceProfileModelContext initWithConfigFilePath:withModelPath:withModelPathExclave:withCompareModelFilePaths:];
-[SSRVoiceProfileModelContext secureProfileModelFilePath];
-[SSRVoiceProfileModelContext voiceProfileModelFilePath];
```
