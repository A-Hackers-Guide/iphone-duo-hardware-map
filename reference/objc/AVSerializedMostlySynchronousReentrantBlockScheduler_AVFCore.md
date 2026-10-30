# `AVSerializedMostlySynchronousReentrantBlockScheduler`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVBlockScheduler`
- 3 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _ivarAccessLock;
@"NSArray" _blocks;
^{OpaqueFigReentrantMutex=} _blockSerializationLock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVSerializedMostlySynchronousReentrantBlockScheduler initialize];
```

## Instance methods

```
-[AVSerializedMostlySynchronousReentrantBlockScheduler init];
-[AVSerializedMostlySynchronousReentrantBlockScheduler dealloc];
-[AVSerializedMostlySynchronousReentrantBlockScheduler scheduleBlock:];
```
