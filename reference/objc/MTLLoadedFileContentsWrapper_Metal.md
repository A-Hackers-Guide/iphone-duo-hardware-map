# `MTLLoadedFileContentsWrapper`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSData" _sourceContents;
@"NSObject<OS_dispatch_data>" _dispatchData;
```

## Properties

```
@property (T@"NSData",R,N,V_sourceContents) sourceContents;
@property (T@"NSObject<OS_dispatch_data>",R,N,V_dispatchData) dispatchData;
@property (Tr^v,R,N) bytes;
@property (TQ,R,N) length;
```

## Instance methods

```
-[MTLLoadedFileContentsWrapper dealloc];
-[MTLLoadedFileContentsWrapper length];
-[MTLLoadedFileContentsWrapper dispatchData];
-[MTLLoadedFileContentsWrapper sourceContents];
-[MTLLoadedFileContentsWrapper initWithData:];
-[MTLLoadedFileContentsWrapper bytes];
```
