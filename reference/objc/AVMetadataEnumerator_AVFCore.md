# `AVMetadataEnumerator`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSEnumerator`
- 7 instance variables, 0 properties, 10 instance methods, 2 class methods

## Instance variables

```
^{OpaqueFigMetadataReader=} _reader;
@"NSEnumerator" _arrayEnumerator;
@ _key;
@"NSString" _keySpace;
@"NSLocale" _locale;
q _count;
q _index;
```

## Class methods

```
+[AVMetadataEnumerator metadataEnumeratorWithArray:key:keySpace:locale:];
+[AVMetadataEnumerator metadataEnumeratorWithMetadataReader:];
```

## Instance methods

```
-[AVMetadataEnumerator nextObject];
-[AVMetadataEnumerator dealloc];
-[AVMetadataEnumerator _setKey:];
-[AVMetadataEnumerator _setLocale:];
-[AVMetadataEnumerator _setArrayEnumerator:];
-[AVMetadataEnumerator _setKeySpace:];
-[AVMetadataEnumerator _setMetadataReader:];
-[AVMetadataEnumerator initWithArray:key:keySpace:locale:];
-[AVMetadataEnumerator initWithMetadataReader:];
-[AVMetadataEnumerator initWithMetadataReader:array:key:keySpace:locale:];
```
