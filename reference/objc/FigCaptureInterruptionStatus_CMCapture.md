# `FigCaptureInterruptionStatus`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
i _reason;
B _resolved;
B _systemWide;
@"<FigCaptureInterruptionDelegate>" _delegate;
@"NSObject" _context;
```

## Properties

```
@property (Ti,R,N,V_reason) reason;
@property (TB,R,N,V_resolved) resolved;
@property (TB,R,N,V_systemWide) systemWide;
@property (T@"<FigCaptureInterruptionDelegate>",W,N) delegate;
@property (T@"NSObject",R,N,V_context) context;
```

## Class methods

```
+[FigCaptureInterruptionStatus initialize];
```

## Instance methods

```
-[FigCaptureInterruptionStatus dealloc];
-[FigCaptureInterruptionStatus setDelegate:];
-[FigCaptureInterruptionStatus delegate];
-[FigCaptureInterruptionStatus description];
-[FigCaptureInterruptionStatus reason];
-[FigCaptureInterruptionStatus context];
-[FigCaptureInterruptionStatus resolve];
-[FigCaptureInterruptionStatus resolved];
-[FigCaptureInterruptionStatus initWithReason:systemWide:delegate:context:];
-[FigCaptureInterruptionStatus systemWide];
```
