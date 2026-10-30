# `MIDIEndpointWrapper`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _isSource;
I _endpointRef;
i _uniqueID;
@"NSString" _name;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
@property (TI,N,V_endpointRef) endpointRef;
@property (Ti,N,V_uniqueID) uniqueID;
@property (TB,N,V_isSource) isSource;
```

## Instance methods

```
-[MIDIEndpointWrapper uniqueID];
-[MIDIEndpointWrapper setName:];
-[MIDIEndpointWrapper setUniqueID:];
-[MIDIEndpointWrapper name];
-[MIDIEndpointWrapper isSource];
-[MIDIEndpointWrapper setIsSource:];
-[MIDIEndpointWrapper setEndpointRef:];
-[MIDIEndpointWrapper endpointRef];
-[MIDIEndpointWrapper initWithName:endpointRef:uniqueID:isSource:];
```
