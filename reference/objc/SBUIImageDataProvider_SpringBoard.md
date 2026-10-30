# `SBUIImageDataProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `XBSnapshotDataProvider`
- 3 instance variables, 5 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"UIImage" _image;
@"XBSnapshotDataProviderContext" _context;
d _scaleFactor;
```

## Properties

```
@property (T@"XBSnapshotDataProviderContext",R,&,N,V_context) context;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUIImageDataProvider context];
-[SBUIImageDataProvider fetchImageForFormat:];
-[SBUIImageDataProvider initWithImage:context:scaleFactor:];
```
