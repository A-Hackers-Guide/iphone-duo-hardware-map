# `MTLResourceList`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{?="hashSize"I"hashShift"I"usedInfo"^Q"hopInfo"^I"hashTable"^Q"currentChunk"{MTLResourceListChunk="currentEntry"I"entries"^Q"nextChunk"^{MTLResourceListChunk}}"chunkEntryCapacity"I"pool"@"MTLResourceListPool""entry"{?="tqe_next"@"MTLResourceList""tqe_prev"^@}"time_added"Q} _listPriv;
[2048Q] _defaultHashTable;
[2048I] _defaultHopInfo;
[2048Q] _defaultUsedInfo;
```

## Instance methods

```
-[MTLResourceList dealloc];
-[MTLResourceList releaseAllObjectsAndReset];
-[MTLResourceList initWithCapacity:];
```
