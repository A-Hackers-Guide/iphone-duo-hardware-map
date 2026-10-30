# `AVMIDISysexEvent`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMusicEvent`
- 1 instance variables, 2 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSMutableData" _sysexData;
```

## Properties

```
@property (T^{MIDIRawData=I[1C]},R) rawData;
@property (TI,R) sizeInBytes;
```

## Instance methods

```
-[AVMIDISysexEvent sizeInBytes];
-[AVMIDISysexEvent rawData];
-[AVMIDISysexEvent initWithData:];
-[AVMIDISysexEvent initWithMIDIRawData:];
```
