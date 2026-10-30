# `CMFallStatsItemsIterator`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 5 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSData" _data;
@"NSDictionary" _item;
{Reader="fDelegate"^{Delegate}"fFd"i"fMappedSize"Q"fMappedOffset"Q"fMappedData"*"fMustScan"B"fZStream"{z_stream_s="next_in"*"avail_in"I"total_in"Q"next_out"*"avail_out"I"total_out"Q"msg"*"state"^{internal_state}"zalloc"^?"zfree"^?"opaque"^v"data_type"i"adler"Q"reserved"Q}"fUncompressedSens"{vector<unsigned char, std::allocator<unsigned char>>="__begin_"*"__end_"*""{?="__cap_"*}}"fSensRemaining"Q"fSensData"*} fMslReader;
{MemoryDelegate="_vptr$Delegate"^^?"fBuffer"*"fLength"Q} fMslReaderDelegate;
{ReaderIterator="fReader"^{Reader}"fItem"{shared_ptr<CMMsl::Item>="__ptr_"^{Item}"__cntrl_"^{__shared_weak_count}}} fMslIterator;
```

## Instance methods

```
-[CMFallStatsItemsIterator dealloc];
-[CMFallStatsItemsIterator countByEnumeratingWithState:objects:count:];
-[CMFallStatsItemsIterator initWithData:];
```
