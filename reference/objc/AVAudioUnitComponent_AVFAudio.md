# `AVAudioUnitComponent`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 20 properties, 29 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) typeName;
@property (T@"NSString",R,N) localizedTypeName;
@property (T@"NSString",R,N) manufacturerName;
@property (TQ,R,N) version;
@property (T@"NSString",R,N) versionString;
@property (T@"NSURL",R,N) componentURL;
@property (T@"NSArray",R,N) availableArchitectures;
@property (TB,R,N,GisSandboxSafe) sandboxSafe;
@property (TB,R,N) hasMIDIInput;
@property (TB,R,N) hasMIDIOutput;
@property (T^{OpaqueAudioComponent=},R,N) audioComponent;
@property (T@"NSArray",C) userTagNames;
@property (T@"NSArray",R,N) allTagNames;
@property (T{AudioComponentDescription=IIIII},R,N) audioComponentDescription;
@property (T@"NSURL",R,N) iconURL;
@property (T@"UIImage",R,N) icon;
@property (TB,R,N) passesAUVal;
@property (TB,R,N) hasCustomView;
@property (T@"NSDictionary",R,N) configurationDictionary;
```

## Instance methods

```
-[AVAudioUnitComponent localeChanged];
-[AVAudioUnitComponent typeName];
-[AVAudioUnitComponent dealloc];
-[AVAudioUnitComponent version];
-[AVAudioUnitComponent versionString];
-[AVAudioUnitComponent manufacturerName];
-[AVAudioUnitComponent iconURL];
-[AVAudioUnitComponent configurationDictionary];
-[AVAudioUnitComponent name];
-[AVAudioUnitComponent icon];
-[AVAudioUnitComponent GetTypeName:];
-[AVAudioUnitComponent allTagNames];
-[AVAudioUnitComponent audioComponent];
-[AVAudioUnitComponent audioComponentDescription];
-[AVAudioUnitComponent availableArchitectures];
-[AVAudioUnitComponent componentURL];
-[AVAudioUnitComponent hasCustomView];
-[AVAudioUnitComponent hasMIDIInput];
-[AVAudioUnitComponent hasMIDIOutput];
-[AVAudioUnitComponent initWithComponentDescription:];
-[AVAudioUnitComponent initWithComponentDescription:withAVAUManagerImpl:];
-[AVAudioUnitComponent isComponentDescriptionMatch:];
-[AVAudioUnitComponent isSandboxSafe];
-[AVAudioUnitComponent localizedTypeName];
-[AVAudioUnitComponent passesAUVal];
-[AVAudioUnitComponent setUserTagNames:];
-[AVAudioUnitComponent supportsNumberInputChannels:outputChannels:];
-[AVAudioUnitComponent userTagNames];
-[AVAudioUnitComponent validateWithResults:inCompletionHandler:];
```
