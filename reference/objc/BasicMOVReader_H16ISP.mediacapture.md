# `BasicMOVReader`

- Image: [`/System/Library/MediaCapture/H16ISP.mediacapture`](../userland/System__Library__MediaCapture__H16ISP.mediacapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"AVAssetReader" _reader;
@"AVAssetReaderTrackOutput" _output;
B _hasReachedEndOfStream;
```

## Properties

```
@property (TB,R,V_hasReachedEndOfStream) hasReachedEndOfStream;
```

## Instance methods

```
-[BasicMOVReader initWithFileURL:error:];
-[BasicMOVReader getNextFrameTimestamp:error:];
-[BasicMOVReader hasReachedEndOfStream];
```
