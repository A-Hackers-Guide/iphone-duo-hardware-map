# `AVAudioUnit`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioNode`
- 0 instance variables, 6 properties, 9 instance methods, 1 class methods

## Properties

```
@property (T{AudioComponentDescription=IIIII},R,N) audioComponentDescription;
@property (T^{OpaqueAudioComponentInstance=},R,N) audioUnit;
@property (T@"AUAudioUnit",R,D,N) AUAudioUnit;
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) manufacturerName;
@property (TQ,R,N) version;
```

## Class methods

```
+[AVAudioUnit instantiateWithComponentDescription:options:completionHandler:];
```

## Instance methods

```
-[AVAudioUnit version];
-[AVAudioUnit manufacturerName];
-[AVAudioUnit name];
-[AVAudioUnit audioUnit];
-[AVAudioUnit loadAudioUnitPresetAtURL:error:];
-[AVAudioUnit audioComponentDescription];
-[AVAudioUnit initWithAudioComponentDescription:];
-[AVAudioUnit setValue:forParam:];
-[AVAudioUnit valueForParam:];
```
