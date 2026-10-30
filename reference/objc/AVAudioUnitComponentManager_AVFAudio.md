# `AVAudioUnitComponentManager`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 9 instance methods, 3 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T@"NSArray",R,N) tagNames;
@property (T@"NSArray",R,N) standardLocalizedTagNames;
```

## Class methods

```
+[AVAudioUnitComponentManager allocWithZone:];
+[AVAudioUnitComponentManager sharedAudioUnitComponentManager];
+[AVAudioUnitComponentManager privateAllocInitSingleton];
```

## Instance methods

```
-[AVAudioUnitComponentManager init];
-[AVAudioUnitComponentManager copyWithZone:];
-[AVAudioUnitComponentManager tagNames];
-[AVAudioUnitComponentManager componentsMatchingDescription:];
-[AVAudioUnitComponentManager componentsMatchingPredicate:];
-[AVAudioUnitComponentManager componentsPassingTest:];
-[AVAudioUnitComponentManager localeChanged:];
-[AVAudioUnitComponentManager registrationsChanged:];
-[AVAudioUnitComponentManager standardLocalizedTagNames];
```
