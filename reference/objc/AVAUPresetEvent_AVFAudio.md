# `AVAUPresetEvent`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMusicEvent`
- 1 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
{AUPresetEvent="scope"I"element"I"preset"^v} _event;
```

## Properties

```
@property (T^{AUPresetEvent=II^v},R) event;
@property (TI) scope;
@property (TI) element;
@property (T@"NSDictionary",R,C) presetDictionary;
```

## Instance methods

```
-[AVAUPresetEvent setElement:];
-[AVAUPresetEvent element];
-[AVAUPresetEvent scope];
-[AVAUPresetEvent dealloc];
-[AVAUPresetEvent event];
-[AVAUPresetEvent setScope:];
-[AVAUPresetEvent initWithAUPresetEvent:];
-[AVAUPresetEvent initWithScope:element:dictionary:];
-[AVAUPresetEvent presetDictionary];
```
