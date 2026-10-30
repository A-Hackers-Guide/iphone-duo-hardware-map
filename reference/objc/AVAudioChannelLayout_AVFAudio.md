# `AVAudioChannelLayout`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 4 class methods

## Instance variables

```
I _layoutTag;
^{AudioChannelLayout=III[1{AudioChannelDescription=II[3f]}]} _layout;
^v _reserved;
```

## Properties

```
@property (TI,R,N) layoutTag;
@property (Tr^{AudioChannelLayout=III[1{AudioChannelDescription=II[3f]}]},R,N) layout;
@property (TI,R,N) channelCount;
```

## Class methods

```
+[AVAudioChannelLayout supportsSecureCoding];
+[AVAudioChannelLayout layoutWithLayout:];
+[AVAudioChannelLayout layoutWithLayoutTag:];
+[AVAudioChannelLayout layoutWithLayout:size:];
```

## Instance methods

```
-[AVAudioChannelLayout layoutTag];
-[AVAudioChannelLayout channelCount];
-[AVAudioChannelLayout layoutSize];
-[AVAudioChannelLayout init];
-[AVAudioChannelLayout dealloc];
-[AVAudioChannelLayout initWithLayout:];
-[AVAudioChannelLayout encodeWithCoder:];
-[AVAudioChannelLayout hash];
-[AVAudioChannelLayout initWithCoder:];
-[AVAudioChannelLayout layout];
-[AVAudioChannelLayout isEqual:];
-[AVAudioChannelLayout initWithLayoutTag:];
-[AVAudioChannelLayout initWithLayout:size:];
```
