# `FigFlatToNSDictionaryWrapper`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSDictionary`
- 7 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigFlatDictionary=} _flatDictionary;
^{OpaqueFigFlatDictionaryKeySpec=} _keySpec;
i _keySpace;
^v _dictionaryBacking;
^v _exportedKeySpec;
@? _deallocatorBlock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lazyInitializationMutex;
```

## Instance methods

```
-[FigFlatToNSDictionaryWrapper keyEnumerator];
-[FigFlatToNSDictionaryWrapper dealloc];
-[FigFlatToNSDictionaryWrapper count];
-[FigFlatToNSDictionaryWrapper initWithObjects:forKeys:count:];
-[FigFlatToNSDictionaryWrapper objectForKey:];
-[FigFlatToNSDictionaryWrapper initWithFlatDictionary:keySpec:];
-[FigFlatToNSDictionaryWrapper initLazilyWithFlatDictionaryBacking:exportedKeySpec:deallocatorBlock:];
```
