# `MLWindowedBatchProvider`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLBatchProvider`
- 3 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<MLBatchProvider>" _fullBatch;
q _startIndex;
q _windowLength;
```

## Properties

```
@property (T@"<MLBatchProvider>",&,N,V_fullBatch) fullBatch;
@property (Tq,N,V_startIndex) startIndex;
@property (Tq,N,V_windowLength) windowLength;
@property (Tq,R,N) count;
```

## Instance methods

```
-[MLWindowedBatchProvider startIndex];
-[MLWindowedBatchProvider count];
-[MLWindowedBatchProvider setStartIndex:];
-[MLWindowedBatchProvider windowLength];
-[MLWindowedBatchProvider featuresAtIndex:];
-[MLWindowedBatchProvider fullBatch];
-[MLWindowedBatchProvider initWithBatch:startIndex:windowLength:error:];
-[MLWindowedBatchProvider setFullBatch:];
-[MLWindowedBatchProvider setWindowLength:];
```
