# `AVCaptureSynchronizedDataCollection`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 1 instance variables, 1 properties, 9 instance methods, 4 class methods

## Instance variables

```
@"AVCaptureSynchronizedDataCollectionInternal" _internal;
```

## Properties

```
@property (TQ,R) count;
```

## Class methods

```
+[AVCaptureSynchronizedDataCollection initialize];
+[AVCaptureSynchronizedDataCollection _shortStringForMetadataObjects:];
+[AVCaptureSynchronizedDataCollection _shortStringForDataDroppedReason:];
+[AVCaptureSynchronizedDataCollection _shortStringForDataOutput:syncedData:];
```

## Instance methods

```
-[AVCaptureSynchronizedDataCollection debugDescription];
-[AVCaptureSynchronizedDataCollection dealloc];
-[AVCaptureSynchronizedDataCollection count];
-[AVCaptureSynchronizedDataCollection objectForKeyedSubscript:];
-[AVCaptureSynchronizedDataCollection countByEnumeratingWithState:objects:count:];
-[AVCaptureSynchronizedDataCollection description];
-[AVCaptureSynchronizedDataCollection _initWithPossibleDataOutputs:];
-[AVCaptureSynchronizedDataCollection _setSynchronizedData:forCaptureOutput:];
-[AVCaptureSynchronizedDataCollection synchronizedDataForCaptureOutput:];
```
