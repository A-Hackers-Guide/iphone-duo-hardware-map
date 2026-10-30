# `FigCaptureProcessHandle`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 7 properties, 16 instance methods, 3 class methods

## Instance variables

```
@"RBSProcessHandle" _rbsProcessHandle;
@"LSBundleRecord" _bundleRecord;
```

## Properties

```
@property (T@"RBSProcessHandle",R,N) rbsProcessHandle;
@property (T@"FigCaptureProcessHandle",R,N) nonRootSourceProcessHandleForVisibilityEndowment;
@property (Ti,R,N) pid;
@property (T{?=[8I]},R,N) auditToken;
@property (T@"NSString",R,N) bundleIdentifier;
@property (T@"NSString",R,N) extensionPointIdentifier;
@property (T@"NSString",R,N) extensionContainingAppBundleIdentifier;
```

## Class methods

```
+[FigCaptureProcessHandle initialize];
+[FigCaptureProcessHandle handleForAuditToken:error:];
+[FigCaptureProcessHandle handleForPID:error:];
```

## Instance methods

```
-[FigCaptureProcessHandle debugDescription];
-[FigCaptureProcessHandle dealloc];
-[FigCaptureProcessHandle extensionPointIdentifier];
-[FigCaptureProcessHandle bundleIdentifier];
-[FigCaptureProcessHandle pid];
-[FigCaptureProcessHandle description];
-[FigCaptureProcessHandle auditToken];
-[FigCaptureProcessHandle _ancestorPathWithinEndowmentTree:root:visitedLinks:];
-[FigCaptureProcessHandle _initWithAuditToken:error:];
-[FigCaptureProcessHandle _initWithPID:error:];
-[FigCaptureProcessHandle _initWithRBSProcessHandle:bundleRecord:];
-[FigCaptureProcessHandle _nonRootSourcePIDForVisibilityEndowmentWithTree:];
-[FigCaptureProcessHandle extensionContainingAppBundleIdentifier];
-[FigCaptureProcessHandle nonRootSourceProcessHandleForVisibilityEndowment];
-[FigCaptureProcessHandle rbsProcessHandle];
-[FigCaptureProcessHandle rbsProcessMonitorForEndowmentNamespace:serviceClass:updateHandler:];
```
