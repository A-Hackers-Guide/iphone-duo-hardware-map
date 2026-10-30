# `_FBSSnapshot`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"_FBSSnapshotContext" _context;
^{CGImage=} _imageRef;
@"IOSurface" _nonProtectedSurfaceRef;
@"IOSurface" _protectedSurfaceRef;
```

## Properties

```
@property (T@"_FBSSnapshotContext",R,C,N,V_context) context;
@property (TB,R,N) hasProtectedContent;
@property (T@"IOSurface",R,N) IOSurface;
@property (T@"IOSurface",R,N) fallbackIOSurface;
@property (T^{CGImage=},R,N) CGImage;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_FBSSnapshot CGImage];
-[_FBSSnapshot hasProtectedContent];
-[_FBSSnapshot dealloc];
-[_FBSSnapshot invalidate];
-[_FBSSnapshot initWithSnapshotContext:];
-[_FBSSnapshot _doInvalidate];
-[_FBSSnapshot _scale];
-[_FBSSnapshot _scaledSnapshotSize];
-[_FBSSnapshot _synchronizedCaptureWithCompletion:];
-[_FBSSnapshot context];
-[_FBSSnapshot IOSurface];
-[_FBSSnapshot fallbackIOSurface];
-[_FBSSnapshot capture];
```
