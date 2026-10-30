# `AVAudioChannelGroupSemantics`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
I _semantics;
I _terminalType;
I _channelCount;
@"AVAudioChannelLayout" _layout;
```

## Properties

```
@property (TI,N,V_channelCount) channelCount;
@property (TI,N,V_semantics) semantics;
@property (TI,N,V_terminalType) terminalType;
@property (T@"AVAudioChannelLayout",C,N,V_layout) layout;
```

## Class methods

```
+[AVAudioChannelGroupSemantics supportsSecureCoding];
```

## Instance methods

```
-[AVAudioChannelGroupSemantics channelCount];
-[AVAudioChannelGroupSemantics init];
-[AVAudioChannelGroupSemantics setChannelCount:];
-[AVAudioChannelGroupSemantics encodeWithCoder:];
-[AVAudioChannelGroupSemantics initWithCoder:];
-[AVAudioChannelGroupSemantics layout];
-[AVAudioChannelGroupSemantics setLayout:];
-[AVAudioChannelGroupSemantics createAudioChannelGroupSemantics];
-[AVAudioChannelGroupSemantics initWithAudioChannelGroupSemantics:];
-[AVAudioChannelGroupSemantics initWithChannelCount:semantics:terminalType:layout:];
-[AVAudioChannelGroupSemantics semantics];
-[AVAudioChannelGroupSemantics setSemantics:];
-[AVAudioChannelGroupSemantics setTerminalType:];
-[AVAudioChannelGroupSemantics terminalType];
```
