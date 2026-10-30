# `AVAudioFile`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<AVAudioFileImpl, std::default_delete<AVAudioFileImpl>>=""{?="__ptr_"^{AVAudioFileImpl}}} _impl;
```

## Properties

```
@property (TB,R,N) isOpen;
@property (T@"NSURL",R,N) url;
@property (T@"AVAudioFormat",R,N) fileFormat;
@property (T@"AVAudioFormat",R,N) processingFormat;
@property (Tq,R,N) length;
@property (Tq,N) framePosition;
```

## Instance methods

```
-[AVAudioFile close];
-[AVAudioFile init];
-[AVAudioFile dealloc];
-[AVAudioFile fileFormat];
-[AVAudioFile length];
-[AVAudioFile isOpen];
-[AVAudioFile url];
-[AVAudioFile initForReading:error:];
-[AVAudioFile initForWriting:settings:commonFormat:interleaved:error:];
-[AVAudioFile processingFormat];
-[AVAudioFile readIntoBuffer:error:];
-[AVAudioFile setFramePosition:];
-[AVAudioFile writeFromBuffer:error:];
-[AVAudioFile framePosition];
-[AVAudioFile initForReading:commonFormat:interleaved:error:];
-[AVAudioFile readIntoBuffer:frameCount:error:];
-[AVAudioFile initForReadingFromExtAudioFile:commonFormat:interleaved:error:];
-[AVAudioFile initForReadingFromExtAudioFile:error:];
-[AVAudioFile initForWriting:settings:error:];
-[AVAudioFile initSecondaryReader:format:error:];
```
