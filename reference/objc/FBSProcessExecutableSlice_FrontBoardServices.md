# `FBSProcessExecutableSlice`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 5 class methods

## Instance variables

```
i _type;
i _subtype;
```

## Properties

```
@property (Ti,R,N,V_type) type;
@property (Ti,R,N,V_subtype) subtype;
```

## Class methods

```
+[FBSProcessExecutableSlice initialize];
+[FBSProcessExecutableSlice arm64];
+[FBSProcessExecutableSlice arm64e];
+[FBSProcessExecutableSlice sliceWithType:];
+[FBSProcessExecutableSlice sliceWithType:subtype:];
```

## Instance methods

```
-[FBSProcessExecutableSlice subtype];
-[FBSProcessExecutableSlice type];
-[FBSProcessExecutableSlice description];
-[FBSProcessExecutableSlice membersForCoder];
```
