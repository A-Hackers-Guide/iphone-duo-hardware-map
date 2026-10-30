# `FigCaptureTrie`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _complete;
@"NSMutableDictionary" _subTries;
```

## Properties

```
@property (TB,R,N,GisComplete) complete;
@property (T@"NSDictionary",R,N) children;
```

## Instance methods

```
-[FigCaptureTrie isComplete];
-[FigCaptureTrie initWithPath:];
-[FigCaptureTrie init];
-[FigCaptureTrie containsPath:];
-[FigCaptureTrie dealloc];
-[FigCaptureTrie children];
-[FigCaptureTrie description];
-[FigCaptureTrie copyWithZone:];
-[FigCaptureTrie isEqual:];
-[FigCaptureTrie addPath:];
-[FigCaptureTrie extractFrom:];
-[FigCaptureTrie enumeratePaths:];
-[FigCaptureTrie _addPath:index:];
-[FigCaptureTrie _enumeratePathsWithPrefix:stop:processLeaf:];
-[FigCaptureTrie _extractFrom:writeTarget:destinationMutability:overwrite:];
-[FigCaptureTrie containsParentPath:];
-[FigCaptureTrie extractFrom:writeInto:assumeMutable:overwrite:];
-[FigCaptureTrie generatePathArray];
-[FigCaptureTrie getSubTrie:];
-[FigCaptureTrie initWithPathArray:];
```
