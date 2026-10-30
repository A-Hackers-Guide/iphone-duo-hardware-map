# `MTLLoadedFile`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSData" _fileData;
^v _parent;
q _modifiedTimeWhenCached;
{FileIdentifier="dev"i"ino"Q} _identity;
B _isCached;
```

## Properties

```
@property (T@"NSData",R,V_fileData) contents;
```

## Instance methods

```
-[MTLLoadedFile contents];
-[MTLLoadedFile initWithData:parent:];
-[MTLLoadedFile dealloc];
```
