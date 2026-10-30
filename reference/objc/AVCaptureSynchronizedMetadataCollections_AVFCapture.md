# `AVCaptureSynchronizedMetadataCollections`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _time;
@"NSMutableSet" _handledMetadataObjectTypes;
@"NSMutableSet" _expectedMetadataObjectTypes;
@"NSMutableArray" _collections;
@"NSObject<OS_dispatch_source>" _emitTimer;
```

## Properties

```
@property (T{?=qiIq},R,V_time) time;
@property (TB,R) readyToEmit;
@property (T@"NSObject<OS_dispatch_source>",&) emitTimer;
@property (T@"NSArray",R,C) metadataCollections;
@property (T@"NSArray",R,C) metadataObjects;
@property (T@"NSMutableSet",R,C) metadataObjectTypes;
```

## Instance methods

```
-[AVCaptureSynchronizedMetadataCollections dealloc];
-[AVCaptureSynchronizedMetadataCollections metadataObjectTypes];
-[AVCaptureSynchronizedMetadataCollections time];
-[AVCaptureSynchronizedMetadataCollections metadataObjects];
-[AVCaptureSynchronizedMetadataCollections addCollections:];
-[AVCaptureSynchronizedMetadataCollections emitTimer];
-[AVCaptureSynchronizedMetadataCollections initWithMetadataCollections:expectedMetadataObjectTypes:];
-[AVCaptureSynchronizedMetadataCollections metadataCollections];
-[AVCaptureSynchronizedMetadataCollections readyToEmit];
-[AVCaptureSynchronizedMetadataCollections setEmitTimer:];
-[AVCaptureSynchronizedMetadataCollections skipMetadataObjectTypes:];
```
