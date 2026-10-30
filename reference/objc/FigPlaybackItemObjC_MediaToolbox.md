# `FigPlaybackItemObjC`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigPlaybackItem=} _item;
^{OpaqueFigAsset=} _asset;
@"NSString" _url;
@"NSNumber" _pid;
@"NSString" _processName;
@"NSString" _loggingIdentifier;
^{OpaqueFigSimpleMutex=} _mutex;
```

## Properties

```
@property (T@"NSString",R,N,V_url) url;
@property (T@"NSNumber",R,N,V_pid) pid;
@property (T@"NSString",R,N,V_processName) processName;
@property (T@"NSString",R,N,V_loggingIdentifier) loggingIdentifier;
```

## Instance methods

```
-[FigPlaybackItemObjC loggingIdentifier];
-[FigPlaybackItemObjC dealloc];
-[FigPlaybackItemObjC pid];
-[FigPlaybackItemObjC processName];
-[FigPlaybackItemObjC url];
-[FigPlaybackItemObjC initWithFigPlaybackItem:pid:processName:loggingIdentifier:];
```
