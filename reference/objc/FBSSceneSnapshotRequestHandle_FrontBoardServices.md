# `FBSSceneSnapshotRequestHandle`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
Q _type;
@"FBSSceneSnapshotContext" _context;
@"BSActionResponder" _responder;
B _canceled;
```

## Class methods

```
+[FBSSceneSnapshotRequestHandle handleForRequestType:context:];
```

## Instance methods

```
-[FBSSceneSnapshotRequestHandle initWithRequestType:context:];
-[FBSSceneSnapshotRequestHandle _clearAction];
-[FBSSceneSnapshotRequestHandle cancelRequest];
-[FBSSceneSnapshotRequestHandle performRequestForScene:];
```
