# `SFSpeechSynthesisInternalSetting`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSUserDefaults" _defaults;
```

## Properties

```
@property (T@"NSUserDefaults",&,N,V_defaults) defaults;
@property (T@"NSString",R,N) ospreyEndpointURL;
@property (T@"NSString",R,N) deviceId;
@property (TB,R,N) disableCaching;
```

## Class methods

```
+[SFSpeechSynthesisInternalSetting sharedInstance];
```

## Instance methods

```
-[SFSpeechSynthesisInternalSetting setDefaults:];
-[SFSpeechSynthesisInternalSetting defaults];
-[SFSpeechSynthesisInternalSetting deviceId];
-[SFSpeechSynthesisInternalSetting init];
-[SFSpeechSynthesisInternalSetting disableCaching];
-[SFSpeechSynthesisInternalSetting ospreyEndpointURL];
-[SFSpeechSynthesisInternalSetting ospreyEndpointURLByType:];
```
