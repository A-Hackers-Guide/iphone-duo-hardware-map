# `AVLazyValueLoadingMetadataItem`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataItem`
- 1 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"AVLazyValueLoadingMetadataItemInternal" _lazyMetadataItem;
```

## Class methods

```
+[AVLazyValueLoadingMetadataItem metadataItemWithPropertiesOfMetadataItem:valueLoadingHandler:];
```

## Instance methods

```
-[AVLazyValueLoadingMetadataItem statusOfValueForKey:error:];
-[AVLazyValueLoadingMetadataItem dealloc];
-[AVLazyValueLoadingMetadataItem value];
-[AVLazyValueLoadingMetadataItem dataType];
-[AVLazyValueLoadingMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVLazyValueLoadingMetadataItem _initWithFigMetadataDictionary:valueLoadingHandler:];
-[AVLazyValueLoadingMetadataItem _valueForKeyDependsOnMetadataValue:];
-[AVLazyValueLoadingMetadataItem _valueRequestDidFinish];
-[AVLazyValueLoadingMetadataItem _valueStatus];
-[AVLazyValueLoadingMetadataItem _waitForLoadingOfValueDependentKey:];
```
