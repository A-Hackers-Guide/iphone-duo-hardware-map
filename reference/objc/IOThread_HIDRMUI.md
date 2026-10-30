# `IOThread`

- Image: [`/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`](../userland/System__Library__PrivateFrameworks__HIDRMUI.framework__HIDRMUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 1 properties, 5 instance methods, 4 class methods

## Properties

```
@property (T@"NSRunLoop",R,N) runLoop;
```

## Class methods

```
+[IOThread classCount];
+[IOThread decrementClassCount];
+[IOThread incrementClassCount];
+[IOThread initializeThread];
```

## Instance methods

```
-[IOThread init];
-[IOThread dispatchAsync:];
-[IOThread dealloc];
-[IOThread dispatchSync:];
-[IOThread runLoop];
```
