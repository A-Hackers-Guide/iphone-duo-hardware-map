# `BWMotionDataTimeMachine`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _cache;
@"NSArray" _motionMetadataKeys;
@"NSArray" _sampleBufferAttachmentKeys;
Q _earliestAvailableMotionDataSerialNumber;
Q _latestAvailableMotionDataSerialNumber;
Q _capacity;
B _synchronizedSlaveMotionDataCachingEnabled;
B _cacheEntireMetadataDictionary;
^{OpaqueFigSimpleMutex=} _propertyMutex;
```

## Properties

```
@property (TB,R) synchronizedSlaveMotionDataCachingEnabled;
@property (TQ,R) earliestAvailableMotionDataSerialNumber;
@property (TQ,R) latestAvailableMotionDataSerialNumber;
```

## Class methods

```
+[BWMotionDataTimeMachine initialize];
```

## Instance methods

```
-[BWMotionDataTimeMachine dealloc];
-[BWMotionDataTimeMachine addMotionDataToCacheForSampleBuffer:];
-[BWMotionDataTimeMachine copyMotionDataForSerialNumber:];
-[BWMotionDataTimeMachine copyMotionDataForStartingSerialNumber:endingSerialNumber:];
-[BWMotionDataTimeMachine earliestAvailableMotionDataSerialNumber];
-[BWMotionDataTimeMachine initWithCapacity:synchronizedSlaveMotionDataCachingEnabled:cacheEntireMetadataDictionary:];
-[BWMotionDataTimeMachine latestAvailableMotionDataSerialNumber];
-[BWMotionDataTimeMachine synchronizedSlaveMotionDataCachingEnabled];
```
