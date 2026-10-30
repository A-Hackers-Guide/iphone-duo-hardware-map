# `PLTimeChunkInterval`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 5 properties, 17 instance methods, 4 class methods

## Instance variables

```
d _startTimestamp;
d _endTimestamp;
Q _chunkIndex;
```

## Properties

```
@property (Td,N,V_startTimestamp) startTimestamp;
@property (Td,N,V_endTimestamp) endTimestamp;
@property (TQ,N,V_chunkIndex) chunkIndex;
@property (Td,R,N) chunkDurationSeconds;
@property (T@"NSString",R,C,N) aggregationKey;
```

## Class methods

```
+[PLTimeChunkInterval supportsSecureCoding];
+[PLTimeChunkInterval chunksForTimeRangeStart:end:chunkDuration:];
+[PLTimeChunkInterval defaultChunksForEndTime:];
+[PLTimeChunkInterval intervalWithStartTimestamp:endTimestamp:chunkIndex:];
```

## Instance methods

```
-[PLTimeChunkInterval toDictionary];
-[PLTimeChunkInterval setStartTimestamp:];
-[PLTimeChunkInterval startTimestamp];
-[PLTimeChunkInterval encodeWithCoder:];
-[PLTimeChunkInterval hash];
-[PLTimeChunkInterval description];
-[PLTimeChunkInterval initWithCoder:];
-[PLTimeChunkInterval setEndTimestamp:];
-[PLTimeChunkInterval copyWithZone:];
-[PLTimeChunkInterval endTimestamp];
-[PLTimeChunkInterval isEqual:];
-[PLTimeChunkInterval chunkIndex];
-[PLTimeChunkInterval setChunkIndex:];
-[PLTimeChunkInterval aggregationKey];
-[PLTimeChunkInterval chunkDurationSeconds];
-[PLTimeChunkInterval initWithStartTimestamp:endTimestamp:chunkIndex:];
-[PLTimeChunkInterval toFilterableDictionary];
```
