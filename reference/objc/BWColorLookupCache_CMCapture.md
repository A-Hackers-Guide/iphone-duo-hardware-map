# `BWColorLookupCache`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _coreImageCacheIsolationQueue;
@"NSMutableDictionary" _coreImageTableCache;
```

## Class methods

```
+[BWColorLookupCache initialize];
```

## Instance methods

```
-[BWColorLookupCache init];
-[BWColorLookupCache dealloc];
-[BWColorLookupCache interpolatedColorLookupTableFromTable:toTable:fractionComplete:];
-[BWColorLookupCache blackColorLookupTable];
-[BWColorLookupCache colorLookupTablesForFilter:];
-[BWColorLookupCache fetchColorLookupTablesForFilter:];
-[BWColorLookupCache identityColorLookupTable];
-[BWColorLookupCache whiteColorLookupTable];
```
