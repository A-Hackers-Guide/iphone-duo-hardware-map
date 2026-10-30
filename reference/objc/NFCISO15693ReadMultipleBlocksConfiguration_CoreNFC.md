# `NFCISO15693ReadMultipleBlocksConfiguration`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCTagCommandConfiguration`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
C _flags;
Q _chunkSize;
{_NSRange="location"Q"length"Q} _range;
```

## Properties

```
@property (TC,N,V_flags) flags;
@property (T{_NSRange=QQ},N,V_range) range;
@property (TQ,N,V_chunkSize) chunkSize;
```

## Instance methods

```
-[NFCISO15693ReadMultipleBlocksConfiguration range];
-[NFCISO15693ReadMultipleBlocksConfiguration setFlags:];
-[NFCISO15693ReadMultipleBlocksConfiguration flags];
-[NFCISO15693ReadMultipleBlocksConfiguration setRange:];
-[NFCISO15693ReadMultipleBlocksConfiguration copyWithZone:];
-[NFCISO15693ReadMultipleBlocksConfiguration chunkSize];
-[NFCISO15693ReadMultipleBlocksConfiguration setChunkSize:];
-[NFCISO15693ReadMultipleBlocksConfiguration asNSDataArrayWithUID:error:];
-[NFCISO15693ReadMultipleBlocksConfiguration initWithRange:chunkSize:];
-[NFCISO15693ReadMultipleBlocksConfiguration initWithRange:chunkSize:maximumRetries:retryInterval:];
```
