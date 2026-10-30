# `FigAlternateObjCVideoAttributes`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigKVCInspectable`
- 6 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigAlternate=} _alternate;
@"NSArray" _videoCodecTypes;
@"NSArray" _videoLayoutAttributes;
^{OpaqueFigSimpleMutex=} _mutex;
d _nominalFrameRate;
{CGSize="width"d"height"d} _presentationSize;
```

## Properties

```
@property (T@"NSString",R,N) videoRange;
@property (T@"NSArray",R,N) codecTypes;
@property (T{CGSize=dd},R,N,V_presentationSize) presentationSize;
@property (Td,R,N) presentationWidth;
@property (Td,R,N) presentationHeight;
@property (Td,R,N,V_nominalFrameRate) nominalFrameRate;
@property (T@"NSArray",R,N) videoLayoutAttributes;
```

## Instance methods

```
-[FigAlternateObjCVideoAttributes nominalFrameRate];
-[FigAlternateObjCVideoAttributes dealloc];
-[FigAlternateObjCVideoAttributes presentationSize];
-[FigAlternateObjCVideoAttributes codecTypes];
-[FigAlternateObjCVideoAttributes initWithFigAlternate:];
-[FigAlternateObjCVideoAttributes videoLayoutAttributes];
-[FigAlternateObjCVideoAttributes videoRange];
-[FigAlternateObjCVideoAttributes presentationHeight];
-[FigAlternateObjCVideoAttributes presentationWidth];
```
