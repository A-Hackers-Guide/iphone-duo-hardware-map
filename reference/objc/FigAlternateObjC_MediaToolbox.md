# `FigAlternateObjC`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigKVCInspectable`
- 8 instance variables, 7 properties, 9 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigAlternate=} _alternate;
@"FigAlternateObjCVideoAttributes" _videoAttributes;
@"FigAlternateObjCAudioAttributes" _audioAttributes;
@"NSURL" _url;
@"NSString" _audioGroupID;
^{OpaqueFigSimpleMutex=} _mutex;
d _peakBitRate;
d _averageBitRate;
```

## Properties

```
@property (Td,R,N,V_peakBitRate) peakBitRate;
@property (Td,R,N,V_averageBitRate) averageBitRate;
@property (T@"NSURL",R,N,V_url) url;
@property (T@"NSString",R,N) audioGroupID;
@property (T@"FigAlternateObjCVideoAttributes",R,N) videoAttributes;
@property (T@"FigAlternateObjCAudioAttributes",R,N) audioAttributes;
@property (T^{OpaqueFigAlternate=},R,N,V_alternate) figAlternate;
```

## Class methods

```
+[FigAlternateObjC dummy];
```

## Instance methods

```
-[FigAlternateObjC dealloc];
-[FigAlternateObjC url];
-[FigAlternateObjC audioAttributes];
-[FigAlternateObjC videoAttributes];
-[FigAlternateObjC averageBitRate];
-[FigAlternateObjC figAlternate];
-[FigAlternateObjC initWithFigAlternate:];
-[FigAlternateObjC peakBitRate];
-[FigAlternateObjC audioGroupID];
```
