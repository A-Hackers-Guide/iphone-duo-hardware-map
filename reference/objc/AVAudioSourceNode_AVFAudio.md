# `AVAudioSourceNode`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioNode`
- Protocols: `AVAudioMixing`
- 0 instance variables, 5 properties, 4 instance methods, 2 class methods

## Properties

```
@property (Tf,D,N) volume;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVAudioSourceNode pullInputBlockFromRealtimeSafeRenderBlock:];
+[AVAudioSourceNode pullInputBlockFromRenderBlock:];
```

## Instance methods

```
-[AVAudioSourceNode initWithFormat:realtimeSafeRenderBlock:];
-[AVAudioSourceNode initWithFormat:renderBlock:];
-[AVAudioSourceNode initWithRealtimeSafeRenderBlock:];
-[AVAudioSourceNode initWithRenderBlock:];
```
