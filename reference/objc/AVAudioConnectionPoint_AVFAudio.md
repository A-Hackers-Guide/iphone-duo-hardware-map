# `AVAudioConnectionPoint`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"AVAudioNode" _node;
Q _bus;
^v _reserved;
```

## Properties

```
@property (T@"AVAudioNode",R,W,N,V_node) node;
@property (TQ,R,N,V_bus) bus;
```

## Class methods

```
+[AVAudioConnectionPoint connectionPointWithNode:bus:];
```

## Instance methods

```
-[AVAudioConnectionPoint init];
-[AVAudioConnectionPoint dealloc];
-[AVAudioConnectionPoint node];
-[AVAudioConnectionPoint hash];
-[AVAudioConnectionPoint isEqual:];
-[AVAudioConnectionPoint bus];
-[AVAudioConnectionPoint initWithNode:bus:];
```
